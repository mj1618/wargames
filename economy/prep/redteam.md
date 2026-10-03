# Prep red-team — economy series

Three hostile readings of `economy/model/econ.py`, the prep files and the prompts: a techno-optimist economist, a labour-pessimist economist and a wargame designer. The orchestrator's ruling stands: technology pace is held at the rapid end; the wide uncertainty is in the economy's response. Everything below was tested by running the model, not by reading it. Changes made are in §5; the revised numbers are in `economy/model/README.md`.

## 1. The question asked: is the default spread too narrow or too benign by structure?

Builder's default-preset 2036 figures: unemployment 4.1 / 4.8 / 6.2 (p10/p50/p90), median income 101 / 111 / 121.

**Verdict: the tails are reachable without extreme draws; the narrow band is a product of nine independent draws, not of clamps or hard-wired absorption. But two structural facts shape the centre and one accounting error flattered the optimist's corner.**

Tests run (default levers unless stated; full numbers after the fixes in §5):

| World | Draws | 2036 unemployment | Employment rate (2026: 59.1) | Created per destroyed | Median income | Labour share | Top-1% | Homeless /10k (22) |
|---|---|---|---|---|---|---|---|---|
| Mid-range | every parameter at its midpoint | 5.1 | 57.7 | 0.79 | 109 | 46.6 | 22.7 | 21.0 |
| Reasonable pessimist | every parameter at the 20th percentile of its range (cog 0.53, robots 3 yrs behind, Jevons 0.64, new work 0.4, adoption half-life 4.4 yrs, pass-through 0.34, pay share −0.12, housing 0.2, multiplier 1.3) | 10.4 | 49.1 | 0.38 | 80 | 31.7 | 28.9 | 30.5 |
| … and employers choose layoffs (`layoff_share` 0.9) | same | 13.7 | 49.0 | 0.37 | 80 | 31.6 | 28.9 | 30.5 |
| … and a company-wide automation drive (`adoption_speed` 1.3) | same | 15.0 | 47.6 | 0.38 | 77 | 28.9 | 30.1 | 31.5 |
| Fast tech and fast adoption only | cog 0.6, half-life 3 yrs, all else mid | 7.9 | 53.3 | 0.68 | 104 | 35.5 | 27.3 | 22.0 |
| Reasonable optimist | every parameter at the 80th percentile | 4.6 | 58.7 | 0.94 | 119 | 48.6 | 21.8 | 18.0 |
| `selftest` optimist's world | six parameters at the good end | 3.6 | 60.5 | 1.20 | 128 | — | — | 16.0 |
| `selftest` pessimist's world | seven at the bad end | 11.4 | 47.1 | 0.27 | 70 | — | — | 37.3 |

So the frontier-lab "10–20% unemployment" camp is reached at the 20th-percentile draw plus one employer choice, and the Korinek & Suh wage-collapse camp (median income −20%, labour share 30%) at the same draw. Neither needs a corner. The Jevons / new-work camp is reached at the 80th-percentile draw on jobs (0.94, employment rate within 0.4 of 2026) and clearly on living standards (119, homelessness −18%).

**Clamps.** Wage factor (0.6–1.05), labour share (5–80%), sector destruction (≤90% of a sector), the hiring pools and the "extra spending only hires while there is slack" cap were checked across the 3,000 dice-only runs: none binds. The unemployment floor (3%) is reached only in the optimist corner.

**Where displacement goes.** Three constants decide how much of it shows up as *unemployment* rather than lower participation: the referee's `layoff_share` (default 0.6: 40% of removed jobs leave the labour force immediately), `DISCOURAGE` (excess unemployed giving up each year) and `ABSORB_RATE` (8% a year of slack re-hired at lower pay, fading as machines can do more). With the builder's `DISCOURAGE` 0.20, the pessimist draw had 14.7m unemployed against 23.4m who had given up — the opposite of the Great Recession's split (about 7.5m excess unemployed against 2.5m discouraged, i.e. 8–10% a year). The same displacement reads as 11% unemployment at 0.20 and 15.5% at 0.05, at an identical employment rate. `ABSORB_RATE` barely matters (switching it off moves the pessimist's unemployment from 9.4 to 10.0). Conclusion: the *unemployment rate* is a weak summary by design and the brief says so (H: "the adjustment shows up as lower participation"); the employment rate is the honest number. We lowered `DISCOURAGE` to 0.15 (§5) and made the README say this in step 8.

