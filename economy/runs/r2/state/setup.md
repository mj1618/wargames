# Setup — run r2, seed 650397 (REFEREE ONLY)

## 1. Dealt by the model (`econ.py init`, verbatim)

```
HIDDEN CONDITIONS (referee only - never show players):
- desk-work AI is extremely fast  [cog_auto_2032 = 0.588, high third of range]
- robots arrive early (2-4 years behind desk AI)  [robot_lag_years = 2.73, low third of range]
- people buy moderately more when things get cheaper  [jevons = 1.25, middle third of range]
- some new kinds of human work appear  [new_task_rate = 0.65, middle third of range]
- firms adopt quickly  [diffusion_t50 = 3.73, low third of range]
- savings are split between prices and profit  [passthrough = 0.636, middle third of range]
- pay barely shares in productivity gains  [wage_share = -0.0335, low third of range]
- housing can be built freely and cheaply  [housing_supply = 0.751, high third of range]
- lost wages snowball into wider spending cuts  [demand_mult = 1.27, high third of range]
- Washington can act within a couple of years  [policy_lag_years = 1.24, low third of range]
- a federal response would be medium-sized  [policy_scale_pct = 5.13, middle third of range]
- starting political configuration: responsive
```

## 2. In plain words

This is a fast, hard world on the jobs side with a soft landing available on housing and politics. Desk-work AI is at the very fast end, robots are only about three years behind, and firms adopt quickly, so a lot of work can be automated and much of it will be, early. Cheaper goods bring a moderate rise in buying and some new kinds of human work appear, but neither is strong. Savings are split between lower prices and profit; pay barely shares at all (slightly bid down). Lost wages snowball into wider spending cuts, so job losses feed on themselves. Against that: housing can be built freely and cheaply, and Washington starts able to act (responsive).

## 3. Non-model setup rolls (all logged in `log.md`)

| # | Roll | Result | Meaning |
|---|---|---|---|
| S1 | coalition, p=0.50 | r=0.2844 SUCCESS | **Growth-first coalition leads** (pro-deployment, tax-averse, sceptical of new entitlements). Public. |
| S2 | central bank, draw 3 | 3 | **Dovish.** If unemployment rose 0.7+ points last round: `shock_demand_pct` +1.0. Referee-only. |
| S3 | state housing politics, draw 3 | 3 | **Several big states already pre-empting local zoning.** `housing_policy` starts at 0.1; +0.05 a round from states, ceiling 0.3 from states alone. Public in broad terms. |
| S4 | round-1 event, draw 24 | 9 | **New-work mirage.** `shock_new_task` 0.7 in round 01. |

Law odds (referee-guide §3): responsive row 0.80 / 0.60 / 0.40; +0.10 for bills fitting growth-first instincts, −0.15 for bills cutting against them.

## 4. Starting levers

All defaults except `housing_policy` 0.1 (S3 = 3). Round-01 `levers.json` must also carry `shock_new_task` 0.7 (event 9) and add the states' +0.05 on `housing_policy` (to 0.15) per referee-guide §4.

## 5. First-round hints (setup-spec §3)

Noise roll p=0.25 per hint; SUCCESS = make it uninformative. All five rolled FAIL, so all five hints are informative (still single noisy observations).

| Seat | Roll | Hint about | Hint given |
|---|---|---|---|
| ai-firms | r=0.4286 FAIL | `passthrough` (middle) | Rivals matched about half of a price cut; the rest of the market held its margins. |
| employers | r=0.3394 FAIL | `jevons` (middle) | A pilot price cut of 10% lifted volumes about 12%. |
| entrepreneurs | r=0.7735 FAIL | `new_task_rate` (middle) | Some new kinds of customer are appearing, steadily but not in a rush. |
| federal-gov | r=0.8125 FAIL | political configuration (responsive) | Can pass most of what the coalition agrees. |
| households | r=0.8613 FAIL | `housing_supply` (high) | Cranes and new blocks nearby; rents on new leases flat. |

Not hinted, per spec: `demand_mult`, `robot_lag_years`, `policy_scale_pct`.
