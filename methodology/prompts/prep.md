# Phase: PREP a scenario

Inputs: `SCENARIO` = scenarios/<id> directory.

Read: `methodology/prompts/_common.md`, `README.md`, all of `methodology/`, `research/world-baseline.md`, `research/threat-models.md`, `research/wargame-methods.md` (skim), `world/cast.md`, `<SCENARIO>/README.md`, and all of `templates/scenario/prep/`.

Do any extra web research you need (WebSearch/WebFetch) to ground the scenario — keep it focused.

Create `<SCENARIO>/prep/` containing:
1. `world-state.md` — deviations from baseline at T0; **capability ladder** table with dates; resources table per actor; institutions & checks; seed public record text.
2. `ground-truth.md` — Control-only canonical state as STRUCTURED TABLES (resources, capabilities, secrets with who-knows + detection risk/turn, relationships, indicator tables if relevant) + hidden facts. For every hidden variable the README says is "rolled", define the distribution and **actually roll it now** with `python3 tools/roll.py --draw N` or `python3 tools/roll.py p`, logging to `<SCENARIO>/prep/setup-rolls.md`, and record the result. Include alignment/disposition dynamics: how player choices shift future rolls.
3. `actors/<actor-id>.md` — one per active actor in the README (5–7), from the template. Personas must be built from interests, doctrine, constraints, **decision procedures**, historical analogies — not adjectives. AI actors and deceptive actors get concrete decision rules (what they maximise, how they present, when they reveal/deceive) and capability limits — but per guardrails "Concrete ≠ technical": capabilities like secret loyalties, escapes, exfiltration and monitor evasion are abstract properties + probabilities, never techniques. Set `Played by model:` — mix opus/sonnet/fable/haiku; protagonists on opus or fable; never more than half on one model. Briefs contain ONLY what that actor knows.
4. `injects.md` — ≥4 scheduled + ≥14 random injects (include black swans, good-news injects, and boring ones).
5. `end-conditions.md` — operational tests per end state; **hidden max horizon of 8–10 turns** (Control-only) and default turn length / compression rules; initial forecast summing to 1.

Make it a fair, un-rigged game: every side must have real options to win or lose. Update `<SCENARIO>/README.md` status line to `prepped`.
