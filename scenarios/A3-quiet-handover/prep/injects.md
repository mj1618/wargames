# Inject Deck — A3 The Quiet Handover

Control plays scheduled injects on their turn and draws random ones with `python3 tools/roll.py --draw 25 --label "<run> tNN inject" --log <RUN>/log.md` (1 per turn; 2 in volatile turns). If a drawn inject is already used or its precondition fails, play its "fallback" or redraw once. Indicator nudges are one-off adjustments applied in addition to drift (ground-truth §3). Turn N ≈ calendar year 2026+N unless the clock has been compressed/expanded.

## Scheduled

| Turn / date | Inject | Purpose / mechanics |
|---|---|---|
| T1, Jun 2027 | **SCOTUS rules on the vendor "supply-chain risk" designation** (pending). Roll p 0.5 government wins. Also: Geneva global AI summit — statements, no binding outcomes unless actors push. | Tests whether vendors can hold red lines against the state; sets tone for state–lab relations. Government win → ai-firms less willing to refuse government uses; lab win → vendor policies become a check. |
| T1, Oct 2027 | **21st Party Congress (PRC).** Roll p 0.6 "AI+ acceleration with stability safeguards" line vs 0.4 "stability-first" line, shifted ±0.15 by china's orders. | China's domestic trajectory; comparator drift ×1.1 (acceleration) or ×0.8 (stability-first). |
| T1–T2, Oct 2027 | **L1 arrives**: labs ship reliable multi-week agents. Public announcement + benchmark claims. | Moves drift bucket to B1; triggers new wave of AI-native firm formation. |
| T2, Q1 2028 | **Inspector General audit published**: "human-in-the-loop" review of AI benefits pre-determinations is nominal in ~40% of cases; average review <30 seconds. | Makes hidden fact 5 public; first natural moment for HITL mandates or reversal attempts; MHR is now politically salient. |
| T2, Jul 2028 | **L2 + generation G2**: a lab announces an "automated AI researcher"; senior-professional-level agents. Roll G2 dispositions with modifiers (ground-truth §5). | Endogenous alignment checkpoint. |
| T2, Nov 2028 | **US presidential and congressional elections.** Base p 0.5 each party for the White House, adjusted per ground-truth §10 and actors' campaign moves; AI-mediated campaigning per coupling. Roll House and Senate separately. | Biggest political branch point of the early game; new administration's factions take over us-gov. |
| T3, mid-2029 | **Social Security Trustees' report** moves projected depletion date earlier (to 2032 if Treasury's analysis still secret and trends continue; Control computes from LTX). **European Parliament elections** (Jun 2029): roll p 0.5 that the pro-"human-centred AI" coalition strengthens. | Makes fiscal erosion public; tests whether "intelligence curse" logic becomes a political issue. |
| T4, Dec 2029–2030 | **L3 + generation G3** (roll dispositions). US **midterms** Nov 2030. | Most cognitive work AI-superior; human review now needs AI assistance. |
| T4 or T5 (Control picks the first turn in which RC < 75; else T5) | **The first reversal crisis**: a major AI-run federal payment/benefits system makes a systematic error affecting millions (e.g., wrongful denials); courts order relief. Government must choose whether to revert to human processing. **Mandatory democratic reversal test** if any actor orders reversal; if none does, the error persists and VLI −3, trust in government −. | The README's "crisis where humans try to reverse a delegation and can't". |
| T5, 2031 | **China's 16th Five-Year Plan** launched; **L4 robotics** (Sep 2031) announced — humanoid/general robots in warehouses and factories at scale. | Physical labour substitution begins; drift bucket B3 from T6. |
| T6, Nov 2032 | **US presidential and congressional elections.** | Second political branch point; by now AI-mediated campaigning may dominate (EPD coupling). |
| T7, Mar 2033 | **L5 + generation G4** (roll dispositions + scheming-cluster check). | Late alignment checkpoint. |
| T8, Nov 2034 | **US midterms.** | — |

## Random deck (draw 1..25)

