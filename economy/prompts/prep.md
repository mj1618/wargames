# Phase: PREP (economy series) — build the model and the scenario

Read `economy/prompts/_common.md`, `economy/README.md`, all of `economy/prompts/` (so what you build fits how it will be used), `economy/research/econ-brief.md` (the evidence base — your parameter ranges must come from it), `research/world-baseline.md`, `world/cast.md`, `methodology/guardrails.md`, `tools/roll.py`.

## A. The economic model — `economy/model/`
Write `econ.py` (Python 3 stdlib only) and `README.md`.

**State (one row per round, written to `scorecard.csv`)** — at least: period label/end date; AI capability index and robotics capability index; share of cognitive tasks and physical tasks automatable and share actually automated; employment (millions) and by broad sector (≥6 sectors incl. care/health, construction/trades, logistics/transport, office/professional, retail/hospitality, manufacturing, new-economy/other); jobs destroyed and jobs created this period (gross) and cumulative; unemployment rate; labour-force participation; average weekly hours; median real household income index (2026=100); bottom-fifth real income index; top-1% income share; labour share of income; real GDP index; price indices for goods, digital/professional services, health care, housing; poverty rate; homelessness per 10,000; federal revenue, spending, deficit as % of GDP; transfer generosity; a public-trust/unrest index.
Start values: calibrated to late 2026 from the research brief/baseline (cite them in README).

**Hidden parameters sampled per run from documented ranges** (`sample_params(seed)`): the 6–10 uncertain parameters the research brief identifies — e.g. demand response to cheaper goods/services (the Jevons strength), rate at which new kinds of human work appear, robotics arrival speed, adoption friction, how much of the cost saving is passed to consumers vs kept as profit (market concentration), housing-supply responsiveness, political starting configuration, macro fragility. The ranges must span genuine expert disagreement — the model must be able to produce good and bad outcomes on both questions. Record evidence for low/high ends in README.

**Levers set by the referee each round from players' decisions** (documented ranges and defaults): e.g. deployment pace by AI firms; price pass-through; employer adoption speed and layoff-vs-attrition/hours choice; wage sharing; new business formation; transfer generosity / basic income; taxes on capital / AI profits; retraining and public employment; working-time policy; deployment regulation; competition policy; housing supply policy; union/worker pressure; household saving vs spending.

**`step(state, params, levers, rng)`** — transparent accounting, not a black box: displacement from automation by sector; job creation from demand expansion (income and price effects), from new task creation and new firms; wages/hours; incomes by group (labour vs capital vs transfers); prices by category; housing and homelessness (driven mainly by housing cost relative to low incomes, per the evidence); public finances (payroll/income-tax dependence); feedbacks (unemployment → demand; unrest → politics). Small random noise per round via `rng`. Round lengths vary (1 or 2 years) — step takes `years`.

**CLI**
- `python3 economy/model/econ.py init --run <RUN> --seed <N>` → writes `<RUN>/state/params.json` (hidden), `state.json`, `scorecard.csv` (2026 baseline row), and prints the sampled conditions in plain words.
- `python3 economy/model/econ.py step --run <RUN> --levers <file.json> --years <1|2> --label <period>` → advances, appends scorecard row, prints key numbers. Validates lever names/ranges.
- `python3 economy/model/econ.py montecarlo --n 1000 --policy <default|laissez|active> --out economy/model/montecarlo.csv` → dice-only runs with fixed lever presets; one row per run with the sampled parameters and final/peak outcomes.
- `python3 economy/model/econ.py selftest` → sanity checks (baseline reproduces start values; bounds hold; shares sum; no NaNs; monotone sanity e.g. higher demand response → more job creation).
Run selftest and a montecarlo and fix problems. In README report the spread of Monte Carlo outcomes (unemployment and median income in 2036: 10th/50th/90th percentile) for each policy preset, and a sensitivity table (which parameters and levers move the two headline answers most).

## B. Scenario files — `economy/prep/`
- `world-state.md`: the starting situation (Jan 2027) in plain words with the baseline numbers.
- `clock.md`: 7 rounds — 2027, 2028, 2029, 2030, 2031–32, 2033–34, 2035–36. Players are not told the end.
- `actors/<id>.md` — 5 players, each ≤450 words: `federal-gov` (President + Congress as one seat with internal factions; laws need a roll), `ai-firms` (frontier labs + robot makers), `employers` (large established companies and their investors), `households` (workers, unions, voters, consumers), `entrepreneurs` (new and small businesses). Each: who you are, what you actually want (self-interested, concrete), what you control (a decision menu mapped to levers, with sizes), what you can see, constraints, how you decide. Set `Played by model:` — mix opus/sonnet/fable/haiku, no model more than twice.
- `referee-guide.md`: how to turn decisions into levers (a mapping table), standing odds for common uncertain things (laws passing under each political configuration, strikes, court blocks), how non-players behave (the central bank, states/cities incl. housing and homelessness policy, courts, voters/elections in 2028/2030/2032/2034/2036, rest of world), how official statistics are lagged/noisy, anti-bias rules (no moderation to the mean, no rescue of bad outcomes, no punishment of good ones).
- `events.md`: a numbered deck of ≥20 random events, each with a defined model effect (good, bad and boring: breakthroughs, robot recalls, financial wobble, energy crunch, a hit new industry, a state pilot that works, a court ruling, a strike wave, a housing-construction breakthrough…).
- `setup-spec.md`: what `init` samples, plus any non-model setup rolls (e.g. which party holds what).

Fairness test before you finish: could a reasonable optimist and a reasonable pessimist both look at the parameter ranges and say "my view is represented"? If not, widen. Final message: one line.
