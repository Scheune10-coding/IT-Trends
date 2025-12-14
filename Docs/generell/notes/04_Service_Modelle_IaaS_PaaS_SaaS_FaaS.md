# Cloud Service-Modelle (HaaS/IaaS/PaaS/SaaS/FaaS) – ausführlich

## Grundidee der "Schichtenpyramide"
- Unten: Hardware
- Dann: Infrastruktur (VMs, Netz, Storage)
- Dann: Plattform (OS, Laufzeit, DB)
- Oben: Software (fertige Anwendung)

Je weiter oben du einkaufst, desto weniger musst du selbst verwalten.

---

## HaaS (Hardware as a Service)
- Du mietest Hardware-Ressourcen (selten als Begriff in Public-Cloud-Prüfungen, aber als Konzept).
- Anbieter stellt physische Maschinen/Komponenten bereit.

---

## IaaS (Infrastructure as a Service)
- Du bekommst virtuelle Infrastruktur:
  - VM
  - Netzwerk
  - Storage
- Du verwaltest selbst:
  - Betriebssystem
  - Updates
  - Anwendungen

Beispiel:
- AWS EC2 + EBS
- Du installierst selbst Apache/Nginx, konfigurierst Firewall (SG) etc.

---

## PaaS (Platform as a Service)
- Anbieter betreibt:
  - OS
  - Laufzeitumgebung
  - oft DB/Runtime
- Du bringst:
  - Code + Konfiguration

Beispiel:
- Datenbank als Service (z. B. AWS RDS)
  - du musst keinen DB-Server patchen, sondern nutzt DB direkt

---

## SaaS (Software as a Service)
- Fertige Software, sofort nutzbar
- Anbieter macht alles (Updates, Betrieb, Skalierung)

Beispiele:
- Office 365
- Google Workspace
- Salesforce

---

## FaaS (Function as a Service) / Serverless Functions
- Du schreibst Funktionen, die auf Events reagieren.
- Abrechnung nach Ausführung/Rechenzeit (nicht "pro Anfrage", sondern nach tatsächlicher Compute-Nutzung).
- Event-basiert.

Beispiel:
- AWS Lambda verarbeitet Upload-Event aus S3:
  - sobald Datei hochgeladen: Lambda erzeugt Thumbnail

Typische Vorteile:
- keine Serververwaltung
- sehr gut für unregelmäßige Last

Typische Grenzen:
- Laufzeitlimits, Cold Starts, Debugging schwieriger

---

## Prüfungsfrage aus deinen Notizen: Einordnung
"Linuxrechner mit Webserver, der zwei Zahlen addiert - wo wird das eingeordnet?"
- Als IaaS, wenn du selbst eine VM betreibst und Webserver installierst.
- Als PaaS, wenn du nur Code deployest und Plattform macht den Rest.
- Als SaaS wäre es nur, wenn es eine fertige App ist, die du einfach nutzt.