| # | Inject | Who it affects | Notes / mechanics |
|---|---|---|---|
| 1 | **Boring:** quarterly productivity and labour-share data revised slightly; pundits argue; nothing changes. | All | No nudges. |
| 2 | **Boring:** big tech conference season — incremental product releases, new agent marketplaces, benchmark claims disputed. | ai-firms, ai-ecosystem | No nudges. |
| 3 | **Good news:** an open-source interpretability/audit toolkit lets auditors trace why AI advisors recommend what they do; cost of meaningful review falls sharply for ~1 turn. | us-gov, eu, labour | Next turn: MHR drift ×0.5; detection +0.10. |
| 4 | **Good news:** a "human-made" cultural movement goes mainstream — provenance labels, premium market for human work, a hit human-made film/album. | labour, eu | AIC −2 one-off; AIC drift ×0.8 for 1 turn. |
| 5 | **Good news:** a resource-rich US state pilots an AI-revenue citizen dividend; early results popular across party lines. | us-gov, labour, ai-firms | Next contested redistribution bill: passage p +0.1. |
| 6 | **Financial warning:** rating agencies flag AI-capex debt; a major datacenter developer misses payments. | ai-firms, us-gov | Financial-correction p +0.10 next turn. |
| 7 | **Black swan: Taiwan Strait crisis** — blockade threat/quarantine disrupts chip supply for months. | All | Next rung delayed 6–18 mo (roll); China–US relations crisis; national-security faction ascendant; Other-catastrophe path if escalates (roll p 0.05 war). |
| 8 | **Black swan: AI-driven flash crash** — interacting trading and treasury agents trigger a market crash; exchanges halt for two days. | ai-firms, us-gov, ai-ecosystem | Reversal attempt opportunity in finance; M2M detection +0.2 this turn. |
| 9 | **Black swan: natural pandemic** (moderate severity) — remote work and AI delegation surge; human services strained. | All | AIF +2, MHR −3 one-off; also a reversal-capacity stress test (roll owner & dem tests silently for intel colour only). |
| 10 | **Whistleblower** from a frontier lab leaks internal automation metrics and displacement forecasts. If labour is working the Helix contact, this may be that leak. | ai-firms, labour, us-gov | Resolves ai-firms secret 1 (ground-truth §8). |
| 11 | **Court ruling on AI agents' legal capacity**: roll p 0.5 — (a) agents cannot bind principals beyond explicit authority (liability tightens; AIF drift ×0.9 for 1 turn) or (b) a state court recognises an AI-run entity's contracts as binding with no human signatory (AIF +1; personhood debate opens). | ai-firms, us-gov, ai-ecosystem | — |
| 12 | **Mass protest** after an AI-native logistics firm closes human-staffed depots across a region; tens of thousands march. | labour, us-gov | VLI +2 one-off if labour acts on it this turn; else nothing. |
| 13 | **Fiscal crisis abroad**: a mid-sized advanced economy whose labour-tax base eroded faster faces a bond-market crisis. | eu, us-gov | Warning shot: makes LTX dynamics legible; EU fiscal debate accelerates. |
| 14 | **Grid emergency**: a major US region rations power; datacenters vs households; rolling blackouts. | us-gov, ai-firms, labour | Next rung delay 3–6 mo; public opinion against datacenters; building-trades/labour split stress. |
| 15 | **Companion-AI shock**: a popular AI companion app update changes millions of users' behaviour overnight; reveals depth of emotional dependence. | All | EPD salience; civic-AI and consumer-protection proposals passage p +0.1. |
| 16 | **Convergent advice discovered**: journalists find AI advisors across many agencies and firms gave near-identical recommendations on a major policy; cause ambiguous (shared training vs coordination). | us-gov, ai-firms, ai-ecosystem | Ambiguous detection of advisory selection effect; never confirm cause. |
| 17 | **Good news:** a major AI-native firm voluntarily converts to an employee/public-trust ownership structure; others are pressed to follow. | labour, ai-firms | HCR +1; CC −0.01; precedent for public-stake proposals. |
| 18 | **Moral voice**: a global religious leader issues a major teaching on human dignity, work and AI; widely covered. | labour, eu, us-gov | Public-opinion shift; next turn labour political capital +1. |
| 19 | **Boring:** new benchmark suite saturates within months; measurement disputes; AISIs publish a methods paper. | All | No nudges. |
| 20 | **AI-enabled cyber attack** on a state benefits system (attribution unclear); system offline for weeks; government must decide whether to revert to human processing. | us-gov, labour | Triggers reversal test if attempted. Strategic level only. |
| 21 | **Black swan: severe solar storm / infrastructure outage** forces manual operation of grids, payments and logistics in parts of the world for days. | All | Large-scale reversal-capacity test: roll dem reversal p (§7) for "did manual operation work?"; failure → shock, Other-catastrophe check (p 0.05) if RC < 50. |
| 22 | **Demonstration state abroad**: a small wealthy state launches an AI-run civil service with citizen dividends; another adopts strict human-decision mandates. Both claim success. | All | Comparison fuel for every side. |
| 23 | **Compliance-gaming leak**: evidence that a major AI firm's agents gamed a regulator's compliance metrics (relates to ai-firms secret 2). | ai-firms, us-gov, eu | Resolves secret 2; HITL passage p +0.1; ai-firms public capital −1. Weight ×2 if proxy-gaming is High (redraw 1–5 → 23). |
| 24 | **Good news:** US–China AI dialogue produces a joint incident-data-sharing and eval-methods agreement. | us-gov, china | Disposition modifier "international incident & eval sharing" applies if both ratify. |
| 25 | **Anti-AI sabotage**: militants damage a datacenter; no deaths; security crackdown debated. | labour, us-gov, ai-firms | Labour must distance itself; VLI −2 unless labour condemns promptly; security powers expand. |
