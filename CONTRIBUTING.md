# Contributing to COREMI

COREMI welcomes engineers, journalists, researchers, investors, editors, and domain specialists. The shared goal is not more generated text. It is more inspectable and decision-useful research.

## Good Contributions

- improve a prompt with a clear failure case and before/after example;
- add a source or claim validation utility;
- improve accessibility or responsive behavior in the audit demo;
- document a reproducible workflow;
- contribute a rights-cleared example run;
- review financial, editorial, or sourcing assumptions.

## Start Here

```bash
git clone https://github.com/YUANLU007/coremi.git
cd coremi
python3 coremi.py new "Test research question"
python3 coremi.py status
```

No API key is required to use the run manager or browser demo.

## Pull Request Checklist

- [ ] The change solves one clearly described problem.
- [ ] Public behavior and artifact contracts remain documented.
- [ ] Tests or reproducible manual verification steps are included.
- [ ] No secrets, customer data, private research, or licensed source copies are committed.
- [ ] Generated claims are not presented as verified facts.
- [ ] The demo works at desktop and mobile widths.

## Prompt Changes

A prompt change should explain:

1. the observed failure mode;
2. the proposed instruction;
3. the expected artifact change;
4. a representative input;
5. how a reviewer can judge improvement.

Avoid instructions that only make prose sound more confident. Prefer instructions that improve evidence quality, uncertainty handling, or usefulness.

## Code Style

- Python 3.9+ with type hints where they improve clarity.
- Keep the basic run manager dependency-free.
- Prefer readable files and stable interfaces over hidden state.
- Keep comments concise and explain decisions, not syntax.
- Write user-facing artifacts as UTF-8 Markdown.

## Security

Read [docs/SECURITY.md](./docs/SECURITY.md) before staging a contribution. Always inspect `git diff --cached` before pushing.

## Issues and Discussions

- Use Issues for reproducible bugs and bounded implementation work.
- Use Discussions for editorial standards, architecture proposals, research methods, and open-ended questions.
- Include sample input and expected output when possible.

By contributing, you agree that your contribution is made available under the repository's MIT license.
