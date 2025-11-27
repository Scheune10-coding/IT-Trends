# AWS-Anleitung: VPC + Subnetz + EC2(Ubuntu) + HTTP-Server

---

## 1. VPC erstellen (10.17.0.0/16)
1. AWS-Konsole öffnen → VPC → "Ihre VPCs"
2. Klick auf "VPC erstellen"
3. Wähle "nur VPC" aus
4. Einstellungen:
    - Name: `mein-vpc`
    - IPv4 CIDR: `10.17.0.0/16` (bietet Platz für viele Subnetze und Instanzen)
5. VPC erstellen

**Hinweis:**  
Das CIDR-Format legt den Adressbereich fest. Ein /16-Netz bietet 65.536 IP-Adressen.

---

## 2. Subnetz erstellen (öffentliches Subnetz)
1. In der VPC-Ansicht: Subnets → "Subnet erstellen"
2. Einstellungen:
    - VPC: die VPC, die du gerade erstellt hast
    - Availability Zone: z. B. eu-central-1a (für Ausfallsicherheit mehrere Zonen nutzen)
    - IPv4 CIDR: z. B. 10.17.1.0/24 (251 nutzbare IPs)
3. Subnet erstellen

**Tipp:**  
Öffentliche Subnetze sind für Server mit Internetzugriff, private Subnetze für interne Dienste.

---

## 3. Internet Gateway erstellen und zuweisen
1. Internet Gateways → "Internet Gateway erstellen"
    - Name: mein-igw
2. Gateway zu VPC hinzufügen → deine VPC auswählen
3. Internet Gateway anhängen

**Hinweis:**  
Ohne Internet Gateway ist kein Internetzugriff möglich.

---

## 4. Routing für öffentliches Subnetz aktivieren
1. Route Tables → passende Routing-Tabelle auswählen (meist automatisch erstellt)
2. "Edit routes" → Neue Route hinzufügen:
    - Destination: 0.0.0.0/0 (alle Ziele im Internet)
    - Target: Internet Gateway (IGW)
3. Unter "Subnet associations" → "Edit subnet associations"
4. Öffentliches Subnetz auswählen → speichern

**Tipp:**  
Prüfe, ob die Routing-Tabelle wirklich mit deinem Subnetz verknüpft ist.

---

## 5. EC2 Instanz (Ubuntu) starten
1. EC2 → "Launch Instance"
2. Einstellungen:
    - AMI: Ubuntu Server 22.04 LTS (aktuelle Version wählen)
    - Instance Type: t2.micro (kostenloses Kontingent, falls verfügbar)
3. Network:
    - VPC: deine VPC
    - Subnet: öffentliches Subnetz
    - Auto-assign Public IP: ENABLED (sonst kein Internetzugriff)
4. Security Group:
    - Regel 1: Type: HTTP (Port 80) / Source: 0.0.0.0/0 (für Webzugriff)
    - Regel 2: Type: SSH (Port 22) / Source: nur deine IP (z. B. 203.0.113.5/32)
5. Nach der Konfiguration → "Launch Instance"

**Hinweis:**  
Die Security Group ist die Firewall für deine Instanz. Öffne SSH nur für deine eigene IP!

---

## 6. Mit EC2 verbinden
1. Lade deine .pem-Datei herunter (Key Pair beim Start der Instanz auswählen oder neu erstellen)
2. Terminal öffnen
3. Verbindung herstellen:
    ```sh
    chmod 400 deinKey.pem  # Schlüsseldatei schützen
    ssh -i deinKey.pem ubuntu@<PUBLIC-IP-ADDRESS>
    ```

**Tipp:**  
Falls die Verbindung nicht klappt, prüfe Security Group, Key und Public IP.

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
5. Code in HTML Datei einfügen:
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
6. Datei speichern (CTRL + X, dann Y und Enter)
7. Apache neu laden:
    ```sh
    sudo systemctl reload apache2
    ```

---

## 8. Test im Browser
1. Browser öffnen
2. URL eingeben:
   ```
   http://<PUBLIC-IP-ADDRESS>
   ```
3. Erwartete Ausgabe:
   "Hallo Dienstag"

---

**Typische Fehlerquellen und Tipps:**
- Security Group erlaubt keinen HTTP/SSH-Zugriff → Regeln prüfen!
- Public IP fehlt → Instanz neu starten mit "Auto-assign Public IP: ENABLED"
- Routing-Tabelle nicht korrekt → Subnetzzuordnung prüfen
- Key Pair falsch → Instanz neu starten oder Key korrekt angeben

---

