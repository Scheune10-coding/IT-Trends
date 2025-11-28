## Download-Skript – Datei aus AWS-Bucket herunterladen

1. AWS CLI konfigurieren:
   aws configure

2. Skript erstellen, z. B. s3_sync.sh:
```bash
echo "Bitte gib den Bucket-Namen ein:"
read bucketname

echo "Bitte gib den Dateienpfad ein:"
read dateipfad

dateiname=$(basename "$dateipfad")

echo "Starte download von $dateiname von $bucketname ..."
aws s3 cp s3://$bucketname/$dateipfad ../$dateiname

echo "Download abgeschlossen."
```

3. In Scripts/S3_SNYC (Ordner wo script Datei liegt) wechseln
```
cd Scripts/S3_DOWNLOAD
```

4. Skript ausführbar machen:
```
chmod +x s3_download.sh
```

5. Skript ausführen:
```
./s3_download.sh
```

6. Überprüfen:
  - Datei muss neben Skript-Datei erscheinen
