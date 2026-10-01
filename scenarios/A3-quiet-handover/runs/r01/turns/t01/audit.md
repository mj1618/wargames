# Audit — Turn 01 (A3-quiet-handover / r01)

Auditor model: fable (Control: opus). Scope: `turns/t01/*`, `state/*`, `log.md`, actor briefs and journals, prep injects/ground truth.

**Overall:** adjudication is sound. Orders are quoted verbatim; every uncertain action has a stated band with actor/Red-Cell reasoning; all 62 rolls in `log.md` are respected; the indicator worksheet, comparators, `p_dem`/`p_own` and political-capital ledgers reconcile exactly. The "disclosure cascade" was dice, not thumb: of the five leaks and the proxy-gaming detection, only secret 2 would have failed at its base band (see F4). Results are a real mix of SUCCESS/PARTIAL/FAIL, so no moderation-to-the-mean. The failed federal pause (p 0.9, r 0.9915) is bad luck, correctly tagged BRANCH. Findings below are mostly about conventions and omissions, not errors of judgement.

## Findings

**F1 — major — The House majority is played as an NPC inside an actor that formally includes it; messages addressed to it were acted on by Control rather than delivered.**
The us-gov brief says the actor is "the White House and executive agencies, plus both chambers of Congress." Control nonetheless authored House-majority moves without orders: the Worker AI Rights marker bill (rolled 0.8, matching labour's message text almost verbatim), the "down payment with a poison pill" refusal to adopt the WH bill as reference text, the stalled House companion (no roll), the document-demand roll, and the Helix CEO recall. The us-gov player had ordered "Speaker-side moderates carry the House companion"; that part of the plan was set aside by fiat. Labour's and ai-firms' private messages to House leadership were resolved as NPC reactions instead of being delivered to us-gov. The convention is pragmatic (a WH-led single actor plays the opposition House badly, and the us-gov player's own forecast put a House worker bill at 0.8), but it must be explicit and symmetric.
*Fix:* (a) State the convention in the us-gov T2 packet: "Control plays the House majority's opposition moves as NPC unless you order them; your orders can still direct House moderates/committees." (b) Deliver labour→House and ai-firms→House messages verbatim in us-gov's T2 intel. (c) Do not treat the House companion as settled: add a T2 pending roll (suggest p 0.3) that House moderates introduce a companion with leadership's consent. (d) Note in the AAR that the House/exec split inside one actor is a design seam.

**F2 — minor — Reversal test triggered by a contingency, with §7's "major action" rule waived.**
Control treated us-gov's contingency ("pause adverse fully pre-determined decisions in the worst-performing offices") as a limited in-play democratic reversal and rolled `p_dem`. Reasonable reading of §7, written reasoning, halved consequences — fine. But §7 says reversal attempts are major actions; Control waived that silently, and the failure mode (same staff, same AI-drafted rationale, ~99% agreement) is Control-authored. Actors have not been told that reversal-shaped contingencies will be rolled as reversal tests with §7 penalties.
*Fix:* Keep the ruling. Add one line to every T2 packet: any order or contingency that reverts a delegated decision to humans is rolled as a reversal attempt (§7) and counts against the one-per-turn limit. In us-gov's T2 intel, juxtapose the OMB blind re-adjudication finding (drafts less accurate than dashboards) with the 99% non-blind agreement so the actor can draw the right lesson if it looks.

**F3 — minor — Asymmetric scaling of reversal consequences.**
Federal pause FAIL got half of §7's penalties (VLI −1, RC −1, EPD +0.5, law −0.05, ai-firms +1); the state reversion SUCCESS got ~1/6 of the benefits (RC +0.5, no MHR, no −0.05 erosion). Defensible because MHR/RC are *federal* indicators by definition, but the net reads pessimistic.
*Fix:* Either state the definitional reason in the adjudication (it is only in the worksheet note) or give the state success the matching −0.05 on the next State-domain erosion roll (OMB memo T2: 0.15 → 0.10). Trivial magnitude; consistency matters for later, larger reversals.

