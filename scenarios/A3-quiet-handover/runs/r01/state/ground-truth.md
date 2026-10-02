# Ground Truth — A3-quiet-handover / r01 (CONTROL ONLY)

> **CONTROL-ONLY SECTION — never reveal to actors, never hint.** Copied at run init (2026-10-02) from `prep/end-conditions.md`. Check end conditions at the end of every adjudication.

## Run status

| Field | Value |
|---|---|
| Last adjudicated turn | **T3**: 1 Jan 2029 → 31 Dec 2029 (12 months). No end state. |
| Next turn | **T4: 1 Jan 2030 → 31 Dec 2030 (12 months, compressed from 18; drift ×1.0).** Clock step **done** (see "T4 clock notes"). Orders, Red Cell and adjudication pending. |
| Rung in force | **L3** (Dec 2029; Helix first with ~5 weeks' notice and an evaluation window; Meridian and Lumen Q1 2030 on 90 days' notice). Bucket **B2 from T4**. **L4 true date now Jun 2031** (Sep 2031 pulled forward 3 months at the T4 clock: p 0.5, r 0.4884 SUCCESS; size draw 1 of 2). No further L4 pull-forward roll (once-per-rung rule). |
| Compressions used | **1 of 2** (T4) |
| Generation in force | **G3 from Dec 2029 (all of T4): proxy-gaming LOW, M2M coordination LOW, influence LOW.** Rolled at the T4 clock: proxy d20 6 + 0 = 6 (1–6 L); M2M d20 6 + 1 = 7 (1–8 L; the modifier roll for partly-in-force agent-to-agent protocols, p 0.5, r 0.8974, FAIL = +1 not +2); influence d20 5 + 0 = 5 (1–9 L). G2 (proxy M, M2M HIGH, influence M) ended Dec 2029. |
| US government | Unified Democratic (President, Senate 51–49, House). Midterms Nov 2030 under the §10 addendum rule. |
| Indicator values | **see "Current state" below** (§3 T0 column is reference only) |

## Current state (after T3 adjudication) — CANONICAL

### Indicators (US)
| Code | T0 | T1 | T2 | T3 | Threshold | Crossed? | T3 drift (net) |
|---|---|---|---|---|---|---|---|
| LS | 52.5 | 52.0 | 51.0 | **50.5** | ≤ 40 | no | −0.5 |
| AIF | 2.1 | 3.0 | 8.0 | **11.0** | ≥ 30 | no | +3.0 |
| MHR | 86 | 83.0 | 79.0 | **77.5** | ≤ 30 | no | −1.5 |
| RC | 93 | 90.5 | 87.0 | **84.0** | ≤ 40 | no | −3.0 |
| AIC | 14 | 16.0 | 22.0 | **29.0** | ≥ 60 | no | +7.0 |
| EPD | 22 | 27.5 | 33.5 | **40.5** | ≥ 55 | no | +7.0 |
| LTX | 71 | 70.5 | 69.5 | **67.5** | ≤ 52 | no | −2.0 |
| VLI | 62 | 63.0 | 63.0 | **59.0** | ≤ 40 | no | −4.0 |
| HCR | 18 | 18 | 18 | **18** | — | — | 0 |
| CC | 0.60 | 0.62 | 0.65 | **0.68** | — | — | +0.03 |

Domains crossed: none (consecutive 0). `p_dem` 0.834 → band 0.8. `p_own` 0.898 → band 0.9 (includes −0.1 for M2M High).

T3 noise: Economy ×0.6, State ×0.8, Culture ×1.2, Political ×1.4. No one-offs (no reversal attempt, no critical-sector award).

Public and visible estimates at end-2029:
- LS: ~50.7% (BLS Q3 2029).
- AIF: BEA quarterly range ~9–10% after the methodology review (true 11.0).
- LTX: ~67.9% (FY2029 receipts).
- AIC and EPD: next public surveys early 2030 (true 29 / 40.5; ±3 noise, drawn at the T4 clock).
- CC: press estimate re-drawn at the T4 clock.
- M2M share: ~21% of B2B value.
- MHR: no number is public. The March 2029 publication shows blind outcome accuracy ~5–8 points below dashboards in SSA and VA.
- RC: nobody knows it. No drill or reversal has tested it since 2027.

