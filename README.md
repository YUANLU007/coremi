# COREMI 科睿 — AI-Native Newsroom & Investment Intelligence System

> *"Business is not a sale but a reshaping of destinies."*

**One journalist. One system. The world's information, restructured.**

COREMI is an open-source, multi-agent AI system built to replace an entire newsroom — fetching, analyzing, writing, verifying, and publishing financial and technology news at Bloomberg speed, with Reuters accuracy, and WSJ storytelling quality.

Born in Silicon Valley, January 2026.

---

## 🌐 English | [中文](#中文介绍)

### What is COREMI?

COREMI (科睿) is a **10-module multi-agent system** — not a simple pipeline, but a network of specialized AI agents that collaborate, cross-verify, and iterate — designed to:

- 📡 **Fetch** news from 20+ elite global sources (WSJ, FT, Reuters, Caixin, The Economist...)
- 🔍 **Pitch** — score, select, and identify the highest-value stories for investors and decision-makers
- 💹 **Analyze** companies financially (DCF, 5-year trends, CFA-standard)
- ✍️ **Write** in WSJ narrative style + Xinhua precision + Economist macro insight
- ✅ **Verify** every fact with dual-source cross-validation (PSC method)
- 📤 **Publish** to WeChat, Xiaohongshu, TikTok, CBN — in seconds

**Target**: 300 pieces of intelligence published per day. 2 staff. Sub-minute latency.

---

## 🏗️ System Architecture — 10 Modules

```
┌─────────────────────────────────────────────────────────────┐
│                    COREMI Multi-Agent System                 │
│                                                             │
│  [1] Soul.md ──────── Unified editorial mind & values       │
│       │                                                     │
│  [2] News Fetcher ─── 20+ sources, RSS + API, scored        │
│       │                                                     │
│  [3] Pitch ────────── Story selection, 5W1H, value score    │
│       │                                                     │
│  [4] Financial ────── DCF, 5Y trend, CFA-standard analysis  │
│  [5] Competitor ───── How rivals covered the same story     │
│  [6] Beneficial ───── Related stocks: US/HK/A/DE/JP/UK      │
│       │                                                     │
│  [7] Writer ───────── Inverted pyramid, killer lede         │
│  [8] Editor ───────── Standards check, CN↔EN alignment      │
│       │                                                     │
│  [9] PSC ──────────── Cross-verification, source database   │
│       │                                                     │
│  [10] Router ──────── Publish matrix: style, author, date   │
│                                                             │
│         ↕ Multi-agent, not pipeline. Agents re-call         │
│           each other. e.g. NVDA → Samsung/Hynix → re-fetch  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Workflows

| Workflow | Modules Used | Output | Depth |
|----------|-------------|--------|-------|
| `#newspress` | Fetcher + Pitch + Writer | 8 posts, 800 words, 6am | Fast |
| `#researcher` | All 10 | 5000-word industry report | Deep |
| `#trader` | Financial + Competitor + Beneficial | Portfolio strategy | Expert |

---

## 📁 Repository Structure

```
coremi/
├── README.md
├── VISION.md              # Founder story & market thesis
├── ROADMAP.md             # What's built, what's needed
├── CONTRIBUTING.md        # How to join
├── prompts/               # Core prompts for each module
│   ├── 01-soul.md
│   ├── 02-news-fetcher.md
│   ├── 03-pitch.md
│   ├── 04-financial-analyst.md
│   ├── 05-competitor.md
│   ├── 06-beneficial-stocks.md
│   ├── 07-writer.md
│   ├── 08-editor.md
│   ├── 09-psc.md
│   └── 10-router.md
├── docs/
│   ├── architecture.md
│   ├── source-list.md     # Verified source list (20+)
│   └── examples/          # Real system outputs
└── src/                   # Code (Python, CLI-first)
    ├── fetcher/
    ├── pitch/
    ├── writer/
    └── router/
```

---

## 🛠️ Tech Stack

