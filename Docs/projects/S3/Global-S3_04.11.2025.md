## S3-Datei für alle Nutzer sichtbar machen

1. AWS-Konsole → S3 öffnen

2. Neuen Bucket erstellen (oder bestehenden wählen)
   - **Block all public access** DEAKTIVIEREN (falls erlaubt)
   - **Block public access to buckets and objects granted through any access control lists (ACLs)** einschalten

3. Datei hochladen:
   - **Upload** → Datei auswählen → hochladen

4. Datei öffentlich machen:
   - Bucket auswählen → **Permissions** → **Edit Bucket policy**
   - du kannst auch durch Klick auf **Add Statement** eine Standard json erzeugen lassen
   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "JPEG_TestZugriff",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::<bucket>/<file>"
        }
      ]
    }
   ```
   **Erklärung der Variablen:**
   - `"Version"`: Gibt die Version des Policy-Formats an (immer `"2012-10-17"` verwenden).
   - `"Statement"`: Liste von Berechtigungsregeln.
   - `"Sid"`: (Statement ID) Beliebiger Name zur Identifikation der Regel.
   - `"Effect"`: `"Allow"` (erlauben) oder `"Deny"` (verbieten).
   - `"Principal"`: Wer erhält Zugriff? `"*"` bedeutet jeder (öffentlich).
   - `"Action"`: Welche Aktion ist erlaubt? Beispiele für häufig genutzte Actions:
     - `"s3:GetObject"` – Datei herunterladen (Lesen)
     - `"s3:PutObject"` – Datei hochladen (Schreiben)
     - `"s3:DeleteObject"` – Datei löschen
     - `"s3:ListBucket"` – Inhalte des Buckets auflisten
     - `"s3:GetBucketLocation"` – Standort des Buckets abfragen
     - `"s3:GetObjectAcl"` – Zugriffsrechte einer Datei abfragen
     - `"s3:PutObjectAcl"` – Zugriffsrechte einer Datei setzen
     - `"s3:ListAllMyBuckets"` – Alle eigenen Buckets auflisten

   Du kannst `"Action"` auch als Array angeben, um mehrere Aktionen zu erlauben:
   ```json
   "Action": [
     "s3:GetObject",
     "s3:PutObject"
   ]
   ```

   - `"Resource"`: Auf welche Ressource bezieht sich die Regel?  
     - `"arn:aws:s3:::<bucket>/<file>"` = nur eine bestimmte Datei  
     - `"arn:aws:s3:::<bucket>/*"` = alle Dateien im Bucket

   **Weitere Beispiele für Bucket-Policies:**

   - **Alle Dateien im Bucket öffentlich machen:**
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadAll",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::<bucket>/*"
         }
       ]
     }
     ```

   - **Nur bestimmte IP-Adresse darf lesen:**
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "AllowFromIP",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::<bucket>/*",
           "Condition": {
             "IpAddress": { "aws:SourceIp": "203.0.113.0/24" }
           }
         }
       ]
     }
     ```

   - **Nur bestimmte Datei öffentlich machen:**
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadOneFile",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::<bucket>/meinbild.jpg"
         }
       ]
     }
     ```

   - **Nur GET und LIST erlauben (Lesen und Auflisten):**
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadList",
           "Effect": "Allow",
           "Principal": "*",
           "Action": [
             "s3:GetObject",
             "s3:ListBucket"
           ],
           "Resource": [
             "arn:aws:s3:::<bucket>",
             "arn:aws:s3:::<bucket>/*"
           ]
         }
       ]
     }
     ```

5. Öffentlichen Link kopieren:
   - Datei im Bucket auswählen → **Object URL** → Link verwenden

6. Test:
   - Link in privatem Browserfenster öffnen
   - Datei muss ohne Login sichtbar sein

**Hinweis:**  
Öffentliche Zugriffsrechte sollten nur vergeben werden, wenn es wirklich notwendig ist (z. B. für statische Webseiten, öffentliche Downloads). Für sensible Daten immer restriktive Policies verwenden!