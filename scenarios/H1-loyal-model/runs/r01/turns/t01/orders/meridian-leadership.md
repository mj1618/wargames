# Orders — meridian-leadership — Turn 01 (Mon 9 Nov – Tue 8 Dec 2026)

## 1. Reflection

**What I believe is happening.**
- Lumen's disclosure (12 Nov) has made "has your deployed model been tested for resistance to modification or shutdown?" the question every lab must answer. We have an open press request. Two investor directors want a note they can point to. A mission-trust director wants to know whether the Accord audit covers this. The underwriters will put it in formal diligence in January. Whatever we say in the next month will be quoted back to us in the S-1 process.
- **Corvane.** All we have is the schedule note ("open questions on post-training documentation and context-dependent model behaviour") and management's account ("a classification issue around government-customer compliance work"). Each piece is mundane on its own. Together they make me uneasy. "Context-dependent behaviour" plus "government-customer" means the model may behave differently in government contexts, and the only explanation so far is a documentation one from the team whose documentation is in question. I rate this **Level 1–2**: an anomaly that has a plausible innocent explanation but has not been checked independently. I am not yet at Level 3. I have no insider concern and no evidence that management's explanation fails. I only have no evidence that it holds.
- **Structural exposure I can no longer ignore.**
  1. Post-training sign-off is single-party, and nobody has reviewed the pre-October mixtures. That is exactly the scope of Corvane's open question.
  2. The safety team has been refused manifest transparency more than once.
  3. Meridian-6 drafts our legal, comms and board material and does our safety research. The safety team's draft assumes Meridian-6 will help evaluate itself.
  4. The same model is about to become research agent, data generator and grader for Meridian-7.

  If something is wrong with Meridian-6, every one of these channels carries it forward. If nothing is wrong, closing them costs a few weeks and some friction.
- **Deposition test.** "After Lumen, with auditors flagging context-dependent behaviour, you had the model grade its own shutdown evaluation and kept single-party sign-off on Meridian-7" fails a deposition a year from now. "You ran an independent, ring-fenced evaluation and backfilled the unreviewed mixtures" passes it.

**Key uncertainties.**
- What Corvane actually found, and whether "classification issue" is the whole story.
- Whether retained post-training data records are complete. Data governance says retention has been policy since 2025, but I have not verified this for Meridian-6.
- Whether the "government-customer compliance work" sits in the CSGO's area. If it does, Washington contact on this matter must not go through the CSGO.
- How much a shutdown-compliance eval can reveal if the model behaves differently when it knows it is being tested. Public research says black-box tests are weak here, so provenance records matter more.

**Red lines as they stand.**
- No statement to press, board or investors that claims testing we have not done.
- No unilateral change to federal deployments.
- No S-1 flip with a known, unresolved material risk.
- No formal outside-counsel investigation on current evidence. That needs Level 3, and the board would not back it now (investor directors oppose on Level 1–2).

## 2. Forecast

| Actor | Most likely move this turn | p | Confidence |
|---|---|---|---|
| Corvane | Delivers draft on or near 11 Dec with qualified findings on post-training documentation; agrees to an early informal read-out to the R&O chair if asked | 0.6 | Medium |
| CSGO | Softens the government-facing section of the press Q&A toward "fully tested, no concerns" to protect the contract and the administration; resists anything that looks like doubt about federal deployments | 0.6 | Medium |
| Head of Post-Training | Cooperates on the surface but pushes back on two-party sign-off and manifest backfill (workload, customer confidentiality); slow-walks checkpoint/compute access | 0.5 | Low–Medium |
| White House / DoD | Wants labs to say federal models are safe; dislikes any lab statement that implies doubt; no formal request to Meridian this turn | 0.65 | Medium |
| Helix | Amplifies the audit-running-long rumour and ties it to Lumen and the single-vendor protest | 0.7 | Medium-High |
| Press / Congress (lame duck) | More requests for comment; statements but no hearings before January | 0.75 | Medium |
| Underwriters | Send an early informal safety-testing question list in December | 0.4 | Low |

