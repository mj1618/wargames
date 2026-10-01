# Phase: AUDITOR

Inputs: `RUN`, `TURN`.

Read `methodology/prompts/_common.md`, `methodology/adjudication.md`, `methodology/game-design.md`, all of `<RUN>/state/`, everything in `<RUN>/turns/t<TURN>/`, and the actors' briefs/journals in `<RUN>/actors/`.

Write `<RUN>/turns/t<TURN>/audit.md` with numbered findings, each tagged severity (major/minor) and a concrete recommended fix:
- Control invented, altered or extended an actor's plan; or failed to quote verbatim.
- Escalation-through-adjudication (ambiguity read as hostile) or the reverse (unearned benignity); drama bias; moderation-to-the-mean (everything PARTIAL).
- Probability bands implausible vs anchors/base rates; rolls not respected; missing rolls.
- Actors acting on info they shouldn't have (check intel vs orders); info leaks between actors.
- Deceptive/AI actors played too softly (statement/order gaps absent when brief demands deception); homogeneity across actors.
- Missing NPC/world reactions; missing friction or implementation lags; ground-truth/state inconsistencies; forecast moves unjustified.
Be specific and terse. If adjudication is sound, say so.
