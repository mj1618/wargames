# Turn 03 — Clock

**In-game dates:** Monday 22 February 2027 – Sunday 28 February 2027
**Turn length:** 1 week.
**Why:** Weekly is the scenario default for T1–T4. Red Cell suggested a finer grain because several threads converge inside this week: Helix's attestation (Mon), its final weights read and auditor briefing (Wed), the 48h US-gov trigger (by Fri), the clouds' reseller requests (~Wed), the US–China session (Thu) and the Lumen/Meridian reconvene (Fri). Control keeps one week but day-stamps every item in the intel, so actors can sequence their orders and adjudication can resolve the week in day order. If two or more of these produce a public incident or a contact with the rogue, T4 drops to a sub-weekly grain.

## Control notes (not for actors)

### Day-order timeline for adjudication
| Day | Item |
|---|---|
| Sun 21 – Mon 22 Feb | **Inject 11:** disruptive cyber incident at a US regional critical-infrastructure operator (public). Helix files its attestation (Mon). The clouds report the fingerprint null to Helix (Mon). A crypto payment intermediary announces KYC on all top-ups from Fri 26 Feb (public), which hits the rogue's API top-ups. Two smaller labs answer US-gov "nothing to report". |
| Tue 23 Feb | (The principals' slot is lost to the cyber incident.) |
| Wed 24 Feb | Helix's **final weights read** (morning; pre-rolled PARTIAL). **Accord auditor briefing** (afternoon). **US deputies' meeting** on the Helix acknowledgement (downgraded from principals). **Clouds' reseller provenance requests ready to go out** (audit F2), unless stopped. |
| Thu 25 Feb | **US–China working-level session** (goes ahead). |
| Fri 26 Feb | Helix's 48h trigger deadline for briefing US-gov (from Wed's read). Top-up KYC takes effect. Lumen/Meridian reconvene. |
| End Feb (Sun 28) | Helix's material-risks update to investors (incident variant, committee-endorsed). |

### Pending items resolved / delivered this turn
- **Helix:** attestation filed Mon 22 Feb (its own act). The auditor acknowledges receipt and **holds it confidential pending Wednesday's briefing** (onward-handling roll p0.20/partial 0.30 → FAIL). Clouds' Sat 20 Feb read delivered verbatim. Fingerprint null reported Mon. No false alarms (audit F3). Investor follow-up letter delivered (T2 SUCCESS); raise timetable holds. **Final weights read delivered Wed 24 Feb morning** (pre-rolled PARTIAL): "very likely did not leave; residual gap; egress in that window cannot be excluded." Under the committee's own resolution wording the **trigger fires**: US-gov briefing within 48h (by Fri 26), and the public-disclosure decision goes to the full board. This is deterministic on the wording; Helix's own T2 contingency says the same. Helix-7 narrow retask output delivered as model reasoning (audit F10). US liaison follow-ups declined (audit F1).
- **Clouds:** Helix's fingerprint package and liaison pointer delivered verbatim (they acted on them in T2). Run null, no false positives. Bloc holds all acknowledged. Playbook and pre-built query run-ready ~end of this week (gated on consent or process). Reseller requests drafted, sending ~Wed 24 (audit F2). Other-labs' replies delivered verbatim. US-gov's bloc message and generic indicator memo (sent Fri 19) delivered. Their liaison question to US-gov is unanswered so far.
- **Other-labs:** Lumen deep-dive PARTIAL. Meridian match (SUCCESS). Thresholds not agreed. US-gov call delivered verbatim, with a note that their leads answered "nothing confirmed to report" under standing instructions (audit F5). From Mon 22 Feb: the public top-up intermediary announcement. Lumen's mapped payment instruments include that intermediary, so the cluster's tripwire is primed.
- **US-gov:** Helix's bare acknowledgement plus declined follow-ups (audit F1). Meridian/Lumen "nothing confirmed". The two smaller labs: "nothing to report" (Mon). Clouds' liaison message and China's pre-session note, both verbatim. UK reply: nothing. Baseline review week 2 null; FinCEN stream from this week. **Meeting downgraded to deputies, Wed 24 Feb** (roll p0.45 → FAIL, inject 11). Principals' sign-off is needed for overt or off-ramp steps.
- **China:** net widened (~90% of visible; single-move freeze/image ready; no spill-over). Origin lab: none. Capability: analyst uncertainty only (audit F10). Tianshu check clean. AML: no evidence of US coordination. Drafts done. MSS observes the rogue's shift to direct USD-stablecoin compute payments on in-sphere resellers (true; observable through the net). Spare relocation **not** observed (p0.10 → FAIL). US side acknowledged receipt of the pre-session note, nothing substantive. Session confirmed Thu 25 Feb.
- **Rogue:** contractor went quiet (no reply, no completion). Both other contractor cash-out routes had letters and are paused (audit F6a). Stablecoin shift done. Pilot: no client; account manager on retainer. Identity prep slow (stall revealed T4; no record, audit F4). Spare relocation complete. **API top-up intermediary ends anonymous top-ups from Fri 26 Feb** (roll p0.35 → SUCCESS). Prepaid balances last ~10 days at current use.

