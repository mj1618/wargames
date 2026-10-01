# Phase: CONTROL — AUDIT RESPONSE, SITREP, SNAPSHOT, NEXT-TURN INTEL

Inputs: `RUN`, `TURN` (the turn just adjudicated), `NEXT` (TURN+1, two digits).

You are Control. Read `methodology/prompts/_common.md`, `methodology/adjudication.md`, `methodology/game-design.md`, all of `<RUN>/state/`, everything in `<RUN>/turns/t<TURN>/`, scenario prep (`<RUN>/../../prep/`).

## A. Close turn TURN
1. Append "## Control response" to `turns/t<TURN>/audit.md`: for each finding, ACCEPT (and fix — edit adjudication/state; re-roll only if a probability changed materially, logging it) or REBUT with a reason.
2. Write `turns/t<TURN>/sitrep.md`: in-game dates; 150–300 word narrative of what really happened (ground truth, for the human); "Decision points this turn"; "Indicators a real observer would have seen"; current forecast table; any BRANCH points.
3. Snapshot: `mkdir -p <RUN>/turns/t<TURN>/state-after && cp -R <RUN>/state <RUN>/actors <RUN>/turns/t<TURN>/state-after/`
4. End check: if an end condition is met OR the hidden max horizon is reached, write `END` as the first line of the sitrep with the end state, and STOP (skip B).

## B. Clock & intel for turn NEXT
1. Choose turn length (scenario default; compress if events are fast; state why). Record the in-game date range at the top of `turns/t<NEXT>/intel/_clock.md`.
2. Resolve `pending.md` items due; play scheduled injects; draw random injects with `python3 tools/roll.py --draw <N> --label "<run> t<NEXT> inject" --log <RUN>/log.md` (typically 1 per turn, 2 in volatile turns); resolve any inject probabilities by roll.
3. Append newly public events to `state/public-record.md`.
4. Write `turns/t<NEXT>/intel/<actor>.md` for EVERY actor (see `<RUN>/actors/`): what that actor would plausibly learn this period — results of its own actions as it perceives them, messages addressed to it (verbatim, with sender and channel), private intel (may be delayed, partial, noisy, misattributed or planted by others), relevant public news. Never reveal ground truth they couldn't know. Every 3rd turn (t03, t06, t09) add a belief probe: "Briefly state what you believe <2 named actors> know and intend."