- **Language**: Python 3, CLI-first
- **AI**: Claude API (multi-agent orchestration)
- **Data**: feedparser, Reuters RSS, Futu API, Tonghuashun
- **Publish**: WeChat API, Xiaohongshu, TikTok
- **Architecture**: Multi-agent (not pipeline) — agents can re-invoke each other

---

## 🤝 We Need You

COREMI is **architecture-complete** but code-hungry. The 10-module design is defined. Now we build.

**Open Issues — Good First Tasks:**

| Module | Task | Skill Needed |
|--------|------|-------------|
| News Fetcher | RSS ingestion + scoring engine | Python, feedparser |
| Financial Analyst | Futu API integration | Python, finance API |
| Writer | Prompt-to-article pipeline | Python, LLM API |
| Router | Multi-platform publisher | Python, WeChat/API |
| Editor UI | Web newsroom interface | React/Next.js |
| PSC | Cross-verification logic | Python, NLP |

→ See [CONTRIBUTING.md](./CONTRIBUTING.md) to get started
→ Browse [open issues](../../issues)

---

## 💡 For Investors

COREMI addresses a **$30B+ market** (financial intelligence, Bloomberg Terminal alone: $6B/year).

**The gap**: Bloomberg costs $25,000/year per seat. COREMI aims to deliver 80% of the intelligence at 1% of the cost — with AI agents doing the labor.

**Traction**: Full architecture designed, source list validated, prompts tested in production by the founder across 10+ stories published in CBN and FT Chinese.

**Contact for investment inquiries**: [Add your email here]

---

## 👤 Founder

**Lu Yuan (陆媛)** — Investigative journalist, Silicon Valley Observer Editor.

- Former Senior Editor, China Business News (第一财经)
- Silicon Valley-based since 2024
- Author & Google Scholar: [scholar.google.com/citations?user=wAi9MdkAAAAJ](https://scholar.google.com/citations?view_op=list_works&hl=zh-CN&user=wAi9MdkAAAAJ)
- Published column: [yicai.com/author/100008939.html](https://www.yicai.com/author/100008939.html)

*"I am a journalist who decided to build the newsroom I always wished existed."*

---

## 📄 License

MIT License — open for contribution, attribution appreciated.

---

---

## 中文介绍

# COREMI 科睿 — AI原生新闻编辑部与投资情报系统

**一个记者。一套系统。重构全球信息流。**

科睿（COREMI）是一个开源的**10模块多智能体系统**——不是简单的pipeline，而是多个专业AI智能体协同工作、交叉验证、反复迭代——目标是：

- 以彭博社的速度、路透社的准确性、华尔街日报的叙事质量，完成新闻生产全流程
- 两个员工，每天发布300条资讯
- 秒级发布，全球多平台分发

### 系统起源

2026年1月，硅谷。

作为在第一财经工作多年的调查记者，我一直在想：**如何把人对金融财经商业信息的需求AI化？**

不是替代记者，而是让一个记者能做整个编辑部的工作。

于是有了科睿。

### 10个模块

| 编号 | 模块 | 功能 |
|------|------|------|
| 1 | Soul.md | 统一编辑心智与价值观 |
| 2 | News Fetcher | 抓取20+权威信源新闻 |
| 3 | Pitch | 新闻价值评估与选题 |
| 4 | Financial Analyst | 财务分析，DCF，CFA标准 |
| 5 | Competitor | 竞品报道对比分析 |
| 6 | Beneficial Stocks | 相关上市公司（美股/A股/港股/德股） |
| 7 | Writer | 倒金字塔写作，华尔街日报叙事风格 |
| 8 | Editor | 编辑审核，中英文对齐 |
| 9 | PSC | 双信源交叉验证 |
| 10 | Router | 多平台发布（公号/小红书/抖音/CBN） |

### 我们需要

- Python 后端开发者
- LLM应用工程师
- 新闻/金融领域专家（验证输出质量）
- 投资人（天使/种子轮）

**投资/合作联系**：[填写你的邮件]

---

*独立 · 独家 · 独到*
