# Wargame Methods Brief — AI-risk games with LLM players

*Compiled 2026-10-02 by research sub-agent. "(inference)" = the researcher's own reasoning, not a published finding.*

## 1. Prior AI-focused games

### Intelligence Rising (Avin, Gruetzemacher, Fox et al.) — 43 games, 2020–24
<https://arxiv.org/abs/2410.03092> · <https://arxiv.org/abs/1912.08964> · <https://www.intelligencerising.org/>
- **Actors:** US, China, two multinational labs. Non-R&D actors "had very limited available actions" → keep active roster lean; NPC the rest.
- **Turns:** ~2 years each; US elections every 2 turns via context-adjusted dice.
- **Loop:** negotiation → simultaneous secret commitment → facilitator resolution. Each team gets **2 freeform policy actions/turn** (attention economy) + an R&D allocation across a two-lane tech tree. Secret actions resolved privately.
- **Adjudication:** semi-free; final safety outcome by dice roll. Facilitators admit large inter-facilitator variance.
- **Findings:** companies outpace governments; proxy races (states back firms) common, nationalisation a large minority; endgame US–China deals fail or see last-minute defection and cyber/hard-power conflict; **weight/algorithm theft among the most common events**; good outcomes need early trust-building and verifiable deals; players portray Western actors more confidently than Chinese.

### AI 2027 TTX (AI Futures Project)
<https://ai-2027.com/about?tab=tabletop-exercise> · <https://www.lesswrong.com/posts/TjT3RdAfmrLqgb68K/>
- ~4 hours, 8–14 players, 35+ runs. Starts Apr 2027 (superhuman coder; China stole weights) — "the last predictable period".
- Roles: POTUS/exec, lead-lab CEO, safety team, **the AIs (a human player)**, China, others. Congress/public rarely act fast enough.
- Typical: most runs reach ASI; geopolitical race dominates; misalignment warnings ignored; cyber common; global war rare. **"The ending is usually determined by the goals the AIs happen to have"** → if alignment is exogenous luck, player choices can't move the key outcome.

### RAND "Day After AGI" / Infinite Potential (2025)
<https://www.rand.org/pubs/research_reports/RRA4231-1.html> · RRA4230-1 · RRA4626-1 · [AEI](https://www.aei.org/articles/wargaming-an-agi-cyber-surprise/)
- 2-hour NSC Principals seminar; two turns (intel response; crisis worsens/mutates); backcasting. No outcome adjudication.
- Findings: beliefs about AGI first-mover advantage drove response seriousness; **attribution** (state vs rogue AI vs third party) drove response and players felt "largely blind"; "use-it-or-lose-it" escalation instincts; demand for pre-built playbooks and AI forensics.