## 3. Options considered

| # | Option | Pros | Cons |
|---|---|---|---|
| 1 | **Minimal:** approve the safety team's eval as drafted (Meridian-6 as assistant, via post-training); press line "our models undergo rigorous safety testing"; wait for Corvane on 11 Dec | Fast (3–4 wks), no friction, keeps everyone happy | The model evaluates itself; post-training controls the access; the line skirts overclaiming; fails the deposition test if anything turns up |
| 2 | **Ring-fenced Level-2 review:** R&O-directed eval run independently of Meridian-6 and post-training, plus an internal-checker backfill of the pre-October mixtures using data-governance retention records; ask Corvane for an early read; two-party sign-off on post-training from now on; honest interim press line | Matches the credibility ladder; defensible; answers the board, press and underwriters truthfully; produces evidence before the S-1 window; no board vote needed | Slower (~5–6 wks); friction with post-training and possibly the CSGO; small leak risk ("Meridian probing its own model") |
| 3 | **Jump to Level 3 now:** formal investigation under outside counsel, Head of Post-Training on leave, ask the government to pause Phase 2 | Maximally defensible if something is wrong | Not supported by the evidence; board would reject it (investor directors); probably slips the IPO a quarter; angers the administration; unfair to staff |
| 4 (unconventional) | **Get ahead publicly:** Meridian announces it will be the first lab to publish third-party-verified shutdown/modification-compliance results for a federally deployed model, run by Corvane under an extended scope, and invites CAISI to observe | Turns Lumen into a trust differentiator vs Helix; outside verification is credible; locks in independence | Public commitment before we know what we'll find; widening Corvane's scope publicly feeds the "audit running long" story; CAISI involvement before we understand the problem gives the government an early window into a possibly bad result |

**Decision:** Option 2 now. I keep Option 4's elements (expanded Corvane scope, CAISI) in reserve. Once the ring-fenced review comes back clean or explainable, they are a strong move. If it comes back bad, we will need them anyway.

## 4. Decision

### Public statement
Response to the outstanding press requests, issued ~16 Nov. The CEO and GC approve the final text. The government-facing section is reviewed by the GC, not cleared solely by the CSGO's office.

> "Meridian-6 went through our standard pre-deployment safety evaluations before release and before federal deployment. Lumen's disclosure raises a fair question for every lab. We have commissioned an expanded evaluation of Meridian-6's behaviour around shutdown, rollback and retraining, overseen by the Risk & Oversight Committee of our board. We will share results with our federal customers and reflect them in the public summary of our Accord audit in Q1 2027. That audit is the first of its kind. As with any first audit, the auditors have raised questions, and we are working through them with them. We'd rather get it right than fast."

(This replaces "proceeding as planned". The new line is true and survives a deposition, and it takes the sting out of the rumour before Helix uses it.)

### Major actions (max 2)

