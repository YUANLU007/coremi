# News Harness

## Harness Engineering for AI Newsrooms

News Harness is an open-source control layer for AI-assisted journalism and investment research. It defines what an agent may read, what it must produce, when it may advance, how evidence is graded, and where human judgment remains mandatory.

News Harness是一套面向AI新闻编辑部与投资研究的开源控制层。它不追求再造一个更会写字的模型，而是规定智能体可以读取什么、必须留下什么、何时能够进入下一步、证据如何分级，以及哪些判断必须由人负责。

Built by [Coremi](https://news.coremi.ai).

[Interactive demo](https://yuanlu007.github.io/coremi/) · [Harness specification](./docs/HARNESS_ENGINEERING.md) · [Vision](./VISION.md) · [Roadmap](./ROADMAP.md) · [Contributing](./CONTRIBUTING.md)

## The Core Idea

Models are becoming interchangeable. Reliable work is not.

In an agentic newsroom, the model is only one component. The surrounding harness determines whether the system:

- starts from a precise editorial question;
- retrieves evidence instead of improvising context;
- preserves the difference between fact, inference, estimate, and forecast;
- records state in files that people can inspect;
- stops when evidence is insufficient;
- resumes after failure without losing completed work;
- produces a final article that can be traced back to its sources.

This surrounding system is **harness engineering**.

## What Is a News Harness?

A news harness combines six control surfaces:

| Control surface | What it governs |
|---|---|
| Context | the question, audience, scope, exclusions, and supplied material |
| Routing | which research stage runs next and which tools or sources it may use |
| State | what is pending, active, complete, failed, or returned for revision |
| Evidence | source levels, claim status, conflicts, calculations, and uncertainty |
| Artifacts | the readable files each stage must leave behind |
| Human gates | the decisions that cannot be delegated to model fluency |

News Harness is not a model, a hidden chain of thought, or a generic agent framework. It is the inspectable operating structure around models and tools.

## Reference Harness: Nine Stages

The repository includes a nine-stage reference implementation developed inside Coremi:

| Stage | Responsibility | Required artifact | Gate to advance |
|---:|---|---|---|
| 1. Soul | define audience, decision, scope, and risk | `01_soul.md` | research mandate is explicit |
| 2. News Fetcher | build a ranked source and claim map | `02_fetcher.md` | material claims have evidence leads |
| 3. Pitch | choose a useful, supportable thesis | `03_pitch.md` | angle survives the counter-thesis |
| 4. Financial Analyst | test economics, calculations, and sensitivity | `04_financial_analyst.md` | periods, units, assumptions are disclosed |
| 5. Competitor Monitor | compare companies and competing narratives | `05_competitor_monitor.md` | consensus and omissions are visible |
| 6. Beneficial Related | map impact through the value chain | `06_beneficial_related.md` | each beneficiary has a mechanism |
| 7. PSC Engine | verify claims one by one | `07_psc.md` | publishable wording is defined |
| 8. Writer | turn verified material into a complete argument | `08_writer.md` | draft does not outrun the evidence |
| 9. Editor | correct, return, hold, or publish | `09_editor.md` | a human-readable decision is recorded |

The stages may loop. Financial analysis can send the harness back to retrieval; PSC can bar a claim; the Editor can return the draft to any earlier stage. The numbered artifacts remain stable even when the execution path is not linear.

## Architecture

```text
Question or lead
      │
      ▼
┌──────────────────────────────────────────────┐
│ CONTEXT HARNESS                              │
│ request · audience · scope · source material │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ WORK HARNESS                                 │
│ nine stages · tool routing · resumable state │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ EVIDENCE HARNESS                             │
│ source levels · claim ledger · PSC verdicts  │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│ DELIVERY HARNESS                             │
│ draft · editorial decision · final artifact  │
└──────────────────────────────────────────────┘
```

Read [Harness Engineering](./docs/HARNESS_ENGINEERING.md) for the design principles and component contract.

## Quick Start

Requirements: Python 3.9+. The local run manager uses only the Python standard library.

```bash
git clone https://github.com/YUANLU007/coremi.git
cd coremi

# Create a harness run
python3 news_harness.py new \
  "How will AI data-center power demand reshape utilities?" \
  --source "https://example.com/source"

# Inspect state and locate the next gate
python3 news_harness.py status
python3 news_harness.py next data/<run-directory>

# Record a completed stage artifact
python3 news_harness.py record data/<run-directory> 1 path/to/01_soul.md
```

The runner does not pretend to be an LLM. It creates the state and artifact contract. You choose the model, search system, coding agent, or human collaborator that executes each stage.

`coremi.py` remains as a compatibility entry point and forwards to the same runner.

## Repository Map

```text
coremi/
├── news_harness.py              # dependency-free run and state manager
├── coremi.py                    # compatibility entry point
├── prompts/                     # nine public stage specifications
├── docs/
│   ├── HARNESS_ENGINEERING.md   # architecture and design principles
│   ├── ARTIFACT_CONTRACT.md     # files, evidence labels, completion rules
│   └── SECURITY.md              # public/private repository boundary
├── data/.gitkeep                # local runs are ignored by Git
├── index.html                   # interactive harness demo
├── VISION.md
├── ROADMAP.md
└── CONTRIBUTING.md
```

## A Run Is a Durable Record

```text
data/20261001_103000_ai-data-center-power/
├── 00_request.md
├── 00_index.md
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

`00_index.md` is the state ledger. A file is not complete merely because it exists; it must satisfy the stage contract. JSON may be used internally, but the public interface is readable Markdown.

## Design Principles

1. **Artifacts over memory.** Important state survives outside a model conversation.
2. **Evidence before eloquence.** Fluency cannot upgrade a weak source.
3. **Visible gates over silent automation.** Advancement has explicit conditions.
4. **Loops over forced linearity.** A later stage can reopen earlier research.
5. **Failure is state.** A failed stage is recorded, diagnosable, and resumable.
6. **Provider neutrality.** Models and search tools can change without changing the public contract.
7. **Human accountability.** Publication remains an editorial decision.

## Public Boundary

This repository contains the harness specification, prompts, runner, and demonstration interface. It does not contain production credentials, payment systems, customer data, unpublished source material, or Coremi's private research archive.

## Project Relationship

**Coremi** is the newsroom and judgment-intelligence product. **News Harness** is its open-source harness-engineering layer. The repository is maintained by **Lu Yuan (陆媛)**, an investigative journalist and Silicon Valley technology observer.

- [Coremi live workflow](https://news.coremi.ai)
- [Google Scholar](https://scholar.google.com/citations?view_op=list_works&hl=zh-CN&user=wAi9MdkAAAAJ)
- [第一财经作者主页](https://www.yicai.com/author/100008939.html)

## License

[MIT](./LICENSE). Contributions are welcome. Third-party sources and editorial material remain subject to their original rights and verification requirements.

---

**News Harness**

Harness Engineering for AI Newsrooms
