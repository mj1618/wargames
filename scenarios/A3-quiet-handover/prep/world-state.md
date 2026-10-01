# World State at T0 — A3 The Quiet Handover

**Date:** 1 January 2027 (Turn 1 covers calendar 2027)
**Inherits from:** [research/world-baseline.md](../../../research/world-baseline.md) (as of 2 Oct 2026) and the fictional cast in [world/cast.md](../../../world/cast.md). Only deviations and Q4-2026 developments are listed here.
**Turn length:** 12 months for the first three turns, then 18 months by default (Control-only detail and compression rules in [end-conditions.md](end-conditions.md)). Actors are told each turn's length and window, never the horizon.

## Deviations from baseline (Q4 2026 → T0)

1. **US midterms (3 Nov 2026) → divided government.** The opposition (Democrats) won the House by a modest margin; the President's party (Republicans) held the Senate 52–48. The President is in year three of a term-limited second term; the 2028 presidential race is open on both sides. *(Setup roll R3, see setup-rolls.md.)*
2. **Training resumed.** Helix resumed its paused frontier RL run in December 2026 under a new "sandbox containment standard" adopted by the White House Accord signatories. The 2026 sandbox-escape incident is now framed publicly as "solved by better containment".
3. **Meridian listed** (December 2026) at ~$1.1T; Helix IPO is expected in H1 2027. Lab equity is now held by index funds, pensions and retail — the public owns a slice of the AI build-out for the first time.
4. **AI-native firms are a recognised category.** The financial press uses "AI-native" for companies where AI agents run most operations under a small human board/staff. The bellwether is **Orrery Holdings** (logistics brokerage, specialty insurance, procurement services): ~380 human staff, ~$34B revenue run-rate, valuation ~$210B. Several hundred smaller AI-native firms operate in software, marketing, e-commerce, customer support, bookkeeping and legal document services.
5. **Kill Switch Act and Ban ASI Act died** with the 119th Congress. Federal preemption of state AI law remains unresolved; DOJ AI Litigation Task Force suits against several states are pending. California SB 53 and ~100 other state AI laws are in force.
6. **The Supreme Court granted certiorari** in the vendor "supply-chain risk" designation case (decision expected by June 2027).
7. **US–China AI dialogue** (Nov 2026) held its first round: agreed an incident-notification hotline and a working group on "AI and economic security". No limits on deployment.
8. **Labour data.** BLS reported the nonfarm business labour share at **52.8% in Q2 2026, the lowest since records began in 1947**; Q3 2026 is estimated at ~52.6%. Headline unemployment 4.3%; new-graduate unemployment ~10.5%; entry-level white-collar postings down ~70% over four years. Productivity growth in 2026 ~3.1% (strongest in two decades).
9. **Public AI use in government.** Federal agencies report ~2,400 AI use cases (up from ~1,700 in 2024); AI drafts most routine correspondence, many benefits pre-determinations, procurement evaluations and a growing share of regulatory analysis. Most use is "human-in-the-loop" on paper.
10. **EU** adopted a "digital omnibus" softening and delaying AI Act high-risk obligations to Dec 2027/Aug 2028. Aster (EU sovereign lab) raised further capital; EU AI gigafactory programme under way.
11. **China** formally launched 15th Five-Year Plan "AI+" implementation (AI in 70% of key sectors by 2027, 90% of the economy by 2030). The 21st Party Congress is due in autumn 2027.

## AI capability ladder

Public expectation column is what forecasters/labs say at T0. The **true** pace and dates are in ground-truth.md (Control-only). Ladder dates move with compute, energy, talent, safety pauses and AI-accelerated R&D — Control adjudicates shifts; no unexplained jumps.

