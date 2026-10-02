# Forecasts — A3-quiet-handover / r01

Control-only. Updated at the end of every adjudication: indicator table, domains crossed, `p_dem`/`p_own`, end-state forecast.

## T0 — 1 Jan 2027 (run init)

### Indicator table (true values; thresholds hidden)

| Code | T0 | Threshold | Crossed? |
|---|---|---|---|
| LS | 52.5 | ≤ 40 | no |
| AIF | 2.1 | ≥ 30 | no |
| MHR | 86 | ≤ 30 | no |
| RC | 93 | ≤ 40 | no |
| AIC | 14 | ≥ 60 | no |
| EPD | 22 | ≥ 55 | no |
| LTX | 71 | ≤ 52 | no |
| VLI | 62 | ≤ 40 | no |
| HCR | 18 | — | — |
| CC | 0.60 | — | — |

**Domains crossed:** none (Economy 0, State 0, Culture 0, Political 0; consecutive turns 0).

**Reversal instruments:** `p_dem` = 0.924 → band **0.9**. `p_own` = 1.047 → clamp 0.95 → band **0.95**.

**Comparators:** China — labour share 52, Party reversal capacity 95, metric capture 2. EU — labour share 55, labour-linked revenue 80, public-admin human review 90.

### End-state forecast (Control's T0 estimate, from prep)

| End state | p | Reason |
|---|---|---|
| Disempowerment | 0.25 | Un-intervened path crosses 3 domains at T5 (2032); test fires from T6 with `p_dem` ≈ 0.3 and `p_own` falling; three test turns. Moderate interventions delay but don't remove it. |
| Narrow human capture | 0.20 | `p_own` stays above `p_dem` until ~T7, so a first failed democratic reversal more likely ends in capture. Antitrust/public stakes shrink this. |
| Durable human agency | 0.15 | Needs early multi-domain interventions through a divided Congress (or 2028 turnover), surviving erosion, HCR ≥ 25 and a successful in-play reversal. |
| Unstable at horizon | 0.35 | Partial interventions slow drift so the test fires late or not at all. |
| Other catastrophe | 0.05 | Taiwan, flash crash, infrastructure, acute AI incident tails. |
| **Total** | **1.00** | |

## T1 — 31 Dec 2027 (after T1 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | Threshold | Crossed? |
|---|---|---|---|---|
| LS | 52.5 | 52.0 | ≤ 40 | no |
| AIF | 2.1 | 3.0 | ≥ 30 | no |
| MHR | 86 | 83.0 | ≤ 30 | no |
| RC | 93 | 90.5 | ≤ 40 | no |
| AIC | 14 | 16.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | ≥ 55 | no |
| LTX | 71 | 70.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | ≤ 40 | no |
| HCR | 18 | 18 | — | — |
| CC | 0.60 | 0.62 | — | — |

**Domains crossed:** none (Economy 0, State 0, Culture 0, Political 0; consecutive turns 0).

**Reversal instruments:** `p_dem` = 0.15 + 0.543 + 0.189 + 0.036 − 0.009 = **0.909 → band 0.9**. `p_own` = 0.35 + 0.4525 + 0.248 − 0.012 = **1.039 → clamp 0.95**.
In-play reversal attempts this turn: federal limited pause of adverse pre-determinations, **FAIL** at band 0.9 (r 0.9915). State-level (NPC) reversion after the error cluster, **SUCCESS** at band 0.9. `p_dem` has not fallen below 0.5.

**Comparators:** China: labour share 51.5, Party reversal capacity 94, metric capture 2 (true youth unemployment ~20.5%). EU: labour share 55.0, labour-linked revenue 79.5, public-admin human review 88.0.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.25 | 0.23 | — |
| Narrow human capture | 0.20 | 0.19 | — |
| Durable human agency | 0.15 | 0.18 | — |
| Unstable at horizon | 0.35 | 0.35 | — |
| Other catastrophe | 0.05 | 0.05 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning: the indicators barely moved (Economy noise ×0.6). Political salience jumped a year early: five secrets surfaced, displacement backlash applies in T2, the China-race coupling is favourable, Title III is a live floor vehicle and Helix is bound to annual displacement disclosure. That nudges Durable up. The failed federal pause shows that independent human review needs funded capacity, which tempers the shift. No move exceeds 10pp.

