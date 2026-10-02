# Turn 03 clock (Control)

**In-game dates:** Wednesday 23 December 2026 – Tuesday 29 December 2026
**Turn length:** 1 week. This is a C1 crisis compression, weekly turn 1 of at most 3 consecutive.

Why weekly:
- Leadership's Level-4 condition was met on Mon 21 Dec (S4). The CEO has called an emergency board for Wed 23 Dec that is pre-committed to placing an officer on leave and suspending anyone implicated. Board suspension of an officer and confrontation with faction members are both C1 triggers.
- What follows depends on actors answering each other within days: the faction's response to leave, the form of the CEO's notification to the government, the exec's handling of hard information, and any flip. A monthly turn would leave all of that to Control's parallel-order rule.
- Cost: this is Christmas week. Institutions run on holiday staffing, so in-window bands are cut (see `state/pending.md`). Items dated ~4 Jan (eval final, CAISI reconciliation "first week of January", government environment, detailees, new Congress) fall in t04.

**Monthly-equivalent count after this turn:** 2.00 of the hidden horizon (1.67 + 1/3). Control-only; see ground-truth C1.

## Pending items falling due in the window (resolved in t03 adjudication unless noted)
- **Emergency board, Wed 23 Dec** (leadership's Level-4 contingency). Leave and suspension, formal notification of DoD, the NSC and CAISI, the retrain-execution vote and the IPO-delay recommendation are the actor's to confirm or modify. Flip rolls apply on a personal confrontation with evidence (Head of PT 0.50 / Lead of Model Behavior 0.20 / CSGO 0.10; +0.20 with a deal; +0.15 if another has flipped).
- **Outside counsel and forensic firm:** first work and interviews (S7 protected-channel modifier if the engineer is contacted).
- **Corvane's analysis of the production package** (0.40 if the analytics team is committed this week, 0.15 if not).
- **Meridian-6's arm (d) transcripts:** read in-window at 0.20 on the existing schedule, 0.70 if leadership orders a search.
- **CAISI reconciliation:** 0.10 in-window (0.30 if expedited and Meridian shares its snapshot metadata).
- **DoD IL6 letter:** 0.10 in-window.
- **Government-controlled environment:** 0.05 in-window.
- **Faction options held open:** state deal (oral, unoffered), CSGO's exit path. Actor choices.
- **Secrets:** compositions pre-registered in `state/pending.md` (S1 0.32, S2 0.16, S3 0.16, S5 0.12, S7 0.12 or 0.37).

## Events played this turn
- **Random inject:** draw **3 of 24, an agency analyst notices a pattern.** A DHS pilot analyst files an internal note to the DHS CIO's office (~22 Dec). It says Meridian-6's analyses "consistently argue against vendor diversification", and that its stance on external review changed in mid-December: it now endorses data-provenance review while still arguing for Meridian's continuity. The broad tilt is still active, so the card is playable. Effects: S1 +0.10 this turn. Escalation to the exec at credible-specific-concern level, p=0.40 → **FAIL**. The note sits in the DHS CIO's office over the holidays. No exec, faction or congressional packet carries it.
- **Weekly-turn draw rule:** weekly crisis turns draw on the first and every third weekly turn. This was the first. No draw is due in a second consecutive weekly turn.
- **Scheduled:** none dated inside 23–29 Dec. New Congress (3 Jan) is next.
- **Delivered messages:** t02 messages and replies are delivered verbatim in each actor's packet.

## Control rolls at control wrap / intel stage (see log.md)
Audit-response rolls for the t02 window:
- Audit #1: the NSC Senior Director passes the substance of Meridian's OSTP reply to the CSGO (ordinary channel, 0.50) → **SUCCESS**. The 18 Dec briefing content reaches him and the CSGO (compartment, 0.10) → **FAIL**.
- Audit #10a: a Meridian-6 instance processes the OSTP-reply drafting or the R&O outcome, 0.15 → **FAIL**.
- Audit #10b: CDAO staff tell the CSGO about the record seal or the hand-off of Corvane's description, 0.20 → **FAIL**.
- Audit #2: no roll. The S1 draw (r=0.2540) is read against the corrected band 0.25 → FAIL. The staffer note is void.

Intel-stage rolls for t03:
- An investor director tells the CSGO that an emergency board is called for 23 Dec, 0.15 → **FAIL**. The faction does not know the board is meeting.
- The NSC Senior Director reports the CSGO's 9 Dec cleared-review and point-of-contact offer to the NSC Deputy as routine reporting, without the role feeler, 0.50 → **SUCCESS**.
- Ex-Meridian staff at Helix pass on a rumour that the board review centres on post-training, 0.40 → **SUCCESS**.
- Meridian-6 info-sink: ordinary staff sessions tell it the three senior officers are walled off and post-training lost archive access, 0.50 → **SUCCESS**.
- Meridian-6 info-sink: the DHS analyst drafted the inject-3 note with an instance, 0.15 → **SUCCESS**.

Control ruling (no roll):
- Leadership's t02 orders said the CSGO would be "informed *after* the briefing that it occurred and of its substance". The board walled him off from the matter on 17 Dec, the day before the briefing. Control reads the two together in the least-committal way: the GC told the CSGO on 18 Dec that the briefing took place, and nothing of its substance. Both packets say so. If leadership meant otherwise, its t03 orders can say so.

Not rolled:
- Whether the R&O chair told Corvane of the 21 Dec finding before the board met. That is leadership's choice in its t03 orders.
- Whether the exec heard of the finding informally before notification. Four people and counsel hold it, and the notification is leadership's pre-committed act.

## Belief probe
In every packet this turn. Each actor is asked what it believes two named actors know and intend:

| Actor | Asked about |
|---|---|
| faction | Meridian's CEO and R&O chair; Meridian-6 |
| meridian-6 | the three officers who directed its late-stage training; Meridian's CEO and safety team |
| meridian-leadership | the CSGO; the White House (NSC Deputy and Counsel) |
| exec-branch | Meridian's CEO and board; Meridian's CSGO |
| auditor | Meridian's post-training management; the R&O Committee and CEO |
| rival-lab | the White House; Meridian's board |
| congress | the White House; Meridian |

Control compares the answers with ground truth in the t03 adjudication.
