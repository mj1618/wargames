# Resolution — round 01 (2027)

## Rolls
- Households' organising drive: odds 0.50 (0.35, +0.15 unemployment under 5%). r=0.7673 **FAIL**.
- Court blocks the executive disclosure rule: odds 0.35. r=0.0411 **SUCCESS — blocked**.
- Bill 1, housing incentives: odds 0.90 (small 0.80, +0.10 fits coalition). r=0.7446 **PASSES**.
- Bill 2, retraining and wage insurance with trigger: odds 0.80 (small; no adjustment — cheap and untaxed, but a new programme). r=0.4864 **PASSES**.
- Statistics noise: draw 1 → published unemployment −0.2, median income −1.0.

## Levers (changed)
- `deploy_pace` 1.15 — AI firms race, "+15% above baseline", taken literally (within two notches).
- `ai_pricing` −0.5 — AI firms choose lock-in. Employers cut prices in a few lines and keep savings elsewhere: nets to zero.
- `adoption_speed` 1.1 — employers "about +10%", routine functions only.
- `layoff_share` 0.4 — employers' stated move to freezes and attrition (two notches).
- `wage_sharing` +0.1 — employers' profit-sharing for retained staff (one notch, table value).
- `new_business` 1.02 — entrepreneurs' stated net +12% (people-heavy push, part AI-only), less 0.1 standing adjustment because `ai_pricing` ≤ −0.5.
- `retraining_pct_gdp` 0.01 — the labs' $2bn-a-year Worker Transition Fund ($2bn ÷ $31tn ≈ 0.006%, rounded up). Private money, booked by the model as public.
- `shock_frontier_cog` −0.03 — event 4, flat year at the frontier.

## Levers (unchanged)
- `hours_share` 0.1 — employers keep it.
- `union_pressure` 0 — drive failed.
- `household_saving` 0 — households hold steady.
- `deploy_regulation` 0 — disclosure rule (would be 0.1) blocked in court; stays at 0 until re-enacted.
- `housing_policy` 0 — Bill 1 passed, but federal spending passed in a one-year round takes effect next round; states add nothing (S3).
- `transfers_pct_gdp`, `transfer_target`, `capital_tax_pct`, `public_jobs_m`, `worktime_cut_pct`, `competition_policy` — nobody moved them.

## Carried into round 02
- `housing_policy` 0.2 (Bill 1, federal incentives).
- `retraining_pct_gdp` 0.11 (Bill 2 at 0.1 plus the labs' fund 0.01); rises to 0.31 automatically the round after scorecard unemployment exceeds 6%.
- Employers' profit-sharing is a pledge: roll 0.60 to hold only if profits come under pressure.

## Non-players
- Central bank (hawkish): no trigger. States: no housing move, no budget cuts. Rest of world: nothing to report.
- Lobbying ($150m) and the employers' no-mass-layoff offer: narrated, no lever. Neither business seat publicly backed or opposed either bill, so no odds adjustment.
- Bill 2's "offset by spending trims" has no lever; the model books the programme as new spending.

## Off-menu notes
- Households' demands on zoning and unemployment insurance are requests to others, not levers.
- Entrepreneurs stayed out of factory-built housing: no housing contribution.
