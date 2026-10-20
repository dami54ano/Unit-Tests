# Lernjournal - M450, Auftrag 3.1

Datum: 20.10.2026

## Die drei Pflichtfragen

### Warum reicht ein gültiger Titel mit 50 Zeichen nicht?

50 liegt innerhalb der gültigen Klasse von 1 bis 100 Zeichen. Sowohl
`length() < 100` als auch `length() <= 100` akzeptieren diesen Wert.
Der Test entdeckt den falschen Vergleichsoperator deshalb nicht.
Zusätzlich brauche ich die Grenzpaare 0/1 und 100/101 sowie Spezialfälle.
TF-04 mit genau 100 Zeichen macht den gemeldeten Fehler sichtbar.
Beim Testen nach Gefühl werden gerade diese Grenzen und häufig null oder
reine Leerzeichen ausgelassen.

### Welche Codezeile steckt vermutlich hinter dem 100-Zeichen-Fehler?

`return title.length() < MAX_TITLE_LENGTH;`

Die obere Grenze ist laut Anforderung inklusive. Die unmittelbare Korrektur
ist `<=` statt `<`. Für die Unicode-Zusatzaufgabe wird ausserdem die Länge
in Codepoints gezählt, weil `String.length()` UTF-16-Codeeinheiten zählt.

### Warum sind null und nur Leerzeichen getrennte Testfälle?

`null` bedeutet, dass kein String vorhanden ist. Ein Methodenaufruf wie
`title.isBlank()` auf null würde eine NullPointerException auslösen.
`"   "` ist dagegen ein vorhandener String mit Inhalt, der fachlich als leer
gilt. Die Fälle prüfen unterschiedliche Bedingungen: Nullprüfung und
Blank-Prüfung. Beide müssen ohne Ausnahme abgelehnt werden.

## Klassen und Grenzwerte

Priorität: unter 1 (z.B. 0), gültig von 1 bis 5 (z.B. 3), über 5 (z.B. 6).
Die Grenzpaare sind 0/1 und 5/6. Das verlangte Raster umfasst fünf Fälle:
0, 1, 3, 5, 6. Rein für Klassen und Grenzen wären vier Werte ausreichend,
weil 1 und 5 bereits Vertreter der gültigen Klasse sind; der Auftrag verlangt
zusätzlich den Normalwert.

Fälligkeit: Vergangenheit, heute, Zukunft und fehlend. Das ergibt mindestens
vier Fälle. Die fachliche Grenze ist heute; gestern ist der erste ungültige
und heute der erste gültige Tag. Eine fachliche obere Datumsgrenze gibt es nicht.

Titel: 0, 1, 50, 100, 101 Zeichen, null und Leerzeichen ergeben die sieben
vorgegebenen Fälle. TF-17 ergänzt Tabulator und Zeilenumbruch, denn die
vorgegebenen 7 + 5 + 4 Fälle ergeben erst 16 statt der verlangten 17.

## Wiederholbare Tests

Das feste Heute ist der 20.10.2026. Das tatsächliche Ausführungsdatum soll
keinen Einfluss auf das Ergebnis haben. Ein übergebener Parameter ermöglicht
das; im Zusatzteil übernimmt eine injizierte `Clock` diese Aufgabe.
`Clock.fixed(...)` liefert stets denselben Zeitpunkt. Die Zeitzone entscheidet,
welcher Kalendertag an diesem Zeitpunkt lokal gilt.

Ein Grenzwerttest prüft den Übergang gültig/ungültig, beispielsweise gestern/heute.
Ein Spezialfall wie null prüft eine besondere Eingabeform, keinen benachbarten
Wert auf einer numerischen Skala.

## Fehler und Korrekturen

Der ursprüngliche Titelvergleich schliesst genau 100 aus. Der ursprüngliche
Datumsvergleich `dueDate.isAfter(today)` schliesst heute aus.
Der korrigierte Datumstest lautet `!dueDate.isBefore(today)` nach der Nullprüfung.
Die Ergebnisse der echten Testläufe stehen im Testfall-Raster und in den
JUnit-XML-Dateien unter `nachweise/`.

## Zusatzaufgaben und Erkenntnisse

Die Entscheidungstabelle R1 bis R4 prüft die gesamte Aufgabe. In jedem
negativen Fall ist genau ein Feld ungültig, damit das Ergebnis zugeordnet
werden kann.

Die Clock wird im Konstruktor übergeben. Die neue API berechnet heute mit
`LocalDate.now(clock)`. Die ursprünglichen Methoden mit explizitem `today`
bleiben als Überladungen erhalten, damit die unveränderten Pflicht-Regressionstests
und die ausdrücklich verlangte Vier-Parameter-Methode weiter funktionieren.

100 einfache grinsende Emojis haben in Java `length() == 200`, aber
`codePointCount(...) == 100`. Für dieses Projekt bedeutet Zeichen ein
Unicode-Codepoint. Diese Auslegung wird offengelegt, weil die Aufgabenstellung
keine genaue Unicode-Definition enthält. Ein zusammengesetztes Familien-Emoji
kann mehrere Codepoints besitzen und trotzdem ein sichtbares Zeichen bilden.
Für eine produktive App müsste die gewünschte Zähleinheit fachlich geklärt werden.

Systematisches Ableiten findet Fehler, die ein normaler Beispielwert übersieht.
Die erwarteten Ergebnisse werden aus der Anforderung festgelegt und bei der
Fehlerkorrektur nicht dem fehlerhaften Programm angepasst.

## Transparenz

Dies ist ein mit KI-Unterstützung erarbeiteter fachlicher Lernjournal-Entwurf.
Persönliche Erfahrungen, Namen eines Partners oder ein tatsächlich durchgeführter
Driver/Navigator-Wechsel werden nicht erfunden. Die Antworten sollten vor der
Abgabe selbst nachvollzogen und bei Bedarf in eigene Worte gefasst werden.
