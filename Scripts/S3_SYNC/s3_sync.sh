echo "Bitte gib den lokalen Ordnerpfad ein:"
read ordnerpfad

echo "Bitte gib den Ziel-Bucket-Namen ein:"
read bucketname

# Der letzte Teil des Pfades wird als Ordnername im Bucket verwendet
ordnername=$(basename "$ordnerpfad")

echo "Starte sync von $ordnerpfad zu s3://$bucketname/$ordnername/ ..."
aws s3 sync "$ordnerpfad" "s3://$bucketname/$ordnername/" --delete

echo "Sync abgeschlossen."