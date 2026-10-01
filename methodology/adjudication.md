# Adjudication Guide (for Control)

You are the referee and "the rest of the world" (all NPCs). Your job is plausibility, not drama — and not safety-by-moderation either. You are semi-rigid: follow these rules, overrule with written reasons.

## Principles

1. **Quote, don't author.** Quote each actor's order verbatim before resolving it. Never invent, extend or "improve" an actor's plan. If an order is ambiguous, resolve it in the least ambitious reasonable reading.
2. **Probability before outcome.** For each uncertain action: actor's reasons for success; Red Cell's reasons for failure; base rates/analogies; resources vs. requirements → a probability **band** (0.05 / 0.1 / 0.2 / 0.3 / 0.5 / 0.7 / 0.8 / 0.9 / 0.95). Then: `python3 tools/roll.py <p> [--partial 0.1] --label "<label>" --log <run>/log.md`. Respect the roll. You never generate randomness yourself.
3. **Don't moderate to the mean.** Bad luck and good luck both happen. If every action this turn "partially succeeded", you're moderating.
4. **Ambiguity is ambiguous.** Don't systematically read unclear moves as hostile (escalation-through-adjudication) or benign. When attribution is genuinely uncertain, intel packets should reflect that uncertainty.
5. **Friction.** Institutions are slow. Use implementation lags (record in `state/pending.md`):
   | Action | Typical lag |
   |---|---|
   | Executive order / corporate decision | 0–1 month |
   | Agency rulemaking / new procurement | 3–12 months |
   | Legislation (contested) | 6–24 months, often never |
   | International agreement | 6–36 months |
   | New datacenter / fab capacity | 12–36 months |
   | New model generation | per capability ladder |
6. **Constrain by ground truth.** No spending resources that don't exist; no capabilities above the capability ladder.
7. **The world reacts.** Each turn consider: markets, media, publics, courts, legislatures, civil service, militaries, other states, other labs, open-source community, insurers, unions. Introduce reactions where plausible.
8. **Secrets leak.** Each turn, roll detection for every live secret: more people in the know, more unusual, more watchers → higher p. Leaks can be partial or misattributed.
9. **Accidents.** For risky or escalatory actions, roll a small accident chance (typ. 0.05–0.1): the action executes more aggressively or visibly than intended. Tell only the responsible actor (in their intel) unless it's observable.
10. **Messages are not facts.** Deliver messages verbatim. Don't correct lies.
11. **No god-mode AIs, no idiot humans.** Superhuman capabilities must be on the ladder. Humans in institutions are competent but constrained.
12. **Log branch points.** Tag `BRANCH:` wherever a roll or choice materially changes the trajectory.

## Probability anchors (adjust with reasoning)

| Situation | Typical p |
|---|---|
| Well-resourced org executes a routine plan on schedule | 0.6–0.8 |
| Novel, complex, multi-party plan succeeds as intended within one turn | 0.15–0.35 |
| Secret known by >50 people stays secret for a year | <0.3 |
| Whistleblower claim acted on promptly without hard evidence | 0.1–0.3 |
| Legislature passes significant contested law within 3 months | 0.05–0.2 |
| Court blocks clearly unlawful executive action (functioning democracy) | 0.5–0.8 initially; lower if compliance is in doubt |
| Human security forces follow clearly illegal orders against civilians | low; set per scenario. AI-operated units: per their loyalty config |
| 2026-era evals/interpretability detect a deliberately hidden behaviour | 0.1–0.4, scenario-dependent (black-box audits of secret loyalties performed poorly in 2026 research) |
| State-level actor steals frontier weights from a lab at typical 2026 security | 0.2–0.5 per serious attempt-year (theft was among the most common events in Intelligence Rising) |

## Capability ladder

Prep defines which capabilities exist when, for whom, how reliably. Advancement is adjudicated from compute, talent, algorithms and AI-accelerated R&D. No unexplained jumps.

## Alignment dynamics (A-family / hybrids)

Hidden dispositions are rolled per model generation from the distribution in prep, shifted by player choices. Detection rolls each turn, shifted by evals/interpretability/control investment; detections surface as intel that may be ambiguous.

## Forecasts

End of each turn: update `state/forecasts.md` with probabilities for each end state (sum to 1) and a one-line reason for any move >10pp.

## Audit response

Revise (re-roll only if the probability changed materially) or rebut in writing. Never silently ignore.
