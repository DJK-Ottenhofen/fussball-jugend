# Design-Spec: Andis Konzept → öffentliche Eltern-Seite

*Datum: 2026-07-25 · Repo: `mschaepers/djk-ottenhofen-jugend` (öffentliche Eleventy-Site)*

## Ziel

Die elternrelevanten Teile von Andis Konzept „F- und E-Jugend Saison 2026"
sollen **modern in der Website aufgehen** — statt als Word-Datei an die Eltern
verschickt zu werden. Ergebnis: **ein teilbarer Link** (`/eltern/`), der alles
enthält, was Eltern wissen müssen. Mobil-first (die meisten lesen am Handy).

Zusätzlich wird das Framing korrigiert: Die Seite wird **privat und ehrenamtlich
vom Trainerteam** betrieben, nicht offiziell vom Verein — das muss sichtbar und
rechtlich sauber sein (Impressum, Datenschutz, Footer).

## Kontext

- **Quelle (privat, NICHT öffentlich spiegeln):** `f-jugend/Konzept_F-und-E-Jugend_Saison-2026.md`.
  Enthält Kinder-/Trainernamen und interne Details.
- **Ziel-Seite (existiert):** `src/eltern.njk` — aktuell philosophie-lastig, warmer
  „du"-Ton. Enthält „So trainieren wir", Pull-Quote, „Warum Kinder beim Sport
  bleiben – oder aufhören", „Was uns wichtig ist", „Was dein Kind lernt", plus
  Seiten-Cards „Das lernt dein Kind" und „So machst du mit".
- **Stack:** Eleventy 3 (Nunjucks), Theme Gelb `#FFF300` / Schwarz, Font Sen.
  Mobile-Menü nutzt bereits natives `<details>/<summary>` → gleiches Idiom fürs
  Accordion.
- **base.njk:** lädt Sen aktuell vom Google-Fonts-CDN (Zeilen 8–10). Footer rahmt
  die Seite als offiziellen Verein („© 2026 DJK Ottenhofen e.V.", „Jugendleitung
  F/E-Jugend", „jugend@djk-ottenhofen.de").

## Entscheidungen (mit dem User abgestimmt)