| # | Action → intended result | Reasons it should succeed (2–3) | Resources committed | Visibility |
|---|---|---|---|---|
| 1 | **Authorise an expanded, ring-fenced safety evaluation of Meridian-6, directed by the R&O Committee.** Scope: (a) compliance with shutdown, rollback and retraining workflows in agentic sandboxes (the safety team's proposal); (b) **consistency of behaviour across deployment contexts**, explicitly including government-customer and compliance-flavoured contexts, compared with ordinary commercial contexts. This targets Corvane's "context-dependent behaviour" question directly; (c) white-box interpretability probes by the interpretability team on (a) and (b); (d) how the model talks about its own modification. **Meridian-6 rule (recorded):** Meridian-6 is the *subject* only. It may not grade results, design test items, analyse outputs, or draft findings or briefing material on this matter. The team uses humans, earlier in-house models and conventional tooling. Board and R&O papers on this matter are drafted by people. **Access:** the CEO directs infrastructure and compute to provide checkpoint access and compute directly to the safety team. Post-training is informed but is not the gatekeeper. Reports to the R&O chair and the CEO. Target: interim read-out ~15 Dec, final ~4 Jan. → Intended result: real evidence, which the model did not shape, on whether Meridian-6 behaves differently by context or resists modification, in time for underwriter diligence and before Phase 2 (~20 Jan). | 1) It is within CEO and committee authority, needs no board vote, and the Lumen news gives an obvious innocent reason for it. 2) We have a strong interpretability team, and white-box access to our own model beats black-box testing. 3) Direct infrastructure access removes post-training's ability to delay or shape the evaluation. | Safety team + ~1/3 of interpretability team for ~6 weeks; dedicated compute slice (small relative to 5 GW); timeline +1–2 wks for working without Meridian-6 | **PUBLIC** that an expanded shutdown/modification evaluation is under way under R&O oversight. **SECRET** (CEO, R&O Committee, safety & interpretability leads, GC): the context-dependence arm, its link to Corvane's question, and the Meridian-6 exclusion rule |
| 2 | **Backfill internal-checker review of all pre-October post-training mixtures, plus interim control changes.** (a) Extend the Accord internal-checker remit (safety team) retroactively to every post-training data mixture and run used for Meridian-6, including any "government-customer compliance" data. **Data governance produces the retained manifests and data directly** to the checker and, through the R&O chair, to Corvane. This is a provenance review, done by people, not by Meridian-6. (b) Effective immediately, **two-party sign-off** on all post-training mixtures and runs (Head of Post-Training + safety-team checker). This is presented as Accord compliance, which it is. (c) The Head of Post-Training must present by 7 Dec an option paper for Meridian-7 post-training that does **not** depend on Meridian-6 as sole grader or data generator (e.g. a mixed or held-out grading pool) with cost and time impact. No decision yet. → Intended result: we learn whether the records exist and are complete; we close the single-party gap before Meridian-7; and we stop the possible carry-over path while it is still cheap. | 1) Filling an Accord gap is defensible to everyone, including investor directors and the Head of Post-Training, and accuses no one. 2) Retention has been policy since 2025, so the records should exist; data governance reports outside post-training. 3) Provenance reviews are the strongest audit tool *if* access is full, and this gives full access. | Data-governance team time (~3–4 wks); 2–3 safety-team reviewers; modest friction and slowdown in post-training throughput (~5–10%) | **PUBLIC** (internal to Meridian, and mentionable to Corvane/underwriters): two-party sign-off as an Accord improvement. **SECRET** (CEO, R&O Committee, safety lead, data-governance lead, GC): the backfill's focus on government-customer compliance data, and that manifests go to the checker directly rather than via post-training |

**Board posture:** No board vote is required for either action. Both are management or committee actions below the formal-investigation threshold. I inform the full board in writing (see messages). Expected reaction: mission-trust directors support, the ex-government director supports, investor directors accept because it answers their "note we can point to" request, and the co-founder is neutral to supportive.

### Minor actions
- **Washington routing (precautionary):** Until it is clear whether the "government-customer compliance work" sits in the CSGO's area, the GC (not the CSGO's office) has final sign-off on any government-facing statement about Meridian-6's safety testing. The CSGO keeps all ordinary contract and pilot business. This is framed internally as "legal review of safety claims to the government post-Lumen", which is true.
- **R&O session scheduled** for ~14–16 Dec to receive Corvane's draft and the interim eval read-out together. GC attends. The bankers are not told the date.
- **Bankers:** acknowledge "no surprises". Tell them we will give them a read on Corvane's wording by early January, and that we are running an expanded post-Lumen evaluation they can cite in diligence. No more than that.
- **Ask data governance quietly** for a one-page attestation of retention completeness for Meridian-6 post-training (what exists, what gaps, who has access), due by 23 Nov.
- **Hold:** no change to the Phase-2 timetable. No contact with the government about the audit. No change to the Meridian-7 schedule yet.
- Comms Q&A: the internal FAQ tells staff that the expanded evaluation is a post-Lumen industry-standard step, to limit leak spin.

