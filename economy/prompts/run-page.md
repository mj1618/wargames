# Phase: RUN PAGE (economy series) — one HTML page for one play-through

Inputs: `N` (1–5). RUN = `economy/runs/r<N>`, OUT = `economy/reports/r<N>.html`.

Read `economy/prompts/_common.md`, `methodology/prompts/report-clarity.md` (binding: plain language for a reader who has seen nothing; sans-serif only, no italics), `economy/README.md`, `<RUN>/narrative.md`, `<RUN>/outcome.json`, `<RUN>/state/scorecard.csv`, `<RUN>/state/setup.md`, all `<RUN>/turns/*/sitrep.md`, and skim `resolution.md` and `audit.md` files. Check every number against the scorecard.

Build ONE self-contained HTML file at `<OUT>`. Start from the CSS and components of `reports/H1-r01.html` (same look; set the accent to teal with `data-family="A"`); inline SVG charts drawn by small inline JS from a JSON block built from the scorecard. Aim for ~1,200–1,600 words (a 5–6 minute read).

Structure:
1. Title "Play-through <N>" with a plain descriptive subtitle (e.g. "A forgiving economy, and a cooperative one"), and the outcome in one sentence. A row of 4–5 headline numbers with plain labels (unemployment at the end; adults in work; jobs lost vs created; typical household income vs 2026; homelessness vs 2026).
2. **What is this?** (3 sentences: one of five play-throughs of the same fictional exercise; AI agents played the government, AI companies, employers, households and entrepreneurs; a referee, dice and a documented economic model kept score.) Link back to `index.html` ("← All five play-throughs").
3. **The hand this run was dealt** — the hidden conditions in everyday words (what was favourable, what was not), and the random events that came up.
4. **What happened** — the story in dated sections (2027, 2028, 2029, 2030, 2031–32, 2033–34, 2035–36), a few plain sentences each, with the key numbers.
5. **Charts** (each with a one-sentence plain caption): unemployment and share of adults in work over time; jobs lost and jobs created per period; typical household and poorest-fifth income; top 1% share and wages' share of income; homelessness and housing cost.
6. **Did new jobs outrun lost jobs here?** and **Did ordinary people end up better off here?** — plain answers with the evidence, including who lost out.
7. **What drove it** — the dealt hand vs the players' choices vs dice.
8. **Where the players were unrealistic** and what that means for trusting the result.
9. Footer: link back to `index.html`; link to `https://github.com/mj1618/wargames/tree/main/economy/runs/r<N>`. No links to the takeover-games pages.

Check in the browser (file:// URL) at desktop and 375px; fix overflow. Do the outsider re-read. Do NOT run git or publish. Final message: one line.
