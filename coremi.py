#!/usr/bin/env python3
"""Small, dependency-free run manager for the public COREMI workflow."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import unicodedata
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
PROMPT_DIR = ROOT / "prompts"

STEPS = (
    (1, "Soul", "01_soul.md", "01-soul.md"),
    (2, "News Fetcher", "02_fetcher.md", "02-news-fetcher.md"),
    (3, "Pitch", "03_pitch.md", "03-pitch.md"),
    (4, "Financial Analyst", "04_financial_analyst.md", "04-financial-analyst.md"),
    (5, "Competitor Monitor", "05_competitor_monitor.md", "05-competitor-monitor.md"),
    (6, "Beneficial Related", "06_beneficial_related.md", "06-beneficial-related.md"),
    (7, "PSC Engine", "07_psc.md", "07-psc.md"),
    (8, "Writer", "08_writer.md", "08-writer.md"),
    (9, "Editor", "09_editor.md", "09-editor.md"),
)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return slug[:56] or "coremi-run"


def resolve_run(value: str | Path) -> Path:
    candidate = Path(value).expanduser()
    if not candidate.is_absolute():
        candidate = (ROOT / candidate).resolve()
    if not candidate.is_dir() or not (candidate / "00_request.md").exists():
        raise SystemExit(f"Not a COREMI run directory: {candidate}")
    return candidate


def step_status(run_dir: Path, filename: str) -> str:
    artifact = run_dir / filename
    if not artifact.exists():
        return "pending"
    text = artifact.read_text(encoding="utf-8", errors="replace").strip()
    return "complete" if text else "empty"


def write_index(run_dir: Path) -> None:
    request = (run_dir / "00_request.md").read_text(encoding="utf-8", errors="replace")
    title_match = re.search(r"^# Request\n\n(.+)$", request, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else run_dir.name
    states = [(number, name, filename, step_status(run_dir, filename)) for number, name, filename, _ in STEPS]
    complete = sum(state == "complete" for _, _, _, state in states)
    overall = "complete" if complete == len(STEPS) else "in progress"
    rows = [
        "# COREMI Run Index",
        "",
        f"- **Question:** {title}",
        f"- **Status:** {overall}",
        f"- **Progress:** {complete}/9",
        f"- **Updated:** {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "",
        "| Step | Agent | Status | Artifact |",
        "|---:|---|---|---|",
    ]
    icons = {"complete": "complete", "pending": "pending", "empty": "empty"}
    for number, name, filename, state in states:
        rows.append(f"| {number}/9 | {name} | {icons[state]} | [{filename}](./{filename}) |")
    rows.extend(
        [
            "",
            "## Audit Rule",
            "",
            "A stage is complete only when its Markdown artifact exists and contains substantive output.",
            "Generated text is not automatically verified evidence.",
            "",
        ]
    )
    (run_dir / "00_index.md").write_text("\n".join(rows), encoding="utf-8")


def command_new(args: argparse.Namespace) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = DATA_DIR / f"{timestamp}_{slugify(args.question)}"
    run_dir.mkdir()
    request = [
        "# Request",
        "",
        args.question.strip(),
        "",
        "## Source material",
        "",
    ]
    if args.source:
        request.extend(f"- {source}" for source in args.source)
    else:
        request.append("- None supplied. The News Fetcher must locate and label sources.")
    request.extend(
        [
            "",
            "## Requested output",
            "",
            args.output.strip(),
            "",
        ]
    )
    (run_dir / "00_request.md").write_text("\n".join(request), encoding="utf-8")
    write_index(run_dir)
    print(f"Created {run_dir.relative_to(ROOT)}")
    print("Next: [1/9] Soul")
    print(f"Prompt: {(PROMPT_DIR / STEPS[0][3]).relative_to(ROOT)}")


def command_status(args: argparse.Namespace) -> None:
    if args.run:
        run_dirs = [resolve_run(args.run)]
    else:
        run_dirs = sorted(
            (path for path in DATA_DIR.glob("*") if (path / "00_request.md").exists()),
            reverse=True,
        )
    if not run_dirs:
        print("No runs found. Start one with: python3 coremi.py new \"your question\"")
        return
    for run_dir in run_dirs:
        write_index(run_dir)
        complete = sum(step_status(run_dir, filename) == "complete" for _, _, filename, _ in STEPS)
        print(f"{run_dir.relative_to(ROOT)}  {complete}/9")
        if args.run:
            for number, name, filename, _ in STEPS:
                print(f"  [{number}/9] {name:<20} {step_status(run_dir, filename):<8} {filename}")


def command_next(args: argparse.Namespace) -> None:
    run_dir = resolve_run(args.run)
    for number, name, filename, prompt in STEPS:
        if step_status(run_dir, filename) != "complete":
            print(f"[{number}/9] {name}")
            print(f"Input ledger: {run_dir / '00_index.md'}")
            print(f"Prompt: {PROMPT_DIR / prompt}")
            print(f"Output: {run_dir / filename}")
            return
    print("All nine stages are complete.")


def command_record(args: argparse.Namespace) -> None:
    run_dir = resolve_run(args.run)
    try:
        _, name, filename, _ = STEPS[args.step - 1]
    except IndexError as error:
        raise SystemExit("Step must be between 1 and 9.") from error
    source = Path(args.file).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Artifact not found: {source}")
    target = run_dir / filename
    if target.exists() and not args.force:
        raise SystemExit(f"Artifact already exists: {target}. Use --force to replace it.")
    shutil.copyfile(source, target)
    write_index(run_dir)
    print(f"[{args.step}/9] {name}: recorded {target}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="COREMI nine-step audit run manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="create a new audit run")
    new_parser.add_argument("question", help="research question or news lead")
    new_parser.add_argument("--source", action="append", default=[], help="source URL or local path")
    new_parser.add_argument("--output", default="A source-grounded research draft and final edit.")
    new_parser.set_defaults(func=command_new)

    status_parser = subparsers.add_parser("status", help="show run status")
    status_parser.add_argument("run", nargs="?", help="run directory")
    status_parser.set_defaults(func=command_status)

    next_parser = subparsers.add_parser("next", help="show the next incomplete stage")
    next_parser.add_argument("run", help="run directory")
    next_parser.set_defaults(func=command_next)

    record_parser = subparsers.add_parser("record", help="record a completed Markdown artifact")
    record_parser.add_argument("run", help="run directory")
    record_parser.add_argument("step", type=int, help="stage number, 1 through 9")
    record_parser.add_argument("file", help="Markdown file to record")
    record_parser.add_argument("--force", action="store_true", help="replace an existing artifact")
    record_parser.set_defaults(func=command_record)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
