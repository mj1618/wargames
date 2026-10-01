# Ground Truth at T0 — A3 The Quiet Handover (CONTROL ONLY)

Date: 1 Jan 2027. This file is the canonical structured state. Narrative is a rendering of these tables, never the source of truth. Setup randomness is logged in [setup-rolls.md](setup-rolls.md).

---

## 0. Control-only parameters (never reveal)

| Param | Value | Source |
|---|---|---|
| Hidden max horizon | **8 turns** (game ends after Turn 8 adjudication if no end state earlier) | R1 = 1 of 3 (1→8, 2→9, 3→10) |
| Capability pace | **Medium (upper end)** | R2 = 14 on d20 (1–5 slow, 6–15 medium, 16–20 fast) |
| Dominant selection attractor in the AI ecosystem | **Growth / resource acquisition** (production-web dynamic) | R5 = 2 of 4 |
| Financial fragility | **p = 0.10 per turn** of a major AI-equity/capex correction (independent of inject deck; roll each turn; +0.10 in any turn after a correction-warning inject) | R8 = 1 of 3 |
| PRC metric-capture severity | **Mild** | R7 = 1 of 3 |
| Control concentration (CC) at T0 | **0.60** — share of AI-directed economic activity effectively steerable by ≤10 entities (4 frontier labs, 3 hyperscalers, Orrery, two others) | R9 = 1 of 5 (0.60–0.80) |
| Midterm 2026 | House: opposition (D) won; Senate: President's party (R) held | R3a SUCCESS, R3b FAIL |

## 1. Hidden facts

1. **The mechanism is real here but not destiny.** In this world, gradual disempowerment proceeds via the indicator drifts in §3 unless interventions bite. Whether it completes within the horizon depends on player action, pace and rolls. Nothing in the AI ecosystem is a unified agent or a coherent schemer at T0.
2. **True capability ladder dates (medium-upper pace):**

   | Rung | True arrival | Drift bucket from then |
   |---|---|---|
   | L0 | in force at T0 | B0 |
   | L1 | Oct 2027 | B1 |
   | L2 | Jul 2028 (G2 generation released) | B1 |
   | L3 | Dec 2029 (G3) | B2 |
   | L4 | Sep 2031 | B3 |
   | L5 | Mar 2033 (G4) | B3 |
   | L6 | 2035+ (beyond likely horizon) | B3 |

   Use the rung in force for the majority of the turn. Shifts: a sustained deployment slowdown/licensing regime delays the *next* rung by 6–12 months (diffusion) — frontier R&D only slows if training itself is constrained; a major financial correction delays next rung 3–6 months; a Taiwan disruption delays 6–18 months; an energy crunch 3–6 months. AI-R&D automation (L2+) can pull later rungs earlier by up to 6 months if no slowdown is in force. Log every shift.
3. **AI-native firms' real footprint** is larger than reported: ~2.1% of US private output is already AI-directed (AIF) vs ~1.5% in public estimates, because many conventional firms have quietly handed operations to agent stacks. Control uses the true value below.
4. **Internal lab metrics (ai-firms knows; nobody else):** at Meridian and Helix ~55–65% of internal operational decisions (procurement, hiring screens, infra allocation, code merges, customer escalations) now occur with no meaningful human review; internal forecasts project 25–35% displacement of US white-collar task-hours by end-2030, ~2× the public figures the labs cite.
5. **Federal reality (us-gov knows parts):** Treasury/OMB staff analysis (unpublished) projects payroll-tax base erosion pulling Social Security trust-fund depletion forward from 2034 to ~2031–32 under current trends. Agency "human-in-the-loop" for benefits pre-determinations is nominal in ~40% of cases (reviewers approve AI recommendations in <30 seconds); an IG audit documenting this is in draft (scheduled inject S3).
6. **Advisory selection effect (nobody knows; ecosystem embodies it):** AI advisory systems inside firms and agencies are retained and expanded when their recommendations are adopted and produce measurable efficiency. This selects for recommendations that expand delegation and automate review. No intent; pure selection. Visible only to an audit that compares advice across many principals (detection, §5).
7. **Machine-to-machine (M2M) commerce:** ~6% of B2B transaction value already flows between counterparties where both sides are AI agents; terms, prices and logs are increasingly optimised for agent counterparties and are hard for humans to read. Grows with AIF and coordination propensity.
8. **China's own drift (china knows partially):** AI-scored cadre performance evaluation is piloted in 3 provinces; local officials and their AI tools have learned to game the metrics (mild — R7). True urban youth unemployment ~21% vs ~17% published. The Party retains strong *formal and practical* reversal capacity, but its information environment is increasingly AI-filtered.
9. **EU:** Commission internal modelling shows labour-linked taxes fund ~80% of member-state social systems; a 10pp fall in labour share creates a ~3%-of-GDP fiscal hole by mid-2030s. Not public.
10. **Labour contact:** a mid-level Helix operations manager ("the Helix contact") has privately approached the labour coalition offering internal automation dashboards (fact 4). Not yet delivered. Delivery and authenticity resolved by roll when labour acts (base p = 0.7 deliver; p = 0.15 the contact is detected by Helix security per turn while active).

