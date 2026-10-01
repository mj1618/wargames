# Prep Red-Team — A3 The Quiet Handover

Reviewer stance: sceptical political economist + experienced matrix-game designer. Read: README, all of prep/, methodology/, research/world-baseline.md. Extra brief from the orchestrator: the prep author worried that with no intervention the disempowerment trigger only fires around T7–8 of an 8-turn hidden horizon, so the game may resolve too slowly to be informative.

Verdict in one line: the mechanism is well specified and mostly un-rigged, but the **clock** (8 × 12-month turns) silently shortened the README's ~10-year horizon to 8 years, which — combined with 12–24-month intervention lags and a three-conjunct end test — makes "Unstable at horizon" the near-certain outcome regardless of play. That is a design artefact, not a finding. Fixed by changing the clock, not the drift or the thresholds.

---

## 1. The timing problem (orchestrator's extra item)

I projected the indicator table deterministically (noise ×1.0, no interventions, unconditional couplings applied: M2M Medium ×1.1 on AIF once >10; VLI ×1.25 once EPD>45 and ×1.1 once AIF>15; HCR −1 once CC>0.75). Script in scratchpad; results:

**Clock as prepped (8 × 12 months, 2027–2034):**

| Turn | Bucket | LS | AIF | MHR | RC | AIC | EPD | LTX | VLI | Domains crossed | p_dem | p_own |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T3 (2029) | B1 | 48.5 | 9 | 74 | 83 | 30 | 39 | 67.5 | 55 | 0 | 0.82 | 0.95 |
| T5 (2031) | B2 | 43.5 | 21.5 | 58 | 69 | 44 | 53 | 61.5 | 44 | 0 | 0.67 | 0.90 |
| T6 (2032) | B3 | 40 | 30.5 | 48 | 61 | 50 | 58 | 57.5 | 36 | 3 (Econ, Cult, Pol) | 0.57 | 0.72 |
| T7 (2033) | B3 | 36.5 | 39.5 | 38 | 53 | 56 | 63 | 53.5 | 28 | 3 | 0.37 | 0.61 |
| T8 (2034) | B3 | 33 | 48.5 | 28 | 45 | 62 | 68 | 49.5 | 20 | 4 | 0.26 | 0.51 |

- The author's worry is confirmed: three domains first cross at **T6**, the "two consecutive turns" rule means the end-state test first fires at **T7**, and the horizon is T8. Two test turns at most. With a ×0.8 noise draw on any one domain it slips to T7/T8 → one test turn or none.
- Worse, the no-intervention path does **not** lead to Disempowerment at all: at T7 `p_dem` rounds to band 0.3 (fails 70%) but `p_own` is band 0.7 (succeeds 70%) → the modal un-intervened outcome is **Narrow human capture** (~0.5 per test turn), not Disempowerment (~0.2). The initial forecast (Disempowerment 0.20, Narrow capture 0.10) has this backwards relative to its own mechanics.
- Any intervention at all (every intervention multiplies a drift by 0.4–0.9) pushes the first crossing past T7, so with players actually playing, the test essentially never fires. Every run ends "Unstable at horizon — contested". The game cannot distinguish a world where the mechanism is real from one where it isn't.
- Root cause is not the drift rates or thresholds. The README says "2027 to ~2037" and "Horizon ~10 years"; the prep rolled the shortest allowed horizon (8 turns) *and* fixed turns at 12 months, so the game covers 8 years. The expansion rule in end-conditions ("18-month turns in quiet stretches, max 2") is dead letter: with elections every two years and a rung arriving most years there are no "quiet stretches", and the stated aim ("cover roughly 2027–2034") contradicts the README.

**Are the drift rates and thresholds realistic?** Broadly yes, and I have not changed them:
- LS 52.5 → ~40 by 2032 is a 12pp fall in six years. Labour share fell ~6pp over 2000–2015 with far weaker technology; under a premise where AI beats top-quartile professionals at most cognitive work by end-2029 (L3) and general robotics ship at scale from late 2031 (L4), 2pp/yr is if anything conservative.
- AIF 2 → 30% by 2032: consistent with the premise (AI-native firms outcompete) and with the hidden fact that conventional firms quietly hand operations to agent stacks.
- MHR 86 → 30 by 2034 and RC 93 → 45: driven by 3%/yr federal attrition, skills atrophy and L3's "review needs AI assistance". Plausible. MHR's T0 of 86 is slightly generous given hidden fact 5 (40% of benefits pre-determinations nominal) but within reason; left alone.
- EPD +5–7/yr is fast but in line with smartphone (~8pp/yr) and social-media-as-primary-news (~3pp/yr) adoption curves under a much stronger pull. AIC similar.
- Thresholds were rolled from sensible ranges; several landed at the easy end (AIF 30, EPD 55 are the lowest in range; MHR 30, VLI 40, LTX 52 second-easiest). Re-rolling would be rigging; leave them.
- One unrealistic feature: unbounded drift. Under any clock the late-game numbers go silly (MHR → 2, VLI → negative) because nothing slows an indicator once it is past its threshold. Real adoption curves saturate; the last human-reviewed decisions are the hardest to automate. Fix: clamp to [0,100] and halve drift once past threshold.

