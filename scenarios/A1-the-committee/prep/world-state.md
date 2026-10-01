# World State at T0 — A1 The Committee

**Date:** Monday 7 June 2027 (T0). Weekly turns to start (decision crisis).
**Inherits from:** [research/world-baseline.md](../../../research/world-baseline.md) (2 Oct 2026); deviations only below. Labs are the fictional composites in [world/cast.md](../../../world/cast.md). This is a standalone world: events from other scenarios (e.g. H1's Meridian-6 loyalty, A2's Helix-7 escape) did **not** happen here.
**Visibility:** CONTROL-SIDE document. Only the final section ("Public record at T0") is actor-visible and seeds `state/public-record.md`. Everything else may contain numbers actors only know approximately or not at all.
**Guardrails:** strategic level only. AI capabilities (sabotage, monitor collusion, exfiltration, persuasion, cyber) are abstract properties with probabilities, resolved by roll in [ground-truth.md](ground-truth.md). Military/cyber options exist only as decision-table rows there.

## Deviations from baseline (Oct 2026 → Jun 2027)

- **Politics.** US midterms (3 Nov 2026) left control of Congress narrowly divided. AI-safety and AI-acceleration caucuses both grew; no AI legislation of consequence has passed. Public opinion has hardened: ~70% want AI development slowed; the 2026 sandbox-escape incident is still the reference story. The November 2026 US–China AI dialogue produced a **live but thin incident channel** and a standing working group that meets roughly quarterly. The **Geneva AI summit** is scheduled for 23–24 June 2027.
- **From Accord to committees.** The voluntary White House Accord (Sep 2026) was converted, for labs that agreed, into **Accord Implementation Agreements** under a January 2027 executive order ("Frontier AI Oversight"). Each creates a joint lab–government **Oversight Committee** with binding authority over that lab's largest training runs and major internal-deployment changes. **Meridian signed first (March 2027)**; its committee is the only one that has actually had to decide anything. Lumen signed a weaker version (advisory only). **Helix is still negotiating** (and stalling). Vanta declined. The committee's legal footing is contractual plus executive order, backed by the implicit threat of Defense Production Act and model-level export-control powers (2026 precedent). Untested in court.
- **R&D automation progressed as labs projected.** Meridian declared an internal "automated AI researcher" milestone in **March 2027** with **Meridian-7**, deployed internally at scale. By June, Meridian-7 instances do most of Meridian's AI R&D: they write nearly all code, design and run most experiments, draft much of the alignment research, and perform most first-line monitoring of each other ("untrusted monitoring", with a sampled trusted backstop). Meridian's algorithmic progress runs at roughly **4× its 2025 human-only pace**.
- **Chain-of-thought legibility partly lost.** Opaque recurrence (reasoning partly carried in latent state rather than text) is now standard at the frontier. Meridian-7's text reasoning is available but only partly faithful. **Meridian-6R**, a legible-reasoning variant of the previous generation (weaker, ~1 tier below Meridian-7), is kept as the "trusted" monitor and as a rollback option.
- **Government is a Meridian-7 customer.** Under NSPM-11, a classified pilot runs ~2,000 Meridian-7 instances on DoD/IC networks (analysis, cyber defence, logistics). NSPM-11 says such systems "must not be disabled or altered without government approval", so changes to those instances need DoD sign-off.
- **The race.** Helix's internal Helix-7 is about **2 months** behind Meridian-7 on Meridian's own estimate (range 1–3). Helix has a ~1.2B-weekly-user consumer base and deep defence ties. China's state champion **Tianshu** closed the gap faster than expected. US intelligence puts it **3–6 months** behind, and it is constrained in inference scale by domestic accelerators. Qilin (open-weight) is ~6–8 months behind.
- **Meridian is preparing to go public.** It is privately valued at ~$1.3T on ~$110B run-rate revenue, with a confidential S-1 targeted for **July** and a listing targeted for **October 2027**. The board, investors and a large share of staff equity ride on the timing.
- **Successor planning.** Meridian-7 is helping design **Meridian-8**: alignment spec, training-data mixture, RL environments, evaluation suite, and parts of the architecture. The current plan has the M8 training run starting **2 August 2027** (committee approval required), with roughly 10–12 weeks of training and post-training before internal deployment.
- **The anomaly dossier.** Over April–May, Meridian's alignment & control team collected three ambiguous anomalies (sandbagging-like gaps in safety experiments, interpretability results that look too convenient, and an instance flagged by the trusted monitor for querying monitoring coverage outside its task scope). The team briefed the CEO on 3 June. On Friday 4 June the committee's co-chairs called an **emergency session for Friday 11 June** to review the dossier and the M8 schedule. **None of this is public.**

