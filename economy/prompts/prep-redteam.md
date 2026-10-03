# Phase: PREP RED-TEAM (economy series)

Read `economy/prompts/_common.md`, `economy/README.md`, `economy/research/econ-brief.md`, everything in `economy/model/` and `economy/prep/`, and `economy/prompts/`.

Act as two hostile reviewers — a techno-optimist economist and a labour-pessimist economist — plus a wargame designer.
1. Read `econ.py` line by line. Run `selftest`, the Monte Carlo for each policy preset, and your own sweeps. Is either headline answer baked in by structure rather than parameters (e.g. job creation that can never exceed destruction, or always does; homelessness that cannot fall; incomes that cannot fall)? Are parameter ranges faithful to the research brief's range of expert views? Are magnitudes sane against history (e.g. unemployment paths, labour-share moves, growth rates)? Do levers have plausible, not magical, effect sizes? Any accounting bugs (shares not summing, double counting, sign errors)?
2. Check briefs (self-interested enough? leak hidden parameters? decision menus map to levers?), referee guide (clear enough that five different referees would set similar levers for the same orders?), events (effects defined?).
3. Write `economy/prep/redteam.md` (critique + changes made), then FIX the model and files. Re-run selftest and Monte Carlo; update the README's spread and sensitivity tables.
4. Do a dry run: `init` a scratch run under the scratchpad or `/tmp`, step it 7 rounds with default levers, confirm the CLI works end to end and the scorecard looks sane. Delete the scratch run.
Final message: ≤3 lines incl. the Monte Carlo 10/50/90 percentiles for 2036 unemployment and median income under default levers.
