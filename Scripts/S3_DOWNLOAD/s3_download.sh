echo "Bitte gib den Bucket-Namen ein:"
read bucketname

echo "Bitte gib den Dateienpfad ein:"
read dateipfad

# Der letzte Teil des Pfades wird als Ordnername im Bucket verwendet
dateiname=$(basename "$dateipfad")

echo "Starte download von $dateiname von $bucketname ..."
aws s3 cp s3://$bucketname/$dateipfad .

echo "Download abgeschlossen."