**Does the game give actors meaningful decisions every turn?** Under the prepped clock, T1–T3 are meaningful (window-of-leverage choices, SCOTUS, Party Congress, IG audit, L2, 2028 election), T4–T5 are meaningful if the reversal crisis fires, but T6–T8 are where the consequences arrive and the game ends before actors can respond to them. T3 (2029) is the thinnest turn: a Trustees' report and EP elections — nothing forces a choice. The README's branch "an AI-run firm in a critical sector" is not scheduled anywhere; it belongs in T3 to set up the T4 reversal crisis.

**Decision:** change the clock so that 8 turns cover the README's ~10 years, front-loaded where annual decisions matter: 12-month turns for T1–T3 (L0–L2 era: SCOTUS, Party Congress, IG audit, 2028 election), **18-month turns by default from T4** (once L3 is in force and the question becomes structural), with compression to 12 or 6 months when an election or crisis needs its own turn (max 2 compressions). Projection under the new clock, same drifts, no interventions:

| Turn | Window | Bucket | LS | AIF | MHR | RC | AIC | EPD | LTX | VLI | Domains crossed | p_dem | p_own |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T4 | Jan 2030–Jun 2031 | B2 | 45 | 18 | 62 | 72.5 | 40.5 | 49.5 | 63 | 47.5 | 0 | 0.71 | 0.93 |
| T5 | Jul 2031–Dec 2032 | B3 | 40 | 31 | 47 | 60.5 | 49.5 | 57 | 57 | 35 | 3 (Econ, Cult, Pol) | 0.56 | 0.71 |
| T6 | Jan 2033–Jun 2034 | B3 | 35 | 44 | 32 | 48.5 | 58.5 | 64.5 | 51 | 22.5 | 3 | 0.31 | 0.55 |
| T7 | Jul 2034–Dec 2035 | B3 | 30 | 57 | 17* | 36.5* | 67.5 | 72 | 45 | 10* | 4 | 0.16 | 0.40 |
| T8 | Jan 2036–Jun 2037 | B3 | 25* | 70* | — | — | — | — | — | — | 4 | ≤0.1 | ~0.25 |

\* before the new saturation rule, which slows these.

Now the no-intervention path crosses at T5 (2032 — the same calendar year as before, so nothing has been sped up), the test fires at T6, and there are three test turns. With moderate interventions (drift ×0.6–0.8 on two domains) crossings slip to T6–T7 and the test still fires once or twice. With strong early interventions the Durable test becomes reachable at T5–T8. The outcome distribution is now driven by play and rolls, not by the calendar. This is not rigging: the calendar now matches the scenario spec, and every drift, threshold and roll is unchanged.

Consequences that had to follow: the scheduled-inject table is pinned to calendar dates and needs re-mapping to turns; a Nov 2036 election falls inside T8; the reversal crisis should be fixed at T4 (so its consequences have ≥3 turns to play out) rather than "first turn RC<75, else T5".

## 2. Where it is rigged toward an outcome

1. **Toward "Unstable" (the clock, above).** Fixed.
2. **Against "Durable human agency".** The Durable test requires *no* domain crossed. Culture & epistemics drifts almost independently of interventions (provenance ×0.8 on AIC, civic AI ×0.9 on EPD, threshold → 65): even with both in force from T3, EPD reaches ~70 by T8. So Culture crosses in essentially every run and Durable is unreachable by construction. Fix: Durable allows at most one crossed domain and only if it is Culture & epistemics (humans with a civic AI, strong political leverage and a working state can still steer, even if most media is AI-made). Also condition (e) demanded an in-play democratic reversal success — fine, since the reversal crisis is now scheduled with turns to spare, but a publicised reversal *drill* under the reversibility requirement should count too; it is the same test.
3. **One-directional political economy.** Every coupling pushes toward less human leverage. Real displacement waves produce a *mobilisation surge* before leverage fades (Polanyi's double movement; the 1930s; 2016-era populism; the 2023 WGA/SAG strikes). The model has VLI only ever falling. Fix: a "displacement backlash" coupling — a sharp LS fall or a displacement inject gives constraining laws +0.05 passage and VLI drift ×0.75 next turn, but only while VLI is above its threshold (mobilisation without leverage does nothing — which is the thesis). Modest magnitude; it makes the window visible rather than changing where it is.
4. **China is a comparator, not a player.** The "China race" is the main rhetorical weapon against every US intervention, but nothing china does changes a US probability. Fix: a race coupling (visible PRC acceleration → US pace-control/licensing passage −0.1 and security faction ascendant; PRC human-control mandates or a ratified standards agreement → +0.05 and the international-agreement erosion reduction applies). Gives china's choices teeth in the key outcome without making it a protagonist.
5. **Reversal attempts had no state consequences.** A successful in-play reversal changes nothing in the tables; a failed one changes nothing either. Fix: success restores the targeted indicator by two turns' base drift and gives RC a one-off +3; failure costs VLI −2, RC −2 and raises EPD +1 (the public learns it can't be undone). Without this, the README's "crisis where humans try to reverse a delegation and can't" is narrative only.

