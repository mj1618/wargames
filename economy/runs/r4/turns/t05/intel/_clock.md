# Round 05 clock (referee only)

- **Period:** January 2031–December 2032. Label `2031-32`, 2 years. **Election at end of round: November 2032, President + Congress.**
- **Event drawn:** #24 **Bond-market scare** — investors balk at federal borrowing. (log: `r4 t05 event | DRAW 24 of 24`)
- **Model effect for `turns/t05/levers.json`:** none. Last scorecard deficit is 5.7% of GDP, under the 7% trigger: headline only, no `shock_demand_pct`, no change to spending-bill odds.
- **Carried in from round 04:**
  - `union_pressure` 1.0 fades to 0.9 unless renewed (new roll; cap 1.0).
  - `deploy_regulation` 0.3 (executive robot certification, survived court; executive ceiling reached).
  - `housing_policy` 0.25: states 0.10 (next step round 06, to their 0.15 ceiling), executive 0.10 (used up), entrepreneurs' factory-housing push 0.05 of a possible 0.15 (+0.05 for a push this round).
  - `ai_pricing` −0.5; `new_business` underlying 1.1, standing −0.1 while `ai_pricing` ≤ −0.5 and no small-business law.
  - `capital_tax_pct` 3, `retraining_pct_gdp` 0.3, `deploy_pace` 1.2, `adoption_speed` 1.15, `layoff_share` 0.45, `hours_share` 0.25, `wage_sharing` 0.10, `household_saving` 0.005, `transfers_pct_gdp` 0.003 persist.
  - Shock levers reset: the recall's `shock_robot_lag_years` and `shock_adoption` are left out.
  - Safe harbour not enacted; labs' $2.5bn escrow lapsed; youth hiring and notice bill not voted; no industry fund; no signed pledge in force.
- **Non-player rules:** central bank does not act (unemployment fell 0.18; 4.14% is above 3.5%). No automatic saving rise. States do not cut.
- **Politics:** worker-first leads; **divided** (0.55 / 0.35 / 0.15). Fits worker-first instincts +0.10; against −0.15. Unrest 34.6: no bonus. Deficit 5.7%: no penalty. `union_pressure` ≥ 0.5: +0.05 for worker bills. Two-year round: federal spending and taxes passed take effect this round. Election roll at end of round: p = 0.35 + 0.01 × (unrest − 35), +0.10 if median income is below end-2029 (105.2), −0.10 if more than 3 points above it; then configuration draw.
- **Published statistics (noise draw 4: +0.1):** unemployment 4.2% (true 4.14), median income 108.7 (true 108.2). Poverty and homelessness for 2030 (11.4%, 18.7) publish next round.
