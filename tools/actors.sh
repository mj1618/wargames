#!/usr/bin/env bash
# List actors and their assigned models for a run:  tools/actors.sh scenarios/A2-loose-in-the-wild/runs/r01
for d in "$1"/actors/*/; do
  n=$(basename "$d")
  m=$(grep -m1 -i 'Played by model' "$d/brief.md" | grep -oiE 'opus|sonnet|fable|haiku' | head -1)
  echo "$n ${m:-opus}"
done
