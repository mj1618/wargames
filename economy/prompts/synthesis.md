# Phase: CROSS-RUN SYNTHESIS + SUMMARY PAGE (economy series)

Read `economy/prompts/_common.md`, `economy/README.md`, `methodology/prompts/report-clarity.md` (binding: plain language for a cold reader; sans-serif only, no italics), `economy/model/README.md` (incl. the Monte Carlo spread and sensitivity tables), `economy/research/econ-brief.md` (skim), and for each run r1…r5: `narrative.md`, `outcome.json`, `state/scorecard.csv`, `state/setup.md`, and the sitreps.

## 0. Extra analysis you must run first (model-only, cheap; write scripts in the scratchpad, save results to `economy/analysis/` as CSV/JSON)
The five random seeds all happened to draw fairly kind hidden conditions for new work (new-task rate 0.65–1.07 on a 0.2–1.2 range; demand response above 1.2 in four of five), and the AI players were notably cooperative (auditors called them "collectively cosy": employers avoided layoffs, AI firms accepted levies, nobody defected). The page must be honest about both. To separate luck, choices and structure:
a. **Where each run's dealt hand sits**: for each hidden parameter, its percentile within the sampling range; and where each run's final outcomes sit in the 1,000-run Monte Carlo spreads (default, laissez, active presets).
b. **Same hand, different behaviour**: for each run's seed/params, replay the model with the laissez preset, the default preset and the active preset (dice-only) and compare with what the players achieved — how much did the players' choices add or subtract?
c. **Same behaviour, harsher hand**: replay each run's actual per-round `levers.json` sequence under (i) an all-median hand and (ii) a harsh hand (the economy-response parameters at about their 20th percentile, as in `economy/prep/redteam.md`) — what would the same decisions have produced in an unlucky economy?
d. From the Monte Carlo files: in what share of dice-only runs do jobs created exceed jobs destroyed; in what share does typical household income end below 2026; in what share does unemployment end above 8%? Which two or three hidden conditions best separate good from bad outcomes?
Use these in the page (a plain section "Were these five games lucky?" with one simple chart) and in the answers. State plainly that the five played games are at the favourable end and why.

## 1. Synthesis text (≤900 words, plain language) — write it to `economy/analysis/cross-run-notes.md`; if that write is refused, include it in your final message instead
Answer the two questions directly and honestly:
- **Jobs / Jevons:** across the five play-throughs, were more jobs created than destroyed? What happened to unemployment and to the share of adults working? Where did new work come from and who could get it? Under which dealt conditions and choices did the Jevons effect hold, partly hold, or fail?
- **Living standards:** who gained — the median household, the bottom fifth, the top 1%? What got cheaper and what didn't? Poverty, homelessness, public finances.
- **What made the difference:** hidden conditions vs players' decisions vs luck — use the Monte Carlo spread to say whether the five games were typical.
- **How much to trust this:** the model is a simplification with documented assumptions; five runs; all players were AI agents of one model family; the premise (rapid progress) was assumed.

## 2. `economy/reports/index.html`
Start from the CSS/components of `reports/index.html` (the takeover-games summary; keep its look, sans-serif, no italics; teal accent). Self-contained; inline SVG charts drawn by small inline JS from a JSON block built from the five scorecards.
Structure:
1. Title, one-sentence premise, and **the two answers up front** in two plain boxes (each: the short answer, then "it depended on…").
2. **What is this?** (4 sentences: fictional exercise; AI agents played government, AI firms, employers, households, entrepreneurs; a referee and a documented economic model with dice; played five times with different hidden conditions; shows what could happen, not what will.)
3. **The five play-throughs at a glance** — a comparison table with plain column names (e.g. "Unemployment at the end", "Highest unemployment", "Adults in work", "Jobs lost / jobs created", "Typical household income vs 2026", "Poorest fifth's income vs 2026", "Share of income going to the top 1%", "Homelessness vs 2026") and a one-line verdict per run.
4. **Charts**: five lines each (one per run, labelled directly, colour-blind-safe) for unemployment; share of adults in work; typical household income; homelessness; top-1% share. Short plain caption under each saying what to notice.
5. **Each play-through as a short story** (≈150–200 words each): the hidden hand it was dealt, what happened, how it ended.
6. **Question 1 — did new jobs outrun lost jobs?** and **Question 2 — did ordinary people end up better off?** — the evidence from the games in plain words, with the conditions that flipped the answer.
7. **What mattered most** (4–6 plain lessons with "so what").
8. **How the five compare with 1,000 dice-only runs** — one simple chart or sentence-level percentiles showing where the five sit.
9. **How much to trust this** and **what we'd try next**.
10. Footer link to the repo folder `https://github.com/mj1618/wargames/tree/main/economy`. Do NOT link to or from the takeover-games pages (the user wants the series kept separate).

Check in the browser at desktop and 375px, light and dark; do the outsider re-read pass. Then run `tools/push.sh "economy: synthesis and summary page"` and `tools/publish_pages.sh`. Final message ≤3 lines incl. the two answers in one sentence each.
