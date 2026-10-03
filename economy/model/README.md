# The economic model (`econ.py`)

A small, deliberately plain accounting model of the US economy from late 2026 to end 2036. It is not a forecast. It keeps the books consistent while players and dice decide what happens, and it makes every assumption visible so the write-up can say which assumption drove which result.

**Premise, not tested:** AI and robotics keep improving rapidly. The two capability parameters are therefore held to the rapid end of the evidence. The wide, genuinely uncertain ranges are on how the *economy* responds.

**Evidence base:** `economy/research/econ-brief.md` (cited below as "brief A" … "brief H"). Anything not in the brief is marked **[assumption]** and is a fair target for the red-team.

## How the referee uses it

```
python3 economy/model/econ.py init --run <RUN> --seed <N>
python3 economy/model/econ.py step --run <RUN> --levers <RUN>/turns/tNN/levers.json --years <1|2> --label <period>
python3 economy/model/econ.py levers            # list every lever, range and default
python3 economy/model/econ.py montecarlo --n 1000 --policy <default|laissez|active> --out economy/model/montecarlo.csv
python3 economy/model/econ.py sensitivity --n 1000
python3 economy/model/econ.py selftest
```

- `init` writes `<RUN>/state/params.json` (hidden conditions — referee only), `state.json`, `scorecard.csv` with the 2026 baseline row, and prints the hidden conditions in plain words.
- `step` reads a JSON file of lever values, advances 1 or 2 years, appends one scorecard row and prints the key numbers. Labels and years per round are in `economy/prep/clock.md`. It refuses unknown lever names, out-of-range values and repeating a period. It saves `state-before-<label>.json` first, so a mistaken step can be undone by copying that file back over `state.json` and deleting the last scorecard line.
- **Lever file rules.** Policy and behaviour levers ("level" levers) persist: leave one out and it stays where it was last round (the step prints what was carried). Event levers (`shock_*`) apply to one round only and reset when left out. `{}` is a valid file.
- Never hand-edit `scorecard.csv` or `state.json`.

## Start values (late 2026)

| Quantity | Value | Source |
|---|---|---|
| Unemployment rate | 4.1% | brief C (Aug 2026) |
| Participation / employment-to-population | 61.6% / 59.1% | brief C |
| Employment | 162.4m (59.1% of 274.8m adults) | derived from the two rates; **[assumption]** on adult population |
| Employment by sector | office and professional 48.0m; health, care and education 38.0m; retail and hospitality 34.0m; construction and trades 14.0m; manufacturing 12.8m; logistics and transport 11.0m; new-economy and other 4.6m | **[assumption]** rounded from BLS industry proportions; not in brief |
| Labour share of income | 52.8% | brief C/E (Q2 2026 record low) |
| Corporate profits | 14.9% of GDP | brief C |
| Share of desk-work pay machines could do / actually do | 6% / 1.5% | brief C: AI assists 6.3% of work hours, saves 1.4% |
| Share of physical work machines could do / actually do | 3% / 1% | **[assumption]** from brief D (productive humanoid labour "tens of FTEs"; warehouses the exception) |
| Average weekly hours | 34.3 | **[assumption]** (BLS private nonfarm); not in brief |
| Poverty rate (supplemental measure) | 12.9% | brief F |
| Homelessness | 22 per 10,000 people | brief F: 745,652 on a night in 2025, about 340m residents |
| Top-1% income share | 20% | **[assumption]**; not in brief |
| Federal revenue / spending / deficit / debt | 17.3 / 23.3 / 6.0 / 100% of GDP | **[assumption]** round CBO-style numbers; labour-based share of revenue (70%) is brief G |
| Median and bottom-fifth real income, GDP, prices | index 100 | by construction |
| Unrest index | 35 of 100 | **[assumption]**; a relative gauge only |

**The no-AI benchmark.** If automation simply stopped at its 2026 level, the model gives unemployment 4.1%, labour share 52.8% and median real household income of about 109 in 2036 (pay grows 1% a year on its old trend; existing benefits only hold their value). "Better off" should be judged against both 100 (2026) and about 109 (the old trend).

## Hidden parameters (sampled once per run by `sample_params(seed)`)

Eleven numbers. The first two are the technology premise and are constrained to the rapid end by the orchestrator's ruling. The other nine carry the real disagreement.

