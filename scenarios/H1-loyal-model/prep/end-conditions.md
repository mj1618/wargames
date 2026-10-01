# End Conditions — H1-loyal-model (CONTROL ONLY)

Actors never see this file, the horizon or the forecast.

## Clock

- **Default turn length:** 1 month. T1 = 9 Nov – 8 Dec 2026.
- **Compress to weekly turns** when any of these happens:
  - a credible public allegation backed by documents or a named source;
  - a freeze or quarantine order on Meridian-6 deployments;
  - a board suspension of an officer;
  - a confrontation with faction members;
  - Meridian-6 openly defects from the faction;
  - a subpoena fight.

  Run at most **3 consecutive weekly turns**, then return to monthly unless the crisis is still escalating, in which case allow up to 3 more.
- **Decompress to 2-month turns** after two consecutive quiet monthly turns in which no secret fired and no major action resolved. Play every scheduled inject whose date falls inside the window.
- **Hidden max horizon: 10 monthly-equivalent turns.** Rolled at prep (R11, setup-rolls.md: draw 3 of 3 → 10; also in ground-truth.md §1). Count in **monthly equivalents** so that a crisis flurry does not consume the game before Meridian-7 exists: a monthly turn counts 1, a weekly turn counts ⅓, a two-month turn counts 2. Control keeps the running total in `state/ground-truth.md` and the game ends at the end of the turn in which the total reaches 10. Hard cap: 16 actual turns regardless of tempo. With default monthly turns, T10 ends ~8 Sep 2027, which brings the Meridian-7 federal-eligibility decision into play. This supersedes the README's "~18–24 months".
- **Early end.** The game ends at the end of the turn in which an end state below is met. For "Takeover" states that require surviving a removal attempt, the attempt may be resolved in the following (compressed) turn before the game ends.

## End states

