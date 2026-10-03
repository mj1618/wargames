# Round 04 clock (referee)

- **Period:** January–December 2030. Model label `2030`, `--years 1`.
- **Election at end of round:** November 2030, Congress. Lead-coalition-loss odds: 0.35 + 0.01 × (unrest − 35), −0.10 if median income is more than 3 above 2028's 105.1, +0.10 if below it; then configuration draw.
- **Event drawn:** #9 **New-work mirage.** Last year's fashionable new job category is itself automated.
- **Model effect (referee only):** `shock_new_task` 0.7 this round.
- **Non-player rule firing:** hawkish central bank — unemployment 3.23% is under 3.5% → `shock_demand_pct` **−0.5** this round. (The round-03 +1.5 boost also ends.)
- **Carried in from round 03 (apply before players' new decisions):**
  - `housing_policy` **0.6**: federal 0.4 + event 0.1 + entrepreneurs 0.10 (another +0.05 if renewed; then at ceiling).
  - `deploy_regulation` **0.1** (statutory disclosure, full size; not blocked). `competition_policy` **0.3** (executive inquiry; not blocked).
  - `union_pressure` 0.5 → **0.4** unless renewed (new roll; success +0.25).
  - `retraining_pct_gdp` 0.11. Trigger (0.31) not met: unemployment 3.23%.
  - Other level levers from `state.json` → `prev_levers`: `deploy_pace` 1.25, `ai_pricing` −0.25, `adoption_speed` 1.2, `layoff_share` 0.35, `hours_share` 0.15, `wage_sharing` 0.15, `new_business` 1.12 (recompute standing adjustment), `household_saving` −0.005.
- **Pledges:** employers' profit-sharing and no-mass-layoff (signed through November 2030) — roll 0.60 only if profits come under pressure (labour share flat at 52.1%: they are not).
- **Standing non-player rules:** states add nothing on housing; no state cuts (unemployment under 6%). No automatic saving rise (unemployment fell).
- **Political configuration:** responsive; growth-first coalition leads. Unrest 29.3.
- **Published-statistics noise for round 03 figures:** unemployment −0.1 (published 3.1%), median income −0.5 (published about 109). Poverty and homelessness one round late.
