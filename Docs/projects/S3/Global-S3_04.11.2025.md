## S3-Datei für alle Nutzer sichtbar machen

1. AWS-Konsole → S3 öffnen

2. Neuen Bucket erstellen (oder bestehenden wählen)
   - **Block all public access** DEAKTIVIEREN (falls erlaubt)
   - **Block public access to buckets and objects granted through any access control lists (ACLs)** einschalten

3. Datei hochladen:
   - **Upload** → Datei auswählen → hochladen

4. Datei öffentlich machen:
   - Bucket auswählen → **Permissions** → **Edit Bucket policy**
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

5. Öffentlichen Link kopieren:
   - Datei im Bucket auswählen → **Object URL** → Link verwenden

6. Test:
   - Link in privatem Browserfenster öffnen
   - Datei muss ohne Login sichtbar sein
