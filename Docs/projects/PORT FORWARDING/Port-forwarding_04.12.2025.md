# **AWS VPC – Public & Private Subnet mit SSH-Portweiterleitung (8017 → 80)**

**Komplette Dokumentation zur Umsetzung der Aufgabe inkl. Routing, Security Groups und Port-Forwarding**

---

## **1. Ziel der Aufgabe**

In dieser Aufgabe wird eine VPC-Struktur aufgebaut, die aus folgenden Komponenten besteht:

* 1 VPC mit **10.10.0.0/16**
* 1 öffentliche Subnetze
* 2 private Subnetze
* 1 EC2-Instanz im **Public Subnet** (Bastion Host)
* 1 EC2-Instanz im **Private Subnet**
* Webserver auf der privaten Instanz (Port 80)
* SSH-Portweiterleitung:
  **Port 8017 auf der Public-Instance → Port 80 auf der Private-Instance**

Erreichbarkeit am Ende:

| Quelle → Ziel                                 | Ergebnis         |
| --------------------------------------------- | ---------------- |
| Internet → Public EC2                         | ✔ möglich        |
| Internet → Private EC2                        | ❌ nicht möglich  |
| Public EC2 → Private EC2                      | ✔ möglich        |
| Internet → Public-Port 8017 → Private-Port 80 | ✔ via SSH-Tunnel |

---

## **2. VPC erstellen**

Pfad: **VPC → Create VPC → „VPC and more“**

Einstellungen:

| Einstellung     | Wert                         |
| --------------- | ---------------------------- |
| IPv4 CIDR       | `10.10.0.0/16`               |
| Anzahl AZs      | 1                            |
| Public Subnets  | 1                            |
| Private Subnets | 2                            |
| NAT Gateway     | None                         |
| VPC endpoints   | None (Kosten einsparen)      |
| DNS Hostnames   | Enabled                      |
| DNS Resolution  | Enabled                      |

AWS erzeugt:

* 1 VPC
* 1 Public Subnet
* 2 Private Subnets
* Internet Gateway
* NAT Gateways
* Route Tables

---

### **2.1 Weiteres öffentliches Subnetz manuell erstellen & mit Route Table verknüpfen**

Da der Wizard bei nur einer AZ nur ein Public Subnet erzeugt, musst du ein weiteres öffentliches Subnetz für z. B. einen Bastion Host manuell anlegen und mit der öffentlichen Route Table verbinden.

#### **Schritt 1: Neues Public Subnet anlegen**

1. AWS-Konsole → **VPC** → **Subnets** → **Create subnet**
2. Wähle deine VPC aus.
3. **Subnet name:** z. B. `Public-Subnet-B`
4. **Availability Zone:** gleiche wie das erste Public Subnet (z. B. `eu-central-1a`)
5. **IPv4 CIDR block:** z. B. `10.10.2.0/24`
6. **Create subnet** klicken.

---

#### **Schritt 2: Subnetz mit öffentlicher Route Table verknüpfen**

1. AWS-Konsole → **VPC** → **Route Tables**
2. Die Route Table mit Ziel `0.0.0.0/0 → Internet Gateway` suchen (meist `Main` oder `Public-RT`).
3. Route Table auswählen → **Subnet Associations** → **Edit subnet associations**
4. Hake das neue Subnetz (`Public-Subnet-B`) an.
5. **Save associations** klicken.

---

Jetzt ist das neue Subnetz öffentlich und erhält automatisch Internetzugang über das Internet Gateway.

---

## **3. Subnet-CIDRs (Beispiel)**

| Subnet           | CIDR         | Zweck        |
| ---------------- | ------------ | ------------ |
| Public-Subnet-A  | 10.10.1.0/24 | Bastion Host |
| Public-Subnet-B  | 10.10.2.0/24 | Reserve      |
| Private-Subnet-A | 10.10.3.0/24 | Private EC2  |
| Private-Subnet-B | 10.10.4.0/24 | Reserve      |

---

## **4. Security Groups einrichten**

### **4.1 Public-SG (für Bastion Host)**

Inbound:

* SSH (22) → Anywhere
* TCP **8017** → Anywhere

Outbound:

* All traffic (default)

### **4.2 Private-SG**

Inbound:

* HTTP (80) → Source: **Public-SG**
* SSH (22) → Source: **Public-SG**

Outbound:

* All traffic (default)

Damit ist die private Instanz vollständig vor externem Zugriff geschützt.

---

## **5. EC2 Instanzen starten**

**Pfad:**  
EC2 → **Instance starten**

---

### 5.1 Öffentliche EC2 (Bastion Host)

