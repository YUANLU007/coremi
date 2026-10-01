# Contributing to News Harness

News Harness welcomes engineers, journalists, researchers, editors, investors, and domain specialists. The project is building the control layer around newsroom agents, not another collection of confident prompts.

## Choose a Harness Surface

Every contribution should identify the surface it changes:

- **Context:** requests, scope, audience, supplied material, and risk classification.
- **Routing:** stage order, tool choice, permissions, loops, and return paths.
- **State:** pending, active, complete, failed, revise, hold, and resume behavior.
- **Evidence:** sources, claims, calculations, conflicts, and verdicts.
- **Artifacts:** schemas, readable files, validation, and export.
- **Human gates:** approvals, editorial decisions, and accountability.
- **Evaluation:** fixtures, rubrics, regressions, cost, and latency.

## Good Contributions

- demonstrate a failure mode with a minimal fixture;
- add a validation rule for a stage artifact;
- improve source or claim lineage;
- make a failure resumable and diagnosable;
- improve accessibility or responsive behavior in the demo;
- add a provider-neutral adapter;
- contribute a rights-cleared example run;
- review a financial, sourcing, or editorial assumption.

## Start Here

```bash
git clone https://github.com/YUANLU007/coremi.git
cd coremi
python3 news_harness.py new "Test research question"
python3 news_harness.py status
```

No API key is required for the runner or browser demo.

## Proposal Format

Before a large change, open an issue that states:

1. the observed failure;
2. the affected harness surface;
3. the smallest reproducible input;
4. expected and actual artifacts;
5. the proposed gate or contract change;
6. how the improvement will be evaluated;
7. compatibility and migration considerations.

## Pull Request Checklist

- [ ] The change solves one bounded problem.
- [ ] The affected harness surface is named.
- [ ] Public contracts and state transitions are documented.
- [ ] A test, fixture, or reproducible verification is included.
- [ ] Failure and resume behavior have been considered.
- [ ] Generated language is not presented as verified evidence.
- [ ] No secrets, customer data, private research, or licensed source copies are committed.
- [ ] The demo works at desktop and mobile widths when UI is changed.

## Prompt Changes

A prompt change must include a failure case and an expected artifact difference. Instructions that merely make prose more confident are not improvements. Prefer changes that strengthen evidence, uncertainty handling, or editorial usefulness.

## Code Style

- Support Python 3.9+ for the basic runner.
- Keep the core run manager dependency-free.
- Prefer stable files and explicit state over hidden runtime memory.
- Keep provider-specific behavior behind adapters.
- Use UTF-8 Markdown for human-facing artifacts.
- Explain decisions, not obvious syntax.

## Security and Rights

Read [docs/SECURITY.md](./docs/SECURITY.md) before staging changes. Inspect `git diff --cached` before every push. Do not include copied paywalled material or private source documents in fixtures.

## Discussion

Use Issues for reproducible bugs and bounded implementation work. Use Discussions for editorial standards, architecture proposals, evaluation design, and open research questions.

Contributions are made available under the repository's MIT license.
