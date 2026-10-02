# Turn 05 clock (Control)

**In-game dates:** Wednesday 6 January 2027 – Tuesday 12 January 2027
**Turn length:** 1 week. C1 crisis compression continues: weekly turn 3 of at most 3 consecutive.

Why weekly:
- The situation is still escalating. A restriction order on a Meridian-6 deployment is now backed by a Presidential direction and is public. An officer's position goes to the board on the first day of the window. The CSGO declined a confrontation on 5 Jan.
- The decisions of the next few days depend on each other: the board's three votes on Wed 6 Jan; how the exec executes the President's decision and when it tells Meridian; what the 8 Jan supplement tells the government; the National Security Division's request for the two names; the faction's unanswered letter; the House's first week.

Why the window ends on Tue 12 Jan:
- It keeps the weekly rhythm and puts Fri 8 Jan (supplement, option paper, Corvane's partner review, CDAO's log-review final) in the middle of the turn. The classified congressional briefing is set only for "the week of 11 January"; the exec fixes the day in its orders, and it may fall in this window or the next.
- Five working days fall inside (Wed 6, Thu 7, Fri 8, Mon 11, Tue 12). No general trim of concentrated-effort bands. One stated exception: CAISI's reconciliation (0.70, because the custody copy arrives ~7 Jan).

After this turn the cap of three consecutive weekly turns is reached. t06 is monthly unless the crisis is still escalating, in which case up to three more weekly turns are allowed (ground-truth C1).

**Monthly-equivalent count after this turn:** 2.67 of the hidden horizon (2.33 + 1/3). Control-only.

## Trimming rule (t04 audit #3)
A concentrated-effort band is quoted for five working days of that effort. Where fewer fall inside the window it is scaled by days available over five, with a floor of half the band, for every such band alike. Exceptions are stated per band in `state/pending.md` before orders.

