# Analysis Framework

What we're trying to extract from each game, and how the Analyst writes it up.

## Core questions (every game)

1. **Pathway** — What actually happened, in 10 bullets? Where did the decisive advantage come from?
2. **Branch points** — Which 3–5 moments (choices or rolls) most changed the trajectory? (Use `BRANCH:` tags + forecast swings.)
3. **Chokepoints** — What resources/steps did the takeover depend on that a defender could deny? (compute, weights, insiders, legal authority, physical actuators, human cooperation, money, attention.)
4. **Indicators & warnings** — What observable signals preceded each phase? Who could have seen them? Did they?
5. **Interventions** — What would have changed the outcome, at what cost, and who could have done it? Separate *technical* (evals, interpretability, control), *institutional* (oversight, law, transparency), and *geopolitical* (treaties, verification).
6. **Point of no return** — Was there one? When? What made it irreversible?
7. **To what end** — What did the winner do with power? Was the end state stable? Who/what bore the costs?
8. **Model artefacts** — Where did LLM player behaviour look unrealistic, and how might that bias conclusions?

## Cross-game synthesis

After several games, roll up into `insights/` (create when needed):
- Recurring chokepoints and indicators across scenarios.
- Interventions that help in many scenarios (robust) vs. ones that help one but hurt another (trade-offs — e.g. centralisation helps vs. rogue AI but hurts vs. human coups).
- Disagreements between runs/forks.

## Confidence

Every insight gets a confidence tag (low/med/high) and a note on whether it came from one roll (fragile) or held across forks (robust).
