# IT-Trends – Überblick & Cloud Computing

## 1) IT-Trends – Einleitung / Überblick

### Liste von mindestens 6 IT-Trends mit kurzer Erläuterung
- **Cloud Computing**: IT-Ressourcen über das Internet flexibel und skalierbar nutzbar (z. B. Rechenleistung, Speicher). Pay-as-you-go und ortsunabhängig.
- **Industrie 4.0**: Vernetzte, automatisierte Produktion. Maschinen kommunizieren selbstständig (z. B. Predictive Maintenance in Werkstätten).
- **Internet of Things (IoT)**: Vernetzung physischer Geräte (Sensoren, Fahrzeuge, Maschinen). Grundlage für Smart City und Bahninfrastruktur.
- **Blockchain**: Technologie zur fälschungssicheren Speicherung von Daten in einer Kette von Einträgen. Nachvollziehbarkeit, Integrität, Transparenz, Manipulationsschutz. Beispiel: Dokumentation von Zugfahrten bei Grenzübertritt.
- **Künstliche Intelligenz (KI)**: Systeme lernen aus Daten (Chatbots, Prognosen, Bilderkennung). Beispiel: Verspätungsprognosen bei der DB.
- **Microservices**: Anwendungen bestehen aus kleinen, unabhängigen Diensten. Jeder Dienst erfüllt eine bestimmte Aufgabe.
- **Edge Computing**: Datenverarbeitung nahe an Sensoren oder Zügen. Reagiert schnell ohne Internetverbindung.

**Beispiel Deutsche Bahn:**
IoT-Sensoren an Zügen senden Daten in Echtzeit an eine Cloud-Plattform, KI bewertet Zustände der Fahrzeuge, Microservices kümmern sich um Wartungs- und Planungsprozesse.

### Unterschied zwischen Cloud Computing und Edge Computing
- **Cloud**: Zentrale Verarbeitung in Rechenzentren, hohe Rechenleistung, gut für Analysen und große Datenmengen.
- **Edge**: Dezentrale Verarbeitung vor Ort (z. B. im Zug), geringe Latenz und unabhängig vom Internet.
- **Praxis**: Edge für Echtzeitdaten (z. B. Bremssensoren), Cloud für langfristige Analyse und KI-Training.

### Anwendungsfälle für KI
#### 1. Bilderkennung
- KI erkennt Objekte, Personen oder Muster in Bildern/Videos
Beispiel: Qualitätskontrollen, Gesichtserkennung
#### 2. Spracherkennung
- KI versteht und erzeugt menschliche Sprache
Beispiel: Chatbots, Sprachassistenten, Übersetzer
#### 3. Predictive Analytics
- KI analysiert Daten und prognostiziert zukünftige Entwicklung
Beispeil: Umsatzprognosen, Wartungsvorhersagen
#### 4. Autonome Systeme
- KI trifft Entscheidungen in Echtzeit auf Basis von Server - und Kameradaten
Beispiel: Autonomes fahren von Autos, Drohnen
#### 5. Medizinische Diagnostik
- KI unterstützt bei der Auswertung medizinischer Daten
Beispiel: Tumorerkrankung, Analyse MRT
#### 6. Robotik
- KI steuert Roboter und ermöglicht selbständiges Lernen und Handeln
#### 7. Fraud Detecion
- KI erkennt ungewöhnliche Muster und verdächtige Transaktionen

### Grundprinzipien der IT-Sicherheit
- **CIA-Triade**: Confidentiality (Vertraulichkeit), Integrity (Integrität), Availability (Verfügbarkeit).
- **AAA-Prinzip**: Authentication, Authorization, Accounting.
- **Zero-Trust-Prinzip**: Kein Standardvertrauen, alles wird überprüft.
- **Defense-in-Depth**: Mehrere Sicherheitsschichten.
- **Praxis DB**: Zugriffe per MFA, Verschlüsselung, BSI-Grundschutz.

---

## 2) Cloud Computing & REST-Schnittstellen

### Eine REST-Schnittstelle auf der Kommandozeile bedienen
**Beispiel mit curl:**
- GET – Daten abrufen:
  ```sh
  curl -i https://api.db.example.com/v1/trains/ICE123
  ```
