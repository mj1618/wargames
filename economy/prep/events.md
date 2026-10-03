# Events deck (24)

Draw one per round: `python3 tools/roll.py --draw 24 --label "<run> t<NN> event" --log <RUN>/log.md`. If the same number comes up twice in one play-through, redraw once; if it repeats again, play it.

**Applying an event.** The "model effect" column is exact. `shock_*` levers go into that round's `levers.json` and last one round (a two-year round counts as one round). Where an event adjusts an ordinary lever ("+0.3 on `ai_pricing`"), add it on top of the value the players' decisions produce, then clip to the lever's range. If two things move the same shock lever (an event and a non-player rule in the referee guide), add them (multiply for `shock_adoption` and `shock_new_task`) and clip. Tell every player the public headline in their intel note; never the model effect.

| # | Kind | Public headline | Model effect |
|---|---|---|---|
| 1 | good/bad | **Robot breakthrough.** A general-purpose "robot foundation model" makes cheap humanoids reliably useful in unstructured settings. | `shock_robot_lag_years` −1.5 |
| 2 | bad for robots | **Robot recall.** Injuries in warehouses and homes force a recall and new safety certification. | `shock_robot_lag_years` +1.0; `shock_adoption` 0.9 |
| 3 | good/bad | **Generation leap.** A new model generation does week-long professional projects unaided. | `shock_frontier_cog` +0.04 |
| 4 | boring | **A flat year at the frontier.** The new models are cheaper, not much smarter. | `shock_frontier_cog` −0.03 |
| 5 | bad | **Financial wobble.** AI shares fall by a third; credit tightens for a year. | `shock_demand_pct` −2.0; `shock_adoption` 0.9; −0.1 on `new_business` this round |
| 6 | good | **Build-out boom.** Data-centre, grid and factory investment surges. | `shock_demand_pct` +1.5 |
| 7 | bad | **Energy crunch.** Power shortages and local moratoria delay data centres. | `shock_adoption` 0.8; `shock_frontier_cog` −0.01 |
| 8 | good | **A hit new industry.** A new kind of service nobody predicted takes off and hires people in large numbers. | `shock_new_task` 1.5 |
| 9 | bad | **New-work mirage.** Last year's fashionable new job category is itself automated. | `shock_new_task` 0.7 |
| 10 | good | **A state pilot works.** A large state's wage-insurance-plus-cash pilot shows faster re-employment at modest cost. | No model effect. +0.10 to the odds of a similar federal bill for the next two rounds. |
| 11 | mixed | **Court ruling.** A federal court hears a challenge to the newest federal measure. | Roll 0.4: on SUCCESS the most recently enacted of `transfers_pct_gdp`, `capital_tax_pct`, `deploy_regulation`, `worktime_cut_pct` reverts to its previous value this round. If no such measure exists: no effect. |
| 12 | mixed | **Liability ruling.** Courts hold firms fully liable for harm done by automated decisions. | `shock_adoption` 0.8 |
| 13 | mixed | **Strike wave.** Walkouts spread across logistics, health and public services. | +0.3 on `union_pressure` this round; `shock_adoption` 0.9; `shock_demand_pct` −0.5 |
| 14 | good | **Housing breakthrough.** Factory-built homes win code approval in most states; costs per home fall sharply. | `shock_housing_pct` −3.0; +0.1 on `housing_policy` permanently |
| 15 | bad | **Housing squeeze.** AI wealth concentrates in a few metros and bids up land; insurers pull out of others. | `shock_housing_pct` +3.0 |
| 16 | bad for AI firms | **Major AI incident.** A widely used system causes serious, visible harm; trust drops. | `shock_adoption` 0.85; +0.15 to the odds of any `deploy_regulation` bill for two rounds |
| 17 | good | **Open-weight price war.** Free models match last year's best; prices for AI services collapse. | +0.3 on `ai_pricing` this round |
| 18 | bad | **Consolidation.** Two of the largest AI and cloud providers merge or sign an exclusive pact. | −0.3 on `ai_pricing` this round and next, unless `competition_policy` ≥ 0.5 |
| 19 | bad | **Chip supply shock.** A crisis abroad interrupts advanced chip supply for months. | `shock_frontier_cog` −0.02; `shock_demand_pct` −1.0; `shock_robot_lag_years` +0.5 |
| 20 | good | **Cheap services catch on.** Households start buying AI-delivered tutoring, legal help and home design in bulk, with people in the loop. | `shock_demand_pct` +1.0; `shock_new_task` 1.2 |
| 21 | boring | **Care demand jumps.** An ageing bulge raises demand for health and care workers. | `shock_new_task` 1.1 |
| 22 | boring | **A quiet year.** Nothing unusual. | None |
| 23 | boring | **Data revision.** The statistics office revises past job numbers. | No model effect. Tell players last round's published unemployment was understated by 0.4 points (roll 0.5; on FAIL, overstated by 0.4). |
| 24 | conditional | **Bond-market scare.** Investors balk at federal borrowing. | If the last scorecard deficit is above 7% of GDP: `shock_demand_pct` −1.0 and −0.15 to the odds of any spending bill for two rounds. Otherwise: headline only, no effect. |

Mix: 7 good, 8 bad, 5 mixed or two-sided, 4 boring. Events 1 and 3 help output and hurt jobs; whether they are "good" depends on the dealt conditions, which is the point.
