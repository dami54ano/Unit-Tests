# Testfall-Raster vor dem Testlauf

Festes Heute: 2026-10-20. Erwartungen aus der Anforderung, vor dem ersten Lauf festgelegt.
Einzelmethoden prüfen nur ihr Feld; Normalwerte für kombinierte Tests: Titel "Aufgabe", Priorität 3, Datum 2026-10-21.

| ID | Feld | Klasse | Eingabe | Erwartet | Tatsächlich | Status |
|---|---|---|---|---|---|---|
| TF-01 | Titel | leer | "" | abgelehnt |  |  |
| TF-02 | Titel | untere Grenze | "a" | akzeptiert |  |  |
| TF-03 | Titel | Normalwert | "a" x 50 | akzeptiert |  |  |
| TF-04 | Titel | obere Grenze | "a" x 100 | akzeptiert |  |  |
| TF-05 | Titel | zu lang | "a" x 101 | abgelehnt |  |  |
| TF-06 | Titel | fehlend | null | abgelehnt |  |  |
| TF-07 | Titel | nur Leerzeichen | "   " | abgelehnt |  |  |
| TF-08 | Priorität | unterhalb / Grenze | 0 | abgelehnt |  |  |
| TF-09 | Priorität | untere gültige Grenze | 1 | akzeptiert |  |  |
| TF-10 | Priorität | gültige Klasse | 3 | akzeptiert |  |  |
| TF-11 | Priorität | obere gültige Grenze | 5 | akzeptiert |  |  |
| TF-12 | Priorität | oberhalb / Grenze | 6 | abgelehnt |  |  |
| TF-13 | Fälligkeit | Vergangenheit / Grenze | 2026-10-19 | abgelehnt |  |  |
| TF-14 | Fälligkeit | heute / Grenze | 2026-10-20 | akzeptiert |  |  |
| TF-15 | Fälligkeit | Zukunft | 2026-10-21 | akzeptiert |  |  |
| TF-16 | Fälligkeit | fehlend | null | abgelehnt |  |  |
| TF-17 | Titel | Spezialfall Whitespace | "\t\n" | abgelehnt |  |  |
