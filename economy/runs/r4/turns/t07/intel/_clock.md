# Round 07 clock (referee only)

- **Period:** January 2035–December 2036. Label `2035-36`, 2 years. **FINAL ROUND** — sitrep starts with `END`. Election November 2036: narrate only.
- **Event drawn:** #20 **Cheap services catch on** — households buy AI-delivered tutoring, legal help and home design in bulk, with people in the loop. (log: `r4 t07 event | DRAW 20 of 24`; no repeat)
- **Model effect for `turns/t07/levers.json`:** `shock_demand_pct` +1.0; `shock_new_task` 1.2.
- **Carried in from round 06:**
  - `union_pressure` 1.0 fades to 0.9 unless renewed (new roll; success +0.25, cap 1.0).
  - `capital_tax_pct` 7; `transfers_pct_gdp` 0.408 (dividend 0.4 + labs' funds 0.003 + 0.005), `transfer_target` 1.0; `retraining_pct_gdp` 0.4.
  - `housing_policy` 0.70: federal 0.40, states 0.15 (ceiling), entrepreneurs 0.15 (limit). No further automatic steps.
  - `deploy_regulation` 0.3; `ai_pricing` −0.5; `new_business` underlying 1.1, standing −0.1 while `ai_pricing` ≤ −0.5 and no small-business law.
  - `deploy_pace` 1.2, `adoption_speed` 1.15, `layoff_share` 0.45, `hours_share` 0.30 (unsubsidised ceiling), `wage_sharing` 0.10, `household_saving` 0.005 persist.
  - No federal safe harbour or statutory levy freeze; state due-care presumptions in several large states (narrated).
  - Event 10 bonus: +0.10 to a federal wage-insurance-plus-cash bill, last round it applies.
- **Non-player rules:** central bank does not act (unemployment rose 0.08; 4.25% is above 3.5%). No automatic saving rise. States do not cut (under 6%).
- **Politics:** worker-first leads; **responsive** (0.80 / 0.60 / 0.40). Fits worker-first instincts +0.10; against −0.15. Unrest 31.1: no bonus. Deficit 5.2%: no penalty. `union_pressure` ≥ 0.5: +0.05 for worker bills. Two-year round: taxes and spending take effect this round.
- **Published statistics (noise draw 4: +0.1):** unemployment 4.4% (true 4.25), median income 120.7 (true 120.2). Poverty and homelessness for 2034 (8.6%, 14.1) publish next round.
