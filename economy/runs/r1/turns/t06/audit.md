# Audit — round 06 (2033–34)

**Verification.** Re-ran `econ.py step` from `state-before-2033-34.json` with `t06/levers.json`: scorecard row and `state.json` reproduce exactly — no hand-edits. Every roll in `log.md` matches the resolution; odds arithmetic (drive 0.50, bills 0.90/0.90, court 0.20, election 0.15 clamped) is correct. Published figures follow §5 (layoffs 3.6m = 40% of 9.08m; poverty/homelessness one round late). Nothing hidden leaked.

**(a) Decisions.** None altered. The referee rightly kept the wage-insurance trigger at 5% although federal-gov wrote "stays 4.5%".

**(b) Levers.** All within the guide; three declared judgement calls:
- `ai_pricing` 0.25 leans optimistic: the labs tagged their move "premium/outcome" and made outcome contracts the *standard* tier — a half-notch margin move (to 0.0) is the more literal reading.
- `new_business` 1.07 looks pessimistic (−0.165 while the player went *more* people-heavy), but 0.1 is the event-17 standing bonus expiring and the rest the "conservative launches" wording. Defensible.
- `housing_policy` 0.75: federal 0.55 for partial pre-emption without Housing First is a fair midpoint.

**Most consequential call.** Bill 1's +0.10 "fits coalition" bonus was decisive: at 0.80, r=0.8719 is **PARTIAL** (federal part ~0.475). Setup §6 called growth-first "least inclined to pre-empt" states; precedent (AI pre-emption, three housing bills) supports the bonus. Not a mis-set, but asserted rather than argued.

**(c)–(e).** No skipped rolls. Bill 2 correctly had no court roll (a guarantee, not a rule). Both-support +0.10 on Bill 2 omitted; immaterial.

**Players.** Plausibly self-interested. Labs backing a levy on themselves is cheap signalling ($3bn ≈ 0.01% of GDP) bought with pre-emption.

**Fixes for round 07 (no history rewrite).**
1. Intel to federal-gov: the trigger is 5%.
2. If labs extend premium/outcome pricing, apply −0.25; write the base explicitly.
3. Under worker-first, justify any coalition-fit adjustment in one line before rolling.
4. Note that entrepreneurs' paused +0.10 persists as built capacity.
