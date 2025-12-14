# Microservices, 3-Schichtenmodell, REST (ausführlich)

## 3-Schichtenmodell (klassisch)
- UI (Präsentation)
  - z. B. Web-Frontend
- Logik (Business-Logik)
  - Services/Anwendungslogik
- Datenhaltung
  - Datenbank

Zweck:
- klare Trennung von Verantwortlichkeiten
- einfacher zu warten und zu testen

---

## Microservices – Definition

Microservices sind kleine, unabhängige Dienste, die zusammen eine Anwendung bilden. Jeder Service hat eine eigene Datenbank und Schnittstelle.  
Sie kommunizieren meist über Netzwerkprotokolle (z. B. HTTP, gRPC) und tauschen Daten über APIs aus.

### Architektur
- Jeder Microservice ist eigenständig deploybar und kann unabhängig entwickelt, getestet und skaliert werden.
- Services sind lose gekoppelt: Änderungen an einem Service beeinflussen andere nicht direkt.
- Jeder Service verwaltet seine eigenen Daten (Database per Service Pattern).
- Kommunikation erfolgt oft über REST-APIs oder Messaging (z. B. RabbitMQ, Kafka).

### Vorteile
- **Skalierbarkeit:** Services können unabhängig voneinander skaliert werden.
- **Unabhängige Entwicklung & Deployment:** Teams können parallel an verschiedenen Services arbeiten.
- **Fehlertoleranz:** Fällt ein Service aus, bleibt die Gesamtanwendung oft funktionsfähig.
- **Technologievielfalt:** Jeder Service kann in einer anderen Programmiersprache oder mit anderen Tools entwickelt werden.

### Herausforderungen
- Komplexeres Monitoring und Logging
- Verteilte Transaktionen sind schwieriger
- Netzwerkkommunikation muss abgesichert werden (z. B. Authentifizierung, Verschlüsselung)

### Eigenschaften (aus Notizen)
- sehr klein, überschaubar, einfach zu ersetzen
- voneinander unabhängig (auch in verschiedenen Sprachen möglich)
- dezentral organisiert
- horizontal skalierbar
- Logging wichtig (Fehler + Zeitstempel)
- gemeinsame Basisdienste oft zentral:
  - Authentifizierung
  - Autorisierung
  - Kryptografie

---

## Kommunikation zwischen Services

### HTTP Request
- Kommunikation oft über HTTP/HTTPS.
- REST-Schnittstellen sind häufigster Standard im Unterrichtskontext.

### Load Balancer
- verteilt Anfragen auf mehrere Instanzen eines Services
- verhindert Überlastung einzelner Knoten
- erhöht Verfügbarkeit

Beispiel:
- Service A läuft 3-mal parallel
- Load Balancer verteilt Requests round-robin oder nach Auslastung

---

## Monolith (Gegenstück)
- eine große Anwendung, alle Teile verwoben
- Vorteil:
  - am Anfang einfacher
- Nachteil:
  - später schwer zu ändern/skalieren
- Praxis-Ansatz:
  - oft startet man monolithisch und schneidet später Services heraus (Strangler Pattern als Begriff optional)

---

## REST (Representational State Transfer)

REST ist ein Architekturprinzip für Web-Schnittstellen. Es ist kein Protokoll und kein Standard, sondern ein Architekturstil.

### Prinzipien
- **Ressourcenorientierte URLs:** Jede Entität (z. B. Nutzer, Ticket) hat eine eindeutige URL.

### HTTP Methoden + typische Bedeutung
- GET: lesen (sollte keine Änderungen machen)
- POST: erstellen/auslösen (nicht idempotent)
- PUT: ersetzen (idempotent)
- PATCH: teilweise ändern
- DELETE: löschen (idempotent)

**Beispiel-Requests:**
```sh
curl -i https://api.example.com/v1/trains/ICE123
curl -X POST -H "Content-Type: application/json" -d '{"status":"ready"}' https://api.example.com/v1/trains
curl -X PUT -H "Content-Type: application/json" -d '{"status":"in_service"}' https://api.example.com/v1/trains/ICE123
curl -X PATCH -H "Content-Type: application/json" -d '{"status":"delayed"}' https://api.example.com/v1/trains/ICE123
curl -X DELETE https://api.example.com/v1/trains/ICE123
```

**Tipps:**  
`-i` Header anzeigen, `-v` Debug, `-sS` Fehler sichtbar, Output ruhig.

- **Datenformat:** Meist JSON, manchmal XML.
- **Statuscodes:**  
  - 200 OK (Erfolg)
  - 201 Created (Erstellt)
  - 400 Bad Request (Fehlerhafte Anfrage)
  - 404 Not Found (Nicht gefunden)
  - 500 Internal Server Error (Serverfehler)

---

### Beispiel-Endpoint
```http
GET /api/v1/users/123
```
Liefert die Daten des Nutzers mit der ID 123 als JSON.

---

### Vorteile/Eigenschaften von REST

* Einfach & standardisiert
* Stateless → sehr gute Skalierung
* Caching möglich
* Lose gekoppelte Architektur
* Breite Tool-Unterstützung

---

### Bedingungen für REST (prüfungsrelevant)
I) Client-Server-Modell  
II) Zustandslos (Stateless)  
III) Caching erlaubt  
IV) Einheitliche Schnittstelle  
V) Schichtenbasiert  
VI) Code on Demand (optional)  

---

### Authentifizierung
- **OAuth2:** Token-basierte Authentifizierung, z. B. für Single Sign-On.
- **JWT (JSON Web Token):** Token enthält Nutzerinformationen und wird bei jedem Request mitgeschickt.

### API-Gateway
- Vermittelt Anfragen an die richtigen Microservices.
- Übernimmt Authentifizierung, Ratenbegrenzung, Logging und Monitoring.

### Dokumentation
- **Swagger/OpenAPI:** Automatische Dokumentation und Testbarkeit der API-Endpunkte.

---

### Beispiel für Microservices-Kommunikation

1. **User-Service:** Verwalten von Nutzerdaten  
2. **Order-Service:** Verwalten von Bestellungen  
3. **Payment-Service:** Zahlungsabwicklung  

Ein Client bestellt ein Produkt:
- POST /api/v1/orders → Order-Service
- Order-Service ruft Payment-Service per REST auf
- Nach erfolgreicher Zahlung wird die Bestellung bestätigt

**Alternative robustere Variante:**
- asynchron via Message Queue (RabbitMQ/Kafka)
- Vorteil: weniger Kaskadenfehler, bessere Entkopplung

---

### Sicherheit

- Alle REST-Endpunkte sollten über HTTPS erreichbar sein.
- Authentifizierung und Autorisierung sind Pflicht.
- Eingaben validieren, um Angriffe (z. B. Injection) zu verhindern.

---