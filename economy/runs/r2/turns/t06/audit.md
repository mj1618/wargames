# Audit — round 06 (2033–34)

**Model integrity.** Re-ran `econ.py step` from `state-before-2033-34.json` with `t06/levers.json`: scorecard row and `state.json` reproduce exactly. No hand edits. Every roll is in `log.md` with stated odds; the result is reported unaltered; statistics noise and lags applied correctly.

**(a) Decisions.** None altered, added or dropped. Bill sizes re-classed per the guide (Metro Homes small, Levy medium) over the player's labels — correct. The labs' $5bn fund rightly held at $4bn because its condition failed.

**(b) Levers.** One clear mis-set: `ai_pricing` −0.25. The guide's table is moves from last round; rounds 03–04 scored "new-gen premium (−0.25) + old-gen cut (+0.25)" as *net unchanged*. The same order shape this round should have left the lever at 0.0, not reset it to a "−0.5 margin base". Pessimistic by 0.25 (≈ −0.04 pass-through); minor, correct it. Defensible: `housing_policy` 0.4→0.55 interpolation; `new_business` one notch (a second was arguable). Bill 2 odds ~0.15 generous ("fits" and "cuts against" both stacked, plus +0.05 "worker bill" for a levy); no effect at r=0.98.

**(c) Rolls.** None skipped; pledge and court rolls rightly not triggered.

**(e) Leaks.** No hidden parameters or the 90% frontier. Employers' intel gives the 0.8m demand-channel loss (`d_demand_m`), a breakdown the guide forbids.

**Players.** Distinct in substance, but all five pivoted to housing on the event headline, and in six rounds the corporate players never chose lock-in, layoffs or AI-only building while labour share fell 11 points — cheap pledges, plausible PR. No odds change warranted.

**Fixes for round 07 (course-correct, no rewrite).**
1. Start `ai_pricing` from 0.0; note the correction in `resolution.md`.
2. Apply "fits" or "cuts against", not both; union +0.05 only for genuine worker bills.
3. Drop channel figures from intel.
4. Narrate that Metro Homes' 0.25% of GDP shows as ~0.05% in the model's deficit.
