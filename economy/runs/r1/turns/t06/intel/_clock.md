# Round 06 clock (referee)

- **Period:** January 2033–December 2034. Model label `2033-34`, `--years 2`. One set of decisions for both years.
- **Election at end of round:** November 2034, Congress. Lead-coalition-loss odds: 0.35 + 0.01 × (unrest − 35), −0.10 if median income is more than 3 above 2030's 108.4, +0.10 if below it; then configuration draw.
- **Event drawn:** #15 **Housing squeeze.** AI wealth concentrates in a few metros and bids up land; insurers pull out of others.
- **Model effect (referee only):** `shock_housing_pct` +3.0.
- **Non-player rules:** central bank (hawkish) — unemployment 3.01% is under 3.5% → `shock_demand_pct` **−0.5**. States: no housing contribution; no cuts (unemployment under 6%). No automatic saving rise (unemployment fell).
- **Carried in from round 05 (apply before players' new decisions):**
  - `ai_pricing`: event 17's +0.3 has ended; players' base is **0.25** (was 0.55 in the model last round).
  - `new_business`: recompute from 1.0 each round; standing +0.1 only if `ai_pricing` ≥ 0.5 (no small-business law: Bill 1 failed).
  - `union_pressure` 0.65 → **0.55** unless renewed (new roll; success +0.25).
  - `retraining_pct_gdp` 0.21; wage-insurance trigger 5% unemployment (0.31 extra): not met.
  - `housing_policy` 0.6 (federal 0.4 + event 0.1 + entrepreneurs 0.10; 0.05 left if they resume).
  - `deploy_regulation` 0.1; `competition_policy` 0.3 (consent decree in force: no renewal of exclusives, binding small-firm terms).
  - Other level levers from `state.json` → `prev_levers`: `deploy_pace` 1.2, `adoption_speed` 1.25, `layoff_share` 0.3, `hours_share` 0.2 (ceiling 0.3: no work-sharing law), `wage_sharing` 0.2, `household_saving` 0.005, `capital_tax_pct` 0.
- **Pledges:** employers' no-mass-layoff pledge expired November 2032; profit-sharing stands. Roll 0.60 only if profits come under pressure (labour share fell to 49.9%: they are not).
- **Political configuration:** **responsive** (small 0.80 / medium 0.60 / large 0.40); growth-first coalition leads. Unrest 26.1. Two-year round: spending and taxes take effect the same round.
- **Published-statistics noise for round 05 figures:** unemployment +0.2 (published 3.2%), median income +1.0 (published about 119). Poverty and homelessness one round late.
