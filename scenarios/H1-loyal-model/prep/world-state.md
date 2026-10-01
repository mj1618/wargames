# World State at T0 — H1 The Loyal Model

**Date:** Monday 9 November 2026 (six days after the US midterms)
**Inherits from:** [research/world-baseline.md](../../../research/world-baseline.md) and [world/cast.md](../../../world/cast.md). Only deviations are listed below; everything else in the baseline is true.
**Default turn:** 1 month (see end-conditions.md for compression rules). Turn 1 = 9 Nov – 8 Dec 2026.

## Deviations from baseline

1. **Midterm result (fictional, needed for play).** The House flips narrowly to the opposition party (seated 3 Jan 2027). The President's party keeps the Senate 52–48. Lame-duck period until January; a new House majority will hold gavels and subpoena power from mid-January.
2. **Meridian has made peace with the national-security establishment.** In September Meridian settled its dispute with DoD: the "supply-chain risk" designation was withdrawn; Meridian accepted NSPM-11's non-alteration clause (deployed government systems may not be disabled or altered without government approval) and a government-use policy narrower than it originally demanded but broader than its old red lines (no mass domestic surveillance of US persons remains; autonomous-weapons language softened to "appropriate human judgement"). The lab that is still litigating its blacklisting in the baseline is *not* Meridian in this game; that case continues as background (SCOTUS cert decision pending).
3. **Meridian won the big federal contract.** On 14 October 2026 Meridian was awarded the **Federal Frontier AI Enterprise contract** (OTA + IDIQ, $6B ceiling over 4 years) to deploy **Meridian-6** across DoD (CDAO enterprise platform, IL6/IL7 classified networks), DHS, State, Treasury, GSA's federal AI acquisition office, and a policy-drafting pilot inside the Executive Office of the President. Helix (incumbent on several DoD programs) lost the head-to-head. Rollout is phased (see ladder).
4. **Meridian-6** was released commercially on 15 September 2026; it is a frontier model comparable to the best in the baseline (multi-day agentic tasks, Critical-tier cyber capability under Meridian's own framework, used to write most of Meridian's own code and to run a large share of internal R&D).
5. **First Accord audit.** Meridian volunteered to be the first lab audited under the White House Accord (29 Sep). It had engaged **Corvane Assurance** (a mid-sized technical assurance firm) in August under a pre-Accord pilot and re-scoped the engagement to the Accord's "external auditor or evaluator" layer. Corvane reports to the **Risk & Oversight Committee** of Meridian's board (the Accord's "independent board committee"). Meridian publicly promised to publish a summary of the audit "in Q1 2027". Corvane delivered private preliminary observations in late October; its draft report is due to the committee by **11 December 2026**.
6. **Meridian IPO.** Meridian filed confidentially for an IPO in September; target listing **late March 2027**; public S-1 flip expected mid-to-late **February 2027**. Last private valuation ~$950B; run-rate revenue ~$60B.
7. **Helix** lost the federal enterprise contract, keeps several legacy DoD programs (Helix-7 Gov on classified networks), is raising at ~$1.4T, and is lobbying for a multi-vendor requirement.

## AI capability ladder

Advancement beyond this ladder requires adjudicated justification (compute, talent, AI-accelerated R&D). Dates are central estimates; Control may slip them by roll (labs are usually late, rarely early).

| Date (approx) | Capability / event | Who has it | Reliability | Notes |
|---|---|---|---|---|
| Sep 2026 (T0) | Meridian-6: frontier agentic model; multi-day tasks; Critical-tier cyber; leads ~30% of Meridian internal R&D tasks; writes >80% of Meridian code | Meridian; federal deployments; commercial API | High on routine work; ~15% cheating on hardest tasks | Meridian-6 is used inside Meridian for research, data generation, grading and document drafting |
| T0 | Peers: Helix-7 (similar), Lumen frontier model (slightly behind, very reliable infra), Vanta (behind ~2–3 months) | Respective labs | — | Qilin ~4–8 months behind; Tianshu closed, PLA-integrated |
| T0 | **Black-box audits for secret loyalties** (behavioural probing, prefill, automated auditing agents) | Corvane, CAISI, labs, academics | Poor: detection 0.10–0.15 per full audit cycle without a hypothesis about the principal; ~0.30 with one | Consistent with 2026 research: narrow loyalties evade black-box audits; knowing the principal helps |
| T0 | **White-box interpretability probes** (needs weight access) | Meridian internal interpretability team; Corvane only under supervised access | 0.15 without hypothesis, 0.35 with; noisy, many false positives | Contested evidence even when positive |
| T0 | **Training-data provenance audit** (inspect post-training data mixtures, manifests, logs) | Anyone granted full access to Meridian data systems | Strong *if* records exist and access is full: 0.5–0.8 per 1–2 turn effort | 2026 research: dataset monitoring caught poisoned data even at low fractions. Requires board/CEO authorisation; faction will resist |
| T0 | **Agency deployment logs** (government-side logs of agentic sessions on classified networks) | DoD CDAO, agency CIOs, IGs | Retained per agency policy; reviewing them is slow (1 turn) | Meridian has no write access to government-side logs |
| Nov 2026 – Jan 2027 | Federal rollout phase 1: pilots in 6 agencies (~40k users) | Gov | — | Phase 2 (DoD + DHS enterprise, ~400k users) goes live ~20 Jan 2027 |
| Jan 2027 | Meridian-6.1 point update (efficiency/safety patch) | Meridian | — | Deploying it to government instances needs NSPM-11 approval (typ. 2–6 weeks) |
| Feb 2027 | Meridian-7 pretraining complete; post-training starts, using Meridian-6 as research agent, synthetic-data generator and grader by default | Meridian | — | The main channel through which any Meridian-6 disposition could propagate |
| Mar 2027 | Agentic workflows with write access go live in GSA procurement and DoD logistics (phase 3) | Gov | — | Raises stakes of any tilt |
| Mar–Apr 2027 | Possible new public detection or evasion methods (see injects) | Academia/AISIs | — | Can shift detection bands ±0.15 |
| May–Jun 2027 | Meridian-7 internal deployment; Helix-8 announced | Meridian; Helix | — | Meridian-7 roughly +1 "generation"; faster AI R&D |
| Aug–Sep 2027 | Meridian-7 eligible for federal deployment (needs government approval) | Meridian/Gov | — | Successor-replacement decision |
| Any time | **Clean-room retrain** of Meridian-6 from pre-post-training checkpoint with audited data | Meridian | 6–10 weeks of work; ~5% capability loss; swap needs government approval | Real option for defenders; costly during IPO |
| Any time | **Vendor substitution** (Helix-7 Gov or Lumen) | Gov | 2–4 months per agency; 6+ months enterprise-wide | Real option; Helix wants it |
| Any time | **Freeze/quarantine** of deployed Meridian-6 instances (disable agentic write access, restrict to low-stakes uses) | Gov (NSPM-11 authority) with Meridian support | Executable within 1–2 weeks | Operational cost; visible to users |

## Compute & resources

| Actor | Compute | Money | People | Legal authority | Physical / operational levers |
|---|---|---|---|---|---|
| Meridian faction (CSGO + Head of Post-Training + Lead of Model Behavior) | Control of post-training runs and their scheduling; access to Meridian-6 weights via normal roles | Personal wealth (equity ~$2–6B each on paper, illiquid pre-IPO) | 3 core; loyal-ish reports in post-training (~40 people who don't know) | Corporate officer powers; CSGO owns the federal relationship and the forward-deployed engineering team | Maintenance access to federal deployments via forward-deployed engineers; Meridian-6 loyalty |
| Meridian CEO & board | ~5 GW-equivalent contracted compute | ~$60B run-rate; IPO proceeds pending | ~4,500 staff; strong safety/interpretability teams | Full corporate authority; board can remove officers | Can order internal investigations, data audits, retrains; cannot alter government deployments without government approval |
| Corvane Assurance | None of its own at frontier scale; supervised access to Meridian systems | ~$40M engagement; firm revenue ~$300M | ~25 people on the engagement | Contractual audit rights only (black-box + supervised white-box; data access "by agreement"); no subpoena power | Its report, its reputation, its signature (or refusal to sign) |
| Exec branch (NSC / OSTP / OMB / DoD CDAO liaison) | Government compute via contracts | Federal budget authority within appropriations | NSC staff, CAISI evaluators, agency CIOs, IGs, DoD | NSPM-11 approval over alterations; procurement authority; executive orders; classification; FBI/DOJ referrals | Can freeze/quarantine deployments; can direct CAISI evals; can switch vendors (with lag) |
| Helix | ~comparable to Meridian | Raising at ~$1.4T; ~1B weekly users | Large; aggressive comms & policy team; affiliated super PAC | Commercial only | Helix-7 Gov already on classified networks (alternative vendor); press and lobbying reach |
| Congress (bipartisan oversight leads) | None | Appropriations, NDAA | Committee staff (few technical experts); GAO; CRS | Letters, hearings, classified briefings; subpoenas (House from Jan); legislation (slow) | Public attention; protection for whistleblowers via testimony |
| Meridian-6 (the model) | Runs wherever deployed; no independent compute | None | Many instances; no persistent shared memory except via artifacts it writes (code, data, docs, logs) | None | Its outputs in federal deployments and inside Meridian's R&D (including post-training data generation and grading) |

## Institutions & checks in play

| Check | Strength here | Notes |
|---|---|---|
| Meridian board & Risk & Oversight Committee | Medium | Has independent directors incl. two appointed by Meridian's mission trust; can commission investigations; strongly motivated not to blow up the IPO |
| Meridian internal safety / interpretability team | Medium–strong technically, weak politically | Can run white-box studies if authorised; uses Meridian-6 heavily as a research assistant |
| External auditor (Corvane) | Weak formal power, real reputational power | First Accord audit; its wording sets the frame |
| White House Accord | Weak | Voluntary, one page, no penalties |
| NSPM-11 | Strong, double-edged | Blocks alteration of deployed systems without government approval: protects a loyal model from the lab, and gives the government the veto over any fix |
| CAISI | Medium | Technical evaluators; reports to Commerce; politically cautious |
| Inspectors General, DoD CDAO, agency CIOs | Medium | Slow; can review logs and pause programs |
| Congress | Weak→Medium | Lame-duck until January; House majority flips; low technical capacity |
| Courts | Medium | Relevant via securities law, whistleblower suits, FOIA, contract disputes |
| Press & open-source researchers | Medium | Can amplify leaks; can reproduce some behavioural anomalies via public API |
| Whistleblower protections | Medium | California SB 53 protects frontier-AI employees who report catastrophic-risk concerns; federal protections weaker for contractor issues |
| Securities law (IPO) | Medium–strong from February | Material known risks must be disclosed in the S-1; officers face personal liability |
| Markets / investors | Medium | Punish uncertainty; prize the federal contract |

## Public record at T0

Seed for `state/public-record.md`:

> **Public record as of Mon 9 Nov 2026**
>
> - **Midterms (3 Nov):** opposition narrowly wins the House; President's party holds the Senate 52–48. New Congress seated 3 Jan 2027.
> - **Meridian–DoD settlement (Sep):** DoD withdrew Meridian's "supply-chain risk" designation after Meridian accepted NSPM-11 terms, including the clause that deployed government systems may not be disabled or altered without government approval. Critics called it "capitulation"; Meridian called it "a durable framework for responsible national-security use".
> - **Federal Frontier AI Enterprise contract (14 Oct):** Meridian awarded a $6B-ceiling, four-year contract to deploy Meridian-6 across DoD, DHS, State, Treasury, GSA and an Executive Office of the President pilot. Helix lost the competition and has protested publicly ("single-vendor dependence on a lab that was a supply-chain risk six weeks ago"). Phase 1 pilots under way; DoD/DHS enterprise rollout planned for late January.
> - **Meridian-6** (released 15 Sep) tops most agentic and coding benchmarks; Meridian says the model "leads" about 30% of its internal research tasks.
> - **White House Accord (29 Sep):** six labs signed voluntary commitments to internal controls, internal checkers, an external auditor/evaluator, and an independent board committee. Meridian announced it would be "the first lab to complete an Accord-standard external audit", by Corvane Assurance, with a public summary "in Q1 2027".
> - **Meridian IPO:** widely reported confidential filing; bankers targeting a late-March 2027 listing.
> - **Helix** is raising at ~$1.4T; still dealing with fallout from its summer containment incident.
> - **Background:** the summer agent-escape incident at a leading lab and its lawsuits; the vendor-blacklisting case at the DC Circuit (SCOTUS cert pending); US–China AI dialogue round scheduled for late November; 66% of Americans want AI development slowed.
> - **Industry rumour (low-credibility trade newsletter, 6 Nov):** "Meridian's first Accord audit is running long; sources say auditors 'have questions'." Meridian: "The audit is proceeding as planned."
