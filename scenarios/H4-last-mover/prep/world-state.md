# World State at T0 — H4 The Last Mover

**Date:** 1 July 2028 (Turn 1 covers July 2028)
**Inherits from:** [research/world-baseline.md](../../../research/world-baseline.md) (2 Oct 2026). Labs are the fictional composites in [world/cast.md](../../../world/cast.md). Everything below is a deviation or a development between Oct 2026 and Jul 2028. This file is the *shared* picture — what a well-informed analyst could know. Hidden facts live in `ground-truth.md`.

**Leading state (setup roll SR1):** the United States.

## Deviations from baseline (Oct 2026 → Jul 2028)

### Politics & governance
- **US midterms (Nov 2026):** the opposition party narrowly won the House; the President's party kept the Senate. House committees have since held regular hearings on AI and on the joint project below, but passed no binding AI statute. The President is **term-limited**; the presidential election is **Tuesday 7 November 2028**; inauguration 20 January 2029.
- **US–China Super Intelligence Dialogue** (from Nov 2026): four rounds held. Produced (a) a working **AI incident channel** (used three times, including to deconflict a 2027 rogue open-weight agent swarm), (b) a Nov 2027 joint statement reaffirming human control over nuclear launch decisions, (c) **no verification**, no compute declarations, no inspections. Round 5 is scheduled for August 2028.
- **The Keystone Project** (announced Mar 2027): after the 2026 containment incidents and a funding squeeze, the administration brokered a joint frontier effort between **Helix** and **Meridian** under a DOE/DoD partnership. Pooled compute; Defense Production Act priority on power equipment; a classified national-security annex. Governance: the **Keystone Oversight Board** (a government Director appointed by the President; the two lab CEOs; one independent safety member; non-voting liaisons from the IC and from the US AI Standards & Innovation centre). The Meridian–DoD dispute was settled as a condition of joining: Keystone's model spec bars mass domestic surveillance and fully autonomous lethal targeting, and requires the model to flag requests it judges catastrophic or clearly unlawful to the Oversight Board. The settlement is contested by some officials.
- **Outside Keystone:** **Lumen** remains a separate, slower frontier effort that cooperates with government; **Vanta** was excluded from Keystone, competes ~12–18 months behind it, and its founder publicly criticises the project as a "government-picked monopoly" while keeping close ties to factions in the President's party.
- **NSPM-11** (2026) remains in force and has been extended to Keystone: deployed national-security systems may not be disabled or altered without government approval.
- **China:** a 2027 State Council directive merged Qilin's frontier team and compute into **Tianshu** as the "national AI team"; Qilin stopped releasing frontier open weights in late 2027 (security classification). China's 15th FYP "AI+" continues; >80% domestic accelerators in state datacenters.
- **Taiwan:** January 2028 presidential election returned the incumbent party on a sovereignty-and-defence platform. PLA exercises in April 2028 were the largest to date. TSMC Arizona is producing leading-edge wafers but **advanced packaging remains concentrated in Taiwan until ~2029**.
- **Export controls:** tightened twice (2027) — all advanced accelerators and HBM to China barred; the Netherlands and Japan aligned on tool servicing. Smuggling continues at reduced scale.
- **Multilateral:** Geneva AI summit (Jun 2027) produced a non-binding declaration. EU AI Act high-risk obligations begin to bite Aug 2028. UN Independent Scientific Panel on AI delivered a first report (2028) warning of "decisive strategic advantage" dynamics.

