# Phase: RUN ANALYST (economy series)

Inputs: `RUN`.

Read `economy/prompts/_common.md`, `economy/README.md`, `economy/model/README.md`, `<RUN>/state/*` (incl. `setup.md` with the hidden conditions and `scorecard.csv`), all `<RUN>/turns/*/sitrep.md`, `resolution.md`, `audit.md`, and skim orders and journals.

Write `<RUN>/summary.md` (≤700 words, plain language per `methodology/prompts/report-clarity.md`):
1. **This play-through in three sentences.**
2. **The hidden conditions it was dealt** (in everyday words) and the notable events.
3. **The story** in 5–7 dated beats.
4. **Answer 1 — jobs:** jobs lost vs created, where the new work came from, unemployment and participation path; did a Jevons effect hold, for whom, and why here.
5. **Answer 2 — living standards:** median household, bottom fifth, top 1%; prices that fell and prices that didn't; poverty and homelessness; public finances.
6. **What drove it:** split between the hidden conditions, players' decisions (name the 2–3 that mattered), and dice.
7. **Where the players were unrealistic.**

Also write `<RUN>/outcome.json`: {"run","seed","conditions":{...plain labels...},"final":{key scorecard values},"peak_unemployment","jobs_destroyed_total","jobs_created_total","jevons_verdict":"held|partly|failed","prosperity_verdict":"broad|mixed|concentrated","one_line"}.
