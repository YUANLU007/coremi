# Contributing to COREMI

Welcome. COREMI is an open-source project built by a journalist, designed for builders who believe information should be intelligent, verified, and accessible.

We need developers, domain experts, and people who want to see this exist.

---

## Ways to Contribute

### 1. Code
Pick a module from the [ROADMAP](./ROADMAP.md) marked 📋 and build it.

Every module has:
- A prompt spec in `/prompts/`
- A defined input/output contract
- An open GitHub issue with requirements

### 2. Domain Expertise
Are you a CFA? A journalist? A trader? A researcher?

We need people who can:
- Validate the output quality of each module
- Improve prompts based on professional standards
- Add sources to the source list
- Review financial analysis outputs

Open a Discussion or comment on relevant Issues.

### 3. Documentation & Examples
Real outputs from the system are worth more than 1000 lines of docs.

If you run any module and get output — share it in `/docs/examples/`.

---

## Getting Started

### Prerequisites
- Python 3.10+
- An Anthropic API key (Claude)
- Basic understanding of LLM API calls

### Setup
```bash
git clone https://github.com/[your-username]/coremi.git
cd coremi
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

### First Run (News Fetcher)
```bash
python src/fetcher/fetch.py --hours 6 --output filtered_news.json
```

---

## Contribution Guidelines

### Code Style
- Python 3, type hints preferred
- Clear comments — this codebase will be read by non-engineers
- CLI-first: every module should be runnable from terminal
- Output to JSON — modules are composable

### Pull Requests
1. Fork the repo
2. Create a branch: `git checkout -b feature/module-name`
3. Write clear commit messages
4. Open a PR describing: what you built, how to test it, what's still missing

### Issues
- Bug reports: include input, expected output, actual output
- Feature proposals: explain the use case, not just the feature
- Questions: use Discussions, not Issues

---

## Module Interface Standard

Each module should follow this contract:

**Input**: JSON or CLI args
**Output**: JSON to stdout or file
**Config**: `.env` or `config.yaml`

Example:
```bash
# Fetch news
python src/fetcher/fetch.py --source reuters --hours 6 > news.json

# Score and pitch
python src/pitch/score.py --input news.json --threshold 70 > pitched.json

# Write article
python src/writer/write.py --input pitched.json --style wsj > article.md
```

---

## Contact

- **For technical questions**: Open a GitHub Issue
- **For editorial/domain questions**: Open a GitHub Discussion
- **For investment/partnership**: [Add founder email]

---

*独立 · 独家 · 独到 — Independent · Exclusive · Insightful*
