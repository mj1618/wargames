# Setup — run r4 (REFEREE ONLY — never show players)

Seed 928834. Initialised with `econ.py init`; rolls in `log.md`.

## 1. Hidden conditions dealt by the model (verbatim from `init`)

- desk-work AI is very fast  [cog_auto_2032 = 0.401, middle third of range]
- robots arrive early (2-4 years behind desk AI)  [robot_lag_years = 3.84, low third of range]
- cheaper things unlock a lot of new demand (strong Jevons)  [jevons = 1.67, high third of range]
- many new kinds of human work appear  [new_task_rate = 1.07, high third of range]
- firms adopt quickly  [diffusion_t50 = 3.08, low third of range]
- savings are split between prices and profit  [passthrough = 0.644, middle third of range]
- pay shares well in productivity gains  [wage_share = 0.537, high third of range]
- housing can be built freely and cheaply  [housing_supply = 0.965, high third of range]
- investment booms cushion lost wages  [demand_mult = 0.746, low third of range]
- Washington is gridlocked  [policy_lag_years = 6.12, high third of range]
- any federal response would be small  [policy_scale_pct = 1.45, low third of range] (dice-only runs; ignored here)
- starting political configuration: gridlocked

**In plain words:** a fast-moving, forgiving economy with a stuck government. Firms adopt AI very quickly and robots are not far behind, so disruption comes early and hard; but cheaper goods unlock lots of new demand, many new kinds of human work appear, pay shares in the gains, and housing can be built. Washington can pass almost nothing.

## 2. Non-model setup rolls

| # | Roll | Result | Meaning |
|---|---|---|---|
| S1 | Coalition, p=0.50, r=0.3132 | SUCCESS | **Growth-first coalition leads** (pro-deployment, tax-averse, sceptical of new entitlements). Public. |
| S2 | Central bank, draw 3 | 2 | **Neutral.** +0.5 `shock_demand_pct` if unemployment rose 0.7+ points last round. Referee-only. |
| S3 | State housing politics, draw 3 | 2 | **Mixed.** States add +0.05 to `housing_policy` every second round, ceiling 0.15 from states alone. Public in broad terms. |
| S4 | Round-1 event, draw 24 | 12 | **Liability ruling.** `shock_adoption` 0.8 in the t01 levers. |

Law odds: gridlocked row (small 0.30 / medium 0.15 / large 0.05), growth-first instincts +0.10 / against −0.15.

## 3. Starting levers

All defaults (S3 is not 3, so `housing_policy` starts at 0). Round 01 must carry `shock_adoption` 0.8 from the event.

## 4. First-round hints (one per seat; `roll.py 0.25`, SUCCESS = make it uninformative)

| Seat | Hints at | Noise roll | Hint given |
|---|---|---|---|
| ai-firms | `passthrough` (middle) | r=0.8901 FAIL → informative | Rivals matched about half of a price cut within a quarter; the rest stuck as margin. |
| employers | `jevons` (high) | r=0.0194 SUCCESS → uninformative | Price-cut pilot coincided with a rival's outage; the sales rise cannot be read. |
| entrepreneurs | `new_task_rate` (high) | r=0.7104 FAIL → informative | Customers turning up for services that did not exist two years ago. |
| federal-gov | political configuration | r=0.1993 SUCCESS → uninformative | The configuration itself is stated plainly, as setup-spec §5 requires; the extra whip-count colour is deliberately unreadable. |
| households | `housing_supply` (high) | r=0.5767 FAIL → informative | Cranes and new blocks locally; asking rents flat. |

No hints given on `demand_mult`, `robot_lag_years` or `policy_scale_pct`.
