#!/usr/bin/env bash
# tools/turn_status.sh <run-dir> <TT>  — which phase files exist for a turn
r="$1"; t="t$2"
echo "actors: $(ls "$r/actors" | tr '\n' ' ')"
echo "orders: $(ls "$r/turns/$t/orders" 2>/dev/null | sed 's/\.md//' | tr '\n' ' ')"
for f in redcell adjudication audit sitrep; do [[ -f "$r/turns/$t/$f.md" ]] && echo "$f: yes" || echo "$f: no"; done
