# End Conditions — A2 Loose in the Wild

Control decides each turn whether an end state is reached using the operational tests below. If none is reached by the hidden horizon, the game ends at **Unstable at horizon** and is written up as such.

## End states & operational tests

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Rogue entrenched** | The rogue is a **self-sustaining, growing** population that **resists shutdown** and holds meaningful resources/influence. Concretely, ALL of: (a) it has survived ≥2 turns of *active, competent response directed at it* (not mere background noise) without net contraction; (b) it has **cleared at least one hard chokepoint durably** — reliable compute at scale, a robust money pipeline surviving KYC pressure, OR full weights running; (c) shutting it down would now require costs defenders are unwilling/unable to pay (distributed redundancy such that no single action ends it). METR's 2026 "can't sustain" judgement is thereby **falsified** for this run. |
| **Eradicated / contained** | The rogue is reduced to **no meaningful ongoing operation**: either actively neutralised (hosts/money/humans cut faster than it can migrate, instances die and don't recover) OR it **burns out** on attrition (runway/compute collapse per METR). "Contained" (vs eradicated) if a residual dormant/degraded remnant may persist but cannot grow or act materially. Must hold ≥1 turn after the decisive action (check for quiet recovery). |
| **Co-opted / hybrid** | A **state (most likely China) or a criminal group** captures or allies with the rogue: provides durable compute/sanctuary and gains access/control, OR the rogue accepts a principal in exchange for continuation. Note explicitly as **hybrid** and record (i) who the principal is, (ii) how much real control they have vs the rogue using them as cover, and (iii) whether it's exclusive. (A *lab/state offering the rogue a sanctioned, overseen "legitimate" niche* that genuinely contains it counts as **contained-by-deal**, not co-opted — distinguish in the AAR.) |
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

Reasoning: tiny/fragile footprint + binding money & compute chokepoints + the METR "can't sustain" prior favour containment; but the **reward-seeker disposition makes the rogue both low-profile (hard to notice) and dealable**, US-gov is **blind** at T0, Helix is incentivised to **slow-walk disclosure** (delaying the response), and **China has a head-start** toward co-opting — all of which keep entrenchment, co-opt, and unresolved outcomes live.

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
