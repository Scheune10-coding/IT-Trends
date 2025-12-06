# IT-TRENDS – KONTROLLFRAGEN – MUSTERLÖSUNG

---

# **1) IT-Trends – Einleitung / Überblick**

## **Frage: Mindestens 6 IT-Trends benennen und kurz erläutern.**

* **Cloud Computing**  
  Bereitstellung von IT-Ressourcen über das Internet. Skalierbar, flexibel, Pay-as-you-go.

* **Industrie 4.0**  
  Vernetzte Maschinen, Sensorik, Automatisierung. Ziel: Effizienz, Predictive Maintenance, Echtzeitdaten.

* **Internet of Things (IoT)**  
  Geräte, Infrastruktur & Fahrzeuge senden kontinuierlich Sensordaten → Basis für Echtzeitüberwachung.

* **Blockchain**  
  Kryptografisch verkettete Einträge, unveränderbar und transparent. Kein Vertrauen in eine zentrale Stelle nötig.

* **Künstliche Intelligenz (KI)**  
  Systeme lernen Muster und treffen Vorhersagen. Einsatz für Prognosen, Bilderkennung, Automatisierung.

* **Microservices**  
  Anwendungen bestehen aus kleinen, unabhängig deploybaren Diensten. Skalierbar, modular.

* **Edge Computing**  
  Datenverarbeitung direkt am Gerät (z. B. Zug). Sehr geringe Latenz, funktioniert ohne Internet.

**DB-Praxisbeispiel Blockchain:**  
Blockchain dokumentiert **grenzüberschreitende Zugfahrten** fälschungssicher.  
Grenzübertritt → kryptografischer Eintrag → eindeutiger Verantwortungsübergang.

---

## **Frage: Unterschied Cloud vs. Edge Computing.**

* **Cloud Computing**
  - zentrale Rechenzentren
  - hohe Rechenleistung
  - ideal für Analyse, Speicherung, KI-Training

* **Edge Computing**
  - Verarbeitung am Gerät
  - extrem geringe Latenz
  - funktioniert offline

**DB-Beispiel:**  
Edge bewertet Sensordaten im Zug → Cloud analysiert Langzeittrends und trainiert KI-Modelle.

---

## **Frage: Anwendungsfälle für KI.**

* Bilderkennung in Werkstätten (Verschleißanalyse)
* Ticket- und Dokumentenauswertung
* Verspätungs- und Auslastungsprognosen
* Chatbots im Kundenservice
* Automatisierte Wartungsplanung

---

## **Frage: Grundprinzipien der IT-Sicherheit.**

* **CIA-Triade:**
  - Confidentiality – Vertraulichkeit
  - Integrity – Integrität
  - Availability – Verfügbarkeit

* **AAA:** Authentication, Authorization, Accounting

* **Zero Trust:** kein implizites Vertrauen

* **Defense in Depth:** mehrere Schutzschichten

* **DB-Bezug:** MFA, Verschlüsselung, Rollen & Rechte, BSI-Grundschutz

---

# **2) Cloud Computing & REST-Schnittstellen**

## **Frage: Eine REST-Schnittstelle auf der Kommandozeile bedienen.**

**GET:**
```sh
curl -i https://api.example.com/v1/trains/ICE123
```

**POST:**
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"status":"ready"}' https://api.example.com/v1/trains
```

**PUT:**
```sh
curl -X PUT -H "Content-Type: application/json" \
     -d '{"status":"in_service"}' https://api.example.com/v1/trains/ICE123
```

**PATCH:**
```sh
curl -X PATCH -H "Content-Type: application/json" \
     -d '{"status":"delayed"}' https://api.example.com/v1/trains/ICE123