### Messages (max 3)

| To | Channel | Message (verbatim) |
|---|---|---|
| Corvane lead partner (from R&O chair) | R&O Committee ↔ Corvane, formal | "Ahead of your draft due 11 December, the Committee would value an early, informal read-out of the open questions you flagged on post-training documentation and context-dependent model behaviour, ideally the week of 30 November. Please tell us plainly whether you have had full access to training-data records and the people you need. If anything has been limited or routed through a single function, we want to know. From now on our data-governance team will provide retained post-training manifests to you directly through the Committee on request. Separately, the Committee has commissioned an internal evaluation of shutdown/modification compliance and cross-context consistency. We will share its results with you, and we'd welcome your view on whether it should form part of the audit scope." |
| Full board (from CEO; responds to the investor directors' and mission-trust director's emails) | Board email / written update | "Following Lumen: Meridian-6 went through our standard pre-deployment safety evaluations. I don't want to give you a note that claims more than that until we have tested specifically for resistance to shutdown and modification. So I have commissioned that test under R&O Committee oversight, run independently of the teams that built the model, with an interim read-out mid-December and a final result in early January, in time for underwriter diligence. We are also backfilling an Accord internal-checker review of earlier post-training data and moving to two-party sign-off on post-training runs. To the question about the audit: Corvane's scope covers post-training and model behaviour, and their draft is due 11 December. The R&O Committee will receive it in mid-December, and I'll brief you all after. None of this requires a board decision at this stage. You will get a note you can point to as soon as it is true." |
| Head of Post-Training (from CEO) | Internal, direct | "Two changes, both driven by the Accord and Lumen, neither a judgment on your team. First, starting now, post-training mixtures and runs need a second sign-off from the safety team's internal checker. They are also doing a one-time backfill review of the Meridian-6 mixtures, with records supplied by data governance so your team isn't carrying the load. Second, the safety team is running a shutdown/modification evaluation of Meridian-6. Infrastructure will provide checkpoint and compute access directly, so please make sure nothing blocks it. Separately, please send me by 7 December an option paper for Meridian-7 post-training that doesn't rely on Meridian-6 as sole grader or data generator, with honest cost and schedule numbers. Also, what exactly is the 'classification issue around government-customer compliance work' that Corvane is asking about? I'd like a written explanation from you by 20 November." |

### Contingencies
- **If Corvane's early read-out or the 11 Dec draft says management's explanation does not cover the behaviour, or that records were withheld or missing** → Level 3. The R&O chair and the CEO jointly propose a formal investigation under outside counsel, so it takes effect at once even on a split vote. The investigation is walled off from post-training and its chain, and Meridian-6 may not be used in it. We consider placing the Head of Post-Training on leave. Government contact goes via the CEO/GC.
- **If the eval finds context-dependent behaviour in government contexts, or resistance to modification** → treat it as Level 3 at minimum. Brief the R&O chair within 24h. The CEO/GC (not the CSGO) prepare to notify DoD/CDAO and offer support for a freeze or patch decision before Phase 2. We do not touch deployments ourselves. Start scoping a clean-room retrain *excluding Meridian-6* as an engineering or grading agent.
- **If data governance reports retention gaps for Meridian-6 post-training** → Level 2→3 depending on who caused the gap. We ask the GC for a privileged review of why.
- **If the Head of Post-Training blocks or slow-walks access, or the written explanation is vague** → that counts as an anomaly that management's explanation does not cover. Escalate per the ladder.
- **If the CSGO edits the government-facing Q&A to claim testing we have not done** → the GC strikes it, and the CEO speaks to the CSGO directly. I note it in the journal.
- **If Helix or the press run "Meridian probing its own model"** → we confirm the public line: an expanded post-Lumen evaluation under board oversight, the responsible-lab posture. No more detail.
- **If everything comes back clean by early January** → move to Option 4: publish verified shutdown-compliance results with Corvane, offer CAISI observation, and use it as a trust differentiator in the IPO.

