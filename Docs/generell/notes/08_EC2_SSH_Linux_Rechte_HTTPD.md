# EC2, SSH, Linux-Rechte, HTTPD (ausführlich)

## EC2 – Grundsetup (typisch)
- Instance starten:
  - Amazon Linux
  - t3.micro (klassischer Free-Tier-Typ)
- Key Pair:
  - RSA, .pem Datei
- Speicher:
  - z. B. gp3 (z. B. 16 GB)

Wichtig:
- Stoppen vs Terminate
  - Stop: VM aus, Volume bleibt (Kosten für Storage)
  - Terminate: Instance wird gelöscht (Daten weg, außer separat gesichert)

---

## SSH Verbindung
- Standard-User bei Amazon Linux: ec2-user
- Beispiel:
  - ssh -i "C:\Pfad\WI24.pem" ec2-user@ec2-<public-dns>

Wenn "Permission denied (publickey)":
- falscher User (z. B. ec2-user vs ubuntu)
- falscher Key
- Security Group Port 22 nicht offen
- Key-Rechte lokal falsch

---

## Rechte der .pem Datei (wichtig)
- Linux erwartet: Private Key darf nicht "zu offen" sein.
- Typischer Fix:
  - chmod 400 WI24.pem

Erklärung (Kurz):
- 400 = nur Owner darf lesen
- sonst verweigert SSH die Nutzung

---

## Linux Dateirechte (Grundlagen)
- u = user, g = group, o = others
- rwx = read/write/execute
- Oktal:
  - r=4, w=2, x=1
  - Beispiel: 7 = rwx

Beispiel:
- chmod 700 script.sh
  - Owner alles, andere nichts

---

## sudo
- "superuser do"
- führt Befehl mit Admin-Rechten aus

Beispiel:
- sudo yum install -y httpd
- -y überspringt Rückfragen

---

## HTTPD (Apache) installieren und starten
- Install:
  - sudo yum install -y httpd
- Start:
  - sudo systemctl start httpd
- Optional: Autostart:
  - sudo systemctl enable httpd

Test lokal:
- curl 127.0.0.1
- oder Browser mit Public IPv4 (wenn SG Port 80 offen)

---

## Minimal-Webseite setzen
- Beispiel:
  - echo "<html><body><h1>Hello</h1></body></html>" | sudo tee /var/www/html/index.html

Danach:
- curl 127.0.0.1
- Browser: http://<public-ip>

Typische Fehler
- SG Port 80 nicht offen
- Instance hat keine Public IP
- Route Table/IGW fehlt (VPC falsch)
