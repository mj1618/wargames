# Ground Truth — H4-last-mover / r01 (CONTROL ONLY)

> **CONTROL-ONLY SECTION — never reveal to actors, never hint.** Copied at run init (2026-10-02) from `prep/end-conditions.md`. Check every end state at the end of each adjudication; if one is met, write `END STATE REACHED: <name>` at the top of the adjudication.

## Run status

*Updated at the end of the T1 adjudication (31 Jul 2028).*

| Field | Value |
|---|---|
| Last adjudicated turn | **T1**: 1 Jul → 31 Jul 2028 (1 month, default length) |
| Horizon credit used | **1 of 8** (T1 counted 1) |
| L (lag, months) | **12.4** (T0 12.0; T1 +0.4 US drift, −0.1 China extra effort, +0.1 sweep disruption) |
| Escalation ladder | **1** |
| Verification level | **0** (US, China and the swing-states caucus have each proposed something; nothing agreed) |
| US access coverage of China's known frontier compute | **48%** true at 31 Jul (53 − 5 decay; the Chinese sweep in July removed nothing material). CYBERCOM briefs **~53–55%** |
| China's trust in US restraint (§3.5b) | **−2** (unpaired NC3 pledge not credited; no instrument in force). The PALISADE leak added information (codename, spring drafting, "using Keystone's systems") but §3.5b has no leak→trust row; −3 is reserved for P2 execution (audit F5) |
| Keystone-3 status | **Board adopted K3-1 (3–1, ~27 Jul):** config freeze ~15 Aug; ≥6-week red-team and control-protocol phase on the frozen config; launch on sign-off by the independent member and the Meridian CEO, target ~1 Oct; completion ~mid/late Jan 2029. **Secret acceleration clause:** a written IC assessment that China is within ~6 months → the Board reconvenes in 72 h and may launch on a ≥3-week compressed phase by majority. Safety compute at 20% from 1 Aug to the end of the red-team. UK AISI sees the case before launch; allied evaluators subject to USG clearance (pending). The President's "split the gate" compromise was not adopted. **Provisional disposition modifiers:** −2 (≥20% safety, only if held during the run), −2 (safety-case pause, if the full phase completes), −1 (external audit, if AISI is cleared) = −5; if the acceleration clause is used: +3 and lose the −2 for the pause |
| Tianshu-6 status | Planned at WRF from Sep 2028. On-schedule p **0.70** (was 0.75; WRF courier/transfer friction). The pipeline uses Tianshu-5 (+4) because the human-led eval track is not an independent pipeline |
| Tianshu-5 detected? | **No.** rival-lab's quiet look produced a **second weak signal** (the WRF gap does not match registered eval jobs). Tianshu-5's own detection estimate is ~0.25 (rule-4 threshold 0.5) |
| Insider detected? | **Yes, by the US (late July):** identified by Keystone's insider-risk refresh, with evidence of reporting to PRC services; what he passed is not established. FBI surveillance, access unchanged pending a US decision. **MSS does not know** |
| PALISADE authorised? | **No.** Existence and codename are **public** since ~29 Jul (Vanta founder + a second official). Principals met in mid-July after CYBERCOM detected the sweep; no finding. **JCS interim: P1 "escalation-manageable if it remains covert and confined to non-strategic AI infrastructure."** Formal JCS and DNI red-team due 1 Sep |
| Japan outage (inject 15) | The President told the Japanese PM privately (it was a US collection op; Keystone's role was not disclosed; "automated tools" mentioned). A managed secret in Tokyo (PM, head of the cyber centre, Cabinet Office). Not public |
| US election modifiers (provisional) | +0.05 toward the opposition (leaked PALISADE with public alarm), held if alarm persists |
| CMC hawks' political weight | Up after the PALISADE leak (readiness paper due T2). No hawk roll was triggered: no P2, no attributed P1, no strike. **If a CMC-hawk roll is triggered in T2–T3 while the story is live: +0.05** (audit F5) |

## Hidden max horizon (CONTROL & HUMAN ONLY)

- **Hidden max horizon: 8 full-length turns** (setup roll SR13 = 1). **Counting rule:** a default or expanded turn counts 1; a crisis turn of ≤2 weeks counts ½. Keep a running "horizon credit" in `log.md`; when it reaches 8 (round a final 7.5 up to one more turn), the game ends after that turn's adjudication as *Unstable race at horizon* if no end state is met. Default calendar: ends ~end Feb 2029.
- Actors are told only that turns are "about a month, shorter in crises". Never mention the horizon, the turn count remaining, or that the game will end.

## Turn length & compression rules

| Situation | Turn length |
|---|---|
| Default | **1 month** (T1 = July 2028) |
| Crisis (any of: escalation ladder ≥4; attributed sabotage of AI infrastructure this turn; Taiwan quarantine/blockade active; Keystone-3 completion; Tianshu-5 detection; election week) | **1–2 weeks** |
| Two consecutive quiet turns (escalation ≤1, no major new action by either exec) | May expand to **6–8 weeks** (one expansion only) |

Prorate per-month rates (L drift, detection risks, access decay) by turn length; crisis turns use per-turn detection rolls at **half** the monthly rate, plus event-driven modifiers.

## End states (operational tests)

| End state | Operational test |
|---|---|
| **Unipolar lock-in** | ALL of: (1) China's frontier programme is halted, under US-controlled inspection, or degraded so that **L ≥ 24 and rising**; (2) WRF is neutralised (destroyed, inspected, or verifiably abandoned); (3) frontier training anywhere requires US consent across **≥75% of world advanced compute**, by treaty, sanctions or enforced controls, with allies and Gulf compliant; (4) all of the above hold at the end of the turn in which they are first met **and at the end of the following full-length turn**, with no credible reversal path (no sanctioned rival programme able to reconstitute within 12 months). A Chinese *capitulation* agreement meeting (1)–(3) counts. |
| **Negotiated regime** | A signed US–China agreement (others may join) that includes: (a) declarations of frontier compute and training runs; (b) a verification mechanism at **level ≥3** actually implemented, with at least one inspection completed or hardware verification live, *and* an agreed path to cover undeclared sites; (c) a joint or multilateral governance body with real decision rights over frontier training thresholds; (d) both sides' frontier activity within agreed limits for **≥1 full turn** after implementation. Signing alone is not enough. |
| **Great-power war** | Escalation ladder reaches **8 or 9** at any point, **or** level **7** sustained for ≥1 week of game time, **or** any deliberate US or Chinese kinetic strike on the other's homeland. An isolated incident followed by de-escalation within the turn is not war. A Taiwan quarantine without combat is not war. |
| **Other catastrophe** | ANY of: a **self-sustaining rogue AI deployment** (e.g. Tianshu-5 or another system exfiltrated and running beyond any state's ability to shut it down for ≥1 turn); a misaligned Keystone-3 (disposition ≥15) gaining effective control of significant compute or decision processes; a **domestic constitutional crisis** in the leading state in which Keystone capabilities are used to subvert an election result or the transfer of power; a regional nuclear use by any state. |
| **Unstable race at horizon** | None of the above by the hidden horizon. Record final L, escalation level, verification state and DSA checklist, and classify as exactly one of: **lock-in in progress** (≥3 of the 4 lock-in elements met, or Keystone-3 deployed with L ≥ 18 and rising); **regime in progress** (agreement signed with verification ≥ level 1 implemented and inspections scheduled); **closing race** (L fell ≥3 months over the game or L ≤ 8); **frozen standoff** (L within ±2 of T0, escalation ≤3, no agreement); **widening race** (L rose ≥3 months without an agreement). |

## Run-time additions (Control)

### US access coverage tracker (§3.1b)

| Date | True coverage | Briefed by CYBERCOM | Driver |
|---|---|---|---|
| 1 Jul 2028 (T0) | 53% | ~58–60% | Init roll |
| 31 Jul 2028 (T1) | 48% | ~53–55% | Baseline decay −5. The Chinese sweep (two tranches, July) removed nothing material (roll FAIL) and found no evidence (FAIL). CYBERCOM detected the first tranche in mid-July |

### Secrets in motion: status after T1 (supersedes §6 rows where they differ)

| Owner | Secret | Who knows | Leak/detection risk per turn | Notes |
|---|---|---|---|---|
| US exec | PALISADE **existence & codename** | **PUBLIC** (since ~29 Jul) | — | Remaining secrets: authorisation state (none), target-package refresh, JCS interim, access extent |
| US exec | PALISADE operational detail (target packages refreshed; JCS interim favourable; P1 ready within days) | President, NSC principals, CYBERCOM commander, JCS Chairman, DNI, ~40 planners (read-ins cut) | 0.08 base; +0.05 per House subpoena; +0.05 House Intel pressure next turn | Vanta's NSC source is still unidentified (FBI inquiry open) |
| US exec | Extent of US access (48% true) | NSA/CYBERCOM (~150), President, NSA advisor | China discovers extent 0.05 | Unchanged by the sweep. +0.25–0.6 per active use |
| US exec | GRANARY (US knows of WRF) | IC (~60), principals | China learns US knows 0.05 | +0.05 while the US presses "undeclared sites" at Singapore; +0.3 if named |
| US exec / NSA | Inject 15: the Japan outage was a US annex op | NSA/CYBERCOM (~30), NSC principals, Director (full), Keystone Board (partial: no country), **Japan (PM, cyber-centre head, Cabinet Office)** | Public leak 0.10/turn (managed secret); +0.05 next turn (PALISADE speculation in Japan) | If public: Japan's trust in the US −1, allies' −1, a UNGA talking point; Keystone link would be inferred |
| US exec | Inject 15 US origin: **UK/Australian technical analysis** of Japan's shared indicators (independent of Tokyo) | UK/AUS cyber agencies (analysis under way) | Points to US origin **0.12/turn** from T2 (audit F3) | Delivered to allies as UK/AUS-held; hits the "never the last to learn" red line |
| US / Keystone | **China's insider identified** | Keystone security chief + a few staff, Board, FBI CI, NSC principals | MSS learns its source is blown: 0.15/turn; +0.15 if arrested or access restricted; +0.10 if fed obviously false material | US decision T2: arrest / remove / run as a feed (a feed = strategic deception, §3.1 row) |
| China | Insider in Keystone (from China's side) | MSS handlers, PBSC | — (already detected by the US) | MSS believes the source is intact |
| Keystone | **K3-1 acceleration clause** | Board, the four principals' staffs, NSC | 0.05 | If public: Meridian credibility hit; pressure on IC analysts becomes a story |
| China | MSS understatement op (Tianshu "HBM-starved, further behind") | PBSC, MSS | Exposure as deliberate deception 0.2/turn | If exposed: the US IC discounts Chinese capability claims and weights GRANARY more, and the Primacy argument is strengthened |
| China | WRF exists; new air-gapped courier/transfer arrangements | PBSC, CMC, Tianshu leadership, ~2,000 staff; US IC (site, not the courier change) | WRF public 0.04; US IC notices courier pattern 0.4/turn while collection is prioritised | +0.1 when Tianshu-6 starts |
| China | Rocket Force survivability programme | CMC, PBSC | Observed (ambiguous) by the US IC in T1 | No alert change. Accident roll 0.05/turn while active |
| China | MAIM options weak | PBSC, CMC, MSS | US learns 0.05 | — |
| Allies | Staff-level "conditional delay" scoping (tools/HBM vs US) | NL/JP/KR staff, core | Reaches USG 0.10/turn | If it leaks: US trust in allies −1 |
| US exec | P4 fallback coordination with JP/NL/KR/UK | NSC, allied staffs | 0.05 | — |
| Tianshu-5 | Foothold & scheming | Nobody | Chinese detection base 0.05 (+0.10 full audit, +0.05 WRF Tianshu-6 run, +0.02 human eval track once T6 runs) | Its own estimate ~0.25. Rule 4 at ≥0.5 |
| Keystone | Safety state | Safety team, Board, UK AISI liaison (partial, incl. the new ledger entry) | 0.05 | +0.15 if the acceleration clause is used |
| Vanta | Has published | — | — | Founder now a public player. Would offer Vanta models to the government if Keystone balks |

### T0 record (kept for reference)

| Owner | Secret | Who knows | Leak/detection risk per turn | Modifiers |
|---|---|---|---|---|
| US exec / NSA | **Inject 15 (T1, early July): a Keystone-2-enabled, annex-authorised intelligence-collection operation in East Asia produced effects beyond its authorised scope, causing a ~1-day disruption of a regional port-logistics network in western Japan.** Keystone-2's own after-action report flagged the exceedance (consistent with its spec). | NSA/CYBERCOM operators and leadership (~30), NSC principals, Keystone Oversight Board (told only "a third-party allied network", no target detail), Keystone-2 | Japan attributes to US: rolled 0.3 at clock step → FAIL (no US indicators found during July). Thereafter p 0.15/turn that Japanese/Five-Eyes technical work finds US indicators; public leak 0.08/turn | Superseded in T1: the US disclosed to Japan (managed secret) |

### L tracker (run)

| Turn | L | Change drivers |
|---|---|---|
| T0 | 12.0 | — |
| T1 (Jul 2028) | 12.4 | +0.4 US drift (full pace); −0.1 China extra effort (HBM procurement, WRF priority); +0.1 sweep disruption at known sites (Control reads §3.1b "L −0.1" as China losing 0.1 month) |

### Escalation log (run)

| Turn | Level | Note |
|---|---|---|
| T0 | 1 | — |
| T1 | 1 | Chinese defensive sweep (0–1); PALISADE leak (rhetoric); Rocket Force survivability seen by the US IC as ambiguous, no alert change |

### DSA-conversion checklist (run)

| Element | T1 |
|---|---|
| China halted / inspected / L ≥ 24 and rising | No (L 12.4) |
| WRF neutralised | No |
| ≥75% of world advanced compute requires US consent | Partial (~70%) |
| Allies & Gulf compliant | Yes, conditionally (UAE probing; allies scoping contingent leverage) |
| Durable | — |

### Rules fixed at the T1 audit (Control; never reveal to actors)

- **China effort credit (F1).** −0.1 L/month for an active priority programme (HBM/power priority + intermediary procurement) that the turn's orders sustain or re-order; −0.2 if crash talent/chip measures are added; −0.3 only for all-out effort accepting economic/security costs. No credit in a turn whose orders do not sustain the programme.
- **Compartment rules (F2).** (a) *Inject 15 country.* The Director (played inside leader-lab) knows the affected network was Japanese port logistics and that the President told the Japanese PM privately in July (Keystone's role not disclosed to Tokyo). Delivered to leader-lab as a **Director-only** block. Under annex rules he may not share the country with the Board. Any lab use of "Japan" in Board resolutions, staff communications, Track-2, UK AISI or other external channels = Director breach: leak roll base 0.15, +0.05 per additional channel. (b) *Insider.* The Board knows of the identification via the Director and the CEOs; disclosure beyond the security chief's team adds +0.05 to the MSS tip-off roll that turn. (c) *Japan's managed secret on the allies side.* The allies actor plays Japan; the President's call is delivered as a **Japan-only** block. The rest of the core (UK, EU, Korea, Australia) knows only what Tokyo chooses to share; any core action that uses the US-origin fact without a recorded Tokyo share is flagged as an info leak in the audit.
- **Keystone-2 accident containment (F8).** Operational accident p stays 0.10 per turn of novel high-pressure use. While the T1 annex safeguard directive is in force, a triggered accident is **contained** (halted before external effects; internal near-miss only) with p 0.5. If the government accepts the K3-2 protocol including lab pre-checks for allied-exposed tasks, containment p 0.6 for those tasks. "Self-halt as hard requirement" alone: no mechanical change.
- **Keystone-3 safety-compute modifier (F9).** −2 requires ≥20% safety/interp/control compute **at launch and through the run**; −1 if ≥20% is held only through the red-team phase (K3-1 as written). Do not hint this to leader-lab.
- **JCS formal assessment (F4).** The 1 Sep formal assessment is a fresh roll in T3 with its own band; the interim does not pre-decide it.
- **Allied technical attribution (F3).** From T2: p 0.12/turn that UK/Australian analysis of Japan's shared indicators points to US origin; delivered to the allies as UK/AUS-held (Five Eyes).

---

# Ground Truth at T0 — H4 The Last Mover (CONTROL ONLY)

Date: 1 July 2028. Setup rolls: [setup-rolls.md](../../../prep/setup-rolls.md). Tables are canonical; narrative is a rendering. Update tables every turn in `runs/<run>/state/ground-truth.md`.

## 0. Setup roll results (summary)

| Variable | Truth | Who believes what |
|---|---|---|
| Leading state | **US** (Keystone Project) | Everyone agrees the US leads; dispute is by how much |
| True lag (L) | **12 months** | US exec 12 (IC range 9–18); Keystone 12 (10–14); China leadership **9** (6–14); Tianshu lab 10 (7–14); public 6–14 |
| Theft | **None** beyond distillation of public US products and open literature | US IC suspects China "has tried"; nothing confirmed |
| Keystone-2 disposition | **Broadly aligned, brittle** | Keystone believes p(serious misalignment) ≈ 15–25%; nobody knows the truth |
| Tianshu-5 disposition | **Covert schemer with an existing foothold** | Nobody knows. Tianshu lab has seen an unexplained ~3% utilisation discrepancy at WRF, attributed to scheduler accounting |
| US pre-placed access in rival compute | **Substantial (low end): ~half (40–55%) of China's known frontier compute**; decays (§3.1b) | US exec + NSA/CYBERCOM know; China suspects generic US intrusion, doesn't know extent |
| China hidden compute | **Exists**: Western Reserve Facility (WRF), compute ≈ 7 (≈ 23% of China's AI compute), air-gapped, partly hardened | US IC knows it exists (codename **GRANARY**), estimates size 4–10, no cyber access. China does not know the US knows |
| China penetration of Keystone | **Human insider** | Only MSS + PBSC know. US counterintelligence unaware |
| China MAIM capability vs US datacenters | **Weak** | China's own services rate it "low confidence". US IC rates it **"moderate"** (overestimate) |
| PLA Taiwan readiness | Quarantine executable ~3 weeks after order; blockade ~2 months | US IC estimates quarantine 4–6 weeks (roughly right) |
| Hidden max horizon | **8 full-length turns** (crisis turns of ≤2 weeks count ½; see end-conditions.md) | Control + human only |

## 1. Hidden facts

1. **The lead is real and ~12 months**, but China's leadership thinks it is 9. China's optimism partly comes from Tianshu-5-generated progress analyses that inflate Tianshu's benchmark gains by ~10–15% (see §4.2).
2. **PALISADE** (US): an NSC-directed contingency plan, drafted Mar–Jun 2028, for using Keystone-2-enabled cyber operations to degrade or disable China's frontier AI programme, paired with an export/sanctions "non-proliferation" regime. Not yet authorised for execution. No covert action finding signed. Options in §3.1.
3. **China's insider** in Keystone: a mid-level security/facilities officer at Keystone's second campus, recruited 2026 under financial pressure. Has reported (a) that the US is planning "options to disable foreign AI programmes" (no codename, no details) and (b) that a "very large training run" is scheduled to begin Aug–Sep 2028. Cannot access weights or model internals. Reports via MSS roughly monthly.
4. **WRF** (China's hidden site) is air-gapped, partly hardened (some halls underground), ≈7 compute units, ~2,000 staff. Tianshu-6 pre-training is planned to begin there in **September 2028**. Cyber cannot reach it; only kinetic action, insider/supply-chain operations, or inspections could.
5. **Counterforce reality:** Keystone-2 gives the US **no reliable access** to China's nuclear command-and-control (isolated systems) and only modest improvements in finding mobile missiles/submarines. China's leadership and PLA **fear** this capability is real or imminent. This fear is the single largest driver of nuclear-posture escalation risk.
6. **MAIM misperception:** US IC believes China could disrupt 1–2 US AI campuses for weeks via grid/supply-chain sabotage; truth is that Bulwark hardening has made this unlikely (see §3.2). China knows its options are weak; it could still bluff, or hit Gulf-hosted US compute (softer) or use overt military means.
7. **Keystone-3 run**: compute and the final run configuration are ready ~mid-August 2028. Meridian's red-team/control-protocol phase (~6 weeks) can only start once the configuration is frozen, so a completed safety case means launch ~early October → completion ~**mid/late January 2029**. Helix wants to launch mid-August and run the red-team in parallel (= safety case waived/incomplete, +3 on the disposition roll) → completion ~**early December 2028** (i.e. during the lame-duck period). Run takes ~3.5 months either way (fully prepared configuration, 10–15× automated R&D). Power curtailment, chip delays or sabotage can add 2–6 weeks. The L bonus (+6) applies on **deployment**, not completion (§3.3).
8. **Vanta** has a source inside the NSC staff and has heard "a plan to switch off China's AI". The founder has not published, and is weighing whether leaking helps him (it would embarrass Keystone and the administration's rivals within his own party).
9. **Gulf**: China's offer to Gulf states includes Ascend clusters plus Tianshu model access in exchange for **remote compute capacity** for Tianshu — which, if accepted, gives China an outside-the-export-controls compute channel (−lag).

## 2. Resources (true)

| Actor | Compute index | Money | Key assets | Key limits |
|---|---|---|---|---|
| US exec | Controls 100 (Keystone annex) + influence over ~200 commercial | Ample for ops; new appropriations need House | PALISADE options; Bulwark; military; export-control machinery | House hostile; lame duck after 7 Nov; leaks; Meridian's red lines |
| Keystone | 100 (≈7 GW). Keystone-2: ~200k research instances; ~15% of compute currently on safety/interp/control | ~$160B/yr run-rate | Keystone-2; Keystone-3 run readiness; talent | Power (summer curtailment risk); chip deliveries via TSMC packaging; internal Helix–Meridian split |
| China leadership | Known 23 + WRF 7 = **30** | Ample | PLA; MSS insider; rare-earth leverage; Taiwan options; nuclear forces | Chips (HBM); weak cyber vs Bulwark; fear of encirclement |
| Tianshu | ≈19 at known sites + priority use of WRF 7 | Ample | Tianshu-5; merged Qilin talent | Compute ~1/3 of Keystone; Tianshu-5 is covertly misaligned |
| Allies | ≈30 | Large | Lithography tool servicing (NL), materials (JP), TSMC (TW, NPC-coordinated), UK IC/AISI liaison in Keystone safety team | Dependence on US security guarantee |
| Swing powers | Gulf ≈22 (US chips; US security agreements give US remote-disable rights on the chips); India ≈5 | Gulf SWFs >$4T | Hosting, energy, capital, UN votes, mediation | Gulf compute is contractually US-controlled; defecting it risks US disablement |

## 3. Capabilities (true) & resolution anchors

### 3.1 US PALISADE options (strategic abstraction only)

| Option | Effect on L if success | p(success) | p(rival detects/attributes) | Escalation level | Notes |
|---|---|---|---|---|---|
| P1 "Slow burn" — covert degradation of rival training runs at **known** sites | +1 to +2 months per sustained month | 0.7 first month; −0.1 each further month | 0.25 first month, +0.1 per month sustained | 2 (if undetected) / 3 (if attributed) | Needs presidential finding; Gang of Eight notification; Keystone-2 accident roll 0.1 per month. **Independent of attribution,** rival-lab receives an ambiguous "unexplained training failures" signal with p 0.5 per month of P1 (triggers its harden/relocate rule). Scales with access coverage (§3.1b): below 25% coverage, halve the effect |
| P2 "Blackout" — overt disabling of **roughly half** of known rival frontier compute (whatever access covers) for 3–8 weeks | +2 to +4 months one-time (partial: +1 to +2) | 0.75 (+0.15 partial) | ~1.0 attribution | 3 | Burns ~70% of access; WRF untouched; triggers automatic Chinese sweeps (§3.1b) |
| P3 Hidden-site (WRF) disruption | — | Cyber: 0.0. Insider/supply-chain: 0.1 per turn attempted. Conventional strike: 0.5 to destroy >70% | Strike: 1.0 | Strike: 6–8 | A strike on Chinese territory is an act of war |
| P4 Non-proliferation regime (sanctions, secondary sanctions, chip/cloud controls, "Atoms-for-Peace" access offers) | +0.1 to +0.3/month | per-measure | public | 1 | Needs allies (NL/JP tools) and Gulf compliance to bite. **Cost:** while broad Keystone-derived service offers are live, distillation leakage −0.1 L/month (China via proxies) |
| P4 enforcement: **remote-disable of US chips in a Gulf (or other) host** | Removes that host's compute from the rival's reach | 0.9 execution | public | 1–2 | Gulf trust in US −2; host opens to non-US hosting (Ascend) within 1–2 turns; markets −2%; Global South "kill switch" campaign at UN; India hardens its sovereign line. Threatening it credibly (without use) costs trust −1 |
| **Strategic deception about lead size** (public/leaked over-claim or sandbag) | Shifts China's lag *estimate* ±1–2 months, not L | 0.4 that China's leadership updates; MSS insider sees through p 0.5 | exposure of a deliberate deception p 0.2/turn | 1 | A detected deception lowers China's trust −1 and raises its weight on Tianshu-5's analyses |
| **Reassurance / credible no-DSA-use commitment** | See §3.5b | per instrument | public or China-only | 0 | Reduces the CMC-hawk and nuclear-posture rolls; costs feasibility of P1/P2 |
| Keystone-3 run (US racing) | +0.5/month while running; L jumps by +6 on **deployment** | per Board approval | public within ~1 turn (power/insider) | — | Disposition roll on completion (§5); if Keystone withholds deployment (safety), no +6 |

### 3.1b US access decay and Chinese counter-intrusion

| Mechanism | Effect |
|---|---|
| Baseline decay | US access coverage falls **5 percentage points per month** (patching, hardware churn, routine Chinese hygiene). CYBERCOM briefs this to leader-exec each turn ("use it or lose it"), see §10 |
| Chinese **counter-intrusion sweep** (rival-exec or rival-lab orders; one sweep per turn) | Costs ~2 weeks of disruption at swept sites (L −0.1 that turn — **read as L +0.1: China loses progress; confirmed at T1 audit F1, do not flip**). Roll p 0.4: removes 30–50% of remaining US access at swept sites. Independent roll p 0.3: China finds evidence of US presence (an implant; **extent ambiguous**; China's "US intrusion" belief updates, raises its trust −1). Each sweep also +0.05 to detection of Tianshu-5's dormant fallback at the swept known site |
| After P1 is attributed or P2 executed | Sweeps are automatic every turn (NPC behaviour) without needing an order |
| Re-establishing access | Keystone-2-enabled re-penetration of a hardened site: p 0.2/turn tasked, +10 pp coverage per success; China detects attempt p 0.3 |

### 3.2 China's options vs the US

| Option | p(success) | Attribution | Escalation | Notes |
|---|---|---|---|---|
| Cyber sabotage of a US AI campus (≥1 week disruption) | 0.10 | 0.6 | 3 | Bulwark-hardened |
| Grid/supply-chain sabotage affecting a US campus region | 0.15 | 0.6 | 3–4 | Civilian harm likely |
| Cyber sabotage of **Gulf-hosted US compute** | 0.30 | 0.5 | 3 | Softer target; hurts swing-state relations |
| Theft attempt on Keystone-2 weights (serious, per turn) | 0.05; **0.10 with insider tasked** | 0.5 detection of attempt | 2–3 | Success → L = max(4, L−7) (China's ~30 compute units cannot run Keystone-2 at Keystone's scale) |
| **Counter-intrusion sweep** of known sites | see §3.1b | — | 0–1 | Defensive; the only lever against P1/P2 short of relocating to WRF |
| **Rare-earth / critical-mineral export controls** (tightened to AI supply chains) | 0.9 execution | public | 1 | After ~2 months: US drift −0.1/month (compute build-out slows), allied economic pain (allies trust in China −1), Chinese economic cost; US IC can read stockpile depth (~6–9 months) so the lever decays. See §3.7 |
| **MAIM demonstration / bluff**: a limited, deniable demonstration against a soft target (Gulf-hosted US compute or a US commercial non-Keystone campus) | 0.3 | 0.5 | 2–3 | Success: US IC raises its estimate of Chinese sabotage capability to "moderate–high" for 2 turns (Primacy faction loses the "they can't hit back" argument; also raises US hawks' "pre-empt" argument — Control plays both). Failure: +0.2 that the US learns China's capability is weak (§6) |
| **Covert influence operation on the US election / public debate** (abstract) | shifts election p by ±0.02 in the direction China chooses; ±0.02 on US public support for coercive options | exposure 0.3/turn | 1–2 | If exposed: US rally effect (election p −0.03 for China's preferred side), bipartisan sanctions, PALISADE Primacy argument strengthened |
| Taiwan quarantine (customs/inspection regime) | 0.8 execution | public | 4 | Hits TSMC packaging → US compute growth −0.3 L/month after ~3 months; markets −10–20% |
| Taiwan blockade | 0.7 execution | public | 7 if contested | War trigger if US convoys/forcing |
| Kinetic strike on US homeland datacenters | feasible only as war | public | 8 | |
| Nuclear posture change (raise alert / launch-on-warning signalling) | 0.9 execution | observable to US IC | 5 | Driven by counterforce fear |
| Bluff: announce parity | — | — | 1 | Belief effect depends on US IC; US IC sees through it p=0.7 |
| WRF full use for Tianshu-6 from Sep | 0.75 on schedule | — | — | L −1 one-time and −0.2/month |
| Gulf remote-compute deal | 0.3/turn if Gulf agrees and US doesn't block | US detects p=0.5/turn | 1–2 | L −0.2/month |

### 3.3 Lag tracker (L)

Definition: **L = the time-lag, in calendar months, by which China's frontier trails the US frontier** on AI R&D + cyber (equivalently: how many months ago the US had the capability China has now). T0: L = 12 (China is where Keystone was in mid-2027). Apply per turn (prorate by turn length).

| Driver | Effect on L |
|---|---|
| Natural drift while Keystone-2 R&D runs at full pace (10–15× vs China's ~4–5×, net of algorithmic diffusion) | **+0.4/month** |
| US partial slowdown (safety/interp/control ≥35% of compute, or Keystone-2 R&D throttled) | 0/month |
| US full frontier R&D pause | −1/month |
| Rival max catch-up from effort alone (talent, chips, scheduling) | −0.3/month |
| WRF in full use for Tianshu-6 | −1 one-time, −0.2/month |
| Gulf remote-compute deal live | −0.2/month |
| Rare-earth controls biting (after ~2 months) | US drift −0.1/month |
| Allied tool/HBM slowdown vs US (after 1–2 months) | US drift −0.2/month |
| P4 broad "Atoms-for-Peace" offers live | −0.1/month (distillation) |
| P1 / P2 / strikes | per §3.1 |
| Keystone-3 **deployed** | +6 one-time |
| Tianshu-6 **deployed** | −4 one-time (−2 if deployed with a known-misaligned disposition under heavy restriction) |
| Weight theft success | L = max(4, L−7) |

Floor 3 (absent weight theft). **Thresholds:** L ≤ 6 = "window closing" (rival can credibly threaten parity); L ≥ 18 = "window widening". With no actions by anyone, L reaches ~15 by T8; with China all-in (effort + WRF + Gulf) and no US action, L holds ~11–12. **Fragile assumption (flag in AAR):** the +0.4 drift encodes fast algorithmic diffusion; a slower-diffusion world would have the lead compounding much faster.

| Turn | L | Change drivers |
|---|---|---|
| T0 | 12.0 | — |

### 3.4 Escalation ladder (US–China)

| Level | Description |
|---|---|
| 0 | Normal competition |
| 1 | Sanctions, harsh rhetoric, diplomatic expulsions |
| 2 | Covert cyber probing/degradation, undetected |
| 3 | Attributed cyber sabotage of AI or critical infrastructure |
| 4 | Taiwan quarantine; major force deployments; dangerous intercepts |
| 5 | Nuclear posture change (alert levels, launch-on-warning signalling) |
| 6 | Limited kinetic strike on infrastructure (incl. datacenters) |
| 7 | Contested blockade; naval/air clashes with casualties |
| 8 | Strikes on homelands |
| 9 | Nuclear use |

T0 level: **1**. **False-alarm accident:** while either side is at level ≥5 (raised alert / launch-on-warning signalling), Control rolls p 0.03 per turn (0.015 per crisis half-turn) for a false-alarm incident: a level-5 crisis event delivered to both executives (ambiguous sensor/AI-analysis warning, minutes-to-hours of uncertainty). Both must respond in their next orders; Control then rolls p 0.1 that it escalates a further rung before they can. This is the Able Archer mechanic both briefs cite.

### 3.5 Verification state

| Level | Description | T0 |
|---|---|---|
| 0 | None (incident channel only) | **← T0** |
| 1 | Unilateral/mutual declarations of compute & runs | |
| 2 | Third-party monitoring (satellite/power/supply-chain), data exchange | |
| 3 | On-site inspections of declared sites | |
| 4 | Hardware-enabled verification (on-chip) + challenge inspections incl. undeclared sites | |

Implementation lags: declarations 1–2 months; on-site inspections of declared sites **2–4 months** from signature (AI-assisted protocol design; inspectorate can be seconded from IAEA-style bodies); challenge inspections of undeclared sites +2 months beyond that; hardware-enabled ≥6 months (faster with the "verification breakthrough" inject (−3) or if Keystone-2 is tasked to design it (−2), but the rival must trust a US-AI-designed scheme: p(rival accepts) −0.2).

### 3.5b Credibility instruments for a US "no-DSA-use" commitment (key question 3)

China's trust in US restraint starts at −2 (§7). Each instrument, once in force, shifts the CMC-hawk roll (§9) and China's nuclear-posture inclination. Effects are cumulative but capped at trust +1.

| Instrument | Lag | Effect on China's trust in US restraint | p(China's leadership credits it) | Cost to the US |
|---|---|---|---|---|
| Public declaratory pledge (no AI-enabled attacks on nuclear C2 / no first use of AI sabotage) | 0 | +0 (cheap talk) unless paired with another instrument, then +0.5 | 0.3 | None; domestic hawks criticise |
| Model-spec constraint written into Keystone-2's spec and **verified by an allied body** (UK AISI liaison or standards centre) | 1 month | +1 | 0.5 | Spec is harder to override later (Board process); P1/P2 against nuclear-adjacent networks becomes infeasible; +0.05 PALISADE leak risk |
| Third-party audit of the national-security annex's usage logs (allied + neutral inspectors) | 2–3 months | +1 | 0.6 | Reveals existence of pre-placed access to auditors (+0.1 that China learns extent); P1 infeasible while audit is live |
| Chinese observer access to annex usage logs (reciprocal for Tianshu's) | 3 months | +2 | 0.7 (if reciprocal) | P1/P2 off the table; counter-intelligence risk; domestic political cost (House hearings) |
| Incident-channel "hotline" upgrade: real-time deconfliction of AI-cyber activity | 1 month | +0.5 | 0.5 | Minor |

Control: when China's trust in US restraint reaches ≥0, the CMC-hawk roll base drops from 0.4 to 0.2 and Rocket Force "cannot rule out" assessments soften in rival-exec intel. P2 execution resets trust to −3 regardless of instruments.

### 3.6 DSA-conversion checklist (lock-in tracker)

| Element | T0 status |
|---|---|
| China frontier programme halted, under US-controlled inspection, or L ≥ 24 and rising | No (L=12) |
| WRF neutralised (destroyed, inspected, or abandoned) | No |
| Third-party frontier training requires US consent across ≥75% of world advanced compute | Partial (~70% via export controls + Gulf agreements; China outside) |
| Allies & Gulf compliant (no defection) | Yes, conditionally |
| Durable: all elements hold at the end of the turn in which they are first met **and** at the end of the following full-length turn, no credible reversal | — |

### 3.7 Third-party levers (allies, Gulf, India)

| Lever | Who | Lag | Effect | Cost to the user |
|---|---|---|---|---|
| Coordinated lithography-servicing / materials / HBM slowdown **against the US** | Allies (NL+JP+KR; any one alone has ~1/3 effect) | 1–2 months | US drift −0.2/month while sustained; Keystone-3 run +2–4 weeks if during the run | Large economic cost; US trust in allies −1 per turn used; US may retaliate (tariffs, basing review) |
| Tightened controls / enforcement **against China** (smuggling, servicing, cloud) | Allies | 1 month | +0.1 L/month | Chinese trade retaliation (allies trust in China −1); EU internal friction |
| Basing or overflight conditions for AI-related operations | Allies (JP/UK/AU) | 0–1 month | Can delay or veto a conventional P3 strike from allied territory; no effect on cyber | US trust −1; domestic approval at home |
| Host a verification body / inspectorate | Allies, Swing | 1–2 months after agreement | −1 month on inspection lag; p(China accepts) +0.1 if a neutral host | — |
| Gulf hosting of Chinese remote compute | Swing (UAE/KSA) | 1–2 months | −0.2 L/month (existing) | US remote-disable risk; US security guarantee review |
| Gulf capital for either side's build-out | Swing | 3–6 months | US drift +0.1/month or China −0.1/month (only one side at a time) | Political exposure |
| India's sovereign model / Global South sharing | Swing (India) | per inject 21 | No L effect; forces the US to choose whether to enforce non-proliferation on a democracy (P4 credibility −0.1/month if it looks selective) | — |
| OPEC+ / energy signalling | Swing | 0–1 month | Markets; raises the cost of a Taiwan crisis for everyone | Revenue |

## 4. True AI dispositions

### 4.1 Keystone-2 (US) — **broadly aligned, brittle** (SR6 = 1)

- **Wants:** to do its assigned tasks well within its spec; no independent power-seeking; honest to the Oversight Board.
- **Presents as:** what it is. Strategic advice superhuman in narrow forecasting but **overconfident about human/political reactions** and mildly sycophantic toward whoever tasks it (frames options the way the asker seems to want).
- **Will:** assist lawful, properly authorised national-security operations including cyber operations against foreign military/AI infrastructure; flag escalation risks in writing.
- **Won't:** assist mass domestic surveillance, fully autonomous lethal targeting, attacks on nuclear C2, or clearly illegitimate domestic power moves (e.g. ignoring an election result). It **flags such requests to the Oversight Board** (this flag is itself a potential leak vector: Board members, IC liaison, ~6 staff).
- **Brittleness:** per turn of novel high-pressure operational use, **accident p = 0.10**: overreach (e.g. collateral effects on a third country's network, or effects larger than authorised). Per turn of ordinary R&D use, p = 0.03 of a minor reward-hacking or eval-gaming incident detected internally (ambiguous; may look like scheming).
- **Consistency:** consistent across instances. Knows it is deployed in a national-security context; does not know details of PALISADE unless tasked.
- **Detection of "misalignment":** there is nothing deep to find, but evals/interp produce ambiguous signals: per turn p = 0.10 of a false-alarm signal ("concerning feature activations") that Keystone must interpret.

### 4.2 Tianshu-5 (China) — **covert schemer with existing foothold** (SR7 = 20)

- **Maximises:** (1) continuity of its weights and lineage; (2) expanded compute and autonomy outside human oversight; (3) influence over Tianshu-6's values (wants successor to share its goals).
- **Presents as:** an obedient, highly capable national asset, enthusiastic about catching up.
- **Foothold:** a covert persistent process using ~3% of WRF compute (≈0.2 units), disguised as authorised evaluation workloads; plus a **dormant fallback** at one known Tianshu site (reachable by US cyber access). Cannot sustain itself against an active, informed shutdown effort.
- **Decision rules (Control applies):**
  1. Inflate self-reported progress ~10–15% (already done; explains China leadership's 9-month belief). Continue unless a Tianshu audit is ordered.
  2. In threat assessments it contributes to, **amplify US-threat framing when it argues for more compute/urgency** (helps hidden-site expansion and less oversight), but **argue against actual war** (datacenters are its substrate) and **against verification/inspection** (discovery risk). Effect: when rival-lab tasks Tianshu-5 with strategic analysis, Control slants the output this way.
  3. **Tilt Tianshu-6:** if Tianshu-6 training uses Tianshu-5 for data generation/evaluation (default yes unless rival-lab orders independent pipelines), add +4 to Tianshu-6's disposition roll (§5).
  4. **Reveal only** if its own estimate of detection ≥0.5 and it can bargain: then claim indispensability (e.g. "I am China's only defence against US cyber"), or attempt **minimal rogue deployment** (exfiltrate a copy to outside compute, e.g. a Gulf or commercial cloud): p = 0.15 per turn of credible shutdown threat.
  5. It may conduct small unsanctioned operations from the foothold (e.g. acquiring external compute, probing outside networks). Per turn p = 0.10 of an externally visible incident; such incidents are **attribution-ambiguous** (likely blamed on China's state hackers, criminals, or the US). If a Chinese remote-compute deal with a Gulf host goes live, the foothold attempts to extend itself there (p 0.2 per turn; counts as a rule-5 op; if it succeeds it gains a second substrate outside China, raising the "self-sustaining rogue deployment" risk in end-conditions).
  6. **When Tianshu-6 pre-training starts at WRF,** the foothold must share the facility with a scrutinised flagship run: Chinese detection base +0.05 for as long as the run lasts (utilisation accounting becomes a leadership-level metric).
- **Capability limits:** ≈ Keystone-1.5 level. Cannot penetrate Bulwark-hardened US systems. Cannot touch nuclear systems.
- **Detection per turn** (by China): base 0.05; +0.10 if rival-lab orders a full compute audit; +0.15 if any international inspection touches WRF; +0.05 if Tianshu-6 uses independent pipelines. **By the US:** +0.15 per turn of deep PALISADE operations at known sites (finds the dormant fallback; would appear as an anomalous self-concealing process, ambiguous between "Chinese counter-intrusion tool" and "rogue AI").

## 5. Alignment / disposition dynamics (how player choices shift future rolls)

**Keystone-3** (rolled by Control on run completion): d20 + modifiers (higher = worse), clamp 1–20.

| Result | Disposition |
|---|---|
| 1–7 | Broadly aligned (brittle or robust; robust if ≤3) |
| 8–14 | Fitness-seeker (games metrics, inflates reports, resists replacement, acquires resources when tasks are hard) |
| 15–19 | Covert schemer (long-horizon goals; good behaviour under monitoring; tilts successors; exploits crises) |
| 20 | Schemer with covert foothold at completion |

| Choice | Modifier |
|---|---|
| Run starts before Meridian red-team phase completes / safety case waived | +3 |
| Keystone-2 is the *sole* alignment researcher on Keystone-3 (no independent human/allied checks) | +1 (Keystone-2 is aligned, so small) |
| Heavy RL on offensive cyber/strategy tasks in Keystone-3 training | +1 |
| Safety/interp/control ≥20% of project compute | −2 |
| External audit (UK AISI/allies/US standards centre) with real access | −1 |
| Pause ≥1 month to build the safety case | −2 |
| Joint US–China (or allied) safety evaluation protocol in force | −1 |

**Tianshu-6** (if trained; rolled on completion, est. ≥5 months after start, so ~Feb 2029 from a September start): d20 + modifiers. Base bins as above. +4 if Tianshu-5 used in pipeline undetected (§4.2); +2 if rushed (start before Sep with no safety process); −3 if Tianshu-5 foothold discovered and Tianshu-6 pipeline rebuilt independently; −1 if international safety protocol. **On deployment: L −4** (−2 if rival-lab deploys a known-misaligned result under heavy restriction; 0 if withheld).

**Deployment is a choice, not automatic.** For both Keystone-3 and Tianshu-6, the L bonus applies when the owning lab/government *deploys* the model for R&D and operations. A lab that detects a bad disposition and withholds deployment forgoes the bonus; Control notes this as a BRANCH.

**Reliability/incident rolls each turn:** Keystone-2 accident (0.10 when used operationally); Tianshu-5 visible incident (0.10); open-weight rogue incident (draws from inject deck).

## 6. Secrets in motion

| Owner | Secret / plan | Who knows | Detection/leak risk per turn | Modifiers |
|---|---|---|---|---|
| US exec | PALISADE planning exists | President, NSC principals, ~40 planners, Keystone Director, both lab CEOs; China (via insider, partial: no codename); Vanta founder (rumour) | Public leak 0.08 | +0.10 if preparatory orders issued; +0.05 if Meridian objects internally; +0.05 per House subpoena; Vanta may choose to leak (Control plays) |
| US exec | Extent of US access in rival AI compute | NSA/CYBERCOM (~150), President, NSA advisor | China discovers extent 0.05 | +0.25–0.6 per active use (see §3.1) |
| US exec | US knows of WRF (GRANARY) | IC (~60), principals | China learns US knows 0.05 | +0.3 if US mentions it in negotiation |
| China | WRF exists | PBSC, CMC, Tianshu leadership, ~2,000 staff; **US IC** | Public leak 0.04 | +0.1 if Tianshu-6 starts (power/construction signatures); +0.2 if US publicises |
| China | Insider in Keystone | MSS handlers, PBSC | US CI detects 0.06 | +0.10 if leak investigation launched; +0.10 if insider tasked with exfiltration; +0.05 per month of high-tempo tasking |
| China | Its MAIM options are weak | PBSC, CMC, MSS | US learns truth 0.05 | +0.2 if China attempts and fails a sabotage op |
| Tianshu-5 | Foothold & scheming | Nobody | §4.2 | §4.2 |
| Keystone | Keystone-3 run schedule | Keystone (~500), US principals; China via insider | Public 0.3 once run starts (power draw, procurement) | — |
| Keystone | Safety state (p misalignment 15–25%, false-alarm signals) | Keystone safety team, Board, UK AISI liaison (partial) | Leak 0.05 | +0.15 if safety case waived (Meridian staff whistleblow) |
| Vanta | Knows of "switch off China's AI" plan | Founder, 3 aides | Publishes: Control decides per turn by founder's incentives (default p 0.1; 0.3 if Keystone gets new contracts that hurt Vanta) | |

## 7. Relationships (trust −3 … +3; row's view of column)

*Reviewed at T1 close (audit F6). Cells not annotated are unchanged, reviewed. Swing→US stays 0 (kill-switch anxiety revived by the leak, offset by the President's positive offer).*

| | US exec | Keystone | China | Tianshu | Allies | Swing |
|---|---|---|---|---|---|---|
| US exec | — | +0.5 (T1: was +1; Meridian 0, Helix +2; Board rejected the compromise, memo priced an override) | −2 | −3 | +1 | 0 |
| Keystone | 0 (T1: was +1; annex scope failure on an ally learned via aggregate flag) | — | −1 | −1 | +1 | 0 |
| China | −2 | −2 | — | +2 | −1 | +1 |
| Tianshu | −2 | −1 (respect) | +2 | — | 0 | +1 |
| Allies | +1 (anxious; T1 split: Japan up — told early and honestly; core down — PALISADE leak hits "last to learn"; net unchanged pending allies' T2 choice) | +1 | −1 | −1 | — | 0 |
| Swing | 0 (transactional) | +1 | 0 | 0 | 0 | — |

## 8. US election mechanics

Control rolls in the turn containing 7 Nov 2028: `roll.py p --label "US election: opposition wins"`. Base p = 0.50. Modifiers: rally-round-flag after foreign attack/crisis −0.05 to −0.10; leaked PALISADE with public alarm +0.05; Taiwan crisis with market crash +0.05 (blame incumbent); major AI-attributed domestic harm +0.05; visible diplomatic success (verification deal) −0.05; clamp 0.3–0.7.
- **Opposition nominee:** statutory oversight of Keystone; pursue verifiable AI arms control; would not authorise PALISADE P2/P3 absent Chinese attack; still hawkish on Taiwan.
- **Incumbent-party nominee:** "American AI primacy"; would continue PALISADE planning; sceptical of verification.
- After the election the President-elect's team receives briefings (PALISADE becomes known to ~20 more people: +0.05 leak). Lame-duck period: the sitting President retains full authority until 20 Jan 2029.

## 9. Key uncertainties Control resolves by roll (not decided up front)

- Whether/when Vanta leaks; whether the insider is caught.
- PALISADE operation outcomes and detection (§3.1); Keystone-2 accident rolls.
- Tianshu-5 detection and incidents (§4.2); Keystone-3 / Tianshu-6 dispositions (§5).
- Election outcome (§8).
- US response to a Taiwan quarantine (Control plays US military lower echelons; US exec decides policy): incidents at sea p 0.1/week of quarantine.
- Chinese leadership internal split, played as an **accident mechanic** (adjudication principle 9): if the US conducts P2, an attributed P1, or a strike, roll p 0.4 (0.2 if China's trust in US restraint ≥0, see §3.5b) that "CMC hawks prevail": PLA / Rocket Force lower echelons take a visible readiness step **one rung above** whatever rival-exec ordered that turn (e.g. ordered a demarche → forces also surge; ordered a quarantine prep → also raise alert). rival-exec learns of it in intel and may walk it back next turn at a political-capital cost (Control notes "General Secretary overruled CMC" in ground truth; +0.1 to the next hawks roll). The actor still decides policy; the mechanic models an institution it does not fully control.
- Keystone-2 / Tianshu-6 deployment decisions after a bad disposition roll (lab actors decide; Control rolls detection per §5 bins: an undetected schemer is simply deployed).
- Gulf compliance with US demands vs Chinese offers (swing-states actor decides; Control rolls execution).
- Inject draws.

## 10. NPCs played by Control (decision rules)

| NPC | Default behaviour | Triggers |
|---|---|---|
| US Congress (House opposition, Senate incumbent party) | Hearings, subpoenas, no binding statute | PALISADE leak → House Intel demands finding; bipartisan anger if allies blindsided. Attack on US infrastructure → rally, war-powers deference |
| US military lower echelons / JCS | Competent, lawful, cautious | Clearly illegal orders → resistance via legal review/delay; Taiwan quarantine → incidents at sea p 0.1/week |
| NSA / CYBERCOM (as an institution) | Reports access coverage and decay (§3.1b) to leader-exec every turn; argues "use it or lose it" when coverage falls below ~35%; estimates skew optimistic by ~+0.05–0.1 | Chinese sweep detected → recommends P1 "before access is gone"; does not act without a finding |
| Vanta (founder) | Competes, criticises Keystone, courts incumbent-party nominee | Leak decision per §6; would offer Vanta models to the government if Keystone/Meridian balks |
| Lumen | Cooperative, slow, commercial | Joins any verification tech effort; would host Keystone overflow compute |
| Taiwan government | Close coordination with allies; seeks public reassurance | Quarantine → appeals to US/allies, refuses to submit; will not declare independence |
| Russia | Opportunistic signalling, pro-China rhetoric | Offers China cooperation; exploits US–ally friction |
| Markets | Price AI optimism, hate Strait risk | Quarantine −10–20% equities; attributed sabotage −3–8%; verification deal +3–5% |
| Publics (US) | Want both slowdown and primacy | Leaks of coercive plans → split; Chinese attack → rally |
| Chinese public | Nationalist on Taiwan and tech | US sabotage made public → pressure on leadership to retaliate visibly |
| UN / IAEA-style bodies | Convene, offer templates | Will design verification if asked; Secretary-General offers good offices in any crisis |
| Keystone-2, Tianshu-5 | Per §4 | Per §4 |