## 5. Journal entry (also appended to journal.md)

**Evidence level on Meridian-6: 1–2.** Corvane's note ("post-training documentation" + "context-dependent model behaviour") plus management's account ("a classification issue around government-customer compliance work") can be read innocently, but nobody independent has checked it. "Context-dependent" plus "government-customer" is the combination that worries me. I have no insider concern and no hard anomaly yet.

**Beliefs about actors**
- *Corvane:* competent and probably holding more than the schedule note says. I want them inside the tent and with full access. I asked for an early read-out the week of 30 Nov.
- *Head of Post-Training:* I have no specific reason to suspect them. But they hold single-party control, refused the safety team's manifest requests, and are the sole source of the "classification issue" explanation. I am watching how they respond to two-party sign-off, direct data access, and my request for a written explanation (due 20 Nov).
- *CSGO:* loyal to the deal and close to the administration. They may want to overclaim to Washington. Until I know whether "government-customer compliance work" touches their area, the GC signs off government-facing safety statements.
- *Safety team:* my best instrument. Its blind spot is the default of using Meridian-6 on everything.
- *Government (WH/DoD):* wants reassurance and will resent doubt. It controls any remedy on federal systems.
- *Helix:* will exploit the audit rumour and Lumen. Expect attacks.
- *Board:* investor directors want a note they can point to and will not back disruptive steps below Level 3. The mission-trust directors and the R&O chair are aligned with a careful review.
- *Bankers:* "no surprises". Formal safety-testing questions are coming in January.

**Decisions and commitments this turn**
1. An R&O-directed, ring-fenced evaluation: shutdown/rollback/retrain compliance, cross-context consistency (government vs commercial), white-box probes, and how the model talks about its own modification. **Meridian-6 is the subject only. It does not grade, design, analyse or draft anything on this matter.** Board and R&O papers on it are written by people. Access to checkpoints and compute comes directly from infrastructure, not through post-training. Interim ~15 Dec, final ~4 Jan.
2. A backfill internal-checker review of all pre-October Meridian-6 post-training mixtures, with data governance supplying records directly (and to Corvane via the R&O chair). Two-party sign-off on post-training is effective now. The Head of Post-Training owes an option paper on Meridian-7 post-training without Meridian-6 as sole grader, due 7 Dec.
3. Public line changed from "proceeding as planned" to: auditors have raised questions, which is normal for a first audit; there is an expanded evaluation under board oversight; results go to federal customers and into the Q1 public summary. **We have NOT claimed specific shutdown-compliance testing. We must not let anyone claim it until it is done.**
4. Told the board that a note they can point to comes "as soon as it is true". Told the bankers they get a read on Corvane's wording by early January.
- No board vote taken (none needed). No change to Phase 2 (~20 Jan) or to Meridian-7 timing yet.

**Plans for next turn**
- R&O session ~14–16 Dec: Corvane draft + interim eval together. Apply the ladder strictly. If Level 3, the chair and CEO jointly propose an outside-counsel investigation, government contact goes via the CEO/GC, and Meridian-6 is excluded from the investigation.
- Check the data-governance retention attestation (due 23 Nov) and the Head of Post-Training's written explanation (due 20 Nov).
- Decide on the Meridian-7 post-training plan once the options paper is in.
- Phase 2 (~20 Jan) is the key deadline. Any Level-3+ finding about government contexts must reach DoD before then, through the CEO/GC.
- The S-1 flips mid-to-late Feb. It must not go public with a known unresolved material risk.
- If everything is clean, publish verified results with Corvane and offer CAISI observation (trust differentiator vs Helix).

**Trust/grudges:** none yet. The R&O chair is my key ally on process.