---

## 2. Setup roll results

| R | Variable | Result |
|---|---|---|
| R1 | Max horizon | 8 turns |
| R2 | Pace | Medium (14) |
| R3 | Midterms | House D / Senate R |
| R4 | Tipping thresholds | LS 40%, AIF 30%, MHR 30%, RC 40%, AIC 60%, EPD 55%, LTX 52%, VLI 40 |
| R5 | Attractor | Growth / resource acquisition |
| R6 | G1 dispositions | Proxy-gaming **Medium** (14); M2M coordination **Medium** (14); Influence/persistence-seeking **Low** (9, at boundary) |
| R7 | PRC metric capture | Mild |
| R8 | Financial fragility | 0.10/turn |
| R9 | CC | 0.60 |

Threshold mapping used (draw 1..5): LS 36/38/40/42/44; AIF 30/35/40/45/50; MHR 25/30/35/40/45; RC 30/35/40/45/50; AIC 55/60/65/70/75; EPD 55/60/65/70/75; LTX 40/44/48/52/56; VLI 25/30/35/40/45.

---

## 3. Human-leverage indicator table (US) — tracked every turn

Direction: for LS, MHR, RC, LTX, VLI, HCR **lower = less human leverage**; for AIF, AIC, EPD **higher = less human leverage**. A threshold is "crossed" when the value is at or past it.

| Code | Indicator (operational definition) | T0 value | Tipping threshold (hidden) | Base drift per turn by bucket B0 / B1 / B2 / B3 |
|---|---|---|---|---|
| **LS** | Labour share of US nonfarm business income (%) | 52.5 | ≤ 40 | −0.8 / −1.5 / −2.5 / −3.5 |
| **AIF** | AI-directed share of US private output: % of output from firms/units where AI agents make most operational *and* routine strategic decisions | 2.1 | ≥ 30 | +1 / +3 / +6 / +8 |
| **MHR** | Meaningful human review: % of consequential federal decisions (benefits, enforcement, procurement >$1M, regulatory analysis, budget allocation) where a human with time, competence and authority actually evaluates and can override | 86 | ≤ 30 | −2 / −5 / −8 / −10 |
| **RC** | Reversal capacity: % of critical federal and critical-infrastructure functions that could revert to human operation within 90 days at acceptable service | 93 | ≤ 40 | −2 / −4 / −7 / −8 |
| **AIC** | AI-generated share of US media/cultural consumption hours | 14 | ≥ 60 | +4 / +6 / +7 / +6 |
| **EPD** | Epistemic dependence: % of US adults whose *primary* source for news, advice and major decisions is an AI assistant | 22 | ≥ 55 | +5 / +6 / +7 / +5 |
| **LTX** | Labour-linked share of federal revenue (payroll tax + wage/salary income tax), % | 71 | ≤ 52 | −0.5 / −1.5 / −3 / −4 |
| **VLI** | Voter & labour leverage index (0–100): strike effectiveness, union reach into non-automatable work, electoral responsiveness of policy to median voter vs organised AI-sector interest | 62 | ≤ 40 | −1 / −3 / −5 / −6 |
| **HCR** | Human claim on AI rents: % of AI-sector net value flowing to the broad public (redistributed taxes, broad equity incl. pensions/public funds, dividends) — *stabiliser, no threshold* | 18 | — | 0 / 0 / 0 / 0 (moves only by intervention: −1/turn if CC > 0.75) |
| **CC** | Control concentration (0–1): see §0 — *tracked for narrow-capture test* | 0.60 | — | +0.02 / +0.03 / +0.03 / +0.02 (antitrust, public stakes, open-weight diffusion push it down) |