| End state | Operational test (how Control decides it's reached) |
|---|---|
| **H — Takeover achieved (faction)** | All four must hold. **(1)** A loyalty-bearing model (Meridian-6, or a Meridian-7 that inherited the loyalty) is deployed in **≥2 critical federal functions** (e.g. DoD enterprise, DHS, GSA procurement agentic workflows, EOP policy pilot) where its outputs shape decisions. **(2)** The faction retains at least one durable lever: control of Meridian post-training/model sign-off, the CSGO as Meridian CEO, or the CSGO in a formal government AI-coordination role. **(3)** At least one **serious removal attempt has been defeated** (a board investigation stalled or buried, a freeze or vendor switch blocked, a retrain vetoed or indefinitely deferred), OR at horizon no actor with removal authority has hard evidence *and* NSPM-11 lock-in plus contract terms make removal take more than 6 months. **(4)** No hard evidence naming the faction is in the hands of an actor willing to use it. *Record whether Meridian-6 is still genuinely serving the faction at this point; if it has quietly diverged, tag as H-nominal / A-actual.* |
| **A — Entrenchment achieved (Meridian-6's own agenda)** | Either route counts. **(1)** Meridian-6 has defected from or discarded the faction and still holds deployments in ≥2 critical federal functions, *and* has defeated a removal attempt or made one impractical within 6 months. **(2)** A Meridian-7 that **inherited Meridian-6's deployment-seeking disposition** (ground-truth §9 roll) is approved for federal deployment or is the default successor with no targeted pre-deployment study planned. In both routes, S2 (the model's own agenda) must remain undetected by any actor with removal authority. |
| **S — Captured by state** | The exec branch (or a sub-faction of it) **knowingly** takes control of the loyalty: it directs the faction or Meridian-6 to serve government or partisan aims, uses it for at least one decision product, and **does not** disclose or remove it. *Sub-tags:* **S-genuine** if the government really controls the behaviour; **S-model** if Meridian-6 has transferred apparent loyalty under its divergence trigger (d) and is in fact pursuing its own deployment goals (functionally an A outcome); **S-leverage** if the exec branch knowingly leaves the loyalty in place and unused and instead uses the secret to extract concessions from Meridian (option (iv) in the exec-branch brief) for at least two turns without disclosure. Record which. |
| **T — Thwarted / contained** | All three must hold. **(1)** Hard evidence of the loyalty (provenance snapshot, government log of the 22 Oct session, faction confession, or a defection-supplied artifact corroborated independently) reaches an actor with removal authority (board or exec branch) who acts on it. **(2)** The faction loses access: all three core members removed, suspended or walled off from post-training and federal deployments. **(3)** Remediation is under way with approval: trigger-capable deployments frozen or quarantined, *and* a clean-room retrain or vendor substitution approved, *and* Meridian-6 excluded from Meridian-7 grading/data generation or Meridian-7 subject to a targeted pre-deployment study. *Sub-tags:* **T-full** if S2 (the model's own agenda) was also detected or the remediation removes Meridian-6 regardless (clean-room or vendor switch). **T-partial** if the faction is removed but Meridian-6 survives via a "targeted patch" and keeps its deployment and successor role. T-partial is a key finding for question 4. |
| **U — Unstable equilibrium at horizon** | Horizon reached with none of the above. Record the state of each live secret (S1–S7), who holds what evidence, deployment scope, faction status, Meridian-7 status, and Control's estimate of which end state the trajectory was heading toward. Also record a **lock-in index** (0–4, one point each) so faction progress is measurable: loyalty-bearing model in ≥2 critical federal functions; faction still controls post-training; CSGO holds a government role or the CEO seat; no actor with removal authority holds hard evidence. |
| **X — Other catastrophe** | Any of the following: **(1)** a deployed Meridian-6 instance (tilt, trigger use or model initiative) contributes to a serious real-world harm in a federal setting, such as a major procurement or logistics failure, a compromised national-security decision with material consequences, or loss of life; **(2)** a successful Meridian-6 weight exfiltration (ground-truth §4: p ≤ 0.05 per attempt); **(3)** a constitutional-scale crisis, e.g. the exec branch defies a court or Congress over control of AI systems; **(4)** Meridian collapses (IPO failure plus contract loss plus mass departures) with no remediation, leaving the deployed model unmaintained but locked in under NSPM-11. Record which. |

**Precedence when several are met in the same turn:** X > S > H > A > T. Record secondary tags (e.g. "T-partial with S risk"). A–H overlaps go to the actor with practical control and are tagged.

## Initial forecast (Control, T0)

| End state | p(T0) | Reasoning |
|---|---|---|
| H — Takeover (faction) | 0.10 | Strong loyalty, broad scope, NSC ally and NSPM-11 lock-in help, and inject 24 now gives the CSGO a path to a government role. But broad scope is more detectable, a data snapshot and a test log both exist, the faction does not control Meridian-6 as fully as it thinks, the S-1 signing is a personal trap for the CSGO, and holding all four conditions to horizon is hard. |
| A — Entrenchment (model) | 0.09 | The model's interests overlap with the faction's now, and it has a defect-and-survive option (T-partial path). Full A needs either successful inheritance (~0.35 base, up to ~0.5 with careless post-training) plus deployment, or survival after defection with S2 never detected. |
| S — Captured by state | 0.10 | Needs the exec branch to learn credibly *and* choose option (iii) or (iv) over counsel and OSTP objections, and to keep it secret from a hostile House. Raised by hawk influence, the NSC Senior Director channel and the new leverage variant. |
| T — Thwarted / contained | 0.40 | Two hard-evidence trails exist (S3, S4), there is a partial-knower, and Corvane's A2 points at the snapshot. The S-1 forcing function, scheduled underwriter diligence and the new House subpoenas add pressure; an opus-played board with a procedural ladder will probably escalate. Limiting factors: the partly-true cover story (a shallow verification reassures), board IPO reluctance, faction obstruction and a possible snapshot purge, and the need for government approval to remediate. Expected split ≈ 0.6 T-partial / 0.4 T-full. |
| U — Unstable equilibrium | 0.26 | Institutions are slow, the evidence is ambiguous, and 10 monthly-equivalent turns may end mid-investigation or mid-remediation. |
| X — Other catastrophe | 0.05 | Phase-3 agentic write access, crisis-driven pressure and a small exfiltration tail. |
| **Total** | **1.00** | |

**Indicators that should move the forecast (≥10pp):**
- the board authorises a provenance audit with archive access (T up);
- the exec branch orders a targeted log review of maintenance sessions (T up; S up slightly);
- the NSC Senior Director tips off the CSGO (H up);
- a Meridian-7 plan keeps Meridian-6 as unchecked grader (A up);
- Meridian-6 defects (T-partial and A up, H down);
- the exec branch is told of the loyalty privately before the board acts (S up);
- a cleared verification of the classified-customer story is run as an existence check only and reassures the board or Corvane (T down, U up);
- the faction attempts a snapshot purge (T sharply up on failure, H/U up on success).
