@echo off
setlocal

REM Bucket-Namen abfragen
set /p bucketname=Bitte gib den Bucket-Namen ein:

REM Datei-Pfad abfragen
set /p dateipfad=Bitte gib den Dateienpfad ein:

REM Dateiname aus Pfad extrahieren
for %%F in ("%dateipfad%") do set dateiname=%%~nxF

echo Starte download von %dateiname% von %bucketname% ...
aws s3 cp s3://%bucketname%/%dateipfad% .

echo Download abgeschlossen.
endlocal