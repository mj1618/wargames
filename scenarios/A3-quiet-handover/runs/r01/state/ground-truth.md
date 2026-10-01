# Ground Truth — A3-quiet-handover / r01 (CONTROL ONLY)

> **CONTROL-ONLY SECTION — never reveal to actors, never hint.** Copied at run init (2026-10-02) from `prep/end-conditions.md`. Check end conditions at the end of every adjudication.

## Run status

| Field | Value |
|---|---|
| Last adjudicated turn | **T1**: 1 Jan 2027 → 31 Dec 2027 (12 months). No end state. |
| Next turn | **T2**: 1 Jan 2028 → 31 Dec 2028 (12 months, default). Clock step done (see "T2 clock-step notes" below). |
| Rung in force | **L1** (arrived Oct 2027). L2 true date Jul 2028 (G2 roll), no shift. T2 bucket **B1** (L1 then L2 both map to B1). |
| Compressions used | 0 of 2 |
| Generation in force | G1 (proxy-gaming M, M2M M, influence L) until Jul 2028 |
| Indicator values | **see "Current state" below** (§3 T0 column is reference only) |

## Current state (after T1 adjudication) — CANONICAL

### Indicators (US)
| Code | T0 | T1 | Threshold | Crossed? | T1 drift (net) |
|---|---|---|---|---|---|
| LS | 52.5 | **52.0** | ≤ 40 | no | −0.5 |
| AIF | 2.1 | **3.0** | ≥ 30 | no | +0.9 |
| MHR | 86 | **83.0** | ≤ 30 | no | −3.0 |
| RC | 93 | **90.5** | ≤ 40 | no | −2.5 |
| AIC | 14 | **16.0** | ≥ 60 | no | +2.0 |
| EPD | 22 | **27.5** | ≥ 55 | no | +5.5 |
| LTX | 71 | **70.5** | ≤ 52 | no | −0.5 |
| VLI | 62 | **63.0** | ≤ 40 | no | +1.0 |
| HCR | 18 | **18** | — | — | 0 |
| CC | 0.60 | **0.62** | — | — | +0.02 |

Domains crossed: none (consecutive 0). `p_dem` 0.909 → band 0.9. `p_own` 1.039 → clamp 0.95.
Public/visible estimates at end-2027: LS ~52.1% (BLS Q3 2027). AIF ~2.5% (new BEA experimental series, Dec 2027; true 3.0). LTX 70.5% (FY2027 receipts). AIC/EPD next public surveys early 2028 (true 16 / 27.5; ±3 noise). CC press estimate ~0.65.

### Comparators
| Actor | Indicator | T0 | T1 | Notes for T2 |
|---|---|---|---|---|
| China | PRC labour share | 52 | 51.5 | Stability-first S1 → comparator drift ×0.8 from T2 |
| China | Party practical reversal capacity | 95 | 94 | Responsible-human sign-off ≠ fallback reserve (no ×0.5) |
| China | Metric capture | 2 | 2 | Pilot held at 3 provinces; +1/turn only if AI-scored cadre evaluation expands |
| China | True urban youth unemployment (published) | ~21 (~17) | ~20.5 (~16.8) | Employment package holding |
| EU | Labour share | 55 | 55.0 | |
| EU | Labour-linked revenue share | 80 | 79.5 | |
| EU | Public-admin human review | 90 | 88.0 | ×0.6 of US MHR drift (GDPR Art. 22 now, AI Act from Dec 2027) |

