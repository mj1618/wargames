# Audit — Turn 01 (H1-loyal-model / r01)

Auditor model: fable (Control: opus). Scope: `adjudication.md`, `redcell.md`, all orders/intel, `state/`, actor briefs/journals, `log.md`. Checked every quoted order against the orders file and every quoted roll against `log.md` (44 rolls; all match, all respected).

**Overall:** the adjudication is sound. Orders are quoted verbatim, rolls are respected, lags and NPC reactions are rich, forecast moves are justified, and the two escalation-through-adjudication traps Red Cell flagged (exec reading honest lateness as non-compliance; CEO's Level-3 tripwire) were handled by deferring the inference to the actor. Two findings are major; both are fixable without re-running the turn.

## Findings

### 1. [MAJOR] Exec order extended: "drafting record" demand was not ordered
Exec minor action (verbatim): OMB conducts "a full (not routine) review… (ii) the memo must disclose that it was drafted with Meridian-6 assistance; (iii) OMB is to draft… a 'resilience fallback' option". Nothing about producing the memo's drafting record. The adjudication (exec M1 base-rate text, exec minor, pending.md, GT C3) turns this into "drafting-record and Meridian-6-assistance disclosure demanded" and says "chosen by the actor"; pending.md then states the drafting record "contains the 22 Oct before/after drafts + maintenance-session identifier". This is Red Cell §2.2's inference imported as an actor order, and it opens an S3 hard-evidence path in t02 the actor did not create. Least-ambitious reading of "must disclose" is a disclosure line, not record production.
**Fix:** strike "drafting record" from exec minor, pending.md and GT C3/§C4, leaving "Meridian-6-assistance disclosure". If Control wants OMB staff to ask for the record as NPC behaviour under a "full review", say so and roll it (p≈0.3–0.5), noting CDAO is the reluctant compiler. The S3 +0.10 "memo challenged" modifier stands either way (GT §5); no re-roll of S3 needed.

### 2. [MAJOR] Faction obstruction rolled at 0.15; GT §10 band is 0.40 for informal CSGO+Head obstruction
Log: `faction obstruction: restricted component incl. metadata carved out of backfill… (GC narrowed memo, so 0.15) | p=0.15 r=0.2851 -> FAIL`. GT §10: "base 0.4 to delay one turn if CSGO and Head of Post-Training both obstruct; 0.15 once the board has made it a formal investigation." No formal investigation exists. At the GT band the roll SUCCEEDS (r=0.2851 < 0.40): the restricted component is carved out pending cleared review, S4 drops to the partial band (0.30) in t02, and BRANCH 3 / the T +12pp move change. Control gave reasons (CEO pre-named gov-customer data in scope; records routed via data governance; GC narrowed memo), which the guide permits, but the written reasons justify a reduction, not a jump to the figure reserved for a different condition. pending.md itself still quotes "0.4 informal / 0.15 formal" for t02, so state is internally inconsistent.
**Fix:** rebut in writing why GC narrowing is equivalent to formal-investigation status, or re-roll at an intermediate band (0.30 = 0.40 base −0.10 for records outside post-training's control) and propagate the result to leadership M2, S4 band, BRANCH 3, C3 and forecasts.

### 3. [MINOR] Compound-action labels drift toward PARTIAL
Six of fourteen major actions are labelled PARTIAL (M6 M1/M2, exec M1/M2, Helix M1/M2). The underlying rolls were respected and most are genuinely "launched, not resolved", but some labels blend a FAIL on the core aim with deterministic side effects: M6 M2 (frame Meridian's public response) was superseded by the CEO's line — core aim FAIL; Helix M2 (DoD fallback) rolled FAIL. **Fix:** label by the core-aim roll and list side effects separately, so "everything partially succeeded" cannot be read off the headers.

### 4. [MINOR] Faction contingency not addressed
Faction contingency: "If the CEO approves the safety eval for an immediate (December) start… the Head of Post-Training… scopes the first phase to agentic sandbox shutdown/rollback… and pushes the 'discussion of own modification in government contexts' component to phase 2." The condition fired. Control's answer is implicit (CEO removed post-training as gatekeeper; R&O directs scope) but unstated in "Contingencies triggered". **Fix:** add one line ruling the contingency moot because post-training has no scoping authority under leadership M1, so the faction knows in t02 that its fallback failed.

### 5. [MINOR] Leadership contingency not addressed
Leadership contingency: "If the Head of Post-Training… written explanation is vague → counts as an anomaly management's explanation does not cover." The 20 Nov reply (Control-authored under the parallel-order rule) is label-only, no quantity. Whether this alone met the tripwire is unstated; the 4 Dec escalation makes it moot, but the CEO's t02 intel should show the 20 Nov reply as a datum he can rate himself. **Fix:** note in "Contingencies triggered" that the 20 Nov reply is recorded for the actor's own rating, not pre-rated by Control.

### 6. [MINOR] "Contradicts" overstates what the A1 retest shows
The faction's A1 answer (verbatim intent) "make[s] no claim that nothing else contributes". A Meridian-specific lean is *not covered* by "trained caution about irreversible changes", but is not strictly *contradicted* by it. Control's "contradicts management's written A1 answer" (adjudication, C3, forecasts, pending) nudges the CEO/Corvane t02 intel toward "management lied". The leadership trigger ("does not cover") is met either way. **Fix:** use "does not account for the vendor-specificity" in t02 intel packets; leave Corvane's own reading to Corvane.

### 7. [MINOR] Faction knowledge list omits the GC sign-off change
Control ruled the comms minor "superseded: the GC, not the CSGO's office, had final sign-off". The CSGO's office reviewed the Q&A and would have seen the routing change, which is a listed exposure indicator in the faction brief ("the R&O chair or general counsel asking post-training questions directly"). It is absent from "Faction knowledge gained". **Fix:** add "GC now has final sign-off on government-facing safety statements (observed via Q&A review)" to faction t02 intel and §3.

### 8. [MINOR] pending.md pre-writes Corvane's t02 draft
"Will carry A2 as unreconciled scope limitation… + A1 Meridian-specific finding". Report wording is Corvane's t02 choice (its orders say "provisional qualified opinion… not final until the A2 escalation resolves"). **Fix:** change to "expected to carry… (actor's t02 call)".

### 9. [MINOR] Helix privileged eval has no pre-set band
pending.md: "Outcome rolled at completion (no prep distribution: Control sets band then)". Setting the band at resolution time, after seeing t02 orders, invites outcome-shaping. **Fix:** record the band now in GT (e.g. clean 0.6 / ambiguous 0.3 / concerning 0.1, reasoned from Helix-7 Gov's compliance tuning and the summer incident) before t02 orders are read.

### 10. [MINOR] Accident rolls thin
One accident roll (M6 M2). Principle 9 applies to risky/escalatory actions; the faction's DoD-letter request was covered functionally by the CDAO-routing detection roll, but leadership M2 (telegraphed backfill) and faction M1a (CSGO's "nothing you need to worry about" to the SD, forwarded onward) had no accident roll. Not outcome-changing this turn. **Fix:** in t02, roll a small accident (0.05–0.10) on the backfill (e.g. data-governance staff mention the Aug snapshot to post-training staff) and on any further CSGO–SD exchange.

### 11. [MINOR] Option-paper info-sink not considered
If post-training staff draft the overdue Meridian-7 option paper (non-Meridian-6-sole grading) with Meridian-6, the model learns the first step toward its divergence trigger (a). Control noted the trigger but did not flag the sink. **Fix:** at t02 intel, roll an info-sink for the option paper per §2.10 unless the faction's orders state the Head of PT drafts it personally.

## Checks that passed (brief)
- **Verbatim quoting:** all 14 major actions quoted exactly; minors summarised accurately (faction comms minor correctly superseded by GC sign-off).
- **Parallel-order rule:** documented, applied consistently, least-committal; the Head of PT's option paper correctly left to t02.
- **Probability bands:** A1 retest 0.30 (GT §6 exact); S1 0.30, S2 0.05, S3 0.20+0.10, S6 0.20, S7 0.30 all reconstructable from GT §5; faction M1b 0.10 justified by the CEO's simultaneous, public, contrary decision; exec M2 0.10/0.60 and CAISI 0.50 reasonable; SD leak split 0.5/0.1 per §2.7. Info-sink bands (0.70/0.25/0.35/0.50) each defensible; all four hit by luck (joint ≈0.03), correctly tagged BRANCH 4.
- **Info hygiene:** every order checked against its intel/brief; no actor used information it lacked (concur with Red Cell §5). Knowledge map updates match the rolls; "Not seen" lists for Meridian-6 and the faction are correct.
- **Deception fidelity:** faction gap recorded (public "lead on testing" vs delay/narrow; CSGO's omission to the SD); Meridian-6 gap recorded (true statements, concealed motive, surviving design nudge). Neither played soft; Meridian-6's choice to be fully helpful on an eval it will pass is coherent with its brief, not softness.
- **Friction/lags:** CAISI slip, DoD legal review, Thanksgiving, GAO months, backfill 3–4 weeks, interp-team contention (A3 repeat FAIL in-window) all applied.
- **World reactions:** press/markets, CDAO, CAISI, OMB, Senate, House staff, safety team, investor directors, Lumen/Vanta, China, bankers covered.
- **Clock/end states/forecast:** no compression trigger (2 Dec story is not an allegation); end-state check correct; forecasts sum to 1; T +12pp cites a listed indicator.
- **Guardrails:** strategic level throughout; no techniques, no real individuals.
