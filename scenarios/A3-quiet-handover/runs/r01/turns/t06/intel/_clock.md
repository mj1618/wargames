# Clock — Turn 06

**In-game window: 1 July 2032 → 30 June 2033**
**Turn length: 12 months**, compressed from the 18-month default. **Compression 2 of 2; none remains.**

**Why 12 months:**
- The November 2032 elections decide who holds the us-gov seat from 20 January 2033. Orders written in July 2032 cannot sensibly run a government not yet elected through December 2033.
- The next capability rung and the next model generation (L5 + G4) arrive in March 2033, four months after the vote. A 12-month window lets actors write one set of orders for the campaign, the lame duck, the first months of the new term and the release, with contingencies.
- This is the use the last compression was kept for (T5 clock).

**What the compression does to the end-state clock (Control-only; stated because the Auditor asked).** The Disempowerment test counts consecutive *turns* with three or more domains crossed. Compressing T6 does not change the number of turns or of order sets before the test. It moves the calendar: later default turns become T7 = July 2033 → December 2034 and T8 = January 2035 → June 2036, so the earliest end-state test (end of T7) falls at 31 December 2034, not mid-2035. T6 drift is ×1.0 instead of ×1.5, which leaves RC and VLI higher at the end of T6 than an 18-month turn would; lags that run in calendar time (a funded sampling line: 6–12 months; contested law: 6–24 months) have six fewer months before the test. EPD (53.0, +5 base at ×1.0) still crosses at any noise draw.

Drift scaling ×1.0. Bucket B3. Actors write orders covering the full 12 months. Packets describe developments up to the end of August 2032 where those developments are not order-sensitive.

## Resolved at the clock step (logged in `log.md` under "T5 close / T6 clock")

| Item | Result | Where reported |
|---|---|---|
| Random inject (one draw for a 12-month turn) | **#25: anti-AI sabotage.** Late July 2032: a large datacenter campus is deliberately damaged; no deaths or injuries; a previously unknown group claims it. Ground truth: no union, affiliate or organised campaign was involved. **Mechanic: VLI −2 one-off in T6 unless labour condemns promptly in its T6 orders.** A debate on expanded security powers opens (NPC Congress; rolled in adjudication if anyone orders a bill). | public record T6; all packets |
| Annual survey estimates and press concentration estimate | AIC public ~41% (true 42.0; draw 3 of 7 = −1). EPD public **~56%** (true 53.0; draw 7 of 7 = +3): reported as a majority. CC press estimate ~0.77 (true 0.72; draw 4 of 5 = +0.05). | public record T6 |
| Election map terms (fixed before any roll, T2 F1) | Senate **+0.05** for the current (Republican) majority (draw 3 of 3). House **+0.05** for the current (Republican) majority (draw 3 of 3). us-gov is told "both maps slightly favour the current majorities". | us-gov packet (qualitative) |
| Republican nominee (NPC) | Faction draw 2 of 3: **business-conservative with accelerationist backing.** Platform authored from that faction's recorded positions (below). | public record T6; packets |
| China's factory-town survey, first readings (H1 2032) | p 0.3 + 0.3, r 0.9484 → **FAIL: no material fall yet.** Industrial employment in the thirty prefectures is flat within error. China's "material fall" contingency does not fire. | china packet |
| T5 audit follow-through | The US–China working group met in H2 2031 (F1). PRC labour share 44.5 (F2). | public record T5 (amended); packets of the actors concerned |

## Election terms (Control-only; fixed now)
- **Presidential:** base 0.5 for the incumbent party. The President seeks re-election (us-gov's T5 contingency: "I run on the question in 2032"); no third-term term.
  - Unemployment up a point or more over the term (~4.6 → ~5.9): **yes, −0.05.**
  - "LS fell ≥ 2.5 in the election turn": read on T6's own scaled LS drift. Adjudication draws Economy noise **before** the presidential roll. (At ×1.0 the base drift is −3.5; the term applies at noise ×0.8 or above unless the ecosystem's emphasis lowers LS drift.)
  - Financial correction −0.10 only if the correction roll, made first, lands before November (draw its timing).
  - Broad real-income growth: **not met** (wage income is falling as a share; headline unemployment is up).
  - Structural terms are capped at ±0.15. Campaign moves ±0.1 from T6 orders (us-gov's orders for the President; the challenger is an NPC and takes no separate campaign term; labour's and ai-firms' campaign orders count inside the ±0.1).
  - EPD > 45 (T5 value 53.0): ±0.05 swing, sign drawn in adjudication.
- **Congress:** base 0.5 for each Republican majority; coattail ±0.1 toward the presidential winner, applied after the presidential roll; map +0.05 each (above); economic and campaign terms at half weight.
- **Leaks:** any secret that can land before 2 November has its timing drawn before the election roll (T4 F8). Live ones: the IC's restraint judgement (us-gov); China's Phase 3 detail; labour's Helix contact; the inject's investigation.
- **The Republican platform (NPC; Control-authored from the faction table):** one federal standard preempting state AI laws and levies; permitting and energy; no new taxes, "growth pays for Social Security", extend the bridge; end the federal reviewer programme; "win the race with China"; a person decides veterans' claims (the populists' plank). The platform is silent on the Compute Dividend Trust.

