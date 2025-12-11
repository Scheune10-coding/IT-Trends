## Download-Skript – Datei aus AWS-Bucket herunterladen

1. AWS CLI konfigurieren:
   ```sh
   aws configure
   ```

<details>
<summary><strong>Skript für Mac/Linux (.sh)</strong></summary>

**Erstellen:**
1. Neues Skript anlegen:
    ```sh
    nano s3_download.sh
    ```

2. Beispielinhalt:
    ```sh
    echo "Bitte gib den Bucket-Namen ein:"
    read bucketname

    echo "Bitte gib den Dateienpfad ein:"
    read dateipfad

    dateiname=$(basename "$dateipfad")

    echo "Starte download von $dateiname von $bucketname ..."
    aws s3 cp s3://$bucketname/$dateipfad ./$dateiname

    echo "Download abgeschlossen."
    ```
- [.sh for mac](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_DOWNLOAD/s3_download.sh)

3. Skript ausführbar machen:
    ```sh
    chmod +x s3_download.sh
    ```

4. Skript ausführen:
    ```sh
    ./s3_download.sh
    ```

</details>

<details>
<summary><strong>Skript für Windows (.bat)</strong></summary>

**Erstellen:**
1. Neues Skript anlegen:
    - Rechtsklick → Neu → Textdatei → Umbenennen zu `s3_download.bat`

2. Beispielinhalt:
    ```bat
    @echo off
    setlocal

    set /p bucketname=Bitte gib den Bucket-Namen ein:
    set /p dateipfad=Bitte gib den Dateienpfad ein:

    for %%F in ("%dateipfad%") do set dateiname=%%~nxF

    echo Starte download von %dateiname% von %bucketname% ...
    aws s3 cp s3://%bucketname%/%dateipfad% .\%dateiname%

    echo Download abgeschlossen.
    endlocal
    ```
- [.bat for windows](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_DOWNLOAD/s3_download.bat)

3. Skript ausführen:
    - Doppelklick auf die `.bat`-Datei oder im Terminal:
      ```
      s3_download.bat
      ```

</details>

---

6. Überprüfen:
   - Datei muss im gleichen Ordner wie das Skript erscheinen