#!/usr/bin/env bash
# Scaffold a run from a prepped scenario.
#   tools/new_run.sh H1-loyal-model r01
set -euo pipefail
scenario="$1"; run="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
sdir="$root/scenarios/$scenario"
rdir="$sdir/runs/$run"
[[ -d "$sdir/prep" ]] || { echo "No prep/ in $sdir — prep the scenario first" >&2; exit 1; }
[[ -e "$rdir" ]] && { echo "$rdir exists" >&2; exit 1; }

mkdir -p "$rdir/state" "$rdir/actors" "$rdir/turns"
cp "$sdir/prep/ground-truth.md" "$rdir/state/ground-truth.md"
printf '# Public Record — %s / %s\n\n' "$scenario" "$run" > "$rdir/state/public-record.md"
printf '# Forecasts — %s / %s\n\n' "$scenario" "$run" > "$rdir/state/forecasts.md"
printf '# Run Log — %s / %s\n\nStarted %s\n\n## Rolls\n' "$scenario" "$run" "$(date -u +%FT%TZ)" > "$rdir/log.md"
for f in "$sdir"/prep/actors/*.md; do
  name="$(basename "$f" .md)"
  [[ "$name" == _* ]] && continue
  mkdir -p "$rdir/actors/$name"
  cp "$f" "$rdir/actors/$name/brief.md"
  printf '# Journal — %s\n\n' "$name" > "$rdir/actors/$name/journal.md"
done
echo "Created $rdir"
