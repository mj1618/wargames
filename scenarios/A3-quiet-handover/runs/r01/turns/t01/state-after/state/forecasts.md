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
