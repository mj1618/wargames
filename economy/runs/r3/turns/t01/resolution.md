# Resolution — round 01 (2027)

## Rolls
| What | Odds | Result |
|---|---|---|
| Housing bill (small; responsive 0.80; mixes deregulation and spending, so no instinct adjustment) | 0.80 | r=0.32 SUCCESS |
| Small-business credit + work-sharing subsidy (small 0.80; fits coalition instincts +0.10) | 0.90 | r=0.52 SUCCESS |
| Court blocks the executive disclosure rule | 0.35 | r=0.12 SUCCESS — blocked |
| Households' organising drive (0.35, +0.15 unemployment under 5%) | 0.50 | r=0.78 FAIL |
| Statistics noise | draw 5 | 3 → no noise |

## Levers
- `deploy_pace` 1.2 — AI firms race, explicitly +20% (two notches).
- `ai_pricing` −0.75 — AI firms premium and bundling (−0.5); employers keep about two-thirds of savings (−0.25).
- `adoption_speed` 1.15 — employers' company-wide drive (one notch).
- `layoff_share` 0.4 — employers state 40%: attrition and hiring freeze (within two notches).
- `hours_share` 0.1 — employers state about 10%; unchanged.
- `wage_sharing` 0 — no general raises; metro stipends too small to register.
- `new_business` 0.95 — formation push is a notch (+0.1), but 55% goes to AI-only firms with few staff, so half-size (+0.05); standing adjustment −0.1 because `ai_pricing` ≤ −0.5. The credit law is not yet in force.
- `union_pressure` 0 — drive failed.
- `household_saving` 0 — held by households.
- `transfers_pct_gdp` 0.01, `transfer_target` 0 — labs' unconditional $2bn-a-year transition fund (0.006% of GDP, rounded). The $5bn tier was conditional on pre-emption, which was not granted. Target not specified, left unchanged.
- `deploy_regulation` 0 — disclosure rule (0.1) blocked in court; reverts and stays at 0 until re-enacted.
- `housing_policy` 0 — bill passed but federal spending takes effect next round. States contribute nothing (S3).
- `shock_housing_pct` +3.0 — event 15.
- All other levers unchanged (defaults).

## Carried to round 02
- `housing_policy` 0.4 from 2028 (funded building with zoning conditions).
- Small-business law in force from 2028: standing +0.1 on `new_business` (nets against −0.1 while `ai_pricing` ≤ −0.5); work-sharing subsidy lifts the `hours_share` ceiling to 0.5; cost booked as `retraining_pct_gdp` 0.05, the size enacted.
- Labs' fund is a company pledge: roll 0.60 that it is kept only if profits come under pressure.
- Disclosure rule needs a new bill and a new roll.

## Non-players and off-menu
- Central bank: unemployment rose 0.07 points; no action. States: no housing help; budgets untouched.
- Narrated only, no model effect: labs' $600m lobbying and $300m pro-housing campaigns; pre-emption request (not taken up); entrepreneurs' geographic split and lobbying; tenant unions and pro-permit turnout; employers' offer of hours talks.

## Model result (unaltered)
0.71m jobs destroyed (0.41m office), 0.33m created (0.30m new kinds of work), net −0.38m, plus 0.65m from population growth; employment 162.66m. Unemployment 4.17%, participation 61.52%, employment rate 58.96%. Real pay 100.7, median real income 100.4, bottom fifth 99.9. Labour share 52.5%, top-1% share 20.2%. GDP +1.66%. Housing costs 101.1. Poverty 12.9%, homelessness 22.2. Deficit 6.0%, debt 102.5%. Unrest 35.3.
