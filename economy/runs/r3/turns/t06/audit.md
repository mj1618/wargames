# Audit — round 06 (2033–34)

**Verdict: clean on process; one bill-sizing call sits at the optimistic edge and changed the outcome. No rewrite; r07 fixes the rule.**

**(a) Decisions.** None altered, added or dropped. Pact, hiring floor, apprenticeships, $13bn and merger study narrated (no lever). Labs' fund booked (0.014) though they asked a statutory levy lock and got an executive review clause; their public statement was unconditional, so acceptable.

**(b) Levers.** Every change has a named cause; all within two notches. One flag: **Compute Open Access Act classed *small* (0.80).** *Medium* is "a major regulation"; a statutory open-access mandate on the two largest providers plus pre-emption of local moratoria is at least as major as the bargaining bill, classed medium the same round. At medium (0.60) r=0.86 **fails**: `competition_policy` stays 0.4, event 18 bites (`ai_pricing` −0.55), `new_business` loses 0.1. Not clearly wrong ("a rule change" is the small tier's own wording), so history stands. **r07 rule:** a bill moving a lever ≥0.2 of its range, or imposing mandates on named firms, is *medium*.

`union_pressure` 0.1 from the law: off-menu, minimum size, defensible. `household_saving` −0.02 correct (model uses the change in level). Housing push capped: correct.

**(c) Rolls.** Eight logged, odds first, results honoured; election maths checked (0.151→0.15); event 12 drawn, no repeat. Central-bank and state triggers correctly not met.

**(d) Model.** Re-ran `step` from `state-before-2033-34.json` with the t06 levers in a scratch copy: scorecard row and `state.json` identical. No hand edits.

**(e) Leaks.** r07 intel publishes 2034 poverty/homelessness; §5 says one round late (public record correctly gives 2032). Minor, repeated since r05.

**Players.** Collectively cosy: employers hold a 25% layoff share, 35% hours, a pool and now a hiring floor after the unions' fifth straight failure; labs pay $5bn a year unasked. No odds reward given (correct). Red Cell should name the defection each player passed up.
