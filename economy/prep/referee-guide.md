# Referee guide

Your job: turn what the five players decided into lever values, roll for anything uncertain, run the model, and report what it says. You do not steer the story.

## 1. Order of work each round

1. Read orders. List every decision. Mark each as *certain* (the player controls it outright) or *uncertain* (needs a roll: laws, strikes, court challenges, products landing).
2. Roll the uncertain ones with the odds in §3. State odds before rolling. PARTIAL means half-size.
3. Start `levers.json` from last round's values (`state.json` → `prev_levers`). Change a lever only where a resolved decision, a non-player rule (§4) or the drawn event (`events.md`) says so, using the sizes in §2.
4. Run `econ.py step` as `economy/model/README.md` describes. Report its numbers unaltered.
5. Narrate, publish lagged statistics (§5), draw the next event, write intel.

## 2. Decisions → levers

One "notch" is the size given. A lever moves at most **two notches a round** unless a law sets it directly. If players pull opposite ways, net them. If nobody mentions a lever, it stays where it was.

| Lever (range; default) | Who | What moves it, and by how much |
|---|---|---|
| `deploy_pace` (0.7–1.3; 1.0) | AI firms | Race to release / scale robots: +0.1 a notch. Voluntary slow-down: −0.1. A federal moratorium law sets 0.7. |
| `ai_pricing` (−1–1; 0) | AI firms | Cut prices hard, open access: +0.5. Raise margins, bundle, lock in: −0.5. |
| `adoption_speed` (0.5–1.6; 1.0) | Employers | Company-wide automation drive: +0.15. Cautious pilots only: −0.15. Above 1.3 needs an explicit mass-restructuring decision. |
| `layoff_share` (0.2–0.9; 0.6) | Employers | Layoffs as the main tool: +0.15. No-layoff / attrition-and-hiring-freeze policy: −0.15. |
| `hours_share` (0–0.5; 0.1) | Employers | Shorter weeks instead of cuts: +0.1 a notch. Above 0.3 needs a federal subsidy or law backing work-sharing. |
| `wage_sharing` (−0.1–0.3; 0) | Employers | Profit-sharing or across-the-board raises: +0.1. Pay squeeze: −0.1. |
| `new_business` (0.75–1.3; 1.0) | Entrepreneurs | Big push to found firms that hire people: +0.1. Building AI-only firms with almost no staff: −0.1. Then add a standing adjustment, recomputed every round (not cumulative): +0.1 if `ai_pricing` ≥ 0.5 or a federal small-business law is in force; −0.1 if `ai_pricing` ≤ −0.5. |
| `union_pressure` (0–1; 0) | Households | Organising drive or strike: roll (§3); success +0.25. Fades 0.1 a round if not renewed. |
| `household_saving` (−0.03–0.05; 0) | Households | Cut back and save: +0.02. Spend freely: −0.01. Automatic: +0.01 the round after unemployment rises by 1 point or more. |
| `transfers_pct_gdp` (0–10; 0), `transfer_target` (0–1; 0) | Federal | As enacted. $1,000 a month to every adult ≈ 10; to the bottom two-fifths ≈ 4 with target 1. An expanded child credit ≈ 0.5 with target 0.7. |
| `capital_tax_pct` (0–30; 0) | Federal | As enacted, in percentage points of extra tax on profits. A "token tax" or "robot tax" maps to 3–8 points. |
| `retraining_pct_gdp` (0–1; 0) | Federal | As enacted. Wage insurance counts here. |
| `public_jobs_m` (0–8; 0) | Federal | As enacted, at most +2m a year (hiring takes time). |
| `worktime_cut_pct` (0–15; 0) | Federal | As enacted. A 32-hour standard week ≈ 10 (not all workers are covered). |
| `deploy_regulation` (0–1; 0) | Federal | Disclosure and audit rules 0.1; licensing or human-in-the-loop rules in some sectors 0.3; economy-wide 0.6; near-ban on job-replacing uses 1.0. |
| `competition_policy` (0–1; 0) | Federal | Active antitrust cases 0.3; open-access or interoperability mandates 0.6; break-ups 1.0. |
| `housing_policy` (0–1; 0) | Federal + states | Federal: incentives 0.2; funded building programme with zoning conditions 0.4; pre-emption plus Housing First at scale 0.7. Add the state contribution from §4. Cap 1. |

**Other menu items**
- *Employers' own pricing:* passing savings on = +0.25 on `ai_pricing`; keeping them = −0.25 (net with the AI firms' choice, then clip).
- *Privately funded worker funds or dividends* (AI firms, employers): add to `transfers_pct_gdp` at their size (US GDP ≈ $31 trillion, so $100bn a year ≈ 0.3) with `transfer_target` as described. The model books this as public spending; say so in `resolution.md` if it exceeds 0.5.
- *Work-sharing subsidy law:* lifts the employers' `hours_share` ceiling from 0.3 to 0.5; cost about 0.2% of GDP, booked under `retraining_pct_gdp`.
- *Consumer boycott* (households): roll 0.30; success = `shock_adoption` 0.9 this round.
- *Entrepreneurs' push into factory-built housing:* +0.05 a round on `housing_policy` (at most +0.15 in total), only while `housing_policy` ≥ 0.2 already or setup roll S3 = 3.
- *Dollar amounts* convert at $31 trillion of GDP in 2026 prices, scaled by the scorecard GDP index.

