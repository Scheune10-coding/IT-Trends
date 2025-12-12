# REST API Schnittstelle mit Python

Dieses Skript demonstriert, wie man mit Python eine REST-API abfragt, Daten extrahiert und in eine CSV-Datei speichert. Es ist für die Anmeldung und Namenslistenabfrage einer Beispiel-Webseite konzipiert.

## Funktionen und Ablauf

- [Hier gehts zum Python Skript](https://github.com/Scheune10-coding/IT-Trends/blob/main/Scripts/REST_API/fetch_names_from_url.py)

1. **Registrierung (optional)**
   - Über die Variable `REGISTER` kann gesteuert werden, ob eine Registrierung durchgeführt wird.
   - Die Funktion `register()` sendet eine GET-Anfrage mit den Parametern aus `REGISTER_PARAMS` an die Registrierungs-URL.
   - Die Antwort wird auf ein JSON-Objekt geprüft und ausgegeben.

2. **Namensliste abrufen**
   - Die Funktion `fetch_list_html()` lädt die HTML-Seite mit der Namensliste von der angegebenen URL.
   - Die Funktion `extract_names()` sucht im HTML nach einem `<pre>`-Block, extrahiert den darin enthaltenen JSON-Text und wandelt ihn in eine Python-Liste um.
   - Fehler werden geworfen, falls kein `<pre>`-Block oder keine Liste gefunden wird.

3. **Speichern als CSV**
   - Die Funktion `save_to_csv()` speichert alle gefundenen Namen in einer CSV-Datei mit UTF-8-Kodierung.

4. **Ablauf (main)**
   - Optional Registrierung.
   - Abruf und Extraktion der Namensliste.
   - Ausgabe der Namen in der Konsole.
   - Speicherung der Namen in einer CSV-Datei.

## Wichtige Hinweise
- Die URLs und Parameter sind auf die Beispiel-Webseite zugeschnitten und müssen ggf. angepasst werden.
- Das Skript verwendet reguläre Ausdrücke, um Daten aus HTML zu extrahieren. Die wichtigsten Muster sind im Code kommentiert.
- Die CSV-Datei wird im aktuellen Verzeichnis gespeichert.

## Beispiel für die Nutzung
```python
REGISTER = True  # Registrierung aktivieren
main()           # Skript ausführen
```

## Abhängigkeiten
- requests
- re
- json
- csv

Installiere ggf. fehlende Pakete mit:
```bash
pip install requests
```

---

Dieses Skript eignet sich als Vorlage für REST-API-Abfragen und Datenverarbeitung mit Python.
