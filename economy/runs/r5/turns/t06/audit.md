# Audit — round 06 (2033–34)

**(a) Decisions.** None changed, added or dropped; package, contract and term sheet read literally. Hygiene: `orders/ai-firms.md` was committed early and later edited (wording trims; one trigger, "or licensing", dropped). Decisions identical, but freeze orders before resolving.

**(b) Levers.**
- `retraining_pct_gdp` **0.225 is mis-set; should be 0.25.** Fair Share retraining was 0.3, half-size 0.15, not the 0.1 used: 0.1 + (0.15 + 0.15)/2 = 0.25. Pessimistic by 0.025. The slip is carried into `t07/intel/_clock.md` (0.275); **round 07 must set 0.325** (0.1 + 0.15 + 0.075) and note the correction.
- `new_business` 1.3 leans optimistic. Round 05 netted a 30% AI-only slice at −0.1; this round's 25% slice got nothing, and the Renewal's standing +0.1 was counted in full although the law runs 2034 only (its retraining was halved). A consistent reading gives 1.2–1.25 (≈0.1–0.2m fewer new-work jobs). Not clearly wrong; pick one rule for part-round laws and apply it in round 07 (Renewal covers 2035 only).
- `ai_pricing` 0 defensible: the three-year lock-in never signed; employers' −0.25 persists; net ≈ 0.
- Odds arithmetic checks (0.70, 0.90, 0.20, 0.22, 0.50); 2034-only laws halved, correctly unwound for round 07.

**(c) Rolls.** Every uncertain item rolled, odds stated first, results honoured. No pledge roll due.

**(d) Model.** Re-ran `step` from `state-before-2033-34.json` on a copy: scorecard row and `state.json` identical. Published statistics match the noise draw (3.8%, 111.9).

**(e) Leaks.** None in round 07 intel: no hidden parameters, channels or round count.

**Players.** Distinct and self-interested. Mild public spirit: employers self-fund shorter weeks for 8% of staff unpressured. Six rounds without a strike or boycott is very cooperative; the referee has not rewarded it.

**Fixes.** (1) Round 07 `retraining_pct_gdp` 0.325, noted in resolution. (2) One stated rule for part-round laws' standing adjustments. (3) Commit orders before resolving.
