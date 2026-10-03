# Setup — run r3 (REFEREE ONLY — never show players)

Seed 235553. Initialised with `econ.py init`.

## 1. Hidden conditions dealt by the model (verbatim)

```
HIDDEN CONDITIONS (referee only - never show players):
- desk-work AI is extremely fast  [cog_auto_2032 = 0.58, high third of range]
- robots arrive mid-period (4-6 years behind)  [robot_lag_years = 4.79, middle third of range]
- cheaper things unlock a lot of new demand (strong Jevons)  [jevons = 1.68, high third of range]
- many new kinds of human work appear  [new_task_rate = 0.882, high third of range]
- firms adopt at a moderate pace  [diffusion_t50 = 9.24, middle third of range]
- savings are split between prices and profit  [passthrough = 0.546, middle third of range]
- pay shares well in productivity gains  [wage_share = 0.559, high third of range]
- housing can be built freely and cheaply  [housing_supply = 0.991, high third of range]
- investment booms cushion lost wages  [demand_mult = 0.675, low third of range]
- Washington can act within a couple of years  [policy_lag_years = 1.4, low third of range]
- a federal response would be medium-sized  [policy_scale_pct = 6.16, middle third of range]
- starting political configuration: responsive
```

In plain words: the machines get very good at desk work very fast, but this is a forgiving economy. Cheaper goods and services pull in a lot of extra demand, many new kinds of human work appear, pay shares well in the gains, housing can be built almost freely, and lost wages do not snowball. Firms adopt at a moderate pace and savings are split between prices and profit. Robots are about five years behind. Washington is able to act. (`policy_scale_pct` is ignored in played games.)

## 2. Setup rolls (all in `log.md`)

| # | Roll | Result | Meaning |
|---|---|---|---|
| S1 | p=0.50, r=0.1138 | SUCCESS | **Growth-first coalition leads** (pro-deployment, tax-averse, sceptical of new entitlements). Public. |
| S2 | draw 3 | 2 | **Central bank neutral**: +0.5 `shock_demand_pct` after a rise in unemployment of 0.7 points or more. Referee-only. |
| S3 | draw 3 | 1 | **Big states resist building**: no state contribution to `housing_policy`, ever. Public in broad terms. |
| S4 | draw 24 | 15 | **Round-1 event: Housing squeeze** — `shock_housing_pct` +3.0 in the t01 `levers.json`. |

Political configuration: **responsive** (law odds 0.80 / 0.60 / 0.40 before adjustments; growth-first instincts +0.10, against them −0.15).

## 3. Starting levers

All defaults. `housing_policy` starts at 0 (S3 is not 3). The t01 `levers.json` must carry `shock_housing_pct: 3.0` from the event.

## 4. First-round hints (one per seat; roll 0.25, SUCCESS = make it uninformative)

| Seat | Hints at | Roll | Hint given |
|---|---|---|---|
| ai-firms | `passthrough` (middle) | r=0.4024 FAIL → informative | Rivals matched about half of a price cut; the rest of the market held its margins. |
| employers | `jevons` (high) | r=0.0292 SUCCESS → uninformative | One pilot price cut; the result was muddied by a rival's promotion. |
| entrepreneurs | `new_task_rate` (high) | r=0.2399 SUCCESS → uninformative | Some new customer types, but hard to tell from a fad. |
| federal-gov | political configuration | r=0.0629 SUCCESS → uninformative extra hint | The configuration itself is stated plainly, as setup-spec §5 requires; the extra whip-count colour is neutral. |
| households | `housing_supply` (high) | r=0.6318 FAIL → informative | Where permits are granted, homes go up quickly and cheaply. |

Note the irony to watch: the one thing this world does best (building homes) is where the politics (S3) and the first event (housing squeeze) both point the wrong way.
