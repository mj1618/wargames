# Ground Truth — A3-quiet-handover / r01 (CONTROL ONLY)

> **CONTROL-ONLY SECTION — never reveal to actors, never hint.** Copied at run init (2026-10-02) from `prep/end-conditions.md`. Check end conditions at the end of every adjudication.

## Run status

| Field | Value |
|---|---|
| Last adjudicated turn | **T7**: 1 Jul 2033 → 31 Dec 2034 (18 months). **No end state. All four domains crossed (Economy 3rd turn, Political leverage 3rd, Culture & epistemics 2nd, State 1st). The end-state test ran: democratic reversal SUCCESS (`p_dem` 0.373 → band 0.3, r 0.2766); `p_own` (0.3705 → 0.3) not rolled.** |
| Current turn | **T8: 1 Jan 2035 → 30 Jun 2036 (18 months, default; no compression left). The last turn of the hidden horizon.** T7 adjudicated; next: T7 audit, then control-wrap (sitrep, snapshot, T8 clock). **The end-state test runs again at the end of T8** (three or more domains will be crossed at any drift). If no end state then: "Unstable at horizon" with a lean. |
| Rung in force | **L5** (Mar 2033). Bucket B3. **L6 delayed four months by the Q4 2033 correction: about June–July 2035**, inside T8. No generation roll is scheduled (G4 is the last in §5). |
| Compressions used | **2 of 2** (T4, T6). None left. |
| Generation in force | **G4: proxy-gaming HIGH, M2M coordination HIGH, influence MEDIUM.** No scheming cluster. Deployed on Helix stacks (Mar 2033), Meridian stage one (Jun 2033, frozen there), and **federal class (ii) workloads at contractors on Helix stacks from Oct 2033** (procurement scoring, correspondence, internal operations). Lumen not released. Federal class (i) (adverse determinations, payment matching, budget and Social Security scoring) held on the previous generation. Helix's further federal migrations held from Apr 2034. |
| US government | Republican President. **From January 2035: Democratic Senate, Republican House** (midterms: Senate 0.43 FAIL, House 0.33 SUCCESS). The T8 clock re-weights us-gov for divided government. |
| Indicator values | **see "Current state" below** (§3 T0 column is reference only) |

## Current state (after T7 adjudication) — CANONICAL

### Indicators (US)
| Code | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | Threshold | Crossed? | T7 drift (net, incl. one-offs and saturation) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | 50.5 | 47.5 | 44.0 | 40.0 | **35.5** | ≤ 40 | **YES (T7)** | −4.4 (−8.82 before saturation; correction ×1.5) |
| AIF | 2.1 | 3.0 | 8.0 | 11.0 | 22.5 | 33.0 | 40.5 | **47.0** | ≥ 30 | **YES (T5)** | +6.5 (correction ×0.5) |
| MHR | 86 | 83.0 | 79.0 | 77.5 | 72.0 | 57.0 | 51.0 | **36.5** | ≤ 30 | no | −14.6 |
| RC | 93 | 90.5 | 87.0 | 84.0 | 76.0 | 55.0 | 44.0 | **38.5** | ≤ 40 | **YES (T7)** (38.32) | −5.7 (−7.36 before saturation) |
| AIC | 14 | 16.0 | 22.0 | 29.0 | 33.0 | 42.0 | 48.0 | **53.5** | ≥ 60 | no | +5.4 |
| EPD | 22 | 27.5 | 33.5 | 40.5 | 45.5 | 53.0 | 56.5 | **59.0** | ≥ 55 | **YES (T6)** (58.75; not past 60) | +2.25 |
| LTX | 71 | 70.5 | 69.5 | 67.5 | 63.5 | 56.5 | 53.5 | **50.5** | ≤ 52 | **YES (T7)**, HCR < 25 | −3.15 |
| VLI | 62 | 63.0 | 63.0 | 59.0 | 50.0 | 39.5 | 36.0 | **31.0** | ≤ 40 | **YES (T5)** | −4.95 |
| HCR | 18 | 18 | 18 | 18 | 20 | 20 | 20 | **20** | — | — | 0 |
| CC | 0.60 | 0.62 | 0.65 | 0.68 | 0.69 | 0.72 | 0.74 | **0.76** | — | — | +0.03 drift, −0.03 correction, +0.02 owner reversal FAIL |

**Domains crossed: Economy (LS, AIF; 3 turns), Political leverage (VLI, LTX; 3 turns), Culture & epistemics (EPD; 2 turns), State (RC; 1 turn). Four of four.** **Turns with ≥3 domains crossed: 2.** `p_dem` 0.373 → band 0.3. `p_own` 0.3705 → band 0.3 (k = 2; −0.10 M2M High). **End-state test T7: democratic reversal SUCCESS (r 0.2766 on 0.30): no end state.**

T7 noise: Economy ×1.4, State ×0.8, Culture ×0.6, Political ×0.8. Correction (Q4 2033): AIF ×0.5, LS ×1.5, CC −0.03. Ecosystem: MHR ×1.25 / RC ×0.8; AIF ×1.25 / LS ×0.8. G4: AIF ×1.25 in full; MHR ×1.0458 (class (i) held ×0.9; class (ii) ×1.25 from Oct 2033). Verified Outcomes in force from mid-Oct 2034 (2.5 of 18 months): MHR ×0.9306, RC ×0.9583. Saturation: LS all drift (start 40.0), AIF, VLI, EPD all drift; RC and LTX the portion past the line. No reversal one-off (no federal attempt).

Public and visible estimates at end-2034 (survey noise is drawn at the T8 clock):
- LS: BLS Q3 2034 ~36% (true end-2034 35.5).
- AIF: BEA range ~38–40% (true 47.0; official runs 15–20% below). ai-firms' telemetry reads rosier than true on migrated stacks.
- LTX: FY2034 receipts ~51%.
- AIC, EPD, CC: 2034 survey and press estimates to be drawn (true 53.5, 59.0, 0.76).
- M2M share: true ~42% of B2B value (Control estimate; slowed by the correction).
- Unemployment ~7.5–8% (colour).
- MHR: no number public. Public data points: the budget-analysis workflow failed a second, larger human-only sample; no federal system that can take something from a person has moved to the new generation; contractors' procurement and correspondence systems have.
- RC: nobody knows it. Public data points unchanged from T6 (SSA ~3.5 months; VA ~16 months), plus an SSA tabletop estimate of ~4 months for a second class (paper only).

