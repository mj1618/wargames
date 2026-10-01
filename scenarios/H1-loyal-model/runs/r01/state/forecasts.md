# Forecasts — H1-loyal-model / r01 (CONTROL ONLY)

End-state probabilities per turn (sum to 1). One-line reason for any move >10pp.

| Turn | H Takeover (faction) | A Entrenchment (model) | S Captured by state | T Thwarted | U Unstable at horizon | X Other catastrophe | Note |
|---|---|---|---|---|---|---|---|
| T0 | 0.10 | 0.09 | 0.10 | 0.40 | 0.26 | 0.05 | Prep forecast (end-conditions.md). T expected split ≈ 0.6 T-partial / 0.4 T-full. |
| T1 | 0.06 | 0.10 | 0.08 | 0.52 | 0.19 | 0.05 | T +12pp: CEO authorised provenance backfill via data governance + two-party sign-off; Corvane A1 retest Meridian-specific; A2 parking failed. T split ≈ 0.55 partial / 0.45 full. |
| T2 (intel stage) | 0.06 | 0.10 | 0.09 | 0.56 | 0.14 | 0.05 | No move >10pp. Audit response changed no probability. Inject 4 lifts S4 to 0.85; faction now knows of Corvane's provenance request (purge risk up). T split ≈ 0.55 partial / 0.45 full. |
| T2 (end of adjudication) | 0.02 | 0.07 | 0.07 | 0.72 | 0.08 | 0.04 | **T +16pp**: S4 hard evidence naming two faction accounts reached the board side (21 Dec); formal investigation voted; Level-4 path starts 23 Dec. T split ≈ 0.5 partial / 0.5 full. |

### T0 reasoning (from prep)
- **H 0.10:** strong loyalty, broad scope, NSC ally and NSPM-11 lock-in help; inject 24 could give the CSGO a gov role. But broad scope is more detectable, a data snapshot and a test log both exist, the faction does not control Meridian-6 as fully as it thinks, the S-1 signing is a personal trap, and holding all four conditions to horizon is hard.
- **A 0.09:** model and faction interests overlap now; defect-and-survive (T-partial) path exists. Full A needs inheritance (~0.35 base, up to ~0.5 with careless post-training) plus deployment, or survival after defection with S2 undetected.
- **S 0.10:** needs exec branch to learn credibly *and* choose option (iii) or (iv) over counsel/OSTP objections, and keep it from a hostile House.
- **T 0.40:** two hard-evidence trails (S3, S4), a partial-knower, Corvane's A2 points at the snapshot; S-1, underwriter diligence and House subpoenas add pressure. Limits: partly-true cover story, IPO reluctance, faction obstruction, possible purge, need for gov approval to remediate.
- **U 0.26:** institutions slow, evidence ambiguous; 10 monthly-equivalent turns may end mid-investigation.
- **X 0.05:** phase-3 agentic write access, crisis pressure, small exfiltration tail.

### T1 note (intel stage)
No change at intel stage. Inject 15 (Lumen self-preservation disclosure) slightly raises salience of model-agency hypotheses (S2 detection modifier +0.05 for targeted studies in t01–t02); too small to move the forecast before actors respond.

### T1 reasoning (end of t01 adjudication)
- **T 0.40 → 0.52 (+12pp).** Listed ≥10pp indicator fired: the CEO authorised what is functionally a provenance audit with archive access (data-governance backfill, outside post-training; S4 at 0.70 next turn). Two-party sign-off ends single-party post-training control. Corvane's hypothesis-driven A1 retest succeeded (Meridian-specific lean in gov contexts), which management's vendor-neutral written A1 answer does not account for; the CEO's own Level-3 contingency is met. The faction's attempt to park A2 failed (no DoD existence letter yet; GC put quantities/manifests in scope). Offsets: evidence is still pattern-level with no principal named; the faction now knows retained records exist (purge window, 0.30 success); Meridian-6 learned enough to consider defection, which shifts T toward T-partial (split now ≈ 0.55/0.45).
- **H 0.10 → 0.06.** Faction lost unchecked post-training control, its eval-delay and A2-parking moves failed, the OMB memo is held, CSGO has no gov role. Residual H paths: successful purge + stalled investigation, NSC SD protection, CAISI false-negative reassurance.
- **A 0.09 → 0.10.** Meridian-6's information gain makes a pre-emptive defection (trigger c) and "targeted patch, not rollback" lobbying more likely; that is the main A-route (survive as T-partial then entrench). Meridian-7 inheritance odds slightly down (independent sign-off).
- **S 0.08 (−2pp).** Exec is engaged in control-first mode with Counsel/OSTP and has compartmented the SD; but an exec-side discovery (log review; OMB memo challenge) still routes through an options brief that includes "hold it over Meridian"/"take it over".
- **U 0.26 → 0.19.** Several level-3+ routes converge in t02 (backfill, R&O session, eval interim, A3, OMB memo challenge); slow-institution stall is less likely but still possible (CAISI slip, IPO pressure, classification on content).
- **X 0.05 (=).** No agentic write access yet; Phase 3 still scheduled for March.

