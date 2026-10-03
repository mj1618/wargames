# Round 02 clock (referee)

- **Period:** January–December 2028. Model label `2028`, `--years 1`.
- **Election at end of round:** November 2028, President + Congress (resolve after the model step, guide §3).
- **Event drawn:** #14 **Housing breakthrough.** Factory-built homes win code approval in most states; costs per home fall sharply.
- **Model effect (referee only):** `shock_housing_pct` −3.0 this round; +0.1 on `housing_policy` permanently.
- **Carried in from round 01 (apply before players' new decisions):**
  - `housing_policy` 0.2 (Bill 1 in force) + 0.1 (event) = **0.3**. Entrepreneurs' factory-housing push is now eligible (`housing_policy` ≥ 0.2).
  - `retraining_pct_gdp` **0.11** (Bill 2 at 0.1 + labs' fund 0.01). Trigger: 0.31 the round after scorecard unemployment exceeds 6%.
  - `deploy_regulation` 0 — disclosure order blocked in court; stays 0 until re-enacted with a new roll.
  - All other level levers carry from `state.json` → `prev_levers`: `deploy_pace` 1.15, `ai_pricing` −0.5, `adoption_speed` 1.1, `layoff_share` 0.4, `wage_sharing` 0.1, `new_business` 1.02 (recompute the standing adjustment), `union_pressure` 0.
- **Pledges:** employers' profit-sharing — roll 0.60 to hold only if profits are under pressure (they are not: labour share fell).
- **Standing non-player rules:** hawkish central bank (no trigger: unemployment 4.07%, change −0.03); states add nothing on housing; no state budget cuts.
- **Political configuration:** responsive; growth-first coalition leads. Unrest 34.8.
- **Published-statistics noise for round 01 figures:** unemployment −0.2 (published 3.9%), median income −1.0 (published 100.5). Poverty and homelessness published one round late.
