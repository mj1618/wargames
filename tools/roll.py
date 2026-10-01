#!/usr/bin/env python3
"""Adjudication dice. Probability is decided *before* rolling; this just resolves it.

  roll.py 0.35 --label "Lab B detects backdoor" --log scenarios/H1/runs/r01/log.md
  roll.py 0.6 --partial 0.15     # SUCCESS if r<p, PARTIAL if r<p+partial, else FAIL
  roll.py --draw 12              # draw a random inject 1..12
"""
import argparse
import datetime
import secrets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("p", nargs="?", type=float, help="probability of success (0-1)")
    ap.add_argument("--partial", type=float, default=0.0, help="extra band above p that yields PARTIAL")
    ap.add_argument("--draw", type=int, help="draw an integer 1..N instead")
    ap.add_argument("--label", default="")
    ap.add_argument("--log", help="append result to this markdown file")
    a = ap.parse_args()

    if a.draw:
        result = f"DRAW {secrets.randbelow(a.draw) + 1} of {a.draw}"
    else:
        if a.p is None or not 0 <= a.p <= 1:
            ap.error("p must be in [0,1]")
        r = secrets.randbelow(10_000) / 10_000
        outcome = "SUCCESS" if r < a.p else "PARTIAL" if r < a.p + a.partial else "FAIL"
        band = f" partial={a.partial:.2f}" if a.partial else ""
        result = f"p={a.p:.2f}{band} r={r:.4f} -> {outcome}"

    line = f"- {datetime.datetime.now().isoformat(timespec='seconds')} | {a.label} | {result}"
    print(line)
    if a.log:
        with open(a.log, "a") as f:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
