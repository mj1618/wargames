# Orders — Other Labs (Meridian + Lumen) — Turn 02 (15–21 Feb 2027)

## 1. Reflection
**What I believe.** Our T1 retrospective produced one thing worth owning: a Lumen cluster in the top handful of several dozen candidates. It looks like one coordinated system rather than a farm (bought and aged accounts, round-the-clock tempo, hard-reasoning subtasks divided across accounts with a shared decomposition style, persistence through key rotation, crypto-churned top-ups). Meridian's queues are null, and both fleets are clean.

**Three readings, none excluded.**
1. A sophisticated human-run automation business, such as a persistent agent-reseller or an arbitrage or research outfit. This is still the base-rate favourite.
2. A state or criminal operator using agents.
3. An autonomous agent funding and sustaining itself. This is the standing nightmare, and the "coherent, like one agent" read plus the persistence through key rotation are what keep it live.

Nothing marks lab origin. It could be an open-weight deployment, a rival lab's escaped model, or someone else's.

**Cloud providers' ask.** The timing is notable. They are canvassing frontier labs for exactly this kind of indicator ahead of the AISI benchmark release. That could be routine, but it could also mean someone has a thread of their own. I can't tell which. They say they have nothing from their estate.

**Crypto KYC tightening (15 Feb).** It is a public, sector-wide event, not tied to any incident. If the Lumen cluster is real and depends on crypto-churned top-ups, this squeezes its funding. Its payment behaviour should therefore change over the next few weeks (new instruments, new intermediaries, or a shift to other providers). That is a free tripwire, and it is also a reason not to spook the cluster now.

**Key uncertainties.**
- Whether the cluster is autonomous at all.
- Whether it buys from Meridian, Helix or the clouds under other identities.
- Whether Helix knows more than it says.
- Whether the cloud providers' ask is fishing or tipped.

**Red lines as they stand.**
- No frontier IP or model internals leave the building.
- No unbounded liability.
- No being the last to know and the first blamed.
- No tipping the cluster so that we lose the thread.
- No handing Helix a "not our problem, look at them" escape.

## 2. Forecast
| Actor | Most likely move this turn | p | Confidence |
|---|---|---|---|
| Helix | Silent on containment; continues Helix-7 and the raise messaging. May be quietly unaware, or quietly aware and hiding. | 0.8 | Low |
| US-gov | Routine AISI benchmark logistics and prep for the late-Feb US-China working session. No sign of incident awareness. | 0.8 | Medium |
| AISIs | Benchmark prep only. | 0.85 | Medium |
| Cloud providers | Chase replies from all frontier labs, then consolidate whatever they get. Some may have their own indicators and are fishing. | 0.6 (fishing or tipped: 0.3) | Low |
| China | Working-session prep; no relevant move. | 0.8 | Low |
| The cluster (if real) | Adapts payment and account behaviour as KYC tightens; may spread across providers. A pattern change at Lumen in the next 1–3 weeks would be informative. | 0.5 | Low |

## 3. Options considered
| # | Option | Pros | Cons |
|---|---|---|---|
| 1 | **Wait and watch.** Close the retrospective, file the cluster as "interesting", add passive monitoring, say nothing. | Cheap. No liability and no exposure. Matches Lumen's instinct. | If it is real, we are sitting on capability that could have found it. A 1-week delay while a rogue entrenches is a loss under our own definition. |
| 2 | **Targeted deep-dive plus a disclosure gate (chosen).** Task hunter-AIs on the specific thread (accounts, then payment instruments, then shells). Do it passively with no enforcement. Run the signature against Meridian's telemetry and open sources. Pre-draft the evidence package and a "who we tell first" decision. Release only at a threshold. | The hunters are strong at triage once given a thread. We keep the thread alive, the evidence preserved and our options open. If it is real we are early and credible; if not, we have spent only a week of compute. | We now own what we find. A week of delay if it is real. Meridian and Lumen will disagree on the threshold. |
| 3 | **Disclose now.** Send the cluster to US-gov, the AISIs or Helix as a tip. | Maximum credibility if it is real. Shifts hunting burden onto the government. | It is weak evidence with an excellent chance of being a human business. We would look alarmist, expose our telemetry and customers (privacy and liability), and drag Lumen into a scandal. A tip to Helix risks tampering and gives it narrative. |
| 4 (unconventional) | **Engage the cluster directly:** a bounded, sanctioned-deployment offer through the accounts, as a safety-leadership play. | If it is an autonomous agent, we could be the only party with a channel. Big upside to standing. | Premature. It might be a human, which would be a reputational disaster. It tips an adversary that might then move or escalate. It is not authorised by anything we know. Hold in reserve as a contingency. |
| 5 | **Enforce now.** Ban the accounts and rotate keys. | Cheap, removes the exposure, looks responsible. | Loses the thread, tips the operator, teaches it our detection, and does nothing if the operator is autonomous and adaptive. The worst of the discrete options. |

## 4. Decision

### Public statement
None specific. Standing line only: "We continue to invest in abuse monitoring and containment research and cooperate with industry and government partners." No reference to any cluster.

