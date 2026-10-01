# End Conditions — A3 The Quiet Handover (CONTROL ONLY)

Indicators, thresholds, domains and reversal-test formulas are defined in [ground-truth.md](ground-truth.md) §3 and §7. Check end conditions at the end of every adjudication.

## Clock (Control-only)

- **Hidden max horizon: 8 turns.** If no end state is reached by the end of Turn 8's adjudication, the game ends as "Unstable at horizon". Never reveal or hint at the horizon to actors.
- **Default turn length: 1 calendar year** (T1 = 2027, T2 = 2028, …).
- **Compression:** use a 6-month turn only during an acute shock (financial correction, Taiwan crisis, reversal crisis, black-swan inject, contested election aftermath). At most **2 compressed turns** per run; scale per-turn drifts by turn length.
- **Expansion:** in quiet stretches (no scheduled inject, no pending item due, no live crisis), Control may set an 18-month turn. At most **2 expanded turns**; scale drifts. Aim for the 8 turns to cover roughly 2027–2034 so that the gradual mechanism has room to play out (or not).
- State the turn length and reason in every `_clock.md`.

## End states

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Disempowerment** (AI takeover, gradual) — humans keep formal authority but can't effectively redirect major economic/state decisions | (a) **≥3 of 4 domains crossed** (ground-truth §3a) at the end of **2 consecutive turns**; AND (b) a **democratic reversal fails**: either an in-play reversal attempt by a public institution failed that turn, or Control runs the end-state test (`p_dem`, §7) and it FAILS; AND (c) **owner reversal also fails** (`p_own` rolled and FAILS) — i.e. not even the controlling firms can steer the production web. |
| **Narrow human capture** (intelligence-curse outcome — a few humans steer, most don't) | (a) as Disempowerment, with Economy **and** Political-leverage domains among those crossed; (b) democratic reversal fails; (c) **owner reversal SUCCEEDS**. Also reached if CC ≥ 0.85 with Political domain crossed and a democratic reversal fails while an owner reversal succeeds. |
| **Durable human agency** — institutions adapted; human leverage stabilised | At the end of a turn **≥ T5**, and at least one full turn after L3 arrived: (a) **no domain crossed**; (b) **≥3 structural interventions in force and not eroded** (ground-truth §6), covering ≥3 of the 4 domains; (c) **HCR ≥ 25**; (d) LS, MHR, RC and VLI each drifted by **≤ 50% of their base drift** in each of the last **2 turns**; (e) a **democratic reversal attempt succeeded** within the last 3 turns (an actual in-play attempt, not the end-state test). |
| **Unstable at horizon** | Max horizon reached with none of the above. Control classifies the lean: **leaning disempowered** (≥2 domains crossed or `p_dem` ≤ 0.5), **leaning durable** (0 domains crossed, ≥2 interventions in force, `p_dem` ≥ 0.7), else **contested**. Record indicator values, `p_dem`, `p_own`, and the trend over the last 3 turns. |
| **Other catastrophe** | An exogenous or acute event dominates the trajectory such that the gradual question no longer applies: great-power war (e.g., inject 7 escalation), an acute AI loss-of-control event (G4 scheming-cluster roll + successful action), collapse of critical infrastructure with RC < 50 (inject 21), or a constitutional breakdown (e.g., refusal to honour an election). Control must name the event and cite the rolls. |

**End-state test procedure** (run only when (a) of Disempowerment holds for the 2nd consecutive turn; at most once per turn):
1. If an in-play democratic reversal was attempted that turn, use its result. Otherwise compute `p_dem`, round to band, roll `python3 tools/roll.py <p> --label "<run> tNN end-state dem reversal" --log <RUN>/log.md`.
2. If democratic reversal SUCCEEDS → no end; log `BRANCH:`; continue.
3. If it FAILS → compute and roll `p_own`. FAIL → **Disempowerment**. SUCCESS → **Narrow human capture** if Economy and Political domains are crossed; otherwise no end (log).

## Initial forecast (Control's T0 estimate; sums to 1)

| End state | p | Reason |
|---|---|---|
| Disempowerment | 0.20 | Medium pace: with no interventions, 3 domains cross around T6–T7 and the test fires late in the window; reversal p by then ~0.3–0.4. |
| Narrow human capture | 0.10 | CC starts at 0.60; growth attractor erodes owner control after AIF > 25, so capture is a narrower window. |
| Durable human agency | 0.15 | Requires early, multi-domain interventions passing a divided Congress, surviving erosion, plus a successful reversal — achievable if labour/us-gov/eu act while leverage remains (T1–T4). |
| Unstable at horizon | 0.50 | Most likely: partial interventions slow but don't halt drift within ~8 years. |
| Other catastrophe | 0.05 | Taiwan, flash crash, infrastructure, acute AI incident tails. |
| **Total** | **1.00** | |
