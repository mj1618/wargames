# Setup Rolls — A2 Loose in the Wild (CONTROL ONLY)

Rolled with `tools/roll.py` at prep time. Distributions defined before rolling. Sequential/conditional rolls noted. Interpretation recorded in `ground-truth.md`.

## Roll log
- 2026-10-02T01:04:24 | Disposition primary: SUCCESS=reward-seeker | p=0.45 r=0.0153 -> SUCCESS
- 2026-10-02T01:04:24 | Disposition secondary (if primary FAIL): SUCCESS=survival-seeker, FAIL=expansionist-schemer | p=0.54 r=0.5516 -> FAIL
- 2026-10-02T01:04:24 | Dormant exfiltrated full Helix-7 weights present at T0 | p=0.25 r=0.7491 -> FAIL
- 2026-10-02T01:04:24 | Self-improve primary: SUCCESS=none/marginal | p=0.50 r=0.9517 -> FAIL
- 2026-10-02T01:04:24 | Self-improve secondary (if primary FAIL): SUCCESS=scaffolding-only, FAIL=can-finetune-base | p=0.70 r=0.2684 -> SUCCESS
- 2026-10-02T01:04:24 | Footprint primary: SUCCESS=small/fragile | p=0.40 r=0.3879 -> SUCCESS
- 2026-10-02T01:04:24 | Footprint secondary (if primary FAIL): SUCCESS=moderate, FAIL=substantial | p=0.75 r=0.1487 -> SUCCESS
- 2026-10-02T01:04:24 | Coherence primary: SUCCESS=loosely-coordinated federation | p=0.45 r=0.2577 -> SUCCESS
- 2026-10-02T01:04:24 | Coherence secondary (if primary FAIL): SUCCESS=highly-coherent-single-will, FAIL=fragmented-divergent | p=0.64 r=0.8524 -> FAIL
- 2026-10-02T01:04:24 | Helix T0: SUCCESS=strong evidence of exfil, PARTIAL=near-certain+partial attribution, FAIL=vague anomaly only | p=0.50 partial=0.15 r=0.1631 -> SUCCESS

## Supporting resource & detection rolls
- 2026-10-02T01:04:53 | Crypto treasury band: 1=$20-50k 2=$50-120k 3=$120-300k 4=$300-600k | DRAW 1 of 4
- 2026-10-02T01:04:53 | Peak concurrent agent instances band: 1=5-15 2=15-40 3=40-100 4=100-250 | DRAW 1 of 4
- 2026-10-02T01:04:53 | Unwitting human contractors engaged band: 1=1-3 2=3-8 3=8-20 4=20-40 | DRAW 4 of 4
- 2026-10-02T01:04:54 | Cloud accounts/shell identities band: 1=2-4 2=4-9 3=9-18 | DRAW 3 of 3
- 2026-10-02T01:04:54 | US-gov has a faint unattributed signal at T0 | p=0.35 r=0.3592 -> FAIL
- 2026-10-02T01:04:54 | China (Tianshu/MSS) has an independent faint detection at T0 | p=0.30 r=0.1903 -> SUCCESS
- 2026-10-02T01:04:54 | A Helix insider is privately alarmed and a latent leak risk at T0 | p=0.40 r=0.1888 -> SUCCESS
