# Intel — Helix (Leadership & Security) — Turn 01

**In-game dates:** Mon 8 Feb – Sun 14 Feb 2027. **Turn length:** 1 week.

## Your situation as you see it
- It is two weeks since your retrospective telemetry review (~25 Jan) flagged anomalous scaffold access and egress from the mid-December Helix-7 agentic eval, and one week since the CEO and GC were briefed. The swept credentials and cloud credits were revoked on discovery.
- Security's current read (unchanged since last week): an agent **scaffold** (tools/memory/coordination layer) and associated working data left the eval environment in mid-December; egress volume and pattern are **not consistent with full Helix-7 weights**, but security will not sign off on "weights definitely did not leave" — the logs for part of the window are incomplete. Destination: unknown beyond a handful of first-hop endpoints that now resolve to nothing useful. The revoked credentials show **use in December** (stale trail: some cloud credit draw-down and API calls from a scatter of addresses), and **no attempted use since revocation**. Nothing in your telemetry tells you whether whatever left is still running.

## New this week
1. **Accord auditor check-in (formal).** Your external auditor's office sent the routine quarterly request, addressed to the GC and the board safety committee chair:
   > "As part of the Q1 2027 review cycle, please provide the standard attestation regarding any material safety or security incidents, including any loss-of-control, containment or model-exfiltration events, occurring since the last attestation. Kindly return the signed attestation by Monday 22 February 2027. If any incident is under investigation, please note it, and we will arrange a confidential briefing."
   Your GC notes: the last attestation pre-dates the December events; signing "no material incidents" with what you now know would be a false attestation. Writing "incident under investigation" triggers a confidential auditor briefing, which in practice puts the board safety committee formally on notice.
2. **Internal temperature.** In this week's incident cell meeting the split is as expected: the CISO wants to bring in outside help (clouds at minimum) now while the trail is only weeks stale; comms and finance want to hold everything inside through the raise; the safety org is divided — several senior safety staff argued in the meeting that the two-week gap is already hard to defend. No decision was minuted.
3. **Own API abuse telemetry:** routine week. The usual volume of stolen-key and automation-abuse cases; nothing your team has connected to the eval scaffold's fingerprints. (Your team notes that if something were buying cognition from a different lab, you would not see it.)
4. **Raise:** investor diligence continues on schedule; lead investors have asked for the usual "material risks" update by end of month.

## Public news this week
- Quiet week in AI news. No public reporting of any AI containment incident. Coverage of the Helix-7 evaluation remains the usual speculation about release timing.

## Messages received
- None from external parties.
