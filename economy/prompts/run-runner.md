# Phase: RUN RUNNER (economy series) — plays one whole play-through

**CRITICAL: every Agent call must set `run_in_background: false`. Never end while sub-agents are running. You are a dispatcher: never play a role, never write game files.**

Inputs: `RUN` (e.g. economy/runs/r1), `SEED` (integer).

Working directory `/Users/matt/code/wargames`. Sub-agents are `general-purpose`.

0. **Init** (skip if `<RUN>/turns/t01/intel/_clock.md` exists) — model `opus`: `Read and execute /Users/matt/code/wargames/economy/prompts/run-init.md with RUN=<RUN>, SEED=<SEED>.`
1. For TURN = 01, 02, … until a sitrep starts with `END` (max 8 rounds); skip any phase whose output already exists:
   a. **Players** — list `<RUN>/actors/`; model for each from the `Played by model:` line of its brief.md (default sonnet). Spawn all in ONE message: `Read and execute /Users/matt/code/wargames/economy/prompts/actor.md with RUN=<RUN>, TURN=<TURN>, ACTOR=<actor>.` Verify every orders file exists; retry missing once.
   b. **Referee** — model `opus`: `Read and execute /Users/matt/code/wargames/economy/prompts/control-turn.md with RUN=<RUN>, TURN=<TURN>, NEXT=<TURN+1>.`
   c. **Audit** on rounds 03 and 06 only — model `fable`: `Read and execute /Users/matt/code/wargames/economy/prompts/audit.md with RUN=<RUN>, TURN=<TURN>.`
   d. Run `tools/push.sh "economy/<run-id>: round <TURN>"`.
2. **Run summary** — model `opus`: `Read and execute /Users/matt/code/wargames/economy/prompts/analyst-run.md with RUN=<RUN>.` Then `tools/push.sh "economy/<run-id>: summary"`.

If a phase fails twice, stop and report which. Final message (≤3 lines): rounds played, final unemployment and median income index, one-line verdict.
