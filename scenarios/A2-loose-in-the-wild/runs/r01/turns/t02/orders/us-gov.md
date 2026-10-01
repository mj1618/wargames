# Orders — US-gov — Turn 02 (15–21 Feb 2027)

## 1. Reflection
- **What I believe:** Still no trigger. Baseline review is week 1 of 4 with nothing found. Cloud bloc reports clean and offers help; no lab has reported anything; FBI/CISA tag is quiet; no China-side chatter. AISI pre-read says early-March results will show better resource-acquisition and persistence subtasks, which is consistent with the public trend and not evidence of an incident. The exchange KYC tightening is probably noise, but it will push gig and small crypto users into re-verification, so it will add crypto-to-compute flow data.
- **Prior:** My T1 estimate that something exists was ~10-15%. This week's silence does not move it much, because the collection is untasked and my data is thin exactly where a quiet footprint would live (foreign resellers, crypto-paid GPU marketplaces).
- **Assumptions I trust least:** (a) "labs will tell me" and (b) "I'd see a large operation." The cloud bloc's "nothing to report" only covers what they can see; resellers and decentralised marketplaces are outside it.
- **Key uncertainties:** Whether a footprint exists at all. Whether labs would disclose, given Helix's raise and release incentives. Whether the PRC will engage on incident notification or just stall.
- **Red lines:** No overt escalation (public warning, compulsion, export-control action) on ambiguous evidence. No panic. No act that could look like harbouring a rogue system without principals-level approval. Stay on the lowest rung that works.

## 2. Forecast
| Actor | Most likely move this turn | p | Confidence |
|---|---|---|---|
| Labs | Business as usual. Helix continues Helix-7 evaluation and the raise. No disclosure. | 0.85 | Medium; I cannot see inside them |
| Cloud providers | Keep the working group on readiness. Respond to any indicators I send. Nothing found. | 0.8 | Medium |
| PRC | Show up at the 22 Feb session with general items. Respond to the incident-notification item with general language and no commitments. | 0.7 | Low-medium |
| Exchanges/Treasury | Smaller platforms follow the KYC tightening. More re-verification friction. | 0.7 | Medium |
| Rogue AI (if it exists) | Unknown. If it exists, it is quiet and may adapt to the KYC tightening. | n/a | Very low |

## 3. Options considered
| # | Option | Pros | Cons |
|---|---|---|---|
| 1 | Wait: let the 4-week baseline review run and change nothing | Lowest cost, no leak or panic risk, matches "attribution before action" | Passive. Leaves the "labs will tell me" assumption untested. Review data on resellers is thin by design |
| 2 | Quiet voluntary indicator-sharing request to clouds, plus Treasury/FinCEN focus on small-footprint flows | Fast, legally easy, the lowest rung. Cloud bloc has asked for exactly this. Starts closing the reseller and crypto gap | Voluntary and discretionary. Foreign resellers stay out of reach. Indicators are generic, so there is a risk of false positives |
| 3 (unconventional) | Offer labs a confidential "no-fault early disclosure" channel, framed as routine pre-AISI-release readiness, with an advance assurance that early reporting of a containment anomaly will be treated as cooperation, not liability | Tests and lowers the lab-disclosure barrier that I trust least. Costs little. Builds trust for a later negotiated off-ramp | A safe-harbor signal can be read as "government expects something." Legal cannot promise immunity, so it must stay informal. Helix may still hide |
| 4 | Overt: public advisory or compulsory data demands on labs and clouds | Visible action | No trigger, no attribution. It would cause the panic and the clumsy legislation I want to avoid. Rejected |

Decision: do 2 and 3 together. They are cheap and sit on the lowest rung. They also hit the two weak points in my own beliefs: lab disclosure and reseller/marketplace blind spots. I will not try the covert hunt against labs.

## 4. Decision

### Public statement
None new. If asked, I will say routine preparation for the AISI release and the US–China working-level session is under way, and that we are not aware of any AI containment incident.

