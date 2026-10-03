# Resolution — round 02 (2028)

## Rolls
- **Youth Hiring and Apprenticeship Act** (bill 1, 0.15% of GDP). Small 0.30; no adjustment (a credit, but new spending; nobody else publicly backed the bill itself). r=0.472 → **FAIL**.
- **Accountable Automation Act** (bill 2). Not rolled. Government's own condition was "fund at least $20bn a year… or the bill does not move"; AI firms offered $1bn now and $3bn on passage. Condition unmet, so the bill stays in drafting. Safe harbour not enacted.
- **Court challenge to extending disclosure to hiring freezes** (executive action, 0.35). r=0.202 → **BLOCKED**. The original layoff rule stands.
- **Households' renewed, wider organising drive.** 0.35 +0.15 (unemployment under 5%) = 0.50, r=0.339 → **SUCCESS**.
- **Election, November 2028.** Lead coalition loses with p = 0.35 + 0.01×(36.0−35) = 0.36 (median income +2.7 over two rounds, under the 3-point threshold). r=0.052 → **growth-first loses; worker-first now leads.** Configuration draw 3 → more gridlocked; already at the floor, stays gridlocked.

## Levers
- `deploy_pace` 1.2 — AI firms "race, +20%" (their number).
- `ai_pricing` −0.2 — AI firms cut the commodity tier (+0.5) and lock in premium three-year bundles (−0.5): nets to zero. Employers pass on half only: zero. Event 17 adds +0.3 this round only, on the −0.5 carried.
- `adoption_speed` 1.15 — employers' company-wide drive, one notch.
- `layoff_share` 0.45 — held.
- `hours_share` 0.15 — "modestly toward 15–20%": the smallest figure given.
- `wage_sharing` 0 — "keep" current practice; no broad raises.
- `new_business` 1.0 — underlying 1.1 from 2027's push, −0.1 for expanding AI-only firms; people-heavy side "held", no notch. Standing adjustment is zero this round (`ai_pricing` above −0.5).
- `union_pressure` 0.5 — renewed, roll succeeded, +0.25.
- `household_saving` 0.005 — held flat.
- `transfers_pct_gdp` 0.003, `transfer_target` 0 — AI firms' unconditional $1bn-a-year worker fund (private; negligible).
- `retraining_pct_gdp` 0.05 — 2027's half-size pilot takes effect.
- `deploy_regulation` 0.1 — unchanged; the extension was blocked and was still only disclosure.
- `housing_policy` 0.15 — states' scheduled +0.05 (S3 = 2).
- All others unchanged. No shock levers.

## Narrated only
- Entrepreneurs' factory-housing push: no lever, because `housing_policy` is under 0.2.
- Employers' graduate-intake floor and no-mass-layoff pledge: their own conditions (no deployment rules, no profits tax) held, so it stood for 2028; already reflected in `layoff_share`.
- Labs' pledge and lobbying; households' campaign demands.

## Non-players
- Central bank: unemployment rose under 0.1 point. No action.
- States: no budget cuts (unemployment under 6%).
- Voters: see election roll.

## Carried to round 03
- Event 3 (generation leap): `shock_frontier_cog` +0.04.
- `ai_pricing` returns to −0.5 before new decisions (price-war bonus expires); `new_business` standing −0.1 returns if it stays there.
- `union_pressure` fades 0.1 unless renewed.
- Worker-first leads: +0.10 for bills fitting its instincts, −0.15 against. Still gridlocked (0.30 / 0.15 / 0.05).
- Employers' pledge, if renewed under profit pressure: kept with 0.60.
- States' next housing step is round 04.

## Statistics noise
Draw 3 of 5: none.
