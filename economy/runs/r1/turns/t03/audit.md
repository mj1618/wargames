# Audit — round 03 (2029)

**Verdict: clean round; two minor leaks in round-04 intel, one lever read generously.**

**(a) Decisions.** None altered, added or dropped. `orders/ai-firms.md` shows modified against HEAD, but the diff is wording trims only (decisions identical); it was swept into another run's commit (`8de8683`) mid-write. Not a referee edit; don't commit other runs' in-progress files.

**(b) Levers.** Every change has a named cause and matches the guide, including `union_pressure` 0.5 (renewed, so no fade), `competition_policy` 0.3 (within the executive cap) and `housing_policy` 0.6. Two quibbles: (i) `ai_pricing` held at −0.25 although five-year *exclusive* agent-layer bundles are the table's "bundle, lock in" (−0.5), only partly offset by employers extending 5% cuts; net −0.1 to −0.25 was arguable — optimistic direction. (ii) `hours_share` held at 0.15 though employers wrote "rises to 15–20%"; literal-and-smallest is defensible. No correction needed; round 04 should re-read `ai_pricing` if exclusivity deepens.

**(c) Rolls.** Six rolls, odds correct, all respected (both court challenges failed). Central bank correctly inert (entered 2029 at 3.78%); −0.5 queued for 2030.

**(d) Model.** Re-ran `step` from `state-before-2029.json` with `levers.json`: scorecard row and `state.json` identical. Published noise (−0.1 / −0.5) applied correctly.

**(e) Leaks (round-04 intel).** AI firms told their systems "can now do about a quarter of desk work" — an absolute frontier level from which `cog_auto_2032` is inferable; earlier rounds were relative only. Federal told "the central bank signals the economy is running too hot" — S2 is referee-only. Entrepreneurs told the mirage event "is yours". **Fix:** relative capability only; drop the central-bank line; headlines only.

**Players.** Self-interested and differentiated, but cosy: all five sit inside one grand bargain (pledge, First Job, apprenticeships, no tax), and labs/employers creep +0.05 a round rather than exploit a 3.2%-unemployment, growth-first window. Plausible in a boom; watch whether it survives the mirage event and −0.5 demand.