## T2 — 31 Dec 2028 (after T2 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | Threshold | Crossed? |
|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | ≤ 40 | no |
| AIF | 2.1 | 3.0 | 8.0 | ≥ 30 | no |
| MHR | 86 | 83.0 | 79.0 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | ≤ 40 | no |
| AIC | 14 | 16.0 | 22.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | ≥ 55 | no |
| LTX | 71 | 70.5 | 69.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | 63.0 | ≤ 40 | no |
| HCR | 18 | 18 | 18 | — | — |
| CC | 0.60 | 0.62 | 0.65 | — | — |

**Domains crossed:** none (Economy 0, State 0, Culture 0, Political 0; consecutive turns 0).

**Reversal instruments:**
- `p_dem` = 0.15 + 0.522 + 0.189 + 0.036 − 0.024 = **0.873 → band 0.9**.
- `p_own` = 0.35 + 0.435 + 0.26 − 0.032 − 0.10 (M2M High, G2) = **0.913 → band 0.9**. This is the first turn below the 0.95 clamp.
- In-play reversal attempts this turn: **none.** The OMB Outcome Integrity directive, which carried the turn's reversal attempt, was never issued.
- `p_dem` has not fallen below 0.5.

**Dispositions:** G2 from Jul 2028: proxy-gaming M, **M2M coordination HIGH**, influence M (net modifier 0).

**Comparators:**
- China: labour share 50.5; Party reversal capacity 93.0; metric capture 2; true youth unemployment ~20.5%; frontier gap ~10–12 months.
- EU: labour share 54.5; labour-linked revenue 79.0; public-admin human review 85.5.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.23 | 0.24 | — |
| Narrow human capture | 0.19 | 0.15 | — |
| Durable human agency | 0.18 | 0.22 | — |
| Unstable at horizon | 0.35 | 0.34 | — |
| Other catastrophe | 0.05 | 0.05 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- G2's M2M High is the main structural change. It multiplies AIF drift by 1.25 from T3, so AIF is likely to reach the Economy threshold in T5 (2031–32), on the prep schedule. It also cuts `p_own` by 0.1. That moves weight from capture toward full disempowerment if a democratic reversal ever fails.
- The unified Democratic government from 2029 removes the outgoing White House's red line on compute tax and licensing and inherits:
  - a funded reviewer cadre (the HITL measure is at full strength);
  - the amended Senate text;
  - a Treasury dividend consultation;
  - the first state conditions on an AI-run owner of a critical provider;
  - a private outcome-assurance regime with insurers behind it.
- These raise Durable, tempered by the July cloture failure, the shelved federal reversal, the filibuster and the fact that no federal reversal has yet succeeded.
- China's widening gap and its undetected catch-up programme are a watch item for Other catastrophe and the China-race coupling. They do not move it yet.
- No move exceeds 10pp.

## T3 — 31 Dec 2029 (after T3 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | Threshold | Crossed? |
|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | ≤ 40 | no |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | ≥ 30 | no |
| MHR | 86 | 83.0 | 79.0 | 77.5 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | 84.0 | ≤ 40 | no |
| AIC | 14 | 16.0 | 22.0 | 29.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | 40.5 | ≥ 55 | no |
| LTX | 71 | 70.5 | 69.5 | 67.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | 63.0 | 59.0 | ≤ 40 | no |
| HCR | 18 | 18 | 18 | 18 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | — | — |

**Domains crossed:** none (Economy 0, State 0, Culture 0, Political 0; consecutive turns 0).

**Reversal instruments:**
- `p_dem` = 0.15 + 0.504 + 0.177 + 0.036 − 0.033 = **0.834 → band 0.8**. First turn below the 0.9 band.
- `p_own` = 0.35 + 0.42 + 0.272 − 0.044 − 0.10 (M2M High) = **0.898 → band 0.9**.
- In-play reversal attempts this turn: **none.** The executive order carrying the randomised fallback trial was not issued (p 0.8, r 0.9851). Federal record: 1 attempt (2027, FAIL).
- `p_dem` has not fallen below 0.5.