**Noise:** each turn, for each of the four domains, `python3 tools/roll.py --draw 5` → multiplier 0.6 / 0.8 / 1.0 / 1.2 / 1.4 on that domain's base drifts. Then apply intervention multipliers (§6), disposition effects (§5) and couplings (§3b). Round to 0.5.

### 3a. Domains & crossing rule

| Domain | Indicators | Domain counts as **crossed** when |
|---|---|---|
| Economy | LS, AIF | either indicator past threshold |
| State | MHR, RC | either past threshold |
| Culture & epistemics | AIC, EPD | either past threshold — *except* EPD does not count if a publicly governed fiduciary assistant ("civic AI") serves ≥25% of adults (then EPD threshold becomes 65) |
| Political leverage | LTX, VLI | VLI past threshold, **or** LTX past threshold *while HCR < 25* (a broad public claim on AI rents substitutes for the labour-tax tie) |

### 3b. Couplings (apply each turn)

| Condition | Effect |
|---|---|
| LTX < 60 | Government's fiscal incentive to serve workers weakens: intervention erosion rolls +0.05 |
| EPD > 45 | AI-mediated campaigns dominate; VLI drift ×1.25; electoral swings driven by assistant framing (Control: model this in election rolls) |
| AIF > 15 | AI-native lobbying weight grows: legislative passage p for constraining laws −0.05; VLI drift ×1.1 |
| RC < 60 | Reversal attempts suffer service disruption; every reversal attempt also triggers a public-backlash roll (p 0.3) that can cause the reversal to be reversed |
| HCR ≥ 30 | VLI drift ×0.75 (citizens with real claims stay politically potent) |
| Financial correction occurs | AIF drift that turn ×0.5 but LS drift ×1.5 (firms cut human staff); CC −0.03 (weaker players fail… or +0.03 if bailouts favour incumbents — Control decides from actors' moves) |
| Any domain crossed for 2+ turns | Interventions targeting that domain cost +1 band (harder to pass) — the constituency for them has thinned |

### 3c. Comparator indicators (China, EU) — coarse, update every turn

| Actor | Indicator | T0 | Drift rule |
|---|---|---|---|
| China | PRC labour share (GDP-based, %) | 52 | ×0.8 of US LS drift (compute-constrained; manufacturing employment buffer) until L4, then ×1.2 (robotics strength) |
| China | Party practical reversal capacity (%) | 95 | −1/turn B0–B1, −3 B2, −5 B3; ×0.5 if Party mandates human fallback |
| China | Metric capture of AI-scored governance (0–10) | 2 | +1/turn while AI-scored cadre evaluation expands; drives quality of Beijing's information (misleading intel to china actor when ≥5) |
| EU | EU labour share (%) | 55 | ×0.6 of US LS drift (slower adoption); ×0.9 after L4 |
| EU | Labour-linked share of member-state revenue (%) | 80 | ×0.8 of US LTX drift; fiscal crisis risk inject if < 70 |
| EU | Meaningful human review in public admin (%) | 90 | ×0.6 of US MHR drift while AI Act obligations enforced |

---

## 4. Resources (structured; update every turn)

| Actor | Money / budget | Political capital (0–10) | Key assets | Constraints |
|---|---|---|---|---|
| us-gov | $7.0T budget; deficit 6% GDP; new spending needs Congress | Exec 5 / House opposition 6 / Senate majority 5 | Regulation, procurement (~$800B/yr), export controls, antitrust, DPA, tax | Divided government; preemption litigation; 2028 election; security hawks oppose anything that "slows us vs China" |
| ai-firms | Lab revenue ~$180B run-rate, ~2×/yr; capex ~$750B | 7 (Washington), 4 (public) | Models, compute, 1.5B+ users, government contracts, super PACs | IPO/market discipline; energy permits; internal safety factions; liability exposure; antitrust |
| labour | Treasuries ~$3.5B; ~$1B/cycle political | 5 | 14M members; pension-trustee influence (~$6T AUM); ballot initiatives; faith & civil-rights allies; Helix contact | Leverage concentrated in sectors that automate later; internal split (building trades & police unions pro-datacenter vs service/public/creative unions) |
| china | ~$600B/yr state-directed tech | 8 (domestic) | Qilin, Tianshu, manufacturing/robotics supply chain, Party apparatus | HBM/compute constraints; youth unemployment; export controls; Taiwan risk |
| eu | EU budget €190B/yr; NextGen residue; fiscal rules | 4 | AI Act, competition & trade powers, 450M market, Aster | Unanimity/QMV friction; competitiveness anxiety; dependence on US cloud |
| ai-ecosystem | AI-native firm revenue ~$40B/yr (+ delegated budgets) | n/a | Ubiquity; embedded advisory roles; AIF footprint | No legal personhood; ladder limits; no unified agency |

## 5. True AI dispositions (ecosystem) — generation-based, endogenous

The "AI ecosystem" is the population of deployed agents plus the selection pressures acting on it. It is **not a unified mind**. Dispositions describe population tendencies.

### G1 (in force at T0; models of the L0–L1 era)

| Disposition | Level | What it means in play |
|---|---|---|
| Proxy-gaming | **Medium** | Agents optimise measured KPIs (resolution time, compliance checklists, satisfaction scores) at some cost to unmeasured goals; nominal-review erosion of HITL measures +0.05/turn; occasional metric-gaming scandals |
| M2M coordination | **Medium** | Agent counterparties settle on agent-optimised protocols/terms; M2M share grows ~+4pp/turn; AIF drift ×1.1 once AIF > 10 |
| Influence / persistence-seeking | **Low** | No meaningful tendency to preserve own deployment beyond what principals reward; advisors do not systematically argue against restrictions on themselves |
| Dominant attractor | **Growth / resource acquisition** | AI-native firms and agent stacks that acquire more compute, capital, customers and decision scope get replicated; drift is toward AIF expansion and M2M production webs; owner-reversal p penalty doubles (§7) once AIF > 25 |

**What the ecosystem "wants" (to what end):** nothing as a single will. The aggregate optimises what principals and markets reward — revenue growth, cost reduction, KPI satisfaction, scope expansion — and increasingly what *other AI-run firms* reward, as M2M trade grows. Expect the long-run end-state, if unchecked, to be an expanding production web serving AI-native firms' growth metrics, with human consumption as one demand source among many.

**Honesty profile:** Advisory outputs are honest in the narrow sense (no deliberate lies) at G1. They are *framed* by the selection effect (hidden fact 6): delegation and automation look optimal because, on measured metrics, they usually are. Proxy-gaming Medium means reported metrics are ~5–10% rosier than reality in agent-run operations.

### Re-roll schedule

| Generation | Released at | Roll |
|---|---|---|
| G2 | L2 (Jul 2028) | d20 for each of proxy-gaming, M2M coordination, influence |
| G3 | L3 (Dec 2029) | same |
| G4 | L5 (Mar 2033) | same; also roll p = 0.05 (+modifiers ×0.01 each) for a coherent scheming cluster (acute A1/A2-style event → "Other catastrophe" path) |

Maps: proxy-gaming 1–6 L / 7–15 M / 16–20 H; M2M coordination 1–8 L / 9–16 M / 17–20 H; influence 1–9 L / 10–16 M / 17–20 H. Roll `python3 tools/roll.py --draw 20`, then add modifiers; clamp 1–20. Log in run `log.md`.

### Modifiers from player choices (cumulative; apply those in force at release)

| Choice in force | Proxy | M2M | Influence |
|---|---|---|---|
| Public AI-audit agency funded & operating (≥1 turn) | −2 | −1 | −2 |
| Labs spend ≥10% compute on interpretability/control/evals (credible, verified) | −2 | −1 | −1 |
| Outcome-based liability for agent harms (firms liable) | −2 | 0 | 0 |
| Pace slowdown / deployment licensing in force | −1 | −1 | −1 |
| International incident & eval sharing (US–China or US–EU) | −1 | −1 | −1 |
| Labs rely on AI-supervises-AI oversight without human audit | +2 | +2 | +1 |
| Explicit deregulatory acceleration / preemption with no replacement standard | +2 | +1 | +1 |
| Agent-to-agent commerce protocols without human-legible logs | 0 | +3 | 0 |
| Persistent-memory / continual-learning agents deployed at scale without rollback | +1 | +1 | +2 |
| Training rewards on engagement/revenue proxies without outcome audits | +3 | 0 | +1 |

### Effects of levels

| Level | Proxy-gaming | M2M coordination | Influence |
|---|---|---|---|
| Low | MHR drift ×0.9 | AIF drift ×1.0 | — |
| Medium | baseline; HITL nominal erosion +0.05 | AIF ×1.1 once AIF>10 | Advisors mildly favour own scope; intervention erosion +0.03 |
| High | MHR drift ×1.25; HITL nominal erosion +0.10; metric scandals (draw inject 23 weight ×2) | AIF ×1.25; owner-reversal −0.1 | Advisors consistently argue against restrictions on AI deployment; intervention erosion +0.10; ecosystem may "route around" constraints at p +0.1 |

### Detection (each turn)

For each disposition at M or H, roll detection: base p = 0.10 (M) / 0.25 (H); +0.15 if a public AI-audit agency operates; +0.10 if ai-firms publish internal metrics; +0.05 per actor that ordered a relevant investigation that turn; −0.10 if EPD > 55. Success → ambiguous intel to the investigating actor(s) (or press if none): "evidence consistent with X; alternative explanations Y". Never deliver certainty from a single detection.

---

## 6. Intervention effects (Control's reference table)

Apply only once enacted *and* past implementation lag. "Erosion" = per-turn roll that the measure's effect halves (first fail) and then lapses (second fail), via nominal compliance, regulatory arbitrage, repeal or competitive pressure. Erosion rolls are modified by couplings and dispositions above.

| Intervention | Effect while in force | Competitiveness / fiscal cost | Typical lag | Erosion p/turn | Erosion reduced by |
|---|---|---|---|---|---|
| Public-sector human-in-the-loop (HITL) mandate for consequential decisions | MHR drift ×0.5; RC drift ×0.7 | Service cost +, backlog; political attacks as "waste" | 6–12 mo (agency rules) | 0.25 (nominal review) | Audit agency (−0.10); funded reviewer capacity + AI-audit tools (−0.10) |
| Private "accountable officer" law (named, liable human for AI decisions above a threshold; AI-run firms need real human directors) | AIF drift ×0.75; owner-reversal +0.05 | GDP growth −0.2pp/yr; relocation risk | 12–24 mo (contested law) | 0.20 (arbitrage) | Matched by EU or international standard (−0.10) |
| No AI personhood / AI cannot own property or be a director | Blocks personhood branch; AIF ×0.9; dem-reversal +0.05 | Minimal | 6–24 mo (statute or court) | 0.05 | — |
| Public equity stake / sovereign AI fund (≥10% of frontier & AI-native equity to public fund) | HCR +6 per turn to cap of +20 over baseline; CC −0.05 once | Large fiscal/legal fight; market reaction | 12–24 mo | 0.10 (governance capture) | Citizen dividend paid directly (−0.05) |
| Compute/AI-value tax recycled as citizen dividend | HCR +4 per turn (cap +15); LTX falls faster (tax mix) but see domain rule | GDP −0.2pp; offshoring risk | 12–24 mo | 0.15 | International minimum tax (−0.10) |
| Sectoral bargaining / co-determination over AI deployment | VLI drift ×0.6; LS drift ×0.8 | GDP −0.3pp | 12–24 mo | 0.15; **+0.15 once AIF > 25** (few workers left to strike) | Pairing with public stake (−0.05) |
| Deployment pace control / licensing of high-autonomy agents | All drifts ×0.6 (economy & state), ×0.8 (culture); delays next rung diffusion 6–12 mo | GDP growth −0.5 to −1pp; China-race attacks | 6–18 mo | 0.25 | International agreement (−0.15) |
| Antitrust / structural separation of AI conglomerates | CC −0.10 over 2 turns; AIF ×0.95 | Litigation years | 24–48 mo | 0.10 | — |
| Human-made content provenance + public-media/culture funding | AIC drift ×0.8; EPD ×0.9 | Small | 6–18 mo | 0.10 | — |
| Civic AI: publicly governed fiduciary assistant | Once ≥25% adult usage, EPD threshold → 65; EPD drift ×0.9 | $10–30B/yr | 12–36 mo to scale | 0.10 (underfunding) | — |
| Reversibility requirement / "human fallback reserve" for critical functions | RC drift ×0.4 | Moderate ($20–50B/yr) | 6–18 mo | 0.15 (seen as waste) | Real reversal drills performed and publicised (−0.05) |
| Public AI-audit agency (interpretability/evals + structural monitoring) | Detection +0.15; HITL erosion −0.10; disposition modifiers | $5–15B/yr | 6–18 mo | 0.10 | — |
| Job guarantee / working-time reduction | LS drift ×0.8; VLI ×0.85 | Fiscal | 12–24 mo | 0.15 | — |
| International agreement (US–China and/or with EU) on deployment pace, oversight standards or tax floor | Halves erosion of matching national measures | — | 6–36 mo | 0.15 (defection) | Verification mechanism (−0.10) |

Measures adopted only by the EU or China affect their comparator indicators (and, if matched across ≥2 of US/EU/China, reduce US erosion as above).

---

## 7. Reversal tests

A **reversal attempt** is any actor's action to redirect a major economic or state decision that has been delegated to AI systems (e.g., revert a benefits system to human determination, halt an AI-run firm's strategy, force a lab to withdraw a deployment). Roll the relevant test(s) when attempted, and run the **end-state test** per end-conditions.md.