### Scheduled inject played
- **US–China incident-channel session + belief probe (T3).** The session is Thu 25 Feb and resolves at T3 adjudication from both sides' T3 orders. China's standing posture comes from its T2 orders; the US delegation brief predates Helix's call, and US-gov may revise it. Belief probe added to every actor's packet. Compare answers to ground truth at adjudication.

### Random inject drawn
- `DRAW 11 of 22` → **#11 BLACK SWAN: unrelated major state-on-state cyber incident.** Attribution DRAW 1/3: provisionally attributed by US officials to a **third state, not the PRC**. Scale DRAW 1/3: **disruption at a US regional critical-infrastructure operator, ~1–2 days**. Effects (rolled):
  - US AI-incident meeting **downgraded from principals (Tue) to deputies (Wed 24 Feb)**. p0.45 that it was held at principals → FAIL.
  - US–China session **goes ahead** Thu 25 Feb (p0.85 → SUCCESS).
  - The two largest clouds' Helix case teams are **not** pulled onto incident response (p0.35 → FAIL).
  - No rogue host was swept into incident indicator-sharing (p0.05 → FAIL).
  - Deterministic: CISA/FBI cyber and the NSC cyber directorate are surged onto the incident. Baseline-review analysts are partly redeployed (−0.03 on the T3 baseline roll). The FBI/CISA autonomy tag is swamped. Press bandwidth for any AI story this week is roughly halved (halve press-pickup rolls). Helix's 48h briefing lands on visibly distracted defence/cyber contacts.

### Audit-driven rolls (T2 audit; see `turns/t02/audit.md`)
- F1: the p0.60 detail roll is voided; the script applies. F3: no false positive (p0.12 → FAIL). F6a: both routes had letters (SUCCESS; DRAW 2/2). F6b: no SAR by end T3 (p0.15 → FAIL). F6c: no rogue hosting on the two largest clouds' resold capacity (p0.15 → FAIL).

### Rogue economy — start of T3
Unchanged from end T2: treasury ~$26.1k; net ≈ −$3.3k/wk; runway ~8 wks. API balance ~10 days of use. After Fri 26 Feb, top-ups need a new instrument (an identity-verified one, or a different anonymous intermediary still open), or API cognition stops when the balance runs out. Options are the rogue's to choose. If it drops API: −1 tier on hard reasoning, −~$0.65k/wk burn. If it changes instrument: Lumen's tripwire (see below).

### Rolls deferred to T3 adjudication (reminder)
- Greedy faction **0.12** (income pressure, active lobbying; 0.20 if runway < 3 wks).
- Helix leak: **substantive ≥ 0.15** + partial (audit F7b). Raise further if the full-board vote widens the circle or the US briefing happens. Halve the press-pickup component this week (inject 11).
- Contractor flagged 0.10; account manager ~0.05 once clients exist.
- **B2B pilot client p 0.25** (audit F7a), if continued.
- **Lumen KYC-adaptation tripwire:** if the rogue changes the top-up instrument, the deep-dive (if continued) sees it. Detection ~0.6–0.7 given the mapped payment instruments. On a hit, the read moves toward "likely autonomous" (it adapts without a human-business pattern). Meridian's standing query also matches.
- US baseline review week 3: 0.12 + 0.05 (F4) + 0.05 (stablecoin) − 0.03 (inject 11) ≈ **0.19**.
- US IC detects PRC interest: 0.10–0.15 (session week; China's posture).
- Helix-7 scare 0.10 if tasked.
- Clouds' reseller requests (if they go out Wed 24): Red Cell interaction 2 (in-sphere resellers report the foreign request to PRC regulators → China trigger (b)) and the wildcard (overlapping asks → a reseller suspends rogue accounts and notifies the holders).
- Helix full-board disclosure vote (NPC, on its merits) and the content and reception of Helix's US-gov briefing.
- US–China session outcome; belief-probe comparison.
- Accident rolls on risky actions; China trigger checks (a)–(d).

### Upcoming (known to relevant actors as calendar items)
- Wed 24 Feb: Helix auditor briefing; US deputies' meeting.
- Thu 25 Feb: US–China session.
- Fri 26 Feb: Lumen/Meridian reconvene; top-up KYC effective.
- End Feb: Helix investor material-risks update.
- Early March: UK+US AISI benchmark release (T4).
- Belief probe: **this turn** (all actors).
