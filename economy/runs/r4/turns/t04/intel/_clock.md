# Round 04 clock (referee only)

- **Period:** January–December 2030. Label `2030`, 1 year. **Election at end of round: November 2030, Congress.**
- **Event drawn:** #2 **Robot recall** — injuries in warehouses and homes force a recall and new safety certification. (log: `r4 t04 event | DRAW 2 of 24`)
- **Model effect for `turns/t04/levers.json`:** `shock_robot_lag_years` +1.0; `shock_adoption` 0.9.
- **Carried in from round 03:**
  - Worker Transition Act takes effect: `retraining_pct_gdp` 0.3, `capital_tax_pct` 3 (court challenge already failed).
  - States' scheduled step: `housing_policy` 0.15 → 0.20 (states now 0.10 of their 0.15 ceiling). At 0.20 the entrepreneurs' factory-housing push earns +0.05 a round (max +0.15) for pushes made from this round on.
  - `ai_pricing` −0.5; `new_business` underlying 1.0, standing −0.1 while `ai_pricing` ≤ −0.5 (and no small-business law).
  - `union_pressure` 0.75 fades to 0.65 unless renewed (new roll).
  - `deploy_pace` 1.2, `adoption_speed` 1.15, `layoff_share` 0.45, `hours_share` 0.20, `wage_sharing` 0.05, `household_saving` 0.005, `transfers_pct_gdp` 0.003, `deploy_regulation` 0.1 persist.
  - Safe harbour not enacted; hiring-freeze disclosure still blocked; industry fund and signed pledges never happened. Executive's housing +0.1 is used up.
- **Non-player rules:** central bank does not act (unemployment fell 0.04). No automatic saving rise. States do not cut.
- **Politics:** worker-first leads; gridlocked (0.30 / 0.15 / 0.05). Fits worker-first instincts +0.10; against −0.15. Unrest 35.8: no bonus. Deficit 6.0%: no penalty. `union_pressure` ≥ 0.5: +0.05 for worker bills. Election roll at end of round: p = 0.35 + 0.01 × (unrest − 35), −0.10 if median income is more than 3 points above end-2028 (102.7); then configuration draw.
- **Published statistics (noise draw 1: −0.2):** unemployment 4.1% (true 4.32), median income 104.2 (true 105.2). Poverty and homelessness for 2029 (11.9%, 19.7) publish next round.
