# Eltern-Konzept auf öffentliche Site — Implementierungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Andis elternrelevante Konzept-Teile als mobil-freundliches Accordion auf `/eltern/` bringen, plus Impressum/Datenschutz und ein „von Trainern, nicht vom Verein"-Framing — statt Word-Datei-Versand.

**Architecture:** Reine Eleventy-Content-/Template-Änderung. Accordion via natives `<details>/<summary>` (kein JS), Styles im bestehenden Gelb/Schwarz-Theme. Font Sen wird selbst gehostet (Google-CDN raus). Zwei neue statische Rechtsseiten.

**Tech Stack:** Eleventy 3 (Nunjucks), Vanilla CSS. Kein Test-Framework.

> **Verifikation statt Unit-Tests:** Dieses Projekt hat keine Tests. „Test" = Eleventy-Build (`npx @11ty/eleventy`) erfolgreich + `grep` im gebauten `_site/`-Output auf erwartete Inhalte + zum Schluss Browser-Preview (mobil). Alle Befehle laufen im **öffentlichen** Repo: `C:/Users/MauricioSchäpers/claude-cowork/fe-jugend-wissensdatenbank`.

> **Branch:** Arbeit läuft auf `eltern-konzept` (bereits angelegt, enthält den Spec-Commit). Nicht nach `main` committen — Deploy erfolgt erst nach Merge.

---

## Dateiübersicht

- **Neu:** `src/impressum.njk`, `src/datenschutz.njk`
- **Neu:** `src/assets/fonts/sen-400.woff2`, `sen-700.woff2`, `sen-800.woff2`
- **Ändern:** `src/eltern.njk` (Komplett-Neufassung), `src/_includes/base.njk` (Footer + Font-Links), `src/assets/css/style.css` (Accordion/Callout/Legal-Styles + `@font-face`)

---

## Task 1: Sen-Font selbst hosten

**Files:**
- Create: `src/assets/fonts/sen-400.woff2`, `src/assets/fonts/sen-700.woff2`, `src/assets/fonts/sen-800.woff2`
- Modify: `src/assets/css/style.css` (oben `@font-face` einfügen)
- Modify: `src/_includes/base.njk:8-10` (Google-Fonts-Links entfernen)

- [ ] **Step 1: Font-Dateien herunterladen (OFL, self-host erlaubt)**

Run (Git Bash):
```bash
cd "C:/Users/MauricioSchäpers/claude-cowork/fe-jugend-wissensdatenbank"
mkdir -p src/assets/fonts
curl -L "https://gwfh.mranftl.com/api/fonts/sen?download=zip&subsets=latin&variants=regular,700,800&formats=woff2" -o /tmp/sen.zip
unzip -o /tmp/sen.zip -d /tmp/sen
mv /tmp/sen/sen-v*-latin-regular.woff2 src/assets/fonts/sen-400.woff2
mv /tmp/sen/sen-v*-latin-700.woff2     src/assets/fonts/sen-700.woff2
mv /tmp/sen/sen-v*-latin-800.woff2     src/assets/fonts/sen-800.woff2
ls -l src/assets/fonts/
```
Expected: drei `.woff2`-Dateien, jeweils > 10 KB. Falls die gwfh-API scheitert, Alternative: auf https://gwfh.mranftl.com/fonts/sen Font „Sen" mit Charset „latin" und Styles 400/700/800 im woff2-Format herunterladen und die drei Dateien manuell als `sen-400/700/800.woff2` ablegen.

- [ ] **Step 2: `@font-face` an den Anfang von `style.css` setzen**

Ganz oben in `src/assets/css/style.css` einfügen (vor `:root{`):
```css
/* Sen — selbst gehostet (OFL). Ersetzt das Google-Fonts-CDN. */
@font-face{
  font-family:"Sen"; font-style:normal; font-weight:400; font-display:swap;
  src:url("../fonts/sen-400.woff2") format("woff2");
}
@font-face{
  font-family:"Sen"; font-style:normal; font-weight:700; font-display:swap;
  src:url("../fonts/sen-700.woff2") format("woff2");
}
@font-face{
  font-family:"Sen"; font-style:normal; font-weight:800; font-display:swap;
  src:url("../fonts/sen-800.woff2") format("woff2");
}

```
(Relative URLs `../fonts/...` sind pathPrefix-sicher, weil CSS von HtmlBasePlugin nicht umgeschrieben wird.)

- [ ] **Step 3: Google-Fonts-Links aus `base.njk` entfernen**

