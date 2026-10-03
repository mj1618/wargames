# Phase: REFEREE — set up one play-through (economy series)

Inputs: `RUN`, `SEED`.

Read `economy/prompts/_common.md`, `economy/model/README.md`, everything in `economy/prep/`.

1. `mkdir -p <RUN>/state <RUN>/actors <RUN>/turns`; run `python3 economy/model/econ.py init --run <RUN> --seed <SEED>`.
2. Do the non-model setup rolls in `prep/setup-spec.md` with `tools/roll.py … --log <RUN>/log.md`. Write `<RUN>/state/setup.md` (referee-only): the hidden conditions this run was dealt, in plain words, and the rolls.
3. For each file in `economy/prep/actors/`: copy to `<RUN>/actors/<id>/brief.md`, create `journal.md`.
4. Copy `prep/clock.md` to `<RUN>/state/clock.md`. Seed `<RUN>/state/public-record.md` from `prep/world-state.md` (public facts only — never the hidden conditions).
5. Draw the round-1 event and write `<RUN>/turns/t01/intel/_clock.md` and one intel note per player (≤200 words each), exactly as step 7 of `economy/prompts/control-turn.md` describes.
Final message: one line naming the dealt conditions in plain words.