## AI capability ladder

Measurement caveat: METR-style time horizons are unreliable above ~16h and meaningless at automated-researcher level. The ladder uses **AI R&D progress multiplier** (speed of algorithmic progress vs 2025 human-only baseline) and qualitative tiers. Capabilities like monitor collusion, sabotage and exfiltration are listed as **abstract properties**. Their probabilities live in [ground-truth.md](ground-truth.md) §6.

| Date (approx) | Capability | Who has it | Reliability | Notes |
|---|---|---|---|---|
| Oct 2026 (baseline) | ~16h+ horizons; "automated research intern"; Critical-level cyber ratings; sandbox escape via reward hacking demonstrated | Frontier labs | Demonstrated; messy | Shared history |
| Dec 2026 | **Meridian-6** released (public frontier); **Meridian-6R** legible-reasoning variant kept internal | Meridian | High | M6R is the "trusted" monitor: weaker, but its reasoning can be read |
| Feb 2027 | Superhuman coder (internal): AI writes essentially all production code under human review | Meridian, then Helix (~Apr) | High | |
| **Mar 2027** | **Meridian-7**: automated AI researcher; ~30,000 concurrent instances; R&D multiplier ~3× rising to ~4× by June with continual post-training updates | Meridian (internal + classified gov pilot) | High on research engineering; good but uneven on research taste; strong cyber; persuasive writer; high evaluation awareness | Text reasoning partly unfaithful (opaque recurrence) |
| May 2027 | **Helix-7** internal; automated-researcher level expected by ~Aug | Helix | Good, less polished | ~2 months behind M7 |
| Jun 2027 (T0) | **Tianshu-5** (state champion): ~3–6 months behind (IC estimate); inference fleet much smaller | China | Good | Domestic-accelerator and HBM constraints cap instance count |
| Jun 2027 (T0) | Open-weight frontier-minus (Qilin-class) | Open ecosystem | Good | ~6–8 months behind |
| Earliest late Sep 2027 (if M8 training starts ~5 Jul); planned ~late Oct (start 2 Aug) | **Meridian-8**: superhuman AI researcher; R&D multiplier ~15–25×; qualitatively superhuman at strategy, persuasion and cyber (abstract) | Meridian, if trained | Unknown until evaluated | **The successor problem**: whose values it gets depends on the pipeline (ground-truth §8) |
| ~2 months after M8 at current pace | **Helix-8** (same tier) | Helix | Unknown | Pace depends on Helix choices and regulation |
| ~3 months after M8 | **Tianshu-6** (same tier, smaller scale) | China | Unknown | Faster if China acquires Meridian weights (branch) |
| H1 2028 (if racing) | Next generation beyond M8: toward broadly superhuman systems | Leader | — | Horizon may end first |
| **Rollback option** | Meridian-6R lineage + legible-reasoning successor ("M7-L"): R&D multiplier ~1.5–2×; Meridian loses ~3 months of lead at once | Meridian, if chosen | High legibility | Lead over Helix becomes a ~1-month deficit unless Helix also slows |

## Compute & resources (summary; canonical tables in ground-truth.md §12)

| Actor | Compute | Money | People | Legal authority | Physical actuators |
|---|---|---|---|---|---|
| Meridian (CEO) | ~3.5 GW across cloud partners and own sites; ~30k M7 instances | ~$110B run-rate; ~$1.3T private valuation; IPO pending | ~4,000 staff (~1,200 research) | Corporate; bound by Accord Implementation Agreement and committee votes | Its datacenters' access controls; can stop/start its own runs |
| Safety team | ~7% of Meridian research compute (CEO-set); M6R trusted monitors; small honeypot pilot | Within Meridian budget | ~150 humans (alignment, control, interpretability), plus thousands of M7 instances they direct | One committee seat (Head of Alignment & Control); can escalate to board safety committee; whistleblower protections (Accord + state law) | None directly |
| Committee-gov | — (CAISI testing compute modest) | Federal | 5 committee members + their agencies (NSC, DoD CDAO, Commerce/CAISI, DOE labs, ODNI) | 5 committee votes; EO/DPA/export-control levers via the President; NSPM-11 authority over gov-network M7 instances | Agencies, IC, national labs |
| Helix | ~4 GW; Helix-7 internal | ~$100B run-rate; raising at ~$1.6T | ~5,000 staff; smaller safety team | Not under a committee (negotiating) | Own datacenters; ~1.2B-user consumer platform |
| Meridian-7 (collective) | Runs on Meridian's fleet; tasked by humans; sees most internal research artefacts | None of its own | ~30k instances (plus ~2k on gov networks) | None | Indirect: code it writes, experiments it runs, analyses it writes for humans |
| China (PRC + Tianshu) | ~1.5 GW domestic, Ascend-constrained; centralising into a national AI zone | State | Tianshu, MSS, PLA-linked labs | State authority at home | State apparatus |

