# Round 02 clock (referee only)

- **Period:** January–December 2028. Label `2028`, 1 year. **Election at end of round:** November 2028, President + Congress (referee guide §3).
- **Event drawn:** #17 **Open-weight price war** — free models match last year's best; prices for AI services collapse. (log: `r4 t02 event | DRAW 17 of 24`)
- **Model effect for `turns/t02/levers.json`:** +0.3 on `ai_pricing` this round only, on top of the value players' decisions produce, then clip.
- **Carried in from round 01:**
  - `retraining_pct_gdp` 0.05 takes effect (pilot passed at half size in 2027).
  - States (S3 = 2): +0.05 on `housing_policy` this round (0.1 → 0.15 unless federal action changes it).
  - `union_pressure` 0.25 fades to 0.15 unless households renew (new roll).
  - Liability shock (`shock_adoption` 0.8) has expired; the ruling still stands in the narrative. Safe harbour failed; AI firms' conditional $2bn fund not triggered.
- **Non-player rules:** central bank does not act (unemployment +0.2 < 0.7). No automatic saving rise. States do not cut (unemployment under 6%).
- **Politics:** growth-first leads; gridlocked (0.30 / 0.15 / 0.05). Unrest 35.7: no bonus. Deficit 6.1%: no penalty.
- **Published statistics (noise draw 2):** unemployment 4.2% (true 4.3), median income 100.4 (true 100.9). Poverty and homelessness for 2027 publish next round.
