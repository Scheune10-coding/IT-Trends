# AWS: S3, Infrastructure as Code, CloudFormation, Lambda (ausführlich)

## S3 Basics
- S3 ist Objektspeicher.
- Struktur:
  - Bucket (oberste Ebene)
  - Objekte (Dateien) in Buckets
- Bucket-Name muss weltweit eindeutig sein.

### Public Access (prüfungsrelevant)
- Standard: Public Access blockiert (empfohlen).
- Zugriffsteuerung:
  - Bucket Policy (JSON)
  - ACLs (Access Control Lists) - in vielen Setups deaktiviert/unerwünscht
- Typischer Fehler:
  - Objekt ist hochgeladen, URL funktioniert nicht -> weil Policy/Block Public Access.

---

## Objekte hochladen und URL nutzen
- Objekt hochladen (Console oder CLI)
- Objekt öffnen -> Objekt-URL kopieren
- Wenn AccessDenied:
  - Public Access Block prüfen
  - Bucket Policy prüfen
  - korrekte Resource ARN (inkl. Objektpfad) prüfen

---

## AWS CLI – Setup (Windows-Beispiel)
1) AWS CLI installieren
2) Credentials setzen:
   - aws configure
   - Access Key ID
   - Secret Access Key
   - Default Region (z. B. us-east-1)
   - Output format (json)

Wo liegt es lokal?
- ~/.aws/credentials und ~/.aws/config

---

## AWS S3 Commands (prüfungsnah)
- Liste:
  - aws s3 ls
- Upload (eine Datei):
  - aws s3 cp datei.txt s3://bucket-name/
- Sync (Ordner):
  - aws s3 sync ./localdir s3://bucket-name/remote/

Hinweis:
- Sync ist gut für "alle Dateien" und inkrementell.
- cp ist gut für einzelne Dateien.

---

## Storage Classes (S3)
- Standard
- Standard-IA (Infrequent Access)
- One Zone-IA
- Glacier (Archiv)

Wann welche?
- Standard: häufige Zugriffe
- IA: seltene Zugriffe, aber schnell abrufbar
- Glacier: Archiv, Abruf dauert länger, günstig

---

## Infrastructure as Code (IaC)
- Infrastruktur wird als Code beschrieben statt "klicken".
- Vorteil:
  - reproduzierbar
  - versionierbar (Git)
  - weniger Fehler durch Klickerei

Beispiel:
- VPC, Subnetze, Security Groups als Template statt manuell.

---

## CloudFormation
- AWS IaC-Dienst.
- Templates typischerweise YAML/JSON.
- Du definierst Ressourcen, AWS erstellt Stack.

Prüfungsnutzen:
- Erklären können, warum IaC besser ist:
  - wiederholbar
  - reviewbar
  - automatisierbar (CI/CD)

---

## AWS Lambda (FaaS)
- Pay per Use:
  - Abrechnung nach Rechenzeit/Memory, nicht "pro Anfrage" als Kern.
- Event-basiert:
  - S3 Upload triggert Lambda
  - API Gateway Request triggert Lambda

Beispiel:
- Wenn Bild in S3 hochgeladen:
  - Lambda erzeugt Thumbnail und speichert es zurück.

---

## AWS Pricing Tools
- AWS Pricing Calculator:
  - Kosten abschätzen vor Nutzung
- Cost Explorer:
  - zeigt echte Ausgaben/Verläufe im Account
