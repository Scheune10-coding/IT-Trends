# AWS-Anleitung: VPC + Subnetz + EC2(Ubuntu) + HTTP-Server

---

<details>
<summary><strong>Variante 1: Manuelle Erstellung (Schritt für Schritt)</strong></summary>

## 1. VPC erstellen (10.17.0.0/16)
1. AWS-Konsole öffnen → VPC → "Ihre VPCs"
2. Klick auf "VPC erstellen"
3. Wähle "nur VPC" aus
4. Einstellungen:
    - Name: `mein-vpc`
    - IPv4 CIDR: `10.17.0.0/16`
5. VPC erstellen

**Hinweis:**  
Das CIDR-Format legt den Adressbereich fest. Ein /16-Netz bietet 65.536 IP-Adressen.

---

## 2. Subnetz erstellen (öffentliches Subnetz)
1. In der VPC-Ansicht: Subnets → "Subnet erstellen"
2. Einstellungen:
    - VPC: die VPC, die du gerade erstellt hast
    - Availability Zone: z. B. eu-central-1a
    - IPv4 CIDR: z. B. 10.17.1.0/24
3. Subnet erstellen

---

## 3. Internet Gateway erstellen und zuweisen
1. Internet Gateways → "Internet Gateway erstellen"
    - Name: mein-igw
2. Gateway zu VPC hinzufügen → deine VPC auswählen
3. Internet Gateway anhängen

---

## 4. Routing für öffentliches Subnetz aktivieren
1. Route Tables → passende Routing-Tabelle auswählen (meist automatisch erstellt)
2. "Edit routes" → Neue Route hinzufügen:
    - Destination: 0.0.0.0/0
    - Target: Internet Gateway (IGW)
3. Unter "Subnet associations" → "Edit subnet associations"
4. Öffentliches Subnetz auswählen → speichern

---

## 5. EC2 Instanz (Ubuntu) starten
1. EC2 → "Launch Instance"
2. Einstellungen:
    - AMI: Ubuntu Server 22.04 LTS
    - Instance Type: t2.micro
3. Network:
    - VPC: deine VPC
    - Subnet: öffentliches Subnetz
    - Auto-assign Public IP: ENABLED
4. Security Group:
    - HTTP (Port 80) / Source: 0.0.0.0/0
    - SSH (Port 22) / Source: nur deine IP
5. "Launch Instance"

---

## 6. Mit EC2 verbinden
1. .pem-Datei herunterladen
2. Terminal öffnen
3. Verbindung herstellen:
    ```sh
    chmod 400 deinKey.pem
    ssh -i deinKey.pem ubuntu@<PUBLIC-IP-ADDRESS>
    ```

---

## 7. Webserver installieren und "Hallo Dienstag" anzeigen
1. Paketliste aktualisieren:
    ```sh
    sudo apt update
    ```
2. Apache Webserver installieren:
    ```sh
    sudo apt install apache2 -y
    ```
3. Apache starten & aktivieren:
    ```sh
    sudo systemctl enable apache2
    sudo systemctl start apache2
    ```
4. HTML Datei leeren und öffnen:
    ```sh
    sudo truncate -s 0 /var/www/html/index.html
    sudo nano /var/www/html/index.html
    ```
5. Beispiel-HTML einfügen und speichern:
    ```html
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>Hallo Dienstag</title>
    </head>
    <body>
        <h1>Hallo Dienstag</h1>
    </body>
    </html>
    ```
6. Apache neu laden:
    ```sh
    sudo systemctl reload apache2
    ```

---

## 8. Test im Browser
1. Browser öffnen
2. URL: `http://<PUBLIC-IP-ADDRESS>`
3. Erwartete Ausgabe: "Hallo Dienstag"

---

**Typische Fehlerquellen und Tipps:**
- Security Group erlaubt keinen HTTP/SSH-Zugriff → Regeln prüfen!
- Public IP fehlt → Instanz neu starten mit "Auto-assign Public IP: ENABLED"
- Routing-Tabelle nicht korrekt → Subnetzzuordnung prüfen
- Key Pair falsch → Instanz neu starten oder Key korrekt angeben

</details>

---

<details>
<summary><strong>Variante 2: Erstellung über den VPC Wizard ("VPC and more")</strong></summary>

## 1. VPC Wizard starten
1. AWS-Konsole → VPC → "Create VPC"
2. Wähle **"VPC and more"** Wizard

## 2. Einstellungen im Wizard
- Name: z. B. `mein-vpc`
- IPv4 CIDR: `10.17.0.0/16`
- Availability Zones: 1
- Number of public subnets: 1
- Number of private subnets: 0 (optional)
- NAT Gateway: None
- DNS Hostnames: Enabled

**Hinweis:**  
Der Wizard erstellt automatisch:
- VPC
- Öffentliches Subnetz
- Internet Gateway
- Routing Table mit Route ins Internet
- Security Group (anpassen!)

---

## 3. EC2 Instanz starten
1. EC2 → "Launch Instance"
2. Einstellungen wie oben (Ubuntu, t2.micro, Public Subnet, Auto-assign Public IP: ENABLED)
3. Security Group anpassen (HTTP/80 für alle, SSH/22 nur für eigene IP)
4. Instanz starten

---

## 4. Verbindung & Webserver wie oben

Folge ab Schritt 6 der manuellen Anleitung (SSH, Apache, HTML-Seite, Test).

---

**Vorteile Wizard:**  
- Spart Zeit, weniger Fehlerquellen
- Ressourcen werden automatisch verknüpft

**Hinweis:**  
Prüfe nach dem Wizard, ob Security Groups und Routing Table wie gewünscht konfiguriert sind!

</details>