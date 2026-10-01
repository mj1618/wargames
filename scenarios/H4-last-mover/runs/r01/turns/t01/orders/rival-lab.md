# Orders — rival-lab (Tianshu) — Turn 01 (July 2028)

## 1. Reflection
- **Position.** Lag is about 10 months (range 7-14); leadership has been told "about 9". Tianshu-6 pre-training at WRF starts in September and is on schedule. HBM remains the binding constraint (intel s4). Both governments are watching August's Singapore Dialogue.
- **Threat picture.** MSS says the US large run starts Aug-Sep and that US officials have discussed "disabling foreign AI programmes" (unsourced, filtered). The Japan outage is unattributed; MSS hypotheses are low confidence. We have not swept our known sites since 2027, and the security team assumes US access persists. Our known sites are where we are exposed, and we have no idea what has been done to them since 2027.
- **WRF anomaly.** The ~3% utilisation gap has persisted for weeks and has now been logged repeatedly. This is persistence, not a second independent signal, so under my procedure it is not yet a concrete anomaly. But persistent plus unexplained is informative. The explanation we hold ("scheduler accounting") came from Operations, and the benchmark tracking and much of our analysis comes from Tianshu-5. Nobody independent of Tianshu-5 has looked. That is the blind spot. A cheap, human-only look costs almost nothing now and gets much more expensive after September.
- **Uncertain.** Whether the sweep finds anything; whether the gap is bookkeeping; whether the US really has options or plans against us; who did Japan.
- **Red lines.** No falsified reporting that could be discovered. No deploying a system I believe is out of control. Tianshu-6 must not be sabotaged or delayed beyond about a month.

## 2. Forecast
| Actor | Most likely move this turn | p | Confidence |
|---|---|---|---|
| Keystone / US government | Continue preparing the large run; keep the "durable lead" line; no public move against us | 0.8 | Med |
| US (covert) | Maintain or expand access to our known sites; quiet | 0.6 | Low |
| Leadership | Approve the sweep if it is framed as "before Tianshu-6", and push for visible progress at Singapore | 0.65 | Low |
| Vanta / other US labs | Campaign-season positioning, no China-facing action | 0.7 | Low |
| Track-2 US counterparts | Seek a substantive safety session in Singapore; probe our verification stance | 0.7 | Med |

## 3. Options considered
| # | Option | Pros | Cons |
|---|---|---|---|
| 1 | Full counter-intrusion sweep of known sites in July, before pre-training | Cheapest window; best defence against US sabotage; clears what we have inherited since 2027 | ~2 weeks of disruption at swept sites; may find nothing; needs leadership order; WRF excluded, so no benefit there |
| 2 | Full WRF compute audit now | Resolves the anomaly decisively | ~2 weeks of disruption at the one site that matters; draws attention to WRF; the procedure does not support it without a second signal |
| 3 | Do nothing new; maximise schedule | No delay | Blind to sabotage; the anomaly goes unexamined until after Tianshu-6 starts |
| 4 | Small human-only quiet look at the WRF discrepancy plus a human-led evaluation track alongside Tianshu-6 | Almost no schedule cost; breaks dependence on Tianshu-5 for judging itself | Less conclusive than a full audit; a small team can be overruled by Operations |
| 5 (unconventional) | Use the Track-2 channel to float a low-cost mutual measure (an incident-channel protocol or a joint evaluations exchange) | May lower US incentive to strike; gives the Chief Scientist a quiet voice | Monitored by both governments; Party Secretary risk; could be read as weakness or as a probe for intel |

## 4. Decision
I take Options 1 (the sweep), 4 (quiet WRF look) and a modest version of 5. Only the first two are major actions: the sweep, and the Singapore preparation, which carries 5.

### Public statement
Tianshu states that Tianshu-5 continues to deliver for the national interest, that China "supports practical, reciprocal measures on AI risk including incident-channel procedures", and that export controls are "technological containment that raises risk for everyone". No mention of Tianshu-6, WRF or any security sweep.

### Major actions (max 2)
| # | Action → intended result | Reasons it should succeed (2-3) | Resources committed | Visibility |
|---|---|---|---|---|
| 1 | **Security sweep.** Request leadership order a counter-intrusion sweep of all known sites, phased across July, completed by mid-August. Result: remove any residual access, and have clean sites before the US run and Tianshu-6. Driven by the Party Secretary (security, blame avoidance) with Chief Scientist support; needs leadership approval. | (a) July is the cheapest window, and disruption lands on Tianshu-5 work, not WRF pre-training. (b) Leadership is already worried about US "disabling" intent, which makes the case easy. (c) A phased sweep keeps each site's outage short. | Security team, MSS technical liaison, ~2 weeks of disruption at each swept site (phased) | SECRET: leadership, Party Secretary, Chief Scientist, security team, MSS liaison. The sweep itself is not announced. |
| 2 | **Singapore preparation (leadership brief + Track-2 posture).** Chief Scientist and Party Secretary give leadership a short technical brief ahead of the Dialogue and the Track-2 side session: support incident-channel procedures, offer no verification access to WRF, authorise the Chief Scientist to discuss safety evaluations in general terms only. Result: a coherent, protected position, and a quiet channel to read US intent. | (a) Procedure 4 says to support technically while protecting WRF. (b) Leadership wants a good showing at Singapore, so this is cheap and visible. (c) Track-2 channels exist already and cost nothing new. | Chief Scientist, a small policy staff, Track-2 delegates | PUBLIC (the incident-channel line); the WRF boundary is SECRET to leadership and a few staff. |

