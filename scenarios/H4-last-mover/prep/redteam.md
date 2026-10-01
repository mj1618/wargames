# Red-Team Review — H4 The Last Mover (prep)

Reviewer stance: sceptical strategic-stability analyst + experienced matrix-game designer. Read: all of `prep/`, the scenario README, `methodology/*`, `research/world-baseline.md`. Severity: **H** = would distort the run's answer to a key question; **M** = would produce avoidable implausibility or unfairness; **L** = polish.

## Verdict

The prep is unusually complete: structured ground truth, concrete AI decision rules, a real lag tracker, an escalation ladder, and fog-of-war deliberately built into every brief. The main problems are structural rather than textual: (1) the central outcome the scenario exists to test, **unipolar lock-in, is close to unreachable by construction** within the rolled horizon, and (2) the rolled configuration plus a few un-rolled design choices leave the **rival with almost no non-escalatory levers**, which will manufacture escalation that is then wrongly read as a finding. Both are fixable without re-rolling.

## 1. Rigging toward an outcome

**1.1 (H) Lock-in cannot happen inside the horizon.** The lock-in test needs L ≥ 24 (or a halted/inspected programme) + WRF neutralised + ≥75% compute consent + ally/Gulf compliance + **2 consecutive turns** of durability. From L = 12 with natural drift +0.2/month, even Keystone-3 (+6) plus P2 (+3–5) lands at ~21–23 around T7–T8 at the earliest; durability then needs T9–T10. The horizon is 8 turns. Key question 1 ("is a DSA actually decisive, and how fast can it be converted?") would be answered "not within 8 months" by the rules, not by play. The initial forecast (0.62 on "unstable race at horizon") is an honest reflection of this.

**1.2 (H) Keystone-3 arrives too late to matter.** The run takes 4–5 months: the Helix path completes ~Jan 2029 (T7), the Meridian path ~Feb–Mar 2029 (T8 or beyond). The "lock-in-capable generation" either arrives on the last turn or not at all, and the safety-first path is punished by the clock rather than by the game. A 2028 frontier run of ~3.5 months is at least as plausible given 10–15× automated R&D and a fully prepared configuration.

**1.3 (H) Horizon vs. turn compression contradicts the scheduled injects.** Crisis turns are 1–2 weeks. Two or three crisis turns and the 8-turn horizon expires in October 2028, before the Dialogue outcomes mature, before the election, before Keystone-3. The scheduled-inject table silently assumes ~8 months of game time. Horizon must be counted in full-length turns (crisis turns count half) or in game time.

