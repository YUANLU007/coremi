#!/usr/bin/env python3
"""Compatibility entry point for the renamed News Harness runner."""

from news_harness import main


if __name__ == "__main__":
    raise SystemExit(main())
