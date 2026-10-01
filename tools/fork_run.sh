#!/usr/bin/env bash
# Fork a run at the start of turn N (copies turns < N and the state snapshot saved at end of turn N-1).
#   tools/fork_run.sh H1-loyal-model r01 5 r01-f5-whistleblower
# Requires Control to snapshot state into turns/tNN/state-after/ at the end of each turn.
set -euo pipefail
scenario="$1"; src="$2"; turn="$3"; dst="$4"
root="$(cd "$(dirname "$0")/.." && pwd)"
sdir="$root/scenarios/$scenario/runs"
prev=$(printf 't%02d' $((turn - 1)))
[[ -d "$sdir/$src/turns/$prev/state-after" ]] || { echo "No snapshot at $src/turns/$prev/state-after" >&2; exit 1; }
[[ -e "$sdir/$dst" ]] && { echo "$sdir/$dst exists" >&2; exit 1; }

mkdir -p "$sdir/$dst/turns"
for t in "$sdir/$src"/turns/t*; do
  n=$((10#$(basename "$t" | tr -dc '0-9')))
  (( n < turn )) && cp -R "$t" "$sdir/$dst/turns/"
done
cp -R "$sdir/$src/turns/$prev/state-after/state" "$sdir/$dst/state"
cp -R "$sdir/$src/turns/$prev/state-after/actors" "$sdir/$dst/actors"
printf '# Run Log — %s / %s\n\nForked from %s at start of turn %s on %s\n\n## Rolls\n' \
  "$scenario" "$dst" "$src" "$turn" "$(date -u +%FT%TZ)" > "$sdir/$dst/log.md"
echo "Forked $src -> $dst at turn $turn"
