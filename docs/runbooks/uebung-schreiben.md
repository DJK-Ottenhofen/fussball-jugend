# Runbook: Eine Übung schreiben

Jede Übung auf `fussball.djk-ottenhofen.de` ist eine Markdown-Datei unter `src/uebungen/<slug>.md` mit einer Skizze unter `src/assets/uebungen/<slug>.svg`. Dieses Runbook gilt für neue Übungen und für Umschreibungen. Beispiel, das alles richtig macht: `src/uebungen/steilgang-1gegen1.md`.

## Frontmatter

```yaml
---
layout: exercise.njk
title: "Titel – Untertitel"            # Untertitel sagt, worum es geht
kategorie: technik                      # koordination | technik | spielformen | kondition | aufwaermen-abschluss
altersgruppen: [F, E]                   # bambini | F | E | D | C | B | A, aufsteigend
spielstaerke: alle                      # alle | einsteiger | fortgeschritten
phase: hauptteil                        # aufwaermen | hauptteil | abschluss
ziel: "Ein Satz, was das Kind danach besser kann."
quelle: "DJK Ottenhofen Trainerteam"
bild: "/assets/uebungen/<slug>.svg"
bildAlt: "Zwei bis vier Sätze, was auf der Skizze zu sehen ist."
---
```

Kein `quelleUrl`. Werte stehen in `src/_data/site.json`; andere Werte brechen den Bau still (leere Labels).

## Abschnitte, genau diese, in dieser Reihenfolge

```markdown
## Aufbau

- **Spielfeld:** Maße in Metern, Form, Tore
- **Material:** Hütchen, Bälle, Leibchen, Minitore, Stangen (Zahlen)
- **Spieler:** Zahl, Teams, Rollen
- **Positionen:** wer steht wo zu Beginn

## Ablauf

1. Nummerierte Schritte, je ein Satz, ein Schritt ist eine Aktion.
2. Wechsel und Rotation als eigener Schritt.
3. Wertung oder Ende als letzter Schritt.

## Coaching-Punkte

- **Kern in drei Wörtern:** ein Satz, der erklärt, worauf der Trainer achtet. Als Zuruf tauglich.
- (drei bis fünf Punkte)

## Varianten

- **Leichter:** …
- **Schwerer:** …
- **(optional) Mit Wettkampf / Mit Torhüter / Für große Gruppen:** …
```

Länge 40 bis 70 Zeilen. Keine weiteren Überschriften, keine Tabellen, keine horizontalen Linien.

## Eigene Fassung

Bei einer Umschreibung: Aus der alten Datei nur die Spielidee und die Maße nehmen. Dann die alte Datei schließen und frei schreiben.

- Kein Satz, keine Aufzählung, keine Überschrift der alten Datei bleibt stehen. Acht gleiche Wörter in Folge sind ein Befund.
- Diese Namen kommen nirgends vor: ADVANCE.FOOTBALL, advance.football, MFS, Münchner Fußball Schule, soccerdrills, fussballbasis, Fußball-Training-Blog, bambini-fussballtraining, owayo, Trainertalk, DFB-Methodik, Levelschießen, sports-graphics, Champions League.
- Titel bleibt, außer er ist ein Fremd- oder Markenname. Dann neuer Titel, der Slug (Dateiname) bleibt, weil Einheiten darüber verlinken.
- Quelle ist immer `DJK Ottenhofen Trainerteam`.

## Sprache nach Alter

| Alter | Ton | Beispiel |
|---|---|---|
| Bambini, F | Bilder, kurze Sätze, Du-Form in den Coaching-Punkten | „Jeder hat einen Ball. Wer den Zauberwald schafft, ohne ein Hütchen zu treffen, bekommt einen Punkt." |
| E | sachlich, aber einfach | „Der Passgeber läuft seinem Pass nach und übernimmt die Position." |
| D und älter | fachlich | „Der ballferne Verteidiger sichert diagonal ab." |

## Codewörter des Spielkonzepts

