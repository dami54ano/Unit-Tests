# Testfall-Raster mit tatsächlichen Ergebnissen

Heute = 2026-10-20. Roter Lauf: 17 Tests, 2 Fehler. Grüner Lauf: 36 Tests, 0 Fehler.
Quelle: archivierte JUnit-XML-Dateien unter `nachweise/`. Pflicht-Testdatei vor/nachher SHA-256-identisch.

| ID | Feld | Klasse | Eingabe | Erwartet | Ist vorher | Ist nachher | Status vorher / nachher |
|---|---|---|---|---|---|---|---|
| TF-01 | Titel | leer | "" | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-02 | Titel | untere Grenze | "a" | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-03 | Titel | Normalwert | "a" x 50 | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-04 | Titel | obere Grenze | "a" x 100 | akzeptiert | abgelehnt | akzeptiert | FEHLER / OK |
| TF-05 | Titel | zu lang | "a" x 101 | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-06 | Titel | fehlend | null | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-07 | Titel | nur Leerzeichen | "   " | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-08 | Priorität | unterhalb / Grenze | 0 | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-09 | Priorität | untere gültige Grenze | 1 | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-10 | Priorität | gültige Klasse | 3 | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-11 | Priorität | obere gültige Grenze | 5 | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-12 | Priorität | oberhalb / Grenze | 6 | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-13 | Fälligkeit | Vergangenheit / Grenze | 2026-10-19 | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-14 | Fälligkeit | heute / Grenze | 2026-10-20 | akzeptiert | abgelehnt | akzeptiert | FEHLER / OK |
| TF-15 | Fälligkeit | Zukunft | 2026-10-21 | akzeptiert | akzeptiert | akzeptiert | OK / OK |
| TF-16 | Fälligkeit | fehlend | null | abgelehnt | abgelehnt | abgelehnt | OK / OK |
| TF-17 | Titel | Spezialfall Whitespace | "\t\n" | abgelehnt | abgelehnt | abgelehnt | OK / OK |

Zusatzfälle Z-01 bis Z-19: alle erfolgreich. Eingaben und Erwartungen siehe [Zusatzplanung](zusatz-testplan.md).