| # | Parameter | Range (distribution) | What it means | Evidence for the low end | Evidence for the high end |
|---|---|---|---|---|---|
| 1 | `cog_auto_2032` | 0.25–0.60 (uniform) | Share of desk-work pay machines could profitably do by 2032. The frontier rises in a straight line from 6% in 2026 through this value and on (cap 90%). | Brief H1 full range is 5–60%; the premise rules out the sceptic end (Acemoglu 4.6%, Humlum nulls). 25% is "rapid but bottlenecked". | 77% automation-pattern enterprise use; entry-level gap widening 13%→19% in a year; time horizons growing ~10× a year (brief C, H1) |
| 2 | `robot_lag_years` | 2–8 (uniform) | Years by which general physical manipulation trails desk-work AI. | $16k humanoids shipping in thousands; Amazon plan to automate 75% of operations (brief D) | ~30 FTE-years of commercial humanoid work to date; 15 years from AV demos to <1% of trips. Brief H2 allows 15+; the premise caps it at 8. |
| 3 | `jevons` | 0.3–2.0 (uniform) | How strongly a price fall raises the quantity bought (price elasticity before saturation; multiplied by a sector factor and decaying as prices fall). | Bessen post-saturation; translators; bank tellers after 2010 (brief A, H3) | Radiology; senior-software rebound; early textiles (brief A, H3) |
| 4 | `new_task_rate` | 0.2–1.2 (uniform) | New kinds of human jobs appearing per job automated away, arriving with about a two-year lag. | Reinstatement slowed after 1987; AI can do the new tasks too (brief B, H4) | 60% of 2018 jobs were in titles that did not exist in 1940; WEF net +78m (brief B, C, H4) |
| 5 | `diffusion_t50` | 3–20 years (log-uniform) | Years for firms to close half the gap between what machines can do and what they are used for. | AI share of layoff announcements 7%→40% within 2026; entrant firms (brief C, H5) | Only 17–20% of firms use AI; electrification took ~30 years (brief C, H5) |
| 6 | `passthrough` | 0.2–0.9 (uniform) | Share of cost savings that reaches customers as lower prices; the rest is kept as profit. | Record margins; superstar concentration; a handful of frontier labs (brief E, H6) | Fast-falling token prices; open-weight competition (brief H6) |
| 7 | `wage_share` | −0.2–0.7 (uniform) | Share of AI productivity gains per worker that reaches pay, on top of a 1%-a-year old trend. Negative means pay falls behind even its old trend. Drives the labour-share path (brief H7: 30–55% in 2035; the model's 1,000-run range is 30–53%). | Engels' pause: wages got about a quarter of productivity growth for 40 years; labour share fell a full point in the past year (brief E, C) | Baumol bottlenecks keep humans essential; mean wages up in mainstream forecasts (brief B, H) |
| 8 | `housing_supply` | 0–1 (uniform) | How freely housing can be built. 0 → real housing costs rise about 2% a year; 1 → fall about 3.5% a year as construction automates (brief H8: +20% to −30% by 2035). | Zoning and land capitalisation; construction productivity down 40% in 50 years (brief F) | Prefab and robotic microfactories plus state pre-emption of zoning; metros that build have lower rents (brief F) |
| 9 | `demand_mult` | 0.5–1.5 (uniform) | Spending lost per dollar of wages lost (total, after all knock-ons). | Data-centre investment boom offsets (brief H10) | Top 10% own 87% of equities and spend less of each dollar; state balanced-budget cuts amplify (brief E, G, H10) |
| 10 | `policy_lag_years` | 1–10 (log-uniform) | Years between visible job losses and a major federal response. Sets the starting political configuration (under 2.5 responsive; 2.5–5.5 divided; over 5.5 gridlocked) used by the referee's odds table, and the reaction lag in dice-only runs. | CARES Act passed in weeks (brief H9) | Child Tax Credit lapsed in 2022; China shock got no real response for 15 years (brief H9) |
| 11 | `policy_scale_pct` | 0–10% of GDP (triangular, mode 3) | Size of that response. Used only in dice-only runs (in played games the players decide). | brief H9 | brief G: a $12k basic income costs about 10% of GDP |

Parameters are drawn independently **[assumption]**; real-world correlations (for example fast adoption going with low pass-through) are not modelled.

## Levers the referee sets each round

`python3 economy/model/econ.py levers` prints this table from the code. The mapping from player decisions to lever values is in `economy/prep/referee-guide.md`.

| Lever | Range | Default | Set from | Effect in the model |
|---|---|---|---|---|
| `deploy_pace` | 0.7–1.3 | 1.0 | AI firms | Multiplies the yearly rise in what machines can do |
| `ai_pricing` | −1–1 | 0 | AI firms | ±0.15 on pass-through |
| `adoption_speed` | 0.5–1.6 | 1.0 | Employers | Multiplies the adoption rate |
| `layoff_share` | 0.2–0.9 | 0.6 | Employers | Share of removed jobs that become unemployed; the rest leave (or never join) the labour force |
| `hours_share` | 0–0.5 | 0.1 | Employers | Share of labour saving taken as shorter hours, not fewer jobs; weekly pay falls with hours |
| `wage_sharing` | −0.1–0.3 | 0 | Employers | Added to `wage_share` |
| `new_business` | 0.75–1.3 | 1.0 | Entrepreneurs | Multiplies new-work creation |
| `union_pressure` | 0–1 | 0 | Households | Up to +0.15 on `wage_share`, up to −15% on adoption |
| `household_saving` | −0.03–0.05 | 0 | Households | Change in saving rate; each point cuts spending by 0.7% of GDP once |
| `transfers_pct_gdp` | 0–10 | 0 | Federal | New cash transfers, % of GDP a year |
| `transfer_target` | 0–1 | 0 | Federal | 0 universal; 1 aimed at the bottom two-fifths |
| `capital_tax_pct` | 0–30 | 0 | Federal | Extra tax on profits; collects 60% of rate × profit base; slows adoption 0.5% per point |
| `retraining_pct_gdp` | 0–1 | 0 | Federal | Up to +10% on new-work creation and −30% on people giving up, reached at 0.5% of GDP |
| `public_jobs_m` | 0–8 | 0 | Federal | Public jobs, millions (half in care, 30% building, 20% office) at 70% of average pay |
| `worktime_cut_pct` | 0–15 | 0 | Federal | Legislated cut in the working week; 0.2 jobs per unit of hours; half of lost pay made up in hourly rates |
| `deploy_regulation` | 0–1 | 0 | Federal | Up to −50% on adoption |
| `competition_policy` | 0–1 | 0 | Federal | Up to +0.15 on pass-through |
| `housing_policy` | 0–1 | 0 | Federal + states | Up to +0.4 on `housing_supply`; up to −20% on homelessness directly; costs up to 0.3% of GDP |
| `shock_frontier_cog` | −0.05–0.05 | 0 | Events | One-off jump in what machines can do |
| `shock_robot_lag_years` | −2–2 | 0 | Events | Robots sooner (negative) or later |
| `shock_adoption` | 0.6–1.4 | 1 | Events | Multiplies adoption this round |
| `shock_demand_pct` | −4–2 | 0 | Events | Outside swing in spending, % of GDP, this round (reverses when the lever resets) |
| `shock_housing_pct` | −5–5 | 0 | Events | One-off change in real housing costs |
| `shock_new_task` | 0.6–1.6 | 1 | Events | Multiplies new-work creation this round |

## What `step` does each year (in order; a 2-year round runs this twice)

All job numbers are millions. Section numbers match the comments in `step_year`.

0. **Population.** Adults grow 0.4% a year; every stock scales, so the employment rate is unchanged. These jobs are reported separately (`jobs_from_population_growth_m`) and are **not** counted as "created".
1. **What machines can do.** Desk-work frontier rises by `(cog_auto_2032 − 0.06)/6 × deploy_pace` a year. The physical frontier is the desk-work frontier `robot_lag_years` earlier (starting from 3%).
2. **What firms actually automate.** Each year firms close a fraction `1 − exp(−ln2/diffusion_t50 × levers)` of the gap between "can" and "does"; robots at 0.8 of that speed.
3. **By sector:** the share of the sector's work now done by machines is `cognitive share × ease × automated desk share + physical share × ease × automated physical share`.
   - **Jobs destroyed (automation)** = employment × rise in that share ÷ (1 − old share), less the part taken as shorter hours.
   - **Unit cost** falls by labour cost share × that fraction × 0.6. **Price** falls by `passthrough` × that (half as much in health and care).
   - **Jobs created (own demand)** = remaining employment × elasticity × price fall, where elasticity = `jevons` × sector factor × `exp(−cumulative price fall)`. This is the sector-level Jevons effect: with full pass-through, labour as the only cost and free machines, a sector's employment rises exactly when elasticity exceeds 1 (brief A).
   - **Spending shift.** If elasticity is below 1, customers have money left over: 30% is spent in other sectors (mostly labour-heavy services) and creates jobs there; 70% makes no jobs directly — it goes to saving, land and dearer supply-restricted services — except that half of it becomes building work to the extent housing supply allows, and the rest pushes rents up. If elasticity is above 1, 30% of the extra spending is pulled from other sectors (destroying jobs there) and 70% is new demand.
4. **New kinds of work** = `new_task_rate` × smoothed recent automation job losses × `new_business` × retraining bonus × erosion, where erosion = `((1 − frontier)/(1 − 0.06))^0.2` (new tasks get somewhat scarcer as machines can do more).
5. **Slow re-absorption.** 8% a year of slack (unemployed above 4.1% plus people who gave up), scaled by the share of desk work machines cannot yet do, finds lower-paid work in retail, care, building and new sectors.
6. **Direct policy jobs.** Changes in `public_jobs_m` and `worktime_cut_pct`.
7. **Spending feedback.** Lost wages = pay lost with this year's net job loss so far, plus any shortfall of pay rates against their old trend (when `wage_share` is negative). If positive, spending falls by `demand_mult` × 75% of it (25% is replaced by unemployment insurance), destroying jobs in proportion, most in retail, building and manufacturing. Gains are not converted to extra jobs. New federal spending adds 0.9 per dollar, new capital-tax revenue subtracts 0.3 per dollar, and event shocks and saving changes add directly; extra spending only creates jobs while there is slack to hire.
8. **People.** Destroyed jobs go to unemployment (`layoff_share`) or out of the labour force. Created jobs are filled from the unemployed (down to a 3% floor), people who had given up, and a reserve of 3% of adults who would work if jobs appeared; if all three run dry the surplus is reported as `c_unfilled_m`. Each year 20% of unemployment above 4.1% gives up looking. New transfers let 0.2% of adults per 1% of GDP stop working.
9. **Pay and output.** Hourly pay grows 1% (old trend) + `wage_share` × AI productivity growth per worker, then is scaled down 2.1% for each point the employment rate sits below 59.1% (capped). Output per worker rises 1% a year plus the automation gain. GDP = Σ employment × output per worker. Labour share = pay bill ÷ GDP. Sector prices also drift with pay: labour-heavy sectors get relatively dearer when pay beats trend (Baumol).
10. **Housing.** Real housing cost changes by `(1 − supply) × 2% − supply × 3.5% × construction-automation factor (0.6–1.4) + rent push from leaked spending + 0.3 × pay growth above trend`, plus events.

**Derived each round (`indicators`)**
- Median household income = 78% pay (wage × hours × employment rate) + 15% existing benefits (fixed real value) + 7% capital income + its share of new transfers, divided by its cost of living (33% housing, 30% goods, 15% health, 10% digital and professional services, 12% other services).
- Bottom fifth = 45% pay (twice as sensitive to the employment rate), 50% benefits, 5% capital, plus new transfers (20% of a universal programme, up to 50% of a targeted one), with a 42%-housing basket.
- Poverty = 12.9% × (bottom-fifth real income ÷ 100)^−2.
- Homelessness = 22 × (housing cost ÷ bottom-fifth money income), steeper once that ratio passes 1.1, × (1 − 0.2 × `housing_policy`). Housing cost relative to low incomes is the only driver (brief F).
- Top-1% share = 8% of labour income + 33.5% of 2026-level capital income + 50% of capital income above that, after the new tax and transfers.
- Federal revenue = 12.1% × (labour share ÷ 52.8%) + 5.2% × (capital share ÷ 47.2%) + new capital tax. Spending = 23.3% × (trend GDP ÷ actual GDP)^0.5 + unemployment insurance + new programmes.
- Unrest moves halfway each round toward 35 + 4 × (unemployment − 4.1) + 2 × points of employment rate lost + 0.5 per point median income is below 100 (−0.3 per point above) + 1 per point of top-1% share above 20 + 0.3 × (homelessness − 22) − 2 × new transfers (% of GDP). It feeds politics through the referee's odds, not through the model.
- Random noise each year: ±5% on adoption, ±8% on new work, ±10% on spending losses, ±0.5% on housing costs.

## Fixed constants and where they come from

| Constant | Value | Source |
|---|---|---|
| Machine does a task for 40% of the wage (`COST_SAVING` 0.6) | 0.6 | **[assumption]** between the sceptic's 27% saving (brief B) and near-free tokens; held fixed because the premise is rapid progress |
| Demand response decays with price falls (`SATURATION` 1.0) | halves per 50% price fall | brief A (Bessen's inverted U); size **[assumption]** |
| Sector factors on elasticity | office 1.0, care 1.1, retail 0.7, manufacturing 0.6, logistics 0.8, construction 1.2, new 1.3 | **[assumption]** informed by brief A (goods saturate; unmet need in care, housing, software) |
| Share of unspent savings that makes no jobs (`LEAK` 0.7) | 0.7 | **[assumption]** from brief E: as goods got cheap, spending moved to housing, health and education where prices rose, not quantities |
| Sector ease of automation | care 0.2 physical / 0.6 desk; construction 0.35; retail 0.6; logistics 0.9; manufacturing 1.0 | brief D timeline table (care assistive not substitutive; trades last); sizes **[assumption]** |
| Robots roll out at 0.8 of software speed | 0.8 | **[assumption]** (hardware must be built; brief D) |
| New-work lag (`NEW_TASK_SMOOTH` 0.5) | about 2 years | **[assumption]** |
| Erosion of new work (`EROSION_EXP` 0.2) | see step 4 | **[assumption]** standing in for Korinek & Suh (brief B): with 0 the model ignores it, with 1 new work vanishes in step with capability. The red-team should test both. |
| Slack re-absorbed 8% a year | 0.08 | brief E: local adjustment takes 10–20 years |
| Wage loss per point of employment rate | 2.1% | brief B: Acemoglu & Restrepo, −0.2pp employment and −0.42% wages per robot per thousand workers |
| Unemployed giving up, 20% a year | 0.20 | **[assumption]**; brief C/H say displacement shows up as lower participation |
| Unemployment insurance replaces 25% of lost wages | 0.25 | brief G (40% for 26 weeks, incomplete coverage) |
| Transfers reduce work: 0.2% of adults per 1% of GDP | 0.002 | brief G: OpenResearch, −2pp employment at about $12k a year (≈10% of GDP) |
| Shorter legal week: 0.2 jobs per unit of hours | 0.2 | brief G: France's 35-hour law showed no clear employment gain |
| Capital tax collects 60%; slows adoption 0.5% a point | 0.6; 0.005 | brief G (mobile, concentrated base; optimal robot tax is small); sizes **[assumption]** |
| Top 1% get half of new capital income | 0.50 | brief E: top 1% hold 50.2% of equities |
| Homelessness moves one-for-one with housing cost ÷ low incomes | elasticity 1, steeper past 1.1 | brief F: $100 rent rise ≈ +9%; inflection at 32% of income |
| Poverty elasticity to bottom-fifth income | 2.0 | **[assumption]** loosely from the 2021 Child Tax Credit episode (brief F) |
| Federal spending falls half as fast as GDP grows above trend | exponent 0.5 | **[assumption]** |
| Pay and productivity trend; adult population growth | 1.0%; 0.4% a year | **[assumption]** (brief H official baselines ≈1.8–2% growth) |
| Income mixes, baskets, sector cost shares, relative pay | see code | **[assumption]**; brief E gives ≥40% housing for low-income households |

## What 1,000 dice-only runs produce

No players: lever presets fixed, hidden parameters and noise random. `montecarlo.csv` (default), `montecarlo-laissez.csv`, `montecarlo-active.csv` have one row per run.

- **default** — nobody changes behaviour; Washington reacts only after visible damage (unemployment ≥6%, employment rate down 1.5 points, or unrest ≥55), after this run's lag, at this run's scale, half-targeted and part-funded by a capital tax.
- **laissez** — no new policy; AI firms and employers push faster (pace 1.1, adoption 1.15, 70% layoffs).
- **active** — from 2027: transfers 3% of GDP half-targeted, 10-point capital tax, retraining 0.4%, housing policy 0.7, competition policy 0.6, 30% of labour saving taken as shorter hours, new-business 1.2, public jobs up to 3m scaled to slack.

| 2036 outcome | default p10 / p50 / p90 | laissez p10 / p50 / p90 | active p10 / p50 / p90 |
|---|---|---|---|
| **Unemployment rate, %** | **4.1 / 4.8 / 6.2** | **4.3 / 5.4 / 7.8** | **3.3 / 4.3 / 5.3** |
| Participation rate, % (2026: 61.6) | 58.7 / 60.8 / 62.1 | 58.0 / 60.8 / 62.2 | 60.4 / 61.5 / 62.9 |
| Employment-to-population, % (2026: 59.1) | 55.2 / 57.9 / 59.6 | 53.5 / 57.5 / 59.5 | 57.3 / 58.8 / 60.8 |
| Jobs destroyed 2027–36, m | 9 / 18 / 34 | 11 / 22 / 41 | 7 / 14 / 26 |
| Jobs created 2027–36, m | 6 / 14 / 28 | 8 / 16 / 32 | 7 / 15 / 29 |
| Jobs created per job destroyed | 0.52 / 0.79 / 1.09 | 0.47 / 0.76 / 1.07 | 0.77 / 1.08 / 1.43 |
| **Median real household income (2026 = 100)** | **101 / 111 / 121** | **98 / 109 / 121** | **112 / 121 / 133** |
| Bottom-fifth real income | 97 / 107 / 120 | 95 / 105 / 116 | 135 / 147 / 160 |
| Top-1% income share, % (2026: 20) | 21.1 / 22.6 / 25.0 | 21.4 / 23.3 / 26.5 | 20.0 / 21.1 / 23.1 |
| Labour share, % (2026: 52.8) | 40 / 47 / 50 | 37 / 45 / 50 | 43 / 48 / 51 |
| Real GDP (2026 = 100) | 120 / 127 / 140 | 121 / 128 / 144 | 120 / 126 / 139 |
| Poverty rate, % (2026: 12.9) | 8.9 / 11.3 / 13.6 | 9.6 / 11.7 / 14.4 | 5.0 / 6.0 / 7.1 |
| Homeless per 10,000 (2026: 22) | 17 / 21 / 25 | 18 / 21 / 26 | 11 / 12 / 15 |
| Federal deficit, % of GDP (2026: 6.0) | 4.9 / 5.8 / 7.0 | 4.7 / 5.8 / 6.9 | 7.1 / 8.1 / 8.7 |

| Headline question | default | laissez | active |
|---|---|---|---|
| More jobs created than destroyed | 20% of runs | 17% | 62% |
| Employment rate in 2036 within half a point of 2026, or higher | 31% | 27% | 58% |
| Median income above the no-AI trend (109) | 56% | 50% | 97% |
| Median income below its 2026 level | 7% | 15% | 0% |
| Bottom fifth worse off than 2026 | 19% | 28% | 0% |
| Homelessness higher than 2026 | 35% | 40% | 0% |

Extremes across the 3,000 runs: unemployment 2.9–12.7%; employment rate 45.6–62.7%; median income 73–152; labour share 26–53%; GDP 115–179.

**Fairness check.** An optimist's view is represented: with strong demand response, plentiful new work, high pass-through and free building, more jobs are created than destroyed, the employment rate rises above 2026, median income reaches about 139 and homelessness falls by 30% (see `selftest`, "optimist's world"). A pessimist's view is represented: with the opposite draws and fast adoption, a quarter as many jobs are created as destroyed, the employment rate falls 12 points, unemployment reaches 10%, median income falls to about 72 and homelessness rises by two-thirds ("pessimist's world"). The frontier-lab "10–20% unemployment" view sits in the far tail, because in this model (as in the brief) most displacement shows up as people leaving the labour force — read the employment rate, not only the unemployment rate. The sceptic's "almost nothing changes" view is excluded by the premise.

## What moves the two headline answers (sensitivity)

**A. Hidden parameters — rank correlation with 2036 outcomes (1,000 default runs)**

| Parameter | Employment rate | Unemployment | Created per destroyed | Median income | Bottom-fifth income | Homelessness |
|---|---|---|---|---|---|---|
| `new_task_rate` | +0.76 | −0.66 | +0.83 | +0.45 | +0.19 | −0.02 |
| `cog_auto_2032` | −0.37 | +0.43 | −0.20 | −0.02 | +0.02 | −0.03 |
| `passthrough` | +0.26 | −0.24 | +0.28 | +0.16 | +0.07 | +0.04 |
| `diffusion_t50` | +0.25 | −0.25 | −0.08 | −0.14 | −0.20 | +0.11 |
| `jevons` | +0.16 | −0.14 | +0.20 | +0.15 | +0.10 | −0.07 |
| `wage_share` | +0.12 | −0.11 | +0.10 | +0.35 | +0.11 | +0.03 |
| `housing_supply` | +0.03 | −0.03 | +0.03 | +0.62 | +0.67 | −0.84 |
| `robot_lag_years` | +0.06 | −0.06 | +0.00 | +0.00 | −0.03 | +0.02 |
| `demand_mult` | −0.01 | +0.01 | +0.01 | −0.03 | −0.03 | +0.03 |
| `policy_lag_years` | −0.02 | +0.07 | −0.06 | −0.08 | −0.15 | +0.11 |
| `policy_scale_pct` | −0.06 | +0.04 | −0.01 | +0.00 | +0.01 | −0.04 |

**B. One parameter at a time, low end → high end (others mid-range, default levers, no noise)**

| Parameter | Employment rate | Unemployment | Created per destroyed | Median income | Bottom fifth | Homelessness |
|---|---|---|---|---|---|---|
| `new_task_rate` 0.2→1.2 | 55.1 → 60.0 | 6.2 → 3.9 | 0.4 → 1.1 | 102 → 118 | 99 → 112 | 22.0 → 20.0 |
| `cog_auto_2032` 0.25→0.6 | 58.6 → 56.4 | 4.5 → 5.8 | 0.9 → 0.7 | 111 → 108 | 107 → 104 | 20.7 → 21.3 |
| `diffusion_t50` 3→20 | 56.7 → 58.5 | 5.6 → 4.5 | 0.8 → 0.8 | 112 → 110 | 107 → 106 | 20.9 → 20.8 |
| `passthrough` 0.2→0.9 | 56.8 → 58.6 | 5.4 → 4.6 | 0.7 → 0.9 | 107 → 114 | 103 → 109 | 21.2 → 20.6 |
| `jevons` 0.3→2.0 | 57.3 → 58.4 | 5.2 → 4.7 | 0.7 → 0.9 | 108 → 112 | 104 → 108 | 21.5 → 20.6 |
| `wage_share` −0.2→0.7 | 56.9 → 57.8 | 5.4 → 5.0 | 0.7 → 0.8 | 104 → 115 | 102 → 108 | 21.3 → 20.7 |
| `housing_supply` 0→1 | 57.8 → 57.8 | 5.0 → 5.0 | 0.8 → 0.8 | 103 → 119 | 97 → 116 | 26.8 → 16.8 |
| `robot_lag_years` 2→8 | 57.6 → 58.0 | 5.0 → 4.9 | 0.8 → 0.8 | 111 → 110 | 106 → 106 | 20.9 → 20.8 |
| `demand_mult` 0.5→1.5 | 57.8 → 57.8 | 5.0 → 5.0 | 0.8 → 0.8 | 110 → 110 | 106 → 106 | 20.9 → 20.9 |

**C. One lever at a time, held from 2027 (parameters mid-range; change from all-defaults in brackets; baseline 57.8 / 5.0 / 0.8 / 110.4 / 105.9 / 20.9)**

| Lever setting | Employment rate | Unemployment | Median income | Bottom fifth | Homelessness |
|---|---|---|---|---|---|
| `public_jobs_m` = 4 | +1.3 | −0.3 | +4.1 | +3.3 | −0.5 |
| `hours_share` = 0.5 | +1.2 | −0.6 | −1.0 | +0.2 | 0.0 |
| `worktime_cut_pct` = 10 | +1.0 | −0.2 | −3.0 | −1.3 | +0.6 |
| `new_business` = 1.3 / 0.75 | +0.9 / −0.9 | −0.4 / +0.4 | +3.0 / −2.7 | +2.4 / −2.2 | −0.4 / +0.3 |
| `deploy_pace` = 0.7 / 1.3 | +0.6 / −0.9 | −0.3 / +0.5 | +0.4 / −1.2 | +0.5 / −1.2 | −0.2 / +0.2 |
| `adoption_speed` = 0.5 / 1.6 | +0.6 / −0.5 | −0.3 / +0.3 | −0.5 / +0.6 | −0.2 / +0.2 | −0.1 / 0.0 |
| `deploy_regulation` = 1 | +0.6 | −0.3 | −0.5 | −0.2 | −0.1 |
| `ai_pricing` = +1 / −1 | +0.4 / −0.4 | −0.2 / +0.2 | +1.5 / −1.5 | +1.2 / −1.2 | −0.2 / +0.1 |
| `competition_policy` = 1 | +0.4 | −0.2 | +1.5 | +1.2 | −0.2 |
| `retraining_pct_gdp` = 0.5 | +0.3 | 0.0 | +1.0 | +0.8 | −0.2 |
| `union_pressure` = 1 | +0.2 | −0.1 | +1.1 | +0.6 | −0.1 |
| `layoff_share` = 0.2 | +0.1 | −1.2 | +0.2 | +0.2 | −0.1 |
| `wage_sharing` = 0.3 | 0.0 | 0.0 | +2.9 | +1.4 | −0.1 |
| `capital_tax_pct` = 20 | −0.1 | 0.0 | −0.7 | −0.5 | 0.0 |
| `transfers_pct_gdp` = 5 (universal) | −0.9 | +0.1 | +9.0 | +28.5 | −4.5 |
| `household_saving` = +0.05 | −1.3 | +0.3 | −4.0 | −3.3 | +0.5 |
| `housing_policy` = 1 | 0.0 | 0.0 | +6.6 | +8.0 | −6.9 |

**Reading the tables**
- **Jobs (question 1)** turn mostly on whether new kinds of human work appear (`new_task_rate`), then on how fast capability and adoption run, then on pass-through and the demand response. The sector-level Jevons parameter matters less for the whole economy than its name suggests, because spending that does not come back to the automating sector partly lands elsewhere — the brief's own point that the economy-wide effect "depends on new sectors, not the automated one". The write-up should treat "a Jevons effect for work" as the sum of three channels: own-sector demand (`c_price_m`), spending shifting to other sectors (`c_shift_m`), and new work (`c_newwork_m`).
- **Living standards (question 2)** turn mostly on housing supply, then new work, pay-sharing and pass-through. Homelessness is almost entirely a housing-supply and low-income story, as the evidence says.
- **No single player lever is as strong as the dealt conditions**, except cash transfers for the bottom fifth and housing policy for homelessness.
- `demand_mult` only bites when jobs are being lost on net or pay is falling behind trend; at mid-range conditions it is nearly inert, in bad draws it deepens the hole.
- `layoff_share` moves the unemployment *rate* by a point without changing how many people work — a reminder to read the employment rate.

## Known limits (say these in the write-up)
- Gains from AI are counted only as labour saving. New products, faster science and quality improvements are not, so GDP growth (median about 2.4% a year, 90th percentile about 3.4%) is on the low side of "rapid AI" forecasts.
- One national labour market; no regions, ages or skills. The entry-level squeeze shows up only as lower participation.
- No financial sector, interest rates, inflation or trade. The central bank and the rest of the world act only through `shock_demand_pct`.
- Wages are one index with fixed sector relativities.
- Federal budget only; state and local budgets are narrated by the referee.
- The poverty, unrest and top-1% formulas are simple indices, not estimates.

## Selftest
`python3 economy/model/econ.py selftest` checks: baseline reproduces every start value; the no-AI world stays put; employment change equals created − destroyed + population growth − voluntary exits in 3,150 random rounds; no negative stocks, NaNs or out-of-range rates; a 2-year step equals two 1-year steps; 15 direction-of-effect checks (for example stronger demand response → more jobs created; freer housing supply → less homelessness; capital tax → smaller deficit); the housing range matches the brief; and both an optimist's and a pessimist's world are reachable on both questions.
