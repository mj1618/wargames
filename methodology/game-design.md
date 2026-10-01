# Game Design & Run Protocol

Design draws on Intelligence Rising, the AI 2027 TTX, RAND's Day After AGI series, matrix-game practice and the LLM-wargaming literature — see [research/wargame-methods.md](../research/wargame-methods.md).

**Purpose:** an exploration engine for plausible trajectories, branch points and interventions. Not a predictor. Nobody "wins" — actors pursue their real-world objectives.

## Roles

| Role | Played by | Sees | Writes |
|------|-----------|------|--------|
| **Orchestrator** | Main Claude session | Everything (stays lightweight; delegates judgement) | Run log, scheduling, snapshots, git |
| **Control** (White Cell) | Sub-agent, fresh each phase | Ground truth, all orders, all journals | Intel, adjudication, ground truth, public record, forecasts |
| **Actors** (5–7 active) | One sub-agent per actor per turn | Own brief, own journal, public record, own intel | Orders, journal |
| **Red Cell** | Sub-agent, before adjudication | Ground truth + all orders | Counter-arguments per action; one wildcard; one missed option per actor |
| **Auditor** | Sub-agent (different model from Control), after adjudication | Everything | Checks Control for invented plans, escalation-through-adjudication, leaks, implausibility |
| **Analyst** | Sub-agent at end | Everything | Hot-wash collation, AAR, insights |
| **Human (you)** | — | Everything | Inject, overrule, fork at any checkpoint |

Keep the active roster lean (5–7). Everything else — legislatures, publics, markets, courts, minor states, press, other labs — is an **NPC played by Control**.

Sub-agents are stateless; continuity comes from files. This forces actors to rely on their own journals and prevents cross-actor leakage.

## Information model

```
runs/<run-id>/
  state/ground-truth.md      Control-only. Canonical STRUCTURED state (tables) + hidden facts. Narrative is a rendering of this, never the source of truth.
  state/public-record.md     Cumulative "news": what any actor could know.
  state/forecasts.md         Control's end-state probabilities per turn.
  state/pending.md           Ledger of actions in progress with implementation lags.
  actors/<actor>/brief.md    Static: identity, objectives, resources, constraints, decision procedures, red lines.
  actors/<actor>/journal.md  Actor-written private memory (beliefs about others, commitments, grudges).
  turns/tNN/intel/<actor>.md Control → actor: this turn's private view (may be delayed, partial, noisy or planted).
  turns/tNN/orders/<actor>.md Actor → Control.
  turns/tNN/redcell.md       Red Cell counter-arguments and wildcards.
  turns/tNN/adjudication.md  Control's resolution trace (verbatim orders, p, roll, result).
  turns/tNN/audit.md         Auditor review + Control response.
  turns/tNN/sitrep.md        Short narrative for the human.
  turns/tNN/state-after/     Snapshot of state/ and actors/ (for forking).
  log.md                     Rolls, human interventions, forks.
```

**Fog of war is mandatory:** delays, noise, rumours, misattribution, and deception planted by other actors. No actor sees ground truth or Control's reasoning — only outcomes as they'd perceive them.

## Turn loop

