# CLAUDE.md — Wargames repo

Strategic wargames about AI-enabled human takeover (H) and AI takeover (A). Read [README.md](README.md) and [methodology/](methodology/) before doing anything.

## Ground rules
- Follow [methodology/guardrails.md](methodology/guardrails.md) in every file and every sub-agent prompt: strategic abstraction only, no real named individuals, labs are fictional composites.
- One scenario at a time. Don't start prepping another until the user says so.
- All game state lives on disk. Sub-agents are stateless; give them file paths, not summaries.
- Never decide uncertain outcomes by fiat: Control assigns p, then `python3 tools/roll.py`.

## Git — keep the remote updated
Remote: `origin` (github.com/mj1618/wargames), branch `main`. Standing authorisation to commit and push to it without asking.
- Commit + push after every meaningful step: research brief written, scenario seeded/prepped, **every completed game turn** (after the snapshot), forks, AARs.
- Commit message style: `<scenario-id>: <what>` e.g. `H1/r01: turn 04 adjudicated`, `A2: prep complete`, `repo: methodology tweak`.
- `git pull --rebase` before pushing if the push is rejected. Never force-push.

## Prepping a scenario (seed → prepped)
1. `cp -R templates/scenario/prep scenarios/<id>/prep`
2. Research anything scenario-specific (sub-agents in parallel).
3. Fill world-state, ground-truth, one brief per actor, injects (≥12 random), end-conditions with initial forecast.
4. Run a **prep red-team** sub-agent: "Where is this scenario rigged? Which actor is underpowered/overpowered? What would a real-world expert say is missing?" Revise.
5. Update scenario README status → `prepped`.

## Running a turn (orchestrator = main session)
1. **Control: intel** — one sub-agent. Prompt: read `methodology/adjudication.md`, `methodology/guardrails.md`, run `state/`, last adjudication, scenario `prep/injects.md`; set the clock; write `turns/tNN/intel/<actor>.md` for each actor and append to `state/public-record.md`.
2. **Actors: orders** — one sub-agent per actor, **launched in parallel in a single message**. Prompt: "You are <actor>. Read ONLY: `methodology/player-guidelines.md`, `methodology/guardrails.md`, `actors/<actor>/brief.md`, `actors/<actor>/journal.md`, `state/public-record.md`, `turns/tNN/intel/<actor>.md`. Write `turns/tNN/orders/<actor>.md` using `templates/run/orders-template.md` and append your journal entry to `actors/<actor>/journal.md`." Use the model in the actor's brief.
3. **Control: adjudicate** — one sub-agent. Reads everything in the run; writes `turns/tNN/adjudication.md` (template in `templates/run/`), rolls via `tools/roll.py --log <run>/log.md`, updates `state/*`.
4. **Critic** — one sub-agent; writes `turns/tNN/critic.md`. Then Control (fresh sub-agent) responds/revises in the same file.
5. **Sitrep** — Control writes `turns/tNN/sitrep.md`. Orchestrator snapshots `state/` + `actors/` into `turns/tNN/state-after/`, then shows the user the sitrep and asks: continue / inject / overrule / fork.

Default: pause for the user after every turn unless they've said to run N turns.

## After a run
Analyst sub-agent writes `runs/<run-id>/aar.md` from `templates/run/aar-template.md` and updates `scenarios/<id>/insights.md`.