1. **Name:** z. B. `BastionHost`
2. **AMI:** Ubuntu
3. **Key pair:** Deine `.pem` Datei
4. **Network settings:**
    - VPC: Deine erstellte VPC
    - Subnet: Öffentliches Subnet (z. B. `Public-Subnet-A` oder `Public-Subnet-B`)
    - Auto-Assign Public IP: **ENABLED**
    - Security Group: `Public-SG`
5. **Instance starten** klicken

**SSH Login von deinem Rechner:**
```sh
ssh -i WIA24.pem ubuntu@<PUBLIC-IP>
```

**Schlüsseldatei auf die Public-EC2 kopieren (für späteren Zugriff auf Private-EC2):**

Auf deinem Mac/PC (im Ordner, wo `.pem` liegt):
```sh
scp -i WIA24.pem WIA24.pem ubuntu@<PUBLIC-IP-DER-PUBLIC-EC2>:~/
```

Auf der Public-EC2:
```sh
chmod 400 WIA24.pem
ls -l WIA24.pem
```

---

### 5.2 Private EC2

1. **Name:** z. B. `PrivateWeb`
2. **AMI:** Ubuntu
3. **Key pair:** Deine `.pem` Datei
4. **Network settings:**
    - VPC: Deine erstellte VPC
    - Subnet: Privates Subnet (z. B. `Private-Subnet-A`)
    - Auto-Assign Public IP: **DISABLED**
    - Security Group: `Private-SG`
5. **Instance starten** klicken

**SSH Login (von der Public-EC2 aus):**
```sh
ssh -i WIA24.pem ubuntu@<PRIVATE-IP>
```

---

## **6. Webserver auf der privaten Instanz**

### Verzeichnis anlegen:

```bash
sudo mkdir -p /var/www/html
```

### Beispielseite erstellen:

```bash
echo '<h1>Hello from the private subnet</h1>' | sudo tee /var/www/html/index.html
```

### Webserver starten:

```bash
sudo python3 -m http.server 80 --directory /var/www/html
```

---

## **7. SSH-Portweiterleitung einrichten**

### Wichtig:

Der Tunnel muss **auf der Public Instance** laufen


### **Tunnel starten (auf der Public Instance)**

```bash
ssh -i WIA24.pem -L 0.0.0.0:8017:<PRIVATE-IP>:80 ubuntu@<PRIVATE-IP> -N
```


Der Prozess blockt die Shell → bedeutet: **Tunnel aktiv**
(nicht schließen!)

---

## **8. Zugriff aus dem Internet testen**

Von deinem Laptop:

```bash
curl http://<PUBLIC-IP>:8017
```

Oder im Browser:

```
http://<PUBLIC-IP>:8017
```

Sollte die Website aus `/var/www/html` der privaten Instanz anzeigen.

---

## **9. Funktionsübersicht**

| Funktion                                    | Ergebnis              |
| ------------------------------------------- | --------------------- |
| Internet → Public Instance:22               | ✔ SSH möglich         |
| Public Instance → Private Instance:22       | ✔ per Key             |
| Public Instance → Private Instance:80       | ✔ erreichbar          |
| Internet → PublicInstance:8017 → Private:80 | ✔ via SSH-Portforward |
| Internet → Private:80 direkt                | ❌ blockiert           |

---

## **10. Typische Fehler & Lösungen**

| Problem                                     | Ursache                               | Lösung                                        |
| ------------------------------------------- | ------------------------------------- | --------------------------------------------- |
| `connection refused` bei Port 8017          | Tunnel läuft nicht                    | Tunnelbefehl aktiv halten                     |
| Zeitüberschreitung beim Curl auf Private-IP | Security Group falsch                 | Private-SG muss Public-SG als Source erlauben |
| Tunnel meldet „Address already in use“      | alter SSH-Tunnel blockiert Port       | `sudo lsof -i:8017` und Prozess killen        |
| Browser zeigt nichts an                     | Webserver auf Private nicht gestartet | python-http-server prüfen                     |
| Fehler beim Start von `python3 -m http.server 80` | Port 80 bereits belegt               | Mit `sudo lsof -i:80` prüfen und Prozess beenden |


---

## **11. Abschluss**

Damit erfüllt die Umgebung alle Anforderungen:

* VPC mit public/private Trennung
* Bastion Host
* Private Webserverinstanz
* Portweiterleitung über SSH mit definierter Portnummer (8017 → 80)
* Zugriff von außen ausschließlich über definierte Wege

Wenn du willst, exportiere ich dir diese Dokumentation auch als **PDF, Markdown oder Word-Datei**.
