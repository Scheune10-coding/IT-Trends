# IT-Sicherheit + Kryptografie + HTTPS + Mail (ausführlich)

## IT-Sicherheit ist "Chef-Sache"
- Geschäftsführung ist verantwortlich (nicht "die IT").
- In Unternehmen oft Rollen:
  - DSB = Datenschutzbeauftragter
  - ISB = Informationssicherheitsbeauftragter
  - Mitarbeiter = wichtigster Faktor (Phishing etc.)

---

## Grundschutzziele (Schutzziele)
- Vertraulichkeit
  - nur Berechtigte dürfen lesen
- Integrität
  - Daten dürfen nicht unbemerkt verändert werden
- Verfügbarkeit
  - Systeme/Daten müssen erreichbar sein

Weitere Schutzziele (häufig genannt):
- Authentizität
  - Echtheit von Absender/Partner
- Nichtabstreitbarkeit
  - jemand kann nicht glaubhaft abstreiten, etwas gesendet zu haben
- Verlässlichkeit

Beispiele:
- Vertraulichkeit: Patientendaten verschlüsseln
- Integrität: Checksums/Signaturen verhindern Manipulation
- Verfügbarkeit: Redundanz + Backups

---

## Kryptografie: Symmetrisch vs. Asymmetrisch
### Symmetrisch
- gleicher Key für Ver- und Entschlüsselung
- schnell
- Problem: Key muss sicher ausgetauscht werden

Beispiel:
- AES für Datenübertragung nach erfolgreichem TLS-Handshake

### Asymmetrisch
- Public Key (öffentlich) + Private Key (geheim)
- nutzt man oft für:
  - sicheren Schlüsselaustausch
  - Signaturen
- langsamer als symmetrisch

Beispiel:
- Server hat Zertifikat mit Public Key, Client prüft Identität

---

## Hash + Signatur
- Hashfunktion erzeugt "Fingerabdruck" (z. B. SHA-256).
- Signatur:
  - Hash wird mit Private Key signiert (verschlüsselt)
  - Empfänger prüft mit Public Key

Wichtig:
- MD5 gilt heute als unsicher.
- SHA-256 oder SHA-512 sind moderne Standards.

---

## HTTPS (TLS) – was passiert wirklich?
- HTTPS = HTTP über TLS/SSL
- Ziele:
  - Vertraulichkeit (Verschlüsselung)
  - Integrität (Manipulation erkennen)
  - Authentizität (Server ist echt)

### Grober Ablauf (Handshake)
- Client verbindet, Server schickt Zertifikat
- Client prüft:
  - ist Zertifikat gültig?
  - passt Domain?
  - vertrauenswürdige CA?
- Dann wird ein gemeinsamer Sitzungsschlüssel ausgehandelt (asymmetrisch)
- Danach läuft die eigentliche Datenübertragung symmetrisch (z. B. AES)

Merksatz:
- Asymmetrisch für Start/Schlüssel, symmetrisch für Daten.

---

## E-Mail-Verschlüsselung (S/MIME, PGP)
### S/MIME
- nutzt Zertifikate (X.509)
- typischer in Unternehmen (PKI)

### PGP
- Schlüsselpaare selbst erzeugt, Austausch über Keyserver oder direkt

Gemeinsamkeiten:
- Vertraulichkeit: Empfänger-Public-Key verschlüsselt
- Signatur: Absender signiert mit Private Key, Empfänger prüft mit Public Key

---

## Praxis-Beispiel (prüfungsnah)
- Login-Formular:
  - immer HTTPS, sonst Passwort im Klartext übertragbar (HTTP ist unverschlüsselt)
- API-Aufruf zwischen Services:
  - intern oft mTLS oder mindestens HTTPS + Tokens
