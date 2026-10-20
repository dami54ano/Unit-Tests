# Zusatzaufgaben: Planung vor der Umsetzung

## Entscheidungstabelle

Festes Heute: 2026-10-20. Jeder negative Fall verändert genau ein Feld.
Die Clock-Variante ersetzt später den expliziten Parameter `today`.

| ID / Regel | Titel | Priorität | Fälligkeit | Titel gültig | Priorität gültig | Datum gültig | Erwartet |
|---|---|---|---|---|---|---|---|
| Z-01 / R1 | Aufgabe | 3 | 2026-10-21 | ja | ja | ja | true |
| Z-02 / R2 | "" | 3 | 2026-10-21 | nein | ja | ja | false |
| Z-03 / R3 | Aufgabe | 3 | 2026-10-19 | ja | ja | nein | false |
| Z-04 / R4 | Aufgabe | 0 | 2026-10-21 | ja | nein | ja | false |

## Clock und Unicode

| ID | Klasse / Eingabe | Erwartet |
|---|---|---|
| Z-05 | Clock.fixed: 2026-10-20T10:00:00Z, Europe/Zurich; Datum 2026-10-19 | false |
| Z-06 | gleiche Clock; Datum 2026-10-20 | true |
| Z-07 | gleiche Clock; Datum 2026-10-21 | true |
| Z-08 | gleiche Clock; Datum null | false |
| Z-09 | 2026-10-19T22:30:00Z, Europe/Zurich; Datum 2026-10-19 (lokal bereits 20.10.) | false |
| Z-10 | derselbe Zeitpunkt, UTC; Datum 2026-10-19 | true |
| Z-11 | 100-mal U+1F600 (grinsendes Gesicht) | true; length() = 200, Codepoints = 100 |
| Z-12 | 101-mal U+1F600 | false |
| Z-13 | einmal U+1F600 | true |
| Z-14 | 99-mal "a" und einmal U+1F600 | true |
| Z-15 | 100-mal "a" und einmal U+1F600 | false |
| Z-16 | Priorität Integer.MIN_VALUE | false |
| Z-17 | Priorität Integer.MAX_VALUE | false |
| Z-18 | Fälligkeit LocalDate.MIN, festes Heute | false |
| Z-19 | Fälligkeit LocalDate.MAX, festes Heute | true |

Projektentscheidung: Zeichen werden als Unicode-Codepoints gezählt. Das Aufgabenblatt
definiert nicht, ob mit Zeichen UTF-16-Einheiten, Codepoints oder sichtbare Grapheme
gemeint sind. Ein einfaches Emoji ist ein Codepoint, aber zwei UTF-16-Einheiten.
Kombinierte Emojis und Buchstaben mit kombinierenden Akzenten können aus mehreren
Codepoints bestehen. Graphemzählung ist deshalb eine andere mögliche Anforderung.
Es wird keine vollständige Graphemzählung behauptet.
