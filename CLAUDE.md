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
Phase prompts live in [methodology/prompts/](methodology/prompts/) — sub-agent prompts should just say: "Read and execute `methodology/prompts/<phase>.md` with RUN=…, TURN=…, ACTOR=…". Per turn: actors (parallel) → redcell → control-adjudicate → auditor → control-wrap (audit response + sitrep + snapshot + next-turn intel). Prep: prep → prep-redteam → run-init. End: hotwash (parallel) → analyst → HTML report.

Full protocol: [methodology/game-design.md](methodology/game-design.md). Every sub-agent prompt names the guardrails file. Give paths, not summaries.
1. **Control: clock & intel** — one sub-agent (opus). Reads `methodology/adjudication.md`, run `state/*`, last turn's files, `prep/injects.md`. Resolves due `pending.md` items, plays/draws injects, writes `turns/tNN/intel/<actor>.md` per actor, appends to `state/public-record.md`. Every 3–4 turns include a belief probe.
2. **Actors: orders** — one sub-agent per actor, **all launched in parallel in one message**, model per brief. Prompt: "You are <actor>. Read ONLY: `methodology/player-guidelines.md`, `methodology/guardrails.md`, `actors/<actor>/brief.md`, `actors/<actor>/journal.md`, `state/public-record.md`, `turns/tNN/intel/<actor>.md`. Write `turns/tNN/orders/<actor>.md` per `templates/run/orders-template.md`; append your journal entry to `actors/<actor>/journal.md`. Do not read any other file."
3. **Red Cell** — one sub-agent (sonnet/fable). Reads ground truth + all orders; writes `turns/tNN/redcell.md`.
4. **Control: adjudicate** — one sub-agent (opus). Writes `turns/tNN/adjudication.md` per template, rolls via `tools/roll.py --log <run>/log.md`, updates `state/*` incl. `pending.md` and `forecasts.md`.
5. **Auditor** — one sub-agent (fable — not Control's model). Writes `turns/tNN/audit.md`. Then a fresh Control sub-agent revises or rebuts in the same file and fixes state if needed.
6. **Sitrep** — Control writes `turns/tNN/sitrep.md`.
7. **Snapshot & push** — orchestrator copies `state/` + `actors/` into `turns/tNN/state-after/`, commits (`<id>/<run>: turn NN`) and pushes, then shows the user the sitrep and asks: continue / inject / overrule / fork.

Default: pause for the user after every turn unless they've said to run N turns.

## After a run
1. Hot-wash: one sub-agent per actor answers the hot-wash questions privately; Control lists its 5 most consequential rulings.
2. Analyst sub-agent (not Control) writes `runs/<run-id>/aar.md` from `templates/run/aar-template.md` (incl. backcast), every claim citing turn refs, and updates `scenarios/<id>/insights.md`. Commit + push.