In `src/_includes/base.njk` die drei Zeilen 8–10 löschen:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sen:wght@400;700;800&display=swap" rel="stylesheet">
```
Die Zeile `<link rel="stylesheet" href="/assets/css/style.css">` bleibt.

- [ ] **Step 4: Build + prüfen, dass keine Google-Referenz mehr existiert**

Run:
```bash
cd "C:/Users/MauricioSchäpers/claude-cowork/fe-jugend-wissensdatenbank"
npx @11ty/eleventy
grep -rc "fonts.googleapis.com\|fonts.gstatic.com" _site/ | grep -v ':0' || echo "OK: keine Google-Fonts-Referenz"
ls _site/assets/fonts/
```
Expected: `OK: keine Google-Fonts-Referenz`, und drei woff2-Dateien in `_site/assets/fonts/`.

- [ ] **Step 5: Commit**

```bash
git add src/assets/fonts/ src/assets/css/style.css src/_includes/base.njk
git commit -m "feat: Sen-Font selbst hosten, Google-Fonts-CDN entfernen"
```

---

## Task 2: Footer neu rahmen (Trainer-geführt) + Legal-Links

**Files:**
- Modify: `src/_includes/base.njk` (Footer-Block, Zeilen ~63–84)
- Modify: `src/assets/css/style.css` (`.footer-legal` ergänzen)

- [ ] **Step 1: Footer-Brand-Absatz ersetzen**

In `src/_includes/base.njk`, im `<div class="footer-brand">`:

Alt:
```html
<p>Sportgemeinschaft seit 1956 · {{ site.subtitle }}</p>
```
Neu:
```html
<p>Private, ehrenamtliche Trainerseite der F-/E-Jugend. Keine offiziellen Mitteilungen des DJK Ottenhofen e.V.</p>
```

- [ ] **Step 2: Footer-Kontakt auf Trainer-Mail umstellen**

Alt:
```html
    <div class="footer-contact">
      <h4>Kontakt</h4>
      <p>Jugendleitung F/E-Jugend<br>jugend@djk-ottenhofen.de</p>
      <p>DJK Ottenhofen e.V.<br>Sportgelände, Ottenhofen</p>
    </div>
```
Neu:
```html
    <div class="footer-contact">
      <h4>Kontakt</h4>
      <p>Trainerteam F-/E-Jugend<br><a href="mailto:hallo+djk@mauricio.de">hallo+djk@mauricio.de</a></p>
      <p>Die Kinder spielen für den<br>DJK Ottenhofen e.V.</p>
    </div>
```

- [ ] **Step 3: Footer-Bottom: Copyright ändern + Legal-Links**

Alt:
```html
  <div class="footer-bottom container">
    <p>© 2026 DJK Ottenhofen e.V. — 70 Jahre Sportgemeinschaft</p>
  </div>
```
Neu:
```html
  <div class="footer-bottom container">
    <p>© 2026 Trainerteam F-/E-Jugend · privat &amp; ehrenamtlich betrieben</p>
    <nav class="footer-legal" aria-label="Rechtliches">
      <a href="/impressum/">Impressum</a>
      <a href="/datenschutz/">Datenschutz</a>
    </nav>
  </div>
```

- [ ] **Step 4: `.footer-legal`-Style ergänzen**

Ans Ende von `src/assets/css/style.css` anhängen:
```css
/* Footer-Legal-Links */
.footer-legal{ display:flex; gap: var(--space-4); }
.footer-legal a{ font-weight: var(--fw-bold); }
.footer-legal a:hover{ text-decoration: underline; }
```

- [ ] **Step 5: Build + prüfen**

Run:
```bash
npx @11ty/eleventy
grep -c "hallo+djk@mauricio.de" _site/eltern/index.html
grep -c "privat &amp; ehrenamtlich betrieben\|privat & ehrenamtlich betrieben" _site/eltern/index.html
grep -o "/djk-ottenhofen-jugend/impressum/" _site/eltern/index.html | head -1
```
Expected: Kontakt-Mail und Copyright-Zeile vorhanden (Count ≥ 1); Impressum-Link mit pathPrefix vorhanden. (Kein `DJK Ottenhofen e.V.` mehr als Copyright-Inhaber.)

- [ ] **Step 6: Commit**

```bash
git add src/_includes/base.njk src/assets/css/style.css
git commit -m "feat: Footer als trainer-gefuehrt rahmen, Legal-Links ergaenzen"
```

---

## Task 3: Impressum-Seite

**Files:**
- Create: `src/impressum.njk`
- Modify: `src/assets/css/style.css` (`.legal-page` ergänzen)

- [ ] **Step 1: `.legal-page`-Style ergänzen**

Ans Ende von `src/assets/css/style.css` anhängen:
```css
/* Rechtsseiten (Impressum / Datenschutz) */
.legal-page{ max-width: 70ch; }
.legal-page h3{ font-size: var(--fs-500); margin: var(--space-6) 0 var(--space-3); }
.legal-page p{ color: var(--color-grey-700); margin-bottom: var(--space-3); }
```

- [ ] **Step 2: `src/impressum.njk` anlegen**

```njk
---
layout: base.njk
title: "Impressum"
permalink: "/impressum/"
---
<section class="section">
  <div class="container legal-page">
    <div class="section-head">
      <h2>Impressum</h2>
    </div>

    <h3>Angaben gemäß § 5 DDG</h3>
    <p>Mauricio Schäpers<br>An der Hofmark 29<br>85570 Ottenhofen</p>

    <h3>Kontakt</h3>
    <p>E-Mail: <a href="mailto:hallo+djk@mauricio.de">hallo+djk@mauricio.de</a></p>

    <h3>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h3>
    <p>Mauricio Schäpers, Anschrift wie oben.</p>

    <h3>Hinweis</h3>
    <p>Dieses Angebot wird privat und ehrenamtlich vom Trainerteam der F-/E-Jugend betrieben. Es ist kein offizielles Angebot des DJK Ottenhofen e.V.</p>

    <h3>Haftung für Inhalte und Links</h3>
    <p>Die Inhalte dieser Seiten wurden mit Sorgfalt erstellt. Für Richtigkeit, Vollständigkeit und Aktualität können wir keine Gewähr übernehmen. Für die Inhalte verlinkter externer Seiten sind deren Betreiber verantwortlich; zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.</p>
  </div>
