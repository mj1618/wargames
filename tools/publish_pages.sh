#!/usr/bin/env bash
# Publish reports/index.html and the game reports to the gh-pages branch (GitHub Pages).
#   tools/publish_pages.sh
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'git -C "$root" worktree remove --force "$tmp" 2>/dev/null || true' EXIT
cd "$root"
git fetch -q origin gh-pages 2>/dev/null || true
if git show-ref --quiet refs/remotes/origin/gh-pages; then
  git worktree add -q -B gh-pages "$tmp" origin/gh-pages
else
  git worktree add -q --detach "$tmp"
  git -C "$tmp" checkout -q --orphan gh-pages
  git -C "$tmp" rm -rfq . 2>/dev/null || true
fi
find "$tmp" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
for f in reports/*.html; do
  [[ "$(basename "$f")" == _* ]] && continue
  cp "$f" "$tmp/"
done
if ls economy/reports/*.html >/dev/null 2>&1; then
  mkdir -p "$tmp/economy"
  for f in economy/reports/*.html; do
    [[ "$(basename "$f")" == _* ]] && continue
    cp "$f" "$tmp/economy/"
  done
fi
touch "$tmp/.nojekyll"
git -C "$tmp" add -A
if git -C "$tmp" diff --cached --quiet; then echo "gh-pages already up to date"; else
  git -C "$tmp" commit -q -m "Publish reports from $(git rev-parse --short HEAD)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
  git -C "$tmp" push -q origin gh-pages
  echo "published"
fi
