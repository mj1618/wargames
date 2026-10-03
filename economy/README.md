# Economy Games — what rapid AI and robotics do to jobs and living standards

A separate series from the takeover wargames in `../scenarios/`. Same engine idea (AI agents play organisations with private information; a referee resolves uncertainty with stated odds and dice), but the subject is the economy.

**Premise (given, not tested):** AI and robotics keep improving rapidly through 2036.

**Questions to answer**
1. **Does a Jevons effect hold for work?** Do the improvements create more jobs than they remove? Does unemployment go up, down, or stay put?
2. **Do ordinary people end up better off?** Do living standards rise, do poverty and homelessness fall — or do the gains go mostly to the top?

**Design**
- One scenario (US-centred, Jan 2027 – Dec 2036, 7 rounds), played **5 times**.
- Each play-through rolls different hidden conditions at the start (how strongly cheaper goods and services create new demand and new kinds of work; how fast robots arrive; who captures the profits; politics) plus its own dice and random events.
- A small, documented economic model (`model/`) keeps the numbers: the referee turns players' decisions into policy and behaviour "levers", the model advances the economy one round, the referee narrates. The same model is also run 1,000 times with dice only, so the 5 played games can be placed against the wider spread of outcomes.
- Every round appends a row to `runs/<run>/state/scorecard.csv` (unemployment, jobs created and lost, median income, poverty, homelessness, inequality, public finances…).

**Honesty rule:** the answer depends on assumptions nobody can know yet. The write-up must say which assumptions drove each outcome, and what was decided by players' choices versus the dice.

```
research/   evidence brief the rules are built from
prep/       world state, actor briefs, events deck, setup-roll spec
model/      the economic model (code + documentation of every parameter)
prompts/    lean phase prompts for this series
runs/r1…r5/ the five play-throughs
reports/    the summary page (published at /economy/ on the Pages site)
```
Guardrails, plain-language report rules and git policy are inherited from the repo root (`../CLAUDE.md`, `../methodology/guardrails.md`, `../methodology/prompts/report-clarity.md`).
