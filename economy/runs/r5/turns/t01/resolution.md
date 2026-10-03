# Resolution — round 01 (2027)

## Rolls (odds stated before rolling; see `log.md`)
- **Workforce Transition Act** (small bill, divided 0.55, no adjustments): r=0.8197 → **FAIL**. No retraining money, no work-sharing trigger.
- **Housing incentives bill** (small, divided 0.55, +0.10 fits growth-first deregulation = 0.65, partial band 0.15): r=0.7174 → **PARTIAL**. Half-size passes; takes effect next round.
- **Court blocks the disclosure rule** (executive action, 0.35): r=0.3482 → **SUCCESS**. Rule blocked; reverts until re-enacted.
- **Household organising drive** (0.35 +0.15 unemployment under 5% = 0.50): r=0.1762 → **SUCCESS**.
- Statistics noise: draw 2 of 5 → published unemployment −0.1, median income −0.5.

## Levers
- `deploy_pace` 1.2 — AI firms race at +20% (two notches).
- `ai_pricing` −0.75 — AI firms bundle and lock in (−0.5); employers keep savings, no price cuts (−0.25).
- `adoption_speed` 1.15 — employers' company-wide drive (one notch).
- `layoff_share` 0.4 — employers' stated attrition-and-freeze target (within two notches).
- `hours_share` 0.1 — employers hold.
- `wage_sharing` 0.1 — employers' profit-sharing pool (one notch, table value).
- `new_business` 0.9 — entrepreneurs: 15% more ventures in hiring sectors (+0.1) netted against the shift to 60% AI-only firms (−0.1) = 0; standing adjustment −0.1 because `ai_pricing` ≤ −0.5.
- `union_pressure` 0.25 — organising drive succeeded.
- `household_saving` 0 — households hold.
- `deploy_regulation` 0 — disclosure (0.1) blocked in court, reverts.
- `retraining_pct_gdp` 0 — bill failed.
- `housing_policy` 0 this round — federal spending passed in a one-year round bites next round: 0.1 (half of 0.2) in round 02, plus the states' +0.05 then due.
- `shock_frontier_cog` +0.04 — event #3, Generation leap.
- All other levers unchanged at defaults: no decision touched them.

## Narrated only (no lever)
- AI firms' $2bn/yr Workforce Transition Compact: contingent on federal pre-emption, which Washington did not offer; not paid. (At about 0.006% of GDP it would be below the model's resolution anyway.)
- Lobbying by AI firms and entrepreneurs; households' demands and votes; employers' offer of hours talks (no agreement reached, so `hours_share` unchanged).
- Federal work-sharing trigger died with the bill.

## Non-players
- Central bank (hawkish): unemployment barely moved, no action.
- States (mixed): nothing due this round; +0.05 on housing falls due in round 02.
- Rest of world: keeps deploying; no effect.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t01/levers.json --years 1 --label 2027` — outputs reported unaltered in the sitrep.

## Carry-forward for round 02
- `housing_policy` 0.15 (federal 0.1 + states 0.05).
- `union_pressure` fades to 0.15 unless renewed.
- Employers' profit-sharing pledge: no kept-pledge roll unless profits come under pressure.
- Disclosure rule stays blocked until re-enacted (new roll).
- Event #20 drawn for round 02: `shock_demand_pct` +1.0, `shock_new_task` 1.2.
