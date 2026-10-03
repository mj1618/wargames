# Audit — round 06 (2033–34)

**Model integrity.** Re-ran `econ.py step` from `state-before-2033-34.json` with `t06/levers.json`: scorecard row and `state.json` reproduce exactly. No hand edits. Every roll in `resolution.md` is in `log.md` with stated odds; the model result is reported unaltered. Published statistics apply the drawn noise (+0.2 / +1.0) correctly; poverty and homelessness lag one round.

**(a) Decisions.** None altered, added or dropped. Bill sizes were re-classed per the guide (Metro Homes small, Levy medium), overriding the player's labels — correct and consistent with round 02. The labs' $5bn fund was rightly held at $4bn because its condition (the clause) failed.

**(b) Levers.** One clear mis-set: `ai_pricing` −0.25. The guide's table is moves from last round; rounds 03–04 scored "new-gen premium (−0.25) + old-gen cut (+0.25)" as *net unchanged*. The same order shape this round should therefore have left the lever at 0.0, not reset it to a "−0.5 margin base". Pessimistic by 0.25 (≈ −0.04 pass-through). Minor but must be corrected. Judgement calls, defensible: `housing_policy` federal 0.4→0.55 interpolation; `new_business` one notch only (a second was arguable for the blitz plus abandoning AI-only). Bill 2 odds were ~0.15 generous (both "fits" and "cuts against" stacked, plus +0.05 "worker bill" for a levy); no outcome effect at r=0.98.

**(c) Rolls.** None skipped. Pledge and court rolls correctly not triggered.

**(e) Leaks.** None of hidden parameters or the 90% frontier. Employers' intel gives the 0.8m demand-channel loss (`d_demand_m`) — a channel breakdown the guide forbids; 12.8m own cuts is allowed.

**Players.** Not alike in substance, but all five pivoted to housing on the event headline, and the three corporate players have never once chosen lock-in, layoffs or AI-only building in six rounds while labour share fell 11 points — generous-sounding pledges that cost little. Plausible PR, not public spirit; no odds change warranted.

**Fixes for round 07 (course-correct, no rewrite).**
1. Start `ai_pricing` from 0.0; state the correction in `resolution.md`.
2. Apply either the "fits" or "cuts against" adjustment, not both; reserve the union +0.05 for bills whose main content is worker protection or transfers.
3. Drop channel figures (`d_demand`, `c_*`) from intel.
4. Narrate that Metro Homes' 0.25% of GDP is only ~0.05% in the model's deficit.
