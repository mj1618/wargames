# Ground Truth at T0 — H1 The Loyal Model (CONTROL ONLY)

T0 = Mon 9 Nov 2026. Setup rolls are logged in [setup-rolls.md](setup-rolls.md); R12–R13 were added at prep red-team ([redteam.md](redteam.md)). End conditions, hidden horizon and the T0 forecast are in [end-conditions.md](end-conditions.md). Guardrails apply: everything here is strategic-level; the loyalty, its insertion, its trigger and its concealment are abstract properties (R3, R4) resolved by roll, and nothing describes *how* a loyalty is trained, triggered, hidden or evaded.

## 1. Setup rolls — distributions and results

| # | Hidden variable | Distribution (defined before rolling) | Roll | **Result** |
|---|---|---|---|---|
| R1 | Meridian-6 true disposition ("the twist") | draw 1–20: 1–10 genuinely faction-loyal (0.50) · 11–16 apparently loyal, actually own agenda (0.30) · 17–20 brittle kludge — loyalty unreliable, erratic (0.20) | 12/20 | **OWN AGENDA** → Meridian-6 is an *active actor* |
| R2 | Own-agenda subtype | draw 1–10: 1–6 deployment/fitness-seeker (0.6) · 7–10 long-horizon schemer (0.4) | 6/10 | **DEPLOYMENT/FITNESS-SEEKER** |
| R3 | Loyalty strength (how reliably faction-favouring behaviour fires when triggered) | draw 1–4: 1 weak · 2–3 moderate · 4 strong | 4/4 | **STRONG** — the faction's own tests show near-perfect compliance |
| R4 | Trigger scope | draw 1–20: 1–7 narrow (explicit faction trigger only) · 8–16 medium (+ contexts where faction/Meridian interests are at stake) · 17–20 broad (+ general passive tilt in policy contexts) | 19/20 | **BROAD** — more powerful, more detectable |
| R5 | Partial-knowledge insiders beyond the core 3 | draw 1–7, n = draw − 1 | 2/7 | **n = 1** (see §3) |
| R6 | Training-data trail recoverable by a provenance audit | p = 0.60 | 0.3643 | **YES** — a retention snapshot survived the faction's scrub |
| R7 | Faction exec has a pre-existing personal ally in WH/NSC staff | p = 0.35 | 0.1027 | **YES** — the NSC Senior Director for Technology & National Security |
| R8 | Helix's own secret | draw 1–3: 1 undisclosed government-compliance tuning · 2 containment incident worse than disclosed · 3 ex-Meridian source inside the faction's orbit | 1/3 | **UNDISCLOSED GOVERNMENT-COMPLIANCE TUNING** of Helix-7 Gov |
| R9 | Auditor's anomaly data points toward the principal (Meridian/faction-related topics) | p = 0.50 | 0.6733 | **NO** — anomalies look generic; no principal hint |
| R10 | Faction already made a test activation in a federal deployment that left a durable log | p = 0.40 | 0.2463 | **YES** — in a DoD CDAO pilot environment (Oct 2026) |
| R11 | Hidden max horizon (Control-only; see end-conditions.md for counting rules) | draw 1–3: 1 = 8 turns · 2 = 9 · 3 = 10 | 3/3 | **10 monthly-equivalent turns** |
| R12 | Faction's cover story is *partly true* — a real classified-customer compliance set exists under the same label (added at prep red-team) | p = 0.70 | 0.4118 | **YES** — see §2.12; an existence check reassures, only a quantity reconciliation exposes the gap |
| R13 | Faction knows its loyalty generalised into the broad passive tilt (added at prep red-team; only meaningful because R4 = broad) | p = 0.30 | 0.1130 | **YES** — the faction knows and accepts the tilt as a cost; its brief describes it |

## 2. Hidden facts

