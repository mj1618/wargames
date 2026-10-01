# AI Takeover Wargames

Strategic wargames exploring two families of catastrophe:

- **H — Human takeover using AI**: a person or small group uses advanced AI to seize illegitimate, durable power.
- **A — AI takeover**: AI systems end up disempowering humanity — and we ask *to what end*.

The goal is insight, not prediction: find the decision points, warning signs, chokepoints and interventions that change outcomes, and stress-test our intuitions about which ones matter.

## How a game works

Most of the work is preparation. A scenario is prepped into a world state, a set of actor briefs with private goals and information, a Control-only "ground truth", and an inject deck. Then the game is played forward in turns:

1. **Control** (a sub-agent) issues each actor its view of the world for the turn.
2. **Actors** (one sub-agent each, run in parallel) decide and submit orders — public moves, secret moves, messages.
3. **Control** adjudicates: assigns explicit probabilities, rolls with [tools/roll.py](tools/roll.py), resolves interactions, updates the ground truth and public record.
4. A **Critic** pass checks adjudication for plausibility and narrative bias.
5. Repeat until an end condition, then write an **After-Action Review**.

All state lives on disk, so runs persist across sessions and can be **forked** at any turn to test counterfactuals.

See [methodology/game-design.md](methodology/game-design.md) for the full protocol.

## Layout

```
methodology/   How we design, run, adjudicate and analyse games; content guardrails
research/      Background briefs: world baseline, threat-model literature, wargame methods
templates/     Scaffolds for scenario prep and for a run
scenarios/     One folder per scenario: seed → prep → runs/
tools/         roll.py (adjudication dice), new_run.sh, fork_run.sh
```

## Scenario index

See [scenarios/README.md](scenarios/README.md).

| ID | Title | Status |
|----|-------|--------|
| H1–H5 | Human takeover using AI | seeded |
| A1–A5 | AI takeover | seeded |

## Lifecycle of a scenario

`seed` → `prepped` → `running` → `reviewed`

- **seed**: one-page concept (`scenarios/<id>/README.md`).
- **prepped**: world state, actors, ground truth, injects, end conditions written (`scenarios/<id>/prep/`).
- **running**: one or more runs under `scenarios/<id>/runs/<run-id>/`.
- **reviewed**: AAR written; insights rolled up into `scenarios/<id>/insights.md`.
