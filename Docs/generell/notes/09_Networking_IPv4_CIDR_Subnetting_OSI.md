# Networking: IPv4, CIDR, Subnetting, OSI (ausführlich)

## Netzwerk Definition
- Computer Netzwerk = zwei oder mehr Geräte, verbunden zur Kommunikation.
- kann logisch in Subnetze geteilt werden.

Netzwerkgeräte:
- Switch (Layer 2)
- Router (Layer 3)

---

## IPv4 Grundlagen
- IPv4 Adresse = 32 Bit = 4 Bytes
- Schreibweise: a.b.c.d (0-255)

Private IPv4 Bereiche (klassisch)
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

---

## CIDR Notation
- /n = Anzahl der Netzwerkbits
- Hostbits = 32 - n

Beispiel /24:
- Hostbits = 8
- Adressen = 2^8 = 256
- nutzbar (klassisch) = 254 (Netz + Broadcast nicht nutzbar)

Beispiel /16:
- Hostbits = 16
- Adressen = 65536

---

## Subnetting - Standard-Rechnung
Schritte:
1) VPC/Netz hat Präfix (z. B. /16)
2) Subnetz hat längeren Präfix (z. B. /20)
3) Subnetz-Anzahl = 2^(Subnetzbits)
   - Subnetzbits = /20 - /16 = 4
   - 2^4 = 16 Subnetze
4) Hosts pro Subnetz = 2^(Hostbits_subnet) - 2 (klassisch)
   - Hostbits_subnet = 32 - 20 = 12
   - 2^12 = 4096, nutzbar 4094 (klassisch)

AWS Sonderregel:
- pro Subnetz 5 IPs reserviert
- nutzbar = 2^(Hostbits) - 5

---

## Beispielrechnung (prüfungsnah)
VPC 10.17.0.0/16, Subnetze /20:
- Subnetze: 16
- IPs pro Subnetz: 4096
- nutzbar in AWS: 4096 - 5 = 4091

---

## Subnetzmaske (klassisch)
- /24 = 255.255.255.0
- /16 = 255.255.0.0
- /20 = 255.255.240.0

---

## Typische Prüfungsfalle: Überlappende Subnetze
- Subnetze dürfen sich NICHT überschneiden.
- Wenn AWS meldet "overlap":
  - du hast einen CIDR gewählt, der bereits in einem anderen Subnetz liegt.

Wie erkenne ich gültige Startadressen?
- Blockgröße = 256 - Wert im relevanten Oktett der Maske
- Bei /20 ist Maske im 3. Oktett 240:
  - Blockgröße = 256 - 240 = 16
  - gültige Startwerte im 3. Oktett: 0,16,32,48,64,...

Beispiel:
- 10.17.16.0/20 ist gültig
- 10.17.1.0/20 ist NICHT gültig (weil 1 nicht in 0,16,32,...)

---

## OSI Modell (prüfungsrelevant)
- Layer 7 Application: HTTP/HTTPS, DNS
- Layer 6 Presentation: Format/Encoding, Verschlüsselungskonzepte
- Layer 5 Session: Sitzungssteuerung
- Layer 4 Transport: TCP/UDP
- Layer 3 Network: IP, Routing
- Layer 2 Data Link: MAC, Switches
- Layer 1 Physical: Kabel, Signale

Beispiel:
- HTTPS nutzt:
  - Layer 7 (HTTP)
  - Layer 4 (TCP)
  - Layer 3 (IP)
