"""Exportiert das Abgaberaster aus Testplan und archivierten JUnit-Ergebnissen.

Aufruf: python docs/export_raster.py
Abhängigkeiten: pip install reportlab
"""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
rows = json.loads((DOCS / "testplan.json").read_text(encoding="utf-8"))


def results(folder):
    found = {}
    for path in (DOCS / "nachweise" / folder).glob("TEST-*.xml"):
        root = ET.parse(path).getroot()
        for case in root.findall("testcase"):
            match = re.search(r"(TF-\d+|Z-\d+|Z\d+)", case.attrib["name"])
            if not match:
                raise ValueError(f"Fehlende ID: {case.attrib['name']}")
            key = match.group().replace("Z09", "Z-09").replace("Z10", "Z-10")
            assert key not in found, key
            assert case.find("skipped") is None and case.find("error") is None
            found[key] = case.find("failure") is None
    return found


red, green = results("rot"), results("gruen")
assert len(red) == 17 and {k for k, v in red.items() if not v} == {"TF-04", "TF-14"}
assert len(green) == 36 and all(green.values())
before = json.loads((DOCS / "nachweise/pflichttests-vorher.sha256.json").read_text(encoding="utf-8-sig"))
after = json.loads((DOCS / "nachweise/pflichttests-nachher.sha256.json").read_text(encoding="utf-8-sig"))
actual_hash = hashlib.sha256((ROOT / "src/test/java/ch/bbw/aufgabenapp/TaskValidatorTest.java").read_bytes()).hexdigest()
assert before["Hash"].lower() == after["Hash"].lower() == actual_hash


def verdict(value):
    return "akzeptiert" if value else "abgelehnt"


header = ["ID", "Feld", "Klasse", "Eingabe", "Erwartet", "Ist vorher", "Ist nachher", "Status vorher / nachher"]
data = [header]
for row in rows:
    expected = row["expected"]
    # Beide Fehlermeldungen sind archivierte boolesche Assertion-Abweichungen.
    prior = expected if red[row["id"]] else not expected
    data.append([row["id"], row["field"], row["kind"], row["input"],
                 verdict(expected), verdict(prior), verdict(expected),
                 ("OK" if red[row["id"]] else "FEHLER") + " / OK"])

md = [
    "# Testfall-Raster mit tatsächlichen Ergebnissen", "",
    "Heute = 2026-10-20. Roter Lauf: 17 Tests, 2 Fehler. Grüner Lauf: 36 Tests, 0 Fehler.",
    "Quelle: archivierte JUnit-XML-Dateien unter `nachweise/`. Pflicht-Testdatei vor/nachher SHA-256-identisch.", "",
    "| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"
]
md.extend("| " + " | ".join(row) + " |" for row in data[1:])
md.extend(["", "Zusatzfälle Z-01 bis Z-19: alle erfolgreich. Eingaben und Erwartungen siehe "
           "[Zusatzplanung](zusatz-testplan.md).", ""])
(DOCS / "testfall-raster.md").write_text("\n".join(md), encoding="utf-8")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Cell", fontName="Helvetica", fontSize=8, leading=10, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="SmallText", fontName="Helvetica", fontSize=9, leading=12))
styles["Title"].fontSize = 20
styles["Title"].leading = 24
styles["Title"].textColor = colors.HexColor("#17324d")


def p(text, style="Cell"):
    return Paragraph(escape(text), styles[style])


def table(items, widths, failures=False):
    result = Table([[p(c) for c in row] for row in items], colWidths=widths, repeatRows=1)
    instructions = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dce8f2")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#c0cbd5")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if failures:
        for index, row in enumerate(items[1:], 1):
            if row[0] in {"TF-04", "TF-14"}:
                instructions.append(("BACKGROUND", (0, index), (-1, index), colors.HexColor("#fff0d7")))
    result.setStyle(TableStyle(instructions))
    return result


