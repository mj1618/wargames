# Resolution — round 03 (2029)

## Rolls (odds stated before rolling; see `log.md`)
- **Household organising drive, next tier** (0.35 +0.15 unemployment under 5% = 0.50): r=0.9658 → **FAIL**.
- **AI Deployment Framework Act** (medium, responsive 0.60, +0.10 fits coalition = 0.70, partial band 0.15). Washington's condition was $2bn in escrow before the vote; the labs put $2bn in an escrow trust, so the vote happened. r=0.0008 → **SUCCESS**. Court challenge (0.20): r=0.6940 → not blocked.
- **Housing Supply Act** (medium, 0.60, +0.10 fits coalition as in round 01, offset so no deficit penalty = 0.70): r=0.2543 → **SUCCESS**. Spending law in a one-year round: bites round 04.
- **Court blocks executive antitrust cases** (0.35): r=0.9204 → not blocked.
- Statistics noise: draw 3 of 5 → no adjustment.

## Levers
- `deploy_pace` 1.2 — AI firms race at +20% again.
- `ai_pricing` −0.25 — AI firms: two-year bundles (−0.5) net against a further 20% consumer cut (+0.5) = 0; employers keep prices unchanged (−0.25). Same reading as round 02.
- `adoption_speed` 1.2 — employers' stated "~20% faster".
- `layoff_share` 0.4 — employers hold attrition-first, now in writing.
- `hours_share` 0.12 — employers' stated figure for the bounded shorter-week pilot (their own decision; off-table size).
- `wage_sharing` 0.15 — profit-share held at about 1.5% of payroll.
- `new_business` 1.2 — entrepreneurs' big push to firms that hire, +0.1 on 1.1; standing adjustment 0 (`ai_pricing` between ±0.5, no small-business law).
- `union_pressure` 0.4 — drive failed, so it fades 0.1.
- `household_saving` −0.01 — households spend more freely.
- `retraining_pct_gdp` 0.1 — First Job and Wage Insurance Act takes effect.
- `deploy_regulation` 0.1 — Framework Act makes disclosure statutory. Pre-emption of state licensing has no lever.
- `competition_policy` 0.3 — two executive antitrust cases (within the 0.4 executive ceiling).
- `housing_policy` 0.15 — unchanged this round. Entrepreneurs' factory-housing push has no effect while the lever is under 0.2.
- No shocks: event #23 has no model effect. All others unchanged.

## Narrated only (no lever)
- $2bn Workforce Compact trust: $1bn released on enactment, $1bn in 2030 (about 0.003% of GDP a year, too small to model). Labs' $350m political spend and $500m training fund.
- Employers' written compact and redesign panels; entrepreneurs' paid training and open-access lobbying; households' counter-offer.

## Non-players
- Central bank (hawkish): model unemployment 4.04% then 4.12%; no trigger.
- States: no housing step this round (next due round 04); no budget cuts.
- No election this round.

## Model run
`python3 economy/model/econ.py step --run economy/runs/r5 --levers economy/runs/r5/turns/t03/levers.json --years 1 --label 2029`

## Carry-forward for round 04
- `housing_policy` 0.50: federal funded programme with zoning conditions 0.4 (replaces incentives 0.1) + states 0.10 (second +0.05 falls due). The Act's offset trims *unused* retraining authority, so `retraining_pct_gdp` stays 0.1.
- `union_pressure` fades to 0.3 unless renewed.
- Event #5 Financial wobble: `shock_demand_pct` −2.0, `shock_adoption` 0.9, −0.1 on `new_business`.
- Election November 2030 (Congress) at end of round 04. Configuration responsive; growth-first leads.