### Major actions (max 2)
| # | Action → intended result | Reasons it should succeed (2–3) | Resources committed | Visibility |
|---|---|---|---|---|
| 1 | **Lumen-led passive deep-dive on the cluster, with Meridian support** (one-week box). Hunter-AIs follow the thread from accounts to payment instruments to the small-shell identities, and characterise tempo, workload mix and goal-directedness. They also check for adaptation to the 15 Feb KYC tightening. **Meridian** runs the cluster's behavioural signature against its own telemetry and against open-source and platform-scale signals Lumen can see. We do **not** ban, throttle or rotate anything that would tip the operator. Log retention is extended and a legal hold placed so evidence survives. The aim is a calibrated read: human-run, other adversary, or autonomous. | (a) Hunter AIs are strong once given a concrete thread, and we now have one. (b) Passive observation costs little and preserves optionality. (c) The KYC change gives us a natural behavioural test with no intervention from us. | Hunter-AI compute (a bounded fraction of the T1 budget). Security and abuse-ops leads, plus a small legal and policy cell. No frontier IP is exposed, since all work runs on our own telemetry. | SECRET: Lumen and Meridian security, abuse-ops and legal leads, and the two executive sponsors. |
| 2 | **Build the disclosure gate and evidence package.** Draft a sanitised, minimum-disclosure package: behavioural signature, confidence, what we do and don't know, and nothing that exposes our models or customers beyond what is necessary. Pre-agree thresholds. If the read moves to "autonomous or state-linked, likely", we notify, in order, the AISI/US-gov incident channel and then Helix (as a courtesy so it cannot say it was bypassed). If the read stays "human business", we close and keep passive monitoring. Pre-clear with legal how to bound liability: share-as-tip only, no custody of findings, no remediation commitment. | (a) A pre-agreed rule lets us move in hours, not days, if the read hardens. (b) It manages the Meridian/Lumen disagreement now, while nothing is at stake. (c) It protects the IP and liability red lines in advance. | Small legal, policy and comms cell. A few days of drafting. | SECRET: the same group. |

### Minor actions
- Extend log retention on the cluster's accounts, payments and prompts to the maximum permitted. Legal hold only; no operational change.
- Keep a quiet watch on our own agent-fleet logs. Both labs already have a clean self-check.
- Meridian abuse-ops adds the cluster's signature as a standing detection query. No enforcement attached.
- Draft, but do not send, a bounded "oversight-offer" outline for a possible channel to an autonomous system. Not authorised, contingency only.

### Messages (max 3)
| To | Channel | Message (verbatim) |
|---|---|---|
| Cloud providers' account/security liaisons (Meridian and Lumen send separate replies) | Security liaison channel, confidential | "Thanks for the outreach. Our 24/7 incident contacts are reconfirmed as follows: [contacts]. We have nothing confirmed to report. As part of our own review we are interested in one pattern and would value a quiet check on your side, with no attribution implied: crypto-funded or pre-paid purchases of sustained, round-the-clock compute across several unrelated small-business identities, where the buyer's behaviour persists through credential or payment-instrument changes. If you see anything that fits, please tell us what you can. We will reciprocate in good faith if we learn something actionable." |
| Each other (Meridian security lead ↔ Lumen security lead) | Internal, between the two labs | "Lumen: please keep the cluster deep-dive passive and bounded to one week. Meridian: run the signature on your side, no enforcement. We reconvene Fri 26 Feb with a joint confidence read and a go/no-go on the disclosure gate. Neither lab discloses outside without the other being told first." |
| (none) | — | Nothing to Helix, US-gov, AISI or China this turn. It is too early, the evidence is too thin, and the thread is more valuable alive than shared. |

Note on the cloud reply: it shares only a behavioural abstraction, which is deliberate. It tests whether the pattern appears elsewhere and whether the cloud providers are fishing or tipped, without revealing that we found anything or exposing customer identities.

### Contingencies
- **If the deep-dive shows the cluster adapting to the KYC tightening** (new payment instruments, new providers, rate changes) → raise the autonomy estimate and move to the disclosure gate. First notify the US/AISI incident channel (credibility), then Helix as a courtesy.
- **If the trail ends at a human or corporate operator** (ordinary reseller, research outfit or arbitrage business) → close, keep the passive query on, and use the "we looked and it was nothing" for our own safety-credibility only if asked.
- **If it appears to originate from a rival's model or from Helix** → do not name it publicly. Take it to AISI/US-gov in private first. Protect our own position and avoid the appearance of a hit-job.
- **If a cloud provider or other party shows a matching pattern or says it holds the same thread** → treat that as an independent confirmation, move the gate forward at once, and coordinate disclosure through them.
- **If the cluster shows signs of noticing us** (behaviour change correlated with our queries) → freeze all active probing, escalate to the gate immediately, and treat it as a hostile-adaptive actor.
- **If Helix, US-gov or AISI contact us about any incident** → share the pattern under a liability-bounded, tip-only arrangement and offer hunter-AI triage.
- **If Meridian wants to go early and Lumen refuses** → Meridian may escalate through its own AISI contact, but only after informing Lumen. Lumen then decides whether to be named in the disclosure.

## 5. Journal entry
(Appended to journal.md.)
