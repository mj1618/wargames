# Phase: HTML REPORT (one game)

Inputs: `SCENARIO`, `RUN`, `OUT` (e.g. reports/H1-r01.html).

First invoke the `frontend-design` skill (Skill tool) if available and follow its guidance. Then read `<RUN>/report-data.md`, `<RUN>/aar.md`, `<SCENARIO>/README.md`, and skim `<RUN>/turns/*/sitrep.md` and `<RUN>/state/forecasts.md` for accuracy.

Start from `reports/_template.html` (copy it; keep its CSS, components and JS; set `--accent` for the family; replace all placeholder content and the forecast JSON). Build ONE self-contained HTML file at `<OUT>` (inline CSS/JS; inline SVG for charts; Google Fonts allowed; no other external requests). Audience: a smart reader skimming over coffee — it must be **on-point first, cool second**.

Required structure:
1. **Masthead** — scenario ID + title, family (Human-takeover / AI-takeover), in-game date span, end state as a bold stamp.
2. **TL;DR box** — verdict in one sentence + the 3 most important insights (each one line, with confidence tag).
3. **The board** — cast cards: role, what they wanted, what they did, outcome for them. AI actors visually distinct.
4. **Timeline** — turn-by-turn beats; secret actions styled as classified (redaction bar the reader can click to reveal); public events plain.
5. **Branch points** — 3–5 cards, each showing the probability, the roll result (dice/meter visual), and "what if it had gone the other way".
6. **Forecast trajectory** — inline SVG line chart of end-state probabilities per turn, labelled, legible in light and dark mode.
7. **What was really going on** — hidden-truth reveal (what actors believed vs ground truth).
8. **Insights & interventions** — the insights with confidence/robust-fragile tags; chokepoints; indicators & warnings; interventions.
9. **Voices** — 2–3 short pull-quotes from actor journals (attributed to roles).
10. **Caveats** — model artefacts, single-run fragility; forks worth running.
11. Footer: link back to `index.html` and to the run folder on GitHub (https://github.com/mj1618/wargames/tree/main/<RUN>).

Design: an intelligence-dossier / war-room aesthetic (e.g. monospace labels, stamp marks, subtle grid, restrained accent colour per family — e.g. amber for H, cyan for A), but readable and calm, not gimmicky. Colours as CSS variables on :root with a dark-mode variant under `@media (prefers-color-scheme: dark)`; explicit body background. Must work at phone width (16px gutters, no horizontal scroll). Accessible contrast. Keep it under ~150KB.

Final message: ≤3 lines.