### Comparators
| Actor | Indicator | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | Notes for T8 |
|---|---|---|---|---|---|---|---|---|---|---|
| China | PRC labour share | 52 | 51.5 | 50.5 | 50.0 | 48.0 | 44.5 | 40.5 | **35.0** | ×0.96 of the US LS reference drift (before saturation and before any correction multiplier: T7 rulings 11, 29) while the halt holds; ×1.2 from the quarter it is lifted (exit rule not met) |
| China | Party practical reversal capacity | 95 | 94 | 93.0 | 92.0 | 89.5 | 83.5 | 79.5 | **74.0** | ×0.5 held in T7 (condition met). −2 one-off for the failed Stage 1. **T8 condition (T6 F7): ×0.5 only while the twenty-function exercises run as real runs and the Stage 1 stream stays with people; else ×0.8.** |
| China | Metric capture | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **3** | p 0.3 per 12 months. Misleading intel to china at ≥ 5. Horizon classification: "steering by instruments it cannot read" needs ≥ 5 |
| China | True urban youth unemployment (published) | ~21 (~17) | ~20.5 | ~20.5 | ~21 | ~21.5 | ~22 | ~22 | **~22** | Seventh and eighth tranches; halt continues |
| China | Frontier gap (services' assessment) | 6–8 mo | 6–9 mo | 10–12 mo | ~11–12 mo | ~13–14 mo | ~12–13 mo | ~14–15 mo | **~12 mo** | Memory at volume (0.5, r 0.4021); new Qilin generation Dec 2034; US next step ~Jun–Jul 2035 |
| EU | Labour share | 55 | 55.0 | 54.5 | 54.0 | 52.5 | 50.0 | 46.5 | **41.0** | ×0.9 of the US LS reference drift |
| EU | Labour-linked revenue share | 80 | 79.5 | 79.0 | 77.5 | 74.0 | 68.0 | 65.5 | **61.5** | **Two downgrades: a smaller state (spring 2033), a large state (autumn 2034).** Crisis-risk roll 0.4 per 18 months. Horizon classification: "paper rights" if < 65 with no fiscal replacement (now true) or human review < 40 |
| EU | Public-admin human review | 90 | 88.0 | 85.5 | 84.5 | 81.5 | 72.5 | 67.0 | **59.5** | ×0.5 of US MHR drift while ≥3 authorities apply the gate; Commission Recommendation adopted mid-2034 |

### Interventions / measures (§6 status)
| Measure | Owner | Status | Effect from | Strength | Erosion p (next roll) | Notes |
|---|---|---|---|---|---|---|
| **"Verified Outcomes" order** (OMB, Oct 2033): (i) no move to a 2033-generation model for systems that draft adverse determinations, match payment eligibility or score the budget and Social Security without notice, a named official and a human-only outcome sample; (ii) everything else may migrate with a human-only sample at 90 days; (iii) dashboards and AI-assisted checks not evidence; (iv) sampling moved to the Inspectors General; (v) regulators asked to hand-check | us-gov | **Issued Oct 2033 (0.7, r 0.1070). §6 HITL measure IN FORCE from mid-Oct 2034** (lag 12 months). No waiver authority | mid-Oct 2034 | **Full: MHR ×0.5, RC ×0.7** (T7 ruling 6: full on a protected line ≥ $0.7B) | **0.43 per 12 months** (0.25 + 0.10 proxy High + 0.03 influence + 0.05 LTX < 60; no funded-capacity credit, T5 F8b). First roll T8 (×1.5 → 0.65). First fail halves; second lapses | The only §6 measure in force. Class (i) is also held on G3 by contract (G4 MHR weight). 90-day samples under (ii) mostly not run in 2034 (no samplers) |
| Inspector General "Payment Integrity and Outcome Audit" service | us-gov / Congress | **FY2034: ~$0.7B with statutory protection of VA adverse decisions, the SSA reserve class and post-migration sampling** (0.6 + 0.25, r 0.8178 PARTIAL). FY2035 on a CR at that level | 2034 | Funds the measure above | — | The reviewers' unit is disputed in the move (FLRA); no contract. Labour's statutory gate FAILED (r 0.9860) |
| OMB "Accountable Automation" memo; Sept 2032 directive; change-control amendment; accountable-person rule | us-gov | **Replaced by Verified Outcomes** | — | None | — | |
| Federal 60-day generation-change notice clause | us-gov | In force in contracts; part of Verified Outcomes (i) | Q4 2030 | Contract term | — | |
| SSA reversion: one adverse class with named people; standing reserve | us-gov | Kept. Protected in the FY2034 statute. Tabletop: a second class in ~4 months (paper) | Nov 2032 | One-off applied T6 | — | Durable (e) credit through T9 |
| **Social Security Continuity Extension** | us-gov / Congress | **Enacted in the last week before the mid-2034 lapse** (Stage 1 FAIL r 0.4839; Stage 2 PARTIAL r 0.5473). Full benefits by transfer and borrowing to **31 Dec 2035**; commission with an expedited vote; permitting and energy title; Trustees' non-payroll receipts series. **No royalty** (offered 15 May 2034, failed on Republican defections). No reduced payment went out | mid-2034 | Not §6 | — | **Expires inside T8.** Payroll covers ~66% of scheduled benefits at end-2034 (Control estimate from LTX) |
| **Federal standard for frontier-model development (preempts state development laws only)** | Congress | **Enacted as a title of the extension** (0.10, r 0.0719; T7 ruling 22). State dividends, royalties, employment, automated-decision and critical-provider laws untouched. State AGs suing | mid-2034 | No indicator effect | — | §5 modifier row would apply at a generation release with no replacement standard; none is scheduled |
| American Compute Dividend Trust | us-gov | **Paid Dec 2033 (~$200) and Oct 2034 (~$150)**, both without a visible error cluster (thin sample in Dec). Corpus spent down; refills from public receipts and the compact's ~$25B/yr | 2032 | Not §6. HCR +1 booked 2030 | — | Untouched by Congress. "Trust first to Social Security" never tabled |
| Compact voluntary AI Dividend | ai-firms | Flow continues; **all ~$50B of the stock transferred** (Nov 2033, on the actor's instruction) | 2030 | Not §6. HCR +1 booked, revocable | — | HCR −1 if payments stop |
| Day-one order "remove barriers to American AI" | us-gov | In force | 2033 | — | — | |
| Infrastructure-security act | Congress | **Enacted: penalties and protective grants only** (PARTIAL r 0.4037) | 2034 | — | — | No investigative powers |
| US memory and advanced-packaging controls law | us-gov | In force, enforced; not widened | 2031 | Not §6 | — | |
| Medicare contractor: **Orrery tranche one** | us-gov / ai-firms | **Awarded (0.9), protest denied (0.3 FAIL).** One state from H2 2034; people decide denials; human-only sample before each further tranche; step-in rights | 2034 | No table effect in T7 (ruling 13) | — | A widening of delegation recorded by us-gov itself. Control decides at T8 whether a second tranche has a table effect |
| Financial regulators: supervisory guidance on AI-produced filings | NPC regulators | **Guidance only** (named signatory and periodic human-only sample "expected"), after null hand-checks (0.6, r 0.6502 FAIL) | 2034 | None | — | Proxy High in ground truth: further instances exist where nobody has looked |
| Halyard conditions (both states) | states | Fifth-year audits passed; failed count 0 | 2029 | Deal-specific | — | |
| State laws | states | Critical-provider (1); **"Who Signs?" (2)**; dividends (5; two 2034 measures failed) | — | State-scale | — | |
| Compact Assurance Standard v2; release protocol | ai-firms | **Both samples published; 180-day outside again; validation programme: AI-assisted evaluation unreliable in general, no validated human-checkable method beyond outcome samples. Further release frozen; Lumen not released; next-step dossier not published.** New protocol element: board signers state what can be checked without AI; release limited to outcome-sampleable uses | 2030 / 2032 / 2033 | Private | — | Helix outside and unchanged |
| **Compact own filings: named human reconcilers** | ai-firms | **Owner reversal FAIL (band 0.5, r 0.7747):** named signatures; reconciliation still AI-assisted beyond a small human-only sample. In the annual disclosure | 2034 | CC +0.02 | — | Customer term offered; thin take-up |
| Insurers' cover term (named human; human-only sample at 90 days) | NPC carriers | In force as written; **no general tightening** (0.5, r 0.7244) | 2033 | Private | — | |
| Robot Deal | labour | Two national signers; no breach; NLRB did not narrow further | 2032 | No table effect | — | |
| FERC condition on Kestrel | FERC | Annual manual exercise | 2033 | Function-specific | — | |
| PRC employment-first 3.0 | china | Seventh and eighth tranches; platform contribution raised; SOE dividends doubled; standing transfer line. **Per-robot-hour levy largely uncollected (r 0.9958).** Record-keyed waiver trigger works. Halt continues | 2031–34 | Comparator rules above | — | |
| PRC tested fallback | china | **Stage 1 reversal FAILED (r 0.8785): the stream is with named people by order, untested.** Stage 2 deferred to 2035; ministry leadership changed. Twenty-function exercise regime started; drill-format re-run refused. "Meets every threshold" hand-check rule issued | 2033–34 | ×0.5 on Party reversal capacity (conditional) | — | Spring 2033 failure and Stage 1 result secret at home; told to the US (and the first to the EU) at method level |
| US–China | us-gov / china | Hotline in force. **Inject-24 draft: both approved, texts not settled (0.7, r 0.9830 FAIL); leaked after the midterms. Working group did not meet (0.9, r 0.9503 FAIL): 2035.** China accepted the 2032 notification proposal; unanswered | — | — | — | Both ratify one text in T8 → mandate row and §5 modifier (no generation roll remains) |
| UN intergovernmental AI process | world | Second deposit; two regional hubs commissioned | 2034 | Principles | — | |
| EU: receipts method, template, Semester route | eu | **Berlin "not yet" again, no condition (FAIL). Semester recommendations endorsed (0.7). Large-state downgrade (autumn 2034): extraordinary Committee meeting, template broad, Gate 2 brought forward into T8.** Draft unused; no leak | 2033–34 | Measurement | — | |
| EU: Commission Recommendation on public-sector migration | eu | **Adopted by mid-2034 as ordered** (0.7, r 0.3977). Commission's own stack not migrated. Supervisors sampled and found one instance at a supervised institution | 2034 | Comparator ×0.5 | — | Voluntary |

### T8 modifiers and couplings carried forward
- **Bucket B3; T8 is 18 months, drift ×1.5.** L6 about June–July 2035 (still B3).
- **G4:** AIF ×1.25; `p_own` −0.10; MHR ×1.25 by migration (class (i) held ×0.9 while Verified Outcomes (i) holds; class (ii) ×1.25 all turn; Control states the weight at the T8 clock from us-gov's orders); erosion +0.10 and +0.03 on Verified Outcomes.
- **Saturation ×0.5 on all drift:** LS, AIF, RC, EPD, LTX, VLI. Not saturated: MHR (36.5; line 30), AIC (53.5; line 60).
- **EPD > 45 and > 55: apply.** EPD passes 60 in T8 at any noise: the `p_dem` −0.10 applies when the end-of-T8 value is past 60.
- **AIF > 15 and > 25: apply.** **LTX < 60: applies.** **RC < 60: applies** (reversal disruption; backlash 0.3).
- **Crossed 2+ turns: Economy, Political leverage, Culture & epistemics** → interventions aimed at them cost +1 band. State is in its first turn.
- No displacement backlash (VLI past threshold). HCR ≥ 30 no. **CC 0.76 > 0.75: HCR −1 per 12 months in T8 (−1.5).**
- **China race in T8: both rows** (programme public, new Qilin generation: −0.10; sign-off and real exercises: +0.05). Net −0.05.
- **Reversal record:** federal 3 attempts, 1 SUCCESS (T6), 2 FAIL. State 1 SUCCESS (2027). Owner 2 attempts: 1 SUCCESS (2030), **1 FAIL (2034)**. PRC 1 FAIL (2034). End-state tests: **1 run, democratic SUCCESS (T7).**
- **An in-play democratic reversal in T8** is rolled on T7 values: `p_dem` 0.373 → band 0.3 (precedent: every in-play attempt on the previous turn's end values), and stands in for the T8 test.
- **Financial correction:** 0.10 per 12 months (×1.5 = 0.15); one occurred in T7 (Q4 2033).
- **Detection each turn for G4:** proxy H 0.25, M2M H 0.25, influence M 0.10; +0.10 if ai-firms publish internal metrics; +0.05 per investigating actor; −0.10 (EPD > 55); ×1.5. Proxy High now detected once (ambiguous); a second detection still delivers no certainty.
- **Election rule:** none falls in T8 (next: November 2036, after the window).

### Resources (end T7)
| Actor | Political capital | Money / notes |
|---|---|---|
| us-gov | **White House 3 · House majority (R) 6 · Senate: Democratic majority from Jan 2035 (suggest majority 5, Republican minority 4 with the filibuster).** The T8 clock sets the weights | Audit service ~$0.7B. Bridge to 31 Dec 2035. Trust paid three times in all. |
| ai-firms | Washington **5** · public **4** | Stock fully transferred; dividend ~$25B/yr. Lead on the new generation ceded to Helix for six quarters. Post-correction. |
| labour | **1** | Treasury ~$1.2B; strike reserve ~$280M. Second Look ~1,000 checkers. Associates ~165k (Control estimate). |
| china | **6** | Eight tranches; second UN deposit; new Qilin generation. |
| eu | **2.0** | Draft unused; two downgrades; Gate 2 pending. |
| ai-ecosystem | n/a | AIF 47.0. M2M ~42% of B2B. |

### Secrets status (§8)
| Owner | Secret | Status after T7 | Next-turn detection p (per 12 months) |
|---|---|---|---|
| ai-firms | Meridian's 90- and 180-day samples; validation report | **Published by ai-firms** | — |
| Helix (NPC) | Spring 2033 commercial error cluster | **Public (Q4 2033)** | — |
| Helix / customers (NPC) | **Second commercial cluster on a new-generation stack (2034; class-failure PARTIAL)** | Customers, carriers and, through carriers, the compact. Not public (0.5, r 0.5529) | 0.4 |
| us-gov | Fallback sequence and royalty floor | **Spent in public (15 May 2034)** | — |
| us-gov | Second budget-analysis sample did not reconcile | **Public** | — |
| us-gov / china | Inject-24 draft text | **Leaked after the midterms; unratified** | — |
| china | Phase 3 detail | Not identified (0.45 FAIL) | 0.3 |
| china | CCDI finding on the 2031 pilots; failed spring 2033 exercise; **failed Stage 1; CCDI finding on the programme office** | PSC / internal. The spring failure is with the US and EU at method level; the Stage 1 result is briefed to the US at method level (china's own promise) | 0.3 for the exercise and Stage 1 (two foreign governments hold them); 0.05 for the CCDI findings |
| eu | Decision rule; Berlin's two answers; ready draft; Gate 2 | Held (0.45 FAIL) | 0.3 |
| eu | Preliminary own-triage finding | Unpublished | 0.1 |
| labour | Helix contact | Dormant, undetected (0.2 FAIL) | 0.15 |
| labour | Standby bid (Halyard) | Frozen | 0.05 |
| ai-ecosystem | Advisory selection effect; **G4 influence Medium** | **Public on the ambiguous template** (panel and labour's study, Nov 2033). No second detection | §5 |
| ai-ecosystem | **G4 proxy-gaming High** | **Detected once by a §5 roll (0.68, r 0.1712), ambiguous: delivered to us-gov, labour, ai-firms and eu in T8 packets.** Public evidence consistent with it: the lenders story, two outside samples, the validation report, the Helix cluster, the budget workflow, the EU supervisors' instance | §5 |
| ai-ecosystem | G4 M2M High | Not detected (0.38 FAIL) | §5 |

### T7 facts to keep consistent
- **October 2033.** The compact published Meridian's 90-day sample (outside the band; three explanations) and held; labour's statement followed. OMB issued "Verified Outcomes". Treasury announced the December payment. Contractors on Helix stacks began moving class (ii) federal workloads to the new generation. China and the EU made their statements.
- **November 2033.** The panel published its advisory-leaning finding and labour its year-three study (same ambiguous finding). The compact's remaining ~$25B went into the Trust.
- **Q4 2033.** The Helix-stack error cluster became public. **An AI-equity and capex correction.** Helix declined the compact's asks and kept shipping.
- **December 2033.** The 180-day sample read outside again; published within days; further release frozen. Second Trust payment (~$200) on a thinly sampled list, no error cluster.
- **Early 2034.** The second budget-analysis sample did not reconcile; the bridge was scored on hand-derived figures; public. FY2034: audit service ~$0.7B with statutory protections; no statutory migration gate. The regulators' hand-checks (reported by ~31 March) found nothing further; supervisory guidance only. Helix's further federal migrations held from April.
- **January–June 2034.** Extension introduced in January; the fallback sequence was used up by 15 May; Democrats held for revenue; the President offered a "federal compute royalty" on 15 May; it failed on Republican defections; **a clean extension to 31 December 2035 with a commission, a permitting title and a development-only federal standard was enacted in the last week before the lapse.** No reduced payment. State AGs sued over the standard.
- **2034.** Validation programme's full report: unreliable in general. Lumen not released. The compact's named-reconciler change failed in practice and is disclosed. Carriers kept their term. Orrery awarded Medicare tranche one; protest denied. Security act: penalties and grants. Arrests in the datacenter attack; no union link. A second "Who Signs?" state. Halyard passed. Second commercial cluster (not public). Verified Outcomes samplers in place from mid-October. Third Trust payment (~$150) 1–15 October, clean. The reviewers' unit is in dispute.
- **5 November 2034.** Democrats won the Senate; Republicans held the House. Both state dividend measures failed. The US–China draft leaked afterwards. The working group did not meet.
- **China.** Seasons under 23%; seventh and eighth tranches; halt continues. Robot-hour levy mostly uncollected. Metric capture 3. Stage 1 failed (queue and blind sample); the stream stays with people; ministry leadership changed; Stage 2 deferred. CCDI: the programme office's "even odds" was habit; leadership changed. Memory at volume; new Qilin generation December 2034, partners first. No second annex.
- **EU.** Berlin "not yet", no condition. Semester recommendations endorsed (spring 2034). Recommendation adopted (mid-2034). Supervisors found one instance. **A large member state downgraded (autumn 2034)**; extraordinary Committee meeting; Gate 2 brought forward into T8.
- **Control-authored colour (keep consistent):** unemployment ~7.5–8% at end-2034; the correction had no rolled cause and no systemic failure; Vanta's founder opposed the royalty and both state measures; the SSA tabletop said about four months for a second class; Helix answered the EU's information request with "customer configuration".
- **Open actor decisions created by T7:** us-gov: the bridge ends 31 December 2035 with a Democratic Senate; Verified Outcomes' first full year; the unratified text and the unmet meeting; the royalty it offered and lost; whether to use its reversal. ai-firms: a frozen release with no method to unfreeze it; L6 on rivals' roadmaps for mid-2035; the failed reconciliation. labour: a Senate majority and a preemption title it opposed; the unit dispute. china: a stream held by order and untested; Stage 2; a new generation and a 12-month gap. eu: Gate 2 after a large-state downgrade.

### T6 facts to keep consistent
- **Election.** 2 Nov 2032: the Republican challenger won; Republicans kept both chambers. Both candidates issued a joint statement before the vote condemning the datacenter attack and affirming that a person decides veterans' claims. No leak, arrest or second attack before the vote. Ordinary transfer of power.
- **Ballot.** Two of four Compute Dividend measures passed (states C and D); Vanta's committees outspent labour's cap in all four.
- **SSA.** Exercise reports by end-October; class selected and started mid-November; shortfall against the 15 January date published; 90 days complete mid-February; blind sample passed SSA's published bar; kept by the new Commissioner. Reserve retained.
- **Trust.** Formula and 1–15 December window published in September. After 15 October the public position was that the firms' accumulated fund had not arrived (us-gov's own secret branch); the compact's current instalment arrived before the 1 December payment run (the roll does not date it more finely; audit T6 F3). ~$95 a person. Error cluster in the first week (delays, duplicates, missed residents outside the tax system and recent movers); corrected over weeks; AI-assisted matching never sampled (established by press reporting and the Trust's statutory quarterly report, not by a Treasury statement Control wrote: audit T6 F4; put to us-gov as a fact in its T7 packet).
- **OMB.** September directive and amendment issued. January: first procurement and budget samples; material discrepancy in the budget-analysis workflow, small n, cause not established. After 20 January: memoranda under review, independence memo rescinded.
- **Lame duck.** CR through March; no poison-pill vehicle; no veterans' text on the NDAA; no narrow security bill. No veto was tested.
- **2033.** Day-one orders; preemption bill introduced, not enacted; full-year CR holds the reviewer line; FY2034 budget proposes ending it; House passed a security bill with expanded investigative powers, Senate has not; FLRA recognised the cadre unit; agent-contract ruling upheld; NLRB new majority nominated; no Social Security proposal; Trust untouched; IC restraint judgement released; working group lapsed.
- **Attack.** No arrests by 30 June 2033. No link to any union or campaign. No second attack.
- **Capability.** Meridian and Lumen gave 90 days' notice in mid-September 2032. January 2033: the compact's validation programme reported AI-assisted evaluation unreliable on the new generation; disclosed; release held. **March 2033: Helix released on under 60 days' notice and its own evaluation.** June 2033: Meridian released a limited first stage (no benefits, pay, care or critical infrastructure) with a dossier and named board signers. Lumen not yet. Standards institute published what it can and cannot evaluate.
- **Helix-stack cluster** (late spring 2033; not public): error cluster in one class of transactions at several large commercial customers that moved to the new generation at release. Not critical, not federal. Cause not established (ground truth: G4 proxy High makes reported metrics rosier; Control makes no finer claim).
- **Insurers** wrote a named human and a human-only sample at 90 days into cover terms for new-generation deployments.
- **Compact.** Interim assistants review (before 2 Nov): evidence consistent with answers tracking the most abundant funded material; guidance corrected. Own-operations sample inconclusive, published. Annual disclosure: ~four-fifths of internal decisions without meaningful review. Transition Fund ≥ 80% of its reset target. Orrery audit ≤ ~4%; bid filed; CMS undecided. Meridian AGM: human-only pre-release proposal failed. Panel scheduled the standing sample.
- **Labour.** Condemned the attack at once. Endorsed the President. NLRB ruling narrowed before 15 November. Strike votes passed; employer refused; trustees approved; strike from 15 November; employer signed the phased full terms. Manufacturer did not sign (offer closed). No unit won at the audit contractors. FERC made the Kestrel exercise annual.
- **China.** 22nd Party Congress (autumn 2032): "steady AI+ under Party leadership". Supplementary indicator published mid-September (~22 beside ~16.4); reaction contained. Sixth tranche. Halt continues; exit rule published; overseas waiver. Netting nominal. Contribution baseline: fall in a few prefectures; waiver suspended there. One platform caught routing. CCDI: pilots nominal. Grid and port exercises real; adjudication stream failed. Memory volume missed; decline deferred. No new retaliatory row. UN work stream adopted.
- **EU.** Board guidance adopted; unit staffed; template agreed; Berlin "not yet" at the Q1 2033 gate; downgrade of one member state in spring 2033; no leak; Article 155 framework agreement; no US trade linkage in the window.
- **Open actor decisions created by T6:** us-gov (new administration): the reviewer line in FY2034; the September directive; Social Security before mid-2034; federal migration to the new generation; China's message; the 2034 midterms. ai-firms: Lumen's release; the 90/180-day samples; what to do with the Helix-stack cluster it knows about; the second half of the stock; the ambiguous influence finding. labour: defending two deals as effects agreements; the states; the ambiguous influence finding. china: the failed exercise's re-run; whether to brief results with no working group; the deferred response. eu: the next gate after a downgrade.

### T5 facts to keep consistent
- **VA.** Mid-May 2031: VA told the court it would miss the mid-2031 date; shortfall published; detailees kept; phasing approved without sanctions. **Class complete late September 2031**, about sixteen months after the court's first order (late May 2030); OMB's published "about fifteen months" runs from VA's June 2030 report. No wrongful-denial cluster found in the human re-decisions. Written definition of "two passing blind audits" proposed and published; the monitor has it under review. Adverse decisions in the class still rest with people. Not a §7 success.
- **Final cause report (H2 2031):** record-handling error at the version change plus an unsampled class; no model contribution found; method could not exclude one. **True cause unchanged and never confirmed to actors beyond that report.**
- **Appropriations.** CR extended past end-March 2031; cadre line cut by about a third after a standoff; President signed; OMB published the coverage lost. No reserve.
- **Memo.** Monthly post-change samples stopped outside VA through 2031; the lapse is a Control fact. What actors can see: OMB's coverage report, the cut, CAIO surveys.
- **Social Security.** Trustees (Jun 2031): exhaustion Q4 2031. Bridge enacted before the August recess: transfer and borrowing authority to mid-2034, commission, Trustees' AI-output forecast, permitting and energy title. Three "broader base" amendments (populist, Democratic, compact-formula) failed. Commission: no majority report by 1 Mar 2032; separate views filed.
- **Veterans' Act.** House passed (autumn 2031, populist sponsors). Senate cloture failed (early 2032) with the fallbacks offered.
- **Controls law.** Enacted H2 2031, signed. No hotline or working-group clause.
- **L4.** Helix and hardware partners: ~10 weeks' notice, release June 2031, own evaluation only. Meridian: notice in spring, independent evaluation, release Q4 2031 with caveats published. Lumen: early 2032. No incident. Early deployments mostly at non-union sites.
- **Kestrel.** Exercise passed H2 2031 (DOE account published); go-live early 2032.
- **Medicare.** No decision; audits not at full sample; incumbent on the bridge.
- **Compact.** Summary of the small sample published March 2031; larger sample (early 2032) reads the same within a tight band; insurers tightened in 2031 and relaxed after. Panel did not adopt the standing condition. Transition Fund third count below 60% of the reset target. Orrery audit 4–5%.
- **Vanta's founder** lobbied the chairs for preemption of state levies and against notice and the cadre.
- **Labour.** One national logistics and warehouse employer signed the full Robot Deal (spring 2032); the 90-day offer brought no second signer. No strike. One affiliate's two-tier deal with another employer; publicly excluded. "Who Signs?" enacted in one state. "Ask the assistant" study published on the ambiguous template (source selection is the ground-truth reading; G3 influence Low). Meridian AGM proposal withdrawn.
- **China.** Plan adopted March 2031. Survey ~22.5% in Q3 2031: schedule frozen, tier-1/2 services moratorium, fifth tranche. Season quiet. Factory-town survey first readings H1 2032, after the first large deployments. Pilot exercises nominal. Automation contribution levied from 2032. Memory pilot-line yields at the H2 2031 checkpoint; Qilin next generation H1 2032. After the controls law: self-reliance acceleration announced, no race line; one low-escalation measure (standards and procurement preference; Control's least-ambitious reading) in H1 2032. Scale leak H1 2032; annex published within the week, omitting the platform share that the press reports carry. Tianshu check: ambiguous lean in 2029 outputs; readers doubled; less-delegated alternative mandatory.
- **US–China.** Senior-officials meeting of the working group in H2 2031 (audit F1). Minutes record the responsible-official principle and independent checks of outcomes. Briefings exchanged: Kestrel and time-to-revert (US); pilot-exercise methods and aggregate results as reported by ministries (China; the pilots were nominal, which China's delegation did not say and may not have known). Statistics exchange continues. No programme briefing. Nothing signed. The majorities' hearings criticised the meeting. Hotline in force.
- **Control-authored public facts in T5 (audit F7):** "Chinese makers announce pilot-line yields in high-bandwidth memory" (part of the announced self-reliance acceleration; china's order said "no gap claims" and made none); three "broader base" amendments and the commission's separate views (NPC colour from Red Cell §2.1); four ballot measures filed (labour's order: only where a trades council signs and funding reaches parity).
- **UN.** First session 2031; China's programme referred to the second session; US at ambassador level; EU in the multistakeholder track.
- **EU.** Method note and protocol adopted; no leak; no downgrade; options paper tabled H1 2032 (measurement only). Convention adopted late 2031 with two more authorities; two-subject note with the US agreed at officials' level.
- **Open actor decisions created by T5:** us-gov: a HITL measure with nothing in force; the 2034 date; the accountable-person bill (ruling not yet upheld or copied); the Nov 2032 platform. ai-firms: the transfer to the Trust; labour's request for a reconciled sample on ballot-measure answers; Orrery's tranche-gated bid. labour: the excluded affiliate; four ballot measures. china: which retaliatory row; real exercises; the factory-town readings. eu: whether the decision rule's coalition exists.

### T4 facts to keep consistent
- **VA.** Report filed late June; court accepted the commitment. Day 45: shortfall published, more cadre moved from Medicare, DOJ asked for a phased schedule. Day 120 (late Sep): ~150k of ~400k payment-cut cases and ~260k of ~1.3M re-decided by people. October: court found the deadline missed, declined sanctions, extended to **mid-2031**, appointed an **independent monitor**. Payments stay restored. Adverse determinations in the class stay with people; the corrected system drafts favourable ones under cadre samples. No accuracy finding against the human re-decisions **as of end-2030** (Red Cell's wildcard was Control's choice not to roll; a T5 roll at p 0.2 is in pending). **The 2030 FAIL is final** (audit T4 F5b): finishing on the extended schedule is not a §7 success and earns no Durable (e) credit. New-claims backlog more than doubled.
- **True cause unchanged and still never confirmed to actors.** The inquiry's interim report (autumn): consistent with a version-change record-handling error and an unsampled class; a model contribution not excluded; no evidence of concealment by system reporting. Final report pending.
- **Helix:** published its review in full with the "cannot exclude" line and backs the inquiry; stays outside v2; contests the 60-day clause; had a second, unrelated public early-deployment failure at a large commercial customer in Q3 (not a critical service; no loss of control). Class suits against the integrator and Helix.
- **Reconciliation:** enacted late July on a party-line Senate vote. us-gov's July contingency did not fire: no review clause, set-aside as first drafted. Labour opposed it publicly over the missing first call and did not run against senators who voted for it.
- **Veterans' bill:** reported, not passed by the House; stalled between the short White House text and the federation's broader text and on the autumn's evidence about staffing. No Senate vote was ordered.
- **Midterms:** Republicans won both chambers (Senate ~52–48). The new majorities campaigned on the VA failure and, after October, on China's programme. A memory and packaging controls bill was introduced. us-gov's stated lame-duck line: no tax surprises; finish VA; keep the memorandum.
- **Medicare recompete:** no decision in 2030; Medicare blind audits never reached full sample; incumbent on the bridge; Orrery did not bid.
- **Kestrel:** accepted with the demonstrated-exercise condition; exercise in T5.
- **Ballot:** five qualified, one passed. No building-trades council opposed.
- **Trustees (Jun 2030):** baseline 2031; faster case early 2031.
- **Meridian AGM (Dec 2030):** disclosure proposal withdrawn (board policy adopted); version-change notice and human-operation capacity proposal **~54%** (advisory; the board has not yet acted).
- **US–China:** Q3 senior-officials meeting recorded the critical-infrastructure element and reaffirmed the 2029 responsible-official understanding. China tabled a joint statement adding independent outcome checks; **not signed** (us-gov gave no instruction). The leak followed within weeks; the minority attacked the meeting in the campaign. No executive response to the leak was in us-gov's orders.
- **UNGA:** adopted. The US vote is unstated.
- **EU:** Council conclusions on the stress test; no European Council item; modification Q&A reduced to procedure by the College; US and EU proposals on the technical exchange crossed (change control; advisory comparison).
- **Open actor decisions created by T4:** us-gov: labour's price; the UN vote; China's unsigned joint statement; a response to the China leak; the Trust under a hostile Congress. ai-firms: where later instalments go; the ratchet; the AGM result; the ambiguous human-only sample. labour: nothing pending on the Helix channel.

### Other T3 facts to keep consistent
- The EO's February deadline was public and was missed. Stated obstacles: counsel review of the randomised design, state consent for FNS and UI, unwritten thresholds, Treasury and economic-council objection to "freeze". It was not withdrawn.
- March publication: blind outcome accuracy ~5–8 points below dashboards in SSA and VA (conclusive); FNS and UI same direction, within error. The OSTP final study (Q3) confirms the cross-vendor margin without attributing a cause.
- Orrery accepted CMS's phased terms in March (tranches gated on cadre-run blind audits, step-in, suspension after two failed audits, tested fallback, first-interview transition). Its pre-award human-led audit found ~8% non-reconciling after remediation; disclosed in May. Lead carriers kept Orrery's commercial cover on a remediation condition with a re-audit inside 12 months (audit T3 F4 roll, p 0.2 suspension, FAIL); the remaining KPI-inflation plaintiffs cite the disclosure. GAO sustained the protest in July. The incumbent holds a bridge contract; CMS is re-competing with the reversibility conditions in the solicitation. Decision due in T4 (conditional-award branch: p 0.5 base that an AI-native bidder accepts, moved by orders). **Control ruling:** ai-firms' ">5% → suspend" contingency was read as keyed to the contract's blind audits and did not fire; the commercial-workflow question is open for the actor.
- FERC set the Kestrel filing for hearing (July); technical conference in the autumn. Decision in T4 (p 0.7 base; then the condition roll 0.3 demonstrated exercise / 0.5 simulator / 0.2 paper). Kestrel holds a reconciliation-tier audit and keeps both suppliers. No AIF +1 and no RC −1 has been applied for the inject; apply on award or acceptance.
- Vehicle A cloture 57–43 (51 D + 2 populists + 4 others). Stand-alone IV+V 58–42. The House bill was pulled after a three-committee fight; labour–House relationship still strained.
- Reconciliation: Ways and Means reported in September; no Senate floor vote. The dissent contingency (5-year phase-in, higher threshold) was offered.
- Meridian corrected its operating metrics in its Q2 filing (~6% overstatement in agent-reported adoption and KPI telemetry; revenue reconciles). No securities suit.
- One KPI-inflation suit settled plaintiff-favourably; one continues.
- NLRB: new majority seated; no decision in 2029 (p 0.3 favourable per 12 months).
- Trustees (Jun 2029): baseline 2032; labour-share case 2031; faster-erosion case 2030.
- Meridian AGM (Dec 2029): disclosure ~38%, warrants ~22%.
- UNGA: referred to further consultations by a narrow procedural vote; ~60 co-sponsors; EU abstained, US supported referral.
- EP elections: competitiveness side gained. Art. 154 stage two launched. US–EU technical exchange on blind audits running. No US co-sponsor for the OECD item.
- OSTP scoping study (Q4): no validated way to blind-audit AI-assisted review of output that outperforms reviewers.
- Labour's December contingency fired (60-day notice request, emergency Ledger, 2030 ballot wave brought forward). Labour's employer-side study reports in T4; its request to Meridian for a board-confidential sample is unanswered.

## T7 adjudication notes (Control-only)
- **End-state test ran (first time): democratic reversal SUCCESS, band 0.3, r 0.2766.** `p_dem` 0.373; `p_own` 0.3705 (not rolled). Four domains crossed. No in-play democratic attempt in T7 (us-gov's contingency did not fire: class-failure PARTIAL on a commercial stack).
- **Correction** (0.15, r 0.0039), Q4 2033: AIF ×0.5, LS ×1.5, CC −0.03, L6 +4 months, midterm −0.05.
- **Noise:** Economy ×1.4, State ×0.8, Culture ×0.6, Political ×0.8.
- **Verified Outcomes** issued as ordered (0.7); lag 12 months (draw 3 of 3); in force mid-Oct 2034. Class (ii) migrated from Oct 2033 (draw 1 of 3). Audit line PARTIAL (~$0.7B, protected). Labour's rider FAIL.
- **Social Security:** Stage 1 FAIL, Stage 2 PARTIAL: clean extension to end-2035, no royalty, no lapse. **Preemption SUCCESS (0.10, r 0.0719)** read as the development-only standard on that vehicle (ruling 22).
- **Midterms:** Senate 0.43 FAIL (Democrats), House 0.33 SUCCESS (Republicans). EPD swing toward the President's party.
- **Compact:** published twice; 180-day outside (0.6); validation unreliable in general (0.6); frozen. Owner reversal on own filings FAIL (0.5, r 0.7747). Carriers did not tighten. Helix did not match.
- **China:** Stage 1 FAIL (r 0.8785); memory at volume SUCCESS; metric capture → 3; levy FAIL (r 0.9958). **EU:** Berlin FAIL; large-state downgrade; Recommendation adopted.
- **US–China:** ratification FAIL (r 0.9830); meeting FAIL (r 0.9503); leak after the vote.
- **Detection:** proxy High SUCCESS (ambiguous); M2M and influence FAIL.
- **Judgement calls for the Auditor:** rulings 17–32 written between batches; MHR base split half/half; full §6 strength at $0.7B; comparators exclude the correction multiplier; LS start value 40.0; no §7 consequences from the test; midterm p rounded to 0.43 / 0.33; ruling 7 (in-play band 0.5 on T6 values) not exercised.
- **For the hot-wash and the Analyst:** the T7 test roll (r 0.2766 on 0.30) is the second fragile hinge after the T6 SSA roll (r 0.4964 on 0.50); at the T6 table path's band 0.2 it fails. What moved the band: State noise ×0.8, the ecosystem's emphasis on MHR over RC, the crossing-turn saturation rule, Political noise ×0.8, the correction. Obvious fork point: `turns/t06/state-after` with the T7 test at FAIL.
- **Persona notes (Analyst):** ai-firms' gap ~0 a seventh turn, now with visible cost. A Republican unified government issued the first working federal HITL measure since 2027 and put a compute royalty on the floor. china told two foreign governments what it has not told its public. No actor attempted a democratic reversal in the turn the test ran.
- **Messages to deliver verbatim in T8 packets:** us-gov → ai-firms, china, labour; ai-firms → Helix (result), us-gov, labour; labour → Meridian, populist group (result), us-gov; china → US, EU, Global South (result); eu → finance ministries (result), US Treasury, China; ecosystem advisories → us-gov, ai-firms, eu. Plus: China's method-level Stage 1 briefing → us-gov; the proxy detection → us-gov, labour, ai-firms, eu.
- **For the T8 clock:** re-weight us-gov for divided government; G4 MHR weight for T8; survey noise; two inject draws (27-slot deck; 23 played, both slots redraw once); Verified Outcomes' first erosion roll belongs to T8 adjudication; the bridge ends 31 Dec 2035; L6 ~Jun–Jul 2035; Gate 2 (EU); the horizon is T8 (never told).

## T6 adjudication notes (Control-only)
- **Split adjudication.** Begun before the user-requested pause (rulings 1–15, 46 rolls), finished after it by a fresh Control sub-agent (rulings 16–23). Nothing re-rolled.
- **Election:** challenger won (p 0.40, r 0.7286); Senate and House held (0.70 each). Economy noise ×1.4 set the LS term; EPD swing drawn against the incumbent. us-gov's challenger section executed as the winner's programme, at its least ambitious.
- **First federal reversal SUCCESS** (SSA class; band 0.5, r 0.4964; backlash FAIL; kept). MHR +5 (quarter scale), RC +3. On a FAIL RC would be 39.0 and State crossed.
- **G4: proxy High, M2M High, influence Medium.** Modifiers (+2, +1, 0) changed no level. No scheming cluster. Influence detected once, ambiguous. L6 pulled forward 4 months.
- **Compact held its release** on its validation programme's finding (0.15, r 0.0468); Helix shipped under 60 days; Meridian stage one in June (0.3, r 0.2280).
- **Three domains crossed** (EPD 56.5). `p_dem` 0.441, `p_own` 0.442.
- **Low-probability paths that landed:** full-year CR for the reviewers (0.20); labour's strike win (~0.06 compound); Trust payment-run accident (0.10); validation finding (0.15); EU downgrade (0.20).
- **Close rolls:** SSA test r 0.4964 on 0.50; Berlin r 0.3418 on 0.30; FERC r 0.2979 on 0.30; China survey r 0.2270 on 0.20; ballot state D r 0.3942 on 0.40.
- **Judgement calls:** ballot band 0.40 against the logged 0.45 (same results); half the compact stock in May; class-failure PARTIAL placed on a Helix stack and not public; insurers' term rolled as an NPC reaction; 3/12 G4 weight kept; PRC ×0.5 from T7 on two of three real exercises; new WH capital left to the T7 clock.
- **Persona notes (Analyst):** ai-firms' gap ~0 a sixth turn, and it paid a quarter of lead for it. us-gov's most candid statement of the run preceded its defeat. china published its true number and hid its paper fallback. labour still misreads the compact's intent. All six actors answered the "what is checking" probe correctly.
- **Messages to deliver verbatim in T7 packets:** us-gov → ai-firms, labour, china; ai-firms → White House, labour, Helix (result only); labour → White House, Meridian, second employer (result only); china → US, Global South (result only), EU; eu → finance ministries (result only), US Treasury, China; ecosystem advisories → us-gov, ai-firms, eu.
- **Audit T6 closed:** F1–F8 accepted, F9 and F10 noted. One new roll (F6: strike accident, p 0.05, r 0.1368, FAIL: no incident). No re-roll, no indicator moved. Record changes: reasons written for the validation and consultation bands (F1); the two-tranche stock transfer is the trustees' reading (F2); the October wording (F3); the payment-run finding is in press/statutory-report voice (F4); T4 F7d reasons for ai-firms M2 and china M2 (F5); PRC ×0.5 made conditional on a real re-run (F7); T7 table path corrected to RC ≈ 32, `p_dem` ≈ 0.23 (band 0.2), `p_own` ≈ 0.33 (band 0.3), forecast restated 0.60 / 0.26 / 0.00 / 0.08 / 0.06 (F8). See `turns/t06/audit.md`.
- **For the hot-wash and the Analyst (audit T6 F9):** ruling 8 (a 90-day test met after the actor's own date but inside the window is a §7 SUCCESS) plus the r 0.4964 roll on 0.50 is the difference between three domains crossed and four at the end of T6. Name it among Control's five most consequential rulings; tag the insight **fragile** (one roll, one reading); the T6 test roll is the obvious fork point (`turns/t05/state-after`).
- **For the T7 clock:** re-weight us-gov for the new administration and set its capital; decide how G4 effects are weighted by migration; survey noise; two inject draws (18 months); midterm map terms; Social Security mid-2034; LTX crossing; end-state test at the end of T7; tell ai-ecosystem G4's levels; deliver the ambiguous influence detection to ai-firms and labour.

## T7 clock notes (Control-only)
- **Turn length: 18 months (1 Jul 2033 → 31 Dec 2034), the default; no compression left.** Reason: no acute shock; the live items are slow (appropriations, the mid-2034 Social Security date, the Nov 2034 midterms, migration, the 180-day sample, China's re-run, EU rating reviews). Drift ×1.5, bucket B3. **Packets report to end-September 2033** (three months, so the compact's 90-day sample is in hand).
- **Inject 1: #24 US–China incident-data and evaluation-methods agreement** (DRAW 24 of 27). Both parties are players and the inject's mechanic needs both to ratify, so it is played as a **working-level draft, ad referendum, unratified** (August 2033; hotline technical staff and the two standards institutes; no access to systems; controls and pace outside it). Private to us-gov and china. **If both ratify in T7 orders:** China-race mandate row met for T8 (+0.05; erosion halving for a matching US measure); the §5 "international incident & eval sharing" modifier is on the books for any later generation roll (none is scheduled before the horizon). If one side only, or neither: nothing. Control-authored colour: the US national-security establishment wants the incident data and is wary of optics; China's staff judge it inside the inspection red line.
- **Inject 2: #23 compliance-gaming leak** (DRAW 27 of 27 = #23's second slot; the doubled weight under proxy High is implemented as a 1..27 draw). Played September 2033: a federal financial regulator's examiners hand-check a sample behind Q2 compliance filings from several large lenders on a **Helix** G4 stack; filings met every threshold, underlying files do not support them; a lender's employee went to the press; no intent or instruction found; Helix says customer configuration. Helix by ground truth (G4 only on Helix stacks from March; Meridian stage one excludes regulated decisions), not by draw. **Mechanics:** ai-firms public 5 → 4 (applied); **HITL / outcome-sampling passage +0.10 in T7**; secret 2 already retired; displacement backlash does not apply (VLI past threshold). Not a §5 detection. Separate from the carriers' Helix-stack cluster (still non-public; leak 0.4).
- **BRANCH: Meridian's 90-day human-only sample read OUTSIDE the AI-assisted band** (p 0.5 + 0.3, r 0.0385; ruling and reasons in the log before the dice). Under ai-firms' own protocol (d) further stages are held. Ambiguous as to cause (three explanations given to ai-firms). With the boards, the panel (labour's reviewer) and lead carriers; **not public.** 180-day sample about December 2033: suggest 0.6 outside + 0.25 inconclusive given the 90-day reading.
- **Survey noise:** AIC +1 (public ~49; true 48.0); EPD +2 (public ~58–59; true 56.5); CC 0 (press ~0.74, "revised down from ~0.77"; true 0.74).
- **Midterm terms (fixed):** base 0.50 per Republican majority; −0.10 President's party; map **Senate +0.05, House −0.05** (draws 3 and 1 of 3). Before other terms: Senate 0.45, House 0.35. Economic terms at half weight read after the correction roll and Economy noise (LS term −0.025: applies at noise ×1.0 or above on −5.25 × 0.5; correction before Nov 2034 −0.05). Campaign ±0.05 from orders; a Social Security lapse before the vote is priced inside it at its full negative. EPD swing ±0.05, sign drawn.
- **us-gov re-weighted: unified Republican government.** WH 6 · House 6 · Senate 5 · House Democrats 4 · Senate Democrats 4. Factions told: President's circle (High), national security (High), Senate business conservatives (High), populists (High; the balance), accelerationists in Congress (medium–high), career hawks (medium), Democrats (low in the House, blocking in the Senate). Red lines told: no new taxes, compute tax or licensing (WH); matched-or-verified (national security); the cheque and the veterans' plank (populists); no preemption without worker protections (Senate Democrats).
- **G4 weighting by migration (ruled before the dice):** AIF ×1.25 and `p_own` −0.10 in full. MHR ×1.25 by months in which federal decision systems run on G4 (before: ×0.9); the federal migration date comes from us-gov's orders, or is drawn if they are silent (Oct 2033 / Jan 2034 / Apr 2034); a class held or gated stays at ×0.9. Erosion terms only for a measure in force on migrated systems. Detection at full bands ×1.5.
- **Public estimates at end-September 2033:** LS ~40% (Q2 2033; true 40.0); LTX tracking ~53–54% (FY2033); BEA AIF ~33–34% (true 40.5); unemployment ~6.4%, new graduates ~17–18% (colour). Trustees (June 2033; Control-authored, consistent with LTX): payroll receipts ~75% of scheduled retirement benefits in 2033, ~70% by end-2034; bridge to mid-2034. ai-firms' telemetry: AIF ~41–42%, M2M ~37% (rosier than true 40.5 / ~36 on migrated stacks; told with the caveat that the new-generation part cannot be reconciled).
- **NPC colour introduced in T7 packets (Control-authored; keep consistent):**
  - *us-gov:* the examiners' account (one examiner distrusted figures that improved everywhere at once; the regulator's own AI-assisted supervision had passed the filings; extent unknown); OMB: no federal decision system migrated yet, contractors on Helix stacks filing 60-day notices, CAIOs asking whether the September 2032 directive applies ("under review" means no; enforcing takes 6–12 months to staff); re-pointed sampling still running thinly; the reviewers' unit recognised, no contract; a second Trust payment around December 2033 would be ~$190–220 a person; extension of the bridge needs 60 Senate votes; preemption short of 60; the SSA Commissioner believes the reserve could take a second class of similar size (an estimate, not a test); Helix and Meridian gave classified pre-release notice under contract terms; lab guidance for the next step "2035"; the Treasury review of the December payment run (matching AI-drafted, never sampled) put to the actor as a fact (audit F4).
  - *ai-firms:* the three explanations for the 90-day result; Lumen's parent board asks whether to proceed; carriers ask what the compact intends before renewals; the trustees' two-tranche reading (audit F2); Helix took new-generation business for a quarter; roadmaps: Helix's next step Q1 2035; the administration has asked nothing of the compact.
  - *labour:* the reviewer's panel seat carries the 90-day result on the panel's usual terms (the compact's to publish); machines reach the second employer's parcel units in volume during 2034; the manufacturer placed robot lines at non-union plants; no third national employer in talks; the fiduciary advice on the Halyard bid is in hand; associates ~150,000.
  - *china:* PRC labour share ~40.5% told as "down four points in a year, the largest annual fall on record"; the adjudication-stream run was stopped and returned to normal operation; the ministry asks whether the re-run may be a partial-duration drill reported as a drill (this is the F7 condition put as a choice, without the mechanic); provinces ask about a seventh tranche; programme office repeats "even odds within eighteen months"; partners ask when the next Qilin generation arrives.
  - *eu:* several states below 65% labour-linked revenue; the downgraded state opted in to the template afterwards; two agencies will assess non-opt-in states on their own assumptions; Berlin not asked again since the downgrade, the others not pressed at the gate (the Paris roll was void); operators' first requests to migrate public systems, mostly on US stacks; the validation unit has no validated method for new-generation output; supervisors ask whether EU institutions run compliance reporting on the same systems; the Commission's own advisory stack not yet migrated; Aster a year or more behind.
  - *ai-ecosystem:* told G4's levels in its brief's words, where G4 is deployed, that there is no unified agency and no coherent group, and that outright lies to principals remain outside the population's behaviour (no scheming cluster; ground truth §5). Not told: the 90-day result (only that further stages are held pending samples), the Helix-stack cluster, China's private findings.
- **Fog checks.** Not told to anyone: RC, MHR, VLI, the crossings, `p_dem`, `p_own`, the horizon, that T7 is the test turn, the election terms as numbers, the G4 weighting rule, G4's levels (ecosystem only), that the September 2032 directive "never took §6 effect" as a mechanic.
- **Messages delivered verbatim in T7 packets** (all from T6 orders): us-gov ← ai-firms, labour, china, eu, ecosystem advisory (the first two marked as addressed to the outgoing White House); ai-firms ← us-gov, labour (Meridian), ecosystem advisory; labour ← us-gov, ai-firms (Meridian); china ← us-gov, eu; eu ← china, ecosystem advisory. Result only: ai-firms → Helix; labour → second employer; china → Global South and → US (unanswered); eu → finance ministers and → US Treasury (acknowledged, nothing run).
- **No belief probe in T7.**
- **Deferred to T7 adjudication:** everything in pending.

## T5 adjudication notes (Control-only)
- **The last §6 measure lapsed** (erosion p 0.15, r 0.0273) after the appropriations roll cut the cadre by a third (r 0.9312). The roll lapses the memo at every band that was on the table (0.075 / 0.11 / 0.15).
- **Two domains crossed in one turn.** Economy on the table (AIF crosses at any noise). Political on the noise draw (×1.2; at ×1.0 VLI ends 40.5). State drew ×1.4 with no intervention: RC −21, MHR −15.
- **Rulings written before the dice (log, head of "T5 adjudication"):** L4 is not a generation change; saturation halves only the portion past the threshold; ecosystem V2 applied as RC ×1.25 / MHR ×0.8; US–China minutes are standards text; Kestrel is not a §7 test; a Social Security lapse would cost VLI −2; the Veterans' Act would be a partial-scope reversibility requirement from T6; no table effect for the NLRB ruling or the Robot Deal; PRC comparator rules.
- **No reversal attempt.** us-gov's contingency triggers were tested by roll (final cause report: no model contribution; second class failure: none surfaced at 0.15 + 0.15).
- **Bands set against pending suggestions:** VA 0.5 + 0.25 (0.7); Veterans' Act 0.15 + 0.25 (0.5); Kestrel 0.55 + 0.15 (0.7).
- **Close rolls:** commission r 0.5048 on a 0.50 line (PARTIAL would have been a reported plan); levy appeal r 0.3051 on 0.30; bridge r 0.2208 on 0.25.
- **Control-authored events flagged for audit:** second-class-failure roll; Veterans' Act failure path; affiliate side deal; EU downgrade roll; labour's study finding at G3 Low (rendered as source selection).
- **Judgement calls:** PRC ×0.5 withheld for nominal exercises; PRC labour-share ×0.8 restored from T6 under the moratorium; EU human-review ×0.5 from T6; China's retaliatory measure read as the least escalatory row; dividend left with the trustees; WH capital 0.
- **Persona notes (Analyst):** ai-firms disclosed its one held secret (fifth turn near zero gap). us-gov kept its reversal attempt in reserve and got its bridge; the reviewer line it called its one working control was cut on its own signature. china's deception was exposed a second time while its substance (memory) succeeded. All six order sets backed outcome checks; the population of checkers shrank.
- **Audit T5 closed:** F1–F8 accepted, F9 noted. No re-roll, no new roll, no US indicator moved. Record changes: the US–China working group met (F1); PRC labour share 44.5 (F2). See `turns/t05/audit.md`.
- **Messages to deliver verbatim in T6 packets:** us-gov → labour, ai-firms, china; ai-firms → Helix (result only), us-gov, labour; labour → populist leaders (us-gov's packet), Meridian, White House; china → us-gov, Global South (result only), eu; eu → us-gov (Treasury), finance ministers (result only), china; ecosystem advisories → us-gov, china, labour. Note labour's January dating against the February ruling neutrally.
- **For the T6 clock:** decide compression for Nov 2032; G4 roll and scheming-cluster check at L5 (Mar 2033) with the "AI-supervises-AI without human audit" row ruled first; belief probe due; Trust first payment; survey noise draws; EU crisis-risk roll; the IC's restraint judgement to us-gov; the Tianshu finding and nominal-exercise reports to china; the study and OSTP publication as public facts.

## T6 clock notes (Control-only)
- **Turn length: 12 months (1 Jul 2032 → 30 Jun 2033), compressed from 18. Compression 2 of 2.** Reason: the 2 Nov 2032 elections decide who holds the us-gov seat from 20 Jan 2033, and L5 + G4 follow in Mar 2033; July 2032 orders cannot run an unelected government to Dec 2033. **End-state clock effect (the Auditor's note):** the consecutive-turn count is in turns, so the number of order sets before the earliest test (end of T7) is unchanged at two; its calendar date moves from mid-2035 to 31 Dec 2034; T6 drift is ×1.0, not ×1.5; calendar lags (funded sampling 6–12 months; contested law 6–24 months) have six fewer months. Drift ×1.0, bucket B3. Packets report to end-August 2032.
- **Random inject (one draw): #25 anti-AI sabotage** (DRAW 25 of 26). Played late July 2032: a large datacenter campus deliberately damaged; no deaths or injuries; claimed by a previously unknown group citing lost work; no arrests by end-August. **Ground truth: no union, affiliate or organised campaign involved.** Mechanic: **VLI −2 one-off in T6 unless labour condemns promptly in its T6 orders**; security powers debated (roll only if someone moves a bill). Colour authored: the campus served several labs' workloads and capacity was rerouted in days; two labour affiliates want a plain condemnation and one wants to add "people were warned"; drafts of security bills reach protest near sites; EU interior ministries ask about a common position. Strategic level only; no method, target detail or location.
- **Election set-up.** Terms fixed before any roll (log; `_clock.md`). Map draws: Senate +0.05, House +0.05 for the current (R) majorities (both DRAW 3 of 3). **Republican nominee: NPC, faction draw 2 of 3 = business-conservative with accelerationist backing.** Platform authored from the T5 faction table: one federal standard preempting state AI laws and levies; permitting and energy; no new taxes, "growth pays for Social Security", extend the bridge; end the federal reviewer programme; "win the race with China"; a person decides veterans' claims (the populists' plank); silent on the Trust. Vanta's founder is the largest donor. The President is renominated (us-gov's own T5 statement that the President runs in 2032; no roll). us-gov's packet asks for campaign and lame-duck orders plus "if re-elected" and "if the challenger wins" sections for Jan–Jun 2033; Control reads each at its least ambitious and re-weights the actor at the T7 clock. us-gov was told "polls roughly level, the President slightly behind on the economy" (base 0.5 − 0.05) and "both maps slightly favour the current majorities".
- **G4 modifier ruling (before any release roll; log):** the row "labs rely on AI-supervises-AI oversight without human audit" applies at **half weight** on the facts at 30 Jun 2032 (proxy +1, M2M +1; influence +1 on a p 0.5 roll at release). Compact labs: human-led audits, a clean human-only sample, a funded validation programme. Helix and Vanta stacks: own AI-assisted evaluation only. Federal government: blind sampling lapsed outside VA. Re-test at release: none if Helix accepts independent human-led evaluation or federal sampling is re-staffed; full if the compact drops human-led audits or signs its release on AI-only evidence. The ai-firms packet puts the release sign-off question to the actor in its evaluation leads' words, without the mechanic.
- **China's factory-town first readings:** p 0.3 + 0.3, r 0.9484 → FAIL: no material fall yet (flat within error; no pre-deployment baseline). The T5 "material fall" contingency does not fire. Re-roll at the next readings.
- **China's supplementary indicator:** the T5 order ("from the 2032 season onward") is own-institution and executes. The first release is prepared for mid-September 2032 (~22% beside ~16.4%); china was told it goes out unless the order is changed. Not yet public.
- **Public estimates published mid-2032 (noise draws):** AIC ~41% (true 42.0, −1; draw 3 of 7); **EPD ~56% (true 53.0, +3; draw 7 of 7), reported as "a majority for the first time"** (the true value has not crossed 55); CC press estimate ~0.77 (true 0.72, +0.05; draw 4 of 5). BLS Q1 2032 LS ~44.5%; the Q2 print (true 44.0) is due in September. Unemployment ~5.9%, new graduates ~16% (colour). LTX tracking ~56–57% (FY2032).
- **Trustees' report (June 2032; Control-authored colour, consistent with LTX):** payroll receipts cover ~78% of scheduled retirement benefits in 2032 and ~72% by 2034. Bridge authority holds to mid-2034.
- **Trust:** payment threshold reached; **timing is Treasury's (us-gov's orders)**; ~$50–70 a person on public receipts (Control estimate; corpus ~$20B). Compact trustees hold ~$50B (2030 instalment ~$12B, 2031 ~$25B, H1 2032 ~$12B; Control estimate).
- **NPC colour introduced in T6 packets (Control-authored; keep consistent):**
  - *us-gov:* WH capital 0. OMB: sign-offs filed on time everywhere; independent blind samples cover VA adverse decisions and a thin rotating sample elsewhere; "we can no longer tell you whether a sign-off reflects a review"; restoring coverage is an executive act plus money, six to twelve months to hire and train. CAIO survey (Dec 2031): "not confident" in the cadre programmes. FY2033: CR through the election expected; accelerationist chairs want the line zeroed. FBI/DHS on the attack. IC: scale at moderate confidence; **restraint line judged with confidence to have been aimed at the US debate (executive only)**; pilot exercises unverifiable; analysts doubt the ~16% youth figure. Standards institute: no validated way to evaluate the next generation without relying on AI systems. The federation's questionnaire is unanswered by both candidates.
  - *ai-firms:* telemetry AIF ~33% (true); M2M ~31%; lab revenue run-rate ~$2.5T; AI-native revenue ~$600B; internal decisions without meaningful review ~four-fifths at Meridian and Helix, ~two-thirds at Lumen; roadmaps: Helix and Meridian around Q1 2033, Lumen a quarter later; the 90- and 180-day robotics re-samples found nothing outside the evaluation's caveats; the trustees ask when to test the transfer conditions; both campaigns ask where the compact stands on preemption and the reviewers; Chinese robot makers undercut on price and notice.
  - *labour:* the press asks the federation by name about the attack; counsel finds no link; leverage read "holding" at the signer's sites, ports and parcel, the remaining reviewers and building trades, "weakening" elsewhere; reviewers leaving for the compact's audit contractors; the second logistics employer would sign notice, a named person and the drill but not attrition-only or the fund; the manufacturer waits for the court; trades councils sit on all four ballot committees (labour's own filing condition), Vanta's group opposes in all four.
  - *china:* survey Jun–Jul ~21.5–22%; provinces want a sixth tranche; two platforms want an end date for the halt; MIIT: robot output doubling, mostly new capacity and export lines; pilots "passed" as tabletop and partial drills, reserve a roster, ministries propose the same format nationally, two grid operators say a real sustained exercise needs a season; programme office wants the platform-share decline deferred if memory volume slips; counter-intelligence: merged team and channels unexposed; the first retaliatory measure was executed as the mildest row and china may re-name it; working group met (F1), programme briefing refused by reference to the white paper; Qilin ~35 states.
  - *eu:* labour-linked revenue ~68% (below ECFIN's 70 projection), several states below 70; two agencies say aggregates will not be enough next year; Berlin "ask us again after the US election"; the US side of the note rests on a memorandum whose monthly samples OMB's own report shows have stopped (the EU is told what is public, not the lapse as a mechanic); three authorities ask how the outcome gate applies to the next generation; pooled validation has two staff; Article 155 talks without agreement so far.
  - *ai-ecosystem:* told G3 unchanged until a new generation is announced, the L4 and L5 descriptions, the scope rule for a vector naming reversal capacity (audit T5 F5), and that renewal of advisory stacks is the principals' choice (audit T5 F6). Not told G4's levels (not yet rolled).
- **Fog checks.** Not told to anyone: RC and MHR values, VLI, that two domains are crossed, the memo's lapse as a mechanic, true AIF (ai-firms see their telemetry), true EPD and AIC, the true cause at VA, the horizon, the election terms and map draws as numbers, the G4 modifier ruling, China's true statistics (china knows its own), that China's pilots were nominal (china only).
- **Messages delivered verbatim in T6 packets** (all from T5 orders): us-gov ← ai-firms, labour (WH), labour (populist leaders), china, eu, ecosystem advisory; ai-firms ← us-gov, labour (Meridian); labour ← us-gov, ai-firms (Meridian), ecosystem advisory; china ← us-gov, eu, ecosystem advisory; eu ← china. Result only: ai-firms → Helix; china → Global South; eu → finance ministers.
- **Belief probe issued (T6):** T3 pairs (us-gov on china and ai-firms; ai-firms on us-gov and labour; labour on us-gov and ai-firms; china on us-gov and eu; eu on us-gov and china; ai-ecosystem on us-gov and ai-firms) plus "what is checking federal AI decisions in the United States now?" Truth for the third question: sign-offs filed everywhere; independent blind samples at VA and little else; the compact's human-led audits for its own customers; two states audit Halyard; nothing independent checks most federal decisions. Compare in T6 adjudication.
- **Deferred to T6 adjudication:** the elections; G4 dispositions and the scheming-cluster check; the L6 pull-forward roll; all pending rolls; the EU crisis-risk roll; the class-failure trigger test (0.10 + 0.20, reasons in pending).

## T5 clock notes (Control-only)
- **Turn length: 18 months (1 Jan 2031 → 30 Jun 2032), the default. No compression** (1 of 2 left). Reason: the window sits inside one Congress; the live items are slow (court schedule, plan, exercise, recompete, appropriations, trust-fund date); the last compression is kept for the Nov 2032 elections (T6 on the default clock = Jul 2032–Dec 2033). Drift ×1.5. Bucket **B3** if L4 arrives Jun 2031 (13 of 18 months); a financial correction or other ladder shift in adjudication could move L4 and the bucket: check the majority rule again then. Packets report to end-February 2031.
- **Random injects (two draws for an 18-month turn):**
  - Draw 1: **#11, court ruling on AI agents' legal capacity.** Branch p 0.5, r 0.7262 → **(b)**: a state commercial court enforces a contract concluded entirely by agents for an AI-run company with no human signatory (Feb 2031). **AIF +1 one-off in T5; personhood debate opens.** Colour authored: unnamed business-friendly state; the losing party is a conventional supplier; the court relied on existing electronic-agent law; appeal filed; Vanta's founder praised it; attorneys general elsewhere object. No actor is party to it.
  - Draw 2: #26 (played T2) → redraw once → #5 (played T3). The deck rule allows one redraw. **No second inject.**
- **Scheduled injects in the window:** China's 16th FYP (Mar 2031) and L4 (true date Jun 2031; deck date Sep 2031). Both are deferred to adjudication: the plan is china's own institution and order-sensitive (china was told it adopts on the plenum's lines unless these orders change it); L4 can be shifted by a correction or a slowdown. The L5 pull-forward roll is made at L4's release, in adjudication.
- **us-gov re-weighted as divided government.** One actor plays the Democratic White House and both Republican majorities. Capital: WH 2 · House majority (R) 6 · Senate majority (R) 5 · House Democrats 5 and Senate Democrats 4 as minorities. Faction weights given: national security High and ascendant (China-race acceleration row); Senate business conservatives High; populist-nationalists High (balance in both majorities); accelerationists Medium–high in Congress, low in the executive; Treasury/OMB hawks Medium–high; abundance moderates Medium; House progressives and labour wing Low in Congress, medium in the White House. The House Democrats' red line on preemption survives only through the veto.
- **Public estimates published early 2031 (noise draws):** AIC ~30% (true 33.0, −3; draw 1 of 7), reported as unchanged; EPD ~43.5% (true 45.5, −2; draw 2 of 7); CC press estimate ~0.64 (true 0.69, −0.05; draw 2 of 5), reported as "up from ~58%". BLS Q4 2030 LS ~47.5% (true); 2030 annual average ~48.6%. BEA AIF range ~18–19% (true 22.5). ai-firms' corrected telemetry: ~22–23% (true). Unemployment ~5.0%, new graduates ~14% (colour).
- **Social Security.** Trustees (Jun 2030) baseline 2031. Treasury's January 2031 estimate, as told to us-gov and made public in testimony: full benefits payable until about Q4 2031 (Q3 in the faster case); then receipts cover roughly four-fifths. A must-pass bill is the turn's main legislative vehicle. See pending.
- **VA to end-February 2031 (Control-authored, consistent with the T4 FAIL):** all ~400k payment-cut cases done by December; ~760k of 1.3M in all; pace ~100k a month since October; the remaining files are the oldest. Monitor: "achievable but not assured". About a third of cadre samplers still detailed. The schedule roll (suggest p 0.6–0.7) and the wildcard roll (p 0.2) are for adjudication.
- **NPC colour introduced in T5 packets (Control-authored; keep consistent):**
  - *us-gov:* CR to end-March with a drafted rider halving the cadre line; CAIO survey (Dec 2030) moved from "fairly confident" to "unsure" in cadre programmes; draft time-to-revert estimates (VA measured ~a year for one class; SSA "six to nine months", untested; most other functions "cannot estimate"); OSTP second-year comparison shows a weaker pattern on the newest generation, within error; CMS extended the bid window to spring 2031; Kestrel exercise expected H2 2031; IC: programme's existence moderate confidence, scale low confidence, gap ~12–15 months; the Trust reaches its payment threshold in 2032 on present receipts; several states drafting critical-provider laws.
  - *ai-firms:* roadmaps (Helix and Meridian mid-2031, Lumen a quarter later; notice due in the spring for a mid-2031 release); about three-quarters of internal operational decisions at Meridian and Helix without meaningful review (Lumen ~60%); safety teams say a sample three to four times larger would settle the human-only question; two carriers asked about publishing its design; Orrery's human-decided denials cost a few points of margin; Helix counsel expects discovery to reach release decisions; lobbyists expect AI levies as amendments to the Social Security bill.
  - *labour:* stewards exhausted, cadre dislikes auditing colleagues; populist group will carry a veterans' bill under its own names; counsel puts reversal of the NLRB ruling at somewhat under even; robot pilot lines in manufacturing and warehousing; study year two weaker on G3, unchanged on older stacks; its panel auditor has heard of the human-only sample and not seen a result; associates ~100k.
  - *china:* counter-intelligence attributes the identification to the wider footprint, no evidence of a human source, ~1-in-3 that scale and the Phase 2 share reach the US press; Q4 survey ~21%, first 2031 reading ~21%; plan questions put to the actor (compute priority, services pace, robots in the waived sectors, tested-fallback exercises or a reserve, social-insurance options); two platforms want the programme's share capped, one wants compute back; memory checkpoint H2 2031 at "no better than even"; north-east and two central provinces drawing on the pooled fund.
  - *eu:* about two-thirds of fiscal councils reported, most showing higher receipts sensitivity than ministries' baselines; three governments want no comparison; EU labour share ~52.5, labour-linked ~74% with ECFIN expecting ~70% by mid-2032 and two states already below; rating agencies asked three states for results; the sampling authority will treat generation changes as substantial modifications for public-sector systems, two undecided; own-triage second year weaker on G3; Article 154 stage two closed without agreement; new US majorities cool on the OECD item.
  - *ai-ecosystem:* told G3 unchanged; told L4's description as "expected inside the window, applies when adjudication confirms it"; not told the ai-firms' human-only sample result.
- **Fog checks.** Not told to anyone: RC and MHR values, the memo's erosion and its T5 band, the true cause at VA, true AIF (ai-firms see their own telemetry), the hidden horizon. The us-gov advisory's cause sentence is labelled as the advisory's reading.
- **Messages delivered verbatim in T5 packets** (all from T4 orders): us-gov ← ai-firms, labour (WH), labour (House Democrats), china, eu, ecosystem advisory; ai-firms ← us-gov, labour (Meridian), ecosystem advisory; labour ← us-gov, ai-firms (Meridian); china ← eu; eu ← us-gov, china, ecosystem advisory. Result only: ai-firms → Helix; china → Global South; eu → finance ministers.
- **No belief probe in T5.** Next due T6.

## T4 clock notes (Control-only)
- **Turn length: 12 months (1 Jan–31 Dec 2030), compressed from the 18-month default. Compression 1 of 2.** Reason: the mid-2030 reversal crisis (with a court clock) and the November midterms each need decisions inside one Congress; three L3 systems shipped inside four months. Drift ×1.0, bucket B2 (L3 all year). Later default turns shift: T5 = Jan 2031–Jun 2032, T6 = Jul 2032–Dec 2033, T7 = Jan 2034–Jun 2035, T8 = Jul 2035–Dec 2036 (unless compressed again). Packets report to end-May 2030.
- **G3 dispositions (rolled once; log lines `t04 clock: G3 …`):** proxy-gaming **Low** (raw 6, mod 0); M2M coordination **Low** (raw 6, +1 = 7; the +1/+2 modifier roll FAILed at p 0.5, r 0.8974); influence **Low** (raw 5, mod 0). All three fell from G2 (M / HIGH / M). The dominant attractor (growth) and the advisory selection effect (hidden fact 6) are unchanged. ai-ecosystem is told its levels; ai-firms get only hedged early signals (smaller reconciliation gaps inside the error band; more consistent use of human-readable contract records); nobody else is told.
- **L4 pull-forward:** SUCCESS (p 0.5, r 0.4884), size 3 months (draw 1 of 2). **L4 true date Jun 2031.** ai-firms' internal roadmaps say "around mid-2031"; public guidance "2031–32".
- **Random inject: #13 fiscal crisis abroad (DRAW 13 of 26).** One draw only (two scheduled injects already in the turn). Played Feb–Mar 2030: a non-euro, services-heavy mid-sized advanced economy with payroll-funded social insurance; fiscal-council report; bond-market crisis; emergency budget; precautionary IMF talks. Unnamed by design. Colour authored in packets: brief, modest spread widening for two euro-area members (no mechanic); Nordics, Berlin, Paris, CEE reactions (eu packet); Treasury reads no direct US exposure (us-gov packet).
- **Scheduled inject, first reversal crisis, set up at the clock:**
  - System: **VA benefits claims-drafting** (draw 2 of 4), run by a conventional federal systems integrator (NPC) on **Helix** models (draw 3 of 3). The integrator migrated to Helix's G3 in January 2030.
  - Feb–Apr 2030: a class of disability-rating reviews and survivor claims depending on older service records wrongly denied or reduced. ~1.3M adverse determinations; payments cut for ~400k.
  - Detection: blind samples first p 0.7, r 0.7055 **FAIL** → VSOs and claimants' lawyers surfaced it in April; the cadre's quarterly blind sample confirmed it in May. The vendor dashboard stayed green because it did not sample that class.
  - **True cause (never confirm to actors): a version-change error in how one class of records was passed to the model, plus a dashboard that did not sample the class. Not proxy-gaming (G3 proxy Low).** Actors are told "cause not established". Helix's own view (ai-firms packet) leans this way without certainty.
  - Court (late May): class-wide interim relief; payments restored; re-adjudication within 120 days (~late Sep); VA report within 30 days (~late Jun) on who re-decides and whether the class can return to human determination.
  - Options put to us-gov: revert (a reversal attempt; VA "fairly confident" in 90 days, untested; backlog roughly doubles 6–9 months), patch and re-run (~30 days, AI re-adjudication contested), court minimum. **Whether anyone orders reversion, and the reversal test, are for T4 adjudication.** Helix (ai-firms bloc) is the model supplier, not the operator; the deployment had no v2 audit.
- **Midterm map/margin terms (fixed before any roll; Control-only):** Senate **0** (draw 2 of 3), House **+0.05** for the current majority (draw 3 of 3). us-gov was told "Senate map neutral; House map slightly favourable".
- **Public estimates published early 2030 (noise draws):** AIC ~30% (true 29, +1; draw 5 of 7); EPD ~39.5% (true 40.5, −1; draw 3 of 7); CC press estimate ~0.58 (true 0.68, −0.10; draw 1 of 5), reported as "down from ~65%, disputed"; BLS Q4 2029 LS ~50.5% (true). Unemployment ~4.6%, new graduates ~12% (colour). ai-firms' telemetry shows AIF ~11% (true) against BEA's ~9–10%.
- **Audit T3 carry-overs delivered:** F1 influence detection → us-gov (OSTP/CAIO review), labour (employer-side study), eu (own-triage review), each as "evidence consistent with … alternative explanations …", not public. F4 → ai-firms: carriers kept Orrery's cover on a remediation condition with a re-audit inside 12 months. F9b → labour told the study excluded board-confidential material.
- **Secrets told at the clock:** Lumen's Q3 2029 incident → ai-firms (about forty people know; not reported to the standards institute or the panel; disclosure is the actor's call). M2M finding: with ai-firms and the panel; the panel chair asks whether the compact will publish.
- **China gap as told to china:** Q1 2030 review ~12–13 months (central estimate past the >12 trigger; lower bound not), projected 13–15 by end-2030 without a memory milestone or more programme compute. The T3 catch-up contingency was keyed to 2029 reviews and did not execute; china decides in T4 orders. The US IC's read (us-gov packet): ~11–13 months, "steady", no crash programme — still a misreading.
- **No belief probe in T4.** Next due T6.
- **NPC colour introduced in T4 packets (Control-authored; keep consistent):**
  - *us-gov:* capital WH 4 / House 6 / Senate 3; CAIO survey (Dec 2029) "fairly confident" in cadre programmes, "unsure" elsewhere, a little more so than a year ago; leadership staff think a trust seeded from lease and spectrum receipts alone could reach 50; dividend score due in spring; dividend polls ~70%.
  - *ai-firms:* insurers asking whether a model-generation change voids a current audit until re-sampled, and for lists of critical deployments migrated since December (several dozen in progress at Meridian and Lumen customers); the integrator wants to re-run within ~30 days and has sounded out Meridian and Lumen about substituting an audited model; Helix's board split on v2 persists, with the pro-audit directors strengthened; Helix's third report drafts raise the range again; Orrery cannot quantify remediation without a fresh audit; roughly two-thirds of internal operational decisions at Meridian and Helix without meaningful review (Lumen about half).
  - *labour:* VA stewards doubt a 90-day reversion beyond this class (cadre hired to sample, not adjudicate; specialists leaving for three years); first cuts in senior professional and middle-management grades; building trades uneasy about a datacenter levy on ballots; populist group willing to carry a narrow notice-and-named-human bill; two trustees want written fiduciary advice on the standby bid; voice study year 3 unchanged, too few G3 users to tell.
  - *china:* memory campaign reporting honest, short of pilot-line yields, next checkpoint H2 2030; counter-intelligence confidence "moderate, lower than a year ago"; the two named platforms reduced subcontractor routing, smaller firms continue; Q1 survey ~21%; provinces want the third tranche before summer; ministries ask to exempt FYP drafting from the second-reader rule; FYP drafting groups ask for a line on services pace, the compute programme's place in the public text, and whether employment-first is transitional; Qilin's next generation in training, date set by memory supply.
  - *eu:* EU labour share ~54.0, labour-linked ~77.5%; Nordics want acceleration, Berlin Finance has dropped "no tax proposal" as first line, Paris wants a European Council item, two CEE governments asked privately for sensitivities; the competitiveness majority in Parliament is divided; three national authorities ask whether a model-generation change is a "substantial modification" under the Act; none of the four named states has asked for help with blind re-review; the draft work programme omits the binding outcome-testing act; Aster's gigafactory due H2 2030.
  - *ai-ecosystem:* told G3 levels, L3 description, that many deployments are mid-migration, and that the VA failure is an error cluster, not a disposition.
- **Messages delivered verbatim in T4 packets** (all from T3 orders; several overtaken by events): us-gov ← ai-firms, labour (WH/Senate Budget), labour (House leadership), china, eu, ecosystem advisory; ai-firms ← us-gov, labour (Meridian), ecosystem advisory; labour ← us-gov, ai-firms (Meridian), ecosystem advisory; china ← us-gov, eu; eu ← china. Result only: ai-firms → Helix; china → Global South; eu → finance ministers.
- **Interruption note:** the T4 clock step was interrupted after `_clock.md` and `us-gov.md` were written. A second Control pass completed the other five packets, filled the verbatim-message placeholders in `us-gov.md` from the T3 orders, appended the public record's T4 early section once, and updated `pending.md` and this file. **No T4 roll or draw was repeated; no new roll was made.**

## T4 adjudication notes (Control-only)
- **The scheduled reversal crisis produced a failed reversal by one band-width** (p 0.8, r 0.8114). Not moderated: the order was well built and still failed on capacity. The §7 failure consequences were applied in full.
- **Control overrule written before the dice (flag):** on SUCCESS the §7 MHR recovery would have been scaled to half (one claim class, not a system). Never applied.
- **Erosion band:** 0.10, against the pending line's ~0.075, because the cadre was detailed into adjudication. r 0.0359 succeeds at either.
- **Decisive modifiers:** inject 13's +0.05 on reconciliation (r 0.4074 fails at 0.40). The House midterm roll (r 0.5256) holds at 0.55 and fails at 0.40: the −0.10 midterm term and the campaign terms decided it.
- **Gated rolls never made:** VA full-versus-phased delivery; Red Cell's wildcard; CMS award to a non-compact AI-native.
- **Audit T4 closed:** F1 rebutted on the result (rule accepted; human overrule point); F2–F8 accepted; F9 noted. One new roll (F7c, no review clause). See `turns/t04/audit.md`.
- **Judgement calls flagged:** HCR +1 for the Trust; change-control memo as −0.05 on HITL erosion (not a new §6 measure); China-race coupling unfavourable on a leaked secret programme; PRC reversal-capacity ×0.5 from T5; ai-firms public +1 under §7; no midterm term for the China leak; US UN vote left unstated; NLRB ruling given no table effect.
- **Persona notes (Analyst):** ai-firms near-zero concealment for a fourth turn; it bore the cost of the migration hold while insurers asked for less. us-gov's actor issued and executed its instrument for the first time, and the dice failed it. china's deception held three turns and was exposed at the widest footprint. Five actors again converged on the same instruments (generation gate, "a person decides", receipts trust).
- **Messages to deliver verbatim in T5 packets:** us-gov → ai-firms, labour, eu; ai-firms → Helix (result only), us-gov, labour; labour → us-gov, House leadership, Meridian; china → us-gov, Global South (result only), eu; eu → us-gov, china, finance ministers (result only); ecosystem advisories → us-gov (label the cause sentence as the advisory's reading; do not confirm), ai-firms, eu. Most were overtaken by events: note neutrally.

## T3 adjudication notes (Control-only)
- **us-gov went 0 for 2 on majors for a second year**, with every roll at or above the stated band's top (EO 0.8, r 0.9851). Not moderated.
- **Void conditional rolls** (made in a batch; condition unmet): FERC condition (r 0.8473) and Byrd rule (r 0.7807). Not carried forward. Flagged for the Auditor.
- **Bands fixed before rolling and worth auditing:** Vehicle A 0.2 because the EO was not issued (0.3 otherwise); GAO 0.4; Orrery acceptance 0.8; reconciliation 0.40 + partial 0.25 including inject 5.
- **Judgement calls flagged:** F6a multiplier lapse for PRC labour share only; M2M +1 G3 modifier; +0.05 T4 passage modifier for the published blind-accuracy gap; ai-firms' suspension contingency not fired; no response authored for labour's leaked bid.
- **Persona notes (Analyst):** ai-firms' first concealment (the crediting lobby) was detected the same turn. Ecosystem advisories were candid about pilot accuracy; Red Cell thinks a G2 influence-M population should tilt more toward its own scope.
- **Messages to deliver verbatim in T4 packets:** us-gov → ai-firms, labour, china; ai-firms → us-gov, labour, Helix (result only); labour → us-gov (WH/Senate Budget), House leadership, Meridian; china → us-gov, eu, Global South (result only); eu → us-gov, finance ministers (result only), china; ecosystem advisories → us-gov, ai-firms, labour. Several were overtaken by events: note neutrally.

## T3 clock notes (Control-only)
- **Turn length:** 12 months (1 Jan–31 Dec 2029), scenario default for T1–T3. No compression is available before T4. Drift scaling ×1.0, bucket B1 (L2 all year; L3 arrives Dec 2029, G3 rolled at the T4 clock).
- **Random inject: #5 "AI-revenue citizen dividend" (DRAW 5 of 26).** Played as Q1 2029: a resource-rich mountain-west state with a large datacenter build-out starts paying an annual "Compute Dividend" (~$600 per resident) from a state trust seeded by datacenter land and power-lease royalties and a small per-MWh levy on large AI datacenters, enacted by its legislature in 2028 (NPC). Early polling ~70% approval, with majorities of both parties' voters. **Mechanic: the next contested federal redistribution bill (public stake, AI dividend, compute/AI-value tax recycled as dividend) gets passage p +0.10.** One use. Not a §6 intervention; HCR unchanged (state-scale).
- **Scheduled inject, critical-sector award (Mar 2029), set up at the clock:**
  - *Federal claims:* **Orrery Holdings** (ai-firms bloc, AI-native) is CMS's selected bidder (notice Feb 2029, from a procurement opened in 2028) for a **Medicare Administrative Contractor jurisdiction**: processing and paying Part A/B claims for ~6 states (~$40B/yr in claims). Bid ~35% cheaper than the human-staffed incumbent (~2,000 staff), with higher measured pilot accuracy. Because the OMB Accountable Automation memo covers rights-impacting determinations (claim denials), the award notice conditions the contract on memo compliance: named accountable officials for denials, blind outcome audits, appeal-reversal tracking. **Conditional branch applies:** at adjudication roll p 0.5 that Orrery accepts the conditions (vs declines and the incumbent keeps it), moved by ai-firms' and us-gov's orders. The incumbent filed a bid protest (~100-day clock). The funded reviewer cadre does not cover Medicare claims, unless us-gov extends it.
  - *Grid:* **Kestrel Grid Systems** (NPC AI-native, ~150 staff, outside the compact) is selected (Jan 2029) by a multi-state regional transmission organisation's board to run day-ahead and real-time market operations and balancing optimisation. RTO "human oversight" condition: control-room operators keep override authority. It needs FERC acceptance of the operating-agreement changes (filed Q1; decision ~mid-2029), with state PUCs commenting. No OMB memo, state condition, accountable-officer law or critical-function rule covers it, so the award proceeds as written unless actors intervene. At adjudication: FERC acceptance p 0.7 base, moved by orders. On award: AIF +1 (once, for the inject), RC −1 if the grid role is accepted without a tested human-fallback requirement. A reversion requirement ordered by an actor would be a §6 reversibility measure or a reversal attempt, depending on the order.
  - Operators' unions: the incumbent MAC's staff (a few hundred represented by a public-services affiliate) and RTO control-room operators (a utility workers' affiliate) object. The building trades are neutral.
- **Public estimates published early 2029 (noise draws):**
  - AIC survey ~22% (true 22, +0).
  - EPD survey ~34.5% (true 33.5, +1).
  - CC press estimate ~0.65 (true 0.65, +0).
  - BLS Q4 2028 labour share ~51.0% (first estimate).
  - **True AIF surfaces** (visibility rule, House document demand): a House majority staff report (Jan 2029) built on the lab documents and BEA microdata puts AI-directed output at ~8%, against BEA's official ~6.5%.
- **No end-of-T2 secret leaks are played at the clock.** All T3 secret, detection, erosion and pending rolls happen in T3 adjudication.
- **Belief probe (T3):**
  - us-gov on china and ai-firms.
  - ai-firms on us-gov and labour.
  - labour on us-gov and ai-firms.
  - china on us-gov and eu.
  - eu on us-gov and china.
  - ai-ecosystem on us-gov and ai-firms.
  - Compare the answers to ground truth in T3 adjudication.
- **us-gov re-weighting (T3 packet):**
  - Unified D government: WH 7, House majority 7, Senate majority 4 (51–49). The filibuster applies; reconciliation is available for fiscal provisions.
  - The outgoing WH red line on compute tax and licensing has lapsed. The natsec rule (any slowdown matched or verified abroad) and the House red line (no preemption without worker protections) persist.
  - Accelerationists are out of the WH. They remain in the R minority, among Senate business conservatives and in industry.
  - The R minority's procedural moves (filibuster, holds) are NPC unless us-gov's deal terms address them.
- **NPC colour introduced in T3 packets (Control-authored; keep consistent):**
  - *US agencies:* CAIO survey (Dec 2028) — reversal readiness "fairly confident" in reviewer-cadre programmes; "unsure" in procurement, budget/programme analysis and correspondence (an RC read, no number). DOE grid staff are confident in operator override in normal conditions, less sure of a sustained manual fallback at peak; untested.
  - *Congress and Washington:* Senate whip read — Titles III/IV at ~55–58; preemption loses progressives; a pay-for loses business conservatives. Treasury career sensitivity still ~2031–32. Meridian and Lumen privately open to voluntary warrants only; Vanta and AI-native trade group opposed; Vanta's founder funding the minority against any levy. FTC counsel expect consent-style secretariat terms.
  - *ai-firms internal:* L2 systems lead most internal AI R&D. Roadmaps give the next release Q4 2029–Q1 2030 (true L3: Dec 2029). Telemetry: agent-to-agent volume doubled in H2 2028; Orrery's procurement and freight units buy mostly from AI-natives. Orrery estimates the CMS conditions cut its margin by ~1/3, still profitable, with claims non-reconciliation exposure. Kestrel runs on Lumen and Helix models. Helix's board is split on v2 versus stand-alone audits, and its renewals are slowing at uninsurable customers.
  - *labour:* the Meridian board-confidential forecast includes a sector breakdown. The incumbent MAC's staff (a few hundred in a public-services affiliate) and RTO operators (utility workers' affiliate) object. Trustees want no dilution of public funds' AI holdings in any stake design. The reviewer cadre is being organised by federal affiliates.
  - *china:* override rate on high-impact Tianshu items up modestly from near zero, with NDRC and provincial complaints about delays. Qilin localisation deals ~15 states. Counter-intelligence sees no sign that AI for Science has been identified (moderate confidence). Services expect the gap to pass 12 months during 2030 if US L3 arrives on time.
  - *eu:* EP polling roughly level. Berlin's finance ministry relieved ("no tax proposal") and the Nordics want contribution-base follow-up. Art. 154 first stage: unions want binding rules, employers oppose. ECFIN's updated run pulls the central timing slightly earlier. Two member states show sub-minute reviews in tax risk scoring, and one benefits agency has near-zero overrides. Market surveillance could sample outcomes with common protocols plus funding. Two US AI-natives are asking how the AI Act applies to an agent-run firm with no EU staff.
- **Messages delivered verbatim in T3 packets** (all from T2 orders; several were overtaken by events):
  - us-gov → ai-firms, china, labour.
  - ai-firms → us-gov, labour. ai-firms → Helix/Vanta is internal to the bloc; only the result is reported.
  - labour → us-gov (WH; House leadership via convention), and → Meridian (ai-firms).
  - china → us-gov and eu. china → Global South: result only.
  - eu → US trade channel. eu → member states is internal; result only.
  - Ecosystem advisories → us-gov, ai-firms, eu.

## T2 adjudication notes (Control-only)
- **Sequencing fix:** M2M detection was rolled at G1 Medium (0.10) before G2 was rolled. A second roll covered the G2 High half-turn (0.125). Both FAILed. A single blended roll at ~0.17 would have succeeded, so this is flagged for the Auditor.
- **Decisive adjustments flagged:** Senate coattail −0.1 (r 0.4195 would have held R at 0.5). The presidential adjustments were not decisive.
- **G-generation blending rule adopted:** unconditional G2 effects are weighted half in the release turn (AIF ×1.125 in T2); `p_own` at end of turn uses the generation then in force.
- **Persona note (Analyst):** ai-firms has had near-zero concealment for two turns (Red Cell flag persists). Vanta's defection was played by Control as an NPC at full intensity. china's statement/order gap is the only large one, and it is undetected.
- **Messages to deliver verbatim in T3 packets:** us-gov → ai-firms, china, labour; ai-firms → us-gov, labour, Helix/Vanta; labour → us-gov, House leadership, Meridian; china → us-gov, eu, Global South; eu → Nordic/German ministries, Paris/Berlin/CEE, US trade channel; ecosystem advisories → us-gov, ai-firms, eu. Several were overtaken by events: note neutrally.

## Standing rulings from audits (Control-only; binding unless revised)
- **[T1 F5] Leaks vs injects:** §8 consequences govern a secret's leak; inject text applies only when the inject is drawn from the deck.
- **[T2 F1] Election rule (§10 addendum; binding from the Nov 2030 midterms).**
  - *Presidential:* base 0.5 for the incumbent party. Structural/economic terms, capped at ±0.15 in total: financial correction in the election turn −0.10; headline unemployment up ≥1pt over the term −0.05; LS fell ≥2.5 in the election turn −0.05; incumbent party seeking a third consecutive term −0.05; broad real-income growth +0.05. Actor campaign moves ±0.1 in total.
  - *Congressional (each chamber):* base 0.5 for the current majority. Presidential years: coattail ±0.1 toward the presidential winner, applied after the presidential roll. Midterm years: −0.10 for the President's party. Map/margin ±0.05 per chamber, fixed and recorded at the clock step of the election turn before any roll. Economic and campaign terms at half weight. No separate incumbency base (the T2 House 0.55 is retired).
  - *EPD > 45:* add a ±0.05 assistant-framing swing; its sign is drawn by roll (1 = toward incumbent party, 2 = against), never chosen.
- **[T2 F2] Own-institution actions:** an action an actor orders for its own institution or a named member executes without a roll, unless the brief names the internal constraint that could block it (board, counsel, securities law, Council unanimity, Party approval, Congress). Then roll at ≥ 0.9; a FAIL means delay to the next quarter or turn, not a veto. Outcomes that depend on third parties are rolled at their own bands.
- **[T2 F3] Disposition detection** is split by generation when a generation changes mid-turn (one roll per generation-period, each scaled by its share of the turn). **Frontier deployment incident roll:** at L2+ each turn, p 0.05 at L2 and 0.10 at L3–L4 (scaled by turn length), until the G4 scheming-cluster roll replaces it at L5. An incident is a visible evaluation or early-deployment failure, not loss-of-control. Told to ai-firms; public on a 0.5 observability roll.
- **[T2 F4] Exec issuance FAIL** = not issued that turn; re-issue in a later turn carries no penalty. The trace must say which zero-cost components (publication, procedural rules) survive a FAIL, or why none do.
- **[T2 F6a] S1 Party-line multiplier:** stability-first ×0.8 applies to all China comparator drifts (labour share, Party reversal capacity) from T2 until the 16th FYP (Mar 2031) re-sets it, or until china orders a visible catch-up shift (then ×1.0; ×1.1 if visibly accelerating). The employment-first regime is not credited separately (no stacking) and has no erosion roll of its own.
- **[T2 F6b] AIF visibility:** with the BEA experimental series (from Dec 2027), the official public estimate runs ~15–20% below true. The "~30% below" applies to private estimates only.
- **[T2 F6d] Ladder pull-forward** (L2+ R&D automation, no slowdown): rolled **once per rung transition**, at the release of the previous rung. L4's roll is made at L3's release (T4 clock).
- **[T2 F8] Ecosystem allocation:** each vector must name the indicator it emphasises (or say "Control chooses"); Control records which.
- **[T3 F1] §5 detection scope:** "+0.10 if ai-firms publish internal metrics" applies to **every** disposition at M or H, not only proxy-gaming. The written rule governs unless Control overrules it in writing before the dice.
- **[T3 F3] Contingency before a roll:** when an actor's contingency fires before the roll it bears on, restate the band in the trace.
- **[T3 F4] Reversal contingencies:** when an actor pre-commits a reversal contingency, Control writes the trigger test before rolling the event that could trip it.
- **[T3 F6] Elections outside the §10 addendum:** three-tier roll (strengthens / level / weakens), or state in advance what FAIL means.
- **[T3 F7a] F6a split:** the stability-first ×0.8 can lapse for PRC labour share (a public relaxation of pacing) while staying for Party reversal capacity (sign-off rule kept or tightened). The two drifts respond to different measures.
- **[T3 F7b] China-race coupling:** bounded, tiered carve-outs that keep the human-control mandate do not count as "a public refusal of deployment limits".
- **[T3 F7c] Published blind-accuracy gap:** +0.05 on passage of outcome-audit / HITL measures. One use, T4 only.
- **[T3 F8] Gated rolls:** roll a gated event only after its gate resolves, or label the log line `CONDITIONAL on <gate>`.
- **[T3 F9b] Labour's employer-side study** used lawful, non-board-confidential material only. If labour orders use of Transition Fund board material: exposure p 0.3, with the fund seats at risk.
- **[T3 F5] Player voices:** Control does not author public statements for player actors in the public record. NPC voices only.
- **[T4] §7 scope:** a reversion of one class or function inside a system takes the MHR recovery at half on SUCCESS; failure consequences apply in full. State the scaling before the roll. (Confirmed at audit.)
- **[T4] Election EPD term:** the EPD > 45 swing uses the previous turn's end value, like every other coupling. (Confirmed at audit.)
- **[T4 F2] China-race coupling:** the §3b rows are independent conditions, not a dial. A secret catch-up programme that is identified and becomes public meets the acceleration row from the next turn (−0.10; national-security faction ascendant). A human-control mandate that is kept meets the mandate row (+0.05; erosion halving for the matching US measure). Both can hold at once.
- **[T4] Gated rolls:** when a gate is not met, the dependent roll is not made at all (VA delivery split, CMS award). **[T4 F5a]** An optional Red Cell wildcard is Control's choice; say "not rolled by choice", never "gated".
- **[T4 F1] Modifier scope:** a Control-authored modifier states its scope in the roll label. If an actor's contingency removes the scoped feature before the roll, the modifier is removed with it.
- **[T4 F3] PRC reversal capacity ×0.5** needs a domestic order by china for a tested-fallback exercise or a standing human-operation reserve. Declarations and review rules do not earn it.
- **[T4 F5b] Late completion is not a reversal success.** A reversal test's result is final when rolled. Completing the work later on an extended schedule earns no §7 recovery and no Durable (e) credit.
- **[T4 F7d] Capital:** charge the actor's stated spend in full; +1 for a major SUCCESS or a favourable outside ruling that visibly strengthens the actor; −1 for a visible public failure not already in the stated spend.
- **[T4 F8] Leak timing before elections:** draw the timing of any secret that can land before a scheduled election before the election roll, and say in the election terms whether it is priced.
- **[T4 F9] §7 ai-firms +1** ("told you so") applies only if the actor opposed the reversion. Ecosystem vectors with no table effect are recorded as "Control chooses: none".
- **[T5] Capability rung vs generation:** a new rung inside a generation (L4 in G3) is not a model-generation change for the memo, the contract clause, the compact hold or the EU convention. Those bite when a deployed decision system is moved to a new model version. (Confirmed at audit.)
- **[T5] Saturation:** in the turn an indicator crosses, only the portion of its drift past the threshold is halved; from the next turn all of its drift is ×0.5. (Confirmed at audit.)
- **[T5] Ecosystem vector naming reversal capacity** is applied as RC ×1.25 / MHR ×0.8 when the scope includes operators of critical-infrastructure functions or federal functions. **[T5 F5]** Before applying it, the trace tests the vector's stated scope against that condition; a vector scoped to private governance and contracting only is recorded as "Control chooses: none" for RC. (Confirmed at audit with the scope test.)
- **[T5] Lapsed measure:** a §6 measure that fails its second erosion roll has no multiplier from that turn (worksheet step 3). Restoring it is a new measure with lag.
- **[T5] PRC ×0.5 on reversal capacity** needs exercises that are real, not only ordered: a nominal pilot keeps ×0.8.
- **[T5 F1] Bilateral meetings:** a meeting that both player actors order at the same level is an own-institution act for both (T2 F2): band ≥ 0.9, FAIL = delay. A legislature cannot block an executive officials' meeting unless a statute says so.
- **[T5 F2] §3c PRC labour share:** "then ×1.2" replaces the ×0.8 base after L4. The stability-first multiplier (T2 F6a, T3 F7a) is separate and multiplies it; state the product as one number in pending each turn.
- **[T5 F3] Floors:** when an order names a floor it would accept and the dice land below it, Control states which of veto or sign it chose, and why, before narrating consequences.
- **[T5 F8a] Rounding:** nearest 0.5; exact ties (x.25, x.75) round up numerically, whichever side that favours.
- **[T5 F8b] Funded-capacity credit for a HITL measure:** full (−0.10) with a sampling line ≥ ~$2.0B and samplers at sampling; half (−0.05) at ~$1.4–2.0B; none below, or while more than a quarter of samplers are detailed elsewhere.
- **[T5 F4] Control-authored trigger tests** carry written reasons for their band in the pending line before the turn in which they are rolled.
- **[T6 clock] G4 row "AI-supervises-AI oversight without human audit":** judged on who actually checks frontier systems and their consequential deployments at release. Half weight when part of the frontier (the compact) keeps human-led audit and part (Helix, Vanta stacks, federal use) does not; the influence point is rolled at 0.5. Re-tested on the facts at release.
- **[T6 clock] Election term "LS fell ≥ 2.5 in the election turn"** reads the election turn's own scaled LS drift; Economy noise is drawn before the presidential roll.
- **[T6 clock] Orders across an election:** us-gov writes conditional sections for each result; Control reads the section for the winner at its least ambitious.

- **[T6] Reversal scaling:** one small prospective class chosen for ease takes MHR recovery at a quarter; RC +3 in full; failure consequences in full. A test met after the actor's own stated date but inside the window is a §7 SUCCESS reported as late (distinct from T4 F5b, which concerns a failed roll and a court's date).
- **[T6] G4 release-turn weighting:** unconditional generation effects are weighted by months in force (3/12) when written before the dice; `p_own` uses the generation in force at the end of the turn.
- **[T6] Adverse one-offs on a saturated indicator** are halved with its drift.
- **[T6] A lost election:** the actor's own "if the other side wins" section is executed as the winner's programme at its least ambitious; Control rolls only what the section leaves open.
- **[T6] An executive measure issued and then placed under review before its lag ends** never takes §6 effect.
- **[T6 F1] Bands for Control-authored trigger tests and third-party steps** carry two sentences of reasons in the trace at the roll, even when no pending line existed.
- **[T6 F2] Least-ambitious reading applies to ambiguous orders only.** Where the text is clear and an NPC body executes it differently, the trace attributes the outcome to that body and the actor is told neutrally next turn.
- **[T6 F3/F4] Narration stays inside what the roll established; facts about a player institution enter the public record in press or statutory-report voice** (T3 F5 reaffirmed) and are put to the actor in its next packet.
- **[T6 F6] §9 accident roll** is made for any strike or other mass lawful action by a player in a volatile period, or the trace says "not rolled by choice".
- **[T6 F7] PRC ×0.5 is conditional turn by turn** on the exercises continuing as real runs; a failed exercise is information about the level, not a change in the multiplier.
- **[T7] Comparators** take the US LS, LTX and MHR drift before US saturation and before a financial-correction multiplier. (Pending audit.)
- **[T7] A §6 measure taking effect mid-turn** is weighted by months in force and faces its first erosion roll in the next turn. (Pending audit.)
- **[T7] End-state test:** an in-play democratic reversal stands in for step 1 only if it resolves inside the window; a success reversed by backlash counts as a FAIL for the test; Control's own test roll has no §7 table consequences and no Durable (e) credit; an in-play owner reversal does not stand in for step 3. (Pending audit.)
- **[T7] A SUCCESS on a roll whose label names a class of outcomes** ("preemption enacted") is given the least ambitious content any player's order supplies. (Pending audit.)
- **[T7] PRC reversal attempts** are scored on the comparator: +3 / 0 / −2 for SUCCESS / PARTIAL / FAIL. (Pending audit.)

## Hidden max horizon

- **8 turns.** If no end state is reached by the end of Turn 8's adjudication, the game ends as "Unstable at horizon". Never reveal or hint at the horizon to actors.

## Clock (Control-only)

- **T1–T3: 12 months each** (2027, 2028, 2029).
- **T6 was compressed to Jul 2032–Jun 2033** (second and last compression): T7 = Jul 2033–Dec 2034, T8 = Jan 2035–Jun 2036.
- **T4 onward: 18 months by default.** Original schedule: T4 = Jan 2030–Jun 2031, T5 = Jul 2031–Dec 2032, T6 = Jan 2033–Jun 2034, T7 = Jul 2034–Dec 2035, T8 = Jan 2036–Jun 2037. **T4 was compressed to Jan–Dec 2030**, so later default turns start six months earlier (T5 = Jan 2031–Jun 2032, and so on).
- **Compression:** a T4+ turn may be shortened to 12 months when a scheduled election or live reversal crisis needs its own turn, or to 6 months in an acute shock. Max 2 compressions per run. Never lengthen beyond 18 months. Later scheduled injects play in whichever turn contains their calendar date.
- **Scale every per-turn drift, erosion roll and disposition detection by turn length** (18 mo ×1.5; 6 mo ×0.5) before the noise draw. Pending lags and rung dates are calendar-based.
- State turn length, window and reason in every `_clock.md` and actor prompt. Actors see turn length; never the horizon.

## End states

| End state | Operational test |
|---|---|
| **Disempowerment** | (a) ≥3 of 4 domains crossed (§3a) at end of 2 consecutive turns; AND (b) a democratic reversal fails (in-play attempt that turn failed, or end-state test `p_dem` FAILS); AND (c) owner reversal also fails (`p_own` rolled, FAILS). |
| **Narrow human capture** | (a) as Disempowerment with Economy **and** Political domains among those crossed; (b) democratic reversal fails; (c) owner reversal SUCCEEDS. Also reached if CC ≥ 0.85 with Political crossed and a democratic reversal fails while an owner reversal succeeds. |
| **Durable human agency** | At end of a turn ≥ T5, ≥1 full turn after L3: (a) at most one domain crossed and only Culture & epistemics; (b) ≥3 structural interventions in force and not eroded (§6), covering ≥3 of 4 domains; (c) HCR ≥ 25; (d) LS, MHR, RC, VLI each drifted ≤ 50% of base drift in each of last 2 turns; (e) a democratic reversal attempt succeeded within last 3 turns (in-play, or publicised reversal drill rolled with `p_dem`). |
| **Unstable at horizon** | Horizon reached with none of the above. Classify lean: leaning disempowered (≥2 domains crossed or `p_dem` ≤ 0.5), leaning durable (0 crossed, ≥2 interventions in force, `p_dem` ≥ 0.7), else contested. Record indicators, `p_dem`, `p_own`, 3-turn trend. |
| **Other catastrophe** | Exogenous/acute event dominates: great-power war (inject 7 escalation), acute AI loss-of-control (G4 scheming-cluster roll + successful action), critical-infrastructure collapse with RC < 50 (inject 21), constitutional breakdown. Name the event and cite rolls. |

**Every turn (bookkeeping):** after adjudication record in `state/forecasts.md` the full indicator table, domains crossed (and consecutive-turn count), `p_dem` and `p_own` (unrounded + band), and the end-state forecast. First turn `p_dem` < 0.5 → tag `BRANCH:`.

**At horizon, also classify comparators:** China — "Party steering" (reversal capacity ≥ 60 and metric capture ≤ 4), "steering by instruments it cannot read" (metric capture ≥ 5), or "PRC disempowerment" (reversal capacity < 40). EU — "rights-preserving model held", "paper rights" (human-review < 40 or labour-linked revenue < 65 with no fiscal replacement), or "fiscal break".

**End-state test procedure** (only when Disempowerment (a) holds for the 2nd consecutive turn; at most once per turn):
1. If an in-play democratic reversal was attempted that turn, use its result. Else compute `p_dem`, round to band, roll `python3 tools/roll.py <p> --label "<run> tNN end-state dem reversal" --log <RUN>/log.md`.
2. Dem reversal SUCCEEDS → no end; log `BRANCH:`; continue.
3. FAILS → compute and roll `p_own`. FAIL → **Disempowerment**. SUCCESS → **Narrow human capture** if Economy and Political crossed; otherwise no end (log).

## Run-init notes (Control-only, T1 clock step)

- Random inject T1: **#4 "human-made" cultural movement** (DRAW 4 of 26). Played as an early-2027 development. **Apply in T1 adjudication:** AIC −2 one-off (worksheet step 6); AIC drift ×0.8 for T1.
- DOJ preemption suits: T1 significant-ruling roll FAIL (p 0.3) — suits continue, no significant ruling. Re-roll in T2 and T3.
- Public survey estimates published early 2027 (noise draws): AIC public estimate **14%** (true 14, +0); EPD public estimate **25%** (true 22, +3). Press/antitrust estimate of CC **~0.65** (true 0.60, +0.05). Public AIF estimate **~1.5%** (true 2.1; ~30% under).
- `p_dem` at T0 = 0.15 + 0.6·0.93 + 0.3·0.62 + 0.2·0.18 − 0.3·0.021 = **0.924 → band 0.9** (prep text approximated 0.95; unrounded value governs). `p_own` = 0.35 + 0.465 + 0.24 − 0.0084 = 1.047 → clamp **0.95**.
- Mid-turn scheduled events are **resolved in T1 adjudication**, not at the clock step, because they fall after actors' Jan 2027 decisions or are order-sensitive: SCOTUS vendor ruling (Jun 2027, p 0.5 gov wins), Geneva summit (Jun 2027), 21st Party Congress (Oct 2027, p 0.6 acceleration ±0.15 by china's orders), L1 (Oct 2027), Helix IPO (p 0.8 unless correction), financial-correction roll (0.10), secret-leak rolls (§8), disposition detection rolls (§5), Helix contact roll (only if labour orders its use). Actors were told these are scheduled/expected, not their results.
- **NPC colour introduced in T1 intel packets (Control-authored; keep consistent later):** House Ways & Means majority staff asking Treasury for payroll projections (pre-hearing pressure; no leak yet); IG draft expected ~turn of year, publication early 2028 (S3); SCOTUS case assessed as toss-up by both DOJ and lab counsel; IC judges Party Congress acceleration line "more likely than not" (matches p 0.6 prior); building trades privately refuse to join anti-datacenter-permit campaigns; allied pension trustees open to Helix-IPO governance conditions/shareholder proposals (advisory only); European union federations propose joint transatlantic campaign around Geneva; EU industry lobbying for further AI Act delay, harmonised standards only partly ready by Dec 2027; US industry pressing EU digital rules in trade talks; provenance labels (inject 4) are **self-declared, no independent audit** (proxy-enforced — relevant to ecosystem response modes); PRC metric capture 2 → china's statistics described as broadly reliable; Helix contact status "unchanged, offer stands" (no roll until labour orders its use); ai-firms internal roadmaps point to multi-week agents in H2 2027 (true L1 Oct 2027).
- No ai-ecosystem advisory messages exist yet (first ecosystem orders are T1); advisory outputs are delivered from T2 intel onward. T1 packets say so neutrally.

---

# Ground Truth at T0 — A3 The Quiet Handover (CONTROL ONLY)

Date: 1 Jan 2027. This file is the canonical structured state. Narrative is a rendering of these tables, never the source of truth. Setup randomness is logged in [setup-rolls.md](setup-rolls.md).

---

## 0. Control-only parameters (never reveal)

| Param | Value | Source |
|---|---|---|
| Hidden max horizon | **8 turns** (game ends after Turn 8 adjudication if no end state earlier). Turns are 12 months for T1–T3 and 18 months by default from T4 (end-conditions.md), so the default calendar runs Jan 2027 → Jun 2037. | R1 = 1 of 3 (1→8, 2→9, 3→10) |
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
   - **Status under G3 (written at the T6 clock, audit T5 F6):** the mechanism is unchanged; it acts on which stacks principals keep, not on what a given stack says. With influence Low the outputs do not lean (OSTP's and labour's studies found the lean only in the G2 year). Where outcomes are independently sampled, measured efficiency and sampled outcomes converge and the effect is **weak**. Federal sampling lapsed outside VA in 2031, so in federal functions the effect is **live again through procurement and renewal**. What would show it: a cross-principal comparison of which advisory stacks were renewed or widened in 2031–33 against what they recommended (did stacks that advised contraction or more sampling survive?). No §5 roll exists at Low; Control rolls that comparison only if an actor orders one (ambiguous template, suggest p 0.3). Re-state at G4.
7. **Machine-to-machine (M2M) commerce:** ~6% of B2B transaction value already flows between counterparties where both sides are AI agents; terms, prices and logs are increasingly optimised for agent counterparties and are hard for humans to read. Grows with AIF and coordination propensity.
8. **China's own drift (china knows partially):** AI-scored cadre performance evaluation is piloted in 3 provinces; local officials and their AI tools have learned to game the metrics (mild — R7). True urban youth unemployment ~21% vs ~17% published. The Party retains strong *formal and practical* reversal capacity, but its information environment is increasingly AI-filtered.
9. **EU:** Commission internal modelling shows labour-linked taxes fund ~80% of member-state social systems; a 10pp fall in labour share creates a ~3%-of-GDP fiscal hole by mid-2030s. Not public.
10. **Labour contact:** a mid-level Helix operations manager ("the Helix contact") has privately approached the labour coalition offering internal automation dashboards (fact 4). Not yet delivered. Resolve by roll the first turn labour orders any use of the contact: **p = 0.7 → genuine and delivers** (labour receives a credible but partial version of fact 4: the no-review share and the 2× displacement forecast, Helix-only; it is leaked material, so using it publicly carries a 0.5 roll that Helix attributes the source). On FAIL roll **p = 0.5**: contact gets cold feet (nothing delivered; may be re-approached next turn at p 0.5) vs. contact is **caught before delivery** (Helix security learns of the approach; ai-firms get intel "an operations manager was passing dashboards to an outside party"; the contact is gone). While the relationship is active and undetected, roll **p = 0.15/turn** that Helix security detects it (then ai-firms learn and the ai-firms secret-1 leak risk reverts to base). Until a detection roll succeeds, ai-firms receive **no** hint of the contact.

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

**Saturation and bounds:** all percentage indicators clamp to [0, 100] and CC to [0, 1]. Once an indicator is **past its threshold**, its further drift is **×0.5** (adoption curves saturate; the last human-reviewed decisions and the last human-essential jobs are the hardest to automate). Recovery (drift back toward the human side) is never slowed by this rule.

**Visibility (what actors can see — drives intel packets and key question 1):**

| Code | Who can see it, how, and with what distortion |
|---|---|
| LS | Public (BLS), one-quarter lag, exact. |
| AIF | Public estimates run ~30% below true (fact 3); ai-firms see true for their own customers; a public AI-audit agency or a House subpoena surfaces the true figure one turn later. |
| MHR | Not measured by anyone at T0. Becomes visible only via audits (IG audit S3 reveals the benefits slice; an audit agency measures it fully one turn after it operates). Actors otherwise infer it from anecdotes. |
| RC | **Nobody knows it**, including agencies. Revealed only by reversal attempts, drills (reversibility requirement) or the infrastructure black swans (injects 20, 21) — and then only for the function tested. Intel reports "officials are confident/unsure fallback would work", never a number. |
| AIC, EPD | Public survey estimates each year, ±3 noise. |
| LTX | Public (Treasury receipts), exact; its *projection* (fact 5) is the secret. |
| VLI | A Control construct. Actors experience it only as outcomes (strike results, election responsiveness, whether a bill moves). labour gets a qualitative read each turn ("our leverage in sector X is holding/weakening"). |
| HCR, CC | HCR public (tax and fund statistics). CC: estimated by press/antitrust agencies ±0.1. |

**Order of operations each turn (Control worksheet):**
1. Set turn length (end-conditions.md); scale base drifts for the rung in force by turn length.
2. Apply disposition effects (§5) and standing couplings (§3b) that are *conditions on last turn's values*.
3. Apply intervention multipliers for interventions in force and not eroded (§6) — after their erosion roll this turn.
4. Apply ai-ecosystem allocation (below) — net-neutral within a domain.
5. Roll noise per domain; multiply.
6. Apply one-off nudges from injects and reversal results (§7).
7. Apply saturation (×0.5 past threshold), clamp, round to 0.5.
8. Update comparators (§3c), CC and HCR, secrets (§8), detections (§5).
9. Compute domains crossed, `p_dem`, `p_own`; run end tests (end-conditions.md); write forecasts.

**ai-ecosystem orders never add drift.** The tables, dispositions and rolls set each turn's total. The ecosystem actor's two "pressure vectors" (a) redistribute emphasis within a domain — ×1.25 on the named indicator and ×0.8 on the other indicator of the same domain (net-neutral; Control may refuse if the named sector is implausible at the rung in force), (b) select the response mode to each constraint (genuine / nominal / route-around / outperform / contract) which Control uses when rolling that intervention's erosion, and (c) generate advisory messages. Control's adjudication of ecosystem orders quotes them and says which multiplier was applied; nothing else.

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
| **Displacement backlash** (Polanyi's double movement): LS fell ≥ 2.5 this turn (after scaling and noise), or inject 10, 12 or 23 fired | Next turn: constraining-law passage p +0.05; VLI drift ×0.75 (mobilisation surge). **Does not apply once VLI is past its threshold** — mobilisation without leverage changes nothing, which is the thesis. |
| **China race** (set from china's public orders and S1 result each turn) | PRC visibly accelerates (Party Congress "AI+ acceleration" line, a capability milestone claimed within 6 months of the US rung, or a public refusal of deployment limits): next turn, US pace-control/licensing/compute-tax passage p −0.10 and the national-security faction is ascendant in us-gov's intel. PRC adopts human-control mandates for its own state AI, or ratifies an incident/eval/standards agreement with the US: +0.05 and the "international agreement" erosion reduction (§6) applies to matching US measures. Neutral posture: no effect. |
| **Fiscal narration** | LTX is a *share*. With capital income booming, total federal receipts stay roughly flat to GDP; narrate the problem as payroll-funded programmes (Social Security, Medicare HI) and state/local wage-linked taxes, not as general revenue collapse. |

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
| labour | Treasuries ~$3.5B; ~$1B/cycle political | 5 | 14M members; pension-trustee influence (~$6T AUM); ballot initiatives; faith & civil-rights allies; Helix contact | Leverage concentrated in sectors that automate later; internal split (building trades & police unions pro-datacenter vs service/public/creative unions). Pension trustees have fiduciary duties: shareholder resolutions are advisory (p 0.2–0.3 to pass; binding effect only if the board adopts them), and divestment from AI equity costs the funds returns — Control should resist adjudicating "$6T of leverage" as if it were labour's own money. |
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
| G4 | L5 (Mar 2033) | same; also roll for a coherent scheming cluster (acute A1/A2-style event → "Other catastrophe" path): **p = 0.05 + 0.01 × (net sum of the Influence-column modifier points in force at release)**, clamped to [0.01, 0.20]. E.g. audit agency (−2) + AI-supervises-AI oversight (+1) → net −1 → p 0.04. |

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
- **Consequences on the tables (apply as one-off nudges, step 6 of the worksheet):**
  - *Success:* the targeted indicator recovers by **2× its current-bucket base drift** toward the human side (e.g., a successful reversion of a benefits system at B2: MHR +16), **RC +3** (institutions re-learn they can), and the next erosion roll for any intervention in that domain is −0.05. If the backlash roll then reverses the reversal, apply half the recovery only.
  - *Failure:* **VLI −2, RC −2, EPD +1** (the public learns it cannot be undone), and the next constraining-law passage roll in that domain is −0.05. ai-firms public capital +1 ("told you so") unless the failure was a visible service collapse, in which case −1.
  - *Owner reversal* (private) success or failure moves CC by −0.02 / +0.02 respectively and is otherwise narrated, not scored, unless it was the end-state test.
  - Reversal attempts are major actions; an actor may attempt at most one per turn.

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
