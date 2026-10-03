# Resolution — round 05 (2031–32)

## Rolls (odds stated before rolling; see `log.md`)
- **Household local enforcement drives, about 10 sites** (0.35; unemployment over 5%, unrest under 50). Small drive, sized as in round 04: success = pressure held at 0.3. r=0.9867 → **FAIL**.
- **Paycheck Bridge Act** (medium, divided 0.35; −0.15 new tax and transfers cut against growth-first; +0.10 pre-emption rider fits = 0.30). r=0.7313 → **FAIL**. No cheques, no levy, no pre-emption to 2034, no work-sharing extension.
- **Factory Homes Act** (small, divided 0.55, +0.10 fits = 0.65). r=0.6853 → **PARTIAL**: half-size.
- **Election, November 2032** (0.35 + 0.01 × (35.3 − 35) − 0.10 median income more than 3 points above 2029 = 0.25). r=0.2462 → **SUCCESS: growth-first loses; worker-first leads.** Configuration draw 1 → **divided → responsive**.
- Statistics noise: draw 3 → none.

## Levers
- `deploy_pace` 1.0 — labs hold pace.
- `ai_pricing` 0 — labs: usage tier stays open (+0.5), two-year terms at −15% with volume lock-in (0), netted +0.25; employers keep most savings (−0.25).
- `adoption_speed` 1.0 — employers: "normal", no drive (was 1.05).
- `layoff_share` 0.45 — employers' stated share.
- `hours_share` 0.25 — employers' stated share; within two notches and under the ceiling.
- `wage_sharing` 0.15 — profit-share kept in writing.
- `new_business` 1.2 — base 1.1; housing firms that hire (+0.1) net against AI-only firms (−0.1); +0.1 standing, Main Street Act in force.
- `union_pressure` 0.2 — drive failed, fades 0.1.
- `household_saving` 0 — households chose to hold steady, overriding the automatic +0.01.
- `retraining_pct_gdp` 0.175 — 0.1 plus Main Street's 0.15 for one of two years.
- `housing_policy` 0.825 — carried 0.65; entrepreneurs' housing push +0.05; labs' robot makers supplying home factories +0.05 (off-menu, by analogy with the entrepreneurs' item and counted inside its 0.15 cap, now used up); Factory Homes Act half-size +0.075 (full size judged +0.15, between "funded programme" 0.4 and 0.7).
- `shock_housing_pct` −3.0 — event #14.
- `transfers_pct_gdp`, `capital_tax_pct`, `deploy_regulation` 0.1, `competition_policy` 0.3 — unchanged.

## Narrated only (no lever)
- Labs released the $1bn and doubled the training fund to $1bn a year, so pre-emption held to end 2032. It then **lapsed**: the 2034 extension died with the Paycheck Bridge Act. The $2bn stays in escrow.
- Consent decree: Washington offered open access plus a small-business tier; the labs offered a decree without those terms. Neither accepted the other's, so the cases continue.
- Term sheet: both sides agree notice, advisory seats with sight of deployment plans, and pilot-site no-layoff and shorter weeks. Penalties for breach and the 12-month review are not agreed.
- Entrepreneurs' written trainee-pay pledge; labs' $300m political spend; employers' 5% price cuts in retail and office lines.

## Non-players
- Central bank (hawkish): nothing. States: no housing step due; unemployment under 6%, no cuts.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t05/levers.json --years 2 --label 2031-32`

## Carry-forward for round 06
See `turns/t06/intel/_clock.md`.
