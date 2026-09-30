# COREMI 科睿

> **Judge the future.**

COREMI is an open-source, AI-native newsroom and investment-research workflow. It turns a question, lead, company, or market signal into a nine-stage, source-aware audit trail and a publishable draft.

科睿是一套开源的AI原生新闻编辑部与投资研究工作流。它把一个问题、新闻线索、公司或市场信号，转化为九步可追溯的研究过程和可交付稿件。

[Live workflow](https://news.coremi.ai) · [Interactive demo](./index.html) · [Vision](./VISION.md) · [Roadmap](./ROADMAP.md) · [Contributing](./CONTRIBUTING.md)

## Why COREMI

Most AI research tools only show the answer. COREMI keeps the work visible:

- every stage writes a readable Markdown artifact;
- claims are separated from evidence and assumptions;
- weak or conflicting sources remain visible instead of being silently merged;
- the final article can be traced back to the research that produced it;
- a failed stage does not erase completed work.

This repository contains the public workflow specification, prompt templates, a small local run manager, and an interactive audit-flow demo. It does **not** contain production credentials, private research, customer data, or payment infrastructure.

## The Nine-Step Audit Flow

| Step | Agent | Question answered | Artifact |
|---:|---|---|---|
| 1 | Soul | What are we trying to understand, and for whom? | `01_soul.md` |
| 2 | News Fetcher | What primary and high-quality sources exist? | `02_fetcher.md` |
| 3 | Pitch | Why does this matter now? | `03_pitch.md` |
| 4 | Financial Analyst | What do the numbers imply? | `04_financial_analyst.md` |
| 5 | Competitor Monitor | How are rivals and other outlets framing it? | `05_competitor_monitor.md` |
| 6 | Beneficial Related | Who benefits, who pays, and through which chain? | `06_beneficial_related.md` |
| 7 | PSC Engine | Which claims survive cross-verification? | `07_psc.md` |
| 8 | Writer | What is the complete, readable argument? | `08_writer.md` |
| 9 | Editor | Is it accurate, coherent, and ready to publish? | `09_editor.md` |

`00_index.md` is the run ledger. It records status, timestamps, and artifact paths. JSON may be used internally, but the public contract is human-readable Markdown.

## Quick Start

Requirements: Python 3.9+. The run manager uses only the Python standard library.

```bash
git clone https://github.com/YUANLU007/coremi.git
cd coremi

# Create an auditable run directory
python3 coremi.py new "How will AI data-center power demand reshape utilities?" \
  --source "https://example.com/source"

# Inspect all runs or one run
python3 coremi.py status
python3 coremi.py status data/<run-directory>

# See the next stage and its prompt
python3 coremi.py next data/<run-directory>
```

The CLI does not pretend to be an LLM. It creates and validates the audit trail; you can execute the prompts with the model or agent environment you choose.

## Run Directory

```text
data/20260930_160704_ai-data-center-power/
├── 00_index.md
├── 00_request.md
├── 01_soul.md
├── 02_fetcher.md
├── 03_pitch.md
├── 04_financial_analyst.md
├── 05_competitor_monitor.md
├── 06_beneficial_related.md
├── 07_psc.md
├── 08_writer.md
└── 09_editor.md
```

See [docs/ARTIFACT_CONTRACT.md](./docs/ARTIFACT_CONTRACT.md) for the file contract and completion rules.

## Prompts

The core prompt pack lives in [`prompts/`](./prompts):

```text
01-soul.md
02-news-fetcher.md
03-pitch.md
04-financial-analyst.md
05-competitor-monitor.md
06-beneficial-related.md
07-psc.md
08-writer.md
09-editor.md
```

[`11-lab-chain.md`](./prompts/11-lab-chain.md) remains available as an experimental extension for tracking real procurement and adoption signals. It is not part of the fixed nine-step contract.

## Editorial Rules

1. Prefer primary sources, filings, regulators, company statements, and direct interviews.
2. Label fact, inference, estimate, and forecast separately.
3. A link is not evidence until the underlying claim is checked.
4. Preserve disagreement between credible sources.
5. Do not fabricate missing numbers, quotes, dates, or attribution.
6. The final draft must include limitations and what would change the conclusion.

## What This Release Changes

The `2026.09` release replaces the earlier ten-module architecture with a fixed nine-step audit flow. It also replaces JSON-first promises with Markdown-first artifacts, removes the publishing router from the core research contract, and makes progress and failure states explicit.

See [CHANGELOG.md](./CHANGELOG.md) for details.

## Founder

COREMI was created by **Lu Yuan (陆媛)**, an investigative journalist and Silicon Valley technology observer.

- [Google Scholar](https://scholar.google.com/citations?view_op=list_works&hl=zh-CN&user=wAi9MdkAAAAJ)
- [第一财经作者主页](https://www.yicai.com/author/100008939.html)

## License

[MIT](./LICENSE). Contributions are welcome. Editorial claims and third-party source material remain subject to their original rights and verification requirements.

---

**独立 · 独家 · 独到**

Independent · Exclusive · Insightful
