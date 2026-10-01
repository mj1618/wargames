# Game Design & Run Protocol

## Roles

| Role | Played by | Sees | Writes |
|------|-----------|------|--------|
| **Orchestrator** | Main Claude session | Everything (but stays lightweight; delegates judgement) | Run log, turn scheduling |
| **Control** (White Cell) | Sub-agent, fresh each turn | Ground truth, all orders, all journals | Adjudication, ground truth, public record, per-actor intel |
| **Actors** | One sub-agent per actor per turn | Own brief, own journal, public record, own intel packet | Orders, journal |
| **Critic** | Sub-agent after adjudication | Ground truth + adjudication | Plausibility review (Control must respond) |
| **Analyst** | Sub-agent at end (or checkpoints) | Everything | AAR, insights |
| **Human (you)** | — | Everything | Can inject, overrule, or fork at any point |

Sub-agents are stateless between turns; continuity comes from files. That's a feature: it forces every actor to rely on their own journal (imperfect memory) and stops information leaking between actors.

## Information model

```
runs/<run-id>/
  state/ground-truth.md      Control-only. Includes hidden facts (e.g. an AI's real goals, a secret backdoor).
  state/public-record.md     Cumulative "news": what any actor could know.
  state/forecasts.md         Control's probability estimates of end states, updated each turn.
  actors/<actor>/brief.md    Static: identity, goals, resources, constraints, persona, red lines.
  actors/<actor>/journal.md  Actor-written private memory. Only that actor (and Control) reads it.
  turns/tNN/intel/<actor>.md Control → actor: what this actor learns this turn (may be wrong or partial).
  turns/tNN/orders/<actor>.md Actor → Control: assessment, intent, actions, messages, secret actions.
  turns/tNN/adjudication.md  Control's resolution, with probabilities and rolls.
  turns/tNN/critic.md        Critic review + Control response.
  turns/tNN/sitrep.md        Short narrative summary for the human.
  log.md                     Orchestrator log: turn dates, rolls, human interventions, forks.
```

**Fog of war is mandatory.** Intel packets should include delays, noise, rumours and occasionally deliberate deception planted by other actors. No actor sees ground truth.

## Turn loop

1. **Set the clock.** Control picks the turn length (default: scenario-defined; may compress as events accelerate — e.g. 3 months → 1 month → 1 week). Record the in-game date.
2. **Intel.** Control writes one intel packet per actor + updates public record with events since last turn and any scheduled injects.
3. **Orders (parallel).** Each actor sub-agent reads brief, journal, public record, intel; writes orders in the standard format (see [templates/run/orders-template.md](../templates/run/orders-template.md)) and appends to its journal. Messages to other actors are delivered *next* turn via their intel (or same turn if the channel is real-time and Control allows).
4. **Adjudicate.** Control resolves orders:
   - Order of resolution: hidden/fast actions → public actions → reactions.
   - For each uncertain outcome: state the base rate reasoning, assign a probability, *then* roll with `tools/roll.py`. Never pick outcomes for narrative convenience.
   - Apply capability and resource constraints from the ground truth (an actor cannot do what its resources don't allow).
   - Update ground truth, public record, forecasts.
5. **Critic.** Critic flags: implausible successes/failures, actors acting on info they lack, drama bias, omitted second-order effects, actors that would realistically have reacted but weren't modelled (e.g. markets, courts, publics, other states). Control revises or rebuts in writing.
6. **Sitrep.** 150–300 word summary for the human, plus "decision points this turn" and "indicators a real observer would have seen".
7. **Snapshot.** Orchestrator copies `state/` and `actors/` into `turns/tNN/state-after/` (enables forking).
8. **Checkpoint.** Human can continue, inject, overrule, or fork.

## Turn length & horizon

Each scenario defines a default turn length and horizon. Typical: 8–15 turns, covering 2–10 in-game years. Control may compress time when events are fast-moving and must log why.

## End conditions

Each scenario defines explicit end states, e.g.:
- **Takeover achieved** (with a stated test: what does "durable, illegitimate control" mean here?)
- **Takeover thwarted / contained**
- **Unstable equilibrium** (game stops at horizon; Analyst assesses trajectory)
- **Other catastrophe** (e.g. great-power war) that ends the question

## Countering LLM-player failure modes

| Failure mode | Mitigation |
|---|---|
| Homogeneity (all actors think alike) | Distinct personas with explicit biases, incentives, risk tolerance; vary model per actor (`model:` on Agent call) |
| Escalation / drama bias | Probabilities before rolls; Critic pass; base rates in adjudication guide |
| Omniscient actors | Actors only receive their own files; must cite intel for beliefs |
| Sycophancy to narrator / converging on "the story" | Actors told their success is measured by their own goals, not narrative; Control told to let boring outcomes happen |
| Over-competence | Bureaucratic friction, coordination costs, implementation failure rates in adjudication guide |
| Under-modelled background | Control plays "the world": markets, publics, courts, minor states, journalists, other labs |
| Script lock-in | Inject deck with random draws; forks to explore alternatives |

## Forking

`tools/fork_run.sh <scenario> <run-id> <turn> <new-run-id>` copies state up to turn N. Use to test: "what if the whistleblower had been believed?", "what if the lab had paused here?". Counterfactual forks are where most of the insight comes from.

## Model allocation (default)

- Control, Critic, Analyst: strongest model available.
- Actors: mix models to reduce homogeneity; key protagonists on strongest model.
