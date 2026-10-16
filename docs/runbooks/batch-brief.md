# Brief-Vorlage für einen Übungs-Batch

Der Orchestrator startet je Batch einen `uebung-autor` und danach einen `uebung-pruefer` mit diesem Text. Platzhalter in spitzen Klammern ersetzen.

## Autor

```
Batch <B4> – <Technik F>. Repo: C:/Repositories/privat/fe-jugend-wissensdatenbank (Branch uebungen-eigen-skizzen, bereits ausgecheckt). Scratch: <S>. Lege <S>/png und <S>/reports an, falls sie fehlen.

Slugs: <slug1>, <slug2>, …

Folge deiner Agent-Anweisung: Runbooks lesen, je Slug Text und SVG neu, rendern, ansehen, Prüfskript grün. Report nach <S>/reports/<B4>.md. Keine Commits.

Hinweise zu diesem Batch: <z. B. „champions-league-torschuss bekommt den Titel ‚Aufstiegs-Torschuss – Torschuss mit Auf- und Abstieg'", „funino: Skizze im F-Maß 25 × 20 m mit vier Minitoren">
```

## Prüfer

```
Prüfe Batch <B4> – <Technik F>. Repo: C:/Repositories/privat/fe-jugend-wissensdatenbank (Branch uebungen-eigen-skizzen). Scratch: <S>. Autor-Report: <S>/reports/<B4>.md.

Slugs: <slug1>, <slug2>, …

Folge deiner Agent-Anweisung. Report nach <S>/reports/<B4>-pruefung.md.
```

## Nach dem Prüfer

- Befunde „hoch" per SendMessage an den Autor-Agenten des Batches: „Befunde aus <S>/reports/<B4>-pruefung.md beheben, nur die genannten Slugs, dann Prüfskript erneut, Report aktualisieren."
- Danach Prüfskript selbst laufen lassen, zwei PNGs ansehen, committen.
