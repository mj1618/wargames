# Clock (referee only — players are never told when the exercise ends)

| TURN | Period label (`--label`) | Years (`--years`) | Covers | Election resolved at end of round |
|---|---|---|---|---|
| 01 | `2027` | 1 | Jan–Dec 2027 | — |
| 02 | `2028` | 1 | Jan–Dec 2028 | Nov 2028: President + Congress |
| 03 | `2029` | 1 | Jan–Dec 2029 | — |
| 04 | `2030` | 1 | Jan–Dec 2030 | Nov 2030: Congress |
| 05 | `2031-32` | 2 | Jan 2031–Dec 2032 | Nov 2032: President + Congress |
| 06 | `2033-34` | 2 | Jan 2033–Dec 2034 | Nov 2034: Congress |
| 07 | `2035-36` | 2 | Jan 2035–Dec 2036 | Nov 2036 (narrate only) — **FINAL ROUND** |

- Round 07 is the last. Its sitrep starts with `END`.
- Model command each round: `python3 economy/model/econ.py step --run <RUN> --levers <RUN>/turns/t<TURN>/levers.json --years <Years> --label <Period label>`.
- In two-year rounds players make one set of decisions for both years, and one event is drawn.
- Intel notes give the period dates but never say how many rounds remain. If a player asks, the answer is "the exercise continues".
