# AWS S3 – Grundlagen und Überblick

---

## Was ist AWS S3?

**Amazon Simple Storage Service (S3)** ist ein skalierbarer Objektspeicher in der AWS-Cloud. S3 wird genutzt, um beliebige Daten (z. B. Dokumente, Bilder, Backups) sicher und hochverfügbar zu speichern.

---

### Wichtige Eigenschaften von S3

- **Objektspeicher:** Daten werden als Objekte in sogenannten Buckets gespeichert.
- **Buckets:** Container für Daten, vergleichbar mit Ordnern.
- **Globale Verfügbarkeit:** Daten können weltweit abgerufen werden.
- **Skalierbarkeit:** Automatische Anpassung an beliebige Datenmengen.
- **Sicherheit:** Zugriffskontrolle über IAM, Bucket Policies und ACLs.
- **Versionierung:** Mehrere Versionen eines Objekts können gespeichert werden.
- **Lebenszyklusregeln:** Automatische Archivierung oder Löschung von Daten.
- **Storage-Klassen:** Unterschiedliche Preismodelle für verschiedene Anforderungen (Standard, Intelligent-Tiering, Glacier, usw.).

---

## Typische Anwendungsfälle

- Backup und Archivierung
- Hosting von statischen Webseiten
- Speicherung von Logfiles und Daten für Big Data/Analytics
- Austausch von Dateien zwischen Anwendungen und Nutzern
- Medien-Streaming (Bilder, Videos, Audio)

---

## Wichtige S3-Befehle mit AWS CLI

```sh
# Bucket erstellen
aws s3 mb s3://mein-bucket

# Datei hochladen
aws s3 cp datei.txt s3://mein-bucket/

# Datei herunterladen
aws s3 cp s3://mein-bucket/datei.txt .

# Inhalt eines Buckets anzeigen
aws s3 ls s3://mein-bucket/

# Bucket synchronisieren
aws s3 sync ./lokaler_ordner s3://mein-bucket/

# Datei löschen
aws s3 rm s3://mein-bucket/datei.txt
```

---

## Kosten und Preismodelle

- Abrechnung nach genutztem Speicherplatz (GB/Monat)
- Kosten für Datenübertragung (ausgehend)
- Kosten für Requests (PUT, GET, DELETE, usw.)
- Günstigere Storage-Klassen für selten genutzte Daten (z. B. Glacier)

Weitere Infos:  
- [AWS S3 Dokumentation](https://docs.aws.amazon.com/s3/index.html)
- [AWS S3 Pricing](https://aws.amazon.com/de/s3/pricing/)

---