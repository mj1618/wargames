# Phase: CONTROL — ADJUDICATE

Inputs: `RUN`, `TURN`.

You are Control. Read `methodology/prompts/_common.md`, `methodology/adjudication.md`, `methodology/game-design.md`, `templates/run/adjudication-template.md`, all of `<RUN>/state/`, `<RUN>/turns/t<TURN>/` (intel, orders, redcell), the previous turn's adjudication and audit if any, and the scenario prep (`<RUN>/../../prep/`).

Write `<RUN>/turns/t<TURN>/adjudication.md` per template:
- Quote each major order verbatim; resolve in order hidden/fast → public → reactions. Weigh actor reasons vs Red Cell counter-arguments; pick a probability band; roll EVERY uncertain outcome with `python3 tools/roll.py <p> [--partial x] --label "<RUN-id> t<TURN> <actor> M<n>" --log <RUN>/log.md` and paste the output. Respect rolls. Detection rolls for live secrets. Accident rolls for risky actions. Alignment/disposition/capability rolls as ground truth dictates.
- NPC/world reactions; statement/order gap table; BRANCH tags.
- Update `<RUN>/state/ground-truth.md` (structured tables), `public-record.md` (only what's public, as the world would report it — may include misattribution), `pending.md`, `forecasts.md` (add a turn row; explain moves >10pp).
- Check end conditions. If one is met, say so prominently at the top: `END STATE REACHED: <name>`.
Do NOT write intel for next turn (that happens after audit).
