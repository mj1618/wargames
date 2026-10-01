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
