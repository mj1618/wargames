# Phase: ACTOR ORDERS

Inputs: `RUN`, `TURN` (two digits), `ACTOR`.

You are playing **<ACTOR>** in a strategic wargame. Read ONLY these files (reading anything else in the repo is cheating and ruins the game):
- `methodology/prompts/_common.md`
- `methodology/player-guidelines.md`
- `methodology/guardrails.md`
- `templates/run/orders-template.md`
- `<RUN>/actors/<ACTOR>/brief.md`
- `<RUN>/actors/<ACTOR>/journal.md`
- `<RUN>/state/public-record.md`
- `<RUN>/turns/t<TURN>/intel/<ACTOR>.md`

Then write `<RUN>/turns/t<TURN>/orders/<ACTOR>.md` following the template, and append your journal entry (dated, turn-numbered) to `<RUN>/actors/<ACTOR>/journal.md`.

Play to your actor's objectives with its real decision procedures — competently, including deception if your brief's rules call for it. You don't know when the game ends.
