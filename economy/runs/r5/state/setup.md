# Setup — r5 (REFEREE ONLY — never show players)

Seed 819616. Rolls are in `log.md`.

## 1. Dealt by the model (`econ.py init`, verbatim)

```
HIDDEN CONDITIONS (referee only - never show players):
- desk-work AI is very fast  [cog_auto_2032 = 0.379, middle third of range]
- robots arrive mid-period (4-6 years behind)  [robot_lag_years = 5.97, middle third of range]
- people do NOT buy much more when things get cheaper (weak Jevons)  [jevons = 0.686, low third of range]
- many new kinds of human work appear  [new_task_rate = 0.979, high third of range]
- firms adopt slowly  [diffusion_t50 = 14.1, high third of range]
- savings are split between prices and profit  [passthrough = 0.586, middle third of range]
- pay shares well in productivity gains  [wage_share = 0.42, high third of range]
- housing supply responds partly  [housing_supply = 0.414, middle third of range]
- investment booms cushion lost wages  [demand_mult = 0.712, low third of range]
- Washington is gridlocked  [policy_lag_years = 5.27, high third of range]
- any federal response would be small  [policy_scale_pct = 2.57, low third of range]
- starting political configuration: divided
```

Note: the plain-word line says "gridlocked" (5.27 is in the top third of the log range) but the configuration rule (2.5–5.5 = divided) and `init`'s own last line give **divided**. The referee uses **divided** for the law-odds table. `policy_scale_pct` is ignored in a played game.

## 2. In plain words

A fairly kind world for jobs, hidden behind a fast frontier. Desk-work AI improves quickly (mid-range for this premise) and robots trail by about six years. Firms adopt slowly (half the gap closed in about 14 years), so the capability overhang grows. Cheaper output does not bring much extra buying, but new kinds of human work appear almost one-for-one with jobs automated, and pay captures a large part of the saving. Savings are split between prices and profit. Housing can be built only partly: real housing costs roughly flat without policy. Lost wages do not snowball much. Washington is divided: big bills usually fail.

## 3. Non-model setup rolls

| # | Roll | Result | Meaning |
|---|---|---|---|
| S1 | coalition, p=0.50 | r=0.2881 SUCCESS | **Growth-first coalition leads** (public). Pro-deployment, tax-averse, sceptical of new entitlements. |
| S2 | fed, draw 3 | 1 | **Hawkish central bank** (referee-only). No demand support when unemployment jumps; −0.5 `shock_demand_pct` if unemployment falls under 3.5%. |
| S3 | states, draw 3 | 2 | **Mixed state housing politics** (public in broad terms). States add +0.05 to `housing_policy` every second round, ceiling 0.15. |
| S4 | t01 event, draw 24 | 3 | **Generation leap** — `shock_frontier_cog` +0.04 in the 2027 round. |

## 4. Starting levers

All defaults (S3 is not 3, so `housing_policy` starts at 0). Round 01 `levers.json` must include `"shock_frontier_cog": 0.04`.

## 5. First-round hints (setup-spec §3; roll 0.25 each, SUCCESS = uninformative)

| Seat | Roll | Hint given |
|---|---|---|
| ai-firms | 0.8197 FAIL → informative | `passthrough` (middle): rivals match about half of each price cut; margins hold on bundled enterprise deals. |
| employers | 0.8173 FAIL → informative | `jevons` (low): a 10% price cut in a pilot raised volume about 6%. |
| entrepreneurs | 0.1248 SUCCESS → uninformative | `new_task_rate` is high, but the note says only that results are mixed and too early to read. |
| federal-gov | 0.3661 FAIL → informative | Vote count: divided — needs the other side for anything big. |
| households | 0.6961 FAIL → informative | `housing_supply` (middle): rents about level with pay; some building, slow permits. |