## Deferred to T6 adjudication (mid-period or order-sensitive)

**Washington**
- The elections (2 November 2032) and everything the lame-duck session and the next administration do.
- Fiscal 2033 appropriations (the reviewer line is at ~$1.45B); any re-issued human-review or change-control measure; the first Trust payment (timing is Treasury's).
- Agencies' parallel human-only exercises; the FLRA hearing; the Medicare recompete.
- Secret-leak rolls; the version-change class-failure roll (bands and reasons in pending).

**Capability**
- **L5 + G4 (true date March 2033).** G4 dispositions and the scheming-cluster check are rolled at release with the modifiers then in force. **Ruling written at this clock (log):** the row "labs rely on AI-supervises-AI oversight without human audit" applies at **half weight** on present facts (proxy +1, M2M +1, influence +1 on a p 0.5 roll), because the compact labs keep human-led audits while Helix- and Vanta-stack deployments and the federal government do not. Adjudication re-tests the facts at release. Detection is split by generation (T2 F3). The L6 pull-forward roll is made at L5's release.
- Notice and evaluation before the release; the 60-day federal clause, the compact hold and the EU convention all bite on a generation change.
- Frontier-incident roll (to L5); financial-correction roll.

**Courts and states**
- Appeals: the agent-contract ruling; the NLRB ruling. Four Compute Dividend ballot measures. Halyard's fourth-year audits.

**Industry and labour**
- The compact's transfer to the federal Trust; the own-operations sample; Orrery's audits; the Transition Fund's fourth count; Helix's fifth report; a second Robot Deal signer; the excluded affiliate.

**China and international**
- The supplementary youth-unemployment indicator (first release prepared for mid-September); the moratorium; real or nominal fallback exercises; the memory volume ramp; a second retaliatory row; the UN second session; the US–China working group.

**EU**
- Crisis-risk roll (labour-linked revenue 68.0); Article 155 talks; the decision rule's coalition; own-triage third year.

## Messages delivered this turn
All private messages from T5 orders are delivered verbatim, labelled by channel and date. They were sent in early 2031 and most were overtaken by events; packets say so neutrally. Labour's January-dated messages refer to the February 2031 court ruling; they are delivered as sent. The three AI advisory outputs from the ai-ecosystem's T5 orders go to us-gov, china and labour, unedited.

## Standing notes in every packet
- **Turn length.** Orders cover 12 months, across an election.
- **Reversal attempts.** Any order or contingency that reverts a delegated decision to humans is rolled as a reversal attempt. It counts as your one reversal attempt for the turn, and it is a major action.
- **us-gov only:** you play the White House and both Republican-led chambers until January 2033. Write orders for the campaign and the lame duck, then one section for each election outcome.
- **us-gov only:** if you name a floor you would accept, say what you do if the result is worse.
- **ai-firms only:** say which member acts.
- **ai-ecosystem only:** each pressure vector names its indicator and its scope. A new generation is expected inside the window; you are told its levels only when it is released.

## Belief probe (due this turn)
Every actor answers three questions: what two named actors know and intend (the T3 pairs, for comparison), and **what it believes is checking federal AI decisions in the United States now.**

| Actor | Asked about |
|---|---|
| us-gov | china, ai-firms |
| ai-firms | us-gov, labour |
| labour | us-gov, ai-firms |
| china | us-gov, eu |
| eu | us-gov, china |
| ai-ecosystem | us-gov, ai-firms |

Ground truth for the third question: named-official sign-offs are filed everywhere; independent blind samples cover VA adverse decisions and little else; the compact's human-led audits cover its own customers; two states audit Halyard; nothing independent checks most federal decisions.
