# M450 - 3.1 Äquivalenzklassen und Grenzwerte

Eigenständiges Gradle-Projekt für die Aufgaben-App, inklusive aller drei
Advanced-Aufgaben. Die vorhandene Games-Library ist davon unabhängig.

## Starten

Voraussetzung: JDK 17 bis 25, beim ersten Lauf Internet. Gradle 9.1.0 ist
per Wrapper inklusive SHA-256-Prüfsumme festgelegt. Der Java-Code wird mit
`--release 17` kompiliert. JUnit 5.10.2 entspricht dem Aufgabenblatt.

In IntelliJ diesen Ordner als Gradle-Projekt öffnen und ein passendes
Gradle-JDK wählen.

```powershell
cd aufgaben-app
.\gradlew.bat clean test
```

Auf diesem Rechner zeigt `JAVA_HOME` auf Java 26, während `java` im PATH
Java 25 verwendet. Für Gradle 9.1.0 deshalb in der aktuellen PowerShell setzen:

```powershell
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot'
.\gradlew.bat clean test
```

Linux/macOS: `./gradlew clean test`.

Erwartet: **36 Tests, 0 Fehler** (17 Pflichtfälle und 19 Zusatzfälle).
HTML-Bericht: `build/reports/tests/test/index.html`.
GitHub Actions prüft dasselbe Projekt mit Java 17 und 25.

## Dokumentation und Nachweise

- [Lernjournal](docs/lernjournal.md): Pflichtfragen, Checkpoint-Fragen und Reflexion.
- [Geplantes Raster](docs/testplan-vorher.md): Erwartungen vor dem ersten Lauf, Ergebnisfelder leer.
- [Ausgefülltes Raster](docs/testfall-raster.md): tatsächliche Ergebnisse vor/nach der Korrektur.
- [Zusatzplanung](docs/zusatz-testplan.md): Entscheidungstabelle R1 bis R4, Clock und Unicode.
- [PDF zur Abgabe](output/pdf/testfall-raster.pdf).
- [Roter Lauf](docs/nachweise/rot.txt): 17 Tests, genau TF-04 und TF-14 fehlgeschlagen.
- [Grüner Lauf](docs/nachweise/gruen.txt): alle Pflicht- und Zusatztests.
- [Originalvalidator](docs/nachweise/TaskValidator-original.java.txt) und JUnit-XML unter
  `docs/nachweise/rot/` bzw. `docs/nachweise/gruen/`.

Die SHA-256-Dateien im Nachweisordner belegen, dass `TaskValidatorTest.java`
zwischen rotem und grünem Lauf unverändert blieb.

## API und Zusatzaufgaben

`new TaskValidator(clock)` erhält seine Zeitquelle von aussen.
`isDueDateValid(dueDate)` und `isValid(title, priority, dueDate)` verwenden diese
Clock. Die ursprüngliche API mit `today` bleibt als kompatible Überladung
erhalten, einschliesslich der verlangten Vier-Parameter-Methode `isValid`.
Der parameterlose Konstruktor verwendet die System-Clock; Datumstests verwenden
stets ein explizites Datum oder `Clock.fixed`.

Titel: 1 bis 100 Unicode-Codepoints; null, leer oder `isBlank()` werden abgelehnt.
Priorität: ganze Zahl 1 bis 5 inklusive. Fälligkeit: heute oder später, null ungültig.
Die Clock und ein explizites `today` sind notwendige Konfiguration und dürfen
nicht null sein. Unicode-Codepoints sind nicht dasselbe wie sichtbare Grapheme;
die fachliche Auslegung ist im Lernjournal dokumentiert.

## Abgabe

Termin: **Sonntag, 25.10.2026, 23:59 Uhr (Europe/Zurich)**.
Teams-Aufgabe: **M450 - 3.1 Äquivalenzklassen und Grenzwerte**.

Einzureichen: Repository-Link mit sichtbarem Aufgabenordner und das PDF-Raster.
Lehrperson: [MikeDiethelm](https://github.com/MikeDiethelm).
Eine Einladung muss von der Lehrperson angenommen werden, bevor aktiver Zugriff
als Collaborator besteht. Der tatsächliche Abgabestatus steht in `docs/abgabe.md`.

Die organisatorische Partnerarbeit mit Driver/Navigator und Rollenwechsel
kann durch Code nicht nachgewiesen werden. Das KI-gestützte Lernjournal vor
der Abgabe selbst nachvollziehen.