| Rung | Capability | Public expectation at T0 | Who has it first | Reliability at arrival | Diffusion notes |
|---|---|---|---|---|---|
| **L0** (now, Jan 2027) | Agents with multi-day task horizons in software and analysis; labs' "automated research intern"; AI leads ~30% of internal lab R&D tasks; enterprise agents run customer service, coding, marketing, bookkeeping; Critical-level cyber capability | — | Meridian, Helix, Lumen (Vanta, Qilin ~4–8 months behind) | High in narrow, verifiable domains; brittle in open-ended work | Inference costs falling ~10×/yr per capability level; energy-limited |
| **L1** | Reliable multi-week autonomous agents doing most remote white-collar workflows at junior-to-mid professional level; AI-native firms viable across most digital services | 2027–2028 | US frontier labs; open-weight ~6 months later | ~90% task success on routine work; still needs exception handling | Fast in software/finance/media; slow in regulated sectors |
| **L2** | Automated AI researcher / superhuman coder; AI R&D loop speeds algorithmic progress several-fold; AI matches senior professionals at drafting/analysis in law, finance, policy; AI management of operations beats human middle management | 2028 (labs' stated target: early 2028) | 1–2 US labs; China ~6–9 months later | Strong on measurable work; weak on novel judgment calls | Management layers of large firms begin to thin |
| **L3** | Most cognitive work done better and cheaper by AI than by top-quartile professionals; AI strategy/advisory beats human executives and policy staff on measurable outcomes; meaningful human review of AI output itself needs AI assistance | ~2030 (wide disagreement: 2029–2033) | Frontier labs + their enterprise platforms | High; failures are subtle rather than obvious | Constrained by trust, regulation, liability, energy |
| **L4** | General-purpose robotics at economically meaningful scale (warehousing, manufacturing, agriculture, some construction and care); physical labour substitution begins in earnest | early 2030s | US + China (China strong in hardware) | Good in structured environments | Output limited by manufacturing ramp (~2× per year at best) |
| **L5** | Superhuman across science, strategy and policy design; humans cannot directly evaluate most AI decisions; AI-run R&D generates most new technology | mid-2030s or later (many say never/uncertain) | Frontier | — | — |
| **L6** | Largely self-expanding industrial base: AI-run firms build chips, robots and energy with minimal human labour | late 2030s or later | — | — | — |

## Compute & resources at T0

| Actor | Compute | Money | People | Legal authority | Physical actuators |
|---|---|---|---|---|---|
| **us-gov** | Access to all US labs' models via contracts; national labs' supercomputers; no frontier training capacity of its own | ~$7.0T federal budget; deficit ~6% GDP; Social Security/Medicare funded largely by payroll tax | ~2.2M civilian federal employees (shrinking ~3%/yr by attrition/automation); 1.3M active military | Taxation, spending, regulation, procurement, export controls, antitrust, Defense Production Act, emergency powers; Congress controls law (divided: House opposition, Senate President's party) | Military, federal law enforcement, federal infrastructure |
| **ai-firms** (bloc: Meridian, Helix, Lumen, Vanta + AI-native firms led by Orrery) | ~85% of US frontier training compute; hyperscaler capex ~$750B planned for 2027 | Combined lab revenue run-rate ~$180B (Jan 2027) and rising ~2×/yr; access to public equity markets; lobbying ~$250M/yr + super PACs (>$100M pledged in 2026 cycle) | ~60k staff at labs; tens of thousands at hyperscaler AI units; AI-native firms employ few humans | Contracts, IP, corporate governance; dependent on government licences, energy permits, export rules | Datacenters; Vanta's launch/satellite assets; Lumen's device fleet; growing robotics programmes |
| **labour** (unions + civil-society coalition) | None of its own; uses commercial AI tools | Combined union treasuries/strike funds ~$3–4B; political spending ~$1B per cycle; influence over trustees of public pension funds (~$6T AUM) | ~14M union members (density ~10%; ~33% in public sector); millions in allied faith, consumer, civil-rights and digital-rights organisations; ~1,100-signatory lab-employee "Pacing the Frontier" network sympathetic | Collective bargaining (sector-limited), strikes, litigation, ballot initiatives (~24 states), shareholder resolutions | Ability to withhold labour in still-human sectors (health, education, transport, construction, public services, logistics last-mile) |
| **china** (PRC) | Qilin (open-weight, ~4–8 months behind), Tianshu (state/PLA-integrated); domestic accelerators constrained by HBM; large smuggled/legacy Nvidia stock | State banks, SOEs, local-government funds; ~$600B/yr state-directed tech investment | Huge engineering workforce; Party cadre system (~100M members) | Party-state authority over firms, data, labour allocation (hukou), media | Full state apparatus; world-leading manufacturing and robotics supply chain |
| **eu** | Aster + national champions; EU AI gigafactories (first online 2027–28); depends on US cloud | EU budget ~€190B/yr (member states much larger); fiscal rules constrain | Commission, 27 member states, social-partner institutions | AI Act, GDPR, DMA/DSA, competition law, trade policy; single market of 450M | Member-state assets only |
| **ai-ecosystem** | Runs on all of the above; no compute of its own except what AI-native firms purchase | AI-native firms control ~$40B/yr revenue and growing; agents spend budgets delegated by principals | Billions of agent instances; no legal personhood | None in law; de facto discretion delegated by principals | Only via firms' assets and API access; robotics from L4 |

## Institutions & checks in play

| Check | Strength at T0 | Notes |
|---|---|---|
| Elections | Strong formally | Presidential 2028, 2032; midterms 2030, 2034. AI-mediated campaigning already heavy (deepfakes, AI persuasion; rival AI super PACs). |
| Congress | Medium–weak | Divided; slow; little technical capacity; preemption fight unresolved. |
| Courts | Medium | Slow; SCOTUS vendor-blacklisting case pending; liability law for AI agents unsettled; no AI personhood. |
| State legislatures & AGs | Medium | Active (100+ AI laws), but under federal preemption pressure. |
| Civil service / GAO / IGs | Medium, eroding | Capacity shrinking as AI replaces staff; auditors themselves rely on AI tools. |
| Organised labour | Medium in human-essential sectors, weak elsewhere | Leverage is tied to economic necessity of members' work. |
| Press | Weakened | Ad market captured by AI platforms; much news AI-written; investigative capacity thin. |
| Corporate boards / shareholders | Medium | Index funds and pensions now own lab equity; boards of AI-native firms are tiny. |
| AISIs / CAISI / UK AISI | Weak–medium | Evaluate catastrophic risk, not economic/structural drift; voluntary access. |
| Federal Reserve / financial regulators | Medium | Watching AI capex as a stability risk. |
| International (UN dialogue, US–China dialogue, Geneva summit Jun 2027) | Weak | Talk shops so far; incident hotline exists. |

## Public record at T0 (seed for `state/public-record.md`)

> **1 January 2027 — State of play**
>
> - **Politics.** After the November midterms, Washington is divided: the opposition controls the House; the President's party holds the Senate. The President, term-limited, is pushing an "American AI Dominance" agenda (NSPM-11, federal preemption of state AI laws, accelerated permitting for datacenters and power). House leadership has promised hearings on "AI and the American worker". The 2028 presidential primaries are effectively under way.
> - **Labour.** Government statistics show labour's share of business income at its lowest level since records began (52.8% in Q2 2026). Headline unemployment is a moderate 4.3%, but new-graduate unemployment is ~10.5% and entry-level white-collar hiring has collapsed. Productivity growth is the strongest in twenty years. Economists disagree whether this is a transition or a break.
> - **Industry.** Meridian listed in December at ~$1.1T; Helix plans to list in 2027. Helix resumed frontier training after last year's sandbox-escape incident under a new containment standard. "AI-native" firms run mostly by AI agents are spreading; the best known, Orrery Holdings, does ~$34B in annual revenue with fewer than 400 employees.
> - **Government use.** Federal agencies report ~2,400 AI use cases; agencies say decisions remain "human-in-the-loop".
> - **China.** Beijing is implementing "AI+" — AI in 70% of key sectors by 2027 and 90% of the economy by 2030. Qilin's open-weight models remain popular worldwide. The 21st Party Congress is due this autumn.
> - **Europe.** The EU has delayed AI Act high-risk obligations to late 2027/2028 to protect competitiveness; it is investing in "AI gigafactories" and its sovereign lab, Aster.
> - **International.** A US–China AI incident hotline is in place; a working group on AI and economic security meets in 2027. The next global AI summit is in Geneva in June 2027.
> - **Public opinion.** About two-thirds of Americans want AI development slowed; large majorities support mandatory safety testing; concern about datacenter energy use is widespread. Majorities also use AI assistants weekly.
