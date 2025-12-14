# Kostenberechnung für genutzte Cloud-Services (z. B. AWS)

Um die Kosten für einen Cloud-Service zu berechnen, solltest du folgende Schritte beachten:

1. **Service auswählen**  
   Wähle den genutzten Service aus (z. B. S3, EC2, Lambda, RDS, VPC).

2. **Preismodell prüfen**  
   Jeder Service hat ein eigenes Preismodell. Die wichtigsten findest du auf der offiziellen Preisseite:
   - [AWS Pricing Calculator](https://calculator.aws#/addService)
   - [AWS S3 Pricing](https://aws.amazon.com/de/s3/pricing/)
   - [AWS EC2 Pricing](https://aws.amazon.com/de/ec2/pricing/)
   - [AWS VPC Pricing](https://aws.amazon.com/de/vpc/pricing/)

3. **Nutzungsdaten ermitteln**  
   Ermittle, wie viel du vom Service nutzt:
   - S3: Speicherplatz (GB), Anzahl der Requests, Datenübertragung
   - EC2: Instanztyp, Laufzeit (Stunden), Storage, Netzwerk
   - VPC: Anzahl und Typ der Endpunkte, Datenübertragung, NAT-Gateway-Nutzung

4. **Kosten berechnen**  
   Trage die Werte in den AWS Pricing Calculator ein oder rechne selbst:
   - Beispiel S3:  
     - Speicher: 100 GB x 0,024 USD/GB = 2,40 USD/Monat  
     - GET-Requests: 10.000 x 0,0004 USD = 4 USD  
     - Datenübertragung: 5 GB x 0,09 USD/GB = 0,45 USD  
     - Gesamtkosten: 2,40 + 4 + 0,45 = 6,85 USD/Monat
   - Beispiel EC2:  
     - Instanztyp: t3.medium (ca. 0,0416 USD/Stunde)  
     - Laufzeit: 100 Stunden x 0,0416 USD = 4,16 USD  
     - Storage: 30 GB x 0,10 USD/GB = 3,00 USD  
     - Datenübertragung: 10 GB x 0,09 USD/GB = 0,90 USD  
     - Gesamtkosten: 4,16 + 3,00 + 0,90 = 8,06 USD/Monat
   - Beispiel VPC:  
     - NAT-Gateway: 1 Gateway x 0,045 USD/Stunde x 730 Stunden = 32,85 USD/Monat  
     - Datenübertragung über NAT-Gateway: 10 GB x 0,045 USD/GB = 0,45 USD  
     - VPC-Endpunkte: 2 Interface Endpunkte x 0,01 USD/Stunde x 730 Stunden = 14,60 USD/Monat  
     - Gesamtkosten: 32,85 + 0,45 + 14,60 = 47,90 USD/Monat

5. **Monitoring & Reporting**  
   Nutze die AWS-Konsole oder die CLI, um die tatsächliche Nutzung zu überwachen:
   ```sh
   aws ce get-cost-and-usage --time-period Start=2025-11-01,End=2025-11-30 --granularity MONTHLY --metrics "UnblendedCost"
   ```
   (Voraussetzung: AWS Cost Explorer ist aktiviert)

6. **Tipps zur Kostenoptimierung**
   - Unbenutzte Ressourcen löschen (z. B. alte S3-Buckets, EC2-Instanzen, nicht genutzte VPC-Endpunkte)
   - Storage-Klassen nutzen (z. B. S3 Glacier für Archivierung)
   - Reservierte Instanzen oder Savings Plans für EC2 verwenden
   - NAT-Gateways und VPC-Endpunkte nur bei Bedarf einsetzen
   - Monitoring- und Alarmfunktionen nutzen (z. B. AWS Budgets)

**DIE BEISPIELE WURDEN MIT KI ERSTELLT KÖNNEN ALSO FEHLERHAFT SEIN**

## Beispiel für eine einfache S3-Kostenberechnung

| Nutzung             | Menge   | Preis/Einheit      | Kosten/Monat |
|---------------------|---------|--------------------|--------------|
| Speicherplatz       | 100 GB  | 0,024 USD/GB       | 2,40 USD     |
| GET-Requests        | 10.000  | 0,0004 USD/Request | 4,00 USD     |
| Datenübertragung    | 5 GB    | 0,09 USD/GB        | 0,45 USD     |
| **Gesamt**          |         |                    | **6,85 USD** |

## Beispiel für eine einfache EC2-Kostenberechnung

| Nutzung             | Menge           | Preis/Einheit      | Kosten/Monat |
|---------------------|-----------------|--------------------|--------------|
| Instanz (t3.medium) | 100 Stunden     | 0,0416 USD/Stunde  | 4,16 USD     |
| Storage             | 30 GB           | 0,10 USD/GB        | 3,00 USD     |
| Datenübertragung    | 10 GB           | 0,09 USD/GB        | 0,90 USD     |
| **Gesamt**          |                 |                    | **8,06 USD** |

## Beispiel für eine einfache VPC-Kostenberechnung

| Nutzung                  | Menge         | Preis/Einheit      | Kosten/Monat |
|--------------------------|--------------|--------------------|--------------|
| NAT-Gateway              | 1 x 730 Std  | 0,045 USD/Stunde   | 32,85 USD    |
| Datenübertragung NAT     | 10 GB        | 0,045 USD/GB       | 0,45 USD     |
| VPC Interface Endpunkte  | 2 x 730 Std  | 0,01 USD/Stunde    | 14,60 USD    |
| **Gesamt**               |              |                    | **47,90 USD**|

Weitere Infos:  
- [AWS Pricing Calculator](https://calculator.aws.amazon.com/)
- [AWS Kostenmanagement](https://aws.amazon.com/de/aws-cost-management/)

## Kostenberechnung im Kontext eines Großkonzerns wie der Deutschen Bahn

Gerade bei einem Großkonzern wie der Deutschen Bahn mit tausenden Nutzern und vielen IT-Systemen ist die Kostenkontrolle besonders wichtig. Hier einige Besonderheiten und Tipps:

- **Skaleneffekte**: Große Nutzerzahlen führen zu hohen Datenmengen und vielen Requests. Die Kosten steigen linear mit der Nutzung (z. B. Speicherplatz, API-Aufrufe, Datenübertragung).
- **Zentrale Abrechnung**: Die DB nutzt zentrale AWS Accounts und Kostenstellen, um die Ausgaben einzelnen Projekten oder Abteilungen zuzuordnen.
- **Monitoring & Reporting**: Es werden automatisierte Reports und Dashboards genutzt, um die Kostenentwicklung zu überwachen und frühzeitig auf Ausreißer zu reagieren.
- **Optimierungspotenzial**: Durch Reserved Instances, Savings Plans und gezielte Löschung ungenutzter Ressourcen können Millionenbeträge eingespart werden.
- **Governance & Richtlinien**: Es gibt feste Vorgaben, wie und wann Ressourcen angelegt und gelöscht werden dürfen, um Kosten zu begrenzen.
- **Praxisbeispiel**:  
  - Ein S3-Bucket für Fahrplandaten wird von 10.000 Nutzern täglich abgefragt.  
  - Die EC2-Instanzen für die Fahrplanauskunft laufen rund um die Uhr und müssen hochverfügbar sein.  
  - VPCs werden genutzt, um verschiedene Anwendungen und Daten sicher voneinander zu trennen.

**Fazit:**  
Für Konzerne wie die Deutsche Bahn ist es entscheidend, Cloud-Kosten regelmäßig zu analysieren, zu optimieren und transparent zu machen. Tools wie der AWS Pricing Calculator, Cost Explorer und eigene Dashboards sind dafür unverzichtbar.