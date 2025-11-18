## Sync-Skript – Lokales Verzeichnis mit S3 synchronisieren

1. AWS CLI konfigurieren:
   aws configure
2. Skript erstellen, z. B. s3_sync.sh:
```
echo "Bitte gib den lokalen Ordnerpfad ein:"
read ordnerpfad

echo "Bitte gib den Ziel-Bucket-Namen ein:"
read bucketname

# Der letzte Teil des Pfades wird als Ordnername im Bucket verwendet
ordnername=$(basename "$ordnerpfad")

echo "Starte sync von $ordnerpfad zu s3://$bucketname/$ordnername/ ..."
aws s3 sync "$ordnerpfad" "s3://$bucketname/$ordnername/" --delete

echo "Sync abgeschlossen."
```
3. Skript ausführbar machen:
   chmod +x sync.sh
4. Skript ausführen:
   ./s3_sync.sh
5. Überprüfen:
   - S3-Bucket öffnen → Dateien müssen identisch sein
