# Microservices & REST-API – Grundlagen

## Microservices

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

---

## REST-API

REST (Representational State Transfer) ist ein Architekturprinzip für Web-Schnittstellen.

### Prinzipien
- **Ressourcenorientierte URLs:** Jede Entität (z. B. Nutzer, Ticket) hat eine eindeutige URL.

**GET (lesen):**
```sh
curl -i https://api.example.com/v1/trains/ICE123
```

**POST (erstellen):**
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"status":"ready"}' https://api.example.com/v1/trains
```

**PUT (ersetzen):**
```sh
curl -X PUT -H "Content-Type: application/json" \
     -d '{"status":"in_service"}' https://api.example.com/v1/trains/ICE123
```

**PATCH (Eintrag teilweise ändern):**
```sh
curl -X PATCH -H "Content-Type: application/json" \
     -d '{"status":"delayed"}' https://api.example.com/v1/trains/ICE123
```

**DELETE (entfernen):**
```sh
curl -X DELETE https://api.example.com/v1/trains/ICE123
```

**Tipps:**  
`-i` Header anzeigen, `-v` Debug, `-sS` Fehler sichtbar, Output ruhig.

---

- **Datenformat:** Meist JSON, manchmal XML.
- **Statuscodes:**  
  - 200 OK (Erfolg)
  - 201 Created (Erstellt)
  - 400 Bad Request (Fehlerhafte Anfrage)
  - 404 Not Found (Nicht gefunden)
  - 500 Internal Server Error (Serverfehler)

### Beispiel-Endpoint
```http
GET /api/v1/users/123
```
Liefert die Daten des Nutzers mit der ID 123 als JSON.

### Vorteile/Eigenschaften von REST

* Einfach & standardisiert
* Stateless → sehr gute Skalierung
* Caching möglich
* Lose gekoppelte Architektur
* Breite Tool-Unterstützung

### Authentifizierung
- **OAuth2:** Token-basierte Authentifizierung, z. B. für Single Sign-On.
- **JWT (JSON Web Token):** Token enthält Nutzerinformationen und wird bei jedem Request mitgeschickt.

### API-Gateway
- Vermittelt Anfragen an die richtigen Microservices.
- Übernimmt Authentifizierung, Ratenbegrenzung, Logging und Monitoring.

### Dokumentation
- **Swagger/OpenAPI:** Automatische Dokumentation und Testbarkeit der API-Endpunkte.

---

## Beispiel für Microservices-Kommunikation

1. **User-Service:** Verwalten von Nutzerdaten
2. **Order-Service:** Verwalten von Bestellungen
3. **Payment-Service:** Zahlungsabwicklung

Ein Client bestellt ein Produkt:
- POST /api/v1/orders → Order-Service
- Order-Service ruft Payment-Service per REST auf
- Nach erfolgreicher Zahlung wird die Bestellung bestätigt

---

## Sicherheit

- Alle REST-Endpunkte sollten über HTTPS erreichbar sein.
- Authentifizierung und Autorisierung sind Pflicht.
- Eingaben validieren, um Angriffe (z. B. Injection) zu verhindern.

---