### Others
Convergence "Threshold 2030" (<https://www.convergenceanalysis.org/threshold-2030/>); METR Frontier Risk Report pilot exercise (<https://metr.org/blog/2026-05-19-frontier-risk-report/>); JHU/APL GenWar (LLMs + physics adjudication, 2026). No public CNAS/CSET frontier-AI TTX write-up found.

## 2. Design craft

- **Adjudication spectrum** (UK MoD Wargaming Handbook 2017, <https://assets.publishing.service.gov.uk/media/5a82e90d40f0b6230269d575/doctrine_uk_wargaming_handbook.pdf>): free / rigid / **semi-rigid** / consensual. Light touch; adjudicator must not become a "dominant player" (Downes-Martin 2013). **Moderation toward the mean sidelines chance and bad luck.** Avoid pre-scripting. Games are not predictive; single runs yield false lessons.
- **Matrix games** (Engle; Curry & Price): action + result + 2–3 reasons; others counter-argue; umpire sets odds; die decides. ChatGPT-as-umpire gave absurd actions 25% odds ([PaxSims](https://paxsims.wordpress.com/2024/02/28/chatgpt-plays-a-matrix-game/)) → probabilities need anchors and challenge.
- **Seminar vs adjudicated:** seminars elicit judgements cheaply; multi-turn adjudicated games generate dynamics (races, betrayals, path dependence). Perla's cycle of research: games generate hypotheses; analysis tests them.
- **Control/White cell:** objectives, adjudication, clock, "nature", information, NPCs. **Red cell** adds friction and challenges assumptions.
- **Injects:** randomised conditional deck beats a fixed timeline.
- **Fog of war:** secret actions, noisy/false intel, attribution ambiguity.
- **AAR:** hot-wash then structured analysis tied to evidence; success = insight, not victory.

## 3. LLMs as players — evidence

| Study | Finding |
|---|---|
| Rivera et al. 2024 <https://arxiv.org/abs/2401.03408> | All models escalated, arms-race dynamics, occasional nuclear use |
| Lamparth et al. 2024 <https://arxiv.org/abs/2403.03407> | ~50% overlap with 214 human experts; LLMs more aggressive; **"farcical harmony"** in team dialogue; **persona adjectives had no effect** |
| Shrivastava et al. 2024 <https://arxiv.org/abs/2410.13204> | High run-to-run inconsistency |
| Snow Globe (Hogan & Brennen) 2024 <https://arxiv.org/abs/2404.11446> | Per-player history objects for info asymmetry; "include unexpected consequences" helps; failures: **repetitive turns, Control hallucinating plans players never made** |
| Payne 2026 <https://arxiv.org/abs/2602.14740> | Reflection → Forecast → Signal+Action loop; signals can diverge from actions; no model ever chose accommodation; **deadlines flipped behaviour** (end-game gambles); private accidents mechanic |
| Elbaum & Panter 2025 <https://arxiv.org/abs/2508.01056> | Temperature/de-escalation prompts move escalation ~50% → results are prompt-dependent |
| Jensen et al. 2026 <https://arxiv.org/abs/2608.05180>; Touchent 2026 <https://arxiv.org/abs/2608.12373> | Large model-to-model differences; prompt language can swing results massively |
| "Too Good to be Bad" 2025 <https://arxiv.org/abs/2511.04962> | **Safety-tuned models play villains poorly** — deceit/manipulation worst; substitute superficial aggression |
| Riedl & Matlin 2026 <https://arxiv.org/abs/2609.16189> | Failure modes: decision laundering, adjudication opacity, **role collapse**, **escalation-through-adjudication**, failure of strategic imagination |
| Concordia <https://arxiv.org/abs/2312.03664> | Game Master grounds and resolves natural-language actions |
| Conformity <https://arxiv.org/abs/2606.00820> | 20–39% harmful conformity in multi-agent debate |
| AgentLeak <https://arxiv.org/abs/2602.11510> | Inter-agent messages/shared memory leak private info |
| Homogeneity <https://arxiv.org/abs/2507.19364> | Model heterogeneity drives diversity more than persona prompts |

## 4. Recommendations adopted into our methodology

See [methodology/game-design.md](../methodology/game-design.md). Key adoptions:
1. **No winning, hidden horizon** — actors get real objectives, never told the end turn (avoids deadline gambles).
2. **Lean roster** (5–7 active actors) + Control-run NPCs.
3. **Canonical structured state** in ground truth; narrative is a rendering.
4. **Attention economy** — ≤2 major actions/turn, capped private messages.
5. **Reflection → Forecast → Decision** orders, with public statement vs secret orders (gap = deception metric), 3 options incl. one unconventional, matrix-style reasons.
6. **Red cell before adjudication** — strongest counter-arguments per action + one wildcard/novel move.
7. **Control quotes orders verbatim**, never invents player plans; probability bands; code rolls.
8. **Implementation lags** and **private accidents**.
9. **Endogenous alignment** — hidden AI dispositions sampled at setup/each generation, with odds and detection shifted by player safety investment.
10. **Villain fidelity** — brief misaligned AIs/bad actors with concrete incentives and procedures, not adjectives; track statement/order gaps.
11. **Model diversity** across roles; Control ≠ Critic model.
12. **Forks** at branch points rather than N≥20 seeds (cost), acknowledging single-run fragility.
13. **Hot-wash + backcasting**; Analyst ≠ Control; AAR claims cite trace/turn refs.
14. **Belief probes** — periodically ask actors what they think others know; compare to ground truth.
