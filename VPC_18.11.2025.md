# AWS-Anleitung: VPC + Subnetz + EC2(Ubuntu) + HTTP-Server

---

#### Was ist eine AWS VPC?

Eine **Virtual Private Cloud (VPC)** ist ein isoliertes Netzwerk in der AWS-Cloud, das du selbst konfigurieren kannst. Es funktioniert wie ein eigenes Rechenzentrum, in dem du Subnetze, Routing, Firewalls und Internetzugänge nach deinen Anforderungen einrichtest.  
Mit einer VPC kannst du:
- Ressourcen (z. B. EC2-Instanzen, Datenbanken) sicher voneinander trennen
- Private und öffentliche Subnetze anlegen
- Netzwerkzugriffe und Datenströme kontrollieren
- VPN-Verbindungen zu deinem Unternehmensnetzwerk herstellen
- Sicherheitsgruppen und Netzwerk-ACLs für feingranulare Zugriffskontrolle nutzen

**Typische Komponenten einer VPC:**
- **Subnetze:** Teilbereiche des VPC-Netzes, z. B. für öffentliche und private Server
- **Internet Gateway:** Ermöglicht den Zugang zum Internet für Ressourcen im öffentlichen Subnetz
- **Route Tables:** Regeln, wie Datenpakete innerhalb der VPC und ins Internet geleitet werden
- **Security Groups & NACLs:** Firewall-Regeln für Instanzen und Subnetze
- **VPC Endpoints:** Direkte Verbindung zu AWS-Diensten ohne Internet

**Vorteile einer VPC:**
- Hohe Sicherheit und Isolation
- Flexible Netzwerkkonfiguration
- Skalierbarkeit und Integration mit anderen AWS-Diensten

---

## Wie berechnet man die Anzahl der Subnetze und Rechner (Hosts) in einer VPC?

### Beispiel:
- **VPC:** 10.17.0.0/16  
- **Subnetz:** 10.17.128.0/20

#### Schritt 1: Anzahl der möglichen Subnetze
Die VPC hat das Netz **10.17.0.0/16**.  
Das Subnetz hat **/20**.

- Ein /16-Netz hat 2^(32-16) = 65.536 IP-Adressen.
- Ein /20-Subnetz hat 2^(32-20) = 4.096 IP-Adressen.

**Wie viele /20-Subnetze passen in ein /16-Netz?**
- Unterschied der Präfixe: 20 - 16 = 4
- Anzahl der möglichen /20-Subnetze: 2^4 = **16 Subnetze**

#### Schritt 2: Anzahl der Hosts pro Subnetz
Ein /20-Subnetz hat 4.096 IP-Adressen.
- Davon sind 5 Adressen reserviert (Netzadresse, Broadcast, 3 für AWS intern).
- **Maximal nutzbare Hosts pro Subnetz:** 4.096 - 5 = **4.091 Rechner**

#### Zusammenfassung:
- In einer VPC mit 10.17.0.0/16 kannst du **16 Subnetze** mit jeweils /20 anlegen.
- Jedes /20-Subnetz bietet Platz für **4.091 EC2-Instanzen** (Rechner).

#### Formel:
- **Anzahl Subnetze:** 2^(Subnetz-Präfix - VPC-Präfix)
- **Anzahl Hosts pro Subnetz:** 2^(32-Subnetz-Präfix) - 5

---

## Beispielrechnung für andere Subnetzgrößen

| Subnetzgröße | Hosts pro Subnetz (2^(32-Präfix)-5) |
|--------------|-------------------------------------|
| /24          | 251                                 |
| /20          | 4.091                               |
| /16          | 65.531                              |

---

## Praxis: Subnetze sinnvoll planen
- Öffentliche Subnetze für Webserver, private Subnetze für Datenbanken
- Nicht zu große Subnetze wählen, um IP-Adressen effizient zu nutzen
- AWS reserviert immer 5 IPs pro Subnetz

---

## 1. VPC erstellen (10.17.0.0/16)
1. Gehe in der AWS-Konsole zu VPC → Ihre VPC's
2. Klick auf VPC erstellen
3. Wähle `nur VPC` aus
4. Einstellungen:
    - Name: `mein-vpc`
    - IPv4 CIDR: `10.17.0.0/16`
5. VPC erstellen

## 2. Subnetz erstellen (öffentliches Subnetz)
1. In der VPC-Ansicht: Subnets → Subnet erstellen
2. Einstellungen:
    - VPC: die VPC, die du gerade erstellt hast
    - Availability Zone: egal
    - IPv4 CIDR: z. B. 10.17.1.0/24
3. Subnet erstellen

## 3. Internet Gateway erstellen
1. Internet Gateways → Internet Gateway erstellen
    - Name: mein-igw
2. Gateway zu VPC hinzufügen → deine VPC auswählen

## 4. Routing für öffentliches Subnetz aktivieren
1. Route Tables → deine VPC finden
2. Routing-Tabelle auswählen → "Edit routes"
    - Neue Route:
    - Destination: 0.0.0.0/0
    - Target: Internet Gateway (IGW)
3. Unter "Subnet associations" → "Edit subnet associations"
4. Öffentliches Subnetz auswählen → speichern

## 5. EC2 Instanz (Ubuntu) starten
1. EC2 → Launch Instance
2. Einstellungen:
    - AMI: Ubuntu Server 22.04
    - Instance Type: t2.micro
3. Network:
    - VPC: deine VPC
    - Subnet: öffentliches Subnetz
    - Auto-assign Public IP: ENABLED
4. Security Group:
    - Regel 1: Type: HTTP (80) / Source: 0.0.0.0/0
    - Regel 2: Type: SSH (22) / Source: nur deine IP
5. Nach der Konfiguration → "Launch Instance"

## 6. Mit EC2 verbinden
1. Lade deine .pem-Datei herunter (falls noch nicht geschehen)
2. Terminal öffnen
3. Verbindung herstellen:
    - ssh -i deinKey.pem ubuntu@`<PUBLIC-IP-ADDRESS>`

## 7. Webserver installieren und "Hallo Dienstag" anzeigen
1. Paketliste aktualisieren:
```
sudo apt update
```
2. Apache Webserver installieren:
```
sudo apt install apache2 -y
```
3. Apache starten & aktivieren:
```
sudo systemctl enable apache2
sudo systemctl start apache2
```
4. HTML Datei leeren und öffnen:
```
sudo truncate -s 0 /var/www/html/index.html
sudo nano /var/www/html/index.html
```
5. Code in HTML Datei einfügen z.B.
```
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
6. Datei Speichern und Apache neu laden
    - CTRL + X
```
sudo systemctl reload apache2
```

## 8. Test im Browser
1. Browser öffnen
2. URL eingeben:
   http://`PUBLIC-IP-ADDRESS`
3. Erwartete Ausgabe:
   "Hallo Dienstag"
