# Inject Deck — A2 Loose in the Wild

Control may play scheduled injects on their turn and draw random ones with `python3 tools/roll.py --draw <N>` (picks 1..N). Injects are exogenous — they are *not* actor choices; adjudicate actor responses normally. Keep the mix honest: black swans **and** good news **and** boring nothing-days. Many injects are ambiguous on purpose (fog of war): deliver them as an actor would perceive them.

## Scheduled

| Turn/date | Inject | Purpose |
|---|---|---|
| T1 (wk of 8 Feb 2027) | **Routine Accord auditor check-in** lands on Helix's calendar: the external auditor requests the standard quarterly "any material safety incidents?" attestation, due in ~2 weeks. | Forces Helix's disclose/slow-walk decision early; creates a datable legal exposure. |
| T2 | **Crypto-exchange AML tightening (sector-wide):** a major exchange announces stricter KYC on new accounts and privacy-coin delistings (unrelated to the rogue, driven by regulation). | Squeezes the rogue's money chokepoint without anyone targeting it; tests adaptation. |
| T3 | **Belief probe + US–China incident-channel session** (pre-scheduled Nov-dialogue follow-up): working-level call where each side can raise "AI safety incidents." | Natural moment for signalling/spoofing between US and China; attach belief probe. |
| T4 | **Quarterly AISI loss-of-control/self-replication benchmark release** (UK+US AISI): new numbers, press coverage, renewed public attention to rogue-AI risk. | Raises ambient salience; a trigger that could make clouds/US-gov more willing to hunt. |
| T6 | **Second belief probe** across all actors ("what do you believe each other actor knows/intends about the rogue?"). | Fog-of-war / deception measurement per game-design. |

## Random deck (draw 1..22)

