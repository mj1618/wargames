# Setup — r1 (REFEREE ONLY — never show players)

Seed 107862. Rolls are in `log.md`.

## 1. Dealt by the model (`econ.py init`, verbatim)

```
HIDDEN CONDITIONS (referee only - never show players):
- desk-work AI is very fast  [cog_auto_2032 = 0.447, middle third of range]
- robots arrive late (6-8 years behind)  [robot_lag_years = 7.15, high third of range]
- cheaper things unlock a lot of new demand (strong Jevons)  [jevons = 1.64, high third of range]
- many new kinds of human work appear  [new_task_rate = 0.941, high third of range]
- firms adopt quickly  [diffusion_t50 = 3.66, low third of range]
- competition passes most savings to customers  [passthrough = 0.785, high third of range]
- pay barely shares in productivity gains  [wage_share = -0.262, low third of range]
- housing can be built freely and cheaply  [housing_supply = 0.949, high third of range]
- investment booms cushion lost wages  [demand_mult = 0.53, low third of range]
- Washington can act within a couple of years  [policy_lag_years = 1.63, low third of range]
- a federal response would be medium-sized  [policy_scale_pct = 4.28, middle third of range]
- starting political configuration: responsive
```

## 2. In plain words

Desk-work AI improves fast (mid-range of "fast") and firms adopt it quickly, so job losses in offices come early. Robots trail by about seven years, so physical work is safe for most of the decade. The economy's response is mostly kind: cheaper output draws a lot more buying, many new kinds of human work appear, competition hands most savings to customers, lost wages do not snowball, and housing is physically easy to build. The one harsh condition: pay is bid down below its old trend instead of sharing the gains. Washington starts able to act (ignore `policy_scale_pct` in a played game).

## 3. Non-model setup rolls

| # | Roll | Result | Meaning |
|---|---|---|---|
| S1 | 0.50, r=0.1605 SUCCESS | **Growth-first coalition leads** | Public. Pro-deployment, tax-averse, sceptical of new entitlements. Law odds: +0.10 for bills that fit these instincts, −0.15 against. |
| S2 | draw 3 → 1 | **Hawkish central bank** | Referee-only. No demand support when unemployment jumps; −0.5 `shock_demand_pct` if unemployment falls under 3.5%. |
| S3 | draw 3 → 1 | **Big states resist building** | Public in broad terms. No state contribution to `housing_policy`, ever. Entrepreneurs' factory-housing push works only once `housing_policy` ≥ 0.2. |
| S4 | draw 24 → 4 | **Round-1 event: a flat year at the frontier** | `shock_frontier_cog` −0.03 in `t01/levers.json`. Headline public; effect not. |

Political configuration: **responsive** (small 0.80 / medium 0.60 / large 0.40 before adjustments).

## 4. Starting levers

All defaults. `housing_policy` starts at 0 (S3 ≠ 3). Round 1 adds `shock_frontier_cog` −0.03 from the event.

## 5. First-round hints (one per seat; roll 0.25 each, SUCCESS = make it uninformative)

| Seat | Roll | Hint about | Given as |
|---|---|---|---|
| ai-firms | r=0.4698 FAIL → informative | `passthrough` (high) | Rivals and open-weight models matched a price cut within weeks |
| employers | r=0.6639 FAIL → informative | `jevons` (high) | A price-cut pilot brought a surprisingly large rise in volume |
| entrepreneurs | r=0.7285 FAIL → informative | `new_task_rate` (high) | New kinds of customers turning up for services that did not exist two years ago |
| federal-gov | r=0.5635 FAIL → informative | political configuration | Whip count: can pass most of what the coalition agrees |
| households | r=0.3472 FAIL → informative | `housing_supply` (high) | Where building is allowed, homes go up fast and rents ease |

Not hinted: `demand_mult`, `robot_lag_years`, `policy_scale_pct`, `wage_share`, `diffusion_t50`, `cog_auto_2032`.

## 6. Referee note

The tension in this deal: physical ease of building is high, but state politics block it and the lead coalition is the one least inclined to pre-empt them. And pay falls behind while prices fall. Report what the model says; do not steer.