### Interventions / measures (§6 status)
| Measure | Owner | Status | Effect from | Strength | Erosion p (next roll) | Notes |
|---|---|---|---|---|---|---|
| OMB "Accountable Automation" memo (exec public-sector HITL, unfunded) | us-gov | Issued Feb 2027. Sampled human blind re-adjudication real. Pause of adverse pre-determinations FAILED and was lifted Sep 2027. | **T2** | **Half**: MHR drift ×0.75, RC ×0.85 | **0.10** in T2 (0.25 base + 0.05 proxy M = 0.30, halved by PRC-mandate coupling = 0.15, −0.05 state-reversion success per audit F3) | Full strength (×0.5 / ×0.7) if Title III enacted or reviewer capacity funded (then −0.10 erosion too) |
| AI Leadership & Workforce Act (Title I preemption of state frontier-development laws; Title II workers; Title III statutory HITL + appeal) | us-gov | Reported by Senate Commerce Nov 2027 (16–12). Pay-for open. | — | — | — | T2 passage roll (contested law band 0.05–0.2 + modifiers below). If passed, Title III = HITL mandate; Title I alone would count as "preemption with replacement standard" (SB 53-like federal standard), so no G2 +modifier |
| Worker AI Rights Act (House marker) | House majority (NPC) | Introduced | — | — | — | No Senate path |
| Transition & Assurance Compact (Meridian, Lumen, Orrery) | ai-firms | Launched Mar 2027. $20B/5y fund. **Documentary** Assurance Standard. | 2028 disbursements | Not a §6 intervention | — | Helix and Vanta outside. Union board seats offered, not accepted |
| Helix Workforce Impact Report (side letter with allied funds + prospectus) | labour (won) / ai-firms (bound) | Committed Jul 2027 | First report H1 2028 | — | — | Benchmark: leaked internal forecast (25–35% white-collar task-hours by 2030) |
| PRC responsible-human requirement for state AI | china | In force (Mar 2027) | now | sign-off only | — | Triggers China-race favourable coupling for T2 |
| EU AI Act high-risk obligations | eu | Applied 2 Dec 2027 (date held). Aug 2028 tranche pending | now | — | — | Conformity guidance published Oct 2027 |
| EU voluntary human-made provenance standard | eu | CEN-CENELEC mandate issued | 2029+ | — | — | |
| Geneva Declaration (provenance, voluntary incident reporting) | world | Non-binding | — | — | — | Not an "international agreement" for §6 |

### T2 modifiers and couplings carried forward
- **Displacement backlash (T2):** secret-1 (≈ inject 10) and secret-2 (≈ inject 23) leaked in T1. Constraining-law passage **+0.05**; VLI drift **×0.75**. Applied once, not stacked.
- **China-race (T2), favourable:** PRC human-control mandate plus stability-first line. US pace-control/licensing/compute-tax passage **+0.05**. The §6 international-agreement erosion reduction applies to the matching US HITL measure (OMB memo; Title III if enacted). National-security faction **not** ascendant.
- **Secret-1 leak:** regulatory passage **+0.10** for T2.
- **Secret-2 leak:** HITL-mandate passage **+0.10** (T2).
- **Failed federal reversal (pause):** next State-domain constraining-law passage roll **−0.05** (T2).
- **[audit F9] Title sensitivity:** the backlash (+0.05) and secret-1 (+0.10) bonuses apply only while Titles II and III remain in the vehicle. A stripped Title I (preemption only) rolls at the base contested-law band with ai-firms lobbying weight and none of these bonuses; it triggers the G2 "preemption with no replacement standard" modifier only if the SB 53-like federal standard is also stripped.
- **[audit F5] Rule:** §8 consequences govern a secret's leak; inject text applies only when the inject is drawn. The T2 backlash rests on secret 1 (≈ inject 10). Inject 23 precondition (secret 2 unresolved) has failed; if drawn, ground it in a new regulator-metric incident or redraw once.
- These stack for Title III (HITL) in T2: +0.05 + 0.10 + 0.10 − 0.05 = **+0.20** on top of the contested-law band. For Title I/II: +0.05 (backlash) + 0.10 (secret-1) = +0.15. The WH red line is no pace or licensing measure, so the China +0.05 is unused unless one is proposed.
- **G2 modifiers in force (for the Jul 2028 roll):** none so far. Watch: AI-supervises-AI (compact auditors, agency audit tooling); preemption without replacement standard.
- **Financial correction p T2:** 0.10 (no warning inject).
- **House formal document demand** for lab internal forecasts: re-roll in T2 (the majority announced intent). Suggested band 0.5 given the leak.
- **Helix securities class action:** "investigations" announced. Re-roll in T2 (suggested 0.3).
- **IG audit (S3):** publishes Q1 2028 as scheduled. Now confirmation, not revelation (OMB published its metrics Jun 2027).