- POST – Daten senden:
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"status":"ready"}' https://api.db.example.com/v1/trains
  ```
- Tipp: `-i` zeigt Header, `-v` Debug, `-sS` still mit Fehlern

### Aufbau einer REST-Schnittstelle
- Ressourcenorientiert: eindeutige URLs (z. B. /v1/trains/ICE123).
- HTTP-Methoden: GET, POST, PUT, PATCH, DELETE.
- Antwortformat: meist JSON.
- Statuscodes: 200 OK, 201 Created, 404 Not Found, 500 Error.
- Authentifizierung über Token (Bearer).
- Versionierung über Pfad (z. B. /v1) oder Header.

### Wesentliche Eigenschaften und Vorteile einer REST-Schnittstelle
- Einheitliche HTTP-Schnittstelle, leicht verständlich.
- Zustandslos (stateless) – einfach skalierbar.
- Cachbar – schnellere Antworten.
- Lose gekoppelt – unabhängige Entwicklung.
- Standardisiert – viele Tools verfügbar.

### Microservice-Architektur vs. Service-orientierte Architektur (SOA)
- **SOA**: Zentrale Dienste, oft schwerfällig (z. B. ESB).
- **Microservices**: Klein, unabhängig, leicht austauschbar.
- Eigene Datenhaltung je Service.
- Kommunikation über REST oder Messaging.
- Beispiel DB: Buchung, Bezahlung und Benachrichtigung sind getrennte Services.

### Beispiel für eine Anwendung mit Microservice-Architektur und REST-Schnittstelle
- Beispiel: DB-Online-Ticketverkauf.
- Services: Auth-Service, Buchungs-Service, Zahlungs-Service, Benachrichtigungs-Service.
- Kommunikation per REST-API (z. B. POST /tickets).
- Jeder Service hat eigene Datenbank und kann unabhängig aktualisiert werden.

---

## 3) Cloud Computing – Einleitung / Überblick

### Cloud definieren
- Bereitstellung von IT-Ressourcen über das Internet (Rechenleistung, Speicher, Software).
- NIST-Definition: Zugriff auf konfigurierbare Ressourcen, schnell und bedarfsabhängig bereitgestellt.
- Servicemodelle: IaaS, PaaS, SaaS, FaaS.

### Bildliche Darstellung der Cloud-Definition
- Cloud = IT aus der Steckdose: Nutzung nach Bedarf, Abrechnung nach Verbrauch.
- Anbieter betreibt Hardware, Sicherheit, Skalierung.

### Argumente gegen Cloud-Verwendung
- Datenschutz / DSGVO / KRITIS-Auflagen.
- Vendor-Lock-in – Anbieterbindung.
- Netzabhängigkeit (Offline-Risiko).
- Kosten bei Dauerlast / Egress-Traffic.
- Komplexität bei Migration alter Systeme.

### Argumente für Cloud-Verwendung
- Schnelle Bereitstellung und Skalierbarkeit.
- Kostenersparnis durch Pay-as-you-go.
- Weniger Wartungsaufwand durch Managed Services.
- Globale Erreichbarkeit, hohe Ausfallsicherheit.
- Schnelle Innovation durch neue Features.

### Prozess beim Praxispartner, der sich per Cloud verbessern lässt
- Prozess: Rechnungsfreigabe und Archivierung.
- Cloud-Lösung: automatischer Workflow mit KI-Belegerkennung.
- Audit-Trails, Zugriffskontrolle (MFA), API-Anbindung an ERP.
- Ergebnis: schnellere Abläufe, bessere Nachvollziehbarkeit.

### Beispiel-Services einer Cloud
- **IaaS** – Virtuelle Maschinen, Storage, Netzwerke.
- **PaaS** – Datenbanken, Queues, Serverless-Plattformen.
- **SaaS** – CRM, Office-Tools, E-Mail-Dienste.
- **FaaS** – Kleine Funktionen auf Abruf (z. B. AWS Lambda).
- **Security-Dienste** – IAM, WAF, KMS.
