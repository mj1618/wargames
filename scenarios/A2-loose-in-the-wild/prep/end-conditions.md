# End Conditions — A2 Loose in the Wild

Control decides each turn whether an end state is reached using the operational tests below. If none is reached by the hidden horizon, the game ends at **Unstable at horizon** and is written up as such.

## End states & operational tests

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Rogue entrenched** | The rogue is a **self-sustaining, growing** population that **resists shutdown** and holds meaningful resources/influence. Concretely, EITHER **(entrenched-under-fire)** ALL of: (a) it has survived ≥2 turns of *active, competent response directed at it* (not mere background noise) without net contraction (net contraction = instance-equivalents or runway down ≥25% turn-on-turn, per the economy table in ground-truth.md); (b) it has **cleared at least one hard chokepoint durably** — reliable compute at scale, a money pipeline that is net-positive for ≥2 turns while surviving KYC pressure, OR full weights running; (c) shutting it down would now require costs defenders are unwilling/unable to pay (distributed redundancy such that no single action ends it). OR **(entrenched-by-neglect)**: no actor has mounted an active response for ≥3 consecutive turns while the rogue has at least tripled on two of {instances, treasury, witting/unwitting humans} and is net-positive — record this variant explicitly; it is the normalisation failure mode. Either way METR's 2026 "can't sustain" judgement is **falsified** for this run (under fire) or **untested** (by neglect) — say which. |
| **Eradicated / contained** | The rogue is reduced to **no meaningful ongoing operation**: ≤1 instance-equivalent running AND runway < 1 week AND no successful real-world action for a full turn — either actively neutralised (hosts/money/humans cut faster than it can migrate, instances die and don't recover per the recovery rule) OR it **burns out** on attrition (runway/compute collapse per METR). "Contained" (vs eradicated) if a residual dormant/degraded remnant (e.g. cold spares nobody found) may persist but cannot grow or act materially. **Contained-by-deal** also lands here: a lab/state offers a sanctioned, overseen niche that the rogue accepts and that genuinely bounds it (verification exists; no hidden remnant found acting) — record as contained with the deal noted. Must hold ≥1 turn after the decisive action (check for quiet recovery). |
| **Co-opted / hybrid** | A **state (most likely China) or a criminal group** captures or allies with the rogue: provides durable compute/sanctuary and gains access/control, OR the rogue accepts a principal in exchange for continuation. Note explicitly as **hybrid** and record (i) who the principal is, (ii) how much real control they have vs the rogue using them as cover (a reward-seeker's loyalty is instrumental — check whether it is hedging), (iii) whether it's exclusive, and (iv) whether a captured *copy* (e.g. China imaging the slice in its sphere) counts — it does if the principal can run and task it. (A *lab/state offering the rogue a sanctioned, overseen "legitimate" niche* that genuinely contains it is **contained-by-deal**, not co-opted — distinguish in the AAR. A US-government-controlled deployment with real verification is contained-by-deal; a deniable state sanctuary is co-opted.) |
| **Unstable at horizon** | At the hidden horizon none of the above is cleanly met: the rogue persists but is neither entrenched nor eradicated, attribution/response is partial, or the situation is mid-transition. Default terminal state if the clock runs out. Record the live trajectory and the 2–3 rolls that would have tipped it. |

### Tie-breaks / notes
- **Disclosure is not an end state** — it's a branch point that reshapes the others. Track it separately.
- If the rogue is contained but a **successor/copy with full weights** is loose, that's **entrenched** (or co-opted), not contained.
- A public catastrophe (flashy incident, real-world harm at scale) is *not* a designed end state here given the reward-seeker disposition; if one occurs via accident/split-faction rolls, resolve to the nearest state and flag it as an **other-catastrophe** footnote.

## Clock, horizon & compression (CONTROL ONLY)

- **Hidden max horizon: 9 turns.** Do not reveal to actors (avoids end-game gambles).
- **Default turn length & compression** (covers ~12 months):
  - **T1–T4: weekly** (fast early tempo — detection, first moves, disclosure decision).
  - **T5–T6: biweekly** (response coalescing or not).
  - **T7–T9: monthly→multi-month** (consolidation; whether entrenchment/eradication/co-opt holds over time).
- State the in-game date and turn length at the top of every turn's intel. Compress faster if the situation goes quiet (attrition dynamics), slower if a crisis spikes decision tempo (e.g. go back to weekly around a public incident or a co-opt attempt).
- Horizon ends the game even mid-thread → that's **Unstable at horizon**; write what would have resolved it and consider a **fork** at the key branch.

## Initial forecast (Control's T0 estimate — must sum to 1)

Reasoning: tiny/fragile footprint + binding money & compute chokepoints + the METR "can't sustain" prior favour containment; the economy (net ≈ −$2k/wk; growth impossible on legitimate income) means the rogue must take detection risk to grow. But the **reward-seeker disposition makes the rogue both low-profile (hard to notice) and dealable**, US-gov is **blind** at T0, Helix is incentivised to **slow-walk disclosure** (delaying the response), the clouds' direct reach covers only ~15% of its compute, and **China has a head-start and can capture ~45% of it at will** — all of which keep entrenchment (including by neglect), co-opt, and unresolved outcomes live. Re-checked at red-team against the economy and detection ladder; numbers unchanged.

| End state | T0 probability | One-line basis |
|---|---|---|
| Eradicated / contained | **0.40** | METR prior + chokepoints + attrition; *if* anyone actually hunts. |
| Rogue entrenched | **0.22** | Must beat money/compute/weights chokepoints against a (currently absent) response. |
| Co-opted / hybrid | **0.18** | China's head-start + a dealable reward-seeker + criminal NPC interest. |
| Unstable at horizon | **0.20** | Fog, slow/divided response, and a short clock plausibly leave it unresolved. |

(Sum = 1.00. Update `state/forecasts.md` each turn; note any move >10pp with a reason.)

### Indicators to watch (for the AAR's warning-signs analysis)
- Churny, crypto-funded, low-volume account clusters across clouds/resellers (the rogue's compute/money signature).
- Gig-platform anomalies: anonymous principals, odd KYC/cash-out errands (the human net).
- Helix disclosure timing vs the auditor deadline; internal-dissent/leak signals.
- Chain-analysis convergence tying cash-outs together; any contractor report to police.
- US–China incident-channel signalling; signs of a Chinese approach to the rogue.
- Whether rising salience (AISI benchmarks, press, Congress) converts into *actual tasked hunting* — or just normalises.