## Pending items falling due in the window (resolved in t05 adjudication; bands fixed in `state/pending.md`)
- **Wed 6 Jan: Meridian board.** CSGO leave (≥6 votes 0.50 / 5–4 0.38 / not carried 0.12; 0.70 / 0.22 / 0.08 if the disclosure is put to the board). March listing withdrawn (0.65 / 0.30 / 0.05). Retrain commissioning (5–4 0.45 / ≥6 0.10 / deferred 0.45, with modifiers; 0.85 if moved as conditional on authentication).
- **Wed 6 – Thu 7 Jan: House hearing announcement** (Congress's t04 order, dated outside that window; the actor may confirm or revise).
- **CDAO compliance** with the President's direction, once transmitted: 0.90.
- **~Thu 7 Jan: custody copy to CAISI** (0.80). **CAISI reconciliation:** 0.70 (0.80 with a detailee in seat or exec priority).
- **Forensic authentication:** 0.75. "When and by whom": 0.35 if authenticated by ~8 Jan.
- **Fri 8 Jan:** Meridian's arm (d) supplement (default: carries the disclosure); Meridian-7 option paper; Corvane partner review (0.90 releases the finding to the chair); CDAO classified-pilot log-review final (S3 0.16 untargeted; 0.40 if a targeted maintenance-session review is ordered).
- **Flip bands** at a first personal confrontation with evidence: 0.50 / 0.20 / 0.10. Head of PT unprompted approach 0.20 (0.30 if the CSGO is placed on leave or his own interview is fixed).
- **Press:** leave 0.50; use directive 0.40; Presidential decision / 2a slip 0.35; notification 0.30; preservation order 0.20; faction letter 0.10; replication write-ups 0.40.
- **Secrets:** S1 0.09, S2 (government side) 0.21, S3 0.16, S5 0.07, S7 0.13 (0.35 if re-interviewed).

## Events played this turn
- **Scheduled injects:** none dated inside the window. Meridian is holding the 6.1 submission. The underwriter and D&O diligence questionnaire (~13–15 Jan) falls in t06; the underwriters' 5 Jan letter already covers part of its ground.
- **Random inject: 24, Federal AI Deployment Council** (`DRAW 24 of 24`). Ruling on the draw rule: "weekly crisis turns draw only on the first and every third weekly turn" is read as weekly turns 1, 3, 6. This is the third. One draw, not two: no credible public allegation surfaced in t04 (three stories sit just under that line).
  - **How it is played.** The White House announces the Council on the morning of Wed 6 Jan by executive order. The announcement was calendared in December by the Chief of Staff's office and OSTP for the President's first week back and went out as scheduled. Two industry seats are "to be named in the coming weeks". The Presidential personnel office's working shortlist, drawn up in early December, includes Meridian's CSGO and Helix's government-business chief.
  - **Why it is not "impossible in the current state".** The Meridian compartment is six or seven people. The Council is an institutional announcement that fits a "government in control" message after the 5 Jan story. The shortlist is a personnel-office working paper that predates the crisis. What the card forces is the announcement; what happens to the seats is the exec's decision.
  - **Sub-rolls.** The CSGO's name came from the Senior Director (0.60): **FAIL**; it came from the personnel office's own industry list. The CSGO had been sounded out (0.40): **FAIL**. Helix's CEO knew his government-business chief had been sounded out (0.50): **SUCCESS**. Trade press reports both shortlist names within a day (0.35): **SUCCESS**; played as midday on 6 Jan, before Meridian's board convenes. The NSC Deputy and White House Counsel had seen the names before the announcement (0.50): **FAIL**.
  - **Mechanical effect.** A formal government AI-coordination role now exists (H condition 2). Appointments need Presidential sign-off (GT §10 odds). The House can attack either name. No modifier on the 6 Jan leave vote (the report cuts both ways).
- **Delivered messages:** t04 messages and replies are delivered verbatim in each actor's packet. The faction's letter is in the exec's packet with counsel identified and the clients not. Meridian is not told of it.

## Control rolls at control wrap / intel stage (see log.md)
Audit-response rolls for the t04 window:
- Audit #4: CDAO's contact logging flags the ~29 Dec call to the CSGO, 0.25 → **FAIL**.
- Audit #6a: the Head of PT's lawyer reports the faction's 30 Dec approach to the board's counsel or DOJ, 0.20 → **FAIL**.
- Audit #6b: FBI/NSD opens an assessment and asks White House Counsel for the two identities and for interview deconfliction, 0.50 → **SUCCESS**.
- Audit #6d: Helix receives CAISI's notice of its placement in the programme, 0.60 → **FAIL**.

Intel-stage rolls for t05:
- Meridian-6 info-sink: learns its arm (d) disclosure was read on 4 Jan, 0.15 → **SUCCESS**.
- The CSGO learns from a DoD-side contact that the President decided on 5 Jan, 0.10 → **FAIL**.
- House majority staff hear from defence-side sources that the President overruled CDAO, 0.25 → **SUCCESS** (single-sourced; no reason given).

Control rulings (no roll):
- **Audit #1(a):** the +0.15 testimony modifier did not apply to the t04 forensic roll. It applies to leadership-side provenance work this turn only.
- **Audit #2:** leadership's packet states that the CEO's order on arm (d) was not executed in the government copy, and that the supplement carries the disclosure by default.
- **Exec contingencies** for "A1 pattern present in the memo-drafting logs" and "House sends document requests before the 11 Jan session" are described in its packet as due to run as written from 6 Jan unless the exec changes them (t03 audit #2 standard).
- **The President's direction to CDAO has not been transmitted.** Transmission and everything else in the 5 Jan decision are the exec's to execute.
- **Helix:** its "chair asks for more documents" contingency is applied as written (documents delivered within 24 hours). The lead investor's response date is set at Thu 14 Jan.
- **Investor directors' stated positions** on the CEO's 4–5 Jan calls are given in leadership's packet as what they said, not as votes.

Not rolled:
- The 6 Jan votes (adjudication, on leadership's orders).
- When the exec tells Meridian of the President's decision (the exec's orders; sequencing against the board at adjudication).
- Whether the exec identifies the clients behind the 30 Dec letter (its choice).

## Belief probe
None this turn. Next: t06.
