# Resolution — round 02 (2028)

## Rolls (odds stated before rolling; see `log.md`)
- **Household organising drive, first contracts** (0.35 +0.15 unemployment under 5% = 0.50): r=0.2579 → **SUCCESS**.
- **First Job and Wage Insurance Act** (small, divided 0.55, +0.05 `union_pressure` now 0.5 = 0.60, partial band 0.15): r=0.2846 → **SUCCESS**. Bites next round.
- **AI Deployment Framework Act: no vote, no roll.** Washington required the labs' $2bn before the floor vote; the labs kept it "reserved for pre-emption". Neither order is altered, so no vote.
- **Election, November 2028** (0.35 + 0.01 × (34.5 − 35) = 0.345; income +2.2 in two rounds, no adjustment): r=0.4295 → **FAIL**, growth-first keeps its lead. Configuration draw 1 of 3 → one step more responsive: **divided → responsive**.
- Statistics noise: draw 1 of 5 → unemployment −0.2, median income −1.0.

## Levers
- `deploy_pace` 1.2 — AI firms keep racing at +20%.
- `ai_pricing` −0.25 — AI firms split: enterprise bundles and lock-in (−0.5) net against consumer price cuts and open APIs (+0.5) = 0; employers did not revisit keeping their savings (−0.25 stands).
- `adoption_speed` 1.2 — employers' stated "20% faster than normal".
- `layoff_share` 0.4, `hours_share` 0.1 — employers hold. Hours pilot not agreed (households want no-layoff terms; employers walk from job guarantees).
- `wage_sharing` 0.15 — profit-sharing pool raised from about 1% to about 1.5% of payroll (pro rata to last round's 0.1; off-table size).
- `new_business` 1.1 — entrepreneurs move 60% of expansion capital to firms that hire (+0.1 on a base of 1.0); standing adjustment now 0 because `ai_pricing` is above −0.5.
- `union_pressure` 0.5 — drive succeeded (+0.25).
- `household_saving` 0 — households hold.
- `housing_policy` 0.15 — carried in (federal half-size incentives 0.1 + states 0.05). Faster delivery is not a new measure.
- `retraining_pct_gdp` 0 this round — Act passed in a one-year round, so 0.1 starts in round 03.
- `deploy_regulation` 0 — statutory disclosure died with the unvoted bill.
- `shock_demand_pct` +1.0, `shock_new_task` 1.2 — event #20, Cheap services catch on.
- All others unchanged.

## Narrated only (no lever)
- AI firms' $500m-a-year training fund (0.002% of GDP, too small to model), voluntary disclosure, $300m political spend, 90-day-notice template clause.
- Employers' 60-day notice agreement; federal attrition-first compact (already in `layoff_share` 0.4).
- Entrepreneurs' antitrust and open-access lobbying: Washington ordered nothing, so `competition_policy` stays 0.

## Non-players
- Central bank (hawkish): no trigger, no action.
- States: housing +0.05 fell due this round (included above); next due round 04. No budget cuts.
- Courts: no new federal rule or tax to challenge.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t02/levers.json --years 1 --label 2028`

## Carry-forward for round 03
- `retraining_pct_gdp` 0.1 takes effect.
- `union_pressure` fades to 0.4 unless renewed.
- Political configuration **responsive**; growth-first leads.
- Shocks reset. Event #23 drawn (data revision; no model effect).