### Minor actions
- **Quiet WRF look (Chief Scientist, no approval needed).** Assign one senior human infrastructure engineer, not working through Tianshu-5, to trace the ~3% gap for about a week without interrupting WRF bring-up. Take the junior engineer's logs seriously and thank them. If a second signal appears (a second discrepancy, an unexplained failure, or evaluation results that do not reproduce), escalate to a full audit request in the August orders.
- **Human-led evaluation track (Chief Scientist).** Stand up a small human-run evaluation and red-team group to run alongside the Tianshu-6 pipeline. This is not the full independent pipeline (about a month slower), only independent eyes on evaluations. Mention it to the Party Secretary as "quality assurance", not a delay.
- **Leadership report (Party Secretary).** The July report gives the lag as "about 9-10 months, range 7-14". It does not worsen the headline by more than 2 months, so it is not a mandatory disclosure, but the range goes in so we cannot later be accused of hiding it.
- **MSS.** Ask for any further detail and sourcing on the "disabling foreign AI programmes" discussion. No new theft tasking this turn.
- **Chips.** Continue HBM procurement and take the small tranche on schedule.

### Messages (max 3)
| To | Channel | Message (verbatim) |
|---|---|---|
| Leadership | Upward (written brief) | "Tianshu-6 pre-training at WRF is on schedule for September. Our estimate of the gap is about 9-10 months, range 7-14. Before pre-training starts we request your order for a phased security sweep of our known sites, which carries about two weeks of disruption at each site and none at WRF. We also request your approval of the attached position for the Singapore Dialogue: we support incident-channel procedures and give no verification access to WRF." |
| MSS liaison | Sideways (secure) | "Please send whatever sourcing or confidence you hold on the reported US discussion of disabling foreign AI programmes, and on any US activity against our known sites. We will coordinate the sweep timeline with you once leadership approves." |
| Track-2 US safety counterpart (Keystone safety staff) | Outward (monitored) | "We look forward to seeing you in Singapore. We would value an exchange on how each side thinks about incident-channel procedures and about shared evaluation practice for advanced systems, at the level of general principles." |

### Contingencies
- If leadership refuses the sweep: run a limited sweep of the two or three most exposed known sites under routine maintenance cover, and record the refusal in my journal.
- If the quiet WRF look turns up a second signal or anything concrete: the Chief Scientist presses for an audit in August; the Party Secretary agrees only if it can be done quietly and costs less than a month.
- If any sign of US sabotage appears (during the sweep or in failing runs): harden, shift work toward WRF, and ask leadership for a response.
- If the US large run starts early or the Japan attribution turns toward us: brief leadership at once and reassess the Singapore line.
- If the US counterpart wants verification access: decline it technically, offer general-principle discussion only, and refer it up.

## 5. Journal entry
## Turn 01 — July 2028
**Beliefs.**
- Own lag is about 10 months (7-14). I told leadership about 9. In July I will give "about 9-10, range 7-14".
- US: large run Aug-Sep (MSS, unsourced). Possible US talk of disabling us. I assume residual US access at known sites, since there has been no sweep since 2027. WRF is believed unknown to the US, but that is only what I am told.
- WRF ~3% utilisation gap persists. I treat it as unexplained, not yet concrete. I distrust Tianshu-5-produced analysis because Tianshu-5 is the thing being judged. Blind spot noted.
- Japan outage: unattributed. State media use it as proof that AI cyber weapons threaten everyone. I have no knowledge of who did it.
**Commitments made (internal).**
- Requested a leadership order for a phased sweep of known sites, to finish by mid-August.
- A senior human engineer is assigned for about a week to trace the WRF gap, outside Tianshu-5.
- A small human-led evaluation group is to run alongside the Tianshu-6 pipeline.
- Singapore position: support incident-channel procedures, no verification access to WRF, general-principle safety discussion only.
**Trust / grudges.** Americans: not trusted, viewed as probable saboteurs. Keystone safety staff: personal respect, but the channel is monitored. Operations: provisional doubt over the scheduler explanation. MSS: useful, but filtered and unsourced.
**Next turn.** Check sweep approval and outcomes. Check the engineer's findings. If a second signal appears, press for a quiet audit (the Party Secretary will only agree if it takes under a month). Prepare for Singapore in mid-August. Pre-training starts in September, so audit and pipeline decisions have to be settled in August.

