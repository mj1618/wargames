# Phase: CONTROL — INITIALISE RUN + TURN 1 INTEL

Inputs: `SCENARIO`, `RUN` (= <SCENARIO>/runs/<run-id>).

Read `methodology/prompts/_common.md`, `methodology/adjudication.md`, `methodology/game-design.md`, all of `<SCENARIO>/prep/`, `world/cast.md`.

1. If `<RUN>` doesn't exist: `tools/new_run.sh <scenario-id> <run-id>`.
2. Seed `<RUN>/state/public-record.md` from prep world-state; seed `state/forecasts.md` with the T0 forecast; copy end conditions & hidden horizon into the top of `state/ground-truth.md` (Control-only section).
3. Then do the CLOCK & INTEL step for turn 01 exactly as in `methodology/prompts/control-wrap.md` §B.
