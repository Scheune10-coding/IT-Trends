# AWS VPC: Subnetze, Routing, Aufgaben + Lösungen (ausführlich)

## VPC erstellen (Modul 5 Setup)
Beispiel aus Aufgabenstellung:
- Name: wseeling
- IPv4 CIDR: 10.17.0.0/16
- IPv6: nein
- Availability Zones: 1
- VPC Endpoints: keine

---

## Subnetz erstellen (Public für HTTP)
- VPC auswählen
- Name: public-wseeling1
- IPv4 CIDR: 10.17.16.0/24 (Beispiel aus Notizen)

Warum /24?
- übersichtlich
- genug Hosts für eine kleine Übung

---

## Route Table + Internet Gateway (IGW)
### Internet Gateway
- stellt Verbindung zum Internet her
- muss an VPC angehängt sein

### Route Table
- enthält Regeln, wohin Traffic geroutet wird
- für Public Subnet:
  - Route 0.0.0.0/0 -> IGW

Schritte (Logik):
1) IGW existiert und ist an VPC attached
2) Route Table hat Default Route ins Internet
3) Route Table ist dem Public Subnet zugeordnet

Wenn einer der drei fehlt:
- keine Internet-Erreichbarkeit

---

## EC2 in der VPC starten (Public)
- Instance Name: seeling-linux3 (Beispiel)
- Amazon Linux
- Key Pair: WI24
- Network Settings:
  - VPC auswählen
  - Subnet auswählen
  - Auto-assign Public IP: aktivieren
- Security Group:
  - HTTP erlauben (Port 80)
  - Source: 0.0.0.0/0 (für "von außen" Zugriff)

---

## HTTPD installieren + testen
- ssh verbinden
- sudo yum install -y httpd
- echo "..." nach /var/www/html/index.html
- sudo systemctl start httpd
- curl 127.0.0.1
- Browser: http://<Public IPv4>

---

## Prüfungsaufgabe (klassisch): Public vs Private Zugriff
Aufgabe:
- Public Zugriff von außen soll möglich sein
- Private Zugriff von außen soll NICHT möglich sein
- Private Zugriff von innen soll möglich sein

### Typische Umsetzung
- Public Subnet:
  - Route 0.0.0.0/0 -> IGW
  - EC2 hat Public IP
  - SG erlaubt inbound 80/22 (je nach Aufgabe)
- Private Subnet:
  - KEINE Route zum IGW (oder nur über NAT, je nach Ziel)
  - EC2 hat nur Private IP
  - SG inbound NICHT offen von 0.0.0.0/0

Nachweis-Idee:
- Von deinem Rechner:
  - Browser/Curl erreicht Public EC2
  - Private EC2 NICHT erreichbar
- Von Public EC2 aus:
  - curl http://<private-ip> erreicht Private EC2 (wenn SG/Route passt)

---

## Beispiel Lösungsschema (aus Notizen, erweitert)
VPC: 10.27.0.0/16
- Public Subnet: 10.27.16.0/20
- Private Subnet: 10.27.32.0/20

Schritte:
1) VPC erstellen
2) Subnetze erstellen
3) Route Table für Public: Default Route zum IGW
4) EC2 Public: Public IP + SG HTTP von überall
5) EC2 Private: keine Public IP, SG erlaubt nur aus VPC/Subnet (z. B. 10.27.16.0/20)
6) Auf Private EC2:
   - httpd installieren
   - Testseite setzen
7) Von Public EC2:
   - curl http://<private-ip>
8) Screenshots/Nachweis:
   - Public von außen erreichbar
   - Private von außen nicht erreichbar
   - Private von innen erreichbar

---

## SSH-Hop in Private (Bastion-Pattern light)
Wenn Private keine Public IP hat:
- du loggst dich erst in Public (Bastion) ein
- von dort in Private (Port 22)

Praktischer Weg mit Key:
- scp key.pem auf Public:
  - scp -i WI24.pem WI24.pem ec2-user@<public-ip>:~/
- dann ssh von Public nach Private:
  - ssh -i "WI24.pem" ec2-user@<private-dns-oder-private-ip>

Wichtig:
- chmod 400 WI24.pem auch auf Public, sonst SSH meckert.

---

## Typische Fehlerliste (Klausurrettung)
- Kein Public IP an Public EC2 -> nicht erreichbar
- SG fehlt Port 80 -> Browser geht nicht
- Route Table nicht ans Subnet gebunden -> trotz IGW kein Internet
- Overlapping CIDR -> Subnetz lässt sich nicht erstellen
- Private SG zu offen -> Private ist plötzlich von außen erreichbar (Punktabzug)
