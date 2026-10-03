# Round 05 clock (referee)

- **Period:** January 2031–December 2032. Model label `2031-32`, `--years 2`. One set of decisions for both years.
- **Election at end of round:** November 2032, President + Congress. Lead-coalition-loss odds: 0.35 + 0.01 × (unrest − 35), −0.10 if median income is more than 3 above 2029's 109.3, +0.10 if below it; then configuration draw.
- **Event drawn:** #17 **Open-weight price war.** Free models match last year's best; prices for AI services collapse.
- **Model effect (referee only):** +0.3 on `ai_pricing` this round, on top of the players' value (base 0.0), then clip.
- **Non-player rules:** central bank — no trigger (unemployment rose 0.46 to 3.69%; not under 3.5%). `shock_demand_pct` resets to 0 (the −0.5 ends). States: no housing contribution; no cuts (unemployment under 6%). No automatic saving rise (rise under 1 point).
- **Carried in from round 04 (apply before players' new decisions):**
  - `retraining_pct_gdp` **0.21** (Bill 1: federal 0.2 + labs' fund 0.01). Trigger now 5% unemployment (0.31 extra): not met.
  - `union_pressure` 0.75 → **0.65** unless renewed (new roll; success +0.25).
  - `housing_policy` 0.6 (federal 0.4 + event 0.1 + entrepreneurs 0.10; 0.05 left if they resume).
  - `deploy_regulation` 0.1, `competition_policy` 0.3 (inquiry open; labs' settlement accepted in substance — the federal player decides whether it closes).
  - Other level levers from `state.json` → `prev_levers`: `deploy_pace` 1.1, `ai_pricing` 0.0, `adoption_speed` 1.2, `layoff_share` 0.3, `hours_share` 0.2, `wage_sharing` 0.2, `new_business` 1.0 (recompute standing adjustment: +0.1 if `ai_pricing` including the event reaches 0.5), `household_saving` −0.005.
- **Pledges:** employers' no-mass-layoff pledge expired November 2030; profit-sharing stands. Roll 0.60 only if profits come under pressure (labour share fell to 50.4%: they are not).
- **Political configuration:** **divided** (small 0.55 / medium 0.35 / large 0.15); growth-first coalition leads. Unrest 29.9. Two-year round: spending and taxes take effect the same round.
- **Published-statistics noise for round 04 figures:** unemployment +0.1 (published 3.8%), median income +0.5 (published about 109). Poverty and homelessness one round late.
