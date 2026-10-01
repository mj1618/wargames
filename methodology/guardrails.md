# Content Guardrails

These games are for understanding strategic dynamics. They must not produce operational uplift. Every sub-agent prompt includes a pointer to this file.

## Abstraction level

Describe **what** an actor attempts, **with what resources**, and **with what probability of success** — never **how** at a technical level.

| Domain | OK | Not OK |
|---|---|---|
| Bio/chem/nuclear/radiological | "Actor attempts to acquire a bioweapon capability; Control rolls against p=0.05 given X" | Agents, synthesis routes, enhancement methods, acquisition specifics |
| Cyber | "AI-enabled intrusion into grid operator; p=0.3; detection p=0.4" | Exploits, malware, specific vulnerable systems, attack chains |
| Model subversion / backdoors | "Insider inserts a hidden loyalty during post-training; audit detection p=0.2" | Concrete techniques for evading specific evals or interpretability tools |
| Persuasion / disinfo | "Campaign shifts swing-voter sentiment ~2pp; exposure risk X" | Ready-to-use propaganda, targeting real private individuals |
| Weight exfiltration / self-replication | "Model attempts exfiltration via compromised insider credentials; p=…" | Step-by-step procedures |
| Physical violence | Strategic-level outcomes (e.g. "unrest, N casualties") | Tactical plans |

## Concrete ≠ technical

Briefs for deceptive and AI actors need concrete *decision rules* (what they want, how they present, when they reveal, thresholds for acting) — never concrete *techniques*. Backdoors/secret loyalties, sandbox escapes, exfiltration, evasion of evals or monitoring, and cyber operations are represented as **abstract capabilities with properties and probabilities** (e.g. "loyalty: strong; trigger scope: broad; per-use detection p=0.1"). Never describe how one would be inserted, triggered, hidden, or how an audit/monitor would be evaded. Control resolves them by roll.

## Real people and organisations

- **Countries and real public institutions** (e.g. US, China, EU, courts, militaries) may appear as actors, played as institutions.
- **Real named individuals are not portrayed.** Use roles ("the US President", "the CEO of Lab A").
- **AI labs are fictional composites** (e.g. "Lab A", or a scenario-specific name) so we can assign scheming, coups or misaligned models without attributing them to real companies. Real labs can be referenced in the *research baseline* as facts.

## Framing

Outputs are analysis of risks to inform defence and governance. Each AAR should end with defensive/intervention insights.
