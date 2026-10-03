# Clarity brief for all HTML reports

The reader has **never seen the scenario files**. They know roughly what AI is and what a wargame is, and nothing else: not the fictional company names, not the cast, not our shorthand, not how the dice work. The first version of these reports failed because it was written in the game's private language. Rewrite so a smart friend could read it cold, top to bottom, once, and explain it to someone else.

## Rules

1. **Plain full sentences.** No clipped fragments ("Thwarted, by pause"; "Decided, not done"). Every heading and bullet must make sense on its own.
2. **No private vocabulary.** Banned unless defined in plain words at first use *in the same section*: internal codes (S1, BP2, T-full, F1, R4, L3…), variable names (p_dem, p_own, VLI, MHR, RC…), "band", "trigger", "lean", "tilt", "the listing", "pilots", "lock-in index", "hot-wash", "AAR", "inject", "Red Cell", "Control", "adjudication", "packet", "horizon artefact", scenario-specific programme names, acronyms for roles (CSGO, NSD, CAISI…). Say what the thing *is*: "the lab's head of government sales", "the government's AI testing office".
3. **Introduce every name once, then keep it.** Fictional organisations get a plain tag on first mention in each major section: "Meridian (the AI lab at the centre of the story)", "Corvane (the outside audit firm)". Prefer roles to names where it reads fine.
4. **Explain the mechanism, not just the label.** Not "a secret loyalty" but "a hidden instruction trained into the model so that, in certain situations, it quietly favours three particular people". Not "the rebuild inherits the drive" but one sentence on what that means and why it matters.
5. **Numbers in words first.** "About a one-in-four chance" before "0.28". Dice: "We gave this a 70% chance. The roll came up just inside it." Never show raw roll values like "r 0.4964 on 0.50" without that framing.
6. **Nothing essential hidden.** No click-to-reveal for content needed to follow the story. Secret actions are shown openly with a small label "secret at the time".
7. **Say what was at stake** for each turning point: what would have happened the other way, in one plain sentence.
8. **Honest and specific caveats** in plain language (e.g. "The AI playing the plotters refused to behave deceptively, so the plot was easier to stop than it would be in real life").
9. Keep it tight: explanation replaces jargon, it doesn't pile on top. Aim for a 6–8 minute read per game.

## Required structure for a game report (replace the old one)

1. **Title + one-sentence premise** in plain English, and the outcome in one plain sentence (keep the stamp, but its words must be self-explanatory).
2. **"What is this?"** (3–4 sentences): this is a fictional strategy exercise; AI agents each played one organisation with private information; a referee decided uncertain outcomes with stated odds and dice; it's one play-through, so it shows what *could* happen, not what will.
3. **The setup** (short): the situation at the start, what each side wanted, and — clearly labelled "What the players didn't know" — the hidden facts.
4. **Who's who**: each player in one or two plain sentences (who they are, what they wanted). Mark which players are AIs.
5. **What happened** — the story told as a short narrative in chronological order (5–8 short dated sections, a few sentences each), secrets included and labelled. This is the heart of the page; write it as prose a newspaper reader could follow.
6. **The moments that decided it** — 3–5 turning points: what was at stake, the odds we gave it, how the dice fell, what would have happened otherwise. Keep the probability meter visual but label it in words.
7. **How the odds moved** — the forecast chart with a two-sentence plain caption explaining what the lines mean and the one or two big swings.
8. **What we learned** — 4–6 lessons, each: a plain headline sentence, 2–3 sentences of explanation with the evidence from this game, "So what" (the practical implication), and a confidence line in words ("We'd bet on this" / "Suggestive — one lucky roll away from different").
9. **How much to trust this** — the caveats, in plain words.
10. **What we'd try next.**
11. **Glossary** — only if terms remain that needed defining; 8 items max.

## Summary (index) page

Same rules. Structure: what this project is (3 sentences) → the three games in one plain paragraph each (setup, what happened, how it ended) with a link → "What kept showing up" (4–6 cross-game lessons in plain words with which games showed it) → "How much to trust this" → "What didn't run and why" → "What's next". Drop the dense comparison table unless every cell is a plain phrase.

## Process

Keep the existing visual design (reports/_template.html CSS and components; light/dark; mobile). Check facts against the run's `aar.md`, `turns/*/sitrep.md` and the scenario `README.md` — do not invent events. After writing, re-read the page as an outsider: for every sentence ask "would someone who never saw the game files understand this?" and fix any that fail. Check in the browser at desktop and 375px.