**Timing.** Regulations and company decisions bite in the round decided. Federal spending and taxes passed in a one-year round take effect the next round; in a two-year round, the same round.

**Executive action without Congress** can set at most: `deploy_regulation` 0.3, `competition_policy` 0.4, `housing_policy` +0.1. No new taxes or transfers.

**Off-menu decisions.** Map to the nearest lever at a size you can defend by analogy with the table; say so in `resolution.md`. If nothing fits, narrate it and leave the model alone.

## 3. Standing odds

**Federal laws.** Size: *small* (under 0.5% of GDP, or a rule change), *medium* (0.5–2%, or a major regulation or a tax under 10 points), *large* (over 2%, a new entitlement, a tax of 10+ points, a moratorium).

| Political configuration | Small | Medium | Large |
|---|---|---|---|
| Responsive | 0.80 | 0.60 | 0.40 |
| Divided | 0.55 | 0.35 | 0.15 |
| Gridlocked | 0.30 | 0.15 | 0.05 |

Use `--partial 0.15`. Adjust, then clamp to 0.05–0.95:
- Fits the lead coalition's instincts (setup roll S1) +0.10; cuts against them −0.15.
- Unrest index 50–64: +0.10 for worker-protection and transfer bills; 65 or more: +0.20.
- Deficit above 8% of GDP: −0.10 for unfunded spending.
- Employers **and** AI firms publicly oppose: −0.10. Both publicly support: +0.10.
- `union_pressure` ≥ 0.5: +0.05 for worker bills.
- At most two bills a round get a roll; the player ranks them.

**Other rolls**

| Thing | Odds |
|---|---|
| Strike or organising drive succeeds | 0.35; +0.15 if unemployment is under 5%; +0.15 if unrest ≥ 50; −0.15 if unemployment is over 8% |
| A court blocks a new federal rule or tax in its first round | 0.20 (0.35 if done by executive action). Blocked = lever reverts to its previous value and stays there until re-enacted (a new bill, a new roll). |
| A company pledge (no layoffs, profit-sharing) is actually kept next round when profits are under pressure | 0.60 |
| A voluntary slow-down among AI firms holds for a second round | 0.50 |

**Elections** (end of rounds 02, 04, 05, 06). (a) Lead coalition loses its lead with p = 0.35 + 0.01 × (unrest − 35), +0.10 if median income is lower than two rounds ago, −0.10 if it is more than 3 points higher; clamp 0.15–0.85. On a loss, the other coalition leads. (b) Then `roll.py --draw 3`: 1 = one step more responsive, 2 = no change, 3 = one step more gridlocked; if unrest ≥ 55 read a 2 as a 1.

## 4. Non-players

- **Central bank** (setup roll S2). If unemployment rose by 0.7 points or more last round: `shock_demand_pct` +1.0 (dovish), +0.5 (neutral), 0 (hawkish). If unemployment is under 3.5%: −0.5 if hawkish.
- **States and cities.** Housing: add +0.05 a round to `housing_policy` if S3 = 3 (ceiling 0.3 from states alone), +0.05 every second round if S3 = 2 (ceiling 0.15), nothing if S3 = 1. Budgets: if unemployment is above 6%, states cut — `shock_demand_pct` −0.5.
- **Courts.** As §3.
- **Voters.** As elections above. Between elections they show up only through the unrest index and the households player.
- **Rest of the world.** Other countries keep deploying. If `deploy_regulation` ≥ 0.6, tell AI firms and employers that rivals abroad are pulling ahead; no model effect.

## 5. Statistics the players see

- Unemployment, participation, GDP growth and prices: the scorecard value plus noise. Draw `roll.py --draw 5` once a round: 1 → −0.2, 2 → −0.1, 3 → 0, 4 → +0.1, 5 → +0.2 points on unemployment; apply the same sign at five times the size to the median-income index.
- Homelessness and poverty: published one round late.
- Nobody publishes "jobs destroyed" and "jobs created". Employers see their own cuts; entrepreneurs see their own hiring; the public sees announced layoffs (about 40% of jobs destroyed) and the net change in employment.
- Never reveal hidden conditions, lever names' internals, channel breakdowns (`c_*`, `d_*` columns) or how many rounds remain.

## 6. Anti-bias rules

1. **No drift to the middle.** If the model says unemployment is 3% or 11%, report it.
2. **No rescues.** Do not soften levers, invent a helpful event, or raise law odds because things are going badly. Bad outcomes are data.
3. **No punishments.** Do not add friction because things are going well.
4. **Decisions are the players'.** Never alter, add or drop one. If an order is vague, take the most literal reading and the smallest size.
5. **Every lever change has a named cause** (a decision, a roll, a §4 rule or the event) written in `resolution.md`.
6. **Same orders, same levers.** Before running the model, ask whether another referee reading only this guide would set the same values. If not, move to the table's value.
7. **Self-interest is expected.** Do not reward public-spirited play with better odds.
