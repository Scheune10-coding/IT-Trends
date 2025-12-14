# Agile Entwicklung + DevOps + CI/CD (ausführlich)

## Agile Entwicklung (iterativ)
- Iteratives Vorgehen:
  - Entwickeln
  - Testen
  - Ändern
  - Wieder testen
- Vorteil:
  - Fehler früher sichtbar
  - Feedback schneller
  - weniger Risiko, am Ende "am Kunden vorbei" zu liefern

### Vergleich: Wasserfall / V-Modell
- Wasserfall:
  - Phasen nacheinander (Analyse -> Design -> Implementierung -> Test -> Betrieb)
  - gut, wenn Anforderungen stabil sind
- V-Modell:
  - ähnlich, aber mit Test-Ebenen je Phase (Unit, Integration, System, Akzeptanz)
  - oft in regulierten Bereichen
- Agile:
  - nicht strikt sequenziell, sondern wiederholt kleine Schritte

---

## Prinzipien agiler Projekte (Ergänzung)
- Kurze Iterationen (z. B. 2 Wochen, sog. **Sprints**)
- Am Anfang jedes Sprints: **Sprint Planning** (Ziele und Aufgaben festlegen)
- Am Ende jedes Sprints: **Sprint Review** (Ergebnisse präsentieren) & **Sprint Retrospective** (Verbesserungen diskutieren)
- **Daily Standup:** Kurzes tägliches Teammeeting zum Abgleich
- **Backlog:** Priorisierte Liste aller Anforderungen (User Stories, Tasks)
- **Storyboards/Kanban Boards:** Visualisierung des Arbeitsfortschritts (To Do, In Progress, Done)
- **Regelmäßiges Feedback** von Stakeholdern und Nutzern
- **Selbstorganisierte Teams**
- **Transparenz & Kommunikation**
- **Anpassungsfähigkeit bei Änderungen**
- **Continuous Improvement:** Ständige Optimierung von Prozessen und Ergebnissen

---

## MVP (Minimum Viable Product)
- Definition:
  - Minimal funktionsfähige Produktversion, die echten Nutzen liefert.
- Zweck:
  - Frühes Feedback vom Kunden
  - Schnell lernen, ob Produktidee trägt
  - Vermeidung von "Overengineering"
- **Wichtigkeit:** Ermöglicht schnelles Feedback, frühe Markteinführung, Vermeidung unnötiger Entwicklung und gezielte Weiterentwicklung nach Nutzerbedarf.

Beispiel:
- Statt kompletter Shop-Plattform:
  - MVP = Produktliste + Warenkorb + einfache Zahlung
  - später: Empfehlungen, Rabatte, Kundenkonto, etc.

---

## DevOps (Development + Operations)
- Ziel:
  - Entwicklung und Betrieb enger verzahnen.
  - Releases schneller, stabiler und automatisierter machen.

### DevOps-Kernelemente (aus deinen Notizen)
- Culture
  - Wissensaustausch, Transparenz, gemeinsamer Verantwortungsbereich
- Automation
  - wiederholbare Abläufe automatisieren
- Lean
  - nur bauen, was der Kunde braucht
  - Verschwendung vermeiden
- Measurement
  - Metriken sammeln (z. B. Deployment-Frequenz, Fehlerquote, MTTR)
- Sharing
  - Best Practices, Tools, Prozesse teilen

- **DevOps:** Verbindung von Entwicklung und Betrieb, Automatisierung von Build, Test und Deployment

---

## CI/CD
- CI (Continuous Integration)
  - Code wird regelmäßig zusammengeführt (z. B. Git Push)
  - Automatische Builds + Tests laufen
  - Ziel: Integration-Probleme früh finden
- CD (Continuous Delivery / Deployment)
  - Delivery: jederzeit auslieferbar, Freigabe ggf. manuell
  - Deployment: automatische Auslieferung in Produktion

- **CI/CD Pipelines:** Automatisierte Prozesse für Continuous Integration (Zusammenführen von Code) und Continuous Deployment (automatisches Ausrollen)

Beispiel Pipeline:
- Developer pusht nach Git
- CI:
  - Build
  - Unit Tests
  - Linting
- CD:
  - Deployment in Test/Staging
  - ggf. automatische Freigabe -> Produktion

Tool-Beispiel:
- Jenkins als CI/CD-Server (typischer Klassiker)

---

## Pairing / Pair Programming
- Zwei Personen arbeiten zusammen:
  - Driver tippt
  - Navigator denkt mit
- Nutzen:
  - Wissensaufbau
  - weniger Fehler
  - bessere Codequalität
- Pairing-Tabelle:
  - einfache Übersicht, wer mit wem arbeitet (organisatorisches Tool)
- **Pairing Tabelle:** Übersicht, wer mit wem zusammenarbeitet (z. B. beim Pair Programming), fördert Wissensaustausch und Teamzusammenhalt

---

## Kanban in DevOps-Kontext
- Board hilft, Fluss sichtbar zu machen.
- WIP-Limit verhindert, dass alles "halb fertig" ist.
- **Storyboards/Kanban Boards:** Tools wie Jira, Trello, Azure Boards  
  *Wofür?* Zur Visualisierung und Steuerung des Arbeitsfortschritts im Team (z. B. Aufgabenstatus: To Do, In Progress, Done), Transparenz schaffen, Engpässe erkennen und Aufgaben priorisieren.
- **Backlog Management:** Verwaltung und Priorisierung aller Aufgaben und Anforderungen

---

## Typische Klausurfragen (mit Kurzantwort)
- "Warum Agile?"
  - weil Anforderungen sich ändern und Feedback schnell nötig ist
- "Unterschied CI und CD?"
  - CI integriert + testet Code, CD liefert/rollt automatisch aus
- "Was ist MVP?"
  - minimaler, nutzbarer Funktionsumfang, um Feedback zu bekommen

---

## Vorteile agiler Methoden (Ergänzung)
- Schnelle Reaktion auf Kundenwünsche
- Frühe Fehlererkennung
- Hohe Transparenz
- Motivation im Team
- Kontinuierliche Auslieferung von Mehrwert