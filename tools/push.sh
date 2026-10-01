#!/usr/bin/env bash
# tools/push.sh "<message>"  — commit everything and push (retries on lock/reject)
cd "$(dirname "$0")/.."
for i in 1 2 3; do
  git add -A && git commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" 2>/dev/null
  git push -q 2>/dev/null && exit 0
  git pull -q --rebase 2>/dev/null; sleep 2
done
echo "push failed" >&2; exit 1
