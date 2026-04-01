# IT-Trends
## Allgemeine Infos:
- [Agile Methoden](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/Agile_Methoden.md)
- [Cloud Computing](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/Cloud_Computing.md)
- [Microservices](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/Microservices.md)
- [Mail Verschlüsselung](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/Mail_Verschluesselung_HTTPS.md)
- [AWS CLI](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/AWS_CLI.md)
- [AWS S3](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/AWS_S3.md)
- [AWS EC2](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/AWS_EC2.md)
- [AWS VPC](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/AWS_VPC.md)
- [Kostenmanagement und -berechnung](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/AWS_pricing.md)

## Dokumentationen zu Projekten:
- bedienen einer [REST API Schnittstelle mithilfe eines Python scripts](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/REST_API/REST_API_Schnittstelle_Python.md)

- erstellen einer [Öffentliche Datei in S3](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/S3/Global-S3_04.11.2025.md)
- erstellen eines [Sync-Skripts](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/S3/Sync-Skript_07.11.2025.md)
- erstellen eines [Download-Skripts](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/S3/Download-Skript_28.11.2025.md)

- erstellen eines [Linux Rechners](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/EC2/Linux-Rechner_07.11.2025.md)
- erstellen eines [Windows Rechners](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/EC2/WIN-Rechner_13.11.2025.md)
- erstellen einer [Linux Instanz mit HTTP Daemon](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/EC2/Linux-HTTP-Daemon_14.11.2025.md)

- erstellen einer [Virtual Private Cloud](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/VPC/VPC_18.11.2025.md)
- erstellen einer [VPC mit privaten und öffentlichen Subnet (Webseiten)](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/COMPLEX/VPC-complex_27.11.2025.md)
- erstellen einer [VPC mit SSH Port-Weiterleitung](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/projects/PORT%20FORWARDING/Port-forwarding_04.12.2025.md)

