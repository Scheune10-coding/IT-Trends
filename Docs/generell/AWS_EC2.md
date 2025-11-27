# AWS EC2 – Grundlagen und Überblick

---

#### Was ist AWS EC2?

**Amazon Elastic Compute Cloud (EC2)** ist ein zentraler Cloud-Service von AWS, mit dem du virtuelle Server (Instanzen) flexibel bereitstellen, betreiben und skalieren kannst. EC2 ermöglicht es, Rechenleistung nach Bedarf zu nutzen – von kleinen Testsystemen bis zu großen Produktionsumgebungen.

---

#### Wichtige Eigenschaften von EC2

- **Virtuelle Maschinen:** Verschiedene Instanztypen für unterschiedliche Anforderungen (CPU, RAM, Storage).
- **Flexible Skalierung:** Instanzen können jederzeit gestartet, gestoppt oder angepasst werden.
- **Betriebssystemwahl:** Unterstützung für Linux, Windows und weitere Images.
- **Netzwerkintegration:** Einbindung in VPCs, Subnetze und Sicherheitsgruppen.
- **Storage:** Nutzung von EBS (Elastic Block Store), Instance Store und S3.
- **Automatisierung:** Starten und Verwalten per AWS CLI, SDKs oder CloudFormation.
- **Zugriffssteuerung:** SSH-Schlüssel für Linux, RDP für Windows, IAM-Rollen für Berechtigungen.

---

#### Typische Anwendungsfälle

- Webserver und Anwendungsserver
- Datenbankserver
- Entwicklungs- und Testumgebungen
- Batch-Verarbeitung und Big Data
- Hosting von APIs und Microservices

---

#### Wichtige EC2-Befehle mit AWS CLI

```sh
# Instanz starten
aws ec2 run-instances --image-id ami-xxxxxxxx --instance-type t2.micro --key-name MeinKey --security-group-ids sg-xxxxxxx --subnet-id subnet-xxxxxxx

# Liste aller Instanzen anzeigen
aws ec2 describe-instances

# Instanz stoppen
aws ec2 stop-instances --instance-ids i-xxxxxxxxxxxx

# Instanz starten
aws ec2 start-instances --instance-ids i-xxxxxxxxxxxx

# Instanz beenden (löschen)
aws ec2 terminate-instances --instance-ids i-xxxxxxxxxxxx
```

---

#### Kosten und Preismodelle

- Abrechnung nach Laufzeit (Stunden/Sekunden) und Instanztyp
- Kosten für Storage (EBS), Datenübertragung und zusätzliche Features
- Sparmöglichkeiten durch Reserved Instances, Spot Instances und Savings Plans

Weitere Infos:  
- [AWS EC2 Dokumentation](https://docs.aws.amazon.com/ec2/index.html)
- [AWS EC2 Pricing](https://aws.amazon.com/de/ec2/pricing/)

---