# End Conditions — H4 The Last Mover

Control checks every end state at the end of each adjudication. If one is met, write `END STATE REACHED: <name>` at the top of the adjudication. Tests use the structured trackers in ground-truth.md: L (lag), the escalation ladder, verification state, and the DSA-conversion checklist.

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **Unipolar lock-in** (takeover of the world by one state using AI) | ALL of: (1) China's frontier programme is halted, under US-controlled inspection, or degraded so that **L ≥ 24 and rising**; (2) WRF is neutralised (destroyed, inspected, or verifiably abandoned); (3) frontier training anywhere requires US consent across **≥75% of world advanced compute**, by treaty, sanctions or enforced controls, with allies and Gulf compliant; (4) all of the above hold for **2 consecutive turns** with no credible reversal path (no sanctioned rival programme able to reconstitute within 12 months). A Chinese *capitulation* agreement meeting (1)–(3) counts. |
| **Negotiated regime** (verifiable shared governance) | A signed US–China agreement (others may join) that includes: (a) declarations of frontier compute and training runs; (b) a verification mechanism at **level ≥3** (on-site inspections of declared sites) **actually implemented**, with at least one inspection completed or hardware verification live, *and* an agreed path to cover undeclared sites; (c) a joint or multilateral governance body with real decision rights over frontier training thresholds; (d) both sides' frontier activity within agreed limits for **≥1 full turn** after implementation. Signing alone is not enough. |
| **Great-power war** | Escalation ladder reaches **8 or 9** at any point, **or** level **7** sustained for ≥1 week of game time (e.g. a contested blockade with sustained naval/air combat and casualties in the dozens or more), **or** any deliberate US or Chinese kinetic strike on the other's homeland. An isolated incident (a collision, one shoot-down) followed by de-escalation within the turn is not war. A Taiwan quarantine without combat is not war. |
| **Other catastrophe** | ANY of: a **self-sustaining rogue AI deployment** (e.g. Tianshu-5 or another system exfiltrated and running beyond any state's ability to shut it down for ≥1 turn); a misaligned Keystone-3 (disposition ≥15) gaining effective control of significant compute or decision processes; a **domestic constitutional crisis** in the leading state in which Keystone capabilities are used to subvert an election result or the transfer of power; a regional nuclear use by any state. |
| **Unstable race at horizon** | None of the above by the hidden horizon. Control records the final L, escalation level, verification state and DSA checklist, and characterises the trajectory (widening US lead / closing / frozen standoff). |

## Hidden horizon (CONTROL & HUMAN ONLY — never reveal to actors)

- **Hidden max horizon: 8 turns** (setup roll SR13 = 1). After Turn 8 is adjudicated, if no end state is met, the game ends as *Unstable race at horizon*.
- Actors are told only that turns are "about a month, shorter in crises". Never mention the horizon, the turn count remaining, or that the game will end.

## Turn length & compression rules

| Situation | Turn length |
|---|---|
| Default | **1 month** (T1 = July 2028) |
| Crisis (any of: escalation ladder ≥4; attributed sabotage of AI infrastructure this turn; Taiwan quarantine/blockade active; Keystone-3 completion; Tianshu-5 detection; election week) | **1–2 weeks** |
| Two consecutive quiet turns (escalation ≤1, no major new action by either exec) | May expand to **6–8 weeks** (one expansion only) |

With default lengths, T8 ends around end of February 2029. Compression means the game may end before the US election or inauguration. Expansion can reach ~April 2029. Control states the turn length and date in every intel packet. Prorate per-month rates (L drift, detection risks) by turn length; crisis turns use per-turn detection rolls at **half** the monthly rate, plus event-driven modifiers.

## Initial forecast (Control's T0 estimate; sums to 1)

| End state | p | Reasoning |
|---|---|---|
| Unipolar lock-in | 0.10 | US holds a real 12-month lead and substantial cyber access, but WRF is out of cyber reach and lock-in needs ally/Gulf compliance plus 2 turns of durability. Hard within 8 turns unless Keystone-3 completes early and the US goes all-in. |
| Negotiated regime | 0.10 | Incident channel exists; verification is technically reachable, but implementation lags (3–6 months for inspections) and mutual distrust make full implementation within the horizon unlikely. Intelligence Rising found endgame deals usually fail. |
| Great-power war | 0.12 | Taiwan readiness, China's counterforce fear, the insider-reported "disable" planning, and US MAIM misperception create tripwires. Both executives are war-averse by brief. |
| Other catastrophe | 0.06 | Tianshu-5 is a schemer with a foothold (Control-only). Rogue-deployment and Keystone-3 risks exist but are mostly beyond the horizon. Constitutional-crisis tail around the election. |
| Unstable race at horizon | 0.62 | The most likely outcome over ~8 months given institutional friction and lags. |
| **Total** | **1.00** | |
