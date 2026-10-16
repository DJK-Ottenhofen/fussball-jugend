"""Prüft Übungsdateien gegen das Runbook uebung-schreiben.md.

Aufruf: python tools/pruefe_uebungen.py [slug ...]
Ohne Argument werden alle Übungen geprüft. Exit 1 bei Befund.
"""
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UEB = ROOT / "src" / "uebungen"
SVG = ROOT / "src" / "assets" / "uebungen"
VERBOTEN = [
    "advance", "mfs", "münchner fußball schule", "soccerdrills", "fussballbasis",
    "training-blog", "bambini-fussballtraining", "owayo", "trainertalk",
    "dfb-methodik", "levelschießen", "sports-graphics", "champions league",
]
ABSCHNITTE = ["## Aufbau", "## Ablauf", "## Coaching-Punkte", "## Varianten"]
PFLICHT = ["layout:", "title:", "kategorie:", "altersgruppen:", "spielstaerke:",
           "phase:", "ziel:", "quelle:", "bild:", "bildAlt:"]


def alt_text(slug):
    try:
        return subprocess.run(
            ["git", "show", f"main:src/uebungen/{slug}.md"],
            capture_output=True, text=True, encoding="utf-8", cwd=ROOT, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return ""


def woerter(text):
    return re.findall(r"[\wäöüß]+", text.lower())


def gleiche_folge(alt, neu, n=8):
    """Liefert die erste Folge von n gleichen Wörtern, sonst None."""
    a, b = woerter(alt), woerter(neu)
    folgen = {tuple(a[i:i + n]) for i in range(len(a) - n + 1)}
    for i in range(len(b) - n + 1):
        t = tuple(b[i:i + n])
        if t in folgen:
            return " ".join(t)
    return None


def pruefe(slug):
    befunde = []
    p = UEB / f"{slug}.md"
    if not p.exists():
        return [f"{slug}: Datei fehlt"]
    text = io.open(p, encoding="utf-8").read()
    kopf, _, body = text.partition("\n---\n")
    for f in PFLICHT:
        if f not in kopf:
            befunde.append(f"{slug}: Frontmatter ohne {f}")
    if "quelleUrl" in kopf:
        befunde.append(f"{slug}: quelleUrl ist nicht erlaubt")
    if 'quelle: "DJK Ottenhofen Trainerteam"' not in kopf:
        befunde.append(f"{slug}: quelle muss DJK Ottenhofen Trainerteam sein")
    pos = [body.find(a) for a in ABSCHNITTE]
    if -1 in pos or pos != sorted(pos):
        befunde.append(f"{slug}: Abschnitte fehlen oder falsche Reihenfolge")
    low = text.lower()
    for v in VERBOTEN:
        if v in low:
            befunde.append(f"{slug}: verbotener Name '{v}'")
    zeilen = text.count("\n") + 1
    if not 40 <= zeilen <= 75:
        befunde.append(f"{slug}: {zeilen} Zeilen (Soll 40 bis 70)")
    m = re.search(r'bild: "(/assets/uebungen/([^"]+)\.svg)"', kopf)
    if not m or m.group(2) != slug:
        befunde.append(f"{slug}: bild zeigt nicht auf /assets/uebungen/{slug}.svg")
    svg = SVG / f"{slug}.svg"
    if not svg.exists():
        befunde.append(f"{slug}: SVG fehlt")
    else:
        s = io.open(svg, encoding="utf-8").read()
        if 'role="img"' not in s or "<title>" not in s:
            befunde.append(f"{slug}: SVG ohne role=img oder title")
        inhalte = "".join(re.findall(r"<text[^>]*>([^<]*)</text>", s))
        if inhalte and not re.fullmatch(r"[\d\s]*", inhalte):
            befunde.append(f"{slug}: SVG enthält Text außer Ziffern")
    alt = alt_text(slug)
    if alt and alt != text:
        _, _, altbody = alt.partition("\n---\n")
        f = gleiche_folge(altbody, body)
        if f:
            befunde.append(f"{slug}: übernommene Wortfolge '{f}'")
    return befunde


def main(argv):
    slugs = argv or sorted(p.stem for p in UEB.glob("*.md"))
    alle = []
    for s in slugs:
        alle += pruefe(s)
    for b in alle:
        print(b)
    print(f"{len(slugs)} geprüft, {len(alle)} Befunde")
    return 1 if alle else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