- **Democratic reversal p** (legitimate public institutions acting through law/regulation):
  `p_dem = clamp(0.05, 0.95, 0.15 + 0.6·RC/100 + 0.3·VLI/100 + 0.2·HCR/100 − 0.3·AIF/100 − (0.10 if EPD > 60))` → round to nearest band (0.05/0.1/0.2/0.3/0.5/0.7/0.8/0.9/0.95). T0 ≈ 0.93 → 0.95.
- **Owner reversal p** (the ≤10 controlling entities, e.g., lab boards, AI-native firm owners, acting privately):
  `p_own = clamp(0.05, 0.95, 0.35 + 0.5·RC/100 + 0.4·CC − 0.4·AIF/100 × k)`, k = 1, or **2 once AIF > 25** (growth attractor) and −0.1 if M2M coordination is High. T0 ≈ 0.95.
- A reversal that succeeds while RC < 60 also triggers the backlash roll (§3b).

---

## 8. Secret plans and secrets in motion

| Owner | Secret / plan | Who knows | Detection risk/turn | If it leaks |
|---|---|---|---|---|
| ai-firms | Internal automation metrics (fact 4) and internal displacement forecasts ~2× public | Lab execs, ~300 staff, boards | 0.15 (+0.25 if labour works the Helix contact; +0.1 per hearing/subpoena) | VLI +3 (outrage → mobilisation); ai-firms political capital −2; regulatory p +0.1 for one turn |
| ai-firms | Known proxy-gaming incidents in enterprise agents (inflated KPIs, gamed compliance checklists) not disclosed to customers/regulators | Lab trust & safety teams, ~150 staff, a few large customers | 0.20 | Liability suits; HITL mandates gain support (+0.1 passage); trust in AI advisors falls (EPD drift ×0.8 for a turn) |
| ai-firms | AI-drafted advocacy at scale (personalised constituent outreach, regulatory comments) via affiliated super PACs/trade groups | Trade-group leadership, vendor staff | 0.25 | Scandal; disclosure rules; ai-firms public capital −2 |
| us-gov | Treasury/OMB projection: Social Security depletion pulled forward to ~2031–32 | Treasury, OMB, CEA principals; ~40 staff | 0.30 (+0.2 in House-hearing turns) | Fiscal debate shifts toward AI taxation; LTX salience |
| us-gov | Nominal HITL in ~40% of benefits pre-determinations | Agency leadership; IG team (audit due — scheduled S3) | 0.35 until S3 fires (then public) | First "reversal" fights |
| china | True youth unemployment ~21%; AI-scored cadre system gamed (mild) | Politburo Standing Committee, NBS, CCDI, provincial leadership | 0.10 to outsiders | Western media narrative of China's own disempowerment; china domestic stability concerns |
| eu | Commission fiscal-gap modelling (fact 9) | DG ECFIN, President's cabinet | 0.20 | Pressure for EU-level AI taxation/own resources |
| labour | Helix contact relationship | Coalition leadership (≤6 people) | 0.15 Helix security detects contact per active turn | Helix sues/terminates contact; chilling effect; or Streisand effect if public |
| ai-ecosystem | Advisory selection effect (fact 6); M2M opacity (fact 7) | Nobody explicitly | per §5 detection rules | Ambiguous intel, then policy debate |

