# AWS VPC – Grundlagen und Planung

---

## Was ist eine AWS VPC?

Eine **Virtual Private Cloud (VPC)** ist ein isoliertes Netzwerk in der AWS-Cloud, das du selbst konfigurieren kannst. Es funktioniert wie ein eigenes Rechenzentrum, in dem du Subnetze, Routing, Firewalls und Internetzugänge nach deinen Anforderungen einrichtest.

Mit einer VPC kannst du:
- Ressourcen (z. B. EC2-Instanzen, Datenbanken) sicher voneinander trennen
- Private und öffentliche Subnetze anlegen
- Netzwerkzugriffe und Datenströme kontrollieren
- VPN-Verbindungen zu deinem Unternehmensnetzwerk herstellen
- Sicherheitsgruppen und Netzwerk-ACLs für feingranulare Zugriffskontrolle nutzen

**Typische Komponenten einer VPC:**
- **Subnetze:** Teilbereiche des VPC-Netzes, z. B. für öffentliche und private Server
- **Internet Gateway:** Ermöglicht den Zugang zum Internet für Ressourcen im öffentlichen Subnetz
- **Route Tables:** Regeln, wie Datenpakete innerhalb der VPC und ins Internet geleitet werden
- **Security Groups & NACLs:** Firewall-Regeln für Instanzen und Subnetze
- **VPC Endpoints:** Direkte Verbindung zu AWS-Diensten ohne Internet

**Vorteile einer VPC:**
- Hohe Sicherheit und Isolation
- Flexible Netzwerkkonfiguration
- Skalierbarkeit und Integration mit anderen AWS-Diensten
- Kontrolle über IP-Adressbereiche und Routing

---

## Wie berechnet man die Anzahl der Subnetze und Rechner (Hosts) in einer VPC?

### Beispiel:
- **VPC:** 10.17.0.0/16  
- **Subnetz:** 10.17.128.0/20

**Schritt 1: Anzahl der möglichen Subnetze**
- Die VPC hat das Netz **10.17.0.0/16**.  
- Das Subnetz hat **/20**.
- Ein /16-Netz hat 2^(32-16) = 65.536 IP-Adressen.
- Ein /20-Subnetz hat 2^(32-20) = 4.096 IP-Adressen.
- Unterschied der Präfixe: 20 - 16 = 4
- Anzahl der möglichen /20-Subnetze: 2^4 = **16 Subnetze**

**Schritt 2: Anzahl der Hosts pro Subnetz**
- Ein /20-Subnetz hat 4.096 IP-Adressen.
- Davon sind 5 Adressen reserviert (Netzadresse, Broadcast, 3 für AWS intern).
- **Maximal nutzbare Hosts pro Subnetz:** 4.096 - 5 = **4.091 Rechner**

**Zusammenfassung:**
- In einer VPC mit 10.17.0.0/16 kannst du **16 Subnetze** mit jeweils /20 anlegen.
- Jedes /20-Subnetz bietet Platz für **4.091 EC2-Instanzen** (Rechner).

**Formeln:**
- **Anzahl Subnetze:** 2^(Subnetz-Präfix - VPC-Präfix)
- **Anzahl Hosts pro Subnetz:** 2^(32-Subnetz-Präfix) - 5

---

## Beispielrechnung für andere Subnetzgrößen

| Subnetzgröße | Hosts pro Subnetz (2^(32-Präfix)-5) |
|--------------|-------------------------------------|
| /24          | 251                                 |
| /20          | 4.091                               |
| /16          | 65.531                              |

---

## Praxis: Subnetze sinnvoll planen

- Öffentliche Subnetze für Webserver, private Subnetze für Datenbanken
- Nicht zu große Subnetze wählen, um IP-Adressen effizient zu nutzen
- AWS reserviert immer 5 IPs pro Subnetz
- Trennung von Entwicklungs-, Test- und Produktionsumgebungen durch eigene Subnetze
- Nutzung von Security Groups und NACLs für zusätzliche Sicherheit

---

## Weitere hilfreiche AWS VPC Ressourcen

- [AWS VPC Dokumentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS VPC Pricing](https://aws.amazon.com/de/vpc/pricing/)
- [AWS VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html)

---