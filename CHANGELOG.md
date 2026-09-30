# Changelog

All notable public changes to COREMI are documented here.

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