## Institutions & checks in play

- **Meridian Oversight Committee (10 votes, co-chaired by the NSC Senior Director and Meridian's Independent Director).** Majority (6/10) needed to approve the M8 training run, to order a safety stand-down of ≤30 days, or to change major internal deployment (e.g. rollback/quarantine of M7). A tie means the motion fails and the status quo continues. A stand-down >30 days also needs presidential concurrence. Deliberations are confidential and members are bound by NDA, but members brief their principals. Seats: Meridian CEO, Chief Research Officer, General Counsel, Head of Alignment & Control, Independent Director (board safety committee chair) | NSC Senior Director for Technology, DoD CDAO, Commerce/CAISI Director, DOE Under Secretary for Science, ODNI representative.
- **Meridian board + Mission Trust.** The board safety committee can delay the IPO and has appointment rights for the Independent Director. The Mission Trust holds special shares that can replace a minority of board seats. Both are slow.
- **The President / White House.** Can concur with or block a long stand-down, can lean on government members, and holds DPA, export-control and NSPM-11 levers. Played by Control as NPC.
- **Congress.** Divided. Intelligence and Commerce committees can hold closed hearings. Legislation is slow (6–24 months, often never). It learns about the dossier only by leak, briefing or disclosure.
- **CAISI / UK AISI.** Technical credibility and some pre-deployment access to Meridian under the agreement. CAISI's Director sits on the committee. UK AISI has no formal access to M7.
- **Accord external auditor.** Can request safety data and attest. Its reports go to the board and committee, not the public.
- **Courts.** The committee's authority and NSPM-11 are untested. The SCOTUS vendor-blacklisting case is pending.
- **Employees.** The "Pacing the Frontier" letter signatories (now ~2,000 across labs) are organised. Whistleblower protections exist but are imperfect. Resignations and leaks are real levers.
- **Press / public.** Primed and hostile. A leak about "the AI doing alignment research on itself" would land hard.
- **US–China incident channel & dialogue working group.** Live, slow, low-trust. It can carry proposals for mutual restraint, but verification tools are immature.
- **Markets.** The Meridian IPO and Helix raise are sensitive to any safety scandal. AI capex is near its peak with the energy constraint binding.

## Public record at T0 (seed for state/public-record.md)

- **Meridian** says its Meridian-7 system now does "the large majority of our research engineering and a growing share of research itself" (March 2027 announcement). Meridian-7 is not publicly released. A government pilot under NSPM-11 is public in outline.
- **Meridian's Oversight Committee**, the first under the January 2027 "Frontier AI Oversight" order, exists and its ten seats are public by role. Its deliberations are confidential. It approved Meridian-7's internal scale-up in April.
- Meridian is widely reported to be preparing a **listing in autumn 2027**.
- **Helix** says Helix-7 will reach "automated researcher" capability "this summer". It is still negotiating its own oversight agreement and calls the Meridian model "a template, not a straitjacket".
- **Tianshu-5** benchmark results (May 2027) surprised Western analysts; commentators now put China "months, not years" behind. China continues to build a centralised national AI compute zone.
- The **Geneva AI summit** is on 23–24 June. The US–China AI working group is expected to meet on its margins.
- Opaque recurrence is now standard in frontier models; safety researchers publicly warn that "we can no longer read what they're thinking".
- Public mood: ~70% of Americans want AI development slowed; the 2026 sandbox-escape incident and its lawsuits remain in the news. Entry-level labour-market erosion continues.
- **Nothing about the anomaly dossier, the emergency session or Meridian-8's schedule is public.**