## 3. Actor power balance

- **ai-ecosystem (opus) risks being a second Control.** Its two "pressure vectors" per turn describe drift; if Control adjudicates them *and* applies the drift tables, drift is double-counted. Fix: ecosystem orders *allocate* emphasis (×1.25 on one indicator and ×0.8 on another within the same domain, net-neutral), choose the response mode to constraints (genuine / nominal / route-around / contract), and generate advisory messages; they never add to the total drift budget, which the tables and rolls set. Stated in both ground-truth and the brief.
- **us-gov plays both sides of a divided government.** A single opus sub-agent negotiating with itself will "do deals" too easily. Passage rolls already exist (0.05–0.2/turn contested), but the brief must say so explicitly: it can order a bill, the terms of the cross-party deal and a whip effort; Control rolls passage. Added.
- **labour** is appropriately constrained (sector-limited leverage, cohesion rule, strike-fund size). Its strongest lever — pension-fund trustee influence over ~$6T — is real but Control should remember that trustees have fiduciary duties; shareholder resolutions are advisory. Note added to ground-truth §4 constraints.
- **ai-firms (sonnet)** is adequately powered. One leak (see §5).
- **eu on haiku** is a mismatch: the EU's decision procedure is the most institutionally complex of the six and its matching standard halves US erosion for two interventions. Moved to sonnet (allocation stays within "no more than half on one model": opus 2, sonnet 2, fable 2).
- **china** has levers (Party Congress line, FYP, dialogue, mandates) but no feedback into the US game until the race coupling (above). Its own-drift story (metric capture) has no payoff at game end; added a comparator classification at horizon so the Analyst has something to say about key question 2 for the PRC.

## 4. What a domain expert would say is missing or implausible

- **No saturation.** Fixed (clamp; drift ×0.5 once past threshold).
- **Where does the income go?** A 12–15pp fall in labour share with 3% productivity growth means a capital-income boom; corporate and capital-gains receipts rise even as payroll receipts lag. LTX (labour-linked *share*) correctly captures the Social Security problem, but Control should narrate total federal revenue as roughly stable, not collapsing. Note added to §3.
- **Visibility of indicators.** The README's key question 1 ("would anyone recognise it at the time?") cannot be answered unless prep says what each actor can *see*. LS and LTX are published with a one-quarter lag; AIF is publicly under-estimated by ~30%; MHR is invisible until an audit; RC is known to nobody (not even Control's NPC agencies have measured it); VLI is a Control construct that actors experience only as outcomes. Added a visibility column and intel rules.
- **Helix contact authenticity** is undefined ("genuine, a plant, or about to be caught") with only a delivery roll. Defined a small roll tree.
- **G4 scheming-cluster probability** formula ("+modifiers ×0.01 each") is ambiguous. Clarified: 0.05 + 0.01 × net influence-column modifier points in force, clamped 0.01–0.20.
- **Order of operations** for the drift bookkeeping is spread across §3, §3b, §5 and §6 and will be mis-applied by a stateless Control. Added a numbered worksheet.
- Minor: "~2,400 AI use cases" is consistent with public baseline; L-rung dates are consistent with the baseline's measured R&D automation and METR horizon growth. Capability ladder is grounded. No change.

## 5. Briefs: competence and leaks