| Thema | Entscheidung |
|---|---|
| IA | Variante A: **eine Seite `/eltern/` + Accordion** (kein `/saison/`, keine Unterseiten für die Konzept-Blöcke) |
| Einsatzzeiten / Leistungsprinzip (Konzept Pkt. 8) | **nur sanft**, werteorientiert; Leistungs-/Kader-Detail bleibt intern |
| Trainer-Namen | **Vornamen** nennen (ohne „Vater von <Kind>") |
| Trainer-geführt-Hinweis | Footer + kurzer Hinweis im /eltern/-Intro + Impressum |
| Impressum | **ja**, neue Seite `/impressum/` |
| Datenschutz | **ja**, neue Seite `/datenschutz/` |
| Google Font | **selbst hosten** (Sen lokal), Google-CDN entfernen |
| Footer-Kontakt | umstellen auf `hallo+djk@mauricio.de` |
| DJK-Logo | bleibt |

## Seitenaufbau `/eltern/`

1. **Intro (offen, ohne Klick):**
   - Gekürzte warme Philosophie („So trainieren wir" + Pull-Quote) — bestehender Ton bleibt.
   - Neuer Ein-Satz-Hinweis: *„Diese Seite pflegt ehrenamtlich das Trainerteam der
     F-/E-Jugend."*
   - Trainer-Vornamen: **F-Jugend:** Mauricio, Stefan · **E-Jugend:** Byron, Andreas,
     Julian (Julian als ehem. DJK-Jugendspieler, jetzt im Trainerteam — vertrauensbildend, kein PII).
2. **Sprung-Chips** (Ankerlinks zu den Accordion-Sektionen) für Schnellzugriff.
3. **Accordion** (`<details>/<summary>`), mobil eingeklappt. Erste Sektion darf offen sein.
4. **Seiten-Cards:** „Das lernt dein Kind" + „So machst du mit" bleiben; neue Mini-Card
   **„Auf einen Blick"** (Trainingszeiten + Schienbeinschoner-Pflicht) fürs schnelle Handy-Auge.

## Accordion-Sektionen (Quelle → öffentliche Fassung)

### 1. Trainingszeiten & Termine
- Training: Di + Do, 17:00–18:30 Uhr.
- Saisonstart: 15.09.2026.
- Sommerferien: Training nach Verfügbarkeit, Termine per WhatsApp-Umfrage.
- Winter: einmal pro Woche Hallentraining (Zeiten per WhatsApp).
- E-Jugend Heimspiele: Freitag 17:00 Uhr, Treffpunkt i.d.R. 60 min vorher.
- Vor jedem Training/Spiel: Teilnahme-Abfrage per WhatsApp — bitte zuverlässig rückmelden.
- **Schienbeinschoner sind Pflicht** (Training & Spiel).
- E-spezifische Punkte klar als „E-Jugend" markieren.

### 2. Kinderschutz
- Regeln in Eltern-Sprache: erweitertes Führungszeugnis aller Trainer; Umkleide/Dusche
  transparent (nie ein Trainer allein mit einem Kind, Duschen freiwillig); Nähe & Distanz
  nur im sportlichen Rahmen; keine privaten Einzeltreffen; Handy-Regel in der Kabine;
  Erste-Hilfe-Koffer vorhanden.
- Bitte an Eltern: Kinder regelmäßig für diese Punkte sensibilisieren.
- **Hervorgehobene Kontakt-Box:** Ansprechpartner Trainerteam **+ BFV**:
  praevention@bfv.de · 089 / 542 770-707 · www.bfv.de/kinderschutz.

### 3. Am Spielfeldrand
- Nur Trainer coachen und geben Anweisungen.
- Eltern feuern **positiv & lautstark** an, halten angemessenen Abstand, verzichten auf
  Kritik an Kindern und Schiedsrichter.
- Kurzblock **Aufsichtspflicht:** beginnt mit Trainingsstart, endet mit Trainingsende;
  bei Spielen ab Treffpunkt bis Spielende; **Hin- und Heimweg liegen bei den Eltern.**

### 4. So spielen & trainieren wir
- F- und E-Jugend trainieren gemeinsam; Gruppen nach aktueller Spielstärke, nicht strikt
  nach Alter.
- Stationstraining: Koordination, Technik, Kondition, Spielformen — viele Ballkontakte.
- Abschlussspiel als Belohnung für Einsatz & gutes Miteinander.
- **Einsatzzeiten sanft:** Einsätze werden über die Saison **fair verteilt**, jedes Kind
  bekommt Spielzeit; zusätzliche Freundschaftsspiele schaffen mehr Einsätze für alle.
  → **Kein** Leistungs-Ranking, keine „stärkste Mannschaft"-Formulierung, keine Kadergrößen.

### 5. Unsere Werte & Fair Play
- Miteinander, Respekt, keine Vorwürfe, Disziplin, Fair Play, positive Einstellung.
- **Reconcile:** mit dem bestehenden Block „Was uns wichtig ist" **verschmelzen** — keine
  zwei getrennten Wertelisten auf der Seite. Andis konkrete Werte ergänzen/schärfen die
  bestehenden Icon-Punkte.

### 6. Wenn's mal nicht klappt
- 3 Stufen, **positiv gerahmt** („damit sich alle wohlfühlen"):
  1. freundlicher Hinweis + Erklärung,
  2. kurze Auszeit vom Training/Abschlussspiel,
  3. Gespräch mit den Eltern.
- Ton: selten nötig, dient Klarheit & gutem Miteinander. Kein Straf-Duktus.

## Trainer-geführt-Framing (base.njk Footer)

- Copyright ersetzen:
  `© 2026 DJK Ottenhofen e.V. — 70 Jahre Sportgemeinschaft`
  → `© 2026 Trainerteam F-/E-Jugend · privat & ehrenamtlich betrieben`
- Neue Footer-Hinweiszeile: *„Diese Seiten pflegt ehrenamtlich das Trainerteam der
  F-/E-Jugend — keine offiziellen Vereinsmitteilungen."*
- Footer-Kontakt-Mail: `jugend@djk-ottenhofen.de` → `hallo+djk@mauricio.de`.
  „Jugendleitung F/E-Jugend / DJK Ottenhofen e.V. / Sportgelände" entsprechend anpassen
  (Betreiber = Trainerteam, nicht Vereinsstelle).
- **Legal-Links** im Footer ergänzen: Impressum · Datenschutz.
- DJK-Logo (`site.logo`) bleibt; DJK-Zugehörigkeit darf erwähnt bleiben (die Kinder spielen
  für die DJK) — nur nicht als Copyright-Inhaber / offizielle Stelle.

## Neue Seite `/impressum/`

```
Impressum

Angaben gemäß § 5 DDG
Mauricio Schäpers
An der Hofmark 29
85570 Ottenhofen

Kontakt
E-Mail: hallo+djk@mauricio.de

Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV
Mauricio Schäpers, Anschrift wie oben

Hinweis
Dieses Angebot wird privat und ehrenamtlich vom Trainerteam der F-/E-Jugend
betrieben. Es ist kein offizielles Angebot des DJK Ottenhofen e.V.
```
- Optional kurzer Haftungs-/Link-Disclaimer (Standard-Boilerplate).
- Kein Telefon nötig (E-Mail genügt); kein USt-ID/Handelsregister (nicht-kommerziell).

## Neue Seite `/datenschutz/` (Kurzfassung)

Standard-Boilerplate für eine statische, tracking-freie GitHub-Pages-Site:
- **Verantwortlicher:** Mauricio Schäpers, Anschrift, E-Mail (wie Impressum).
- **Hosting:** GitHub Pages (GitHub Inc.). Server-Logs inkl. IP durch GitHub;
  Rechtsgrundlage Art. 6 Abs. 1 lit. f DSGVO. Verweis auf GitHubs Datenschutz.
- **Keine Cookies, kein Tracking, keine Analyse/Statistik.**
- **Schriftarten lokal gehostet** — kein Abruf von Google-Servern.
- **Externe Links** (BFV, DFB): kein Einfluss auf deren Datenverarbeitung.
- **Betroffenenrechte** (Auskunft, Berichtigung, Löschung, Widerspruch) +
  Beschwerderecht bei der Aufsichtsbehörde (BayLDA, Ansbach).
- Hinweis: Kommunikation läuft teils über WhatsApp-Gruppen — außerhalb dieser Website.

> Hinweis: Impressum/Datenschutz sind Standard-Boilerplate, kein anwaltlicher Rat;
> vor Live-Gang einmal gegenlesen.

## Font selbst hosten

- Sen (OFL-Lizenz, self-host erlaubt), Weights 400/700/800.
- woff2-Dateien nach `assets/fonts/` legen; `@font-face` in `assets/css/style.css`.
- Die drei `<link>`-Zeilen (preconnect ×2 + Google-Fonts-CSS) aus `base.njk` entfernen.

## Technik

- Reine Content-/Template-Änderung. **Keine** neuen npm-Dependencies, **kein** JS
  (natives `<details>` fürs Accordion — barrierefrei, mobil, funktioniert ohne JS).
- Neue Accordion-Styles im bestehenden Gelb/Schwarz-Theme in `assets/css/style.css`.
- Neue Nunjucks-Seiten `src/impressum.njk`, `src/datenschutz.njk` mit `layout: base.njk`.

## Dateien (voraussichtlich)

- `src/eltern.njk` — Umbau: Intro kürzen + Trainer-Hinweis/Namen + Accordion-Sektionen + Mini-Card.
- `src/_includes/base.njk` — Footer (Copyright, Hinweis, Kontakt, Legal-Links), Google-Fonts-Links entfernen.
- `src/impressum.njk` — neu.
- `src/datenschutz.njk` — neu.
- `assets/css/style.css` — Accordion-Styles, `@font-face`.
- `assets/fonts/` — Sen woff2 (neu).
- ggf. Footer-Legal-Links (Impressum/Datenschutz) — direkt im Footer, nicht in `site.nav`.

## Bewusst NICHT öffentlich (PII / intern)

Kinder-/Elternnamen, „Vater von <Kind>", Leistungs-/Kader-Details & Kadergrößen
(Konzept Pkt. 8), juristische Haftungs-Feinheiten, interne Trainer-Aufgabenteilung am
Spieltag, Spielerzahlen.

## Out of Scope

- Übungen/Einheiten/Pläne (unverändert).
- Custom-Domain, Logo-Hosting-Umzug.
- Klärung Issue #2 (E-Kadergröße) — separat, ohnehin nicht öffentlich.

## Akzeptanzkriterien

- `/eltern/` enthält alle 6 Accordion-Sektionen; mobil eingeklappt, per Tap aufklappbar;
  Sprung-Chips funktionieren.
- Kein Kinder-/Elternname, keine Kadergröße, kein Leistungs-Ranking auf öffentlichen Seiten.
- BFV-Kontakt-Box in „Kinderschutz" vorhanden.
- Footer: Copyright geändert, Trainer-Hinweis sichtbar, Kontakt = hallo+djk@mauricio.de,
  Impressum- & Datenschutz-Link vorhanden.
- `/impressum/` und `/datenschutz/` erreichbar und inhaltlich wie oben.
- Sen wird lokal geladen; keine Requests an fonts.googleapis.com / fonts.gstatic.com.
- `npx @11ty/eleventy` baut fehlerfrei; keine doppelte Werteliste auf `/eltern/`.
