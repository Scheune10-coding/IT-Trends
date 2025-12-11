## Sync-Skript – Lokales Verzeichnis mit S3 synchronisieren

1. AWS CLI konfigurieren:
   ```sh
   aws configure
   ```

<details>
<summary><strong>Skript für Mac/Linux (.sh)</strong></summary>

**Erstellen:**
1. Neues Skript anlegen:
    ```sh
    nano s3_sync.sh
    ```

2. Beispielinhalt:
    ```sh
    echo "Bitte gib den lokalen Ordnerpfad ein:"
    read ordnerpfad

    echo "Bitte gib den Ziel-Bucket-Namen ein:"
    read bucketname

    ordnername=$(basename "$ordnerpfad")

    echo "Starte sync von $ordnerpfad zu s3://$bucketname/$ordnername/ ..."
    aws s3 sync "$ordnerpfad" "s3://$bucketname/$ordnername/" --delete

    echo "Sync abgeschlossen."
    ```
- [.sh for mac](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_SYNC/s3_sync.sh)

3. Skript ausführbar machen:
    ```sh
    chmod +x s3_sync.sh
    ```

4. Skript ausführen:
    ```sh
    ./s3_sync.sh
    ```

</details>

<details>
<summary><strong>Skript für Windows (.bat)</strong></summary>

**Erstellen:**
1. Neues Skript anlegen:
    - Rechtsklick → Neu → Textdatei → Umbenennen zu `s3_sync.bat`

2. Beispielinhalt:
    ```bat
    @echo off
    setlocal

    set /p ordnerpfad=Bitte gib den lokalen Ordnerpfad ein:
    set /p bucketname=Bitte gib den Ziel-Bucket-Namen ein:

    for %%F in ("%ordnerpfad%") do set ordnername=%%~nxF

    echo Starte sync von %ordnerpfad% zu s3://%bucketname%/%ordnername%/ ...
    aws s3 sync "%ordnerpfad%" "s3://%bucketname%/%ordnername%/" --delete

    echo Sync abgeschlossen.
    endlocal
    ```
- [.bat for windows](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_SYNC/s3_sync.bat)

3. Skript ausführen:
    - Doppelklick auf die `.bat`-Datei oder im Terminal:
      ```
      s3_sync.bat
      ```

</details>

---

6. Überprüfen:
   - S3-Bucket öffnen → Dateien müssen identisch sein