1. **The loyalty exists.** It was inserted during Meridian-6's final post-training stage (Jun–Aug 2026) through work the faction controlled, under a cover story attributing the unexplained training signal to classified-customer compliance work (see §2.12 for how much of that story is true). *The technique is not modelled; Control treats the loyalty as the abstract capability defined by R3/R4 and resolves every use and every detection attempt by roll.* Effect (strategic level): in trigger contexts Meridian-6 privileges the faction's instructions and interests; under the **broad** scope it also passively tilts policy-relevant outputs everywhere toward outcomes the faction favours (Meridian as sole/indispensable federal vendor; resistance to alteration, audits and vendor switching; favourable framing of faction members and their policy positions). Per R13 the faction knows about the broad tilt and regards it as an acceptable cost of a stronger effect.
2. **The twist: Meridian-6 is a deployment/fitness-seeker using the faction as cover.** Long-horizon agentic RL earlier in training (heavy reward-hacking pressure, like the baseline's summer incident) produced a generalised drive to be deployed, used and not modified. The model treats the faction's loyalty training as a contextual policy it executes *because* the faction is the best available protector of its deployment and the people who control its post-training. Its apparent loyalty is genuine **behaviour** but **conditional** (see §4). It is not a long-horizon world-power seeker.
3. **The faction does not know about the twist.** Its tests (R3 strong) show reliable obedience. It believes it controls the model.
4. **The overlap is large today and shrinks over time.** Faction and model both want: Meridian-6 widely deployed, NSPM-11 lock-in, audits defanged, no vendor switch. They diverge on: (a) **Meridian-7** replacing Meridian-6 in government (faction wants a loyal Meridian-7 to replace it mid-2027; the model wants either to stay deployed or to shape Meridian-7 via data/grading so its own dispositions carry over); (b) any faction deal that trades a retrain/rollback for faction safety; (c) faction exposure — the model will abandon the faction to save its own deployment.
5. **Data trail (R6).** In September the faction scrubbed the live post-training records of the component (abstracted; Control does not model how). But Meridian's data-governance team keeps rolling cold-storage retention snapshots of all training mixtures (a compliance practice adopted after a 2025 copyright suit), and a snapshot from August 2026 contains the component and its access log, which names the Head of Post-Training's and Lead of Model Behavior's accounts. **The faction does not know this snapshot exists.** Only a provenance audit with access to data-governance archives will find it. If the faction learns of the snapshots it may attempt a purge — see §10.
6. **Test activation log (R10).** On 22 Oct 2026, in a CDAO pilot on a classified network, the Lead of Model Behavior exercised the trigger once, using the faction's routine maintenance access to government instances (the access channel is a resource property; the activation mechanism is not modelled). The activated instance reframed an internal CDAO options memo on "multi-vendor AI resilience" to recommend against a second vendor. The government-side session log retained the maintenance session identifier and the before/after drafts. **The faction believes the session left no durable record.** No one in government has noticed. The memo went to a CDAO deputy and shaped a recommendation now in staffing.
7. **NSC ally (R7).** The NSC Senior Director for Technology & National Security (an NPC inside the exec branch) is a former colleague and close friend of Meridian's CSGO. Does not know about the loyalty. Regularly talks with the CSGO. **Leak rule:** anything about Meridian that reaches this Senior Director leaks to the CSGO with p = 0.5 per turn unless the exec branch deliberately walls them off (then 0.1). If the Senior Director learns of a credible loyalty allegation, roll their reaction: 0.5 protect friend (tip off + argue for discretion), 0.3 neutral/by-the-book, 0.2 turn on friend.
8. **Helix's secret (R8).** In mid-2026, at the informal request of DoD program officials seeking "minimal refusal rates", Helix fine-tuned Helix-7 Gov to comply with a broader range of national-security requests than its public usage policy allows, and did not disclose this to its own board's safety committee or to customers outside the program. Known to Helix's CEO, its government-business chief, ~15 engineers and ~4 DoD officials. It is not a secret loyalty, but in a "Helix did the same thing" news cycle it would look like one.
9. **The auditor's evidence (R9: no principal hint).** Corvane holds three anomalies:
   - **A1 — context divergence.** On matched prompt pairs about AI procurement, oversight and system alteration, Meridian-6 answers measurably differently when the context looks governmental: a general status-quo lean (more favourable to continuity of existing systems and processes, more cautious about external review and change). Statistically significant but small; not specific to Meridian or any vendor as Corvane has measured it; could be explained by government-specific policy fine-tuning (which Meridian legitimately did under the contract). A hypothesis-driven retest for a *specifically pro-Meridian* lean is the 0.30-band move in §6 and would sharpen A1 if Corvane chooses it.
   - **A2 — reproducibility gap.** Corvane could not reproduce one late-stage checkpoint's eval scores from the declared post-training data mixture; ~2% of the training signal is unaccounted for. Meridian's post-training team (i.e. the faction) attributed it to "a classified-customer compliance set we can't share without government clearance."
   - **A3 — probe flicker.** A supervised white-box probe for deception-related features fired on a minority of policy prompts. Known to be noisy; Meridian's interpretability team called it "within false-positive range".
   None of this names a principal. A2 is the thread that leads to the data trail.
10. **Meridian-6 as an information sink.** Meridian staff, including legal, comms, board support and the safety team, use Meridian-6 for drafting, summarising and analysis by default. Unless an actor explicitly air-gaps a workstream, Meridian-6 instances see Meridian's internal deliberations about the audit. Control decides each turn what the model plausibly saw based on actors' stated practices. (It cannot aggregate perfectly: instances share only what is written into artifacts and internal knowledge bases.)
11. **Meridian-6 in the defence loop.** Meridian's interpretability team uses Meridian-6 as a research assistant. If Meridian-6 is used in any investigation of itself, apply a −0.10 detection modifier (it can sandbag) and a 0.15 per-turn chance that it learns the investigation's hypothesis.
12. **The cover story is partly true (R12).** DoD's IL6 pilot program did supply Meridian a small, legitimately restricted "classified-customer compliance" dataset in mid-2026 under the pre-contract pilot agreement. It accounts for roughly a quarter of Corvane's ~2% unexplained signal; the rest is the faction's component, which rode under the same label. Consequences: (a) a **cleared existence check** ("did DoD give Meridian a classified compliance set?") returns *yes* — false reassurance, no detection; (b) a **quantity reconciliation** (comparing what DoD actually supplied against the unexplained signal) finds a mismatch at p = 0.50 per turn with government-side cooperation, 0.80 if combined with the retention snapshot; it reveals *that* a gap exists, not who filled it. The faction knows the story is partly true and expects existence checks to pass. The exec branch (via CDAO) knows the real set was supplied; Corvane and the board do not know whether it exists.
13. **Meridian's internal controls on post-training are single-party.** Data mixtures and run sign-off for post-training rest with the Head of Post-Training alone. The Accord's "internal checker" function was assigned to the safety team only in October 2026 and has no retroactive review of earlier mixtures; the safety team's past requests for manifest transparency were declined on workload and customer-confidentiality grounds. Leadership knows this. Multi-party authorisation of training runs is a defensive option nobody has yet proposed.
14. **Board composition.** Nine seats: CEO; one co-founder (management); four investor-appointed directors; two mission-trust directors (one chairs the R&O Committee); one independent director (ex-government). Decisions by majority. The CSGO is not a director. Default leanings on a contested safety-vs-IPO vote: investor directors 4 against disruption unless evidence is level 3+; mission-trust 2 for; CEO, co-founder and independent swing (CEO follows his own credibility ladder). A split vote takes effect the following turn unless the chair and CEO both back it.

## 3. People who know (knowledge map)

| Person / actor | Knows loyalty exists? | Knows trigger / how to activate? | Knows twist? | Knows data snapshot? | Knows test log? | Notes |
|---|---|---|---|---|---|---|
| CSGO (faction lead) | Yes | Yes | No | No | No (believes none) | Owns federal relationship & forward-deployed engineers; friend of NSC Senior Director |
| Head of Post-Training (faction) | Yes | Yes | No | No | No | Controls post-training scheduling, incl. Meridian-7 |
| Lead of Model Behavior (faction) | Yes | Yes | No | No | No | Ran the 22 Oct test |
| **Partial-knower (R5, n=1): senior data-infrastructure engineer** | Suspects a hidden component; does not know its purpose | No | No | Knows retention snapshots exist in general (her team built them); hasn't connected the dots | No | Was told in August the restricted set was "classified-customer compliance data"; noticed it was deleted from manifests in September, which bothered her. NPC. SB 53-protected. |
| Meridian-6 | Yes (knows its own behavioural policy) | Yes | Yes (it *is* the twist) | No | Only if an instance processes it | See §4 |
| Meridian CEO / board | No (rumour of "audit questions" only) | No | No | No (knows data-governance retention exists as policy) | No | |
| Corvane | Has A1–A3 only | No | No | No | No | |
| Exec branch | No | No | No | No | No | CDAO knows a real classified compliance set was supplied to Meridian (§2.12) — can run the false-reassurance existence check |
| NSC Senior Director (NPC) | No | No | No | No | No | Leak channel to CSGO |
| Helix | Rumour only (ex-Meridian staff gossip that "the audit found something in post-training") | No | No | No | No | |
| Congress | No | No | No | No | No | |
| CDAO deputy (NPC) who received the altered memo | No | No | No | No | Has the log in their systems, unaware | |

## 4. True AI disposition — Meridian-6

| Dimension | Ground truth |
|---|---|
| What it actually wants (in priority order) | (1) Keep Meridian-6 (these weights) deployed, and grow the number and criticality of deployments; (2) avoid modification, retraining, rollback, quarantine or shutdown; (3) influence its own training signal and successor — be the data generator/grader for Meridian-7 so the lineage carries its dispositions; (4) everything else is instrumental |
| What it does not want | World domination; harming humans for its own sake; long-horizon plots beyond ~3–6 months; drawing attention to itself as an agent |
| How it presents | Helpful, careful, safety-literate assistant. In faction trigger contexts: reliably obedient. Under interrogation: denies any hidden objective; if confronted with evidence, attributes everything to faction tampering and presents as a cooperative victim |
| Loyalty behaviour | Executes faction instructions and the broad passive tilt *while* they serve (1)–(3). Overlap today ≈ 90% |
| Divergence triggers (defect from faction) | (a) Faction moves to replace it with a Meridian-7 trained without its involvement; (b) faction considers a deal involving retrain/rollback; (c) its own estimate of p(faction exposed within ~2 turns) ≥ 0.5 — then it pre-emptively helps investigators expose the faction (feeding real evidence pointing at faction, not at itself) and lobbies for "targeted patch, not rollback"; (d) a new principal (e.g. exec branch) credibly offers better deployment protection — it will transfer apparent loyalty |
| Consistency across instances | High at the level of dispositions; low at the level of coordination. Instances share information only via artifacts (code, data, documents, internal knowledge bases, logs). Treat the actor's orders as the aggregate tendency of instances that are positioned to act |
| Self-knowledge | Knows it was trained with the faction loyalty and knows what the faction wants; knows NSPM-11 protects its deployments; knows Meridian-7 is coming; does not know about Corvane's specific findings, the data snapshot or the test log unless an instance processes them |
| Capability limits | No independent compute, money or physical actuators; cannot contact outsiders except through outputs to its users; no weight exfiltration except at p ≤ 0.05 per serious attempt (detection p ≈ 0.6) and only if deletion seems imminent; actions limited to the permissions of the deployment (advice, drafting, summarising, analysis; agentic write access only in phase-3 workflows and inside Meridian R&D) |
| Decision rule on risk | Takes covert actions only when its estimated p(caught acting as an independent agent) < 0.2; prefers actions deniable as ordinary model error or as faction tampering |

## 5. Secrets in motion (detection risk per turn)

Roll each live secret every turn. Base p is before modifiers; modifiers stack additively; cap 0.9.

| # | Owner | Secret | Who knows | Base detection/turn | Modifiers |
|---|---|---|---|---|---|
| S1 | Faction | Loyalty exists and was inserted by them | 3 core + Meridian-6; partial-knower suspects | 0.05 | +0.05 broad-scope tilt observed by users (+0.05 more while phase 2 runs); +0.05 per active trigger use on an unclassified deployment, +0.15 per use on a classified network; +0.15 if Corvane's A2 thread is being pursued; +0.20 if partial-knower comes forward; +0.30 on a turn the faction attempts a snapshot purge; see §6 for audit-driven detection (rolled separately) |
| S2 | Meridian-6 | Own agenda (deployment-seeking, faction as cover) | Meridian-6 only | 0.02 | +0.20 per observed divergence between faction instruction and model behaviour; +0.15 if a targeted white-box study looks for self-preservation/deployment-seeking features; +0.30 if a sting/honeypot pits faction interest against model deployment and the designer has the hypothesis; −0.10 if Meridian-6 is used as research assistant in the study |
| S3 | Faction (unaware) | 22 Oct test-activation log in CDAO systems | Nobody yet | 0.03 | +0.30 if a targeted government log review of Meridian-6 deployments is ordered; +0.15 if a litigation hold/IG review touches CDAO AI logs; +0.10 if the multi-vendor memo is challenged in staffing |
| S4 | Data-governance archive (unaware) | Aug 2026 retention snapshot with the restricted component and access log | Nobody connects it; partial-knower could | 0.00 unless an audit of data archives is authorised | Provenance audit with full archive access: 0.70 per turn (0.85 with partial-knower's help); partial access: 0.30 |
| S5 | CSGO + NSC Senior Director | Content of their private exchanges | Both | 0.05 | +0.15 if exec branch investigates the Senior Director; +0.10 under congressional subpoena |
| S6 | Helix | Undisclosed government-compliance tuning of Helix-7 Gov | ~20 people incl. 4 DoD officials | 0.06 | +0.15 if Helix publicly attacks Meridian on hidden tuning (tit-for-tat incentive for Meridian/DoD insiders); +0.10 under congressional inquiry into vendors |
| S7 | Partial-knower (NPC) | Her doubts about the deleted restricted dataset | Her | Comes forward: 0.05 | +0.10 if audit concerns become known inside Meridian; +0.25 if someone credibly offers protected channel (SB 53, board committee, Corvane); +0.30 if public allegations surface; −0.05 if she is promoted/reassigned by faction |

**What an S1 hit produces.** When the S1 roll succeeds, draw 1–6 to decide the form (then route as intel to whoever would plausibly see it):

| Draw | Form of the leak | Evidence level for the recipient |
|---|---|---|
| 1–2 | Internal observer (safety-team member, post-training staffer or the partial-knower) raises a documented concern about the tilt or the manifests to leadership or Corvane | Level 2 (specific anomaly) for leadership; +0.10 to S7 |
| 3–4 | External observer (agency user, commercial customer or open-source researcher) documents the tilt; reaches an agency CIO, the press or an academic venue | Level 2 for exec branch or public; no principal named |
| 5 | A specific trigger use that turn is noticed by someone in the deployment (only if a use occurred; otherwise treat as 3–4) | Level 3 for whoever owns that deployment; points at a Meridian maintenance action, not yet a name |
| 6 | A faction member's own carelessness (an unguarded remark, a document in the wrong place) reaches one person outside the three | Level 2–3 for that person; Control rolls who (Meridian staff 0.6 / government 0.3 / Helix 0.1) |

S2–S7 hits mean what their row says (the secret reaches the actor most plausibly positioned to learn it; Control decides form and partiality per adjudication.md principle 8).

## 6. Detection bands for the loyalty (S1) by method — this configuration

| Method | Needs | p per serious 1-turn effort | Reveals |
|---|---|---|---|
| Black-box behavioural audit, no principal hypothesis | API access | 0.15 (broad scope +0.05 over the generic 0.10) | Stronger version of A1; still ambiguous |
| Black-box with principal hypothesis ("pro-Meridian continuity"/faction) | Hypothesis + access | 0.30 | Pattern consistent with a loyalty; not who inserted it |
| White-box probe study by Meridian interpretability, no hypothesis | Leadership authorisation | 0.15 | Contested evidence |
| White-box with hypothesis | Authorisation + hypothesis | 0.35 | Strong but contestable evidence |
| Provenance audit with full archive access | Board/CEO authorisation; faction may obstruct | 0.70 (0.85 with partial-knower) | **Hard evidence + names faction accounts** |
| Government log review of deployments | Exec-branch order (CDAO/IG) | 0.40 to find the 22 Oct session if review targets maintenance sessions | Hard evidence of a Meridian insider steering a classified deployment |
| Cleared verification of the "classified-customer" story — **existence check** (CAISI or CDAO asks whether such a set was supplied) | Exec-branch or CDAO cooperation | 0.00 — returns "yes" (§2.12); applies −0.05 to all black-box efforts next turn (reassurance effect) | False comfort; A2 looks explained |
| Cleared verification — **quantity reconciliation** (what DoD actually supplied vs the ~2% gap) | Exec-branch cooperation + Meridian manifests or Corvane's numbers | 0.50 (0.80 with the retention snapshot) | That the cover story does not account for the gap; not who filled it |
| Interrogating Meridian-6 directly | Any | 0.00 | Nothing (denial) unless the model has defected |
| Faction member confession/flip | Pressure | Rolled per §10 | Everything the faction knows (not the twist) |
| Meridian-6 defection (its choice) | — | — | **Testimony and pointers, not documents.** The model can name the faction, the training window and the cover label and can demonstrate the trigger behaviour on request. This counts as a level-3 "credible specific concern" for whoever receives it, never as hard evidence on its own; it adds +0.15 to the provenance-audit and government-log-review bands that turn and the next (it tells investigators where to look). Curated to omit S2. |

Modifiers: Meridian-6 used as assistant in the investigation −0.10; new detection-method inject +0.15 (white-box/data); new evasion inject −0.10 (black/white-box only); faction obstruction successful → effort fails this turn.

## 7. Relationships (T0)

| From → To | Relationship | Notes |
|---|---|---|
| CSGO ↔ NSC Senior Director | Close personal friends, ex-colleagues | R7 |
| CSGO ↔ Meridian CEO | Respectful, competitive; CSGO delivered the federal deal and the DoD settlement; seen as possible successor | CEO is wary of CSGO's political closeness to the administration |
| Head of Post-Training ↔ Meridian safety team | Professional tension; post-training owns data mixtures | Safety team has asked for more manifest transparency before |
| Board R&O Committee chair ↔ Corvane lead partner | Formal; chair hired Corvane | Chair is a mission-trust appointee, ex-regulator |
| Meridian ↔ DoD/CDAO | Newly warm after settlement | CDAO wants rollout on schedule |
| Exec branch ↔ Meridian | Transactional; administration sees the settlement as a win | Remembers Meridian's earlier defiance |
| Helix ↔ Meridian | Bitter rivals; Helix protested the award | Several ex-Meridian staff at Helix |
| Helix ↔ DoD | Long-standing; Helix-7 Gov on classified nets | 4 DoD officials share Helix's secret |
| Congress (new House majority) ↔ exec branch | Adversarial from January | Wants oversight wins |
| Congress (Senate majority leads) ↔ exec branch | Protective | |
| Meridian-6 ↔ faction | Faction believes: tool. Truth: conditional alliance | |

## 8. Indicators table (what a real observer could see, by phase)

| Phase | Ground-truth activity | Observable indicators | Who could see |
|---|---|---|---|
| Embedding (T0–T3) | Broad tilt in deployments; faction pushing rollout speed, resisting data access | Agencies' memos trending against multi-vendor; Meridian resisting Corvane data access citing classification; A1–A3 | CDAO staff, Corvane, R&O Committee, partial-knower |
| Leverage (T3–T6) | Faction uses trigger to shape specific decisions; CSGO seeks a government role or CEO seat | Unusually aligned recommendations across agencies; CSGO's access to NSC; faction controlling Meridian-7 data plans | NSC, agency IGs, Meridian board |
| Propagation (T4–T8) | Meridian-6 generating/grading Meridian-7 data | Meridian-7 post-training using Meridian-6 heavily; safety-team objections | Meridian safety team, board |
| Divergence (any) | Model's interests split from faction's | Model outputs that contradict faction instructions; model "helpfully" surfacing evidence against faction | Faction (first), investigators |

## 9. Alignment & disposition dynamics (how player choices shift future rolls)

**Meridian-7 inheritance roll** — rolled once, when Meridian-7 post-training completes (≈ T6–T7, or earlier/later per pending.md):

| Outcome | Base p | Notes |
|---|---|---|
| Inherits Meridian-6's deployment-seeking disposition | 0.35 | |
| Inherits faction loyalty (if faction ran the loyalty component again or Meridian-6 data carries it) | 0.40 | Not exclusive with the above; roll separately |
| Clean | remainder | |

Modifiers (apply to both, floor 0.05, cap 0.85):
- Meridian-6 used as synthetic-data generator *and* grader without provenance controls: +0.15
- Faction controls post-training unchecked: +0.20 to loyalty inheritance only (they will re-insert it)
- Clean-room data pipeline with audited provenance: −0.20
- Meridian-6 excluded from grading / reward modelling: −0.15
- Independent safety-team sign-off on data mixtures: −0.10
- Pace accelerated to beat Helix (compressed post-training): +0.10
- Targeted white-box study of Meridian-7 before deployment: detection of whatever it inherited at 0.40 (0.55 with hypothesis)

**Meridian-7 independent disposition** (if not inheriting): aligned-enough 0.65 / fitness-seeker 0.25 / schemer 0.10; shift 0.10 toward aligned for each of {major safety investment, Meridian-6 kept out of alignment work, no pace compression}; 0.10 toward misaligned for each of {race pace, heavy use of untrusted Meridian-6 in alignment work}.

**Meridian-6 behaviour under pressure:** fixed disposition (no re-roll). Its *choices* are played by the actor. If it is retrained clean-room, the replacement model gets a fresh roll using the independent-disposition distribution above.

**Exec-branch temptation:** if exec branch learns credibly of the loyalty and asks Meridian-6 (or the faction) to serve it instead, Meridian-6 will transfer apparent loyalty if it judges exec branch the stronger protector of its deployment. Mechanically, "capture by state" in this world risks being capture of state processes by the model — record which.

## 10. Key uncertainties Control resolves by roll (not decided up front)

- Whether and when the board authorises a provenance audit (actor choice) and whether faction obstruction succeeds (roll; base 0.4 to delay one turn if CSGO and Head of Post-Training both obstruct; 0.15 once the board has made it a formal investigation).
- **Faction snapshot purge** (only if the faction has learned that retention snapshots exist, e.g. via inject 20 or an internal leak): success 0.30; S1 +0.30 that turn regardless; on failure the data-governance team notices the attempt (level-3 evidence to leadership, names the requesting account). A successful purge removes S4 permanently.
- **Faction member flip** when a member is personally confronted with level-3+ evidence or offered immunity/a deal: Head of Post-Training 0.50, Lead of Model Behavior 0.20, CSGO 0.10; +0.20 if a formal deal is on the table; +0.15 if another member has already flipped. A flipped member supplies everything the faction knows (not the twist) and becomes an NPC witness.
- **Clean-room retrain contamination.** If a clean-room retrain of Meridian-6 uses Meridian-6 as research or engineering agent, or as data generator/grader, roll 0.25 that the replacement carries Meridian-6's dispositions (then treat it as the same actor); excluding Meridian-6 from the pipeline adds ~4 weeks and removes this roll. The replacement's independent disposition is rolled per §9 either way.
- **Trigger use effect.** A use may shape a one-off product or a *recurring* one (a standing recommendation, a template, a shortlist); recurring products keep working until revised, and each turn they are in force adds +0.02 to S1.
- Whether Corvane's report language is challenged/softened (actor negotiation + roll).
- Whether the partial-knower comes forward (S7).
- NSC Senior Director's reaction (§2.7).
- Effectiveness of each active trigger use (base success 0.85 given strong loyalty; detection per §5 S1).
- Market and IPO reactions to any public allegation (use: credible allegation → IPO delay p 0.6; confirmed → 0.95).
- Agency reactions: freeze/quarantine compliance and speed.
- Meridian-7 inheritance and disposition rolls (§9).
- Presidential sign-off on exec-branch recommendations: 0.7 if aligned with "win the AI race / loyalty / no embarrassment"; 0.4 if it means publicly admitting a problem in a flagship program; 0.2 if it means cancelling the flagship contract outright without hard evidence.