## Mitschriften / Zusammenfassungen (feat. Wiebke)
- [01 Themenübersicht und Scrum/Kanban](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/01_Themenuebersicht_und_Scrum_Kanban.md)
- [02 Agile Entwicklung, DevOps, CI/CD, MVP, Tools](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/02_Agile_DevOps_CI_CD_MVP_Tools.md)
- [03 Cloud Grundlagen und Edge](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/03_Cloud_Grundlagen_und_Edge.md)
- [04 Service-Modelle IaaS, PaaS, SaaS, FaaS](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/04_Service_Modelle_IaaS_PaaS_SaaS_FaaS.md)
- [05 Microservices, Architektur, REST](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/05_Microservices_Architektur_REST.md)
- [06 Security, Schutzziele, Krypto, HTTPS, Mail](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/06_Security_Schutzziele_Krypto_HTTPS_Mail.md)
- [07 AWS S3, IaC, CloudFormation, Lambda](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/07_AWS_S3_IaC_CloudFormation_Lambda.md)
- [08 EC2, SSH, Linux-Rechte, HTTPD](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/08_EC2_SSH_Linux_Rechte_HTTPD.md)
- [09 Networking, IPv4, CIDR, Subnetting, OSI](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/09_Networking_IPv4_CIDR_Subnetting_OSI.md)
- [10 AWS VPC, Subnetze, Routing, Prüfungsaufgaben](https://github.com/Scheune10-coding/IT-Trends/blob/main/Docs/generell/notes/10_AWS_VPC_Subnetze_Routing_Pruefungsaufgaben.md)

## Kontrollfragen
- [Lösung zu Kontrollfragen](https://github.com/Scheune10-coding/IT-Trends/blob/main/Kontrollfragen/Lösungen/IT-Trends_Kontrollfragen_Lösung.md)


# IT-Trends Klausur – Networking & AWS

### Vollständige Lösungsdokumentation

> **Hinweis:** Ersetze überall `IHREMATRIKELNUMMER` durch deine echte Matrikelnummer und `DEIN_NAME` durch deinen vollen Namen.

-----

## Inhaltsverzeichnis

- [Aufgabe 1 – S3-Upload-Skript](#aufgabe-1--s3-upload-skript)
- [Aufgabe 2 – EC2-Infrastruktur (manuelle AWS-Konsole)](#aufgabe-2--ec2-infrastruktur-manuelle-aws-konsole)
- [Aufgabe 3 – Architekturdiagramm](#aufgabe-3--architekturdiagramm)
- [Häufige Fehler & Lösungen](#häufige-fehler--lösungen)

-----

-----

# Aufgabe 1 – S3-Upload-Skript

## Konzept

**Ziel:** Dateien in den Bucket `clocowi24-IHREMATRIKELNUMMER` hochladen.

- **JPG-Dateien** → für alle weltweit öffentlich lesbar (über Bucket Policy)
- **Alle anderen Dateien** (z.B. PDF, .py) → privat, direkter URL-Aufruf gibt `AccessDenied`

**Warum Bucket Policy?**
AWS deaktiviert bei neuen Buckets seit 2023 Object-ACLs standardmäßig. Der korrekte Weg ist eine **Bucket Policy** mit `s3:GetObject` und `Principal: *` nur auf die JPG-Ressourcen. Dateien, die nicht in der Policy stehen, bleiben automatisch privat.

-----

## Voraussetzungen

```bash
# boto3 installieren
pip install boto3

# AWS Credentials konfigurieren (einmalig)
aws configure
# → AWS Access Key ID: DEIN_KEY
# → AWS Secret Access Key: DEIN_SECRET
# → Default region name: eu-central-1
# → Default output format: json
```

> Access Key & Secret findest du in der AWS Console unter:
> **IAM → Benutzer → Dein Benutzer → Sicherheitsanmeldeinformationen → Zugriffsschlüssel erstellen**

-----

## Das Skript: `s3_upload.py`

```python
import boto3
import sys
import os
import json

# ── Konfiguration ────────────────────────────────────────────
MATRIKELNUMMER = "IHREMATRIKELNUMMER"   # ← hier anpassen!
BUCKET_NAME    = f"clocowi24-{MATRIKELNUMMER}"
REGION         = "eu-central-1"
# ─────────────────────────────────────────────────────────────


def create_bucket(s3, bucket_name, region):
    """Erstellt den Bucket, falls er noch nicht existiert."""
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
        print(f"Bucket '{bucket_name}' erstellt.")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket '{bucket_name}' existiert bereits.")


def set_public_policy(s3, bucket_name, jpg_keys):
    """Setzt Bucket Policy: nur JPG-Dateien sind öffentlich lesbar."""
    if not jpg_keys:
        return

    resources = [f"arn:aws:s3:::{bucket_name}/{key}" for key in jpg_keys]

    # Block Public Access für Bucket Policy deaktivieren
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls":       True,
            "IgnorePublicAcls":      True,
            "BlockPublicPolicy":     False,  # muss False sein!
            "RestrictPublicBuckets": False,  # muss False sein!
        }
    )

    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicReadJPG",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": resources
        }]
    }
    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
    print(f"Bucket Policy gesetzt – {len(jpg_keys)} JPG(s) sind öffentlich.")


def upload_file(s3, bucket_name, filepath):
    """Lädt eine Datei hoch. Gibt den Dateinamen zurück."""
    filename = os.path.basename(filepath)
    is_jpg   = filename.lower().endswith((".jpg", ".jpeg"))
    extra    = {"ContentType": "image/jpeg"} if is_jpg else {}

    s3.upload_file(filepath, bucket_name, filename, ExtraArgs=extra)
    url = f"https://{bucket_name}.s3.{REGION}.amazonaws.com/{filename}"
    status = "ÖFFENTLICH" if is_jpg else "privat"
    print(f"[{status}] {filename}")
    print(f"  URL: {url}")
    return filename


def main():
    if len(sys.argv) < 2:
        print("Verwendung: python3 s3_upload.py <Datei1> [Datei2 ...]")
        sys.exit(1)

    s3 = boto3.client("s3", region_name=REGION)
    create_bucket(s3, BUCKET_NAME, REGION)

    jpg_keys = []
    for filepath in sys.argv[1:]:
        key = upload_file(s3, BUCKET_NAME, filepath)
        if key.lower().endswith((".jpg", ".jpeg")):
            jpg_keys.append(key)

    set_public_policy(s3, BUCKET_NAME, jpg_keys)


if __name__ == "__main__":
    main()
```

-----

## Aufgabe 1a – Skript hochladen

```bash
python3 s3_upload.py s3_upload.py
```

Das Skript lädt sich selbst hoch. Da `.py` kein JPG ist, bleibt die Datei privat.

-----

## Aufgabe 1b – Screenshot erstellen & in PDF konvertieren

1. Führe den Befehl aus Aufgabe 1a im Terminal aus
1. Mache einen Screenshot des Terminals mit dem erfolgreichen Aufruf
1. Speichere ihn als `Afg1_IHREMATRIKELNUMMER.jpg`
1. Konvertiere JPG → PDF:

```bash
# macOS (eingebaut, kein Extra-Tool nötig):
sips -s format pdf Afg1_IHREMATRIKELNUMMER.jpg --out Afg1_IHREMATRIKELNUMMER.pdf

# Linux (ImageMagick):
convert Afg1_IHREMATRIKELNUMMER.jpg Afg1_IHREMATRIKELNUMMER.pdf
```

-----

## Aufgabe 1c – JPG und PDF hochladen

```bash
python3 s3_upload.py Afg1_IHREMATRIKELNUMMER.jpg Afg1_IHREMATRIKELNUMMER.pdf
```

**Ergebnis:**

- `Afg1_IHREMATRIKELNUMMER.jpg` → in Bucket Policy eingetragen → **öffentlich**
- `Afg1_IHREMATRIKELNUMMER.pdf` → nicht in Policy → **privat (AccessDenied)**

-----

## Aufgabe 1d – Links im Backstage eintragen

Trage beide Links im Backstage ein. Das Schema ist:

```
https://clocowi24-IHREMATRIKELNUMMER.s3.eu-central-1.amazonaws.com/DATEINAME
```

|Datei                        |Erwartetes Ergebnis|
|-----------------------------|-------------------|
|`Afg1_IHREMATRIKELNUMMER.jpg`|Bild öffnet sich ✅ |
|`Afg1_IHREMATRIKELNUMMER.pdf`|`AccessDenied` ❌   |


> **Test:** Beide Links in einem privaten Browser-Fenster (Inkognito) öffnen, damit kein AWS-Login die Sichtbarkeit beeinflusst.

-----

-----

# Aufgabe 2 – EC2-Infrastruktur (manuelle AWS-Konsole)

## Gesamtübersicht

```
Internet
    │
    ▼
Internet Gateway (nkn-igw)
    │
    ▼
VPC: nkn (10.1.0.0/16)
├── Subnetz_public  (10.1.128.0/17)
│       └── nkn-pub  [Ubuntu, Apache2, öffentliche IP, Extra-EBS 8 GB]
│               SG: nkn-pub-sg  → TCP 22, TCP 80, ICMP von 0.0.0.0/0
│
└── Subnetz_private (10.1.0.0/17)
        └── nkn-priv  [Ubuntu, Python3-HTTP-Server, nur private IP]
                SG: nkn-priv-sg → TCP 22, TCP 80 nur von nkn-pub-sg
```

Von `nkn-pub` kann man per `curl http://<PRIVATE-IP>` den Webserver von `nkn-priv` abfragen.

-----

## Schritt 1 – VPC anlegen

1. AWS Console → Suchfeld oben: **VPC** eingeben → öffnen
1. Linke Seitenleiste: **Ihre VPCs** → rechts oben: **VPC erstellen**
1. Option **„Nur VPC”** auswählen *(nicht „VPC und mehr”)*
1. Felder ausfüllen:
   
   |Feld           |Wert         |
   |---------------|-------------|
   |Name-Tag       |`nkn`        |
   |IPv4-CIDR-Block|`10.1.0.0/16`|
   |IPv6-CIDR-Block|Kein IPv6    |
   |Mandant        |Standard     |
1. **VPC erstellen** klicken → Erfolgsmeldung abwarten

-----

## Schritt 2 – Subnetze anlegen

### Öffentliches Subnetz

1. Linke Seitenleiste: **Subnetze** → **Subnetz erstellen**
1. **VPC-ID:** `nkn` aus der Liste wählen
1. Unter **Subnetz-Einstellungen** ausfüllen:
   
   |Feld              |Wert            |
   |------------------|----------------|
   |Name des Subnetzes|`Subnetz_public`|
   |Availability Zone |`eu-central-1a` |
   |IPv4-CIDR-Block   |`10.1.128.0/17` |
1. **Subnetz erstellen** klicken
1. **Auto-Assign Public IP aktivieren** (wichtig – sonst bekommt die EC2 keine öffentliche IP!):
- Subnetz `Subnetz_public` in der Liste anklicken
- Oben: **Aktionen** → **Einstellungen für die automatische IP-Zuweisung bearbeiten**
- Häkchen bei **„IPv4-Adresse automatisch zuweisen aktivieren”** setzen
- **Speichern**

### Privates Subnetz

1. **Subnetz erstellen** (wie oben)
1. Felder ausfüllen:
   
   |Feld              |Wert             |
   |------------------|-----------------|
   |Name des Subnetzes|`Subnetz_private`|
   |Availability Zone |`eu-central-1a`  |
   |IPv4-CIDR-Block   |`10.1.0.0/17`    |
1. **Subnetz erstellen** klicken
1. **Kein** Auto-Assign Public IP – dieses Subnetz bleibt privat

-----

## Schritt 3 – Internet Gateway anlegen & anhängen

1. Linke Seitenleiste: **Internet-Gateways** → **Internet-Gateway erstellen**
1. **Name-Tag:** `nkn-igw`
1. **Internet-Gateway erstellen** klicken
1. Gateway mit VPC verbinden:
- `nkn-igw` in der Liste auswählen
- Oben: **Aktionen** → **An VPC anfügen**
- VPC `nkn` auswählen
- **Internet-Gateway anfügen** klicken

-----

## Schritt 4 – Route Table für das öffentliche Subnetz

Standardmäßig gibt es eine Main-Route-Table ohne Internetzugang. Wir erstellen eine eigene für das öffentliche Subnetz.

1. Linke Seitenleiste: **Routentabellen** → **Routentabelle erstellen**
1. Felder:
   
   |Feld|Wert           |
   |----|---------------|
   |Name|`nkn-rt-public`|
   |VPC |`nkn`          |
1. **Routentabelle erstellen** klicken
1. **Route zum Internet hinzufügen:**
- `nkn-rt-public` in der Liste auswählen
- Tab **Routen** → **Routen bearbeiten**
- **Route hinzufügen:**
  - Ziel: `0.0.0.0/0`
  - Ziel (Target): **Internet Gateway** → `nkn-igw` auswählen
- **Änderungen speichern**
1. **Subnetz zuordnen:**
- Tab **Subnetzzuordnungen** → **Subnetzzuordnungen bearbeiten**
- `Subnetz_public` anhaken
- **Zuordnungen speichern**

> Das private Subnetz bekommt **keine** Route zum Internet-Gateway – es bleibt intern.

-----

## Schritt 5 – Security Groups anlegen

### Security Group für nkn-pub (öffentlich)

1. Linke Seitenleiste: **Sicherheitsgruppen** → **Sicherheitsgruppe erstellen**
1. Grundeinstellungen:
   
   |Feld        |Wert                             |
   |------------|---------------------------------|
   |Name        |`nkn-pub-sg`                     |
   |Beschreibung|`SSH, HTTP und Ping von ueberall`|
   |VPC         |`nkn`                            |
1. **Eingehende Regeln** – drei Regeln hinzufügen (jeweils **Regel hinzufügen** klicken):
   
   |Typ             |Protokoll|Port|Quelle     |Beschreibung    |
   |----------------|---------|----|-----------|----------------|
   |SSH             |TCP      |22  |`0.0.0.0/0`|SSH von überall |
   |HTTP            |TCP      |80  |`0.0.0.0/0`|HTTP von überall|
   |Alle ICMP – IPv4|ICMP     |–   |`0.0.0.0/0`|Ping von überall|
1. **Ausgehende Regeln:** Standard belassen (Alles erlaubt)
1. **Sicherheitsgruppe erstellen** klicken

-----

### Security Group für nkn-priv (privat)

1. **Sicherheitsgruppe erstellen**
1. Grundeinstellungen:
   
   |Feld        |Wert                             |
   |------------|---------------------------------|
   |Name        |`nkn-priv-sg`                    |
   |Beschreibung|`SSH und HTTP nur von nkn-pub-sg`|
   |VPC         |`nkn`                            |
1. **Eingehende Regeln** – zwei Regeln hinzufügen:
   
   |Typ |Protokoll|Port|Quelle                               |
   |----|---------|----|-------------------------------------|
   |SSH |TCP      |22  |Security Group `nkn-pub-sg` auswählen|
   |HTTP|TCP      |80  |Security Group `nkn-pub-sg` auswählen|


> **Wichtig:** Bei „Quelle” keine IP-Adresse eingeben, sondern aus dem Dropdown die Security Group `nkn-pub-sg` wählen. So ist die private Instanz nur von der öffentlichen Instanz erreichbar.
1. **Ausgehende Regeln:** Standard belassen
1. **Sicherheitsgruppe erstellen** klicken

-----

## Schritt 6 – Key Pair anlegen

1. EC2 öffnen (Suchfeld: **EC2**)
1. Linke Seitenleiste: **Netzwerk und Sicherheit** → **Schlüsselpaare**
1. **Schlüsselpaar erstellen**
   
   |Feld            |Wert                |
   |----------------|--------------------|
   |Name            |`nkn-key`           |
   |Schlüsselpaartyp|RSA                 |
   |Dateiformat     |`.pem` (macOS/Linux)|
1. **Schlüsselpaar erstellen** → Datei `nkn-key.pem` wird automatisch heruntergeladen
1. Berechtigung setzen (im eigenen Terminal):
   
   ```bash
   chmod 400 nkn-key.pem
   ```

-----

## Schritt 7 – EC2-Instanz nkn-pub starten

1. EC2 → Linke Seitenleiste: **Instanzen** → **Instanz starten**
1. **Name:** `nkn-pub`
1. **AMI:**
- **Ubuntu** auswählen → Ubuntu Server 22.04 LTS (HVM), SSD Volume Type
- Architektur: `64-Bit (x86)`
1. **Instanztyp:** `t2.micro`
1. **Schlüsselpaar:** `nkn-key` auswählen
1. **Netzwerkeinstellungen** → **Bearbeiten** klicken:
   
   |Feld                               |Wert                                  |
   |-----------------------------------|--------------------------------------|
   |VPC                                |`nkn`                                 |
   |Subnetz                            |`Subnetz_public`                      |
   |Öffentliche IP automatisch zuweisen|**Aktivieren**                        |
   |Firewall (Sicherheitsgruppen)      |Bestehende Sicherheitsgruppe auswählen|
   |Sicherheitsgruppe                  |`nkn-pub-sg`                          |
1. **Speicher konfigurieren:**
- Root-Volume bleibt wie es ist (8 GiB gp3)
- Klicke auf **„Neues Volume hinzufügen”** für die zusätzliche Festplatte:
   
   |Feld                |Wert      |
   |--------------------|----------|
   |Größe               |`8` GiB   |
   |Volume-Typ          |`gp3`     |
   |Gerätename          |`/dev/sdb`|
   |Beim Beenden löschen|Ja        |
1. **Instanz starten** klicken → Status wird erst `pending`, dann `running`

-----

## Schritt 8 – EC2-Instanz nkn-priv starten

1. EC2 → **Instanz starten**
1. **Name:** `nkn-priv`
1. **AMI:** Ubuntu Server 22.04 LTS (gleich wie oben)
1. **Instanztyp:** `t2.micro`
1. **Schlüsselpaar:** `nkn-key`
1. **Netzwerkeinstellungen** → **Bearbeiten**:
   
   |Feld                               |Wert                                  |
   |-----------------------------------|--------------------------------------|
   |VPC                                |`nkn`                                 |
   |Subnetz                            |`Subnetz_private`                     |
   |Öffentliche IP automatisch zuweisen|**Deaktivieren**                      |
   |Firewall (Sicherheitsgruppen)      |Bestehende Sicherheitsgruppe auswählen|
   |Sicherheitsgruppe                  |`nkn-priv-sg`                         |
1. **Speicher:** Standard belassen (keine extra Festplatte)
1. **Instanz starten**

-----

## Schritt 9 – Webserver auf nkn-pub einrichten (Apache2)

### SSH-Verbindung herstellen

Die öffentliche IP von `nkn-pub` findest du in der EC2-Konsole:
**Instanzen** → `nkn-pub` → **Öffentliche IPv4-Adresse** (Spalte oder Details-Panel)

```bash
ssh -i nkn-key.pem ubuntu@<ÖFFENTLICHE-IP-VON-NKN-PUB>
```

### Apache2 installieren und konfigurieren

```bash
sudo apt update
sudo apt install apache2 -y
sudo systemctl enable apache2
sudo systemctl start apache2
```

### index.html mit dem geforderten Text erstellen

```bash
sudo truncate -s 0 /var/www/html/index.html
sudo nano /var/www/html/index.html
```

Folgenden Inhalt einfügen *(Name und Matrikelnummer anpassen!)*:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>nkn-pub</title>
</head>
<body>
    <h1>Hello PUBLIC, mein Name ist DEIN_NAME, meine Matrikel-Nummer ist IHREMATRIKELNUMMER</h1>
</body>
</html>
```

Speichern: **CTRL + X** → **Y** → **Enter**

```bash
sudo systemctl reload apache2
```

**Test im Browser:** `http://<ÖFFENTLICHE-IP-VON-NKN-PUB>` → der Text muss erscheinen *(Screenshot 2)*

-----

## Schritt 10 – Webserver auf nkn-priv einrichten (Python3)

Da `nkn-priv` keinen Internetzugang hat, kann kein `apt install` ausgeführt werden. Python3 ist auf Ubuntu bereits vorinstalliert und kann als HTTP-Server genutzt werden.

### SSH-Verbindung zu nkn-priv (über nkn-pub als Zwischenstation)

**Auf dem eigenen Rechner** – Key auf nkn-pub kopieren:

```bash
scp -i nkn-key.pem nkn-key.pem ubuntu@<ÖFFENTLICHE-IP-VON-NKN-PUB>:~/
```

**SSH in nkn-pub:**

```bash
ssh -i nkn-key.pem ubuntu@<ÖFFENTLICHE-IP-VON-NKN-PUB>
```

**Auf nkn-pub** – Key-Berechtigung setzen, dann weiter zu nkn-priv:

```bash
chmod 400 nkn-key.pem
ssh -i nkn-key.pem ubuntu@<PRIVATE-IP-VON-NKN-PRIV>
```

> Die private IP von `nkn-priv` findest du in der EC2-Konsole: **Instanzen** → `nkn-priv` → **Private IPv4-Adresse**

### Webserver-Verzeichnis und index.html anlegen

```bash
sudo mkdir -p /var/www/html
sudo nano /var/www/html/index.html
```

Folgenden Inhalt einfügen *(Name und Matrikelnummer anpassen!)*:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>nkn-priv</title>
</head>
<body>
    <h1>Antworten von DEIN_NAME – Matrikel: IHREMATRIKELNUMMER</h1>

    <h2>Was bedeutet die Schreibweise 10.1.0.0/16 für ein Subnetz?
    Wie viele Rechner können darin adressiert werden?</h2>

    <p>
        Die Schreibweise <strong>10.1.0.0/16</strong> ist die CIDR-Notation
        (Classless Inter-Domain Routing). Die Zahl nach dem Schrägstrich (/16)
        gibt an, wie viele Bits des 32-Bit-Adressraums für den
        <strong>Netzwerkteil</strong> reserviert sind.
        Die verbleibenden Bits stehen für den <strong>Hostteil</strong>
        zur Verfügung.
    </p>
    <ul>
        <li>Netzwerkteil: 16 Bit → Netzmaske 255.255.0.0</li>
        <li>Hostteil: 32 - 16 = 16 Bit</li>
        <li>Gesamte Adressen: 2^16 = 65.536</li>
        <li>Netzwerkadresse (10.1.0.0) und Broadcast (10.1.255.255): nicht nutzbar</li>
        <li><strong>Nutzbare Host-Adressen: 65.536 - 2 = 65.534</strong></li>
    </ul>

    <h2>Welche Art von Service (PaaS, IaaS oder SaaS) verwende ich,
    wenn ein Service auf einem privaten Rechner über einen Load Balancer
    öffentlich zugänglich gemacht wird? Erläuterung der Abkürzung.</h2>

    <p>
        Es handelt sich um <strong>IaaS – Infrastructure as a Service</strong>.
    </p>
    <p>
        Bei IaaS stellt der Cloud-Anbieter (z.B. AWS) die grundlegende
        Infrastruktur bereit: virtuelle Maschinen (EC2), Netzwerkkomponenten
        (VPC, Subnetze, Internet-Gateway) und den Load Balancer (ELB/ALB).
        Der Nutzer ist selbst verantwortlich für Betriebssystem, Middleware
        und die eigene Anwendung. Da der Dienst auf einem selbst verwalteten
        (privaten) Rechner (EC2-Instanz) läuft, bleibt die Kontrolle über
        die Infrastruktur beim Nutzer – das ist das typische Merkmal von IaaS.
    </p>
    <p>Zum Vergleich:</p>
    <ul>
        <li><strong>PaaS (Platform as a Service):</strong> Der Anbieter
        verwaltet auch Betriebssystem und Laufzeitumgebung. Der Nutzer
        deployt nur seinen Code (z.B. AWS Elastic Beanstalk).</li>
        <li><strong>SaaS (Software as a Service):</strong> Eine fertige
        Anwendung wird als Dienst genutzt, ohne dass der Nutzer irgendeine
        Infrastruktur verwaltet (z.B. Office 365, Gmail).</li>
    </ul>
</body>
</html>
```

Speichern: **CTRL + X** → **Y** → **Enter**

### Python3-HTTP-Server als dauerhaften Dienst einrichten

Der Python-Server stoppt, sobald die SSH-Verbindung getrennt wird. Als systemd-Dienst läuft er dauerhaft weiter.

```bash
sudo nano /etc/systemd/system/http-simple.service
```

Folgenden Inhalt einfügen:

```ini
[Unit]
Description=Einfacher Python HTTP Server Port 80
After=network.target

[Service]
ExecStart=/usr/bin/python3 -m http.server 80 --directory /var/www/html
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Speichern: **CTRL + X** → **Y** → **Enter**

```bash
sudo systemctl daemon-reload
sudo systemctl enable http-simple
sudo systemctl start http-simple

# Status prüfen – muss "active (running)" zeigen
sudo systemctl status http-simple
```

-----

## Schritt 11 – Von nkn-pub aus nkn-priv abfragen (Screenshot 8)

```bash
# SSH in nkn-pub (falls nicht schon verbunden)
ssh -i nkn-key.pem ubuntu@<ÖFFENTLICHE-IP-VON-NKN-PUB>

# HTTP-Anfrage an nkn-priv
curl http://<PRIVATE-IP-VON-NKN-PRIV>
```

**Erwartete Ausgabe:** Der HTML-Inhalt der `index.html` von `nkn-priv` erscheint im Terminal. Dies ist Screenshot 8.

-----

## Schritt 12 – Zusätzliche Festplatte prüfen (Screenshot 5)

```bash
# SSH in nkn-pub (falls nicht schon verbunden)
ssh -i nkn-key.pem ubuntu@<ÖFFENTLICHE-IP-VON-NKN-PUB>

# Blockgeräte anzeigen
lsblk
```

**Erwartete Ausgabe:**

```
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
xvda    202:0    0    8G  0 disk
└─xvda1 202:1    0    8G  0 part /
xvdb    202:16   0    8G  0 disk
```

`xvdb` (8G) ist die zusätzliche Festplatte. Sie muss laut Aufgabenstellung nicht gemountet werden – die Anzeige im `lsblk`-Output genügt für Screenshot 5.

-----

## Screenshot-Checkliste

|Nr.         |Was zeigen                                                 |Wie erstellen                                                                 |
|------------|-----------------------------------------------------------|------------------------------------------------------------------------------|
|Screenshot 1|Erfolgreiche SSH-Verbindung zu nkn-pub im Terminal         |`ssh -i nkn-key.pem ubuntu@<PUB-IP>`                                          |
|Screenshot 2|Browser: „Hello PUBLIC, mein Name ist…”                    |Browser öffnen: `http://<PUB-IP>`                                             |
|Screenshot 3|Ping funktioniert (ICMP-Antworten sichtbar)                |Terminal: `ping <PUB-IP>`                                                     |
|Screenshot 4|Sicherheitsgruppe nkn-pub-sg mit allen 3 Regeln            |AWS Console → EC2 → nkn-pub → Tab „Sicherheit” → nkn-pub-sg anklicken         |
|Screenshot 5|`lsblk` zeigt extra Festplatte (xvdb 8G)                   |Im SSH-Terminal auf nkn-pub: `lsblk`                                          |
|Screenshot 6|Instanz nkn-priv + zugewiesene SG nkn-priv-sg              |AWS Console → EC2 → nkn-priv → Tab „Sicherheit”                               |
|Screenshot 7|Eingehende Regeln von nkn-priv-sg (Source = nkn-pub-sg)    |AWS Console → EC2 → Sicherheitsgruppen → nkn-priv-sg → Tab „Eingehende Regeln”|
|Screenshot 8|`curl http://<PRIV-IP>` von nkn-pub – HTML-Antwort sichtbar|SSH-Terminal auf nkn-pub: `curl http://<PRIV-IP>`                             |

-----

-----

# Aufgabe 3 – Architekturdiagramm

**Aufgabenstellung:** Handgezeichnetes Bild (Stift auf Papier) mit der gesamten Infrastruktur aus Aufgabe 2.

## Pflicht-Elemente im Bild

- Region mit Bezeichnung (`eu-central-1`)
- VPC `nkn` mit CIDR `10.1.0.0/16`
- `Subnetz_public` mit CIDR `10.1.128.0/17`
- `Subnetz_private` mit CIDR `10.1.0.0/17`
- Beide EC2-Instanzen angedeutet (`nkn-pub`, `nkn-priv`)
- Sicherheitsgruppen mit ihrem Wirkungsbereich einzeichnen (gestrichelte Rahmen um die jeweilige Instanz)
- Internet Gateway (`nkn-igw`) für den Zugriff von außen
- Verbindungspfeil von `nkn-pub` → `nkn-priv` (curl intern)

## Beschriftungsreferenz

|Element            |Beschriftung im Bild                      |
|-------------------|------------------------------------------|
|Region             |`eu-central-1` (Frankfurt)                |
|VPC                |`nkn` – `10.1.0.0/16`                     |
|Subnetz_public     |`10.1.128.0/17`                           |
|Subnetz_private    |`10.1.0.0/17`                             |
|Internet Gateway   |`nkn-igw`                                 |
|nkn-pub            |Ubuntu, Apache2, öffentliche IP           |
|nkn-priv           |Ubuntu, Python3-HTTP, nur private IP      |
|SG nkn-pub-sg      |IN: TCP 22 + TCP 80 + ICMP → `0.0.0.0/0`  |
|SG nkn-priv-sg     |IN: TCP 22 + TCP 80 → nur von `nkn-pub-sg`|
|Verbindung pub→priv|`curl http://<PRIV-IP>` (intern)          |

## Empfohlene Zeichnungs-Struktur (von außen nach innen schachteln)

```
┌────────────────────────────────────────────────────────────────┐
│  Region: eu-central-1                                          │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  VPC: nkn  (10.1.0.0/16)                                │  │
│  │                                                          │  │
│  │  ┌───────────────────────┐   ┌────────────────────────┐ │  │
│  │  │  Subnetz_public       │   │  Subnetz_private       │ │  │
│  │  │  10.1.128.0/17        │   │  10.1.0.0/17           │ │  │
│  │  │                       │   │                        │ │  │
│  │  │  ┌- - - - - - - - -┐  │   │  ┌- - - - - - - - -┐  │ │  │
│  │  │  : nkn-pub-sg       :  │   │  : nkn-priv-sg      :  │ │  │
│  │  │  :  ┌───────────┐  :  │──▶│  :  ┌───────────┐  :  │ │  │
│  │  │  :  │  nkn-pub  │  :  │   │  :  │  nkn-priv │  :  │ │  │
│  │  │  :  │  Apache2  │  :  │   │  :  │  Python   │  :  │ │  │
│  │  │  :  └───────────┘  :  │   │  :  └───────────┘  :  │ │  │
│  │  │  └- - - - - - - - -┘  │   │  └- - - - - - - - -┘  │ │  │
│  │  └───────────┬───────────┘   └────────────────────────┘ │  │
│  └──────────────┼─────────────────────────────────────────┘  │
│                 │                                              │
│            [nkn-igw]                                          │
└─────────────────┼──────────────────────────────────────────────┘
                  │
              Internet
```

> **Hinweis:** Sicherheitsgruppen als gestrichelte Rahmen (- - -) direkt um die EC2-Instanzen zeichnen und die Eingangsregeln daneben notieren.

-----

-----

# Häufige Fehler & Lösungen

|Problem                                      |Ursache                                         |Lösung                                                                                                            |
|---------------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
|S3: `AccessDenied` beim Hochladen            |boto3 findet keine Credentials                  |`aws configure` ausführen                                                                                         |
|S3: JPG-URL gibt trotzdem `AccessDenied`     |`BlockPublicPolicy` ist noch `true`             |Das Skript setzt es automatisch auf `false` – Skript nochmal ausführen                                            |
|EC2 hat keine öffentliche IP                 |Auto-Assign Public IP nicht aktiviert           |Subnetz_public → Aktionen → „IPv4-Adresse automatisch zuweisen aktivieren”                                        |
|`curl <PRIV-IP>` hängt / Timeout             |nkn-priv-sg hat falsche Source                  |Inbound-Regel: Source muss die Security Group `nkn-pub-sg` sein, nicht eine IP                                    |
|SSH zu nkn-priv schlägt fehl                 |Key nicht auf nkn-pub kopiert                   |`scp -i nkn-key.pem nkn-key.pem ubuntu@<PUB-IP>:~/`                                                               |
|Python-HTTP-Server läuft nicht mehr          |SSH-Tab wurde geschlossen                       |Systemd-Dienst verwenden (Schritt 10) oder neu starten: `sudo python3 -m http.server 80 --directory /var/www/html`|
|Browser zeigt Apache-Defaultseite            |index.html nicht korrekt geändert               |`sudo nano /var/www/html/index.html` → Inhalt prüfen → `sudo systemctl reload apache2`                            |
|`Permission denied (publickey)` bei SSH      |Falscher Key oder falsche Berechtigungen        |`chmod 400 nkn-key.pem` – und prüfen, ob derselbe Key beim Instanz-Start gewählt wurde                            |
|Route Table leitet Traffic nicht ins Internet|Route Table nicht mit Subnetz_public verknüpft  |Route Table `nkn-rt-public` → Tab „Subnetzzuordnungen” → `Subnetz_public` hinzufügen                              |
|`lsblk` zeigt nur ein Gerät                  |Extra-Volume beim Instanzstart nicht hinzugefügt|Instanz stoppen → Volumes → neues 8-GiB-gp3-Volume erstellen und an `/dev/sdb` anhängen                           |
