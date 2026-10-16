# Runbook: Feldskizze als SVG

Jede Übung hat genau eine Skizze `src/assets/uebungen/<slug>.svg`. Sie zeigt den Aufbau und eine einzige Beispielaktion. Die Legende (Team A, Team B, Hütchen, Pass, Laufweg) rendert das Template `src/_includes/skizze-legende.njk`, deshalb steht im SVG keine Schrift. Referenz: `src/assets/uebungen/steilgang-1gegen1.svg`.

## Maß und Rahmen

- 1 m = 10 Einheiten. Feld B × H Meter → `viewBox="-10 -10 <10B+20> <10H+20>"`. Rand 10 Einheiten ringsum.
- Querformat bevorzugt (Breite ≥ Höhe). Hochkant nur, wenn die Spielrichtung auf ein Tor zeigt (Torschuss, 1-gegen-1 aufs Tor), dann Tor oben.
- Kein Feld größer als 50 × 40 m in der Skizze; bei Parcours und Staffeln den relevanten Ausschnitt zeigen.
- `role="img"` am `<svg>`, erstes Kind `<title>` mit einem deutschen Satz, der die Skizze beschreibt.

## Grundgerüst

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -10 320 220" role="img">
  <title>Feldskizze …: …</title>
  <defs>
    <marker id="pfeil-weiss" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#fff"/></marker>
    <marker id="pfeil-gelb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#FFF300"/></marker>
    <marker id="pfeil-schwarz" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#111"/></marker>
  </defs>
  <rect x="-10" y="-10" width="320" height="220" fill="#2E7D32"/>
  <!-- Feld 30 x 20 m -->
  <rect x="0" y="0" width="300" height="200" fill="none" stroke="#fff" stroke-width="1.5"/>
  …
</svg>
```

Kommentare (`<!-- -->`) vor jeder Gruppe: Feld, Zonen, Tore, Hütchen, Wege, Spieler, Ball. Der Prüfer liest sie gegen den Aufbau-Text.

## Symbole

| Element | SVG |
|---|---|
| Rasen | `<rect>` über die ganze viewBox, `fill="#2E7D32"` |
| Feldlinie | weiß, `stroke-width="1.5"`, `fill="none"` |
| Mittellinie, Hilfslinie | weiß, `stroke-width="1"`, `stroke-dasharray="3 4"`, `opacity=".8"` |
| Zone | `<rect>` weiß, `fill-opacity=".12"`, ohne Rand, oder mit gestricheltem Rand wie Hilfslinie |
| Team A (Spieler) | `<circle r="7" fill="#FFF300" stroke="#111" stroke-width="1.5"/>` |
| Team B (Spieler) | `<circle r="7" fill="#111" stroke="#fff" stroke-width="1.5"/>` |
| Torhüter | wie sein Team, `stroke="#fff" stroke-width="3"` |
| Fänger (Fangspiele) | Team B mit zusätzlichem Ring `<circle r="10" fill="none" stroke="#FFF300" stroke-width="1.5"/>` |
| Nummer im Kreis | `<text x="cx" y="cy+3.2" font-family="Arial, sans-serif" font-size="9" font-weight="700" fill="#111" text-anchor="middle">1</text>` (auf Team B `fill="#fff"`). Einzige erlaubte Schrift. |
| Ball | `<circle r="3" fill="#fff" stroke="#111" stroke-width="1"/>` |
| Hütchen | `<polygon points="x,y-4 x+4,y+4 x-4,y+4" fill="#F28C28"/>` (Seite 8, Spitze oben) |
| Hütchentor / Minitor | zwei Hütchen im Abstand 20 (2 m), oder `<rect width="20" height="4">` weiß `fill-opacity=".25"` `stroke="#fff" stroke-width="2"` |
| Großes Tor (5 m) | `<rect width="50" height="7">` weiß `fill-opacity=".25"` `stroke="#fff" stroke-width="2"`, außerhalb der Feldlinie (z. B. `y="-7"`) |
| Stange | `<rect width="2" height="16" fill="#fff"/>`, Mitte auf dem Punkt |
| Reifen | `<circle r="5" fill="#fff" fill-opacity=".15" stroke="#fff" stroke-width="1.5"/>` |
| Koordinationsleiter | `<rect width="20" height="L" fill="none" stroke="#fff" stroke-width="1.5"/>` plus Sprossen `<line>` alle 5 Einheiten |
| Pass | `<path d="M… L…" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#pfeil-weiss)"/>` |
| Flugball | wie Pass, aber `d="M… Q… …"` (Bogen) |
| Schuss | `<path … stroke="#fff" stroke-width="2.5" marker-end="url(#pfeil-weiss)"/>` ohne Strichelung |
| Laufweg Team A | `<path … stroke="#FFF300" stroke-width="2.5" marker-end="url(#pfeil-gelb)"/>` |
| Laufweg Team B | `<path … stroke="#111" stroke-width="2.5" marker-end="url(#pfeil-schwarz)"/>` |
| Dribbling | Laufweg als Wellenlinie: `d="M x,y q 8,-6 16,0 t 16,0 t 16,0"` in Teamfarbe |

Farben und Maße nicht abwandeln. Keine Verläufe, keine Schatten, keine Emoji, keine Beschriftung von Zonen.

## Was die Skizze zeigt

- Den Aufbau vollständig (Feld, Tore, Hütchen, Zonen) in den Maßen aus dem Abschnitt „Aufbau" der Übung.
- Einen Ausschnitt der Spieler: 3 bis 6 je Team, bei Einzelübungen 2 bis 4 Kinder. Nicht alle zwölf.
- Genau eine Beispielaktion: ein Pass plus ein Laufweg, oder ein Dribbling, oder ein Schuss. Nicht den ganzen Ablauf.
- Bei Sammlungen (Ideensammlung, Stationen) die Grundform oder eine Station.
- Bei Parcours den Rundkurs mit den Stationen als Hütchen/Stangen/Leiter und einem Laufweg.

## Prüfen

```bash
magick -density 150 src/assets/uebungen/<slug>.svg <scratch>/png/<slug>.png
```

PNG ansehen (Read-Tool). Prüfliste:

- [ ] viewBox passt zu den Maßen im Text (Breite/Höhe = 10 × Meter + 20)
- [ ] Nichts ragt über den grünen Rand hinaus, Tore außerhalb der Feldlinie sitzen im Rand
- [ ] Pfeilspitzen sichtbar, Pfeil endet vor dem Spieler, nicht im Kreis
- [ ] Ziffern zentriert im Kreis
- [ ] Nur ein `<title>`, kein anderer Text
- [ ] Dateiname = Slug, `bild` in der Übung zeigt auf `/assets/uebungen/<slug>.svg`
- [ ] `bildAlt` beschreibt: Format, Tore, Hütchen, welche Spieler, welche Aktion (2 bis 4 Sätze)
