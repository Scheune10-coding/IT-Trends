# AWS VPC – Öffentliches & Privates Subnetz über „VPC and more“ Wizard

**Komplette Dokumentation inkl. typischer Fehlerquellen**

Diese Anleitung beschreibt die Erstellung einer vollständigen AWS-VPC-Umgebung über den **„VPC and more“** Wizard.  
Es werden automatisch folgende Ressourcen erzeugt:

- VPC
- Öffentliches Subnetz
- Privates Subnetz
- Route Tables
- Internet Gateway
- Security Groups
- EC2 Instanzen

Am Ende funktioniert:

| Zugriff                  | Ergebnis        |
|--------------------------|-----------------|
| Internet → Public EC2    | ✔ möglich       |
| Internet → Private EC2   | ❌ blockiert    |
| Public EC2 → Private EC2 | ✔ möglich       |

---

## 1. VPC erstellen (Wizard)

**Pfad:**  
VPC → *Create VPC* → Select **VPC and more**

**Einstellungen:**

| Einstellung               | Wert                             |
|---------------------------|----------------------------------|
| Name tag prefix           | `my-vpc-01`                      |
| IPv4 CIDR                 | `10.27.0.0/16`                   |
| Availability Zones        | **1** (für 1 Public + 1 Private) |
| Number of Public Subnets  | **1**                            |
| Number of Private Subnets | **1**                            |
| NAT Gateways              | **None**                         |
| VPC Endpoints             | **None**                         |
| DNS Hostnames             | Enabled                          |
| DNS Resolution            | Enabled                          |

**Einstellungen können je nach Aufgabenstellung variieren

---

## 2. Subnetze konfigurieren

-> **Costumize subnets CIDR blocks**

Setze die CIDR blocks auf:
- **Public Subnet:** `10.27.1.0/20`
- **Private Subnet:** `10.27.128.0/20`

**Ergebnis:**  
AWS erzeugt automatisch:

- `project-subnet-public1-us-east-1a`
- `project-subnet-private1-us-east-1a`

---

## 3. Routing – automatisch durch Wizard

## 4. Internet Gateway - automatisch durch Wizard 

[Genaue Erklärung zur manuellen Erstellung](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/VPC/VPC_18.11.2025.md)

---

## 5. Security Groups

Der Wizard erzeugt eine Default-SG, aber du brauchst eigene.
**Pfad:**  
VPC → *Security* → **Security groups** -> **Create security group**

### Public-SG (für Public EC2)

**Security Group name** -> Public-SG
**Description** -> Allow pulic acces to subnet
**VPC** -> my-vpc-01

**Inbound:**
- **Type** -> HTTP (80) | **Source** -> 0.0.0.0/0
- **Type** -> SSH  (22) | **Source** -> My IP

**Outbound:**
- Allow all (default)

### Private-SG (für Private EC2)

**Security Group name** -> Private-SG
**Description** -> Allow only intern acces to subnet
**VPC** -> my-vpc-01

- **Type** -> HTTP (80) | **Source** -> Public-SG
- **Type** -> SSH  (22) | **Source** -> Public-SG

**Outbound:**
- Allow all (default)

Damit ist die private Instanz nur intern erreichbar.

---

## 6. EC2 Instanzen starten

### Öffentliche EC2

- VPC: `my-vpc-01`
- Subnet: `project-subnet-public1`
- Auto-Assign Public IP: **ENABLED**
- SG: Public-SG

**SSH Login:**
```sh
ssh -i WIA24.pem ubuntu@<PUBLIC-IP>
```

### Private EC2

- VPC: `my-vpc-01`
- Subnet: `project-subnet-private1`
- Auto-Assign Public IP: **DISABLED**
- SG: Private-SG

**SSH Login über Public EC2:**
```sh
ssh -i WIA24.pem ubuntu@<PUBLIC-IP>
ssh ubuntu@10.0.2.X
```

---

## 7. HTML Webserver setzen

### Public EC2 – öffentlicher Webserver

```sh
sudo apt update
sudo apt install apache2 -y
sudo bash -c 'echo "<HTML>" > /var/www/html/index.html'
sudo systemctl reload apache2
```

**<HTML> Bsp.:**
```html
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Public Subnet</title>
    </head>
    <body>
        <h1>Hello public subnet</h1>
    </body>
    </html>
    ```

**Test:**
```
http://<PUBLIC-IP>
```

### Private EC2 – interner Webserver (kein Internet -> kein Apache)

```sh
sudo mkdir -p /var/www/html
sudo bash -c 'echo "<HTML>" > /var/www/html/index.html'
sudo python3 -m http.server 80 --directory /var/www/html
```

**<HTML> Bsp.:**
```html
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Private Subnet</title>
    </head>
    <body>
        <h1>Hello private subnet</h1>
    </body>
    </html>
    ```


**Test (von Public-EC2 aus):**
```sh
curl http://10.0.2.X
```

---

## 8. Funktionstests

- **Test 1 – Internet → Public:**  
  ✔ Muss funktionieren:  
  `http://<PUBLIC-IP>`

- **Test 2 – Internet → Private:**  
  ❌ Muss blockiert sein (Timeout)

- **Test 3 – Public → Private:**  
  ✔ Muss funktionieren:  
  `curl 10.0.2.X`

- **Test 4 – SSH Public → SSH Private:**  
  ✔ Muss funktionieren:  
  `ssh ubuntu@10.0.2.X`

---

## 9. Typische Fehlerquellen

**Fehler 1: Public-SG NICHT als Source in Private-SG**  
- Symptom: `curl 10.0.2.X` hängt.  
- Fix: Private-SG → Inbound → Source = **Public-SG**

**Fehler 2: Public/Private EC2 ist im falschen Subnet**  
- Symptom: Öffentliche EC2 hat keine Public-IP, Private EC2 ist aus Internet erreichbar  
- Fix: Public EC2 MUSS → public-subnet, Private EC2 MUSS → private-subnet

**Fehler 3: Routing vertauscht**  
- Symptom: Public EC2 hat kein Internet  
- Fix: Public-RTB muss Route haben: `0.0.0.0/0 → Internet Gateway`

**Fehler 4: Python Webserver läuft nicht mehr**  
- Passiert, wenn du den SSH-Tab schließt  
- Fix: Neu starten mit  
  `sudo python3 -m http.server 80 --directory /var/www/html`

**Fehler 5: Versucht, Private EC2 per RDP oder Public-IP zu erreichen**  
- Linux hat **kein RDP** und **keine Public IP**  
- Geht nur über SSH von der Public-EC2

