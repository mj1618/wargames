# Resolution — round 06 (2033–34)

## Rolls (odds stated before rolling; see `log.md`)
- **Household drives, about 10 small sites** (0.35 +0.15 unemployment under 5% = 0.50; small drive as rounds 04–05: success = pressure held at 0.2). r=0.7184 → **FAIL**.
- **Fair Share and Stability Act** (medium, responsive 0.60, +0.10 fits worker-first = 0.70; labs and employers did not both publicly oppose; event #24 has no effect on odds). r=0.7378 → **PARTIAL**: half-size.
- **Main Street and Work-Sharing Renewal** (small, responsive 0.80, +0.10 fits = 0.90). r=0.3337 → **SUCCESS**.
- **Court blocks the levy** (0.20). r=0.8043 → **FAIL**: levy stands.
- **Election, November 2034** (0.35 + 0.01 × (32.3 − 35) − 0.10 median income more than 3 points above 2030 = 0.22). r=0.4098 → **FAIL: worker-first keeps its lead.** Configuration draw 2 → stays **responsive**.
- Statistics noise: draw 1 → unemployment −0.2, median income −1.0.

## Levers
- `deploy_pace` 1.0 — labs: "steady"; extra capex goes to tooling and housing robots, not the frontier.
- `ai_pricing` 0 — labs' new small-business tier (+) nets against longer three-year lock-in terms (−); employers' own pricing unchanged.
- `adoption_speed` 1.05 — employers' "normal to slightly faster (~+10%)", midpoint, as in round 04.
- `layoff_share` 0.45, `hours_share` 0.25, `wage_sharing` 0.15 — employers hold all three (shorter weeks self-funded at pilot sites; profit-share floor signed).
- `new_business` 1.3 — base 1.1; 15% expansion, three-quarters in firms that hire (+0.1); +0.1 standing, small-business law in force again.
- `union_pressure` 0.1 — drive failed, fades 0.1.
- `household_saving` 0 — households hold steady; their condition for saving more (yields spiking, layoffs climbing) was not met.
- `capital_tax_pct` 1.5 — half-size levy is 3 points, from 2034: one of two years.
- `transfers_pct_gdp` 0.125, `transfer_target` 1.0 — half-size 0.25 to the bottom two-fifths, from 2034: one of two years.
- `retraining_pct_gdp` 0.225 — standing 0.1; Fair Share half-size +0.1 and Renewal +0.15, each from 2034, so half counted this round.
- `housing_policy` 0.875 — carried 0.825 plus the states' scheduled +0.05 (now at their ceiling). Private housing push already at its cap.
- `deploy_regulation` 0.1, `competition_policy` 0.3 — Washington's stated choice: no pre-emption, cases continue.
- No shocks: event #24 is headline only (deficit 6.2%).

## Narrated only (no lever)
- Labs' package (4-point levy, open-access decree, $2bn, for pre-emption to 2036) was refused on pre-emption. No decree; $2bn stays in escrow; states may license.
- Labs–employers contract: labs offered three years at 50% volume, employers countered two years at 20%. Not matched.
- Term sheet: notice, 1.5% profit-share floor, advisory seats, 12-month review and back-pay remedy agreed. Fixed fine and a no-layoff clause that widens after each review not agreed.
- Entrepreneurs' $600m-a-year paid-to-train places; labs' $400m political spend and training fund (too small for a lever).

## Non-players
- Central bank: nothing. States: housing step applied; no budget cuts.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t06/levers.json --years 2 --label 2033-34`

## Carry-forward for round 07
See `turns/t07/intel/_clock.md`.
