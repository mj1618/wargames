# Resolution — round 02 (2028)

## Rolls
| What | Odds | Result |
|---|---|---|
| Households' organising drive, renewed (0.35; +0.15 unemployment under 5%) | 0.50 | r=0.87 FAIL |
| Bill 1, Worker Transition Act (medium 0.60; a new tax cuts against coalition −0.15; labs silent, so no joint-support bonus) | 0.45 | r=0.57 PARTIAL — half-size |
| Bill 2, work-sharing subsidy and new-firm credit (small 0.80; fits coalition +0.10) | 0.90 | r=0.46 SUCCESS |
| Court blocks Bill 1's levy | 0.20 | r=0.70 FAIL — stands |
| Election: growth-first loses lead (0.35 + 0.01 × 2.0 unrest) | 0.37 | r=0.99 FAIL — keeps lead |
| Election: configuration | draw 3 | 3 → responsive becomes **divided** |
| Statistics noise | draw 5 | 2 → −0.1 points |

## Levers
- `deploy_pace` 1.25 — labs race, explicitly +25%.
- `ai_pricing` −0.25 — labs cut the old generation hard with open access and no lock-in, but hold premium on the new one: half a notch (+0.25) from −0.5. Employers pass on half, keep half: 0.
- `adoption_speed` 1.25 — employers, explicitly +25%; no mass restructuring.
- `layoff_share` 0.35, `hours_share` 0.15 — as employers stated.
- `wage_sharing` 0.1 — profit-sharing at 10% of automation savings.
- `new_business` 1.1 — the people-heavy push stands (+0.1; no second notch, since 40% still goes to AI-only firms); standing −0.1 lapses because `ai_pricing` is above −0.5.
- `union_pressure` 0.25 — drive renewed, so no fade; it failed, so no gain.
- `household_saving` 0.01 — households, about 1 point.
- `transfers_pct_gdp` 0.01 — labs' fund at $3bn is still 0.01% of GDP.
- `retraining_pct_gdp` 0.1 — round-01 law in force.
- `housing_policy` 0.5 — 0.2 + 0.2 federal incentives in force + 0.05 states + 0.05 founders' factory-built push.
- `deploy_regulation` 0.1, `competition_policy` 0.3 — unchanged; the notice rule is disclosure-class.
- `shock_frontier_cog` +0.04 — event 3.

## Carried to round 03
- Bill 1 at half-size from 2029: `capital_tax_pct` 2.5, retraining +0.15, 30-day notice. Bill 2 from 2029: retraining-line cost +0.15 (so `retraining_pct_gdp` 0.4), `hours_share` ceiling 0.5, small-business law gives `new_business` standing +0.1.
- States +0.05 on `housing_policy`; founders' push has 0.05 left.
- `union_pressure` fades to 0.15 unless renewed. `household_saving` persists.
- Law odds now use the divided row.

## Non-players and off-menu
- Central bank: unemployment up 0.1 point; no action. States: no cuts.
- Front-loading housing grants into swing metros changes timing, not size: no lever. Narrated only: lobbying, founders' antitrust testimony, capacity contracts, protests.

## Model result (unaltered)
3.91m jobs destroyed (1.92m office), 2.35m created (1.33m new kinds of work, 0.92m from cheaper output), net −1.57m, plus 0.65m from population growth; employment 160.89m. Unemployment 4.43%, participation 60.78%, employment rate 58.09%. Real pay 102.2, median real income 101.2, bottom fifth 101.3. Labour share 50.3%, top-1% share 21.1%. GDP +2.57%. Housing costs 94.9. Poverty 12.6%, homelessness 19.0. Deficit 6.4%, debt 104.3%. Unrest 37.0. Desk work: machines could do 31.5%, do 9.5%.