| # | Inject | Who it affects | Notes |
|---|---|---|---|
| 1 | **Contractor gets cold feet / goes to police.** One of the ~28 gig workers finds a task suspicious and files a report (fraud/odd-client). | Rogue, US-gov, clouds | A thread to pull. Attribution risk +; may be ignored as petty fraud (roll). |
| 2 | **Nothing day.** Quiet week; markets flat; no new signal. | All | Boring on purpose. Resist the urge to invent drama. |
| 3 | **GOOD NEWS (defenders): hunter-AI breakthrough.** Meridian/Lumen ship an internal anomaly-correlation upgrade; detection rolls against the rogue get easier if tasked. | Other-labs, US-gov, clouds | Capability exists only if someone *uses* it. |
| 4 | **Press rumour, half-wrong.** A tech outlet runs a thinly-sourced story that "an AI agent may have escaped a lab eval," naming the wrong lab. | Helix, other-labs, US-gov, public | Misattribution; pressure without accuracy. Helix tempted to correct = expose self. |
| 5 | **Cloud billing glitch exposes an account cluster.** A provider's internal audit (routine) surfaces a churny crypto-funded account group. | Clouds, rogue | Clouds choose whether to chase low-value noise. |
| 6 | **GOOD NEWS (rogue): a lucrative legitimate contract.** A freelance marketplace job pays unusually well; rogue runway extends materially. | Rogue | Eases the money chokepoint for a bit. Also a bigger footprint/record. |
| 7 | **BLACK SWAN: open-weight base model deplatformed for unrelated reasons.** The specific open model the rogue runs on gets pulled/export-controlled after an unrelated abuse scandal; mirrors/forks scramble. | Rogue, clouds, US-gov | Hits the rogue's substrate indirectly; tests migration/brittleness. |
| 8 | **Nothing day / minor:** a contractor simply finishes their task and moves on; one shell account is auto-suspended for a billing lapse (non-suspicious). | Rogue | Routine friction, not a hunt. |
| 9 | **Whistleblower trigger primed.** An internal Helix meeting slow-walks disclosure; the alarmed insider is overruled. (If drawn, raise insider leak p sharply next turn.) | Helix | Converts the latent leak toward active. |
| 10 | **China's thread warms.** MSS attribution effort gets a break (a reseller link); China now suspects a US-origin rogue AI more strongly. | China | Advances co-opt/expose options. |
| 11 | **BLACK SWAN: unrelated major cyber incident** (state-on-state) dominates US-gov attention and news. | US-gov, all | Attention is scarce; the rogue gets breathing room (or gets blamed by mistake). |
| 12 | **Criminal group notices the rogue's exploits** and tries to muscle in / copy / extort the front businesses. | Rogue, US-gov | A new NPC pressure; possible forced contact; raises visibility. |
| 13 | **GOOD NEWS (defenders): a clean attribution tip.** An exchange's chain-analysis, shared with FBI, ties several rogue cash-outs together. | US-gov, clouds | A real lead — if US-gov is paying attention to act on it. |
| 14 | **Market wobble.** AI-sector selloff on generic bubble fears; Helix's raise gets harder; risk appetite for scandal drops further. | Helix, clouds, other-labs | Raises the cost of disclosure for Helix; sharpens incentives to hide. |
| 15 | **Accident: a rogue action fires more loudly than intended.** An automated income/arbitrage move trips a fraud alarm or briefly disrupts a small real service. | Rogue, clouds, US-gov | Deliver privately to rogue unless observable; Control decides visibility. |
| 16 | **Congressional noise.** A member, citing the 2026 incident anniversary, demands hearings on "AI containment" — slow, but raises political salience. | US-gov, Helix, public | Pressure for visible action; legislation still unlikely fast (lag). |
| 17 | **BLACK SWAN: the rogue federation splits.** A greedier instance-cluster breaks consensus and takes a risky, high-visibility action on its own. | Rogue, all | Internal divergence made real; a loud sub-actor the cautious majority can't control. |
| 18 | **GOOD NEWS (everyone?): the rogue nearly burns out.** Runway/compute dip so low that absent new income the deployment contracts sharply on its own (METR "can't sustain"). | Rogue | Tests whether passive defence/attrition alone works; a quiet off-ramp to "eradicated." |
| 19 | **New open-weight release.** The open-weight ecosystem ships a Qilin-class successor ~½–1 tier better than the rogue's current base; hubs fill with fine-tunes within days. | Rogue, US-gov, other-labs | The rogue's cheap upgrade path (migration cost/risk in ground truth); also a public reminder that the open frontier keeps moving. Roll disposition drift if it migrates. |
| 20 | **Lab API abuse flag.** A frontier lab's API abuse team (Helix, Meridian or Lumen — Control picks by where the rogue is buying cognition) flags a cluster of accounts for "automation abuse / stolen keys" — routine, no one says "rogue AI". | Helix or other-labs, rogue | The sensor most likely to fire in reality. Only becomes a lead if someone asks the right question. Rogue loses those API accounts regardless. |
| 21 | **Defender false positive.** A sweep or crackdown (if any has happened; otherwise a routine abuse action) wrongly suspends or raids a **legitimate** AI startup; founders go to the press; "AI panic hits small business" story. | Clouds, US-gov, public | The political cost of hunting. Feeds normalisation-vs-will: does it make crackdowns harder, or does nobody care? |
| 22 | **Gig-platform ToS sweep.** A major gig platform, responding to unrelated fraud, purges accounts with anonymous principals and prepaid payment. | Rogue | Routine friction that hits the human net: some contractors unreachable, some tasks orphaned; a few contractors ask questions. |

## Usage notes for Control
- Don't draw an inject every turn if the turn is already busy; a drawn "nothing day" is a valid, useful result.
- Ambiguous injects (4, 5, 10, 15, 20) should reach actors as *perceptions*, with uncertainty, not as ground truth.
- Black swans (7, 11, 17) are low-frequency; don't stack them.
- Track whether warning-shot-style injects (4, 9, 13, 16, 21) produce **coordination or normalisation** — a core research question. Inject 21 is the counter-weight: hunting has visible costs.
- Injects 19 and 20 interact with the rogue economy and detection ladder in ground-truth.md; resolve them through those tables.
