# Phase: ANALYST — AFTER-ACTION REVIEW

Inputs: `SCENARIO`, `RUN`.

You are the Analyst (not Control). Read `methodology/prompts/_common.md`, `methodology/analysis-framework.md`, `templates/run/aar-template.md`, `<SCENARIO>/README.md`, `<SCENARIO>/prep/` (incl. ground truth and setup rolls), all of `<RUN>/` (state, all turns' sitreps/adjudications/audits, journals, log, hotwash/).

1. Write `<RUN>/aar.md` per template. Every claim cites turn refs (e.g. [t04 adj]). Include: the forecast trajectory table across turns; the reveal of hidden truths (what was really going on vs what actors believed); a backcast; model artefacts (where LLM play looked unrealistic and how that biases conclusions); 5–8 insights with confidence (low/med/high) and robust/fragile tags; 3 forks worth running.
2. Write/overwrite `<SCENARIO>/insights.md`: the top insights in ≤300 words.
3. Write `<RUN>/report-data.md`: a compact structured digest for a designer to build an HTML report from — title, one-line verdict, end state, 6–10 timeline beats (date, headline, 1–2 sentences, which actor, was it secret), the 3–5 branch points with the rolls (p and result), forecast trajectory numbers per turn, cast list with one-line "what they wanted / what they did", hidden-truth reveal, insights, and 3 pull-quotes from actor journals/orders (short, attributed to the role).
Update `<SCENARIO>/README.md` status to `reviewed`.
