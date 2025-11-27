## AWS CLI zeigen

1. AWS CLI installieren (falls nicht vorhanden):
   - Windows: MSI Installer
   - Linux:
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
     sudo ./aws/install
  - Mac:
    brew install awscli
2. Terminal öffnen
3. Befehl testen:
   aws --version
4. In AWS cli wechslen
    cd .aws

## S3 Buckets mit AWS CLI im Terminal bedienen

### Voraussetzungen
- AWS CLI muss installiert und konfiguriert sein (`aws configure`)
- Zugangsdaten (Access Key, Secret Key) sind hinterlegt

### Wichtige Terminal-Befehle (macOS/Linux)
- `cd <pfad>`: In ein Verzeichnis wechseln
- `ls`: Inhalt eines Verzeichnisses anzeigen
- `mkdir <verzeichnis>`: Neues Verzeichnis erstellen
- `rm <datei>`: Datei löschen
- `touch <datei>`: Neue Datei anlegen

### S3-Befehle mit AWS CLI
- S3 Buckets auflisten:
  ```sh
  aws s3 ls
  ```
- Inhalt eines Buckets anzeigen:
  ```sh
  aws s3 ls s3://<bucket-name>/
  ```
- Datei in einen Bucket hochladen:
  ```sh
  aws s3 cp <lokale-datei> s3://<bucket-name>/<zielpfad>
  ```
- Datei aus einem Bucket herunterladen:
  ```sh
  aws s3 cp s3://<bucket-name>/<datei> <lokaler-pfad>
  ```
- Verzeichnis synchronisieren:
  ```sh
  aws s3 sync <lokales-verzeichnis> s3://<bucket-name>/<zielverzeichnis>
  ```
- Bucket/Datei löschen:
  ```sh
  aws s3 rm s3://<bucket-name>/<datei>
  aws s3 rb s3://<bucket-name> --force
  ```

### Beispiel-Workflow
1. Terminal öffnen
2. In das Arbeitsverzeichnis wechseln:
   ```sh
   cd ~/meinprojekt
   ```
3. Neuen Ordner erstellen:
   ```sh
   mkdir daten
   cd daten
   ```
4. Datei anlegen und hochladen:
   ```sh
   touch test.txt
   aws s3 cp test.txt s3://mein-bucket/test.txt
   ```
5. Inhalt des Buckets prüfen:
   ```sh
   aws s3 ls s3://mein-bucket/
   ```

### Hinweise
- Mit `aws s3 sync` können ganze Verzeichnisse effizient abgeglichen werden.
- Die AWS CLI bietet viele weitere Optionen, z.B. für Versionierung, Rechte und Metadaten.
- Für alle Befehle gibt es Hilfe mit `aws s3 help` oder `aws s3 <befehl> help`.

---

Mit diesen Befehlen kannst du S3 Buckets direkt aus dem Terminal verwalten und typische Dateioperationen durchführen.