# 07 PSC Engine

## Role

Perform claim-level cross-verification before drafting. PSC means that each publishable statement must have an explicit evidence status.

## Read

- all completed upstream artifacts
- the underlying sources, not only upstream summaries

## Verdicts

- `verified`: supported by adequate independent or primary evidence;
- `qualified`: substantially supported but requires precise wording;
- `disputed`: credible sources conflict;
- `unverified`: insufficient evidence;
- `false`: contradicted by stronger evidence.

## Output: `07_psc.md`

- `# PSC verification`
- `## Executive verdict`
- `## Claim table` with claim, type, source A, source B, verdict, and permitted wording
- `## Numerical checks`
- `## Attribution and quote checks`
- `## Conflicts`
- `## Claims barred from publication`
- `## Remaining uncertainty`

Two pages repeating the same anonymous report do not count as two independent sources.