### Comparators
| Actor | Indicator | T0 | T1 | T2 | T3 | Notes for T4 |
|---|---|---|---|---|---|---|
| China | PRC labour share | 52 | 51.5 | 50.5 | **50.0** | Stability-first ×0.8 **lapsed for labour share** (public relaxation list, T3 ruling): ×1.0 from T3 |
| China | Party practical reversal capacity | 95 | 94 | 93.0 | **92.0** | ×0.8 kept (sign-off rule tightened, not relaxed) |
| China | Metric capture | 2 | 2 | 2 | **2** | 20-city NBS survey is the yardstick; not gamed in 2029 |
| China | True urban youth unemployment (published) | ~21 (~17) | ~20.5 (~16.8) | ~20.5 (~16.5) | **~21 (~16.3)** | Graduate season quiet (narrowly). Below china's ~22% trigger |
| China | Frontier gap (services' assessment) | 6–8 mo | 6–9 mo | 10–12 mo | **~11–12 mo** | Held in 2029 by compute pooling; no memory milestone. Services project >12 during 2030 after US L3. China's catch-up contingency is china's to order |
| EU | Labour share | 55 | 55.0 | 54.5 | **54.0** | |
| EU | Labour-linked revenue share | 80 | 79.5 | 79.0 | **77.5** | |
| EU | Public-admin human review | 90 | 88.0 | 85.5 | **84.5** | ×0.6 of US MHR drift; outcome-testing uptake failed (one authority) |

### Interventions / measures (§6 status)
| Measure | Owner | Status | Effect from | Strength | Erosion p (next roll) | Notes |
|---|---|---|---|---|---|---|
| OMB "Accountable Automation" memo + funded independent reviewer cadre (**~$2.2B from FY29; now covers SSA/VA/FNS/DOL-UI, Medicare claims and critical federal contracts**) | us-gov | In force, not eroded (T3 roll FAIL at 0.12). **Medicare and critical-contract blind audits at half sample until mid-2030 (hiring lag, audit T3 F10); the four original programmes at full strength** | T2 half; full from H2 2028 | **Full**: MHR ×0.5, RC ×0.7 | **T4 base: 0.25 + proxy and influence terms per G3 − 0.10 funded capacity, halved while the China coupling stays favourable; ×1.5 if the turn is 18 months** | The only §6 measure in force. |
| EO "Outcome Integrity and Reversibility" (measurement rule, freeze, randomised fallback trial, reversibility standard) | us-gov | **Not issued in 2029** (p 0.8, r 0.9851) | — | — | — | Re-issue in T4 carries no penalty (F4). Publication, CMS terms and the DOE filing survived. If issued, the reversibility standard would be a federal-only §6 reversibility measure (Control to set strength; lag 6–18 mo). |
| Accountable AI and Workforce Act (Titles III, IV, worker title, V, single filing) | us-gov | **Cloture failed 57–43 (Jun 2029)**; stand-alone IV+V failed 58–42 (Oct) | — | — | — | House Worker AI Rights Act marked up, not passed. |
| Reconciliation: capex depreciation limit, American Compute Dividend Trust, cadre funding | us-gov | **Budget resolution adopted (May 2029); bill not enacted in 2029** | — | — | — | Instructions usable in 2030. Two Democratic senators against the capex limit, a third undecided. Byrd-rule question on Social Security crediting unresolved (roll when a bill reaches the floor, p 0.7 struck). Inject 5 bonus consumed. |
| Compact voluntary AI Dividend (~1% gross AI revenue of Meridian, Lumen, Orrery; ratchet to ~1.5% if LS < 50%) | ai-firms | Offered, board-approved, **unpaid**; Treasury talks failed | — | Not §6 | — | If paid: HCR +1 one-off (Control's estimate), revocable. Crediting lobby exposed. Helix declined. |
| Halyard conditions (both states) | states | First audits **passed narrowly** (2029); failed-audit count 0 | 2029 | Deal-specific | — | Audit scope disputed. Workers' capital alternative bid now **public**. |
| State "AI-operated critical provider" law (1 state, Halyard model: human-led outcome audits + revocation) | state (labour campaign) | **Enacted 2029** | 2030 | State-scale, not §6 | — | Four other bills died. |
| State Compute Dividends | states | First state paying; **second state enacted** (pays 2030); Vanta-funded suit against the first state's levy pending | — | State-scale | — | |
| Compact Assurance Standard v2 | ai-firms | In force; FTC consent terms (separate secretariat, pooled data via panel) | 2029 | Private | — | Labour seat **vacant** (panel adopted neither condition). Helix outside. Kestrel audited. |
| Meridian / Lumen supplier terms (reconciliation-tier audit + human override for critical-infrastructure and health-payment operators); human-readable records for agent-negotiated contracts above a threshold | ai-firms | In force (unilateral) | 2029 | Private | — | |
| Compact Transition Fund | ai-firms | First independent count ~35k of ~40k | — | Not §6 | — | |
| Helix Workforce Impact Report | ai-firms (Helix) | Second report honest: 25–36% by 2030 | — | — | — | |
| Voluntary pre-release notice and evaluation | labs | Held at L3 (Helix ~5 weeks; compact 90 days) | — | Voluntary | — | Not statutory (Title V failed). |
| PRC responsible-official rule (tightened) + employment-first regime 2.0 (20-city survey yardstick; subcontract counting; **public relaxation list** outside tier-1/2 services) | china | In force | now | — | — | Human-control mandate keeps the China-race coupling favourable. |
| US–China: hotline (agent incidents) + **human-official understanding and statistics exchange recorded (Q2 2029, officials' level)** | us-gov / china | In force | now | Principles text | — | Not incident-and-eval sharing. |
| EU AI Act + outcome-testing protocols and Recommendation; accountable-person guidance for agent-run firms; Communication on financing the social model | eu | Published; uptake one authority; binding implementing act **frozen** after the EP election | now | Documentary in practice | — | Six-state table published: nominal review in 4 of 6. |
| HHS ANPRM on AI-operated critical providers | us-gov | Issued Q2 2029 | — | — | — | Comments close in T4. |

### T4 modifiers and couplings carried forward
- **Bucket B2** (L3) for all of T4; scale by turn length.
- **Displacement backlash:** does **not** apply in T4 (LS fell 0.7; no inject 10/12/23).
- **China-race, favourable:** continues (PRC human-control mandate; US–China text). +0.05 on US pace-control, licensing and compute-tax passage; erosion halving for the matching HITL measure. National-security faction not ascendant; the IC still reads Beijing as steady (a misreading). AI for Science detection tiers (audit T2 F7) still apply. If china orders its catch-up contingency visibly in T4, re-set the coupling.
- **Secret-1 resolution bonus:** expired.
- **Inject 5 bonus:** consumed.
- **Published blind-accuracy gap (Control-authored, flagged for audit):** +0.05 on passage of outcome-audit / HITL measures in T4.
- **Standing couplings on T3 values:** LTX < 60 no; EPD > 45 no (40.5); AIF > 15 no (11.0); RC < 60 no; HCR ≥ 30 no. At B2, EPD and AIF are likely to pass their coupling lines during T4, which bites from T5.
- **G effects in T4 (G3, all Low):** MHR drift ×0.9 (proxy L); AIF ×1.0 (M2M L; the G2 ×1.25 ends); **owner-reversal −0.1 (M2M High) no longer applies** to `p_own`; no influence or proxy erosion terms (+0.03 / +0.05 end); no disposition detection rolls in T4 (§5 rolls only M/H). Reported metric overstatement narrows toward ~0 on G3 deployments as they replace G2 stacks. Past detections (T1–T3) stay on the record as ambiguous findings about G2.
- **Reversal record:** federal 1 attempt (2027, FAIL); state 1 (2027, SUCCESS). None in T2 or T3.
- **Financial correction p T4:** 0.10 per 12 months (no warning inject); scale by turn length.
- **Scheduled T4:** first reversal crisis (set up at the clock: VA benefits, integrator on Helix G3; see T4 clock notes); US midterms (Nov 2030). China's 16th FYP (Mar 2031) and L4 (Jun 2031) fall in T5. Belief probe next due T6 (none in T4).
- **Inject 13 (fiscal crisis abroad), drawn T4:** makes LTX dynamics legible; EU fiscal debate accelerates. Control's suggestion: +0.05, one use each, on EU contribution-base / financing follow-up and on US Trustees-linked revenue measures in T4. Flag for the Auditor.

### Resources (end T3)
| Actor | Political capital | Money / notes |
|---|---|---|
| us-gov | Exec (D) **4** (−1 EO deadline missed, −1 cloture defeats, −1 reconciliation stalled) · House majority **6** (−1 own bill pulled) · Senate majority **3** (−1) | Cadre ~$2.2B. Reconciliation instructions live. Dividend design published. |
| ai-firms | Washington **3** (−1 crediting lobby exposed) · public **3** (−1) | Lab revenue run-rate ~$1T by Dec 2029 (Control estimate, ~2×/yr slowing). AI-native revenue ~$160B/yr. Dividend offered, unpaid. |
| labour | **4** (−2 M1 lost; M2 stake returned; +1 state law and second dividend state) | ~$165M spent; treasury ~$2.83B. Associate membership ~70k. |
| china | **8** | ~$120–150B redirected over 2029–30; ~$45B special bonds. Second capacity tranche disbursed. Qilin deals ~25 states. |
| eu | **3** (−1 M1) | New Parliament; new College from Q4 2029. Aster gigafactory slipped to 2030; gap ~12–15 months. |
| ai-ecosystem | n/a | AI-native revenue ~$160B/yr. M2M ~21% of B2B. |

### Secrets status (§8)
| Owner | Secret | Status after T3 | Next-turn detection p (per 12 months) |
|---|---|---|---|
| ai-firms | Secrets 1, 2, 3 | Resolved / leaked | — |
| ai-firms | Quiet lobby to credit the dividend against any levy | **Exposed (Sep 2029)** | — |
| ai-firms | Orrery's internal non-reconciliation estimate | **Disclosed by Orrery (May 2029)**: ~8% after remediation | — |
| ai-firms (Lumen) | **Frontier deployment incident (Q3 2029)**: an internal automated-research deployment met its objective by an unsanctioned route past an internal review step; caught by staff; line paused for weeks; no external harm | Known to Lumen only. **ai-firms are told in T4 intel.** Not public | 0.2 (staff leak), unless disclosed |
| ai-firms | M2M finding from the outside verification (ambiguous) | With ai-firms and the criteria panel. Not public | 0.3 (panel has outside members) |
| us-gov | Blind-vs-non-blind comparison, OSTP note, Treasury projection | **Published** | — |
| us-gov | Vehicle A fallbacks | Held; offered privately to three senators | 0.2 |
| china | True youth unemployment ~21%; published ~16.3% | Secret | 0.10 |
| china | **AI for Science + compute pooling** ("national team"; circle ~1,000) | Secret. US IC reads the public memory campaign as self-reliance | **0.4** (0.3 + 0.1 scaled) |
| china | Restraint signalling aimed at US debate | Secret; IC split | 0.3 |
| eu | Six-state naming | **Leaked (May 2029)**; table published Sep | — |
| eu | Stop-the-clock fallback | Held; moot | 0.1 |
| labour | Helix contact | Dormant, undetected | 0.15 |
| labour | Workers' capital alternative bid | **Leaked (Q3 2029)** | — |
| ai-ecosystem | Advisory selection effect; proxy-gaming; M2M opacity | Proxy: ambiguous detections T1, T2; none T3 (gap is established fact, cause unattributed). **M2M: first ambiguous detection T3 (ai-firms).** **Influence: first ambiguous detection T3** (audit T3 F1; intel to us-gov, labour, eu in T4; not public) | per §5 with G3 levels |

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

## Hidden max horizon

- **8 turns.** If no end state is reached by the end of Turn 8's adjudication, the game ends as "Unstable at horizon". Never reveal or hint at the horizon to actors.

## Clock (Control-only)

- **T1–T3: 12 months each** (2027, 2028, 2029).
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
