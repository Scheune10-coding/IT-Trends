## Sync-Skript – Lokales Verzeichnis mit S3 synchronisieren

1. AWS CLI konfigurieren:
   aws configure

2. Skript erstellen, z. B. s3_sync.sh:
- [.sh for mac](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_SYNC/s3_sync.sh)
- [.bat for windows](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/S3_SYNC/s3_sync.bat)
3. In Scripts/S3_SNYC wechseln
```
cd Scripts/S3_SYNC
```

4. Skript ausführbar machen:
```
chmod +x s3_sync.sh
```

5. Skript ausführen:
```
./s3_sync.sh
```

6. Überprüfen:
   - S3-Bucket öffnen → Dateien müssen identisch sein