output = ROOT / "output/pdf/testfall-raster.pdf"
output.parent.mkdir(parents=True, exist_ok=True)
story = [
    Paragraph("M450 | Äquivalenzklassen und Grenzwerte", styles["Title"]),
    p("Testfall-Raster | 20.10.2026 | Festes Heute: 2026-10-20", "SmallText"),
    Spacer(1, 8),
    p("Vorher: Originalvalidator, 17 Tests / 2 Fehler. Nachher: korrigierter Validator, "
      "36 Tests / 0 Fehler. Erwartungen wurden vor dem ersten Lauf festgelegt.", "SmallText"),
    Spacer(1, 10),
    table(data, [42, 58, 112, 100, 64, 64, 64, 112], failures=True),
    Spacer(1, 10),
    p("Grenzpaare: Titel 0/1 und 100/101; Priorität 0/1 und 5/6; Datum gestern/heute. "
      "Für das Datum existiert keine fachliche obere Grenze.", "SmallText"),
    p("Einzeltests prüfen jeweils nur ihr Feld. Normalwerte für Kombinationen: "
      "Titel Aufgabe, Priorität 3, Fälligkeit 2026-10-21. "
      "TF-17 ergänzt die im Blatt auf 16 Fälle summierten Beispiele auf 17.", "SmallText"),
    PageBreak(),
    Paragraph("Zusatzaufgaben | Entscheidungstabelle und Tests", styles["Title"]),
    p("Clock.fixed: 2026-10-20T10:00:00Z, Europe/Zurich. "
      "R1 bis R4 prüfen beide isValid-Überladungen.", "SmallText"),
    Spacer(1, 8),
]
advanced = [["ID / Regel", "Konkrete Eingabe / geprüfter Fall", "Erwartet", "Tatsächlich / Status"]]
descriptions = [
    ("Z-01 / R1", "Aufgabe; 3; 2026-10-21 (alles gültig)", "true"),
    ("Z-02 / R2", '""; 3; 2026-10-21 (nur Titel ungültig)', "false"),
    ("Z-03 / R3", "Aufgabe; 3; 2026-10-19 (nur Datum ungültig)", "false"),
    ("Z-04 / R4", "Aufgabe; 0; 2026-10-21 (nur Priorität ungültig)", "false"),
    ("Z-05", "Fälligkeit 2026-10-19 mit fester Clock", "false"),
    ("Z-06", "Fälligkeit 2026-10-20 mit fester Clock", "true"),
    ("Z-07", "Fälligkeit 2026-10-21 mit fester Clock", "true"),
    ("Z-08", "Fälligkeit null mit fester Clock", "false"),
    ("Z-09", "2026-10-19T22:30Z, Zürich; Fälligkeit 2026-10-19", "false"),
    ("Z-10", "Gleicher Zeitpunkt, UTC; Fälligkeit 2026-10-19", "true"),
    ("Z-11", "100-mal U+1F600; 200 UTF-16-Einheiten, 100 Codepoints", "true"),
    ("Z-12", "101-mal U+1F600; 202 UTF-16-Einheiten, 101 Codepoints", "false"),
    ("Z-13", "Einmal U+1F600; 2 UTF-16-Einheiten, 1 Codepoint", "true"),
    ("Z-14", "99-mal a + U+1F600; 101 UTF-16-Einheiten, 100 Codepoints", "true"),
    ("Z-15", "100-mal a + U+1F600; 102 UTF-16-Einheiten, 101 Codepoints", "false"),
    ("Z-16", "Priorität Integer.MIN_VALUE = -2147483648", "false"),
    ("Z-17", "Priorität Integer.MAX_VALUE = 2147483647", "false"),
    ("Z-18", "Fälligkeit LocalDate.MIN = -999999999-01-01", "false"),
    ("Z-19", "Fälligkeit LocalDate.MAX = +999999999-12-31", "true"),
]
for id_, description, expected in descriptions:
    assert green[id_.split(" / ")[0]]
    advanced.append([id_, description, expected, expected + " / OK"])
story += [
    table(advanced, [70, 410, 76, 160]),
    Spacer(1, 8),
    p("Unicode-Auslegung: Zeichen = Codepoints. String.length() zählt UTF-16-Einheiten; "
      "zusammengesetzte sichtbare Zeichen können mehrere Codepoints enthalten.", "SmallText"),
    p("Nachweise: docs/nachweise/rot und gruen (JUnit XML). "
      "Die 17 Pflichttests sind vor/nach der Korrektur SHA-256-identisch.", "SmallText"),
]


def footer(canvas, doc):
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#526579"))
    canvas.drawString(40, 22, "M450 - Auftrag 3.1 | Abgabe: 25.10.2026, 23:59 Uhr")
    canvas.drawRightString(802, 22, f"Seite {doc.page}")


SimpleDocTemplate(
    str(output), pagesize=landscape(A4), rightMargin=40, leftMargin=40,
    topMargin=28, bottomMargin=36, title="M450 - Testfall-Raster 3.1",
    author="Aufgaben-App"
).build(story, onFirstPage=footer, onLaterPages=footer)
print(f"36 Ergebnisse und unveränderte Pflichttests geprüft. PDF: {output}")
