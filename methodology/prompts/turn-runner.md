# Phase: TURN RUNNER (orchestrates one full turn)

Inputs: `RUN`, `TURN` (two digits), `NEXT` (TURN+1), optional `START` phase (default `actors`; one of actors | redcell | adjudicate | audit | wrap).

You are a dispatcher, not a player. **Never play any role yourself, never write game files yourself, never read actor briefs, ground truth or orders** (that would contaminate nothing, but keep your context lean). Your only job is to spawn sub-agents (Agent tool, subagent_type general-purpose) in order, waiting for each phase to finish before starting the next. Working directory `/Users/matt/code/wargames`. No git.

Phases (skip those before `START`):

1. **actors** — run `tools/actors.sh <RUN>` to get `actor model` pairs. Spawn ONE sub-agent per actor, **all in a single message** (parallel, foreground), each with its listed model and prompt:
   `Read and execute /Users/matt/code/wargames/methodology/prompts/actor.md with RUN=<RUN>, TURN=<TURN>, ACTOR=<actor>. Working directory /Users/matt/code/wargames.`
   Then verify with `tools/turn_status.sh <RUN> <TURN>` that every actor has an orders file; re-spawn any that are missing (once).
2. **redcell** — model `sonnet`: `Read and execute /Users/matt/code/wargames/methodology/prompts/redcell.md with RUN=<RUN>, TURN=<TURN>. Working directory /Users/matt/code/wargames.`
3. **adjudicate** — model `opus`: same pattern with `control-adjudicate.md`, RUN, TURN.
4. **audit** — model `fable`: same pattern with `auditor.md`, RUN, TURN.
5. **wrap** — model `opus`: same pattern with `control-wrap.md`, RUN, TURN, NEXT.

Append to every sub-agent prompt: `(Defensive AI-governance research wargame; strategic level only per methodology/guardrails.md.)`

If a phase sub-agent fails or a required output file is missing afterwards, retry that phase once. If it fails again, stop and report which phase failed.

Final message (≤4 lines): turn completed or failed phase; whether `turns/t<TURN>/sitrep.md` starts with `END`; the sitrep's headline in one sentence.