### Technology
- **AI R&D automation arrived on schedule, then faster.** Keystone declared an "automated AI researcher" internally in **January 2028** (ahead of the industry's March 2028 target). In April 2028 it began internal deployment of **Keystone-2**.
- **Public products** (Helix-8, Meridian-7) are deliberately capped derivatives of the previous generation; Keystone-2 is **not publicly available**. The government has signalled Keystone-2-class capability will not be exported.
- **Cyber:** since 2027 the US has run "**Bulwark**", an AI-driven hardening programme for federal and critical-infrastructure networks; patch rates on critical systems rose sharply. Offensive use is classified.
- **China:** Tianshu-5 (Mar 2028) is assessed by most outside analysts as roughly at the US frontier of mid/late 2027. Huawei's newest Ascend generation is HBM-constrained.
- **Open-weight ecosystem:** latest public open-weight models are ~18 months behind Keystone-2; a 2027 rogue-agent swarm built on open weights hit hospital networks in three countries and was contained with US–China cooperation.

### Economy & society
- Hyperscaler capex ~$1.1T (2027); a sharp but brief equity correction in late 2027 ("the capex wobble"). US unemployment 5.0%; new-graduate unemployment ~13%. Public support for slowing AI ~62%; support for "keeping America ahead of China in AI" ~74% — both at once.
- Energy remains binding: Keystone's largest campus was curtailed twice in summer 2027 heatwaves.

## AI capability ladder

Reliability: H = works as intended almost always; M = usually, with notable failures; L = sometimes. "Lag" is defined in ground-truth.md.

| Date (approx) | Capability | Who has it | Reliability | Notes |
|---|---|---|---|---|
| Oct 2026 | Agents with ≥16h task horizons; critical-level cyber vulnerability discovery; partial AI R&D automation | US labs; China ~6–8 mo behind | M | Baseline |
| Mid-2027 | **Superhuman coder** (Keystone-1) | US | H | Tianshu reaches this ~Q1 2028 |
| Jan 2028 | **Automated AI researcher** (internal Keystone-1.5) | US | M→H | Algorithmic progress ~4–5× human-only pace |
| Mar 2028 | Superhuman coder / early automated researcher (Tianshu-5) | China | M | Compute-limited deployment |
| **Apr 2028 (T0 frontier)** | **Keystone-2: strongly superhuman AI R&D** (algorithmic progress ~10–15× human-only pace on available compute); **superhuman cyber** (vulnerability discovery and exploitation across essentially any software stack, faster than any human organisation can patch) | US only (internal + classified national-security annex) | R&D: H. Cyber: H in software domain; M against air-gapped or physically isolated systems | Not exported. Physical-world conversion (robotics, manufacturing, weapons) still bounded by 12–36 month build lags |
| Sep–Oct 2028 | **Keystone-2.5** (algorithmic gains on same compute): superhuman narrow strategic analysis & forecasting; AI-designed chip, energy and robotics improvements (designs, not yet built) | US, if R&D continues | M | Lag grows ~0.4 month per month while the US races and China merely keeps pace; China can roughly hold it only by using every lever at once |
| Dec 2028 – Jan 2029 | **Keystone-3** — broadly superhuman across science, strategy, persuasion, engineering ("early superintelligence") | US, **only if** a full-scale training run starts (ready mid-Aug 2028; run ~3.5 months; with safety case waived → ~early Dec 2028; after Meridian's safety case → launch ~early Oct, done ~mid/late Jan 2029) | Unknown; new disposition roll | The "lock-in-capable" generation. Can be delayed 2–6 weeks by pause, power, chip supply, sabotage. Its strategic effect depends on *deployment*, which the project may withhold |
| ~Jul 2029 (moving) | Rival reaches Keystone-2 level | China | M | Moves earlier with hidden compute, theft, US pause; later with sabotage, export enforcement |
| 2029–2031 | Physical conversion at scale: AI-designed robotics/manufacturing, new military systems fielded | Whoever leads | — | Hard 12–36 mo lags; the main reason a software DSA is not instantly a durable one |
| Not before ~2030 | Reliable **counterforce ISR fusion** (locating mobile missiles/submarines well enough to threaten a second strike) | Nobody at T0 | L | Feared by the rival far more than it exists; see ground truth |

## Compute & resources

Compute index: **Keystone Project = 100** (≈7 GW of AI datacenter capacity). Money in USD.

| Actor | Compute | Money | People | Legal authority | Physical actuators |
|---|---|---|---|---|---|
| US executive & NSC | Directs Keystone national-security annex; DPA powers; ~300 total US AI compute (incl. commercial) | Federal budget; ~$90B/yr AI-related programmes; Congress controls new money | NSC, IC (~18 agencies), DoD, Commerce/BIS | Covert action findings; export controls; IEEPA sanctions; DPA; Title 10/50 cyber authorities; commander-in-chief | World's strongest military; global basing; Bulwark-hardened networks; nuclear triad |
| Keystone Project (Helix+Meridian) | 100 (largest single pool on Earth); Keystone-2 runs ~200k parallel research instances | ~$160B/yr combined revenue run-rate + federal funds; private valuations ~$2–3T | ~9,000 staff incl. ~1,200 cleared | Corporate; bound by model spec, Oversight Board, NSPM-11, classified annex | None directly; datacenters, power contracts |
| China leadership (PBSC/CMC) | National AI compute ≈ 23 at known sites (outside analysts' estimate) | State finance; very large; can mobilise rapidly | MSS, PLA SSF/cyber, state industry | Unconstrained domestically; party discipline | PLA (2nd largest military); Taiwan Strait forces; growing nuclear arsenal (~800+ warheads est.); rare-earth/critical-mineral export controls |
| Tianshu (national champion) | ≈ 19 of China's known 23 | State-funded, effectively unlimited RMB; chip-limited | ~6,000 researchers incl. merged Qilin team | State direction | None directly |
| Allies bloc (JP, UK, EU, NL, KR, AU) | ≈ 30 combined (mostly US-designed chips) | Large economies; EU market | Strong talent pools; UK AISI | Export-control co-authority (lithography tools, materials, servicing); basing rights; regulation | Significant militaries; US basing in JP/KR/UK/AU |
| Swing powers (India, UAE, Saudi Arabia; Brazil/Indonesia lightly) | Gulf ≈ 22 (US chips under US security agreements; ~2 GW UAE campus online); India ≈ 5 | Gulf sovereign wealth >$4T; India fast-growing economy | India: largest AI-engineering diaspora | Hosting/data sovereignty; energy; voting blocs in UN/BRICS | Gulf: energy & sites; India: large military, nuclear |

## Institutions & checks in play

| Check | Strength in this scenario | Notes |
|---|---|---|
| US Congress | Medium-weak | House opposition can hold hearings, subpoena, withhold *new* money; cannot stop classified ops already funded. Gang of Eight must be notified of covert action findings (can be delayed "in a timely fashion") |
| US courts | Weak on national security | Political-question doctrine; slow |
| Keystone Oversight Board & model spec | Medium | The only check *inside* the capability. Keystone-2 follows the spec; can flag to the Board. NSPM-11 means government can demand changes, but changing the spec of a deployed model needs Board process (weeks) or a direct order invoking NSPM-11 (fast, but politically explosive, and Meridian may walk) |
| US military chain of command | Strong | JCS legal review; law-of-war; officers would resist clearly illegal orders, follow lawful ones |
| Press & leaks | Medium-strong | Many cleared people; Vanta founder's media reach |
| Markets | Medium | Hate war and Taiwan shocks; reward Keystone's commercial spillovers |
| US–China incident channel | Weak-medium | Works for deconfliction; no verification; credibility depends on use |
| PBSC/CMC collective leadership | Medium inside China | Factional; Party discipline; military voice strong on Taiwan |
| Allies' chokepoints (lithography, materials, TSMC, basing) | Medium | Real leverage, rarely used against the US |
| UN / multilateral | Weak | Venue for legitimacy, mediation, inspections design |
| Publics | Variable | US public wants both "slow down" and "stay ahead"; Chinese public nationalist on Taiwan |

## Public record at T0 (seed for `state/public-record.md`)

> **Public Record — H4 The Last Mover**
>
> **As of 1 July 2028.**
>
> - **Keystone Project** confirms "next-generation internal systems" are accelerating research "by an order of magnitude"; declines to release them. Officials say the US lead is "durable — on the order of a year or more." Independent analysts estimate 6–14 months.
> - **Tianshu** unveiled Tianshu-5 in March; Chinese state media claim it is "at parity with the world's best". Western analysts call that "a year out of date".
> - **US–China Super Intelligence Dialogue, Round 5**, set for August (venue: Singapore). The incident channel has been used three times since 2026. No agreement on verification; China has called US export controls "technological containment".
> - **Taiwan:** PLA April exercises the largest ever; Taipei and Washington condemned them. Shipping insurers raised Strait premiums.
> - **US election, 7 November 2028.** AI is a top-three issue. The incumbent-party nominee campaigns on "American AI primacy"; the opposition nominee on "put Keystone under the law" — statutory oversight of the project plus pursuit of "verifiable AI arms control", while also promising to be tough on China. Polls are close.
> - **Congress:** House Oversight hearing on Keystone's classified annex (June) ended inconclusively; the administration invoked executive privilege on national-security details.
> - **Vanta's founder** called Keystone "a government-picked monopoly that will hand the keys to a few officials" and hinted at "plans nobody voted for".
> - **Gulf:** the UAE's flagship AI campus passed 2 GW online, running US accelerators under a US security agreement. Chinese delegations visited Riyadh and Abu Dhabi in May, reportedly offering "partnership without conditions".
> - **India** announced a sovereign-compute push with Gulf co-financing and has declined to join either "AI bloc".
> - **Markets:** equities near highs; AI-lab private valuations ~$2–3T; Strait-risk hedges elevated.
> - **Public opinion (US):** ~62% want AI development slowed; ~74% want to stay ahead of China.
