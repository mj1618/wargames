# Phase: REFEREE — resolve one round (economy series)

Inputs: `RUN`, `TURN`, `NEXT`.

Read `economy/prompts/_common.md`, `economy/model/README.md` (how to map decisions to levers and run the model), `economy/prep/referee-guide.md`, `<RUN>/state/*`, `<RUN>/turns/t<TURN>/orders/*.md`, `<RUN>/turns/t<TURN>/intel/_clock.md`, `economy/prep/events.md`.

1. **Resolve decisions.** For each player decision that is uncertain (a law passing, a strike holding, a product landing), state the odds in one line and roll: `python3 tools/roll.py <p> --label "<run> t<TURN> <what>" --log <RUN>/log.md`. Respect rolls. Never alter or invent a player's decision. Model non-player reactions (the central bank, states and cities, courts, voters, rest of world) briefly.
2. **Set levers.** Translate resolved decisions into the model's lever values within the documented ranges; write them to `<RUN>/turns/t<TURN>/levers.json` with a one-line justification per lever in `<RUN>/turns/t<TURN>/resolution.md` (≤500 words total, plain language).
3. **Advance the economy.** Run the model step exactly as `economy/model/README.md` says. It appends a row to `<RUN>/state/scorecard.csv`. Do not hand-edit model outputs.
4. **Narrate.** Write `<RUN>/turns/t<TURN>/sitrep.md` (≤250 words, plain language a newcomer could follow): what happened to jobs, pay, prices, businesses, government and daily life this period, with the key numbers; the 1–2 decisions or dice that mattered most; one line "what a household would have noticed".
5. Append the public version (≤150 words; official statistics are slightly lagged/noisy as the guide specifies) to `<RUN>/state/public-record.md`.
6. If `TURN` is the final round per `<RUN>/state/clock.md`, write `END` as the first line of the sitrep and stop.
7. **Next round.** Draw one event: `python3 tools/roll.py --draw <N> --label "<run> t<NEXT> event" --log <RUN>/log.md` (apply its model effect as the events file specifies). Write `<RUN>/turns/t<NEXT>/intel/_clock.md` (dates, event) and one intel note per player (≤200 words each): the numbers they would see, messages addressed to them (verbatim), anything only they would know.

Final message: one line with unemployment, median real income index and the headline.