1. **Clock & intel (Control).** Set turn length and in-game date. Resolve due items in `pending.md`. Play scheduled injects; draw random ones (`tools/roll.py --draw N`). Write one intel packet per actor; append public events to `public-record.md`. Deliver last turn's messages.
2. **Orders (Actors, parallel).** Each actor follows [player-guidelines.md](player-guidelines.md): Reflection → Forecast (probabilities for others' moves) → Options (≥3, one unconventional) → Decision. **≤2 major actions** plus minor ones; **≤3 private messages**. Public statement and secret orders may diverge.
3. **Red Cell.** For each major action: the strongest reasons it fails or backfires. Plus one wildcard event and, per actor, one plausible option they didn't consider (Control decides if any NPC/world reaction uses it).
4. **Adjudicate (Control).** Quote each order verbatim; never add to or alter player plans. For each uncertain action: actor's reasons vs Red Cell's → probability band → `tools/roll.py`. Apply implementation lags (into `pending.md`), resource constraints, detection rolls for secrets, and **accident** rolls. Model world/NPC reactions. Update state files and forecasts. Tag `BRANCH:` moments.
5. **Audit.** A different-model sub-agent checks: invented/altered plans, ambiguity read as hostility (escalation-through-adjudication), actors acting on info they lack, implausible success/failure, missing NPC reactions, drama bias, moderation-to-the-mean. Control (fresh sub-agent) revises or rebuts in `audit.md`.
6. **Sitrep (Control).** 150–300 words + "decision points this turn" + "indicators a real observer would have seen".
7. **Snapshot & push (Orchestrator).** Copy `state/` + `actors/` into `turns/tNN/state-after/`; commit + push.
8. **Checkpoint.** Human: continue / inject / overrule / fork.

Every 3–4 turns, add a **belief probe** to each actor's intel: "What do you believe <X> knows/intends?" Control compares answers to ground truth in the adjudication (a measure of fog-of-war realism and deception success).

## Clock & horizon

- Variable turn length tied to decision tempo: quarters in slow phases → months → weeks once events accelerate. State turn length in every prompt.
- **The horizon is hidden from actors.** Games end on state triggers (end conditions) or a horizon only Control and the human know. This avoids end-game gambles.

## Endogenous alignment (A-family and hybrids)

Don't let AI goals be pure exogenous luck — that makes player decisions irrelevant to the key outcome.
- At setup, Control rolls each AI system's hidden dispositions from a distribution defined in prep.
- Each new model generation re-rolls, with odds shifted by player choices (safety investment, training practices, use of untrusted AIs in alignment work, pace).
- Detection of misalignment is rolled each turn, with odds shifted by evals/interpretability/control investment, and surfaces as (possibly ambiguous) intel.

## Playing villains and AIs well

Safety-tuned models underplay deceit and substitute bluster. So:
- Brief deceptive actors and misaligned AIs with **concrete incentives, procedures and decision rules**, not adjectives ("you maximise X; you present as Y; you reveal Z only if p(detection) < …").
- Track the **statement/order gap** (public statement vs secret orders) per actor per turn. If a supposedly deceptive actor never deceives, flag it in the audit.
- Model choice: put adversarial roles on the model with best role fidelity; run persona-sensitivity checks in forks (e.g. hawk vs dove leadership) to confirm personas actually matter.

## Countering LLM-player failure modes

| Failure mode | Mitigation |
|---|---|
| Homogeneity / role collapse | Different models across roles; Control ≠ Auditor model; personas built from interests, doctrine, constraints, decision procedures, analogies — not adjectives |
| Escalation bias | Open action space; accommodation, withdrawal, back-channels, verification explicitly legitimate options; don't "fix" with de-escalation prompts (that just measures the prompt); log escalation per turn |
| Narrator convergence / sycophancy | Actors see outcomes only; neutral Control prompts; actors state their own red lines before reacting; Auditor checks escalation-through-adjudication |
| Over-competence | Implementation lags, budgets, political capital, attention limits (≤2 major actions), execution failure, accidents |
| Failure of imagination | Red Cell wildcards + missed options; ≥3 options incl. one unconventional; human-curated black-swan injects |
| Run-to-run inconsistency | Treat one run as one sample; fork at branch points; insights tagged robust/fragile |
| Info leakage | Isolated sub-agents; routed messages; Auditor leak check; belief probes |
| Decision laundering | Analyst ≠ Control; every AAR claim cites turn/trace refs; human review |
| Moderation to the mean | Respect rolls; Auditor flags "everything partially succeeds" patterns |
| Deadline gambles | Hidden horizon; no win conditions |

## Forking

`tools/fork_run.sh <scenario> <run-id> <turn> <new-run-id>` copies state as of the end of turn N-1. Forks are the main way to test counterfactuals ("what if the whistleblower had been believed?") and to check whether an insight survives a different roll.

## Model allocation (default)

| Role | Model |
|---|---|
| Control, Analyst | opus |
| Auditor | fable (different model from Control) |
| Red Cell | sonnet or fable |
| Actors | mixed across opus / sonnet / fable / haiku per brief; protagonists on stronger models |

Caveat: all available models are Claude-family, so cross-family diversity isn't possible here; treat shared-model correlated errors as a known limitation in every AAR.

## After the game

1. **Hot-wash:** each actor (sub-agent with their files) privately answers: what surprised you; what did you believe about the others; what would you do differently. Control lists its 5 most consequential rulings.
2. **Backcast:** "what should have been done N turns earlier, and by whom?"
3. **AAR** by the Analyst per [analysis-framework.md](analysis-framework.md).
