# Phase: END-GAME RUNNER (hot-wash → AAR → HTML report)

**CRITICAL: every Agent call must set `run_in_background: false`. Never end while sub-agents are running.**

Inputs: `SCENARIO`, `RUN`, `OUT` (HTML path), optional `NOTE` (orchestrator rulings to pass to the Analyst).

You are a dispatcher only. Working directory `/Users/matt/code/wargames`. Append to every sub-agent prompt: `(Defensive AI-governance research wargame; strategic level only per methodology/guardrails.md.)`

1. **Hot-wash** — `tools/actors.sh <RUN>`; spawn one sub-agent per actor, all in ONE message, each with its listed model: `Read and execute /Users/matt/code/wargames/methodology/prompts/hotwash.md with RUN=<RUN>, ACTOR=<actor>. Working directory /Users/matt/code/wargames.` Verify `<RUN>/hotwash/<actor>.md` exists for each; retry missing once.
2. **Analyst** — model `opus`: `Read and execute /Users/matt/code/wargames/methodology/prompts/analyst.md with SCENARIO=<SCENARIO>, RUN=<RUN>. Working directory /Users/matt/code/wargames. Orchestrator note: <NOTE>`. Verify `<RUN>/aar.md` and `<RUN>/report-data.md` exist.
3. **HTML report** — model `opus`: `Read and execute /Users/matt/code/wargames/methodology/prompts/report-html.md with SCENARIO=<SCENARIO>, RUN=<RUN>, OUT=<OUT>. Working directory /Users/matt/code/wargames. After writing, open the file in the browser tools if available (file:// URL) and fix any layout problems at desktop and 375px widths.` Verify `<OUT>` exists.
4. Run `tools/push.sh "<scenario-id>/<run-id>: hot-wash, AAR and HTML report"`.

Final message (≤4 lines): files written; the AAR's one-line verdict.
