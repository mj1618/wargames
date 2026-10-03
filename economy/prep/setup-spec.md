# Setup spec — what is dealt at the start of each play-through

Everything here is referee-only. Record it all in `<RUN>/state/setup.md`. Never put any of it in `public-record.md` or an intel note, except where marked "public".

## 1. Dealt by the model (`econ.py init --run <RUN> --seed <SEED>`)

`init` samples eleven hidden conditions and prints them in plain words with the band (low / middle / high third of the range). Ranges and evidence are in `economy/model/README.md`.

| Condition | In plain words |
|---|---|
| `cog_auto_2032` | How fast desk-work AI gets (always fast; this is how fast) |
| `robot_lag_years` | How far behind robots are (2–8 years) |
| `jevons` | Whether cheaper things make people buy a lot more of them |
| `new_task_rate` | Whether new kinds of human work appear |
| `diffusion_t50` | How quickly firms actually adopt |
| `passthrough` | Whether savings reach customers as lower prices or stay as profit |
| `wage_share` | Whether pay shares in the gains |
| `housing_supply` | Whether housing can be built |
| `demand_mult` | Whether lost wages snowball into lost spending |
| `policy_lag_years` | How slow Washington is → the **starting political configuration** (printed by `init`: responsive / divided / gridlocked) |
| `policy_scale_pct` | Used only by dice-only runs; ignore in played games |

Copy the printed block into `setup.md` verbatim.

## 2. Non-model setup rolls (`python3 tools/roll.py … --log <RUN>/log.md`)

| # | Roll | How | Use |
|---|---|---|---|
| S1 | **Which coalition leads the federal government** | `roll.py 0.5 --label "<run> setup S1 coalition"` — SUCCESS = growth-first coalition (pro-deployment, tax-averse, sceptical of new entitlements); FAIL = worker-first coalition (wants protections and transfers, open to taxing AI profits) | Public. Sets the lead faction in the `federal-gov` seat and which column of the law-odds table favours which bills (referee-guide §3). The political configuration from `init` says how much it can get done. |
| S2 | **Central bank stance** | `roll.py --draw 3 --label "<run> setup S2 fed"` — 1 hawkish, 2 neutral, 3 dovish | Referee-only. Governs how the central bank answers demand swings (referee-guide §4). |
| S3 | **State housing politics** | `roll.py --draw 3 --label "<run> setup S3 states"` — 1 big states resist building, 2 mixed, 3 several big states are already pre-empting local zoning | Public in broad terms. Sets the starting value and ceiling of `housing_policy` from state action (referee-guide §4). |
| S4 | **Round-1 event** | `roll.py --draw 24 --label "<run> t01 event"` | As `events.md`. |

## 3. Narrating the dealt conditions without revealing them

Players should be able to *infer* conditions from what they see, as real actors would, but must never be told a parameter or its band.

- Give each player first-round intel that is consistent with the conditions and visible from their seat. Examples: employers see how much customer demand rose when they cut a price in a pilot (hint about `jevons`); AI firms see how fast rivals undercut them (hint about `passthrough`); entrepreneurs see whether new kinds of customers are appearing (hint about `new_task_rate`); the federal seat sees its vote count (political configuration); households see local rents and building activity (hint about `housing_supply`).
- Hints are single noisy observations, not statements of fact. One line each. Roughly one hint in four should be ambiguous or misleading-by-chance (roll `roll.py 0.25` per hint; on SUCCESS make it uninformative).
- Never hint at `demand_mult`, `robot_lag_years` beyond what the scorecard shows, or `policy_scale_pct`.

## 4. Starting lever values

All defaults (see `econ.py levers`), except: if S3 = 3, start `housing_policy` at 0.1.

## 5. First intel notes must include

The world-state baseline numbers; the S1 and S3 results in plain words; the political configuration in plain words to `federal-gov` only ("you can count on passing most of what your coalition agrees" / "you need the other side for anything big" / "almost nothing passes"); the round-1 event; one seat-specific hint as in §3.
