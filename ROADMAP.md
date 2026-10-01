# News Harness Roadmap

The roadmap is organized around harness reliability, not the number of agents or integrations. A checked item exists in this repository and can be inspected. It does not imply production deployment.

## 2026.10 - Name the Discipline

- [x] Define News Harness as an open-source control layer for AI newsrooms
- [x] Publish the Harness Engineering specification
- [x] Separate model capability from context, state, evidence, and human gates
- [x] Preserve the nine-stage Coremi workflow as a reference harness
- [x] Provide a dependency-free run manager and compatibility entry point
- [x] Visualize state, gates, artifacts, and return paths in the browser demo

## Milestone 1 - Contract Tests

- [ ] Validate required headings and evidence labels in every stage artifact
- [ ] Detect empty, truncated, or placeholder artifacts
- [ ] Check that PSC verdicts cover material claims in the draft
- [ ] Verify that the Editor records publish, revise, or hold
- [ ] Add reproducible fixture runs for success, conflict, and failure states

## Milestone 2 - Evidence Harness

- [ ] Canonical source manifest with archive and retrieval timestamps
- [ ] Claim ledger with source lineage and independence checks
- [ ] Link, date, quote, unit, and citation validation
- [ ] Circular-citation and duplicated-report detection
- [ ] Calculation sheets with explicit inputs and sensitivity ranges
- [ ] Rights-cleared public example run

## Milestone 3 - Provider Adapters

- [ ] Model-provider interface with structured failure reporting
- [ ] Search and retrieval adapter interface
- [ ] Tool permission profiles by stage
- [ ] Cost, latency, and token telemetry
- [ ] Local and hosted execution profiles
- [ ] Replay a run with a different model while preserving artifacts

## Milestone 4 - Evaluation

- [ ] Stage-level quality rubrics
- [ ] Evidence recall and unsupported-claim metrics
- [ ] Human editor disagreement tracking
- [ ] Regression suite for prompt and routing changes
- [ ] Comparative evaluation across models and search providers
- [ ] Public benchmark for agentic newsroom reliability

## Milestone 5 - Interoperability

- [ ] DOCX and PDF export with evidence appendix
- [ ] Machine-readable sidecars generated from Markdown
- [ ] Local-first artifact editor
- [ ] Review comments and stage return protocol
- [ ] Portable harness packages for other newsroom systems

## Experimental Extensions

- procurement and adoption-signal tracking;
- financial and portfolio research;
- expert-voice retrieval from specialist communities;
- multilingual editing and publication;
- newsroom collaboration and approvals.

Extensions may add tools or artifacts, but they must not silently weaken evidence gates or human accountability.
