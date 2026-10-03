# Resolution — round 04 (2030)

## Rolls
| What | Odds | Result |
|---|---|---|
| Wage Insurance and First Job Act (medium 0.60: a 5-point levy and 0.25% of GDP of programmes, no cash entitlement; fits worker-first instincts +0.10; labs back, employers oppose: no adjustment) | 0.70 | r=0.42 SUCCESS |
| Court blocks the levy (rolled blind) | 0.20 | r=0.41 FAIL — levy stands |
| Households' organising effort to win and police the package (0.35, +0.15 unemployment under 5%) | 0.50 | r=0.54 FAIL |
| Election: worker-first loses its lead (0.35 − 0.04 unrest 31.0 − 0.10 median income up over 3 points) | 0.21 | r=0.54 FAIL — keeps Congress |
| Election: configuration | draw 3 | 3 → responsive becomes **divided** |
| Statistics noise | draw 5 | 1 → published unemployment −0.2, median index −1.0 |

Rule settled (audit t03): a tax under 10 points without new cash transfers is *medium*; a new cash programme is *large*. No pledge roll: profits not under pressure.

## Levers
- `deploy_pace` 1.2 — labs "race +20%", one notch.
- `ai_pricing` −0.25 — unchanged. The small-firm tier's 10% floor rise and the voluntary compute charter are small and opposite in sign; netted to zero. Employers still pass on one-third.
- `adoption_speed` 1.1 — employers' "+10%", taken literally (under one notch).
- `layoff_share` 0.25 — as employers state.
- `hours_share` 0.35, `wage_sharing` 0.15 — held; the equity pilot is narrated.
- `new_business` 1.15 — unchanged: selective entry is no new big push; standing +0.1 (law) stays; no penalty.
- `union_pressure` 0.05 — effort failed; fades 0.1.
- `household_saving` 0 — "spend, don't hoard", −0.01.
- `transfers_pct_gdp` 0.01 — labs' fund pays $3bn. The further $2bn was tied to a five-year lock at 8 points, which the Act does not contain; literal reading, not released.
- `capital_tax_pct` 0, `retraining_pct_gdp` 0.15 — the Act passed but takes effect next round.
- `public_jobs_m` 1.0 — 2029 law, now hiring.
- `deploy_regulation` 0.1, `competition_policy` 0.3 — reporting enforced; cases continue; charter not accepted as a settlement.
- `housing_policy` 0.55 — entrepreneurs' factory-housing push, second +0.05 of three. States: nothing (S3 = 1).
- `shock_new_task` 1.5 — event 8. `shock_demand_pct` resets to 0; central bank (neutral) does nothing.

## Carried to round 05 (2031–32, two years)
- `capital_tax_pct` 5 and `retraining_pct_gdp` 0.4 take effect.
- `union_pressure` fades to 0 unless renewed; `shock_new_task` resets.
- Event 7 (energy crunch): `shock_adoption` 0.8, `shock_frontier_cog` −0.01.
- Configuration **divided** (0.55 / 0.35 / 0.15); worker-first leads.

## Non-players and off-menu
Narrated only: labs' politics spend and charter; employers' equity pilot; entrepreneurs' API migration; households' upzoning campaign (big states did not move).

## Model result (unaltered)
1.32m jobs destroyed (all automation), 3.25m created (1.43m new work, 1.00m public jobs, 0.68m spending, 0.13m re-absorbed); net +1.93m; employment 166.39m. Unemployment 3.26%, employment rate 59.59%. Real pay 110.0, median income 108.8, bottom fifth 107.3. Labour share 52.6%. GDP +3.63%. Poverty 11.2%, homelessness 17.6. Deficit 6.2%. Unrest 31.0.