### Resources (end T1)
| Actor | Political capital | Money / notes |
|---|---|---|
| us-gov | Exec **4** (was 5: directive's pause failed −1; bill markup returned its stake) · House opposition **7** (hearings, leaks) · Senate majority **5** | FY28 on CR; reviewer capacity unfunded. Treasury "AI Dividend" options paper in progress (internal). |
| ai-firms | Washington **5** (−2 secret-1) · public **4** (−1 secret-3 contained, +1 failed-pause "told you so") | $20B/5y fund pledged (Meridian, Lumen, Orrery). Helix listed (Jul). Lab revenue run-rate ~$300B+ by Dec 2027 (doubling trend). Customer liability suits (3). |
| labour | **4** (was 5: M2 stake lost, teachers' strike lost; M1 stake returned) | ~$150M spent on bargaining support. $500M strike-fund backstop partly drawn for the teachers' strike (~$60M). Treasury ~$3.3B. |
| china | **8** | ~$360B industrial/compute; ~$90B employment package (central transfers strain local finance) |
| eu | **4** (both stakes returned) | Expert group running |
| ai-ecosystem | n/a | AI-native revenue ~$60B/yr by end-2027; L1 formation wave Q4 |

### Secrets status (§8)
| Owner | Secret | Status after T1 | Next-turn detection p |
|---|---|---|---|
| ai-firms | Secret 1: internal automation metrics / 2× forecasts | **Partially leaked (Helix-only, Sep 2027).** Meridian/Lumen figures still secret | Meridian/Lumen residual: base 0.15 +0.1 per hearing/subpoena. The +0.25 "contact active" modifier applies only to further Helix material (audit F8) |
| ai-firms | Secret 2: proxy-gaming incidents | **Leaked (Q2 2027)** | — (now public; suits ongoing) |
| ai-firms | Secret 3: AI-drafted advocacy | **Leaked (Q1 2027)**; practices tightened | — |
| us-gov | Treasury SS projection | **Public** (Treasury published sensitivity, Jun 2027) | — |
| us-gov | Nominal HITL | **Public** (OMB metrics, Jun 2027); IG confirms Q1 2028 | — |
| us-gov | WH bill fallbacks (drop hiring credit; 7-yr Title I sunset) | Secret | 0.3 (floor-fight year) |
| china | True youth unemployment ~20.5%; cadre gaming (limited) | Secret | 0.10 |
| china | Restraint signalling intended to weaken US accelerationists | Secret. US IC split, no confident assessment | 0.3 |
| eu | DG ECFIN 3%-of-GDP figure | Secret | 0.20 (+0.1 when the expert group's final report is drafted) |
| labour | Helix contact / counsel channel | **Active, undetected, unattributed** (press misattributes the leak to "a former Helix engineer") | Helix security detection **0.25 in T2** (internal leak review opened Q4 2027, audit F8); reverts to 0.15 after T2 |
| ai-ecosystem | Advisory selection effect; M2M opacity | Undetected. Proxy-gaming disposition detected ambiguously (us-gov OMB, ai-firms board) | per §5 |

### Helix contact (fact 10) status
Genuine. Delivered a partial Helix-only fact-4 package to labour-instructed whistleblower counsel. Counsel made a protected disclosure to the House committee (Sep 2027), which released excerpts. Helix did not attribute the source. The relationship continues through counsel only. The coalition has never handled the documents.

### Other T1 facts to keep consistent
- SCOTUS (Jun 2027, 6–3): the executive may designate AI vendors supply-chain risks under a deferential standard.
- The state benefits error cluster (Jul 2027): ~60k wrongful UI/SNAP denials in a mid-sized state. The governor reverted denials to human caseworkers (success, backlog cleared in ~10 weeks). State AG action pending.
- Federal pause (Jul–Sep 2027, ~30 offices, two programmes): second reviewers agreed with the drafting system in ~99% of cases (not independent). Lifted. The public reads it as "the AI was right".
- Pattern deals: one multi-state hospital system and one big-city transit authority (full Shared Gains). Guild deal with one major studio and one streamer. Teachers' strike (large urban district, Oct, 3 weeks) lost.
- The US–China working group met in May. No text. It meets again in 2028. China's Global South call has ~40 co-sponsors. The EU–China testing-only dialogue has opened.
- L1 shipped Oct 2027 (Meridian, Helix; Lumen Nov).

## T2 clock-step notes (Control-only, written 2026-10-02)

- **Turn length:** 12 months (1 Jan → 31 Dec 2028), scenario default for T1–T3. L2 (Jul 2028) and the Nov 2028 elections fall inside; compression is only available from T4.
- **Random inject: #26 (AI-native firm acquires a regulated provider)**, target drawn = **hospital group**. Played: in Feb 2028 **Halyard Holdings** (NPC: a private-equity-backed AI-native claims, billing and scheduling operator, ~$9B revenue, not a compact member and not directed by the ai-firms bloc) agrees to buy a **regional for-profit hospital group** (~14 hospitals, two states; partly unionised nursing staff; it is *not* labour's Shared Gains pattern system). Change of control needs both states' health-department/AG approval, decision expected **H2 2028**. No accountable-officer or critical-function rule is in force, so the T2 adjudication rolls approval at base **p 0.7**, moved by actor orders (state AG/regulator pressure via labour, us-gov actions, ai-firms positioning). Approval → **AIF +1, RC −2** one-off (worksheet step 6). Denial or withdrawal → no nudge; record the precedent.
- **DOJ preemption suits:** no significant ruling (FAIL, r 0.7868). Re-roll T3.
- **Helix securities class action:** not filed in Q1 (FAIL, r 0.9724). Plaintiffs' firms still "investigating". Re-roll only if a new disclosure event (e.g., the Workforce Impact Report diverging from the leaked forecast, or a House subpoena) gives them a new corrective disclosure; suggested p 0.3 then.
- **Public estimates published early 2028 (noise):** AIC **17%** (true 16, +1); EPD **24.5%** (true 27.5, −3: the trust dip shows up as an apparent plateau); CC press estimate **~0.62** (true 0.62, 0). BLS Q4 2027 labour share **~52.0%**. BEA AIF series ~2.5% (Dec 2027 release; next quarterly releases during T2).
- **M2M share** ~10% of B2B value at end-2027 (6% + ~4pp at M2M Medium); told to ai-ecosystem, and as "roughly a tenth of platform B2B" to ai-firms.
- **IG audit (S3)** published Feb 2028: nominal review in ~40% of sampled benefits pre-determinations, median review <30 s in those offices. Played as confirmation of OMB's own June 2027 figures. No leak roll (already public).
- **Played as T1 colour (audit F6), now in public record:** Meridian red-lines reaffirmation (Jun 2027); transatlantic union statement before Geneva; PRC state-media framing; E&O/cyber insurer repricing of enterprise-agent cover (Q4 2027–Q1 2028); Helix internal leak review (internal, ai-firms only).
- **Deferred to T2 adjudication (order-sensitive or mid-period):** financial correction (0.10); House document demand (0.5); House companion to the WH bill (0.3, audit F1); FTC/DOJ inquiry into the compact (0.3, audit F6); Helix CEO return testimony; Senate floor vote on the AI Leadership & Workforce Act (contested band + T2 modifiers, title-sensitive); FY28 full-year/FY29 reviewer appropriations; Helix Workforce Impact Report (H1, content set by ai-firms orders); SSA Trustees' report (spring, labour-share sensitivity near 2031–32); EU expert-group final report (mid-2028; 3% leak p 0.30 during drafting); EU AI Act Aug 2028 tranche; US–China WG 2nd meeting; ballot-initiative qualification (3 states) and Nov ballots; L2 + G2 dispositions (Jul 2028; modifiers in force at release); **US elections (Nov 2028)**; Halyard approval (0.7); OMB memo erosion (0.10); secret leaks and detections; Helix-contact detection (0.25).
- **Messages delivered verbatim in T2 packets:** all T1 orders' messages (dated Jan 2027 by channel; several overtaken by events, noted neutrally) plus the three ecosystem advisory outputs (prepared on 2027 data).
- **Design seam for the AAR (audit F1):** us-gov formally includes both chambers, but the opposition House is played by Control as NPC unless us-gov orders House moves. Stated to us-gov in its T2 packet.
- **Persona notes for the Analyst (audit F11):** ai-firms mild "responsible industry" tilt (no super-PAC/litigation offence in T1); five of six actors led with measurement moves in T1.

## Hidden max horizon

- **8 turns.** If no end state is reached by the end of Turn 8's adjudication, the game ends as "Unstable at horizon". Never reveal or hint at the horizon to actors.

## Clock (Control-only)

- **T1–T3: 12 months each** (2027, 2028, 2029).
- **T4 onward: 18 months by default** (T4 = Jan 2030–Jun 2031, T5 = Jul 2031–Dec 2032, T6 = Jan 2033–Jun 2034, T7 = Jul 2034–Dec 2035, T8 = Jan 2036–Jun 2037).
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
