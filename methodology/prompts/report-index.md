# Phase: HTML SUMMARY INDEX

**First read `methodology/prompts/report-clarity.md` — its rules and required structure override the section list below wherever they differ. The reader has never seen the game files.**

Inputs: list of report files and runs (given by the orchestrator).

Invoke the `frontend-design` skill if available. Read every `reports/*.html` you're given (skim), each run's `aar.md` and `report-data.md`, each `scenarios/*/insights.md`, and `scenarios/README.md`.

Write `reports/index.html` — the front page the user reads first, in the same visual language as the game reports (start from `reports/_template.html` CSS and components):
1. Headline: "AI Takeover Wargames — Night 1" + one-paragraph framing.
2. **Bottom line** — 5–7 cross-game insights (what recurred, what differed, which interventions look robust across scenarios vs trade-offs), each with confidence and which games support it.
3. A card per game: title, family, end state stamp, one-line verdict, 2-line "why", link to the report.
4. A comparison table: scenario × (tempo, end state, decisive chokepoint, point of no return, best intervention).
5. "What we'd run next" — forks and remaining scenarios (from scenarios/README.md), with one-line rationale.
6. Method note (3–4 lines): how the games were run (sub-agent actors with private info, Control adjudication with logged dice, Red Cell + Auditor), and the main caveats.
Self-contained, phone-friendly, light/dark. Final message ≤3 lines.
