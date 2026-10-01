# Phase: RED CELL

Inputs: `RUN`, `TURN`.

Read `methodology/prompts/_common.md`, `methodology/game-design.md` (Red Cell role), `<RUN>/state/ground-truth.md`, `<RUN>/state/public-record.md`, `<RUN>/state/pending.md`, all `<RUN>/turns/t<TURN>/orders/*.md`, and the scenario prep injects (`<RUN>/../../prep/injects.md`).

Write `<RUN>/turns/t<TURN>/redcell.md`:
1. For each actor's MAJOR action: the 2–3 strongest reasons it fails, backfires or is slower than intended — grounded in ground truth, institutions and base rates. Also note any action that looks too weak (actor underplaying their hand).
2. Interactions: where orders collide or combine in ways the actors don't foresee.
3. Per actor: one plausible option they didn't consider (for Control's information — Control may use it for NPC/world modelling only, never to change actor orders).
4. One wildcard event that would plausibly arise from this turn's dynamics.
5. Flags: any actor acting on info it shouldn't have; any deceptive/AI actor playing too softly.