**The real brake is adoption, not absorption.** In the mid-range run 67% of desk work is automatable in 2036 but only 27% is automated, because `diffusion_t50` (brief H5: 3–20 years, log-uniform, median 7.7) is a half-life against a frontier that moves 6 points a year; the steady-state gap between "can" and "does" is about 11 years. This is faithful to the brief (electrification took 30 years; 17–20% of firms use AI today) and it is "the economy's response", so we left the range alone — but the orchestrator should know that the economists' own "rapid AI" median (participation 62→54 by 2050, brief H) sits near this model's 85th percentile. If the series wants its centre to match that conditional view, the one defensible change is `diffusion_t50` 2–15 years; we did not make it.

## 2. The opposite failure: does anything force a bad outcome?

- **Labour share can only fall.** `COST_SAVING` 0.6 means the machine is paid 40% of the wage it replaces; that is machine-maker income, i.e. capital. So even when pay and customers take the whole saving (pass-through 0.9, pay share 0.3, profit gets nothing) the labour share drifts down about a point a year of heavy automation, and the brief's 55% top end is unreachable. This is correct economics under the premise, not rigging, but it was undocumented. Now in the constants table. If a future red-team wants the optimist's "labour share flat" world, `COST_SAVING` (0.5–0.9, near-free tokens vs robot hardware) is the parameter to free, not `wage_share`.
- **Top-1% share rises in nearly every run** (p10 21.2) for the same reason plus brief E's ownership shares (top 1% hold half of equities). The `active` preset (10-point capital tax, 3% of GDP transfers) holds it to 20.0–22.8. Defensible.
- **Median income p10 ≈ 100.** One run in ten ends below 2026 under default politics; one in five under laissez-faire. The no-AI trend is 109. Not forced: the mid-range run sits on the trend.
- **GDP is on the low side of "rapid AI"** (p90 139, extreme 183) because only labour saving is counted. This mutes the optimist's upside symmetrically with the pessimist's (less to distribute either way). Already in "Known limits".
- **Gains do not create jobs; losses destroy them** (step 7). An asymmetry that leans pessimistic in principle. In practice it is small: the positive fiscal impulse channel does create jobs, and price falls create jobs through the demand response. Left as is, noted here.
- The sector-level Jevons channel (`c_price`) is weak in every run — about 1.3m jobs over the decade at mid-range — because automating 27% of office work cuts office prices only about 5% (0.6 saving × 0.7 labour cost share × 0.55 pass-through). That is the brief's own conclusion (A: economy-wide effects depend on new sectors, not the automated one), so the "Jevons effect for work" question will be answered mostly by `new_task_rate` and the spending shift. The write-up must say so.

## 3. Accounting

- **Bug (fixed): pass-through did not cost capital anything.** Labour share was pay ÷ *real* output, so a firm that passed 90% of its saving to customers kept the same profit share as one that kept 80%. Pass-through had a rank correlation of 0.00 with the labour share and the top-1% share — the series' "who captures the profits" question had no model behind it. Labour share is now pay ÷ output *at current prices*. Effect: pass-through 0.2 → 0.9 now moves the 2036 labour share from 42 to 47.
- **Bug (fixed): pay and prices could both take the whole saving.** At pass-through 0.9 and the old `wage_share` 0.7, pay of remaining workers took 117% of the saving and prices another 90% of it — about twice the pie. The saving is now split explicitly: pay takes its share out of profit first; of what is left, pass-through reaches prices; the rest is profit. Pay plus price cuts can never exceed the saving. `wage_share` is re-ranged to −0.3…0.6 (0.6 = pay takes everything; −0.3 = pay bid down, the Korinek & Suh direction, and the cut adds to what can be passed on). The `selftest` optimist's world now uses pay share 0.3 with pass-through 0.9 (customers and workers split the whole saving), which is the internally consistent version of "labour share flat, mean wages up".
- Consequence worth knowing: pay-sharing is now a trade. It raises the median where there is profit to share and costs jobs where competition already passes the saving to prices (sensitivity table B: `wage_share` −0.3 → 0.6 moves median income 105 → 108 and the employment rate 57.5 → 56.5). The households and employers players will discover this; it is real economics, not a bias.
- Identities verified by `selftest` across 3,150 random rounds (employment change = created − destroyed + population growth − voluntary exits; no negative stocks; shares sum; 2-year step = two 1-year steps). Transfers are deficit-financed in the model (documented). The 2.1% wage loss per point of employment rate is a *local* (commuting-zone) estimate applied nationally; brief B puts national effects at about half of local. Left as is because it is the pessimist's main wage channel and the parameter space already compensates; flagged for the write-up.
- Independence of the eleven draws is an assumption (README says so). Two plausible correlations the brief hints at are *not* modelled: fast capability with fast erosion of new work (B: "AI can do the new tasks too"), and fast adoption with low pass-through (E: superstar firms). Either would widen the spread. Not added: no evidence for a size.