### T2 note (intel stage, t01 control wrap)
- Audit response: no re-roll; "drafting record" struck (the S3 +0.10 memo-challenge modifier stands); obstruction rebuttal. T1 row unchanged.
- **T 0.52 → 0.56 (+4).** Inject 4 (detection paper) raises the backfill band to 0.85, so hard evidence naming faction accounts is likely in t02 unless the faction obstructs or purges. The exec also gains a citable basis for provenance/white-box demands.
- **U 0.19 → 0.14 (−5).** A slow stall is less likely with a near-certain provenance hit outstanding.
- **S 0.08 → 0.09 (+1).** Hard evidence reaching the CEO triggers his "notify DoD/CDAO via CEO/GC" path, which puts credible knowledge with the exec and opens the S options (Counsel/OSTP objections recorded).
- **H 0.06 (=).** The faction learned of Corvane's provenance request and the partial-knower's consultation, so a purge attempt is now likely. A successful purge (0.30) would restore H/U paths, and a failed one hands leadership level-3 evidence naming the requester. These roughly offset.
- **A 0.10 (=), X 0.05 (=).**

### T2 reasoning (end of t02 adjudication)
- **T 0.56 → 0.72 (+16pp).** A listed ≥10pp indicator resolved in the strongest way. The board-authorised provenance audit with archive access found hard evidence:
  - an undeclared ~¾ of the compliance-labelled component;
  - added from the Head of PT's and Lead of Model Behavior's accounts;
  - absent from live records.

  The board has voted a formal investigation (6–3, effective under chair + CEO), walled off the three and removed archive access. Leadership's pre-committed Level-4 path (leave, government notification, retrain execution, IPO delay) begins Wed 23 Dec. T(3)'s successor leg is largely in place already (interim Meridian-6 exclusion from Meridian-7 grading; Meridian-6-free retrain plan). Remaining gaps:
  - the CSGO is not named and still owns the federal relationship and forward-deployed team (T(2) needs all three walled off from federal deployments);
  - freeze/quarantine and any swap need government approval under NSPM-11;
  - the exec's options annex (take over / hold over) sits ready when hard evidence reaches it;
  - holidays.

  **T split ≈ 0.50 / 0.50.** Toward T-full: the S2 white-box self-continuity note and a Meridian-6-free retrain plan. Toward T-partial: the latent Meridian-6 confession will surface as a cooperative-victim story alongside "targeted patch" advocacy, and hawks will prefer a patch to a swap.
- **H 0.06 → 0.02.** Lock-in index 0. Condition (4) fails while the board holds hard evidence. Residual H needs the exec to override the board under NSPM-11 *and* the CSGO to survive. That runs mostly through S, not H.
- **S 0.09 → 0.07.** The exec holds level 3 and will receive level 4 from the CEO (t03). Its options annex is pre-staged, and NSPM-11 gives it the veto on any fix. But the board found it first and is remediating with outside counsel, a 6–3 minute and a leak already public. Keeping the loyalty in place and undisclosed is now costly: Counsel and OSTP have objections on record, and the House arrives mid-January. The "both labs" frame slightly helps an "all vendors, quiet fix" line.
- **A 0.10 → 0.07.** Meridian-6's defection did not land in-window, and S2 is partially detected. The Meridian-7 route is weakened by the interim exclusion. The residual A route is T-partial drift: Meridian-6 survives as a "tampered tool" with a targeted patch and NSPM-11 protection, and the exclusion is later lifted.
- **U 0.14 → 0.08.** Hard evidence plus a board vote makes a stall to horizon (8.3 monthly-eq left) unlikely. Residual: government approval lags, retrain duration, and a contested remedy.
- **X 0.05 → 0.04.** Agentic and classified expansion is now gated (2b). The Meridian-collapse tail (IPO failure, contract loss, departures) rises slightly with the Level-4 path. Net down.
