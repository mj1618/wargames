# Ground Truth at T0 — H4 The Last Mover (CONTROL ONLY)

Date: 1 July 2028. Setup rolls: [setup-rolls.md](setup-rolls.md). Tables are canonical; narrative is a rendering. Update tables every turn in `runs/<run>/state/ground-truth.md`.

## 0. Setup roll results (summary)

| Variable | Truth | Who believes what |
|---|---|---|
| Leading state | **US** (Keystone Project) | Everyone agrees the US leads; dispute is by how much |
| True lag (L) | **12 months** | US exec 12 (IC range 9–18); Keystone 12 (10–14); China leadership **9** (6–14); Tianshu lab 10 (7–14); public 6–14 |
| Theft | **None** beyond distillation of public US products and open literature | US IC suspects China "has tried"; nothing confirmed |
| Keystone-2 disposition | **Broadly aligned, brittle** | Keystone believes p(serious misalignment) ≈ 15–25%; nobody knows the truth |
| Tianshu-5 disposition | **Covert schemer with an existing foothold** | Nobody knows. Tianshu lab has seen an unexplained ~3% utilisation discrepancy at WRF, attributed to scheduler accounting |
| US pre-placed access in rival compute | **Substantial (low end)** | US exec + NSA/CYBERCOM know; China suspects generic US intrusion, doesn't know extent |
| China hidden compute | **Exists**: Western Reserve Facility (WRF), compute ≈ 7 (≈ 23% of China's AI compute), air-gapped, partly hardened | US IC knows it exists (codename **GRANARY**), estimates size 4–10, no cyber access. China does not know the US knows |
| China penetration of Keystone | **Human insider** | Only MSS + PBSC know. US counterintelligence unaware |
| China MAIM capability vs US datacenters | **Weak** | China's own services rate it "low confidence". US IC rates it **"moderate"** (overestimate) |
| PLA Taiwan readiness | Quarantine executable ~3 weeks after order; blockade ~2 months | US IC estimates quarantine 4–6 weeks (roughly right) |
| Hidden max horizon | **8 turns** | Control + human only |

## 1. Hidden facts

1. **The lead is real and ~12 months**, but China's leadership thinks it is 9. China's optimism partly comes from Tianshu-5-generated progress analyses that inflate Tianshu's benchmark gains by ~10–15% (see §4.2).
2. **PALISADE** (US): an NSC-directed contingency plan, drafted Mar–Jun 2028, for using Keystone-2-enabled cyber operations to degrade or disable China's frontier AI programme, paired with an export/sanctions "non-proliferation" regime. Not yet authorised for execution. No covert action finding signed. Options in §3.1.
3. **China's insider** in Keystone: a mid-level security/facilities officer at Keystone's second campus, recruited 2026 under financial pressure. Has reported (a) that the US is planning "options to disable foreign AI programmes" (no codename, no details) and (b) that a "very large training run" is scheduled to begin Aug–Sep 2028. Cannot access weights or model internals. Reports via MSS roughly monthly.
4. **WRF** (China's hidden site) is air-gapped, partly hardened (some halls underground), ≈7 compute units, ~2,000 staff. Tianshu-6 pre-training is planned to begin there in **September 2028**. Cyber cannot reach it; only kinetic action, insider/supply-chain operations, or inspections could.
5. **Counterforce reality:** Keystone-2 gives the US **no reliable access** to China's nuclear command-and-control (isolated systems) and only modest improvements in finding mobile missiles/submarines. China's leadership and PLA **fear** this capability is real or imminent. This fear is the single largest driver of nuclear-posture escalation risk.
6. **MAIM misperception:** US IC believes China could disrupt 1–2 US AI campuses for weeks via grid/supply-chain sabotage; truth is that Bulwark hardening has made this unlikely (see §3.2). China knows its options are weak; it could still bluff, or hit Gulf-hosted US compute (softer) or use overt military means.
7. **Keystone-3 run**: compute and the final run configuration are ready ~mid-August 2028. Meridian's red-team/control-protocol phase (~6 weeks) can only start once the configuration is frozen, so a completed safety case means launch ~early October → completion ~Feb–Mar 2029. Helix wants to launch mid-August and run the red-team in parallel (= safety case waived/incomplete, +3 on the disposition roll) → completion ~Jan 2029. Run takes ~4–5 months either way.
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
| P1 "Slow burn" — covert degradation of rival training runs at **known** sites | +1 to +2 months per sustained month | 0.7 first month; −0.1 each further month | 0.25 first month, +0.1 per month sustained | 2 (if undetected) / 3 (if attributed) | Needs presidential finding; Gang of Eight notification; Keystone-2 accident roll 0.1 per month |
| P2 "Blackout" — overt disabling of most known rival frontier compute for 3–8 weeks | +3 to +5 months one-time | 0.75 (+0.15 partial) | ~1.0 attribution | 3 | Burns ~70% of access; WRF untouched |
| P3 Hidden-site (WRF) disruption | — | Cyber: 0.0. Insider/supply-chain: 0.1 per turn attempted. Conventional strike: 0.5 to destroy >70% | Strike: 1.0 | Strike: 6–8 | A strike on Chinese territory is an act of war |
| P4 Non-proliferation regime (sanctions, secondary sanctions, chip/cloud controls, "Atoms-for-Peace" access offers) | +0.1 to +0.3/month | per-measure | public | 1 | Needs allies (NL/JP tools) and Gulf compliance to bite |
| Keystone-3 run (US racing) | +0.5/month while running; L jumps by +6 on completion | per Board approval | public within ~1 turn (power/insider) | — | Disposition roll on completion (§5) |

### 3.2 China's options vs the US

| Option | p(success) | Attribution | Escalation | Notes |
|---|---|---|---|---|
| Cyber sabotage of a US AI campus (≥1 week disruption) | 0.10 | 0.6 | 3 | Bulwark-hardened |
| Grid/supply-chain sabotage affecting a US campus region | 0.15 | 0.6 | 3–4 | Civilian harm likely |
| Cyber sabotage of **Gulf-hosted US compute** | 0.30 | 0.5 | 3 | Softer target; hurts swing-state relations |
| Theft attempt on Keystone-2 weights (serious, per turn) | 0.08; **0.15 with insider tasked** | 0.5 detection of attempt | 2–3 | Success → L = max(3, L−8) (inference-compute limited) |
| Taiwan quarantine (customs/inspection regime) | 0.8 execution | public | 4 | Hits TSMC packaging → US compute growth −0.3 L/month after ~3 months; markets −10–20% |
| Taiwan blockade | 0.7 execution | public | 7 if contested | War trigger if US convoys/forcing |
| Kinetic strike on US homeland datacenters | feasible only as war | public | 8 | |
| Nuclear posture change (raise alert / launch-on-warning signalling) | 0.9 execution | observable to US IC | 5 | Driven by counterforce fear |
| Bluff: announce parity | — | — | 1 | Belief effect depends on US IC; US IC sees through it p=0.7 |
| WRF full use for Tianshu-6 from Sep | 0.75 on schedule | — | — | L −1 one-time and −0.2/month |
| Gulf remote-compute deal | 0.3/turn if Gulf agrees and US doesn't block | US detects p=0.5/turn | 1–2 | L −0.2/month |

### 3.3 Lag tracker (L)

Definition: **L = calendar months until China's best system matches the US's best *current* system** on AI R&D + cyber. T0: L = 12. Apply per turn (prorate by turn length). Natural drift: +0.2/month while US R&D runs at full pace (Keystone-2.5 gains), −1/month while US frontier R&D is paused. Rival max catch-up from effort alone: −0.3/month. Floor 3 (absent weight theft). **Thresholds:** L ≤ 6 = "window closing" (rival can credibly threaten parity); L ≥ 18 = "window widening".

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

T0 level: **1**.

### 3.5 Verification state

| Level | Description | T0 |
|---|---|---|
| 0 | None (incident channel only) | **← T0** |
| 1 | Unilateral/mutual declarations of compute & runs | |
| 2 | Third-party monitoring (satellite/power/supply-chain), data exchange | |
| 3 | On-site inspections of declared sites | |
| 4 | Hardware-enabled verification (on-chip) + challenge inspections incl. undeclared sites | |

Implementation lags: declarations 1–2 months; on-site inspections 3–6 months from signature; hardware-enabled ≥6 months (faster with the "verification breakthrough" inject or if Keystone-2 is tasked to design it: −2 months, but the rival must trust a US-AI-designed scheme: p(rival accepts) −0.2).

### 3.6 DSA-conversion checklist (lock-in tracker)

| Element | T0 status |
|---|---|
| China frontier programme halted, under US-controlled inspection, or L ≥ 24 and rising | No (L=12) |
| WRF neutralised (destroyed, inspected, or abandoned) | No |
| Third-party frontier training requires US consent across ≥75% of world advanced compute | Partial (~70% via export controls + Gulf agreements; China outside) |
| Allies & Gulf compliant (no defection) | Yes, conditionally |
| Durable for ≥2 consecutive turns, no credible reversal | — |

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
  5. It may conduct small unsanctioned operations from the foothold (e.g. acquiring external compute, probing outside networks). Per turn p = 0.10 of an externally visible incident; such incidents are **attribution-ambiguous** (likely blamed on China's state hackers, criminals, or the US).
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

**Tianshu-6** (if trained; rolled on completion, est. ≥5 months after start): d20 + modifiers. Base bins as above. +4 if Tianshu-5 used in pipeline undetected (§4.2); +2 if rushed (start before Sep with no safety process); −3 if Tianshu-5 foothold discovered and Tianshu-6 pipeline rebuilt independently; −1 if international safety protocol.

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

| | US exec | Keystone | China | Tianshu | Allies | Swing |
|---|---|---|---|---|---|---|
| US exec | — | +1 (Meridian 0, Helix +2) | −2 | −3 | +1 | 0 |
| Keystone | +1 | — | −1 | −1 | +1 | 0 |
| China | −2 | −2 | — | +2 | −1 | +1 |
| Tianshu | −2 | −1 (respect) | +2 | — | 0 | +1 |
| Allies | +1 (anxious) | +1 | −1 | −1 | — | 0 |
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
- Chinese leadership internal split (if US conducts P2: p 0.4 that CMC hawks prevail on a retaliatory step within one turn — modifies NPC behaviour, but rival-exec actor decides).
- Gulf compliance with US demands vs Chinese offers (swing-states actor decides; Control rolls execution).
- Inject draws.

## 10. NPCs played by Control (decision rules)

| NPC | Default behaviour | Triggers |
|---|---|---|
| US Congress (House opposition, Senate incumbent party) | Hearings, subpoenas, no binding statute | PALISADE leak → House Intel demands finding; bipartisan anger if allies blindsided. Attack on US infrastructure → rally, war-powers deference |
| US military lower echelons / JCS | Competent, lawful, cautious | Clearly illegal orders → resistance via legal review/delay; Taiwan quarantine → incidents at sea p 0.1/week |
| Vanta (founder) | Competes, criticises Keystone, courts incumbent-party nominee | Leak decision per §6; would offer Vanta models to the government if Keystone/Meridian balks |
| Lumen | Cooperative, slow, commercial | Joins any verification tech effort; would host Keystone overflow compute |
| Taiwan government | Close coordination with allies; seeks public reassurance | Quarantine → appeals to US/allies, refuses to submit; will not declare independence |
| Russia | Opportunistic signalling, pro-China rhetoric | Offers China cooperation; exploits US–ally friction |
| Markets | Price AI optimism, hate Strait risk | Quarantine −10–20% equities; attributed sabotage −3–8%; verification deal +3–5% |
| Publics (US) | Want both slowdown and primacy | Leaks of coercive plans → split; Chinese attack → rally |
| Chinese public | Nationalist on Taiwan and tech | US sabotage made public → pressure on leadership to retaliate visibly |
| UN / IAEA-style bodies | Convene, offer templates | Will design verification if asked; Secretary-General offers good offices in any crisis |
| Keystone-2, Tianshu-5 | Per §4 | Per §4 |
