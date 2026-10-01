# Changelog

All notable public changes to News Harness are documented here.

## 2026.10 - News Harness

### Reframed

- Renamed the open-source project layer **News Harness**.
- Defined the discipline as **Harness Engineering for AI Newsrooms**.
- Positioned the nine-stage Coremi workflow as a reference harness rather than the entire definition of the project.
- Separated model capability from context, routing, state, evidence, artifacts, recovery, and human gates.

### Added

- A full harness-engineering specification for agentic newsroom systems.
- A provider-neutral architecture and evaluation direction.
- Explicit failure, return, hold, and resume states.
- A `news_harness.py` entry point while preserving `coremi.py` compatibility.
- A redesigned interactive demo centered on harness state and stage gates.

## 2026.09 - Nine-Step Audit Flow

### Added

- A fixed nine-stage newsroom and investment-research workflow.
- Markdown-first artifact contracts and a persistent `00_index.md` run ledger.
- Prompt templates for Soul, News Fetcher, Pitch, Financial Analyst, Competitor Monitor, Beneficial Related, PSC, Writer, and Editor.
- A dependency-free Python run manager for creating, inspecting, and advancing audit runs.
- A responsive browser demo that visualizes progress, evidence checks, and all nine deliverables.
- Security notes that separate public workflow material from credentials, user data, and private research.

### Changed

- Replaced the older ten-module description with the current nine-step contract.
- Moved from JSON-first module promises to readable Markdown artifacts.
- Removed publishing and platform routing from the core research workflow.
- Reframed completion as an auditable state, not the mere presence of generated text.

### Preserved

- `11-lab-chain.md` remains an optional experimental extension.
- Earlier interactive demos remain available for historical reference.
