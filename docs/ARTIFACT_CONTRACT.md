# News Harness Artifact Contract

The public News Harness interface is a directory of readable Markdown files. A run can be resumed, inspected, reviewed, or handed to another model without a proprietary database.

## Required Control Files

### `00_request.md`

Contains the original question, user-provided sources, and requested output. Preserve it verbatim after a run begins.

### `00_index.md`

Contains the current run status and links to every stage artifact. The included CLI rebuilds this file from the artifacts present on disk.

## State Model

The reference runner currently derives `pending`, `empty`, and `complete` from the filesystem. A full harness implementation should also preserve:

- `active`: execution has started;
- `failed`: execution stopped with a recorded cause;
- `revise`: a later gate returned the artifact;
- `hold`: an editor blocked advancement;
- `complete`: the artifact satisfies its gate.

State changes should include a timestamp, actor or provider, reason, and next action. A transition must not erase the earlier artifact.

## Stage Files

| File | Minimum acceptable content |
|---|---|
| `01_soul.md` | audience, decision, scope, exclusions, editorial posture |
| `02_fetcher.md` | source inventory, dates, source level, extracted claims, gaps |
| `03_pitch.md` | thesis, novelty, stakes, counter-angle, reporting plan |
| `04_financial_analyst.md` | metrics, periods, calculations, assumptions, sensitivity |
| `05_competitor_monitor.md` | comparable coverage, consensus, omissions, framing differences |
| `06_beneficial_related.md` | impact chain, beneficiaries, losers, timing, listed-company relevance |
| `07_psc.md` | claim-by-claim verdicts and source comparison |
| `08_writer.md` | complete draft with attribution and limitations |
| `09_editor.md` | corrections, unresolved risks, publication decision, final copy |

## Evidence Labels

Use these labels consistently:

- **Fact:** directly supported by a cited source.
- **Inference:** reasoned conclusion from disclosed facts.
- **Estimate:** calculation based on stated inputs.
- **Forecast:** forward-looking judgment with uncertainty.
- **Unverified:** plausible claim that has not met the evidence threshold.

## Source Levels

- **L1:** filings, regulators, courts, official statistics, direct company material, full interviews.
- **L2:** reputable original reporting with named or clearly described sourcing.
- **L3:** research notes, specialist publications, and credible secondary analysis.
- **L4:** aggregators, social posts, unattributed summaries, or search snippets.

L4 material can generate leads. It cannot independently verify a material claim.

## Completion Rules

An artifact is not complete merely because a file exists. It must:

1. answer the stage question;
2. distinguish evidence from analysis;
3. link or identify the sources used;
4. disclose missing information and conflicts;
5. avoid invented facts, quotes, numbers, and citations.

The Editor may return a run to an earlier stage. Auditability is more important than forcing a green status.

## Compatibility Rule

Harness implementations may store additional structured state, but they should be able to export the required Markdown artifacts and `00_index.md`. Provider-specific metadata must not become the only way to understand a run.
