@echo off
setlocal

REM Lokalen Ordnerpfad abfragen
set /p ordnerpfad=Bitte gib den lokalen Ordnerpfad ein:

REM Ziel-Bucket-Namen abfragen
set /p bucketname=Bitte gib den Ziel-Bucket-Namen ein:

REM Ordnername aus Pfad extrahieren
for %%F in ("%ordnerpfad%") do set ordnername=%%~nxF

echo Starte sync von %ordnerpfad% zu s3://%bucketname%/%ordnername%/ ...
aws s3 sync "%ordnerpfad%" "s3://%bucketname%/%ordnername%/" --delete

echo Sync abgeschlossen.
endlocal