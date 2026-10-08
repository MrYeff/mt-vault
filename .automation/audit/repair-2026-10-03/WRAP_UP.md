# Audit repair wrap-up — 2026-10-03

- Scope: 31 previously audit-failed papers.
- Finalized: 18, after independent source audits and required re-audits.
- Remaining: 13; every remaining note retains `audit failed`.
- The usage limit stopped all three cheap agents. Completed reports were applied; incomplete audits were not counted as passes. No new papers started after the wrap-up request.
- One finalized note remains `fulltext unavailable`: Redesigning algorithms to intervene on social norm misperceptions during a national election. Only accessible abstract claims and bibliography were audited; detailed model extraction is skipped.
- Sources remain in `vault/.automation/sources/files/`, with provenance in `index.json` and individual audit/repair records.
- Final checks: all 31 scoped notes pass structural checks; no undefined footnotes; all unfinished failure flags verified. Structural checks do not substitute for source audits.

## Repaired; independent audit still required

- Modeling Interaction in Collaborative Groups- Affect Control Within Social Structure
- Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics
- Social Simulacra- Creating Populated Prototypes for Social Computing Systems
- The Power of Social Cognition
- Towards operational validation of LLM-agent social simulations- a replicated study of a Reddit-like technology forum
- User Behavior Simulation with Large Language Model based Agents
- Using artificial agents to understand laboratory experiments of common-pool resources with real agents
- Y Social- an LLM-powered Social Media Digital Twin

## Interrupted repair

- Reciprocal Recommender Systems- Analysis of state-of-art literature- challenges and opportunities towards social recommendation

## Not started

- Reranking partisan animosity in algorithmic social media feeds alters affective polarization
- Social Agents- A Systematic Review of Social Identity Formalizations
- Social capital II- determinants of economic connectedness
- The Focused Organization of Social Ties

## Resume records

- `checkpoint.json`: exact current hashes, per-paper status and warnings.
- `finalized.json`: passing reports and final hashes; previous finalizations retained.
- `batch-1-repairs.json`, `batch-2-repairs.json`, `batch-3-repairs.json`: source coverage and repair checkpoints.
- `audit-*.json`: independent findings and re-audits, including failed/withdrawn checks.
- `root-latent-bibliography-check.json`: independent 71-title comparison completed during wrap-up.