```

**DELETE:**
```sh
curl -X DELETE https://api.example.com/v1/trains/ICE123
```

**Tipps:**  
`-i` Header anzeigen, `-v` Debug, `-sS` Fehler sichtbar, Output ruhig.

---

## **Frage: Aufbau einer REST-Schnittstelle.**

* Ressourcenorientierte URLs
* HTTP-Methoden: GET / POST / PUT / PATCH / DELETE
* JSON als Standardformat
* Statuscodes: 200, 201, 400, 404, 500
* Authentifizierung via Bearer Token
* Versionierung: /v1 oder per Header

---

## **Frage: Vorteile/Eigenschaften von REST.**

* Einfach & standardisiert
* Stateless → sehr gute Skalierung
* Caching möglich
* Lose gekoppelte Architektur
* Breite Tool-Unterstützung

---

## **Frage: Microservices vs. SOA.**

* **SOA:** große Dienste, zentralisiert, oft schwerfällig
* **Microservices:** klein, leicht, unabhängig deploybar
* eigene Datenhaltung je Service
* Kommunikation über REST / Messaging

**DB-Beispiel:**  
Ticketkauf, Zahlung, Benachrichtigung sind getrennte Services.

---

## **Frage: Beispielanwendung als Microservices + REST.**

**DB-Online-Ticketverkauf**

* Services: Auth, Ticket, Payment, Notification
* REST-Beispiele:  
  `POST /tickets` erstellt Ticket  
  `GET /tickets/{id}` liest Ticket
* Jeder Service unabhängig skalierbar

---

# **3) Cloud Computing – Überblick**

## **Frage: Cloud definieren.**

* IT-Ressourcen über Netzwerk bereitgestellt
* flexibel, elastisch skalierbar
* Abrechnung nach Nutzung
* Servicemodelle: IaaS, PaaS, SaaS, FaaS

---

## **Frage: Bildliche Darstellung.**

Cloud = „Strom aus der Steckdose“  
Man nutzt Ressourcen ohne Geräte/Hardware selbst zu besitzen.

---

## **Frage: Argumente gegen Cloud.**

* Datenschutz, DSGVO, KRITIS
* Abhängigkeit von Anbietern
* Netzabhängigkeit
* mögliche Kosten bei Dauerlast
* Altsystemmigration komplex

---

## **Frage: Argumente für Cloud.**

* hohe Skalierbarkeit
* keine eigene Hardware
* schnelle Bereitstellung
* moderne Dienste (KI, Analytics)
* hohe Ausfallsicherheit

---

## **Frage: Verbessern eines Prozesses (DB).**

**Beispiel: Rechnungsfreigabe**

* digitaler Workflow
* automatische Belegerkennung (KI)
* revisionssichere Speicherung
* MFA + Audit-Trails
* Integration ins ERP

---

## **Frage: Beispiel-Services einer Cloud.**

* IaaS: EC2, EBS, VPC
* PaaS: RDS, SQS, Lambda
* SaaS: Office 365, Salesforce
* FaaS: AWS Lambda

---

# **4) AWS – CLI, Skripte, Preisberechnung**

## **Frage: Datei aus einem S3-Bucket herunterladen.**

```sh
aws s3 cp s3://BUCKET/DATEI .
```

---

## **Frage: Skript mit Parametern (Bucket, Datei).**

**Bash:**
```bash
bucket=$1
file=$2
aws s3 cp s3://$bucket/$file ~/Downloads/$file
```

---

## **Frage: Kosten berechnen.**

**Beispiel: S3 Glacier Deep Archive**

* 2 TB gespeichert → ca. 3.72 USD / Monat
* 100 GB Upload → ca. 0.62 USD
* **Gesamt: ca. 4.34 USD / Monat**

---

## **Frage: Drei Cloud-Service-Modelle.**

* IaaS → komplette Infrastruktur
* PaaS → Plattform (DB, Apps)
* SaaS → fertige Software

---

# **5) AWS – VPC, Netzwerke, EC2**

## **Frage: VPC erstellen.**

```sh
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```

---

## **Frage: Bedeutung des CIDR-Werts.**

`10.0.0.0/16`  
→ 16 Bit Netzwerkanteil  
→ 65.536 IP-Adressen verfügbar

---

## **Frage: Subnetze erstellen, IP-Bedarf bestimmen.**

Beispiel: 4 Subnetze  
→ 2 zusätzliche Bits  
→ `/18` pro Subnetz

---

## **Frage: Routing + Internetzugriff einrichten.**

**Public Subnet:**
* IGW verbinden
* Route 0.0.0.0/0 → IGW
* EC2 mit Public IP

**Private Subnet:**
* Route 0.0.0.0/0 → NAT Gateway

---

## **Frage: EC2-Instanz mit Hello PUBLIC / PRIVATE.**

```bash
#!/bin/bash
yum install -y httpd
echo "Hello PUBLIC" > /var/www/html/index.html
systemctl enable httpd
systemctl start httpd
```

---

## **Frage: Sicherheitsgruppen.**

**Public:**
* Port 80 → 0.0.0.0/0
* Outbound alles frei

**Private:**
* nur interner Zugriff erlaubt
* Outbound über NAT

---

## **Frage: Nutzen im Unternehmen (DB).**

* strikte Trennung kritischer Systeme
* bessere Sicherheit (Subnetze, SGs)
* klar definierte Zugriffswege
* effizienter Betrieb durch Automatisierung

---