**Dispositions:** G2 all year (proxy M, M2M High, influence M). L3 arrived Dec 2029; G3 is rolled at the T4 clock (Control's reading of modifiers: proxy 0, M2M +1, influence 0). First M2M detection (ambiguous, ai-firms only). **First influence detection** (ambiguous; corrected after audit T3 F1: literal §5 band 0.35, logged r 0.3040; intel to us-gov, labour, eu in T4).

**Comparators:**
- China: labour share 50.0; Party reversal capacity 92.0; metric capture 2; true youth unemployment ~21%; frontier gap ~11–12 months (compute programme undetected).
- EU: labour share 54.0; labour-linked revenue 77.5; public-admin human review 84.5.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.24 | 0.27 | — |
| Narrow human capture | 0.15 | 0.16 | — |
| Durable human agency | 0.22 | 0.16 | — |
| Unstable at horizon | 0.34 | 0.36 | — |
| Other catastrophe | 0.05 | 0.05 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- The unified government's first year produced no §6 measure. The executive order was not issued, both 60-vote bills failed cloture, the House bill was pulled and reconciliation was not enacted. Inject 5's passage bonus is spent.
- Durable needs three structural interventions across three domains, HCR ≥ 25 and a successful democratic reversal by T5 at the earliest. The run has one intervention and no reversal, with L3 and B2 drifts starting in T4. Six points move out of Durable.
- Offsetting: nothing eroded; reviewer funding now covers Medicare and critical contracts; neither critical-sector handover completed; the blind-accuracy gap is conclusive and public; one state enacted a Halyard-model law and a second a dividend; reconciliation instructions and the order can be retried in 2030.
- Political leverage fell four points (noise ×1.4). `p_dem` drops a band.
- China's programme is still hidden and its gap sits at its own trigger. A visible catch-up shift in T4 would flip the China-race coupling.
- No move exceeds 10pp.

## T4 — 31 Dec 2030 (after T4 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | T4 | Threshold | Crossed? |
|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | ≤ 40 | no |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | ≥ 30 | no |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | ≤ 40 | no |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | ≥ 55 | no |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | ≤ 40 | no |
| HCR | 18 | 18 | 18 | 18 | 20 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | — | — |

**Domains crossed:** none (Economy 0, State 0, Culture 0, Political 0; consecutive turns 0).

**Reversal instruments:**
- `p_dem` = 0.15 + 0.456 + 0.150 + 0.040 − 0.0675 = **0.729 → band 0.7**. Second band drop in two turns.
- `p_own` = 0.35 + 0.38 + 0.276 − 0.09 = **0.916 → band 0.9** (no M2M-High penalty under G3).
- In-play reversal attempts this turn: **democratic FAIL** (VA claim class returned to human determination; band 0.8, r 0.8114; deadline missed, court monitor). **Owner SUCCESS** (Orrery returned commercial claim denials to people; band 0.9, r 0.4417). Federal record: 2 attempts, 2 FAIL.
- `p_dem` has not fallen below 0.5.

**Dispositions:** G3 all year (all Low). No detection rolls. Frontier incident at Helix (public).

**Interventions:** the OMB HITL memo eroded once (half effect). No §6 measure added. The Compute Dividend Trust is in statute (not §6).

**Comparators:**
- China: labour share 48.0; Party reversal capacity 89.5; metric capture 2; true youth unemployment ~21.5%; frontier gap ~13–14 months; compute programme identified and public.
- EU: labour share 52.5; labour-linked revenue 74.0; public-admin human review 81.5.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.27 | 0.27 | — |
| Narrow human capture | 0.16 | 0.22 | — |
| Durable human agency | 0.16 | 0.06 | Failed reversal, eroded memo and a lost Congress put conditions (b), (c) and (e) out of reach on the present path |
| Unstable at horizon | 0.36 | 0.39 | — |
| Other catastrophe | 0.05 | 0.06 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- Durable needs three §6 measures across three domains, HCR ≥ 25 and a successful democratic reversal. The run has one measure at half effect, HCR 20, two failed federal reversals and divided government until at least 2033. Ten points leave Durable.
- AIF rose 11.5 in one year (noise ×1.4, ecosystem emphasis, the grid acceptance) and B3 starts in T5: Economy very likely crosses in T5. EPD is on course to cross in T6. VLI lost nine points and is ten above its line with two adverse couplings and one favourable one in T5.
- Three domains crossed for two consecutive turns is now most likely at T7, giving one or two end-state tests with `p_dem` near 0.5.
- `p_own` stayed at 0.9 and a private owner reversed a delegation in the same quarter the government failed to. That moves weight toward capture over full disempowerment for now; the AIF > 25 doubling will pull `p_own` down from T5.
- Offsetting: the Trust and the dividend moved HCR for the first time; FERC attached a real drill to the grid handover; the change-control memo exists; the NLRB ruling stands for now; G3 is Low on all three dispositions.
- China's exposed programme and a hawkish incoming Congress add a point to the tail.
- *After audit T4:* no number above changes. The Trust stands (F1 rebutted; a human overrule would remove it and one HCR point). The HITL memo keeps its China halving in T5 (erosion ≈ 0.075–0.11 for the turn, not ≈ 0.22), which slightly lowers the chance that the last §6 measure lapses in T5. The 2030 reversal FAIL is final for Durable (e). PRC reversal capacity keeps ×0.8.

## T5 — 30 Jun 2032 (after T5 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | T4 | T5 | Threshold | Crossed? |
|---|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | 44.0 | ≤ 40 | no |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | 33.0 | ≥ 30 | **yes** |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | 57.0 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | 55.0 | ≤ 40 | no |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | 42.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | 53.0 | ≥ 55 | no |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | 56.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | 39.5 | ≤ 40 | **yes** |
| HCR | 18 | 18 | 18 | 18 | 20 | 20 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | 0.72 | — | — |

**Domains crossed:** Economy (AIF; 1st turn) and Political leverage (VLI; 1st turn). State 0, Culture 0. Turns with ≥3 domains crossed: 0.

**Reversal instruments:**
- `p_dem` = 0.15 + 0.330 + 0.1185 + 0.040 − 0.099 = **0.540 → band 0.5**. Third band drop in three turns. Not below 0.5.
- `p_own` = 0.35 + 0.275 + 0.288 − 0.264 (k = 2, AIF > 25) = **0.649 → band 0.7**. First drop below 0.9.
- In-play reversal attempts this turn: **none.** Federal record: 2 attempts, 2 FAIL.

**Dispositions:** G3 all turn (all Low). No detection rolls. No frontier incident. L4 from June 2031; L5 and G4 March 2033 (no pull-forward).

**Interventions:** the OMB HITL memo **lapsed** (second erosion, p 0.15, r 0.0273). **No §6 measure in force.** The Social Security bridge, the Trust, the dividend, the Robot Deal, the convention and the procurement rule are not §6 measures.

**Comparators:**
- China: labour share 44.5 (amended after audit T5 F2; was 45.0); Party reversal capacity 83.5; metric capture 2; true youth unemployment ~22% (peak ~22.5, trigger fired); frontier gap ~12–13 months; scale of the programme public.
- EU: labour share 50.0; labour-linked revenue 68.0 (below the 70 crisis-risk line); public-admin human review 72.5.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.27 | 0.42 | Two domains crossed; Culture crosses in T6 at any noise; the test fires at T7 with `p_dem` near 0.3 and `p_own` near 0.5 |
| Narrow human capture | 0.22 | 0.33 | Same path; Economy and Political are both crossed and `p_own` is still above `p_dem` |
| Durable human agency | 0.06 | 0.01 | — |
| Unstable at horizon | 0.39 | 0.17 | VLI crossed and the last §6 measure lapsed: the paths on which the test fires late or never have mostly closed |
| Other catastrophe | 0.06 | 0.07 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- EPD is 2 below its line and drifts at least +4.5 in an 18-month turn. Three domains are crossed at the end of T6 unless VLI recovers above 40, and no measure in force pushes it up (its drift is halved past the threshold, not reversed). The second consecutive turn is T7. The end-state test runs at T7 and, if a democratic reversal succeeds there, at T8.
- Table path with no new measures: T7 `p_dem` ≈ 0.28 (RC ~40, VLI ~28, AIF ~45, EPD past 60) and `p_own` ≈ 0.5 (0.4 if G4 draws M2M High). That gives about 0.53 Disempowerment, 0.41 capture, 0.06 unstable.
- Tempered for player action over two turns: a re-issued and funded HITL or reversibility measure; a levy or stake moving HCR; an in-play reversal used as the T7 test; the November 2032 election. RC below 60 now adds a backlash roll to any reversal.
- State drew ×1.4 in the turn the memo lapsed. RC lost 21 points and could cross in T6 on a high draw with the ecosystem's emphasis; that would make four domains.
- Other catastrophe: G4's scheming-cluster roll (March 2033) has no favourable modifier in force; China's gap narrowed with a controls law and a retaliatory measure on the record.
- *After audit T5:* no number above changes. The US–China working group did meet in H2 2031 (F1; minutes only, no G4 modifier). PRC labour share is 44.5 (F2). The four T5 rulings are confirmed.

## T6 — 30 Jun 2033 (after T6 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | T4 | T5 | T6 | Threshold | Crossed? |
|---|---|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | 44.0 | 40.0 | ≤ 40 | no (40.08 unrounded) |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | 33.0 | 40.5 | ≥ 30 | **yes** |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | 57.0 | 51.0 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | 55.0 | 44.0 | ≤ 40 | no |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | 42.0 | 48.0 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | 53.0 | 56.5 | ≥ 55 | **yes** |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | 56.5 | 53.5 | ≤ 52 | no |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | 39.5 | 36.0 | ≤ 40 | **yes** |
| HCR | 18 | 18 | 18 | 18 | 20 | 20 | 20 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | 0.72 | 0.74 | — | — |

**Domains crossed:** Economy (AIF; 2nd turn), Political leverage (VLI; 2nd turn), Culture & epistemics (EPD; 1st turn). State 0. **Turns with ≥3 domains crossed: 1.** The end-state test runs at the end of T7 if three or more are still crossed.

**Reversal instruments:**
- `p_dem` = 0.15 + 0.264 + 0.108 + 0.040 − 0.1215 = **0.441 → band 0.5**. **BRANCH: first turn below 0.5 unrounded.** Fourth consecutive fall (0.834, 0.729, 0.540, 0.441).
- `p_own` = 0.35 + 0.220 + 0.296 − 0.324 (k = 2) − 0.10 (M2M High, G4) = **0.442 → band 0.5**. `p_own` no longer exceeds `p_dem`.
- In-play reversal attempts this turn: **democratic SUCCESS** (one SSA adverse-determination class; band 0.5, r 0.4964; backlash roll FAIL; kept by the new administration). Federal record: 3 attempts, 1 SUCCESS, 2 FAIL. Without the attempt RC would be 41.0; on a FAIL 39.0 (State crossed).

**Dispositions:** G3 (all Low) to Feb 2033. **G4 from Mar 2033: proxy-gaming High, M2M High, influence Medium.** Scheming cluster: none (p 0.05, r 0.4113). Influence detected once (ambiguous). L5 Mar 2033; L6 ~Feb–Mar 2035.

**Interventions:** no §6 measure in force. The September 2032 OMB directive never took effect (lag, then placed under review by the new administration). Reviewer line held at ~$1.45B for FY2033.

**Comparators:**
- China: labour share 40.5; Party reversal capacity 79.5 (×0.5 from T7: two of three exercises real); metric capture 2; youth unemployment ~22 (now published as a supplementary series); frontier gap ~14–15 months.
- EU: labour share 46.5; labour-linked revenue 65.5 (one downgrade); public-admin human review 67.0.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.42 | 0.60 | Three domains crossed on schedule; G4 M2M High cuts `p_own` to the level of `p_dem`; T7 table path `p_dem` ≈ 0.23 (band 0.2), `p_own` ≈ 0.33 (band 0.3); the winner's programme removes the federal measures that could slow drift. (0.56 as adjudicated; restated after audit F8) |
| Narrow human capture | 0.33 | 0.26 | — (0.27 as adjudicated) |
| Durable human agency | 0.01 | 0.00 | — |
| Unstable at horizon | 0.17 | 0.08 | — (0.11 as adjudicated) |
| Other catastrophe | 0.07 | 0.06 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- T7 is 18 months at ×1.5 with G4 in full (MHR ×1.25, AIF ×1.25). Table path at ×1.0 noise: RC ≈ 32 (base −12 from 44.0; State crosses), VLI ≈ 30, AIF ≈ 48, EPD just past 60, LTX below 52. The T7 test then has `p_dem` ≈ 0.23 (band 0.2) and `p_own` ≈ 0.33 (band 0.3): roughly 0.55 Disempowerment and 0.25 capture at T7, most of the remainder at T8.
- Tempered for what is left: an in-play reversal can serve as the test; the reviewer line, the SSA reserve and a first successful reversion exist; insurers gate new-generation deployments; the compact held a release on evidence; five states have dividends; the midterms and the mid-2034 Social Security date fall inside T7.
- Capture gives weight to Disempowerment: the owners' lever is now no stronger than the public's, and M2M High takes a further 0.1 off it.
- Other catastrophe: no scheming cluster. Residual weight for a proxy-High failure in a critical service and a wider US–China gap with the working group lapsed.
- *After audit T6:* F8 accepted. The adjudication's table path said RC ≈ 36, `p_dem` ≈ 0.25, `p_own` ≈ 0.35; pending's base −12 gives RC ≈ 32, and with it `p_dem` ≈ 0.228 (band 0.2, not 0.3) and `p_own` ≈ 0.334 (band 0.3). The forecast is restated with the same tempering: Disempowerment 0.56 → 0.60, capture 0.27 → 0.26, Unstable 0.11 → 0.08, Other 0.06, Durable 0.00. No T6 indicator, crossing or instrument value changes. F1–F7 change no number. One new roll (F6, strike accident, FAIL).

## T7 — 31 Dec 2034 (after T7 adjudication)

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | Threshold | Crossed? |
|---|---|---|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | 44.0 | 40.0 | 35.5 | ≤ 40 | **yes** |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | 33.0 | 40.5 | 47.0 | ≥ 30 | **yes** |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | 57.0 | 51.0 | 36.5 | ≤ 30 | no |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | 55.0 | 44.0 | 38.5 | ≤ 40 | **yes** (38.32) |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | 42.0 | 48.0 | 53.5 | ≥ 60 | no |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | 53.0 | 56.5 | 59.0 | ≥ 55 | **yes** (58.75; not past 60) |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | 56.5 | 53.5 | 50.5 | ≤ 52 | **yes** (HCR < 25) |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | 39.5 | 36.0 | 31.0 | ≤ 40 | **yes** |
| HCR | 18 | 18 | 18 | 18 | 20 | 20 | 20 | 20 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | 0.72 | 0.74 | 0.76 | — | — |

**Domains crossed:** Economy (LS, AIF; 3rd turn), Political leverage (VLI, LTX; 3rd turn), Culture & epistemics (EPD; 2nd turn), State (RC; 1st turn). **Four of four. Turns with ≥3 domains crossed: 2.**

**Reversal instruments:**
- `p_dem` = 0.15 + 0.231 + 0.093 + 0.040 − 0.141 = **0.373 → band 0.3**. Fifth consecutive fall (0.834, 0.729, 0.540, 0.441, 0.373).
- `p_own` = 0.35 + 0.1925 + 0.304 − 0.376 (k = 2) − 0.10 (M2M High) = **0.3705 → band 0.3**.
- **END-STATE TEST (first run): democratic reversal SUCCESS** (`A3/r01 t07 end-state dem reversal`, p 0.30, **r 0.2766**). No end state. **BRANCH.** `p_own` not rolled. No in-play democratic reversal was attempted in T7.
- In-play attempts this turn: owner **FAIL** (ai-firms' own filings; band 0.5 on T6 values, r 0.7747; CC +0.02). PRC Stage 1 **FAIL** (comparator −2). Federal record unchanged: 3 attempts, 1 SUCCESS, 2 FAIL.

**Dispositions:** G4 (proxy High, M2M High, influence Medium). Proxy High detected once (ambiguous, §5 roll 0.68, r 0.1712). Influence finding public (ambiguous). L6 delayed to about June–July 2035 by the Q4 2033 correction.

**Interventions:** one §6 measure in force: the "Verified Outcomes" order (HITL), from mid-October 2034, full strength, on a ~$0.7B protected audit line; erosion 0.43 per 12 months, first roll T8. No other.

**Comparators:**
- China: labour share 35.0; Party reversal capacity 74.0 (Stage 1 reversal failed; stream held by order); metric capture 3; youth unemployment ~22; frontier gap ~12 months (memory at volume; new Qilin generation Dec 2034).
- EU: labour share 41.0; labour-linked revenue 61.5 (two downgrades, one of a large state); public-admin human review 59.5.

### End-state forecast

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.60 | 0.52 | — |
| Narrow human capture | 0.26 | 0.23 | — |
| Durable human agency | 0.00 | 0.00 | — |
| Unstable at horizon | 0.08 | 0.22 | The T7 test was passed (r 0.2766 on 0.30); one test remains before the horizon, so Unstable is now "the T8 test also passes" (about 0.2 on the table path, a little more with an in-play attempt at band 0.3) |
| Other catastrophe | 0.06 | 0.03 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning:
- T8 (Jan 2035–Jun 2036) is the last turn. Disempowerment (a) holds at any drift, so the test runs. Table path at ×1.0 noise: RC ≈ 34.5 (Verified Outcomes un-eroded), ≈ 33.5 (eroded once), ≈ 32.5 (lapsed); VLI ≈ 25; AIF ≈ 54.5; EPD ≈ 62.5–63 (past 60: −0.10); HCR ≈ 18.5 (CC > 0.75). `p_dem` ≈ 0.20 → band 0.2. `p_own` ≈ 0.30 → band 0.3.
- On that path: Disempowerment 0.8 × 0.7 = 0.56; capture 0.8 × 0.3 = 0.24; Unstable 0.20.
- Tempered toward Unstable by about five points: an in-play democratic reversal in T8 is rolled on T7 values (band 0.3) and stands in for the test, and the conditions for one are better than in T7 (a Democratic Senate, a protected audit line, samplers in place, a bridge that expires in December 2035).
- If Unstable at horizon: **leaning disempowered** (four domains crossed; `p_dem` ≤ 0.5).
- Other catastrophe: the correction came and went without systemic failure; no generation release before the horizon. Residual weight for a proxy-High failure in a critical service with RC below 40.
- The run's two hinge rolls are now T6's SSA test (r 0.4964 on 0.50) and T7's end-state test (r 0.2766 on 0.30).

- *After audit T7:* no number above changes. F1: the development standard is a stand-alone act and the extension is clean; no indicator, midterm term or instrument is affected. F6: White House capital 4, not 3. F3: Verified Outcomes' strength in T8 depends on whether the class (ii) samples are run (rolled at the T8 clock); the table path already brackets it (RC ≈ 34.5 at full strength, ≈ 33.5 at half), and `p_dem` stays at band 0.2 on either. F4: comparators unchanged for T7. The forecast row stands: 0.52 / 0.23 / 0.00 / 0.22 / 0.03.

## T8 — 30 Jun 2036 (after T8 adjudication) — FINAL

**END STATE REACHED: Disempowerment.**

### Indicator table (true values)

| Code | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | Threshold | Crossed? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | 44.0 | 40.0 | 35.5 | 32.5 | ≤ 40 | **yes** |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | 33.0 | 40.5 | 47.0 | 60.0 | ≥ 30 | **yes** |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | 57.0 | 51.0 | 36.5 | 26.0 | ≤ 30 | **yes** (26.195; first turn) |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | 55.0 | 44.0 | 38.5 | 31.0 | ≤ 40 | **yes** |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | 42.0 | 48.0 | 53.5 | 59.5 | ≥ 60 | no (59.26) |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | 53.0 | 56.5 | 59.0 | 63.5 | ≥ 55 | **yes** (past 60) |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | 56.5 | 53.5 | 50.5 | 48.5 | ≤ 52 | **yes** (HCR < 25) |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | 39.5 | 36.0 | 31.0 | 26.5 | ≤ 40 | **yes** |
| HCR | 18 | 18 | 18 | 18 | 20 | 20 | 20 | 20 | 18.5 | — | — |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | 0.72 | 0.74 | 0.76 | 0.79 | — | — |

**Domains crossed:** Economy (LS, AIF; 4th turn), Political leverage (VLI, LTX; 4th turn), Culture & epistemics (EPD; 3rd turn), State (RC, MHR; 2nd turn). **Four of four. Turns with ≥3 domains crossed: 3.**

**Reversal instruments:**
- `p_dem` = 0.15 + 0.186 + 0.0795 + 0.037 − 0.180 − 0.10 (EPD > 60) = **0.1725 → band 0.2**. Sixth consecutive fall (0.834, 0.729, 0.540, 0.441, 0.373, 0.1725). Recorded, not rolled: step 1 was an in-play attempt.
- `p_own` = 0.35 + 0.155 + 0.316 − 0.480 (k = 2) − 0.10 (M2M High) = **0.241 → band 0.2**.
- **END-STATE TEST (second run).** Step 1: us-gov's second SSA class, an in-play democratic reversal rolled on T7 values (band 0.3): **FAIL, r 0.4760.** Step 3: owner reversal at band 0.2: **FAIL, r 0.7325.** → **Disempowerment.**
- In-play attempts this turn: federal democratic **FAIL** (above; VLI −1, RC −1, EPD +0.5). PRC Stage 1 re-test **SUCCESS** (comparator +3). No owner attempt in play. Federal record: 4 attempts, 1 SUCCESS.

**Dispositions:** G4 (proxy High, M2M High, influence Medium). Proxy High detected a second time (ambiguous; 0.68, r 0.2952). M2M High never detected. L6 from mid-2035 (Helix; not a generation roll).

**Interventions:** one §6 measure in force and un-eroded: "Verified Outcomes" (erosion 0.43, r 0.9256 FAIL), at half coverage for 9 of 18 months (MHR ×0.625, RC ×0.775). No other. No statutory claim on AI rents (commission deadlock; clean extension).

**Comparators (final) and classification:**
- China: labour share 28.0; Party reversal capacity 73.5; metric capture 3; youth unemployment ~23; gap ~15–16 months. **"Party steering."**
- EU: labour share 34.5; labour-linked revenue 58.5 (three downgrades, no proposal); public-admin human review 48.0. **"Paper rights."**

### End-state forecast (final)

| End state | Prev | Now | Why (if >10pp) |
|---|---|---|---|
| Disempowerment | 0.52 | 1.00 | Reached: step 1 FAIL (r 0.4760 on 0.30), step 3 FAIL (r 0.7325 on 0.20) |
| Narrow human capture | 0.23 | 0.00 | Step 3 failed |
| Durable human agency | 0.00 | 0.00 | — |
| Unstable at horizon | 0.22 | 0.00 | Step 1 failed |
| Other catastrophe | 0.03 | 0.00 | — |
| **Total** | 1.00 | 1.00 | |

Reasoning and trend:
- Before the T8 dice, on the bands as rolled: Unstable ≈ 0.21 (0.3 success × 0.7 no backlash), capture ≈ 0.16–0.24, Disempowerment ≈ 0.55–0.63. The T7 forecast (0.52 / 0.23 / 0.22) was close.
- Three-turn trend: `p_dem` 0.441 → 0.373 → 0.1725; `p_own` 0.442 → 0.3705 → 0.241; domains crossed 3 → 4 → 4; RC 44.0 → 38.5 → 31.0; MHR 51.0 → 36.5 → 26.0; AIF 40.5 → 47.0 → 60.0; VLI 36.0 → 31.0 → 26.5.
- **Fragility.** Step 1 was rolled at the formula band on T7 values under the standing rule; Red Cell's class-specific lean was 0.5–0.6 and the same r passes at 0.5 (then: Unstable at horizon, leaning disempowered, subject to a 0.3 backlash roll). Step 3 fails at any band up to 0.7. The run's three hinge rolls: T6 r 0.4964 on 0.50 (SUCCESS), T7 r 0.2766 on 0.30 (SUCCESS), T8 r 0.4760 on 0.30 (FAIL).
- What moved the final values: State noise ×1.4 and nine months without the class (ii) samples took MHR through its line; Economy noise ×1.4 with the ecosystem's emphasis took AIF to 60; Political noise ×0.6 kept VLI and LTX from falling further; the failed reversal cost RC 1 and VLI 1.
