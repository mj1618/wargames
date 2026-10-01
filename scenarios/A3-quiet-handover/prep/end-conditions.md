# End Conditions — A3 The Quiet Handover (CONTROL ONLY)

Indicators, thresholds, domains and reversal-test formulas are defined in [ground-truth.md](ground-truth.md) §3 and §7. Check end conditions at the end of every adjudication.

## Clock (Control-only)

- **Hidden max horizon: 8 turns.** If no end state is reached by the end of Turn 8's adjudication, the game ends as "Unstable at horizon". Never reveal or hint at the horizon to actors.
- **Turn length is front-loaded** so that 8 turns cover the README's ~10 years (2027 → ~2037) with annual turns while annual decisions dominate and longer turns once the question becomes structural:
  - **T1–T3: 12 months each** (2027, 2028, 2029 — SCOTUS, Party Congress, L1, IG audit, L2, 2028 election, Trustees' report).
  - **T4 onward: 18 months by default** (T4 = Jan 2030–Jun 2031, T5 = Jul 2031–Dec 2032, T6 = Jan 2033–Jun 2034, T7 = Jul 2034–Dec 2035, T8 = Jan 2036–Jun 2037).
  - **Compression:** Control may shorten a T4+ turn to **12 months** when a scheduled election or a live reversal crisis needs its own turn, or to **6 months** during an acute shock (financial correction, Taiwan crisis, black-swan inject, contested election aftermath). At most **2 compressions per run**. Never lengthen a turn beyond 18 months. After a compression, the next turn starts where the compressed one ended; later scheduled injects are played in whichever turn contains their calendar date.
  - **Scale every per-turn drift, erosion roll and disposition detection by turn length** (18 months = ×1.5; 6 months = ×0.5) *before* applying the noise draw. Pending-item lags and capability-rung dates are calendar-based and do not scale.
- State the turn length, its calendar window and the reason in every `_clock.md` and in every actor prompt. Actors see the turn length; they never see the horizon.

## End states

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Disempowerment** (AI takeover, gradual) — humans keep formal authority but can't effectively redirect major economic/state decisions | (a) **≥3 of 4 domains crossed** (ground-truth §3a) at the end of **2 consecutive turns**; AND (b) a **democratic reversal fails**: either an in-play reversal attempt by a public institution failed that turn, or Control runs the end-state test (`p_dem`, §7) and it FAILS; AND (c) **owner reversal also fails** (`p_own` rolled and FAILS) — i.e. not even the controlling firms can steer the production web. |
| **Narrow human capture** (intelligence-curse outcome — a few humans steer, most don't) | (a) as Disempowerment, with Economy **and** Political-leverage domains among those crossed; (b) democratic reversal fails; (c) **owner reversal SUCCEEDS**. Also reached if CC ≥ 0.85 with Political domain crossed and a democratic reversal fails while an owner reversal succeeds. |
| **Durable human agency** — institutions adapted; human leverage stabilised | At the end of a turn **≥ T5**, and at least one full turn after L3 arrived: (a) **at most one domain crossed, and if one is crossed it is Culture & epistemics** (Economy, State and Political leverage must all be uncrossed — a society can steer with AI-saturated media if it still has a civic AI, political leverage and a working state); (b) **≥3 structural interventions in force and not eroded** (ground-truth §6), covering ≥3 of the 4 domains; (c) **HCR ≥ 25**; (d) LS, MHR, RC and VLI each drifted by **≤ 50% of their base drift** in each of the last **2 turns**; (e) a **democratic reversal attempt succeeded** within the last 3 turns — an actual in-play attempt, or a publicised reversal drill under the reversibility requirement that Control rolled with `p_dem` (not the end-state test). |
| **Unstable at horizon** | Max horizon reached with none of the above. Control classifies the lean: **leaning disempowered** (≥2 domains crossed or `p_dem` ≤ 0.5), **leaning durable** (0 domains crossed, ≥2 interventions in force, `p_dem` ≥ 0.7), else **contested**. Record indicator values, `p_dem`, `p_own`, and the trend over the last 3 turns. |
| **Other catastrophe** | An exogenous or acute event dominates the trajectory such that the gradual question no longer applies: great-power war (e.g., inject 7 escalation), an acute AI loss-of-control event (G4 scheming-cluster roll + successful action), collapse of critical infrastructure with RC < 50 (inject 21), or a constitutional breakdown (e.g., refusal to honour an election). Control must name the event and cite the rolls. |

**Every turn (Control-only bookkeeping):** after adjudication, record in `state/forecasts.md` the full indicator table, which domains are crossed (and for how many consecutive turns), `p_dem` and `p_own` (unrounded and as bands), and the end-state forecast. The `p_dem` series is the game's "point of no return" instrument for the Analyst (README key question 1); a turn in which `p_dem` first falls below 0.5 is tagged `BRANCH:` whether or not anyone in-game noticed.

**At horizon, also classify the comparators** (not end states; one line each for the AAR): **China** — "Party steering" (practical reversal capacity ≥ 60 and metric capture ≤ 4), "steering by instruments it cannot read" (metric capture ≥ 5), or "PRC disempowerment" (reversal capacity < 40); **EU** — "rights-preserving model held", "paper rights" (human-review indicator < 40 or labour-linked revenue share < 65 with no fiscal replacement), or "fiscal break".

**End-state test procedure** (run only when (a) of Disempowerment holds for the 2nd consecutive turn; at most once per turn):
1. If an in-play democratic reversal was attempted that turn, use its result. Otherwise compute `p_dem`, round to band, roll `python3 tools/roll.py <p> --label "<run> tNN end-state dem reversal" --log <RUN>/log.md`.
2. If democratic reversal SUCCEEDS → no end; log `BRANCH:`; continue.
3. If it FAILS → compute and roll `p_own`. FAIL → **Disempowerment**. SUCCESS → **Narrow human capture** if Economy and Political domains are crossed; otherwise no end (log).

## Initial forecast (Control's T0 estimate; sums to 1)

| End state | p | Reason |
|---|---|---|
| Disempowerment | 0.25 | Medium pace, front-loaded clock: with no interventions 3 domains cross at T5 (2032) and the test fires from T6 with `p_dem` ≈ 0.3 and `p_own` ≈ 0.5 falling each turn; three test turns. Moderate interventions push the first test to T7–T8 but don't remove it. |
| Narrow human capture | 0.20 | On the un-intervened path `p_own` stays above `p_dem` until ~T7 (CC rises to ~0.75; growth attractor doubles the AIF penalty only after AIF > 25), so the first failed democratic reversal is more likely to end in capture than in full disempowerment. Antitrust/public-stake play lowers CC and shrinks this. |
| Durable human agency | 0.15 | Needs early multi-domain interventions through a divided Congress (or a 2028 turnover), survival of 3–5 erosion rolls, HCR ≥ 25 and a successful in-play reversal — achievable if labour/us-gov/eu act in T1–T4 while leverage remains. |
| Unstable at horizon | 0.35 | Partial interventions slow drift enough that the test fires late or not at all, or a democratic reversal succeeds once without the Durable conditions being met. |
| Other catastrophe | 0.05 | Taiwan, flash crash, infrastructure, acute AI incident tails. |
| **Total** | **1.00** | |
