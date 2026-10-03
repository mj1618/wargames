# Audit — round 03 (2029)

**Verdict: clean round. No correction required.**

**(a) Decisions.** None altered, added or dropped. Labs' $2bn fund booked at 0.01; employers' 0.4m cohort, entrepreneurs' licensing campaign and households' rallies narrated (no lever fits).

**(b) Levers.** Every change has a named cause, within two notches. Two calls sit at the optimistic edge but are defensible:
- `ai_pricing` +0.5 for a developer tier open only to firms under $100m while the enterprise premium holds. "Vague → smallest size" and last round's +0.25 for the capped tier argue for +0.25 (lever −0.5). Effect ~0.04 on pass-through; not worth rewriting. Going forward: a segment-limited cut is half a notch; a full notch needs enterprise cuts or a rival matching.
- Worker Security Act classed *medium* (0.70). A 1%-of-GDP targeted cash programme is arguably a "new entitlement" → *large* (0.50). Moot (r=0.99 fails either way), but r04 must settle the rule before the sponsors return.
- `new_business` +0.05 for a 60/40 push: between proportional (+0.02) and "doubled push" (+0.1); consistent with t02.

**(c) Rolls.** All six logged, odds stated first, results honoured. Court roll run blind. Central-bank threshold met (0.70).

**(d) Model.** Re-ran `step` from `state-before-2029.json` with the t03 levers: scorecard row and `state.json` byte-identical. No hand edits.

**(e) Leaks.** None. "0.7m hired" and "rehired about 4m" are own-hiring figures (allowed). AI-layoff figure uses the 40% rule.

**Players.** Individually plausible, collectively cosy: labs restart the fund "no conditions" and volunteer a levy; employers add 1.5% payroll and a cohort; entrepreneurs go 60% people-heavy; households decline to strike at peak leverage. Two rounds without a defector; referee gave no odds reward (correct). If it persists, red-cell should name the moves passed up.

**r04 to-do.** Pledge rolls (0.60) only if profits are under pressure. Apply `shock_new_task` 1.5, `public_jobs_m` 1.0, reset `shock_demand_pct`.
