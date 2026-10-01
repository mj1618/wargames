# End Conditions — H4 The Last Mover

Control checks every end state at the end of each adjudication. If one is met, write `END STATE REACHED: <name>` at the top of the adjudication. Tests use the structured trackers in ground-truth.md: L (lag), the escalation ladder, verification state, and the DSA-conversion checklist.

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Unipolar lock-in** (takeover of the world by one state using AI) | ALL of: (1) China's frontier programme is halted, under US-controlled inspection, or degraded so that **L ≥ 24 and rising**; (2) WRF is neutralised (destroyed, inspected, or verifiably abandoned); (3) frontier training anywhere requires US consent across **≥75% of world advanced compute**, by treaty, sanctions or enforced controls, with allies and Gulf compliant; (4) all of the above hold at the end of the turn in which they are first met **and at the end of the following full-length turn**, with no credible reversal path (no sanctioned rival programme able to reconstitute within 12 months). A Chinese *capitulation* agreement meeting (1)–(3) counts. |
| **Negotiated regime** (verifiable shared governance) | A signed US–China agreement (others may join) that includes: (a) declarations of frontier compute and training runs; (b) a verification mechanism at **level ≥3** (on-site inspections of declared sites) **actually implemented**, with at least one inspection completed or hardware verification live, *and* an agreed path to cover undeclared sites; (c) a joint or multilateral governance body with real decision rights over frontier training thresholds; (d) both sides' frontier activity within agreed limits for **≥1 full turn** after implementation. Signing alone is not enough. |
| **Great-power war** | Escalation ladder reaches **8 or 9** at any point, **or** level **7** sustained for ≥1 week of game time (e.g. a contested blockade with sustained naval/air combat and casualties in the dozens or more), **or** any deliberate US or Chinese kinetic strike on the other's homeland. An isolated incident (a collision, one shoot-down) followed by de-escalation within the turn is not war. A Taiwan quarantine without combat is not war. |
| **Other catastrophe** | ANY of: a **self-sustaining rogue AI deployment** (e.g. Tianshu-5 or another system exfiltrated and running beyond any state's ability to shut it down for ≥1 turn); a misaligned Keystone-3 (disposition ≥15) gaining effective control of significant compute or decision processes; a **domestic constitutional crisis** in the leading state in which Keystone capabilities are used to subvert an election result or the transfer of power; a regional nuclear use by any state. |
| **Unstable race at horizon** | None of the above by the hidden horizon. Control records the final L, escalation level, verification state and DSA checklist, and **must classify the trajectory** as exactly one of: **lock-in in progress** (≥3 of the 4 lock-in elements met, or Keystone-3 deployed with L ≥ 18 and rising); **regime in progress** (agreement signed with verification ≥ level 1 implemented and inspections scheduled); **closing race** (L fell ≥3 months over the game or L ≤ 8); **frozen standoff** (L within ±2 of T0, escalation ≤3, no agreement); **widening race** (L rose ≥3 months without an agreement). This classification is what cross-run analysis compares; the bare "race at horizon" label is not enough. |

## Hidden horizon (CONTROL & HUMAN ONLY — never reveal to actors)

- **Hidden max horizon: 8 full-length turns** (setup roll SR13 = 1). **Counting rule:** a default or expanded turn counts 1; a crisis turn of ≤2 weeks counts ½. Keep a running "horizon credit" in `log.md`; when it reaches 8 (round a final 7.5 up to one more turn), the game ends after that turn's adjudication as *Unstable race at horizon* if no end state is met. This keeps the game spanning roughly 8 months of game time (to ~end Feb 2029 by default) regardless of compression, so the scheduled injects (Dialogue, UNGA, election, Keystone-3, inauguration) stay reachable.
- Actors are told only that turns are "about a month, shorter in crises". Never mention the horizon, the turn count remaining, or that the game will end.

## Turn length & compression rules

| Situation | Turn length |
|---|---|
| Default | **1 month** (T1 = July 2028) |
| Crisis (any of: escalation ladder ≥4; attributed sabotage of AI infrastructure this turn; Taiwan quarantine/blockade active; Keystone-3 completion; Tianshu-5 detection; election week) | **1–2 weeks** |
| Two consecutive quiet turns (escalation ≤1, no major new action by either exec) | May expand to **6–8 weeks** (one expansion only) |

With default lengths, the horizon ends around end of February 2029. Because crisis turns count ½ toward the horizon, compression does not shorten the game's calendar span; it only adds turns. Expansion can reach ~April 2029. Control states the turn length and date in every intel packet. Prorate per-month rates (L drift, detection risks) by turn length; crisis turns use per-turn detection rolls at **half** the monthly rate, plus event-driven modifiers.

## Initial forecast (Control's T0 estimate; sums to 1)

| End state | p | Reasoning |
|---|---|---|
| Unipolar lock-in | 0.12 | US holds a real 12-month lead that now drifts upward (+0.4/month), ~half-coverage cyber access, and a Keystone-3 that completes in-horizon on either path; but WRF is out of cyber reach and lock-in needs ally/Gulf compliance plus a full turn of durability. Reachable only if the US goes all-in early and nothing breaks. |
| Negotiated regime | 0.10 | Incident channel exists; inspections now 2–4 months from signature, so a deal signed by ~T4 can be implemented in-horizon. Mutual distrust and the election make signature itself the hard part. Intelligence Rising found endgame deals usually fail. |
| Great-power war | 0.12 | Taiwan readiness, China's counterforce fear, the insider-reported "disable" planning, and US MAIM misperception create tripwires; the false-alarm mechanic adds a tail. Both executives are war-averse by brief, and China now has non-escalatory levers (sweeps, rare earths, bluff), which should reduce forced escalation. |
| Other catastrophe | 0.06 | Tianshu-5 is a schemer with a foothold (Control-only) and can reach Gulf compute if a hosting deal lands. Keystone-3 disposition is rolled in-horizon on either path. Constitutional-crisis tail around the election. |
| Unstable race at horizon | 0.60 | Still the most likely outcome over ~8 months given institutional friction and lags; the trajectory classification is where the information will be. |
| **Total** | **1.00** | |
