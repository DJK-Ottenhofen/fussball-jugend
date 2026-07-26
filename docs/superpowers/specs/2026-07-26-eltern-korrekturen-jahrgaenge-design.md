# Design-Spec: Eltern-Korrekturen + Mehr-Jahrgänge sortieren

*Datum: 2026-07-26 · Repo: `mschaepers/djk-ottenhofen-jugend` (öffentliche Eleventy-Site)*

## Ziel

Vier inhaltliche Korrekturen auf `/eltern/` (Handy-Regel, Erste-Hilfe, Spieltermine,
Anmeldung) sowie das Sortieren der jahrgangsabhängigen Inhalte, weil die **G-Jugend**
dazukommt (D-Jugend hat Interesse bekundet).

Kernproblem: `/eltern/` ist aktuell F/E-verdrahtet (Trainer-Zeile im Intro, Zeiten
„Di & Do 17:00–18:30", E-Heimspiele). Mit weiteren Jahrgängen bricht das.

## Entscheidungen (mit dem User abgestimmt)

| Thema | Entscheidung |
|---|---|
| Struktur | **Eine Seite bleibt.** Keine Unterseiten pro Mannschaft — jahrgangsabhängig sind nur Zeiten/Ansprechpartner, dafür wären eigene Seiten halbleer. Stattdessen ein kompakter Block „Unsere Mannschaften". |
| Trainer-Namen | **Nur Vornamen** (konsistent mit bisherigem Stand), auch bei der G-Jugend. |
| G-Jugend Training | **Di & Do, 16:00–17:00 Uhr**, Trainerin Cornelia, `g-jugend@djk-ottenhofen.de` |
| Kinderschutz/Werte/Maßnahmen | Gelten **für alle Jahrgänge** → Framing von „F-/E-Jugend" auf „DJK-Ottenhofen-Jugend" erweitern. |
| G-Jugend Spiele | **Keine Spieltermine.** Zweimal pro Woche Training; kurze Fokus-Zeile statt Spielangaben. Halbjahres-Spielplan wird als F/E gekennzeichnet. |
| Erste-Hilfe | Nur die positive Aussage (Training + Heimspiele, vor Ort). **Kein** Auswärts-Vorbehalt, **kein** „führen keinen eigenen mit". |

## 1. Vier Textkorrekturen

### a) Handy-Regel (Accordion „Kinderschutz")
Alt: „In der Umkleide gilt für die Kinder Handyverbot – Ausnahme: kurz die Familie kontaktieren."

Neu:
> In der Umkleide gilt striktes Handyverbot – ohne Ausnahme. Außerhalb der Umkleide darf das Handy nur in Absprache mit einem Trainer genutzt werden, zum Beispiel um kurz die Familie zu kontaktieren.

### b) Erste-Hilfe (Accordion „Kinderschutz")
Alt: „Ein Erste-Hilfe-Koffer ist bei Training und Spiel verfügbar."

Neu:
> Beim Training und bei Heimspielen ist vor Ort ein Erste-Hilfe-Koffer verfügbar.

### c) Spieltermine (Accordion „Trainingszeiten & Termine")
Ersetzt die bisherige Zeile „Heimspiele E-Jugend: Freitag, Anstoß 17:00 Uhr – Treffpunkt in der Regel 60 Minuten vorher."

Neu, zwei Punkte:
> **Spieltermine (F- und E-Jugend):** Die Termine stehen für ein Halbjahr im Voraus fest und werden frühzeitig bekanntgegeben. Bitte tragt sie euch gleich ein und haltet sie frei – wir können nicht vor jedem Spiel einzeln bei allen nachfragen.
>
> **Treffpunkt:** in der Regel 60 Minuten vor Anstoß.

### d) Card „So machst du mit"
WhatsApp-Gruppe entfällt hier (für Außenstehende nicht erreichbar). Neu:

> 1. Sprecht eine Trainerin oder einen Trainer direkt an – oder schreibt eine Mail an euren Jahrgang: `g-jugend@djk-ottenhofen.de`, `f-jugend@djk-ottenhofen.de` oder `e-jugend@djk-ottenhofen.de`. Alle Adressen findet ihr auch auf der offiziellen Vereinsseite.
> 2. Zum Probetraining vorbeikommen – jederzeit möglich, bitte im Beisein eines Elternteils.
> 3. Dabei bleiben: Dafür braucht ihr die DJK-Mitgliedschaft, den Jugend-Pass und die Bildrechte-Erklärung für den Spielerpass.
>
> **Formulare:** [Fußball-Downloads auf djk-ottenhofen.de](https://djk-ottenhofen.de/weiteres/downloads/fussball-downloads/)
> **Mitbringen:** Schienbeinschoner (Pflicht), Hallen-/Fußballschuhe, Getränk.

WhatsApp bleibt an der richtigen Stelle: bei der Teilnahme-Abfrage im Accordion
(betrifft bestehende Mitglieder) und in der Card „Auf einen Blick".

## 2. Neuer Block „Unsere Mannschaften"

Kompakte Karten-Reihe, platziert **oben in `.parents-main`** (vor „So trainieren wir"),
plus Jump-Chip „👥 Mannschaften" mit Anker `#mannschaften`. Mobil untereinander,
ab Tablet nebeneinander (bestehendes `.card-grid`-Muster).

| Karte | Trainer | Training | Kontakt | Zusatz |
|---|---|---|---|---|
| **G-Jugend** (Bambini) | Cornelia | Di & Do, 16:00–17:00 Uhr | g-jugend@djk-ottenhofen.de | Fokus-Zeile (siehe unten), keine Spieltermine |
| **F-Jugend** | Mauricio & Stefan | Di & Do, 17:00–18:30 Uhr | f-jugend@djk-ottenhofen.de | — |
| **E-Jugend** | Byron, Andreas & Julian | Di & Do, 17:00–18:30 Uhr | e-jugend@djk-ottenhofen.de | Heimspiele: Freitag, 17:00 Uhr |

Fokus-Zeile G-Jugend:
> Zweimal pro Woche Training, noch keine Spieltermine. Im Mittelpunkt stehen der Ball
> und viele Spaßspiele – spielerisch Richtung Fußball, nach den Empfehlungen des DFB
> für die Kleinsten.

Zeile zur E-Jugend behält Julians Kurz-Info nicht mehr im Intro; stattdessen bleibt sie
als Halbsatz in der E-Karte erhalten: „Julian ist ehemaliger DJK-Jugendspieler."

**Folge:** Die Trainer-Zeile (`.trainer-line`) im Intro entfällt — ihre Information steckt
jetzt in den Karten. Die Accordion-Sektion „Trainingszeiten & Termine" behält nur
Übergreifendes: Saisonstart, Sommerferien, Hallentraining, Spieltermine, Teilnahme-Abfrage,
Schienbeinschoner. Die konkrete Zeile „Training: Dienstag & Donnerstag, 17:00–18:30 Uhr"
wird dort durch einen Verweis auf die Mannschafts-Karten ersetzt.

## 3. Framing auf alle Jahrgänge erweitern

„F-/E-Jugend" → „DJK-Ottenhofen-Jugend" bzw. „Jugend" an diesen Stellen:

- `src/eltern.njk` — Intro-Lead („…mit den Kindern der F- und E-Jugend arbeiten" → „…mit den Kindern unserer Jugendmannschaften arbeiten"); `.parents-note` („Trainerteam der F-/E-Jugend" → „Trainerteam der DJK-Ottenhofen-Jugend").
- `src/_includes/base.njk` — Footer-Brand („Private, ehrenamtliche Trainerseite der F-/E-Jugend" → „…der DJK-Ottenhofen-Jugend"), Footer-Kontakt („Trainerteam F-/E-Jugend" → „Trainerteam der Jugend"), Footer-Copyright („© 2026 Trainerteam F-/E-Jugend" → „© 2026 Trainerteam DJK Ottenhofen Jugend").
- `src/impressum.njk` — Hinweis-Absatz („vom Trainerteam der F-/E-Jugend betrieben" → „vom Trainerteam der DJK-Ottenhofen-Jugend betrieben").

Nicht ändern: die Sektion „So spielen & trainieren wir" sagt weiterhin korrekt, dass
**F- und E-Jugend** gemeinsam trainieren (das ist eine zutreffende Einzelaussage).

## 4. Zwei Folgefehler mitfixen

Beide entstehen, weil die G-Jugend andere Zeiten hat:

- **Card „Auf einen Blick"**: Zeile „Training: Di & Do, 17:00–18:30" → „Trainingszeiten: siehe Mannschaften" (Link auf `#mannschaften`).
- **Accordion „Am Spielfeldrand" → Aufsichtspflicht**: „(in der Regel 17:00–18:30 Uhr)" → „(Zeiten je Mannschaft)".

## 5. Technik

- Reine Content-/Template-Änderung, keine neuen Dependencies, kein JS.
- Neue CSS-Klassen `.team-card` / `.team-meta` (an `.info-card` und `.fact-card dl`
  angelehnt, bestehende Design-Tokens), Layout über das vorhandene `.card-grid`.
- Betroffene Dateien: `src/eltern.njk`, `src/_includes/base.njk`, `src/impressum.njk`,
  `src/assets/css/style.css`.

## 6. Bewusst NICHT gemacht

- Keine Unterseiten/Mannschaftsseiten (siehe Entscheidung oben).
- Keine D-Jugend-Karte (noch nicht konkret).
- Keine Aussage zu Bambini-Spielfesten/Turnierformaten (nicht verifiziert).
- Keine Nachnamen von Trainern; keine Kinder-/Elternnamen.
- `site.json`-Altersgruppen (Übungs-Filter) bleiben unverändert — „Bambini" bleibt dort
  das Label; die Eltern-Seite nennt es „G-Jugend (Bambini)".

## 7. Akzeptanzkriterien

- Handy-Regel enthält „striktes Handyverbot" und „ohne Ausnahme"; keine Umkleide-Ausnahme mehr.
- Erste-Hilfe-Satz nennt Training + Heimspiele, ohne Auswärts-Vorbehalt.
- Spieltermine-Punkt ist als „(F- und E-Jugend)" gekennzeichnet und enthält den
  Halbjahres-Hinweis; Treffpunkt 60 Minuten steht separat.
- Card „So machst du mit" enthält alle drei Jahrgangs-Mails, den Downloads-Link,
  „im Beisein eines Elternteils" — und **keine** WhatsApp-Erwähnung mehr.
- Block `#mannschaften` mit drei Karten (G/F/E) ist vorhanden, Jump-Chip verlinkt darauf.
- Keine „17:00–18:30"-Angabe mehr an Stellen, die für alle Jahrgänge gelten
  („Auf einen Blick", Aufsichtspflicht).
- Kein „F-/E-Jugend" mehr in Footer, Impressum und Eltern-Intro.
- Keine Trainer-Nachnamen im gebauten Output von `/eltern/`.
- `npx @11ty/eleventy` baut fehlerfrei; mobile Browser-Prüfung ohne Konsolenfehler.
