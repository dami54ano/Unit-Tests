# Abgabe und Anforderungsprüfung

Termin: Sonntag, **25.10.2026, 23:59 Uhr**, Europe/Zurich.

Teams-Aufgabe: **M450 - 3.1 Äquivalenzklassen und Grenzwerte**.

## Für Teams

Repository mit Aufgabenordner:
https://github.com/dami54ano/Unit-Tests/tree/aufgabe-3.1-grenzwerttests/aufgaben-app

Anhang: [`testfall-raster.pdf`](../output/pdf/testfall-raster.pdf).

Lernjournal: [`lernjournal.md`](lernjournal.md).

## Pflichtanforderungen und Bewertung

| Kriterium | Nachweis | Ergebnis |
|---|---|---|
| Klassen und Grenzpaare, Erwartungen vor Lauf (3 Punkte) | testplan-vorher.md; Titel 0/1, 100/101; Priorität 0/1, 5/6; gestern/heute | umgesetzt |
| ID, konkrete Eingabe, Erwartung (2 Punkte) | TF-01 bis TF-17 im Markdown- und PDF-Raster | umgesetzt |
| Positive/negative Fälle, Grenzen, Spezialfälle (3 Punkte) | 17 Pflichttests plus 19 Zusatztests | umgesetzt |
| Beide Fehler gefunden, korrigiert, Tests unverändert (2 Punkte) | Rot: 2 Fehler; Grün: 0 Fehler; identische SHA-256 der Pflicht-Testdatei | umgesetzt |
| Drei Lernjournal-Antworten | lernjournal.md, erste drei Abschnitte | ausgearbeitet |
| JUnit 5 und Gradle Kotlin DSL, JDK >= 17 | build.gradle.kts, Wrapper, Java-17-Bytecode | umgesetzt |
| Tatsächliche Ergebnisse und Status | testfall-raster.md und PDF, echte JUnit-XML | dokumentiert |
| Entscheidungstabelle R1 bis R4, isValid | zusatz-testplan.md, TaskValidatorAdvancedTest | umgesetzt |
| Clock im Konstruktor, Clock.fixed | Clock-API, Datums- und Zeitzonentests | umgesetzt |
| Emoji-Grenzwert 100 | Z-11 bis Z-15, dokumentierte Unicode-Auslegung | umgesetzt |

Die Bewertung bleibt bei der Lehrperson; die Tabelle dokumentiert die Abdeckung,
sie ist keine Zusage einer bestimmten Punktzahl.

## Externe Schritte

- Einladung an GitHub-Benutzer **MikeDiethelm** am 20.10.2026 erstellt
  (Einladungs-ID 338727237). Annahme durch die Lehrperson steht aus.
- Repository-Link und PDF müssen in der genannten Teams-Aufgabe eingereicht werden.
  Eine tatsächliche Teams-Abgabe ist hier noch nicht bestätigt.
- Die geforderte Zusammenarbeit mit Driver/Navigator und Rollenwechsel ist eine
  organisatorische Vorgabe. Sie kann nicht durch die Implementierung erledigt oder
  rückwirkend belegt werden.
- Das Lernjournal wurde mit KI-Unterstützung erstellt; Antworten vor der Abgabe
  selbst nachvollziehen und eigene Erfahrungen ergänzen.