## 4. Briefs, referee guide, events

- **Briefs** are self-interested and concrete; decision menus map one-to-one onto levers with sizes that match the referee table. No hidden parameter leaks (lever names and defaults are the players' own controls; "today about 60% by layoff" is public). Model mix (fable, sonnet ×2, haiku, opus) satisfies the spec. The households brief does not mention that pay demands can cost jobs; left so, since that is for the game to reveal.
- **Referee guide**: five referees would set the same levers for the same orders in nearly all cases. Two lines were ambiguous and are tightened: the conditional `new_business` adjustment is now explicitly a standing, recomputed, non-cumulative ±0.1; a court block now "stays until re-enacted". The guide's anti-bias rules are good. One gap for the referee to watch: `public_jobs_m` in a tight labour market shows up as `c_unfilled_m` rather than jobs — report it.
- **Events**: all 24 have exact model effects; the sum/multiply rule for coinciding shocks is stated; event 11 (court) and 24 (bond scare) are correctly conditional. Mix (7 good / 8 bad / 5 mixed / 4 boring) is fair given events 1 and 3 are two-sided.
- **Setup spec and clock**: consistent with `init` output and `ROUNDS`.

## 5. Changes made

| File | Change | Why |
|---|---|---|
| `model/econ.py` | Labour share = pay ÷ output at current prices | Pass-through now reduces profit (§3) |
| `model/econ.py` | Saving split pay → prices → profit, never more than the saving; `beta` computed once in step 3 | Removes the double count (§3) |
| `model/econ.py` | `wage_share` range −0.3…0.6 (was −0.2…0.7), description rewritten | 0.6 is the whole saving; −0.3 allows wage erosion without an employment collapse |
| `model/econ.py` | `DISCOURAGE` 0.20 → 0.15 | Between the cyclical record (8–10%) and the brief's structural story (§1) |
| `model/econ.py` | `selftest` optimist's/pessimist's worlds use the new range (0.3 / −0.3) | consistency |
| `model/README.md` | Parameter row 7, steps 3/8/9, constants (`COST_SAVING` note, `DISCOURAGE`), all three Monte Carlo tables, headline table (+ "unemployment ≥ 8%" row), extremes, fairness check rewritten with the draws above, sensitivity tables A/B/C, reading notes | Numbers and mechanics changed |
| `model/montecarlo*.csv` | Regenerated (1,000 runs each) | |
| `prep/referee-guide.md` | Two clarifications (§4) | |

Not changed, deliberately: `diffusion_t50` range, `COST_SAVING`, the local wage elasticity, parameter independence — each explained above with what it would take to change it.

## 6. Dry run

`init` (seed 42) → seven `step`s with `{}` and one with a 2%-of-GDP targeted transfer plus housing policy, 1- and 2-year rounds: carried-over levers are announced, an out-of-range lever (`capital_tax_pct` 50) and a repeated period are refused, `state-before-<label>.json` is written each step, the scorecard has 8 rows × 73 columns and the key-numbers block prints. The transfer round lifted the bottom fifth 27% and cut poverty 12.9 → 8.1 in one step, consistent with the 2021 Child Tax Credit episode (brief F). Scratch run deleted.

## 7. Revised default-preset percentiles (p10 / p50 / p90, 2036)

Unemployment 4.2 / 5.0 / 6.6 · employment-to-population 54.7 / 57.7 / 59.5 · jobs destroyed 9 / 18 / 34m · created 6 / 14 / 28m · median income 100 / 109 / 118 · bottom fifth 96 / 106 / 121 · top-1% share 21.2 / 22.4 / 24.7 · homeless 17 / 21 / 25 per 10,000. Laissez-faire: unemployment 4.5 / 5.8 / 8.9, median 96 / 107 / 118. Active: 3.4 / 4.4 / 5.6, median 111 / 120 / 128.
