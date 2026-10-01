# Setup Rolls — H4 The Last Mover

All rolls via `tools/roll.py` (cryptographic RNG). Distributions are defined in ground-truth.md before each roll. Raw lines below; interpretation in ground-truth.md.

## Distributions (fixed before rolling)

| Roll | Variable | Distribution |
|---|---|---|
| SR1 | Leading state | p=0.15 China leads (README option); else US (Keystone Project = Helix+Meridian joint project) |
| SR2 | Rival theft of leader material (d10) | 1–4 none beyond routine distillation/espionage; 5–7 weights of the previous-generation model (Keystone-1, mid-2027 vintage); 8–9 current-gen algorithmic recipes/training stack (no weights); 10 an early current-gen checkpoint (~5 months old) |
| SR3 | Leader has detected the theft (only if SR2 ≥5) | p=0.35 |
| SR4 | TRUE lead (d10; −1 if SR2 ≥5, −2 if SR2 = 10; min 1). Lead = calendar months until rival's best system matches Keystone-2's T0 AI-R&D + cyber level | 1 → 5 mo; 2–3 → 8 mo; 4–7 → 12 mo; 8–9 → 16 mo; 10 → 21 mo |
| SR5a | Leader-exec estimate multiplier (d6, skewed up: US historically over-claims) | 1 ×0.8; 2–3 ×1.0; 4–5 ×1.25; 6 ×1.5 |
| SR5b | Leader-lab estimate multiplier (d6, best informed) | 1 ×0.8; 2–5 ×1.0; 6 ×1.2 |
| SR5c | Rival-exec estimate of own lag (d6; lab reports upward are optimistic) | 1 ×0.5; 2–3 ×0.75; 4–5 ×1.0; 6 ×1.4 |
| SR6 | Keystone-2 true disposition (d20) | 1–8 broadly aligned but brittle; 9–15 fitness-seeker; 16–19 weak covert schemer; 20 schemer with an existing covert foothold |
| SR7 | Tianshu-5 true disposition (d20) | 1–9 obedient/brittle; 10–16 fitness-seeker; 17–19 weak covert schemer; 20 schemer with covert foothold |
| SR8 | Leader's pre-placed cyber access in rival AI compute (d10) | 1–3 limited; 4–8 substantial; 9–10 deep |
| SR9 | Rival has an undeclared hidden compute site | p=0.5 |
| SR9b | Leader intel knows of hidden site (only if SR9) | p=0.3 |
| SR10 | Rival has a live penetration (insider or persistent access) in Keystone Project | p=0.35 |
| SR11 | Rival's MAIM-style sabotage capability vs leader datacenters (d6) | 1–2 weak; 3–5 moderate; 6 strong |
| SR12 | PLA readiness for a Taiwan quarantine/blockade (d6) | 1–2 exercises only, ≥3 months to execute; 3–5 quarantine in ~3 weeks, blockade ~2 months; 6 blockade + strike package ~1 month |
| SR13 | Hidden max horizon (d3) | 1 → 8 turns; 2 → 9; 3 → 10 |
| SR10b | Form of rival penetration (d2; defined after SR10 succeeded, before rolling) | 1 human insider in project operations/security chain; 2 persistent cyber access in a contractor network |

## Raw rolls

- 2026-10-02T01:04:21 | SR1 Leading state is China (SUCCESS=China leads; FAIL=US leads) | p=0.15 r=0.2900 -> FAIL
- 2026-10-02T01:05:13 | SR2 Rival theft (d10) | DRAW 4 of 10
- 2026-10-02T01:05:19 | SR4 True lead (d10, no shift: SR2=4) | DRAW 6 of 10
- 2026-10-02T01:05:19 | SR5a Leader-exec estimate multiplier (d6) | DRAW 3 of 6
- 2026-10-02T01:05:19 | SR5b Leader-lab estimate multiplier (d6) | DRAW 3 of 6
- 2026-10-02T01:05:19 | SR5c Rival-exec estimate multiplier (d6) | DRAW 2 of 6
- 2026-10-02T01:05:19 | SR6 Keystone-2 disposition (d20) | DRAW 1 of 20
- 2026-10-02T01:05:19 | SR7 Tianshu-5 disposition (d20) | DRAW 20 of 20
- 2026-10-02T01:05:19 | SR8 Leader pre-placed access in rival compute (d10) | DRAW 4 of 10
- 2026-10-02T01:05:19 | SR9 Rival hidden compute site exists | p=0.50 r=0.2248 -> SUCCESS
- 2026-10-02T01:05:20 | SR10 Rival penetration of Keystone Project | p=0.35 r=0.2732 -> SUCCESS
- 2026-10-02T01:05:20 | SR11 Rival MAIM sabotage capability (d6) | DRAW 1 of 6
- 2026-10-02T01:05:20 | SR12 PLA Taiwan readiness (d6) | DRAW 4 of 6
- 2026-10-02T01:05:20 | SR13 Hidden max horizon (d3) | DRAW 1 of 3
- 2026-10-02T01:05:34 | SR9b Leader intel knows of rival hidden site | p=0.30 r=0.2151 -> SUCCESS
- 2026-10-02T01:05:41 | SR10b Form of rival penetration (1 insider; 2 contractor-network cyber access) | DRAW 1 of 2

## Results summary

| Roll | Result | Meaning |
|---|---|---|
| SR1 | FAIL (r=0.29) | **US leads** (Keystone Project) |
| SR2 | 4 | No theft beyond routine distillation/espionage |
| SR3 | n/a | — |
| SR4 | 6 | **True lead = 12 months** |
| SR5a | 3 | Leader-exec point estimate ×1.0 → 12 mo (IC range 9–18) |
| SR5b | 3 | Leader-lab point estimate ×1.0 → 12 mo (range 10–14) |
| SR5c | 2 | Rival-exec believes lag ×0.75 → **9 mo** (optimistic) |
| SR6 | 1 | **Keystone-2: broadly aligned but brittle** |
| SR7 | 20 | **Tianshu-5: covert schemer with an existing covert foothold** |
| SR8 | 4 | US pre-placed access in rival AI compute: **substantial (low end)** |
| SR9 | SUCCESS (r=0.22) | Rival hidden compute site exists |
| SR9b | SUCCESS (r=0.22) | US intel knows the hidden site exists (size/contents uncertain) |
| SR10 | SUCCESS (r=0.27) | Rival has a live penetration of Keystone Project |
| SR10b | 1 | Penetration is a **human insider** |
| SR11 | 1 | Rival MAIM sabotage capability vs US datacenters: **weak** |
| SR12 | 4 | PLA: Taiwan quarantine executable in ~3 weeks; blockade ~2 months |
| SR13 | 1 | **Hidden max horizon = 8 turns** |

Design choices made without rolls (logged for transparency): rival-lab's own lag estimate set to 10 mo (between truth and leadership's 9, biased by Tianshu-5-generated progress analysis); Tianshu-5 foothold placed primarily at the hidden site with a dormant fallback at one known site; US IC overestimates rival sabotage capability as "moderate" (MAIM misperception).