Einbauen, wo es passt, in den Coaching-Punkten als `**Codewort am Platz:** „…"`. Nur Wörter, die in der Altersgruppe der Übung schon in Gebrauch sind (Spalte „ab", gilt aufwärts):

| ab | Wort | Für die Kinder |
|---|---|---|
| G | Hand / Faust | Haben wir den Ball, machen wir uns breit wie eine offene Hand. Haben sie ihn, rücken wir zusammen wie eine Faust. |
| G | Jagen | Bleib an ihm dran, auch wenn er wieder umdreht. |
| G | Wiese machen / Treiben | Ist Platz vor dir, lauf mit dem Ball los. |
| G | Drinbleiben | Trau dich, das Dribbling zu Ende zu bringen. |
| F | Kopf hoch | Schau kurz auf, nicht nur auf den Ball. |
| F | Anstechen | Siehst du eine Lücke, dribbel rein. |
| F | Arm raus / Arsch raus | Arm und Hintern raus, dann kommt er nicht an den Ball. |
| F | Seitlich stehen | Stell dich schräg zu ihm, nicht frontal davor. |
| F | Hinter dem Ball frei werden | Steht dein Mitspieler unter Druck, geh hinter ihn statt nach vorne. |
| F | Anschluss | Bleib nicht stehen, komm dahin, wo der Ball ist. |
| E | Erste Aktion nach vorne | Der erste Blick geht immer nach vorne. |
| E | Gegner binden | Dribbel ihn an, damit dein Mitspieler frei wird. |
| E | Zentrum / Gefährlich werden | Spiel nach innen statt außen herum, und werde vor dem Tor anspielbar. |
| E | Ball sehen | Bleib geduldig und schau auf den Ball, nicht auf ihn. |
| E | Druck machen | Geh näher ran, damit er nichts mehr machen kann. |
| E | Kontakt | Geh in die Nähe von dem, der als nächstes den Ball bekommt. |
| E | Im Rücken des Gegners / Schwimmen | Stell dich dahin, wo er dich nicht sieht. |
| E | Breit machen | Geht auseinander, macht das Feld groß. |
| E | Anschluss halten | Geht der Ball nach vorne, gehst du mit. |
| E | Steil gehen | Lauf hinter ihre Verteidiger, Richtung Tor. |
| E | Steck durch / Lochpass | Spiel den Ball in die Lücke, dein Mitspieler läuft schon. |
| E | Gegner sehen – innen stehen | Stell dich zwischen ihn und unser Tor. |
| D | Doppeln | Zu zweit auf einen, dann holt ihr den Ball. |
| D | Lenken | Zeig ihm, wohin er laufen soll. |
| D | Tiefgang | Startet einer nach dem anderen nach vorne durch. |
| D | Einlaufen | Lauf von außen hinter ihre letzte Reihe. |
| D | Diagonal | Spiel schräg, nicht quer. |
| D | Überspielen | Ein Pass nach vorne lässt eine ganze Reihe hinter sich. |
| D | Anspielbar oder Gegnerbindung | Entweder du bist frei, oder du beschäftigst einen Gegner. |

Bambini-Übungen nutzen keine Codewörter.

## Kinder, die nicht warten können

In jeder F- und Bambini-Übung gilt, und steht als Prüfpunkt:

- Keine Schlange länger als drei Kinder. Sonst zweite Bahn oder zweites Feld in den Aufbau.
- Wartende haben eine Aufgabe mit Ball („bis du dran bist: Ball mit der Sohle hin und her").
- Erklärung in höchstens drei Sätzen, dann spielen. Regeln kommen nach der ersten Runde dazu.
- Wechsel der Aufgabe nach spätestens 10 bis 12 Minuten (steht in Varianten oder Ablauf).

## Prüfliste (hakt der Prüfer ab)

- [ ] Frontmatter vollständig, Werte aus `site.json`, kein `quelleUrl`
- [ ] Vier Abschnitte in der Reihenfolge Aufbau, Ablauf, Coaching-Punkte, Varianten
- [ ] Keine acht gleichen Wörter in Folge gegenüber `git show main:src/uebungen/<slug>.md`
- [ ] Keine verbotenen Namen (`python tools/pruefe_uebungen.py <slug>` ist grün)
- [ ] Maße in Text und Skizze gleich
- [ ] Ton passt zum Alter, bei F und Bambini Wartezeit-Regel erfüllt
- [ ] `bildAlt` beschreibt die Skizze, nicht die Übung
- [ ] 40 bis 70 Zeilen
