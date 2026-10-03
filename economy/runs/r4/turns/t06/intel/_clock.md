# Round 06 clock (referee only)

- **Period:** January 2033–December 2034. Label `2033-34`, 2 years. **Election at end of round: November 2034, Congress.**
- **Event drawn:** #10 **A state pilot works** — a large state's wage-insurance-plus-cash pilot shows faster re-employment at modest cost. (log: `r4 t06 event | DRAW 10 of 24`)
- **Model effect for `turns/t06/levers.json`:** none. +0.10 to the odds of a similar federal bill (wage insurance plus cash) in rounds 06 and 07.
- **Carried in from round 05:**
  - `union_pressure` 0.9 fades to 0.8 unless renewed (new roll; success +0.25, cap 1.0).
  - `capital_tax_pct` 7 (survived court), `transfers_pct_gdp` 0.303 with `transfer_target` 1.0, `retraining_pct_gdp` 0.3.
  - `housing_policy` 0.60: federal 0.40 (Housing Build Act), states 0.10 (+0.05 due this round, to their 0.15 ceiling → 0.65 before decisions), entrepreneurs' push 0.10 of a possible 0.15.
  - `deploy_regulation` 0.3; `ai_pricing` −0.5; `new_business` underlying 1.1, standing −0.1 while `ai_pricing` ≤ −0.5 and no small-business law.
  - `deploy_pace` 1.2, `adoption_speed` 1.15, `layoff_share` 0.45, `hours_share` 0.30 (unsubsidised ceiling), `wage_sharing` 0.10, `household_saving` 0.005 persist.
  - No safe harbour; no industry fund beyond the labs' $1bn; labs' layoff-notice pledge and the Employers–Households entry-level pledge are in force (narrated).
- **Non-player rules:** central bank does not act (unemployment rose 0.03; 4.17% is above 3.5%). No automatic saving rise. States do not cut.
- **Politics:** worker-first leads; **responsive** (0.80 / 0.60 / 0.40). Fits worker-first instincts +0.10; against −0.15. Unrest 32.7: no bonus. Deficit 5.4%: no penalty. `union_pressure` ≥ 0.5: +0.05 for worker bills. Two-year round: taxes and spending take effect this round. Election roll at end of round: p = 0.35 + 0.01 × (unrest − 35), +0.10 if median income is below end-2030 (108.2), −0.10 if more than 3 points above it; then configuration draw.
- **Published statistics (noise draw 2: −0.1):** unemployment 4.1% (true 4.17), median income 113.3 (true 113.8). Poverty and homelessness for 2032 (9.7%, 15.7) publish next round.
