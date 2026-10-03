# Resolution — round 04 (2030)

## Rolls (odds stated before rolling; see `log.md`)
- **Household renewal drive, about 8 sites** (0.35 +0.15 unemployment under 5% = 0.50). A small defensive drive, so success was set as "pressure held at 0.4", not a full notch. r=0.5493 → **FAIL**.
- **Employers' written attrition-first pledge kept with profits under pressure** (guide §3, 0.60; credit squeeze and falling orders). r=0.7698 → **FAIL**: many member firms turn to layoffs.
- **Main Street Credit and Work-Sharing Act** (small, responsive 0.80; mixed fit with the coalition, no adjustment). r=0.6137 → **SUCCESS**. Spending law in a one-year round: bites round 05.
- **Framework Extension Act** (small rule change, 0.80 +0.10 fits coalition = 0.90). The $1bn was paid; Washington named no pre-vote condition, so the vote was held. r=0.8778 → **SUCCESS**. Court challenge (0.20): r=0.5070 → not blocked.
- **Election, November 2030** (0.35 + 0.01 × (38.9 − 35) + 0.10 median income below 2028 = 0.49): r=0.5329 → **FAIL**, growth-first keeps its lead. Configuration draw 3 → **responsive → divided**.
- Statistics noise: draw 5 → unemployment +0.2, median income +1.0.

## Levers
- `deploy_pace` 1.0 — AI firms return to baseline (two notches down).
- `ai_pricing` 0 — labs: enterprise bundles at current rates (0) and an open usage tier at −25% (+0.5), netted at +0.25; employers' kept savings −0.25 stands. Applies the round 03 audit correction.
- `adoption_speed` 1.05 — employers' "normal to 10% faster", midpoint.
- `layoff_share` 0.55 — employers chose 0.4; the pledge roll failed, one notch up.
- `hours_share` 0.13 — pilot extended from 3% to 5% of headcount, pro rata to last round's 0.12 (off-table size).
- `wage_sharing` 0.15 — profit-sharing held, in contracts.
- `new_business` 1.0 — entrepreneurs cut expansion (−0.1 on 1.2); event −0.1; no standing adjustment yet.
- `union_pressure` 0.3 — drive failed, fades 0.1.
- `household_saving` 0 — saving up one point from −0.01.
- `housing_policy` 0.55 — carried 0.50 (Housing Supply Act 0.4 + states 0.10) plus 0.05 for entrepreneurs' move into building (menu item, lever now above 0.2). The Act's "offset" is narration; the model books the cost.
- `retraining_pct_gdp` 0.1, `deploy_regulation` 0.1, `competition_policy` 0.3 — unchanged.
- `shock_demand_pct` −2.0, `shock_adoption` 0.9 — event #5.

## Narrated only (no lever)
- Pre-emption now runs to end 2032, conditional in statute on the labs' training fund doubling to $1bn a year; the labs have not yet answered. Their further $2bn sits unreleased in escrow: its terms (pre-emption to 2034, a consent decree) were not enacted.
- Bundle terms: employers took one-year terms and the usage tier; no 15% cut, no two-year deal.
- Households' term sheet (full pay, sight of deployment plans) against employers' advisory seats: unsigned.
- Labs' $300m political spend; entrepreneurs' open-access lobbying.

## Non-players
- Central bank (hawkish): no support. States: no housing step due; unemployment under 6%, no cuts.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t04/levers.json --years 1 --label 2030`

## Carry-forward for round 05
See `turns/t05/intel/_clock.md`.
