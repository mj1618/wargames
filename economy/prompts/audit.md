# Phase: AUDIT (economy series)

Inputs: `RUN`, `TURN`.

Read `economy/prompts/_common.md`, `economy/model/README.md`, `economy/prep/referee-guide.md`, `<RUN>/state/*`, and everything in `<RUN>/turns/t<TURN>/` and the previous round.

Write `<RUN>/turns/t<TURN>/audit.md` (≤300 words): did the referee (a) change or invent player decisions, (b) set levers outside what the decisions justify — in either the optimistic or pessimistic direction, (c) skip rolls or ignore results, (d) hand-edit model outputs, (e) leak hidden information to players? Are players behaving implausibly alike or implausibly public-spirited? List concrete fixes. If a lever was clearly mis-set, say what it should have been; the next referee step must correct course (not rewrite history) and note it.