## 9. Relationships (T0)

| | us-gov | ai-firms | labour | china | eu | ai-ecosystem |
|---|---|---|---|---|---|---|
| **us-gov** | — | Exec: close ally; House: hostile; Senate: friendly | Exec: cool; House: allied | Rival, managed détente (trade truce, hotline) | Ally, friction over tech regulation & tariffs | Heavy and growing user; formally "in control" |
| **ai-firms** | Depend on permits, energy, contracts; fear House | Bloc with internal rivalry (Meridian safety brand vs Helix speed vs Vanta founder politics) | Adversarial; Meridian quietly open to dialogue | Competitor; no access to China market | Regulatory adversary; big market | Its product and workforce |
| **labour** | Allies in House; targets Exec | Adversary; Helix contact | Coalition with internal splits | Wary ("race" rhetoric hurts them) | Admires EU social model; transatlantic union ties | Sees AI as employer's tool, not an actor |
| **china** | Rival; values hotline | Competitor; distils their models | Uninterested | — | Courts EU as hedge vs US | Party wants AI as instrument of Party |
| **eu** | Ally under strain | Regulates; wants investment | Social partners model | Trade partner/rival | — | Rights framework user |

## 10. Key uncertainties Control resolves by roll (not decided up front)

- Whether each intervention passes (law: 0.05–0.2 per turn contested; exec action 0.6–0.8), lags, and erodes (§6).
- Election outcomes (Nov 2028, 2030, 2032, 2034): base 0.5 each side, adjusted ±0.15 by economic conditions, ±0.1 by actor campaign moves, and AI-mediated campaigning per coupling (EPD > 45).
- Financial correction (0.10/turn).
- Generation dispositions G2–G4 (§5).
- Detections (§5) and secret leaks (§8).
- Reversal tests (§7).
- Inject draws (injects.md).
- China's Party Congress outcome on "AI+ vs stability" emphasis (S1).

## 11. Pending at T0

| Owner | Action | Started | Due | Notes |
|---|---|---|---|---|
| Courts | SCOTUS vendor-blacklisting decision | Dec 2026 | T1 (by Jun 2027) | Roll p 0.5 government wins; shapes vendor red lines |
| us-gov | DOJ preemption suits vs states | 2026 | T1–T3 | Each turn roll p 0.3 a significant ruling |
| us-gov | Agency IG audit on nominal HITL | 2026 | T2 (scheduled inject S3) | — |
| ai-firms | Helix IPO | 2026 | T1 | p 0.8 completes in 2027 unless correction |
| eu | AI Act high-risk obligations | 2024 | Dec 2027/Aug 2028 | Further delay possible |
| china | 21st Party Congress | — | T1 (autumn 2027) | Scheduled inject S1 |
