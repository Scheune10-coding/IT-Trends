# E-Mail-Verschlüsselung & HTTPS – Grundlagen

## E-Mail-Verschlüsselung – Wie funktioniert das technisch?

E-Mail-Verschlüsselung schützt Nachrichten vor dem Zugriff Dritter. Es gibt zwei Hauptverfahren:

### S/MIME (Secure/Multipurpose Internet Mail Extensions)
- Nutzt digitale Zertifikate (X.509).
- Jeder Nutzer besitzt ein Schlüsselpaar (privat/öffentlich).
- Der öffentliche Schlüssel wird an Kommunikationspartner verteilt.
- Beim Versand wird die E-Mail mit dem öffentlichen Schlüssel des Empfängers verschlüsselt.
- Nur der Empfänger kann die Nachricht mit seinem privaten Schlüssel entschlüsseln.
- Die Signatur (Hash der Nachricht, mit privatem Schlüssel verschlüsselt) garantiert die Integrität und Authentizität.

### PGP (Pretty Good Privacy)
- Funktioniert ähnlich wie S/MIME, aber mit selbst erzeugten Schlüsselpaaren.
- Öffentlicher Schlüssel wird ausgetauscht (z. B. per Mail, Keyserver).
- Nachricht wird mit öffentlichem Schlüssel des Empfängers verschlüsselt.
- Hashwert der Nachricht wird zur Integritätsprüfung genutzt.
- Private Schlüssel bleiben geheim und sind nur lokal gespeichert.

### Hash-Funktion und Signatur
- Vor dem Versand wird ein Hashwert (z. B. SHA-256) der Nachricht berechnet.
- Dieser Hash wird mit dem privaten Schlüssel des Absenders signiert.
- Der Empfänger prüft die Signatur mit dem öffentlichen Schlüssel und vergleicht den Hash mit der empfangenen Nachricht.
- So wird Manipulation erkannt und die Echtheit des Absenders bestätigt.

**Zusammengefasst:**  
E-Mail-Verschlüsselung nutzt asymmetrische Kryptografie (Schlüsselpaar) und Hashes, um Vertraulichkeit, Integrität und Authentizität sicherzustellen.

## HTTPS – Wie funktioniert die Verschlüsselung technisch?

HTTPS basiert auf dem TLS/SSL-Protokoll und verwendet folgende Mechanismen:

- **Zertifikat:** Der Webserver besitzt ein digitales Zertifikat, das von einer vertrauenswürdigen CA (Certificate Authority) signiert ist.
- **Handshake:** Beim Verbindungsaufbau tauschen Client und Server kryptografische Informationen aus. Der Server sendet sein Zertifikat, der Client prüft die Echtheit.
- **Schlüssel-Austausch:** Mit asymmetrischer Verschlüsselung (z. B. RSA, ECC) wird ein gemeinsamer Sitzungsschlüssel ausgehandelt.
- **Symmetrische Verschlüsselung:** Die eigentliche Datenübertragung erfolgt mit einem schnellen symmetrischen Algorithmus (z. B. AES).
- **Hash-Funktion:** Jede Nachricht wird mit einem Hash (z. B. SHA-256) versehen, um die Integrität zu prüfen. Manipulationen werden so erkannt.
- **Authentizität:** Durch das Zertifikat und den Hash ist sichergestellt, dass die Verbindung wirklich zum gewünschten Server besteht und die Daten nicht verändert wurden.

**Zusammengefasst:**  
HTTPS schützt die Verbindung durch Zertifikate (Authentizität), Verschlüsselung (Vertraulichkeit) und Hashes (Integrität).

## Vorteile
- Vertraulichkeit
- Integrität
- Authentizität

---