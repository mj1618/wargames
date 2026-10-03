# Round 07 clock (referee)

- **Period:** January 2035–December 2036. Model label `2035-36`, `--years 2`. One set of decisions for both years. **FINAL ROUND: sitrep starts with `END`.** Never tell players.
- **Election at end of round:** November 2036, President + Congress — narrate only.
- **Event drawn:** #8 **A hit new industry.** A new kind of service nobody predicted takes off and hires people in large numbers.
- **Model effect (referee only):** `shock_new_task` 1.5.
- **Non-player rules:** central bank (hawkish) — unemployment 2.93% is under 3.5% → `shock_demand_pct` **−0.5**. States: no housing contribution; no cuts. No automatic saving rise.
- **Carried in from round 06 (apply before players' new decisions):**
  - `ai_pricing` 0.25. `new_business`: recompute from 1.0; standing +0.1 only if `ai_pricing` ≥ 0.5 or a small-business law passes.
  - `union_pressure` 0.55 → **0.45** unless renewed (new roll; success +0.25 on 0.55).
  - `retraining_pct_gdp` 0.21; wage-insurance trigger 5% unemployment (0.31 extra): not met.
  - `housing_policy` 0.75 (federal 0.55 + event 0.1 + entrepreneurs 0.10; 0.05 left if they resume).
  - `deploy_regulation` 0.1; `competition_policy` 0.3 (consent decree in force).
  - Bill 2: no-deployment-limits guarantee through 2036 takes force only if the labs' Fund reaches $6bn a year (committed: $3bn). Until then Congress may still legislate limits.
  - Other level levers: `deploy_pace` 1.15, `adoption_speed` 1.25, `layoff_share` 0.3, `hours_share` 0.2 (ceiling 0.3), `wage_sharing` 0.2, `household_saving` −0.005, `capital_tax_pct` 0.
- **Pledges:** employers' pledge expired November 2034; profit-sharing stands. Roll 0.60 only if profits come under pressure (labour share 48.3%: they are not).
- **Political configuration:** **responsive** (small 0.80 / medium 0.60 / large 0.40). **Worker-first coalition now leads Congress**; the presidency stays growth-first. S1 adjustments flip: +0.10 for bills fitting worker-first instincts (worker protection, transfers, levies on AI profits), −0.15 for bills against them. Unrest 22.0. Two-year round: spending and taxes take effect the same round.
- **Published-statistics noise for round 06 figures:** unemployment −0.1 (published 2.8%), median income −0.5 (published about 125). Poverty and homelessness one round late.
