import re, json, csv, html, requests  # Importiere benötigte Bibliotheken

REGISTER = False  # Steuert, ob eine Registrierung durchgeführt wird
REGISTER_URL = "https://awsanmeldung.kasche.dhge-web.de/register"  # URL für die Registrierung
LIST_URL     = "https://awsanmeldung.kasche.dhge-web.de/list"      # URL für die Namensliste
OUTFILE      = "aws_name_list.csv"                                 # Name der Ausgabedatei

# Parameter für die Registrierung
REGISTER_PARAMS = {
    "name":  "Leon Scheunemann",              # Name des Teilnehmers
    "email": "schele.wi24@stud.gera.dhge.de", # E-Mail-Adresse
    "login": "schele.wi24",                   # Login-Name
    "kurs":  "d3d2kyNA==",                    # Kurs (Base64-codiert)
}

# Führt eine Registrierung durch (wenn aktiviert)
def register(url: str, params: dict):
    r = requests.get(url, params=params,  timeout=15)  # Sende GET-Anfrage mit Parametern
    r.raise_for_status()                               # Fehler werfen, falls HTTP-Fehler
    match = re.search(r'\{([^}]*)\}', r.text)          # Suche nach Objekt in geschweiften Klammern
    print("Register Object:", match.group(1))          # Gib das gefundene Objekt aus

# Holt die HTML-Seite mit der Namensliste
def fetch_list_html(url: str) -> str:
    r = requests.get(url,  timeout=15)                 # Sende GET-Anfrage
    return r.text                                      # Gib den HTML-Text zurück

# Extrahiert die Namen aus dem HTML (im <pre>-Block als JSON)
def extract_names(html: str) -> list[str]:
    # (.*?) ist ein regulärer Ausdruck:
    # ( )   : Klammern markieren eine Gruppe, die später mit match.group(1) abgerufen werden kann
    # .     : steht für ein beliebiges Zeichen (außer Zeilenumbruch)
    # *     : beliebig viele Wiederholungen (auch null)
    # ?     : macht die Suche "nicht gierig" (also das kürzeste passende Stück)
    # Es wird also der Inhalt zwischen <pre> und </pre> gesucht.
    # Alternativen wären z.B.:
    # (.*)   : "gierig" – sucht das längste passende Stück
    # ([^<]*) : sucht alles außer dem Zeichen '<'
    # ([\s\S]*) : sucht wirklich alles, auch Zeilenumbrüche
    match = re.search(r"<pre>(.*?)</pre>", html, re.S)            # Suche nach <pre>-Block
    if not match:
        raise ValueError("Kein <pre>...<\\/pre>-Block gefunden.") # Fehler, falls kein Block gefunden
    json_text = match.group(1).strip()                            # Entferne Leerzeichen
    data = json.loads(json_text)                                  # Lade JSON-Daten
    if not isinstance(data, list):
        raise ValueError("JSON enthält keine Liste.")             # Fehler, falls keine Liste
    return data                                                   # Gib die Liste zurück

# Speichert die Namen in einer CSV-Datei
def save_to_csv(names: list[str], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as f:         # Öffne Datei zum Schreiben
        w = csv.writer(f)                                                # Erstelle CSV-Schreiber
        w.writerow(["Name"])                                             # Schreibe Kopfzeile
        for n in names:
            w.writerow([n])                                              # Schreibe jeden Namen in eine Zeile
    print(f"\n{len(names)} Namen wurden in '{filename}' gespeichert.\n") # Ausgabe der Anzahl

# Hauptfunktion: Steuert den Ablauf des Programms
def main():
    if REGISTER:                                      # Falls Registrierung aktiviert
      print(f"Registriere (GET {REGISTER_URL}) …")    # Hinweis auf Registrierung
      register(REGISTER_URL, REGISTER_PARAMS)         # Registrierung durchführen

    print(f"Lade Liste von {LIST_URL} …")             # Hinweis auf Laden der Liste
    names = extract_names(fetch_list_html(LIST_URL))  # Namen aus HTML extrahieren

    print("\nGefundene Namen:")                       # Ausgabe der gefundenen Namen
    for n in names:
        print(" -", n)

    save_to_csv(names, OUTFILE)                       # Namen in CSV speichern

main() # Starte das Programm
