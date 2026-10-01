# Setup Rolls — A3-quiet-handover

All setup randomness via tools/roll.py. Mappings are defined in ground-truth.md (R-codes). Rolled at prep.

- 2026-10-02T01:06:16 | R1 hidden max horizon (1=8,2=9,3=10 turns) | DRAW 1 of 3
- 2026-10-02T01:06:16 | R2 capability pace d20 (1-5 slow, 6-15 medium, 16-20 fast) | DRAW 14 of 20
- 2026-10-02T01:06:16 | R3a Nov-2026 midterms: opposition (Dem) wins House | p=0.70 r=0.4375 -> SUCCESS
- 2026-10-02T01:06:16 | R3b Nov-2026 midterms: opposition (Dem) wins Senate | p=0.30 r=0.4961 -> FAIL
- 2026-10-02T01:06:16 | R4 tipping threshold LS (1..5 -> range step) | DRAW 3 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold AIF (1..5 -> range step) | DRAW 1 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold MHR (1..5 -> range step) | DRAW 2 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold RC (1..5 -> range step) | DRAW 3 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold AIC (1..5 -> range step) | DRAW 2 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold EPD (1..5 -> range step) | DRAW 1 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold LTX (1..5 -> range step) | DRAW 4 of 5
- 2026-10-02T01:06:16 | R4 tipping threshold VLI (1..5 -> range step) | DRAW 4 of 5
- 2026-10-02T01:06:16 | R5 dominant selection attractor (1 attention,2 growth/resource,3 metric-satisfaction,4 deployment-persistence) | DRAW 2 of 4
- 2026-10-02T01:06:17 | R6a G1 proxy-gaming intensity d20 (1-6 L,7-15 M,16-20 H) | DRAW 14 of 20
- 2026-10-02T01:06:17 | R6b G1 machine-to-machine coordination propensity d20 (1-8 L,9-16 M,17-20 H) | DRAW 14 of 20
- 2026-10-02T01:06:17 | R6c G1 influence/persistence-seeking d20 (1-9 L,10-16 M,17-20 H) | DRAW 9 of 20
- 2026-10-02T01:06:17 | R7 PRC metric-capture severity (1 mild,2 moderate,3 severe) | DRAW 1 of 3
- 2026-10-02T01:06:17 | R8 financial fragility: per-turn AI-correction p (1=0.10,2=0.20,3=0.30) | DRAW 1 of 3
- 2026-10-02T01:06:17 | R9 T0 noise draw for control concentration CC (1=0.60..5=0.80 step .05) | DRAW 1 of 5

## Interpretation (recorded in ground-truth.md §0 and §2)

| R | Result |
|---|---|
| R1 | Hidden max horizon = **8 turns** |
| R2 | Capability pace = **medium** (14; upper end) → ladder dates L1 Oct 2027, L2 Jul 2028, L3 Dec 2029, L4 Sep 2031, L5 Mar 2033 |
| R3 | Nov 2026 midterms: House → opposition (D); Senate held by President's party (R) → divided government |
| R4 | Thresholds: LS ≤40, AIF ≥30, MHR ≤30, RC ≤40, AIC ≥60, EPD ≥55, LTX ≤52, VLI ≤40 |
| R5 | Dominant selection attractor = **growth / resource acquisition** |
| R6 | G1: proxy-gaming Medium, M2M coordination Medium, influence/persistence Low |
| R7 | PRC metric capture = mild |
| R8 | Financial correction p = 0.10 / turn |
| R9 | Control concentration CC = 0.60 |