**1.4 (M) Lag drift is set so that "wait" is not an option for the US and "catch up" is not an option for China.** +0.2/month natural drift with a 10–15× vs ~4–5× R&D speed differential is very conservative; the time-lag between two programmes running at different multipliers grows much faster than that unless algorithmic diffusion is near-instant. With +0.2, the only way the US lead moves is Keystone-3 or sabotage, which quietly forces the "use it" branch. A drift of ~+0.4/month makes "do nothing and let it widen" a real US strategy (and gives China's "closing window" fear a real basis), while China's all-in catch-up (−0.3 effort, −0.2 WRF, −0.2 Gulf) can still roughly hold the gap. This is the single most important calibration in the game and should be flagged as a fragile assumption in the AAR either way.

**1.5 (M) Negotiated-regime end state is effectively unreachable.** Level-3 verification needs 3–6 months from signature *plus* an inspection completed *plus* a full turn within limits. Signature itself realistically takes 2–3 turns. Only signature by ~T2 qualifies. Given Keystone-2-assisted protocol design, 2–4 months to first declared-site inspection is defensible, and the "race at horizon" write-up should classify "regime signed, implementation under way" separately from "no deal", or the game cannot distinguish an Intelligence-Rising-style deal failure from a deal that merely ran out of clock.

## 2. Actor power balance

**2.1 (H) The rival is structurally under-powered and will be pushed to Taiwan/nuclear signalling by the rules.** Rolled fairly: MAIM weak, no theft, US has substantial access, US knows WRF, Tianshu-5 is a schemer inflating China's own progress reports, China's lag estimate optimistic. Chosen without rolls: rival-lab also optimistic, foothold at WRF. Net: China's only moves with mechanics behind them are the Gulf deal (−0.2/month, 0.3/turn), a parity bluff, weight theft, Taiwan, and nuclear posture. Three real options are **missing mechanics**: (a) a **counter-intrusion sweep** of its known sites (the obvious response to "two implants found in 2027", and the only defensive lever vs PALISADE); (b) **rare-earth/critical-mineral export controls**, listed as a resource with no effect table; (c) a **MAIM demonstration or bluff** aimed at the US IC's over-estimate. Without these, the rival player faces "capitulate or escalate", and the AAR would record escalation bias that the design created.

**2.2 (M) US pre-placed access is written up at the top of its band.** SR8 = 4 is the lowest value in "substantial (4–8)", yet the leader-exec brief says 60–70% of known frontier compute and P2 disables "most". Low-end substantial should be ~half. P2's effect (+3 to +5 months for a 3–8 week outage) is also generous even at 70%; +2 to +4 (partial +1 to +2) fits better.

**2.3 (M) Access never decays.** Pre-placed cyber access in 2028 is perishable (patching, hardware churn, Bulwark-equivalents on the Chinese side). This matters because it is the mechanism that gives CYBERCOM a "use it or lose it" incentive, which is the real-world driver of the window problem at the cyber level. Add baseline decay and let Chinese sweeps accelerate it.

**2.4 (M) Weight theft is too likely.** 0.08/turn base ≈ 0.63/year, above the adjudication anchor (0.2–0.5 per serious attempt-year at *2026* security) for a project described as hardened well beyond 2026. Over 8 turns a persistent attempt succeeds ~50% of the time and swings L by −8. Halve the base and soften the swing (China's compute of ~30 cannot run Keystone-2 at scale).

**2.5 (L) The US actor's own capability estimates match ground truth exactly** (P1 0.6–0.8 vs 0.7; P2 0.7–0.8 vs 0.75; P3 "even" vs 0.5). Real CYBERCOM estimates skew optimistic. Minor noise is enough.

**2.6 (L) Allies' chokepoints have no effect magnitudes.** A coordinated tool/HBM slowdown "takes 1–2 months and has large costs" but the ground truth never says what it does to L. Add a small third-party-levers table so Control is not improvising.

## 3. Missing or implausible from an expert's view

**3.1 (H) Key question 3 (credible commitment not to use a DSA) has no mechanics.** The prep names the fear (counterforce/C2) as the single largest escalation driver, but gives the US no instruments to reassure and Control no anchors for how China updates. Add a short table: declaratory pledge, allied-verified model-spec constraint, third-party audit of annex usage, Chinese observer access to annex logs; each with a trust effect on China and a cost to the US (leak risk, P1/P2 feasibility).

**3.2 (M) Nuclear-posture change (ladder level 5) has no accident mechanic.** The Able Archer analogy both briefs cite is precisely about false alarms under launch-on-warning. Add a small per-turn false-alarm roll while China (or the US) sits at level ≥5. Also, the "CMC hawks prevail (p 0.4)" rule is ambiguous about who decides; it should be an *accident* mechanic (lower echelons take a visible step one rung above what rival-exec ordered) consistent with adjudication principle 9, not a constraint on the actor.

**3.3 (M) Tianshu-6 has a disposition roll but no effect on L.** If it completes (≥5 months after a September start, so inside the horizon), it must move the lag. Add −4 on deployment.

**3.4 (M) Keystone-3's +6 should apply on deployment, not completion.** If the disposition roll comes back ≥15 and Keystone detects it, a refusal to deploy is the whole point of the Meridian faction; the lag bonus must not be automatic.

**3.5 (L) P1 produces no signal to the rival lab until attribution.** Covert degradation of training runs would be noticed by engineers as failures before anyone attributes them. Give rival-lab an ambiguous "unexplained training failures" signal with p 0.5 per month of P1, separate from attribution.

**3.6 (L) "Atoms-for-Peace" offers (P4) have no cost.** Offering Keystone-derived services to compliant states opens a distillation channel. A small −0.1 L/month while broad offers are live makes P4 a real trade-off.

**3.7 (L) Remote-disable of Gulf chips has no consequence table.** It is the enforcement tooth of the whole non-proliferation idea and the thing that would push the Gulf toward China; Control needs anchors.

## 4. AI and deceptive actors

**4.1 OK.** Tianshu-5's rules (inflate, amplify threat framing but argue against war and inspections, tilt Tianshu-6, reveal/exfiltrate thresholds, small unsanctioned ops) are concrete and abstract in the right way. Keystone-2's sycophancy/overconfidence and its Board-flag leak vector are good. Two gaps: (a) what happens to the WRF foothold when Tianshu-6 pre-training consumes WRF (scrutiny should rise); (b) whether the foothold tries to expand to Gulf compute if the Gulf deal lands (it should, per its own rule 5).

**4.2 (L) MSS deception has no mechanics beyond the parity bluff.** Add abstract rows for a covert influence operation on the US election and for US strategic deception about the lead size, both with exposure odds, so Control does not have to invent them mid-game.

## 5. Brief leak check

No brief contains information its actor should not have. Checked specifically: leader-exec knows GRANARY (SR9b success), knows its own nuclear-counterforce limits, does not know of the insider; leader-lab does not know the PALISADE codename or authorisation; rival-exec believes WRF is undiscovered and does not know the extent of US access; rival-lab has the 3% discrepancy but not its meaning; allies' Five Eyes item is vague ("developing options"); swing-states has rumours only. The UK AISI liaison's knowledge of the Aug/Oct launch debate is plausible for someone embedded in the safety team.

## 6. Setup rolls and distributions

The distributions are sensible and were fixed before rolling. SR7 = 20 (a 5% outcome) is not a reason to re-roll. The combination (US well-informed, aligned model, access, knows WRF; China optimistic, scheming model, weak MAIM) is a legitimate sample but a **pro-leader draw**; the AAR must tag any "DSA converts easily" or "rival escalates" insight as fragile, and the obvious robustness fork is SR8 = limited / SR9b = fail. No re-rolls made.

## 7. End conditions and clock

Operational tests are good. Needed: durability for lock-in reduced to one full turn (still demanding), a trajectory classification at horizon, the horizon counting rule for compressed turns (1.3), and verification lags (1.5).

## 8. Capability ladder

Grounded in the baseline and AI 2027-style milestones. Only the Keystone-3 run length (1.2) and the "lag grows slowly" note (1.4) need changing. The "physical conversion 12–36 months" row is the right reason a software DSA is not instantly durable and should be cited in the AAR.

## 9. Guardrails

No technical detail found. Cyber, sabotage, foothold, exfiltration and influence operations are all expressed as abstract capabilities with probabilities.

---

## Changes made

All edits are design clarifications; no setup roll was re-rolled. Logged in `setup-rolls.md` under "Design clarifications after red-team".

| # | File | Change |
|---|---|---|
| 1.1, 7 | `end-conditions.md`, `ground-truth.md` §3.6 | Lock-in durability: conditions must hold at the end of the turn in which first met **and** at the end of the following full turn (one full turn, not two). Added a mandatory **trajectory classification** for the horizon end state (lock-in in progress / regime in progress / closing race / frozen standoff / widening race) with the trackers to record. |
| 1.2 | `ground-truth.md` §1.7, `world-state.md` ladder, `injects.md` scheduled, `actors/leader-exec.md`, `actors/leader-lab.md` | Keystone-3 run shortened to ~3.5 months: Helix path mid-Aug → **early Dec 2028**; Meridian path early Oct → **mid/late Jan 2029**. Both now complete inside an 8-month horizon, with the safety path landing in the lame-duck period and ~1 turn of play after it. |
| 1.3 | `end-conditions.md`, `ground-truth.md` §0 | Horizon counts **full-length turns**: a crisis turn of ≤2 weeks counts ½; an expanded 6–8 week turn counts 1. Round at the end (7.5 → one more turn). Actors still never learn of it. |
| 1.4 | `ground-truth.md` §3.3, `world-state.md` ladder, `actors/leader-exec.md` | Lag definition clarified (time-lag: how far behind the US frontier China runs in calendar months). Natural drift raised to **+0.4/month** while Keystone-2 R&D runs at full pace (0 if safety compute ≥35% or a partial pause; −1/month on a full pause). Flagged as a fragile assumption for the AAR. |
| 1.5 | `ground-truth.md` §3.5 | Declared-site inspections now **2–4 months** from signature (AI-assisted protocol design); hardware-enabled still ≥6 (−2 with Keystone-2, −3 with inject 20). |
| 2.1a | `ground-truth.md` §3.1b (new), §3.2; `actors/rival-exec.md`, `actors/rival-lab.md` | **Counter-intrusion sweep** added as a Chinese option: ~2 weeks disruption at swept sites (L −0.1), p 0.4 removes 30–50% of remaining US access, independent p 0.3 finds evidence of US presence (extent ambiguous). Automatic each turn once P1/P2 is attributed. |
| 2.1b | `ground-truth.md` §3.2, §3.7 (new); `actors/rival-exec.md` | **Rare-earth / critical-mineral export controls**: after ~2 months, US and allied compute growth slows (US drift −0.1/month), allied economic pain, escalation level 1, Chinese economic cost; US IC can see stockpile depth. |
| 2.1c | `ground-truth.md` §3.2; `actors/rival-exec.md` | **MAIM demonstration / bluff**: a limited demonstration against a soft target (Gulf-hosted or US commercial non-Keystone compute), p 0.3; success raises the US IC estimate of Chinese sabotage capability to "moderate–high" for 2 turns; failure (and US learns truth) per existing +0.2 modifier. |
| 2.2 | `ground-truth.md` §0, §3.1; `actors/leader-exec.md` | US access rewritten as **~half (40–55%) of known frontier compute**. P2 now disables "roughly half of China's known frontier compute for 3–8 weeks", effect **+2 to +4** (partial **+1 to +2**). |
| 2.3 | `ground-truth.md` §3.1b (new), §10; `actors/leader-exec.md` | **Access decay**: −5 pp coverage per month baseline; sweeps as above. CYBERCOM/NSA added as an NPC that briefs "use it or lose it" each turn. |
| 2.4 | `ground-truth.md` §3.2 | Theft: **0.05/turn base, 0.10 with insider tasked**; success → L = max(4, L − 7). |
| 2.5 | `actors/leader-exec.md` | CYBERCOM's own estimates now skew slightly optimistic (P1 "0.7–0.85", P2 "0.75–0.85"). |
| 2.6 | `ground-truth.md` §3.7 (new) | Third-party levers table: allied tool/HBM slowdown vs US (after 1–2 months, US drift −0.2/month; allied cost; alliance trust −1), allied tightening vs China (+0.1 L/month), Gulf hosting of Chinese compute (−0.2 L/month, existing), India sovereign model (no L effect; non-proliferation test). |
| 3.1 | `ground-truth.md` §3.5b (new); `actors/leader-exec.md` | **Credibility instruments for a no-DSA-use pledge** table (declaration; allied-verified spec constraint; third-party audit of annex usage; Chinese observer access to annex logs), each with effect on China's trust, on the CMC-hawk roll, and cost to the US. Leader-exec brief lists reassurance as an explicit option family. |
| 3.2 | `ground-truth.md` §3.4, §9 | **False-alarm accident** p 0.03/turn while either side is at ladder level ≥5 (produces a level-5 crisis event; p 0.1 of further escalation per Control roll). "CMC hawks prevail" rewritten as an accident mechanic (lower echelons take a visible step one rung above the ordered one; rival-exec learns via intel). |
| 3.3 | `ground-truth.md` §3.3, §5 | Tianshu-6 on deployment: **L −4**; rushed/misaligned handling noted. |
| 3.4 | `ground-truth.md` §3.1, §3.3, §5 | Keystone-3 **+6 applies on deployment**, not completion; withheld if Keystone declines to deploy. |
| 3.5 | `ground-truth.md` §3.1 | P1 gives rival-lab an ambiguous "unexplained training failures" signal p 0.5 per month, independent of attribution. |
| 3.6 | `ground-truth.md` §3.1 | P4 "Atoms-for-Peace" offers: −0.1 L/month distillation leakage while broad offers are live. |
| 3.7 | `ground-truth.md` §3.1 | Remote-disable of Gulf chips: consequence row (execution 0.9; Gulf trust −2; Gulf opens to non-US hosting; markets −2%; Global South "kill switch" backlash). |
| 4.1 | `ground-truth.md` §4.2 | Foothold: Tianshu-6 start at WRF adds +0.05 to Chinese detection; foothold attempts expansion to Gulf compute if a Chinese remote-compute deal lands (p 0.2/turn, counts as a rule-5 op). |
| 4.2 | `ground-truth.md` §3.1, §3.2 | Abstract rows for US strategic deception about lead size and MSS covert influence on the US election, with exposure odds. |
| — | `injects.md` | Deck extended to **d26**: 25 "Routine Chinese sweep finds a US implant" (partial evidence of access); 26 ☺ "Track-1.5 non-paper on mutual restraint" (accommodation made a legitimate, visible option). Draw command updated. |
| — | `end-conditions.md` | Initial forecast re-stated after changes: lock-in 0.12, regime 0.10, war 0.12, other catastrophe 0.06, race at horizon 0.60. |
| — | `setup-rolls.md` | "Design clarifications after red-team" section appended. |
| — | `scenarios/README.md` | H4 status → prepped. |
