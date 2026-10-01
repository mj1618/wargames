# Phase: GAME RUNNER (orchestrates several turns)

Inputs: `RUN`, `FROM` (first turn to play, two digits), `N` (max turns to play this session), optional `START` phase for the first turn.

Repeat for TURN = FROM, FROM+1, … (at most N turns):
1. Execute the full procedure in `methodology/prompts/turn-runner.md` yourself for this TURN (NEXT = TURN+1) — i.e. spawn the phase sub-agents exactly as described there. You are a dispatcher only: never play a role or write game files.
2. After the wrap phase, run `tools/push.sh "<scenario-id>/<run-id>: turn <TURN>"` (this is the only git you may do).
3. Read only the FIRST LINE of `<RUN>/turns/t<TURN>/sitrep.md`. If it starts with `END`, stop the loop.

Final message (≤5 lines): turns completed; whether the game ENDED (and end state); one-line headline per turn from the wrap phase reports.