</section>
```

- [ ] **Step 3: Build + prüfen**

Run:
```bash
npx @11ty/eleventy
test -f _site/impressum/index.html && echo "OK: Impressum gebaut"
grep -c "§ 5 DDG" _site/impressum/index.html
grep -c "An der Hofmark 29" _site/impressum/index.html
```
Expected: `OK: Impressum gebaut`, beide Counts ≥ 1.

- [ ] **Step 4: Commit**

```bash
git add src/impressum.njk src/assets/css/style.css
git commit -m "feat: Impressum-Seite"
```

---

## Task 4: Datenschutz-Seite

**Files:**
- Create: `src/datenschutz.njk`

- [ ] **Step 1: `src/datenschutz.njk` anlegen**

```njk
---
layout: base.njk
title: "Datenschutzerklärung"
permalink: "/datenschutz/"
---
<section class="section">
  <div class="container legal-page">
    <div class="section-head">
      <h2>Datenschutzerklärung</h2>
    </div>

    <h3>Verantwortlicher</h3>
    <p>Mauricio Schäpers<br>An der Hofmark 29<br>85570 Ottenhofen<br>E-Mail: <a href="mailto:hallo+djk@mauricio.de">hallo+djk@mauricio.de</a></p>

    <h3>Grundsätzliches</h3>
    <p>Diese Website ist ein statisches Informationsangebot. Wir erheben selbst keine personenbezogenen Daten, setzen keine Cookies und verwenden keine Analyse- oder Tracking-Dienste.</p>

    <h3>Hosting (GitHub Pages)</h3>
    <p>Die Seite wird bei GitHub Pages gehostet (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Server-Logdaten, darunter die IP-Adresse. Rechtsgrundlage ist unser berechtigtes Interesse an einem sicheren und stabilen Betrieb (Art. 6 Abs. 1 lit. f DSGVO). Weitere Informationen in der <a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">Datenschutzerklärung von GitHub</a>.</p>

    <h3>Schriftarten</h3>
    <p>Die verwendete Schriftart wird lokal von diesem Server ausgeliefert. Es werden keine Schriftarten von Google-Servern oder anderen Dritten nachgeladen.</p>

    <h3>Externe Links</h3>
    <p>Diese Seite verlinkt auf externe Angebote (z. B. den Bayerischen Fußball-Verband). Für deren Datenverarbeitung sind die jeweiligen Betreiber verantwortlich.</p>

    <h3>Kommunikation über WhatsApp</h3>
    <p>Absprachen zu Training und Spielen laufen teils über WhatsApp-Gruppen. Das geschieht außerhalb dieser Website und unterliegt den Datenschutzbestimmungen des jeweiligen Anbieters. Die Teilnahme ist freiwillig.</p>

    <h3>Deine Rechte</h3>
    <p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung sowie Widerspruch. Zudem besteht ein Beschwerderecht bei der zuständigen Aufsichtsbehörde (Bayerisches Landesamt für Datenschutzaufsicht, Ansbach).</p>
  </div>
</section>
```

- [ ] **Step 2: Build + prüfen**

Run:
```bash
npx @11ty/eleventy
test -f _site/datenschutz/index.html && echo "OK: Datenschutz gebaut"
grep -c "GitHub Pages" _site/datenschutz/index.html
grep -c "lokal von diesem Server" _site/datenschutz/index.html
```
Expected: `OK: Datenschutz gebaut`, beide Counts ≥ 1.

- [ ] **Step 3: Commit**

```bash
git add src/datenschutz.njk
git commit -m "feat: Datenschutzerklaerung"
```

---

## Task 5: Accordion-, Callout- und Jump-Nav-Styles

**Files:**
- Modify: `src/assets/css/style.css` (ans Ende anhängen)

- [ ] **Step 1: Styles anhängen**

Ans Ende von `src/assets/css/style.css`:
```css
/* =====================================================================
   COMPONENT: Eltern — Jump-Nav, Accordion, Callout
   ===================================================================== */
.parents-note{ font-size: var(--fs-200); color: var(--color-grey-600); font-weight: var(--fw-bold); margin-top: var(--space-3); }
.trainer-line{ font-size: var(--fs-200); }

.jump-nav{ display:flex; flex-wrap:wrap; gap: var(--space-2); margin-bottom: var(--space-7); }

.accordion{ display:flex; flex-direction:column; gap: var(--space-3); margin: var(--space-6) 0; }
.accordion-item{
  border:1px solid var(--color-grey-200); border-radius: var(--radius-md);
  background: var(--color-white); overflow:hidden;
  scroll-margin-top: calc(var(--header-h) + 1rem);
}
.accordion-item > summary{
  list-style:none; cursor:pointer;
  display:flex; align-items:center; justify-content:space-between; gap: var(--space-3);
  padding: var(--space-4) var(--space-5);
  font-weight: var(--fw-black); font-size: var(--fs-400);
}
.accordion-item > summary::-webkit-details-marker{ display:none; }
.accordion-item > summary:hover{ background: var(--color-grey-100); }
.accordion-item[open] > summary{ background: var(--color-grey-100); border-bottom:1px solid var(--color-grey-200); }
.accordion-chevron{ color: var(--color-grey-600); transition: transform .15s ease; }
.accordion-item[open] .accordion-chevron{ transform: rotate(90deg); }
.accordion-body{ padding: var(--space-5); }
.accordion-body > * + *{ margin-top: var(--space-4); }
.accordion-body p{ color: var(--color-grey-700); max-width: 65ch; }
.accordion-body h4{ font-size: var(--fs-400); }
.accordion-body ul{ list-style: disc; padding-left: 1.25em; display:flex; flex-direction:column; gap:.4rem; }
.accordion-body li{ color: var(--color-grey-700); }
.accordion-body .value-list{ list-style:none; padding-left:0; }

.callout{
  background: var(--color-tint-bg); border:1px solid var(--color-tint-border);
  border-radius: var(--radius-md); padding: var(--space-5);
}
.callout h4{ color: var(--color-tint-ink); margin-bottom: var(--space-3); }
.callout p{ color: var(--color-grey-700); }
.callout a{ font-weight: var(--fw-bold); }
```

- [ ] **Step 2: Build (Smoke-Test, Styles werden erst mit Task 6 sichtbar)**

Run:
```bash
npx @11ty/eleventy
grep -c "accordion-item" _site/assets/css/style.css
```
Expected: Count ≥ 1 (CSS ist durchgereicht).

- [ ] **Step 3: Commit**

```bash
git add src/assets/css/style.css
git commit -m "feat: Accordion-, Callout- und Jump-Nav-Styles"
```

---

## Task 6: `/eltern/` neu aufbauen (Accordion + Konzept-Inhalte)

**Files:**
- Modify: `src/eltern.njk` (Komplett-Neufassung)

- [ ] **Step 1: `src/eltern.njk` komplett ersetzen**

Gesamter neuer Datei-Inhalt:
```njk
---
layout: base.njk
title: "Für Eltern"
permalink: "/eltern/"
---
<section class="section section-parents" id="fuer-eltern">
  <div class="container">
    <div class="section-head">
      <h2>Für Eltern</h2>
      <p class="section-lead">Herzlich willkommen! Hier findet ihr, wie wir mit den Kindern der F- und E-Jugend arbeiten, was uns wichtig ist und alles Organisatorische auf einen Blick. Bei Fragen sprecht uns jederzeit an.</p>
      <p class="parents-note">Diese Seite pflegt ehrenamtlich das Trainerteam der F-/E-Jugend – sie ist keine offizielle Vereinsseite.</p>
    </div>

    <nav class="jump-nav" aria-label="Abschnitte">
      <a class="chip" href="#zeiten">🗓️ Zeiten &amp; Termine</a>
      <a class="chip" href="#kinderschutz">🛡️ Kinderschutz</a>
      <a class="chip" href="#spielfeldrand">📣 Am Spielfeldrand</a>
      <a class="chip" href="#so-spielen">⚽ So spielen wir</a>
      <a class="chip" href="#werte">🤝 Werte &amp; Fair Play</a>
      <a class="chip" href="#massnahmen">💬 Wenn's mal nicht klappt</a>
    </nav>

    <div class="parents-layout">
      <div class="parents-main">
        <h3>So trainieren wir</h3>
        <p>Bei uns ist jedes Kind möglichst oft am Ball. Wir spielen in kleinen Gruppen auf kleinen Feldern – viele Ballkontakte, viele Erfolgserlebnisse, wenig Warten. Statt langer Lauf- und Dehnübungen startet das Training direkt mit einem Spiel. Fußball lernt man am besten, indem man Fußball spielt.</p>

        <blockquote class="pull-quote">„Freude ist der Motor – Kinder, die Spaß haben, bleiben dabei und lernen schneller."</blockquote>

        <p class="trainer-line"><strong>Euer Trainerteam:</strong> Mauricio &amp; Stefan (F-Jugend) · Byron, Andreas &amp; Julian (E-Jugend). Julian ist ehemaliger DJK-Jugendspieler und sammelt jetzt Erfahrung als Trainer.</p>

        <h3>Warum Kinder beim Sport bleiben – oder aufhören</h3>
        <p>Die Sportwissenschaft, an der sich auch die DFB-Kinderfußball-Philosophie orientiert, zeigt recht deutlich, was Kinder im Verein hält und was sie fernbleiben lässt. Das nehmen wir uns zu Herzen:</p>

        <h4>Was Kinder dabeibleiben lässt</h4>
        <ul class="value-list">
          <li>
            <span class="value-icon">😄</span>
            <div><strong>Spaß und Freude</strong><p>Der wichtigste Grund überhaupt: Das Training macht einfach Freude.</p></div>
          </li>
          <li>
            <span class="value-icon">🏆</span>
            <div><strong>Erfolgserlebnisse</strong><p>Kleine Erfolge – ein gelungener Trick, ein Tor, ein gutes Spiel – geben Auftrieb.</p></div>
          </li>
          <li>
            <span class="value-icon">📈</span>
            <div><strong>Etwas dazulernen</strong><p>Fortschritt spüren und sich verbessern hält die Motivation oben.</p></div>
          </li>
          <li>
            <span class="value-icon">👫</span>
            <div><strong>Freunde und Zusammenhalt</strong><p>Die Gruppe ist Kindern oft genauso wichtig wie der Fußball selbst.</p></div>
          </li>
          <li>
            <span class="value-icon">🧡</span>
            <div><strong>Gelassene Eltern</strong><p>Eine entspannte, unterstützende Haltung am Spielfeldrand gibt Rückhalt.</p></div>
          </li>
        </ul>

        <h4>Was die Lust nimmt</h4>
        <ul class="value-list">
          <li>
            <span class="value-icon">😟</span>
            <div><strong>„Ich bin nicht gut genug"</strong><p>Das Gefühl, nicht mitzuhalten, ist einer der häufigsten Gründe zum Aufhören.</p></div>
          </li>
          <li>
            <span class="value-icon">😬</span>
            <div><strong>Zu viel Ernst und Druck</strong><p>Wenn sich Training wie Pflicht statt Spiel anfühlt, bleibt die Freude auf der Strecke.</p></div>
          </li>
          <li>
            <span class="value-icon">🥅</span>
            <div><strong>Nur das Ergebnis zählt</strong><p>Wenn allein der Sieg wichtig ist, verliert das Spielen an sich seinen Reiz.</p></div>
          </li>
          <li>
            <span class="value-icon">⚖️</span>
            <div><strong>Ungleichbehandlung</strong><p>Wer sich zurückgesetzt fühlt, verliert schnell die Lust.</p></div>
          </li>
          <li>
            <span class="value-icon">😩</span>
            <div><strong>Überforderung</strong><p>Zu hohe Erwartungen schrecken ab, statt anzuspornen.</p></div>
          </li>
        </ul>

        <h3>Unser Konzept – zum Aufklappen</h3>
        <p>Alles Wichtige zu Terminen, Kinderschutz, Verhalten am Spielfeldrand und unseren Werten – tippt einfach auf einen Abschnitt.</p>

        <div class="accordion">
          <details class="accordion-item" id="zeiten" open>
            <summary>🗓️ Trainingszeiten &amp; Termine <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <ul>
                <li><strong>Training:</strong> Dienstag &amp; Donnerstag, 17:00–18:30 Uhr.</li>
                <li><strong>Saisonstart:</strong> 15. September 2026.</li>
                <li><strong>Sommerferien:</strong> Training nach Verfügbarkeit – Termine kommen rechtzeitig per WhatsApp-Umfrage.</li>
                <li><strong>Winter:</strong> einmal pro Woche Hallentraining (Zeiten per WhatsApp).</li>
                <li><strong>Heimspiele E-Jugend:</strong> Freitag, Anstoß 17:00 Uhr – Treffpunkt in der Regel 60 Minuten vorher.</li>
                <li><strong>Teilnahme:</strong> Vor jedem Training und Spiel gibt es eine Abfrage per WhatsApp – bitte zuverlässig und rechtzeitig zurückmelden.</li>
                <li><strong>Pflicht:</strong> Schienbeinschoner bei Training und Spiel.</li>
              </ul>
            </div>
          </details>

          <details class="accordion-item" id="kinderschutz">
            <summary>🛡️ Kinderschutz <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <p>Der Schutz und das Wohl der Kinder stehen bei uns an erster Stelle. Dafür gelten klare Regeln:</p>
              <ul>
                <li>Alle Trainer legen ein erweitertes polizeiliches Führungszeugnis vor.</li>
                <li>Umkleide und Dusche bleiben transparent: Ein Trainer ist nie allein mit einem Kind in der Kabine, Duschen ist freiwillig.</li>
                <li>Nähe und Distanz: Körperkontakt nur im sportlichen Rahmen (z. B. Erste Hilfe), immer respektvoll und transparent.</li>
                <li>Keine privaten Einzeltreffen zwischen Trainer und Kind. Ausnahmen (z. B. Fahrt zum Auswärtsspiel) nur mit Zustimmung der Eltern.</li>
                <li>In der Umkleide gilt für die Kinder Handyverbot – Ausnahme: kurz die Familie kontaktieren.</li>
                <li>Ein Erste-Hilfe-Koffer ist bei Training und Spiel verfügbar.</li>
              </ul>
              <p>Bitte sprecht auch mit euren Kindern regelmäßig über diese Punkte.</p>
              <div class="callout">
                <h4>Ansprechpartner Kinderschutz</h4>
                <p>Bei Fragen, Beobachtungen oder Unsicherheiten könnt ihr euch jederzeit vertrauensvoll an das Trainerteam wenden – auch anonym.</p>
                <p>Unabhängige Stelle beim Bayerischen Fußball-Verband:<br>
                Referat Prävention &amp; Schutz vor Gewalt<br>
                E-Mail: <a href="mailto:praevention@bfv.de">praevention@bfv.de</a><br>
                Telefon: 089 / 542 770-707<br>
                <a href="https://www.bfv.de/kinderschutz" target="_blank" rel="noopener">www.bfv.de/kinderschutz</a></p>
              </div>
            </div>
          </details>

          <details class="accordion-item" id="spielfeldrand">
            <summary>📣 Am Spielfeldrand <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <p>So helft ihr euren Kindern am meisten – ein paar Bitten für Trainings- und Spieltage:</p>
              <ul>
                <li>Anweisungen geben nur die Trainer. So bekommen die Kinder klare, einheitliche Ansagen.</li>
                <li>Feuert euer Kind und das ganze Team positiv und lautstark an.</li>
                <li>Bitte haltet angemessenen Abstand zum Spielfeld.</li>
                <li>Verzichtet auf Kritik an Kindern, gegnerischen Spielern und Schiedsrichtern – auch wenn's mal schwerfällt.</li>
              </ul>
              <h4>Aufsichtspflicht</h4>
              <p>Unsere Aufsichtspflicht beginnt mit dem Trainingsstart und endet mit dem Trainingsende (in der Regel 17:00–18:30 Uhr), bei Spielen ab dem Treffpunkt bis Spielende. Der Hin- und Heimweg liegt in der Verantwortung der Eltern.</p>
            </div>
          </details>

          <details class="accordion-item" id="so-spielen">
            <summary>⚽ So spielen &amp; trainieren wir <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <ul>
                <li>F- und E-Jugend trainieren gemeinsam. Wir bilden Gruppen nach aktueller Spielstärke – nicht strikt nach Alter –, damit jedes Kind passende Herausforderungen bekommt.</li>
                <li>Wir trainieren in Stationen: Koordination, Technik, Kondition und viele kleine Spielformen. Ziel sind möglichst viele Ballkontakte für jedes Kind.</li>
                <li>Zum Abschluss gibt es meist ein Abschlussspiel – als Belohnung für Einsatz und gutes Miteinander.</li>
                <li>Einsätze bei Spielen verteilen wir über die Saison möglichst fair; jedes Kind bekommt Spielzeit. Zusätzliche Freundschaftsspiele schaffen weitere Einsätze für alle.</li>
              </ul>
            </div>
          </details>

          <details class="accordion-item" id="werte">
            <summary>🤝 Unsere Werte &amp; Fair Play <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <ul class="value-list">
                <li>
                  <span class="value-icon">🤝</span>
                  <div><strong>Miteinander &amp; Respekt</strong><p>Wir gehen freundlich und hilfsbereit miteinander um, hören einander zu und respektieren Trainer, Mitspieler, Gegner und Schiedsrichter. Schimpfwörter gibt es nicht – auch nicht „im Spaß".</p></div>
                </li>
                <li>
                  <span class="value-icon">💬</span>
                  <div><strong>Fehler sind erlaubt</strong><p>Bei Fehlern machen wir keine Vorwürfe. Wir bleiben positiv – die Trainer korrigieren und begleiten.</p></div>
                </li>
                <li>
                  <span class="value-icon">🎯</span>
                  <div><strong>Disziplin &amp; Einsatz</strong><p>Bei Erklärungen hören wir zu, halten unsere Positionen und geben vollen Einsatz.</p></div>
                </li>
                <li>
                  <span class="value-icon">⚖️</span>
                  <div><strong>Fair Play</strong><p>Wir verhalten uns fair gegenüber Gegnern – auch bei unfairen Aktionen bleiben wir diszipliniert.</p></div>
                </li>
                <li>
                  <span class="value-icon">💪</span>
                  <div><strong>Positive Einstellung</strong><p>Auch auf der Bank oder auf einer ungewohnten Position bleiben wir motiviert und unterstützen das Team.</p></div>
                </li>
                <li>
                  <span class="value-icon">😄</span>
                  <div><strong>Freude zuerst</strong><p>Spaß steht vor dem Ergebnis. Jedes Kind wird nach seiner Spielstärke gefördert.</p></div>
                </li>
              </ul>
            </div>
          </details>

          <details class="accordion-item" id="massnahmen">
            <summary>💬 Wenn's mal nicht klappt <svg class="icon accordion-chevron"><use href="#icon-chevron"></use></svg></summary>
            <div class="accordion-body">
              <p>Damit sich alle wohlfühlen, haben wir klare Schritte, falls Regeln verletzt werden. Sie kommen selten vor:</p>
              <ol class="step-list">
                <li>Freundlicher Hinweis und Erklärung, warum das Verhalten nicht okay ist.</li>
                <li>Kurze Auszeit vom Training oder Abschlussspiel.</li>
                <li>Gespräch mit den Eltern.</li>
              </ol>
              <p>Ziel ist immer ein sicheres, respektvolles und positives Umfeld für alle Kinder.</p>
            </div>
          </details>
        </div>

        <h3>Was dein Kind bei uns lernt</h3>
        <p>Neben Ballgefühl und Technik geht es um Bewegungsfreude, Selbstvertrauen und Teamgeist. Wir setzen auf eine breite, vielseitige Grundausbildung – auch andere Sportarten sind willkommen; eine frühe Spezialisierung nur auf Fußball ist kein Ziel.</p>
      </div>

      <div class="parents-side">
        <div class="info-card">
          <h3>Auf einen Blick</h3>
          <ul class="check-list">
            <li><svg class="icon"><use href="#icon-check"></use></svg> Training: Di &amp; Do, 17:00–18:30</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Saisonstart: 15.09.2026</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Pflicht: Schienbeinschoner</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Infos &amp; Abfragen: WhatsApp-Gruppe</li>
          </ul>
        </div>

        <div class="info-card">
          <h3>Das lernt dein Kind</h3>
          <ul class="check-list">
            <li><svg class="icon"><use href="#icon-check"></use></svg> Ballgefühl &amp; Technik</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Bewegung &amp; Koordination</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Selbstvertrauen</li>
            <li><svg class="icon"><use href="#icon-check"></use></svg> Teamgeist</li>
          </ul>
        </div>

        <div class="info-card info-card--tint">
          <h3>So machst du mit</h3>
          <ol class="step-list">
            <li>Eine Trainerin/einen Trainer ansprechen oder über die Eltern-WhatsApp-Gruppe melden.</li>
            <li>Zum Schnuppertraining vorbeikommen – unkompliziert und jederzeit.</li>
            <li>Dabei bleiben.</li>
          </ol>
          <p><strong>Mitbringen:</strong> Schienbeinschoner (Pflicht), Hallen-/Fußballschuhe, Getränk.</p>
        </div>
      </div>
    </div>

    <p class="card-source">Diese Seite ersetzt kein persönliches Gespräch – sprecht uns jederzeit an.</p>
  </div>
</section>
```

- [ ] **Step 2: Build + Inhalts-Checks**

Run:
```bash
npx @11ty/eleventy
grep -c 'class="accordion-item"' _site/eltern/index.html          # erwartet: 6
grep -c 'id="kinderschutz"' _site/eltern/index.html               # erwartet: 1
grep -c "praevention@bfv.de" _site/eltern/index.html              # erwartet: 1
grep -c "Schienbeinschoner" _site/eltern/index.html               # erwartet: >=2
grep -c "15. September 2026\|15.09.2026" _site/eltern/index.html   # erwartet: >=2
```
Expected: 6 Accordion-Items, Kinderschutz-Anker, BFV-Mail, Schienbeinschoner mehrfach, Saisonstart mehrfach.

- [ ] **Step 3: Kein PII / kein Leistungs-Ranking im Output**

Run:
```bash
grep -Ei "vater von|stärkste mannschaft|leistungsprinzip|9 spieler|kadergröße|schäpers|kirchbaumer|haas|gerlach|berger" _site/eltern/index.html || echo "OK: kein PII / kein Leistungs-Detail"
```
Expected: `OK: kein PII / kein Leistungs-Detail`. (Nachnamen dürfen auf `/eltern/` NICHT auftauchen; Vornamen sind erlaubt.)

- [ ] **Step 4: Commit**

```bash
git add src/eltern.njk
git commit -m "feat: /eltern/ mit Konzept-Accordion (Zeiten, Kinderschutz, Werte u.a.)"
```

---

## Task 7: Gesamt-Verifikation im Browser (mobil)

**Files:** keine (nur Prüfung)

- [ ] **Step 1: Dev-Server-Config anlegen (falls nicht vorhanden)**

`.claude/launch.json` im öffentlichen Repo:
```json
{
  "version": "0.0.1",
  "configurations": [
    { "name": "eltern-site", "runtimeExecutable": "npx", "runtimeArgs": ["@11ty/eleventy", "--serve"], "port": 8080 }
  ]
}
```

- [ ] **Step 2: Preview starten + zur Eltern-Seite navigieren**

`preview_start` mit `{ name: "eltern-site" }`, dann `navigate` zu `http://localhost:8080/djk-ottenhofen-jugend/eltern/`.

- [ ] **Step 3: Mobil prüfen**

`resize_window` preset `mobile`. Dann:
- `read_console_messages` (onlyErrors) → keine Fehler.
- `read_network_requests` urlPattern `fonts.g` → **keine** Requests an fonts.googleapis.com / fonts.gstatic.com.
- `read_page` → Accordion-Summaries sichtbar, „Trainingszeiten" offen, restliche zu.
- `computer` left_click auf „Kinderschutz"-Summary → `read_page` bestätigt aufgeklappt, BFV-Box sichtbar.
- Jump-Chip „Kinderschutz" antippen → scrollt zum Anker.

- [ ] **Step 4: Footer + Rechtsseiten prüfen**

- `navigate` zu `.../impressum/` und `.../datenschutz/` → beide rendern, Inhalt korrekt.
- Footer: Copyright „Trainerteam", Kontakt-Mail `hallo+djk@mauricio.de`, Impressum/Datenschutz-Links klickbar.

- [ ] **Step 5: Screenshot als Nachweis**

`computer` `screenshot` (mobil, /eltern/ mit Accordion) für den User.

- [ ] **Step 6: Abschluss**

Kein Commit nötig (nur Prüfung). Danach: `superpowers:finishing-a-development-branch` für Merge/PR-Entscheidung. Deploy erst nach Merge auf `main` (GitHub-Action).

---

## Self-Review (vom Plan-Autor durchgeführt)

**Spec-Abdeckung:** Zeiten → Task 6 (Accordion „zeiten") ✓ · Kinderschutz+BFV → Task 6 ✓ · Spielfeldrand+Aufsicht → Task 6 ✓ · So spielen (Einsatzzeiten sanft) → Task 6 ✓ · Werte (merged, keine Doppelung) → Task 6 ✓ · Maßnahmen → Task 6 ✓ · Trainer-Framing/Footer → Task 2 ✓ · Impressum → Task 3 ✓ · Datenschutz → Task 4 ✓ · Font self-host → Task 1 ✓ · Mini-Card „Auf einen Blick" → Task 6 ✓ · PII/Leistungs-Detail raus → Task 6 Step 3 (grep-Gate) ✓.

**Platzhalter-Scan:** keine TBD/TODO; vollständige Copy + CSS + Befehle vorhanden.

**Typ-/Namens-Konsistenz:** CSS-Klassen (`.accordion-item`, `.accordion-chevron`, `.callout`, `.jump-nav`, `.parents-note`, `.trainer-line`, `.footer-legal`, `.legal-page`) in Task 1/2/3/5 definiert und in Task 6 verwendet. Font-Dateinamen `sen-400/700/800.woff2` konsistent zwischen Task 1 Step 1 und Step 2. Accordion-Item-Count = **6** (sechs Sektionen; der Mobile-Menü-`<details>` trägt Klasse `mobile-toggle`, zählt nicht mit) — Erwartungswerte in Task 6 entsprechend auf 6 gesetzt.