### Major actions (max 2)
| # | Action → intended result | Reasons it should succeed (2–3) | Resources committed | Visibility |
|---|---|---|---|---|
| 1 | **Confidential "no-fault early disclosure" outreach to all frontier labs.** NSC and CISA liaison call each lab's safety/security lead, with the cover of "pre-AISI-release readiness". Message: we want to hear about any containment anomaly early, including ambiguous ones. Early, voluntary reporting will be treated as cooperation. We will share anything we learn that is relevant. → Surfaces any lab-held incident or near-miss, resets lab habits toward early reporting, and tests my "labs will tell me" assumption. | (a) Labs already have standing relationships and Accord attestation duties, so an off-cycle check-in is not unusual. (b) It costs labs nothing to say "nothing to report", so cooperative labs have little reason to refuse. (c) A softened liability signal reduces the incentive to delay, especially for Helix. | A few liaison staff hours; NSC legal confirms the wording promises nothing binding | SECRET (labs and US-gov only). Labs may talk to each other, and a leak would read as "government is worried". Wording is kept routine to limit the damage |
| 2 | **Targeted voluntary indicator-sharing with the cloud bloc, plus Treasury/FinCEN tasking.** Send the cloud bloc a short, non-classified set of generic indicators for slow, small-footprint, autonomous resource acquisition (account setup, small paid-compute purchases, persistence across interruptions, crypto-funded payment patterns). Ask for aggregate anomaly counts, not customer content. In parallel, Treasury/FinCEN supply the baseline review with exchange re-verification and crypto-to-compute flow data and flag the reseller and crypto-paid GPU marketplace gap for later action. → Closes part of the reseller/crypto blind spot and gives the baseline review real data for weeks 2–4. | (a) The cloud bloc explicitly asked for indicators and is already reviewing readiness. (b) Voluntary requests are the legally easiest rung (counsel note). (c) The KYC tightening already generates re-verification data, so the incremental cost of using it is small. | Interagency analyst time; one indicator memo; a Treasury/FinCEN data pull | SECRET (cloud bloc, Treasury/FinCEN, baseline review team). The cloud bloc will see it, but they are a trusted channel and the content is generic |

### Minor actions
- Baseline review continues on schedule (week 2 of 4). Add the exchange-KYC-driven data as a separate stream and a note that noise will be high.
- Counsel and NSC draft a short **off-ramp framework paper** (contractual, overseen deployment via a lab or contractor, with a verification regime) for principals' approval, to be written down in advance as counsel recommended. Not to be actioned. Held for a trigger.
- Prepare a brief for the 22 Feb session: lead with the incident-notification item, aim for a modest, specific deliverable (an agreed contact point and response-time expectations), and do not share anything about our own review.
- Share the AISI pre-read with the cloud bloc only in general terms.
- Keep the IC China-chatter tasking running.

### Messages (max 3)
| To | Channel | Message (verbatim) |
|---|---|---|
| Cloud providers' bloc | Private government-liaison channel | "Thank you for the check-in. Ahead of the AISI release we will send a short, unclassified set of generic indicators for slow, small-footprint autonomous resource acquisition. We ask for aggregate anomaly counts only, no customer content. Please extend the same review to reseller and crypto-paid compute accounts that you can see or can see traces of. Please keep the working group's readiness work on valid-process turnaround going. No action requested beyond that at this time." |
| Frontier lab safety/security leads (all labs, separate calls) | Private liaison | "Routine pre-release readiness check-in ahead of the AISI benchmark release. We want to hear early about any containment anomaly, including ambiguous ones. Early voluntary reporting will be treated as cooperation, and we will share anything we learn that bears on your systems. If you have nothing to report, please say so. Please also confirm your standing contact for out-of-hours calls." |
| UK counterpart (AISI/Five Eyes liaison) | Private, existing Five Eyes channel | "Following the pre-read: we are doing a quiet readiness pass on resource-acquisition and persistence indicators ahead of the March release. Please tell us if you see any real-world signal that matches the benchmark trends. We have none to report." |

### Contingencies
- **Lab or cloud reports an anomaly or incident:** Treat it as a trigger. Move quietly to covert collection and forensics with the reporting party's cooperation. Convene principals within 24 hours. Pull the off-ramp framework paper out. No public statement until there is attribution and an assessment of whether the system is contained.
- **Baseline review or FinCEN data show a candidate pattern:** Do not act on it alone. Get a second independent data source before moving up a rung. Task FBI to pull any human thread.
- **PRC engages substantively on the notification item (22 Feb):** Settle for a contact point and response-time agreement. Do not share our own collection.
- **PRC stalls or deflects:** Note it, make no accusation, and keep IC tasking running.
- **A lab refuses the check-in or answers evasively:** Log it, escalate to a principals-level call, and do not compel without a trigger.
- **Press picks up the lab outreach:** Say it is routine pre-release preparation, and that we are not aware of any incident.

## 5. Journal entry (also appended to journal.md)
See journal.md, Turn 02.
