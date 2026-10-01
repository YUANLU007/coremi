# Harness Engineering for AI Newsrooms

## 1. Definition

A **news harness** is the control system around models, tools, and people that turns an editorial request into a traceable publication decision.

The harness does not replace model intelligence. It constrains, routes, observes, and evaluates that intelligence.

```text
capability + context + tools + state + evidence + gates + recovery = dependable agent work
```

Harness engineering is the practice of designing those surrounding conditions as explicit, testable components.

## 2. Why Journalism Needs a Distinct Harness

News work differs from generic task automation in four ways:

1. **Evidence changes.** A source can be corrected, superseded, or contradicted while work is underway.
2. **Claims carry unequal risk.** A wrong date and a false allegation are not equivalent failures.
3. **Judgment is irreducible.** Importance, fairness, proportionality, and public interest require accountable decisions.
4. **The process matters.** A fluent article is not reliable if its evidence path cannot be inspected.

The harness must therefore control both production and restraint.

## 3. Control Surfaces

### 3.1 Context Harness

The context harness creates the research mandate:

- original request;
- intended audience and decision;
- scope and exclusions;
- time horizon;
- supplied sources;
- high-risk claims;
- definition of done.

The request is preserved as an artifact rather than repeatedly paraphrased into conversation memory.

### 3.2 Routing Harness

The routing harness decides:

- which stage is eligible to run;
- which upstream artifacts it may read;
- which tools and source types it may use;
- whether stages may run in parallel;
- which failure returns work to which stage;
- when a human decision is required.

The reference implementation uses nine named stages, but the public contracts matter more than the specific model executing them.

### 3.3 State Harness

State must be durable and legible. At minimum, a stage can be:

- pending;
- active;
- complete;
- failed;
- returned for revision;
- held by an editor.

The reference runner derives state from a run directory and records it in `00_index.md`. Future implementations may use a database, but must retain an exportable human-readable ledger.

### 3.4 Evidence Harness

The evidence harness keeps distinct objects distinct:

- source;
- claim;
- quotation;
- reported number;
- calculation;
- inference;
- estimate;
- forecast;
- verdict.

It records source level, retrieval time, independence, supported wording, conflict, and uncertainty. Retrieval is not verification; repetition is not independence.

### 3.5 Artifact Harness

Every stage leaves a durable artifact with:

- known filename;
- required sections;
- evidence and uncertainty labels;
- completion conditions;
- compatibility expectations.

Artifacts allow a human, another model, or a later run to inspect work without reconstructing a private conversation.

### 3.6 Human Harness

Human gates are not an implementation failure. They are part of the architecture.

Typical gates include:

- approving a high-risk research mandate;
- deciding whether contested evidence is publishable;
- accepting a material correction;
- choosing publish, revise, or hold;
- authorizing public release.

The harness should present the evidence needed for a decision without pretending to make accountability disappear.

## 4. The Reference Execution Graph

```text
Soul → Fetcher → Pitch → Financial → Competitor → Beneficial → PSC → Writer → Editor
  ▲        ▲         │          │            │          │       │         │       │
  └────────┴─────────┴──────────┴────────────┴──────────┴───────┴─────────┴───────┘
                         explicit return paths
```

The numbering creates stable artifacts, not a requirement that execution remain linear. Examples:

- Pitch can request additional retrieval.
- Financial Analyst can request a missing filing.
- PSC can return an unsupported claim to its originating stage.
- Editor can hold publication or reopen any stage.

## 5. Gates

A gate is a test that must pass before the harness advances. Good gates are:

- observable;
- local to a stage;
- explainable to a reviewer;
- testable with fixtures;
- capable of failing without destroying prior work.

Examples:

| Stage | Weak condition | Harness gate |
|---|---|---|
| Fetcher | links were collected | each material claim has a source lead and level |
| Financial | numbers were mentioned | period, unit, source, formula, and assumptions are present |
| PSC | two links agree | source independence and permitted wording are recorded |
| Writer | a long draft exists | barred claims are absent and uncertainty is preserved |
| Editor | all files exist | publication decision and unresolved risks are explicit |

## 6. Failure and Recovery

Failure should produce state, not disappearance.

A failed stage should record:

- stage name;
- attempted input;
- tool or provider used;
- failure category;
- retryability;
- partial artifact location;
- recommended next action.

Completed upstream artifacts remain valid unless the failure reveals a specific integrity problem. A resumed run continues from the first unmet gate.

## 7. Observability Without Private Reasoning

News Harness displays work products and decisions:

- current stage;
- tool and source activity;
- artifact previews;
- evidence verdicts;
- costs and latency when available;
- return and failure events;
- editorial decision.

It does not claim to expose a model's private chain of thought. The public audit surface is the structured work the newsroom needs, not hidden model internals.

## 8. Provider Neutrality

Models, search systems, and data providers change. The harness should isolate them behind adapters and preserve stable public contracts.

A provider adapter should report:

- identity and version;
- request and response timing;
- usage and cost when available;
- truncation or quota failure;
- tool errors;
- structured output validity;
- retry behavior.

No provider may silently mark a stage complete.

## 9. Evaluation

Evaluate both the final article and the process that produced it.

Suggested dimensions:

- unsupported material claims;
- primary-source coverage;
- citation and quote accuracy;
- calculation reproducibility;
- conflict preservation;
- stage-gate precision and recall;
- recovery success after injected failure;
- human editor disagreement;
- cost and latency per completed run.

The most persuasive evaluation artifact is a replayable run with known evidence and expected gates.

## 10. Open-Source Boundary

The harness specification, prompts, runner, validators, adapters, and rights-cleared fixtures can be public. Production credentials, user data, private source material, payment systems, and unpublished research must remain outside the repository.

This boundary lets the operating method improve in public without turning openness into data leakage.