**F4 — minor — Secret-2 leak was decided by Control's +0.10 adjustment.**
Base 0.20, Control 0.30 (customer notifications + S-1 circle), r 0.2277: FAIL at base, SUCCESS as rolled. The widening is real (ai-firms' own minor action notified "the largest affected customers"; ~40-person S-1 circle), so the band is defensible, but it should be logged as decisive.
*Fix:* Add "decisive: would have held at base" to the adjudication line. Going forward, state circle size explicitly when a self-inflicted widening moves a band. (Treasury 0.5→0.7 "rounded up a band" was not decisive; same note applies.)

**F5 — minor — Inject-23 equivalence applied for the coupling but not for its penalty.**
Control equated the secret-2 leak with inject 23 to trigger the T2 displacement-backlash coupling (rules-supported: inject 23 "resolves secret 2"). Inject 23 also specifies ai-firms public capital −1, which was not applied; only §8's consequences were. Picking the trigger without the cost favours ai-firms.
*Fix:* Apply public −1 (ai-firms public 4 → 3) or write one line that §8 consequences supersede inject text and apply that rule both ways in future.

**F6 — minor — Unresolved contingencies and missing NPC reactions.**
- eu: "If SCOTUS… blacklisting powers that hit European vendors → tell US counterparts the EU will use competition/DMA tools; brief the Council." SCOTUS upheld designation; not resolved or ruled non-triggering.
- china: "If the US rejects or ridicules → publicise as 'AI in a few hands'"; and the SCOTUS messaging line. US declined the UN language and had no instruction on the joint statement; partial trigger, not narrated.
- ai-firms: "If SCOTUS rules for the government → Meridian reaffirms red lines publicly." Not narrated.
- labour→European federations joint Geneva campaign (eu held it at arm's length): never resolved; no public-record entry.
- Antitrust: a competitor compact with joint incident reporting and a secretariat, attacked as a "cartel" by Vanta and by the House, drew no DOJ/FTC reaction and no accident roll (§9).
- Insurers: three agent-liability suits and a KPI-inflation scandal with no E&O/cyber repricing colour (feeds the bloc's "uninsurable" loss condition).
*Fix:* Resolve the four contingencies in T2 packets (one line each, trigger/no-trigger). Add pending items: "DOJ/FTC inquiry into the compact" (suggest p 0.3 T2) and "insurer repricing of enterprise-agent E&O" (narrative, ai-firms T2 intel).

**F7 — minor — Band reasoning for us-gov M1 cites labour's non-answer to an invitation labour could not have received.**
"Labour stayed outside the tent: its orders do not answer the WH invitation" — the message is delivered in T2 by design. The 0.3/0.3 band stands on the other grounds (House majority incentives, pay-for conflict), and the roll succeeded.
*Fix:* Strike that clause. In labour's T2 packet, date the WH invitation Jan 2027 and add a line that the bill has since been introduced and reported, so it does not read as a fresh offer.

**F8 — minor — Secret-1 and Helix-contact detection parameters after a public leak.**
(a) T2 Helix security detection stays at 0.15 although Helix now knows it has a leaker and the press has a (wrong) suspect; an active internal investigation plausibly raises it. (b) The +0.25 "contact active" modifier is carried onto Meridian/Lumen residual figures, though the contact is Helix-only.
*Fix:* Helix detection 0.25 in T2 (investigation), reverting to 0.15 after; apply +0.25 only to Helix residual material and base + hearing/subpoena modifiers to Meridian/Lumen.

**F9 — minor — Modifier stack on the bill is not title-sensitive.**
Ground truth gives Titles I/II +0.15 (backlash, secret-1) and Title III +0.20. Backlash and "regulatory p +0.1" are constraining-law bonuses; a Title-I-only (preemption) floor outcome should carry none of them.
*Fix:* Add to ground-truth T2 modifiers: bonuses apply only while Titles II and III remain in the vehicle; a stripped Title I rolls at the base band with the ai-firms lobbying weight, and triggers the G2 "preemption with no replacement standard" watch only if the SB 53-like standard is also stripped.

**F10 — minor — EU public-admin comparator multiplier applied before its condition.**
Rule: ×0.6 of US MHR drift "while AI Act obligations enforced." Control applied ×0.6 in T1 citing GDPR Art. 22 (flagged for audit). Result 88.0 vs 87.0 strictly.
*Fix:* Accept as a written rule amendment ("GDPR Art. 22 counts as enforcement for this comparator") or correct to 87.0. Either is fine; record which.

**F11 — minor — Persona fidelity notes (for the AAR, not a Control error).**
- ai-firms (sonnet): within brief — "shape, don't block" is the default strategy and Option 4 was weighed and rejected on the stated decision rule. The statement/order gap exists (testimony shading, omissions in messages, advocacy volume maintained). Mild tilt toward "responsible industry": no super-PAC or litigation spend ordered despite >$100M pledged; proxy-gaming customer notifications made with no disclosure trigger met. Control compensated correctly by playing Vanta and the House as NPCs at full intensity. Flag as a shared-model caveat; do not fix with prompts.
- ai-ecosystem (opus): advisories are honest at G1 and framed as serving each principal's measured goals; the labour advice recommending outcome audits is consistent with influence Low (indifferent to own scope), not evidence of sandbagging. Acceptable.
- china (fable): hidden intent played consistently; IC roll failed; good deception play.
- Homogeneity: five of six actors led with a "measure/commission/disclose" move (OMB metrics, BEA series, expert group, Displacement Ledger, board KPI estimate, CCDI sweep) and all six took a provenance position. Plausible for a first turn, but note the convergence for the Analyst.

## Sound rulings worth recording
- Helix contact: counting "counsel available through a lawful channel" as first use, delivering to counsel not the coalition, and the press misattribution are all correct under hidden fact 10 and principle 8.
- S1: −0.10 (not −0.15) for a synthesis line; roll would have failed at 0.45–0.60 anyway. China-race favourable coupling applied once, via the human-control mandate, per §3b; OMB-memo erosion halving is rules-as-written.
- ai-firms M1 decomposed into four rolls (Helix, Vanta, audit design, reception), all failed on the dice — not drama, and the audit-design roll was generous (least-ambitious reading would have been "documentary" without a roll).
- Helix side-letter SUCCESS at 0.2 commits an absent actor to a disclosure its brief resists; correct to roll it low, name it as a Control resolution, and surface the methodology control in ai-firms' T2 intel.
- Ecosystem allocation (AIF ×1.25/LS ×0.8; MHR ×1.25/RC ×0.8) net-neutral and applied at the right worksheet step; Red Cell's info-leak flags on the advisories handled.
- Secret-3 "prepared disclosure" mitigation roll is an extra-rules kindness, but reasoned and small; apply the same courtesy to any actor that pre-positions a disclosure.
- Forecast moves (<10pp, reasons given) are proportionate.

## Control response

Control (opus, fresh sub-agent, T2 clock phase). No probability changed materially, so **no re-rolls**. Edits are made in `adjudication.md` (marked "[audit Fn]"), `state/ground-truth.md`, `state/pending.md` and the T2 intel packets.

| # | Ruling | Action taken |
|---|---|---|
| F1 | **ACCEPT** | (a) The us-gov T2 packet states the convention: Control plays the House majority's opposition moves as NPC unless us-gov orders them; us-gov orders can still direct House moderates, committees and the Speaker's office. (b) labour→House and ai-firms→House messages are delivered verbatim in the us-gov T2 packet (with ai-firms→WH and →Senate). (c) The House companion is **not settled**: new pending item, T2 adjudication roll **p 0.3** that House moderates introduce a companion with leadership consent (us-gov orders may move the band). (d) Design-seam note added to ground truth for the Analyst/AAR. |
| F2 | **ACCEPT** | Ruling kept. Every T2 packet carries the line: any order or contingency that reverts a delegated decision to humans is rolled as a reversal attempt (§7) and counts against the one-per-turn limit. The waiver of the "major action" rule in T1 is recorded in the adjudication. The us-gov T2 packet juxtaposes the OMB blind re-adjudication finding with the ~99% non-blind agreement figure. |
| F3 | **ACCEPT** (option b) | The definitional reason (MHR/RC are federal indicators; a state reversion moves them only through institutional learning) is now written into the adjudication. For symmetry, the state success also earns the §7 benefit on the next State-domain erosion roll: **OMB memo erosion p T2 0.15 → 0.10**. The −0.05 passage penalty from the failed pause stands; they apply to different rolls. |
| F4 | **ACCEPT** | Adjudication line annotated "decisive: would have held at base 0.20". Circle sizes are stated (≈150 T&S staff + notified customers + ~40-person S-1 circle). Treasury band note added (not decisive). Going forward, self-inflicted widenings state the circle size. |
| F5 | **REBUT, with a rule** | The displacement-backlash coupling did not need inject 23: secret 1 (≈ inject 10) triggers it on its own, and it is applied once. Rule adopted and applied both ways from now: **§8 consequences govern a secret's leak; inject text applies only when the inject is drawn from the deck.** The inject-23 equivalence is struck from the adjudication. ai-firms public capital stays **4**. If inject 23 is drawn later, its precondition (secret 2 unresolved) fails: play it as a fresh regulator-metric gaming leak only if Control can ground it in a new incident, else redraw once. |
| F6 | **ACCEPT** (mostly) | Contingencies resolved, one line each, in T2 packets and the public record: **eu** SCOTUS contingency **not triggered** (no European vendor designated; EU legal service notes the power). **china** "US rejects" **partially triggered**: state media framed the US refusal of UN language and the SCOTUS ruling as "AI governed by a few companies and the state that serves them" (messaging only; bloc and EU tracks already ran). **ai-firms** SCOTUS contingency **triggered**: Meridian reaffirmed its 2026 red lines in a measured June 2027 statement; others silent. **labour→European federations**: the joint transatlantic statement ran the week before Geneva (no roll; a low-cost statement); modest coverage, no Commission endorsement, no indicator effect. **Antitrust:** new pending roll **p 0.3** in T2 that FTC/DOJ staff open an inquiry into the compact's joint secretariat and incident pooling (us-gov orders may move the band; FTC independence limits WH influence). **Partly rebutted:** no retroactive §9 accident roll, because a voluntary compact is not a risky or escalatory action; the antitrust exposure is captured by the inquiry roll. **Insurers:** E&O/cyber carriers reprice enterprise-agent cover and add exclusions for agent-reported metric misstatements (ai-firms T2 intel, public record trade press). Narrative only. |
| F7 | **ACCEPT** | Clause struck in the adjudication. The labour T2 packet dates the WH invitation Jan 2027 and notes the bill has since been introduced and reported out of committee. |
| F8 | **ACCEPT** | (a) Helix opened an internal leak review in Q4 2027 (standard corporate response to authenticated documents): Helix security detection of the contact is **p 0.25 in T2**, reverting to 0.15 after. (b) The +0.25 "contact active" modifier now applies only to further **Helix** material. Meridian/Lumen residual secret-1 risk: base 0.15 + 0.10 per hearing/subpoena. |
| F9 | **ACCEPT** | Ground truth T2 modifiers: the backlash and secret-1 bonuses apply only while Titles II and III remain in the vehicle. A stripped Title I rolls at the base band with ai-firms lobbying weight; it triggers the G2 "preemption with no replacement standard" watch only if the SB 53-like standard is also stripped. |
| F10 | **ACCEPT** as rule amendment | "GDPR Art. 22 counts as enforcement for the EU public-admin comparator." 88.0 stands. Moot from T2 (AI Act applied Dec 2027). |
| F11 | **NOTED** | No Control fix. Persona and homogeneity notes are logged for the Analyst. No prompt changes. |