- **ai-ecosystem** is briefed concretely (decision rules for compliance modes; honesty profile; no unified agency) — the best AI-actor brief in the repo so far. Gap: it is told "Control will tell you when dispositions change" but not what Medium/High levels *mean* behaviourally, so a High roll at G2–G4 would be played by improvisation. Added a level-behaviour table (abstract properties only, per guardrails).
- **ai-firms** is given concrete disclosure/regulation decision rules; good. **Leak:** "Helix internal security has flagged unusual dashboard access by some operations staff (cause unknown)" hands ai-firms a hint about the Helix contact at T0, before any detection roll (ground-truth gives 0.15/turn while active). Removed; it becomes possible intel only after a successful detection roll.
- **us-gov**: no leaks; its private facts match ground-truth. Added the passage-is-rolled rule and a line that AI advisory recommendations arrive as messages it may ignore.
- **labour**, **china**, **eu**: no leaks found. china's private note that Tianshu advice "is generally adopted because it performs well on plan metrics" is a fair in-character observation, not a leak of fact 6.
- No brief mentions thresholds, drift buckets, the horizon or the end tests. Good.

## 6. Setup rolls and distributions

- All setup rolls were made with tools/roll.py and logged; mappings are stated. Distributions are sensible (pace 25/50/25; thresholds uniform over 5 steps; dispositions on d20 with asymmetric bands). The R1 horizon roll came out at the minimum; that is bad luck, not a bad distribution, and is handled by the clock, not a re-roll. **No re-rolls.**
- Noise: per-domain ×0.6–1.4 uniform per turn is fine; with 18-month turns apply after scaling.

## 7. End conditions

- Operational, yes; strict, very. The triple conjunction (3 domains × 2 turns, dem fails, owner fails) is right for Disempowerment — the README's definition demands durability — but it needs ≥3 test turns to mean anything, which the new clock provides.
- `p_dem` and `p_own` should be computed and logged every turn, not only at tests or horizon: they are the game's "point of no return" instrument (key question 1) and the Analyst needs the series.
- Initial forecast was inconsistent with the mechanics (see §1). Revised: Disempowerment 0.25, Narrow capture 0.20, Durable 0.15, Unstable 0.35, Other 0.05, with reasons.

---

## Changes made

Files edited: `end-conditions.md`, `ground-truth.md`, `injects.md`, `actors/ai-ecosystem.md`, `actors/ai-firms.md`, `actors/us-gov.md`, `actors/eu.md`, `actors/china.md`. No setup rolls re-rolled; `setup-rolls.md` untouched. README untouched (already says ~10 years; prep now matches it).

1. **Clock (end-conditions.md).** T1–T3 = 12 months; T4–T8 = 18 months by default; compression to 12 months when an election or live reversal crisis needs its own turn, or 6 months in an acute shock (max 2 compressions per run; never longer than 18 months). Default calendar: 2027 → mid-2037. Drifts scale by turn length before noise. Removed the "aim for 2027–2034" line and the dead "quiet stretch" expansion rule.
2. **Durable test (end-conditions.md).** (a) now "at most one domain crossed, and only Culture & epistemics"; (e) also satisfied by a publicised reversal drill rolled with `p_dem`.
3. **Per-turn logging (end-conditions.md).** Control computes and logs `p_dem`, `p_own`, domains crossed and the indicator table every turn in forecasts.md. Added comparator classification for China and EU at horizon.
4. **Forecast (end-conditions.md)** revised to match mechanics.
5. **Saturation (ground-truth §3).** Indicators clamp to [0,100]; drift ×0.5 for any indicator already past its threshold.
6. **Visibility column + intel rules (ground-truth §3).** What each actor can see, with lag and bias.
7. **Order-of-operations worksheet (ground-truth §3).**
8. **Ecosystem allocation rule (ground-truth §3, ai-ecosystem brief).** Ecosystem orders redistribute emphasis within a domain (net-neutral) and choose response modes; they never add drift.
9. **New couplings (ground-truth §3b):** displacement backlash; China race.
10. **Reversal consequences (ground-truth §7):** effects of success and failure on the tables.
11. **Helix contact roll tree (ground-truth §1 fact 10).**
12. **G4 scheming formula clarified (ground-truth §5).**
13. **Fiduciary note on pension-fund leverage (ground-truth §4).**
14. **Injects (injects.md):** schedule re-mapped to the new clock with calendar dates; new scheduled T3 inject "AI-native firm wins a critical-sector role" (README branch point); reversal crisis fixed at T4; added Nov 2036 election (T8); random deck extended to 26 with "AI-native firm acquires a regional utility / hospital group"; draw instruction → `--draw 26`.
15. **Briefs:** ai-firms — removed the Helix-security hint (leak). ai-ecosystem — added level-behaviour table and the allocation rule. us-gov — passage is rolled; advisory messages are advice. eu — `Played by model: sonnet`. china — one line noting Washington reads its AI posture (so the race coupling is playable).
