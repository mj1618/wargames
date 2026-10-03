# Resolution — round 07 (2035–36)

## Rolls (odds stated before rolling; see `log.md`)
- **Household drives, about 8 small sites** (0.35 +0.15 unemployment under 5% = 0.50; small drive as rounds 04–06). r=0.8010 → **FAIL**.
- **Metro Homes and Insurance Act** (medium, responsive 0.60; no adjustment). r=0.0791 → **SUCCESS**.
- **AI Services Levy and Open Access Act** (medium, 0.60; +0.10 levy and open access fit worker-first; −0.15 pre-emption cuts against = 0.55; labs and employers neither both backed nor both opposed). r=0.6482 → **PARTIAL**: half-size.
- **Court blocks that Act** (0.20). r=0.6812 → **FAIL**: stands.
- **Election, November 2036, narration only** (0.35 + 0.01 × (30.1 − 35) − 0.10 = 0.20). r=0.6294 → worker-first keeps its lead.
- Statistics noise: draw 5 → unemployment +0.2, median income +1.0.

## Levers
- `deploy_pace` 1.05 — labs: models steady, robot lines +15%; half a notch, as only robots speed up.
- `ai_pricing` 0.125 — labs' open access and small-business tier are worth +0.25 on their side; they arrive only through the half-size Act, so half. Employers' own pricing unchanged.
- `adoption_speed` 1.05, `layoff_share` 0.45, `hours_share` 0.25, `wage_sharing` 0.15 — employers hold all four ("about +10%" read as in rounds 04 and 06).
- `new_business` 1.25 — base 1.2; the 15% hiring push (+0.1) nets against a 30% AI-only slice (−0.1), the round-05 rule; standing +0.05 because the Main Street law covers 2035 only. Rule adopted after the round-06 audit: a law in force for one of two years counts half.
- `union_pressure` 0.0 — drive failed; fades.
- `household_saving` 0 — households hold steady.
- `transfers_pct_gdp` 0.25, `transfer_target` 1.0 — Fair Share cheques, both years.
- `capital_tax_pct` 3.5 — levy from 3 towards 4, half-size.
- `retraining_pct_gdp` 0.325 — standing 0.1 + Fair Share 0.15 + Renewal 0.15 for 2035 only (0.075). This includes the round-06 audit correction (Fair Share is 0.15, not 0.1). Washington lets Main Street money lapse.
- `deploy_regulation` 0.2 — a single federal licensing standard would be 0.3 (from 0.1); half-size.
- `competition_policy` 0.45 — open-access mandate would be 0.6 (from 0.3); half-size.
- `housing_policy` 0.9875 — federal rung rises from 0.475 to 0.7, funded from 2036, so half the step (0.5875); plus states 0.15, private 0.15, event #14 0.1.
- `shock_housing_pct` +3.0 — event #15.
- `public_jobs_m`, `worktime_cut_pct` 0 — no decision.

## Narrated only (no lever)
- Half-size Act read as: open access and the small-business tier bind the largest labs on a phased schedule; the federal licensing standard pre-empts state licensing to end 2036; $1bn of the $2bn is released into paid-to-train places. The labs asked for 2038 and did not get it.
- Labs–employers contract: labs accepted the two-year counter with a changed floor; employers' orders keep one-year, most-favoured pricing. Not signed.
- Households–employers term sheet signed: capped breach penalties, 12-month review, site-level no-layoff.
- Households' housing and insurance campaign; entrepreneurs' $600m-a-year trainee cohort and move to secondary metros; labs' $300m for factory homes and $450m political spend (too small for a lever).
- No pledge roll: profits not under pressure.

## Non-players
- Central bank (hawkish): unemployment not under 3.5%, nothing. States: at housing ceiling; no budget cuts.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t07/levers.json --years 2 --label 2035-36`
