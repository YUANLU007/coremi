"""
COREMI Module 2: News Fetcher
=============================
Fetches, scores, and filters news from verified sources.
Output: filtered_news.json — top 15 scored stories.

Usage:
    python fetch.py --hours 6 --output filtered_news.json
    python fetch.py --hours 24 --sources reuters ft techcrunch
"""

import feedparser
import requests
import json
import argparse
from datetime import datetime, timedelta, timezone

# ─────────────────────────────────────────────
# RSS SOURCE LIST
# ─────────────────────────────────────────────
SOURCES = {
    "reuters_top":     "https://feeds.reuters.com/reuters/topNews",
    "reuters_tech":    "https://feeds.reuters.com/reuters/technologyNews",
    "reuters_biz":     "https://feeds.reuters.com/reuters/businessNews",
    "techcrunch":      "https://techcrunch.com/feed/",
    "theverge":        "https://www.theverge.com/rss/index.xml",
    "ars_technica":    "https://feeds.arstechnica.com/arstechnica/index",
    "ft":              "https://www.ft.com/rss/home",
    "guardian_biz":    "https://www.theguardian.com/business/rss",
}

# ─────────────────────────────────────────────
# SCORING WEIGHTS
# ─────────────────────────────────────────────
HIGH_VALUE   = ["exclusive", "investigation", "revealed", "breaking", "独家", "调查", "突发"]
MID_VALUE    = ["controversy", "regulation", "merger", "acquisition", "监管", "并购", "争议"]
LOW_VALUE    = ["announced", "report", "data", "发布", "报告", "数据"]
NEGATIVE     = ["weather", "celebrity", "entertainment", "sports", "娱乐", "明星", "体育"]

SCORES = {kw: 5 for kw in HIGH_VALUE}
SCORES.update({kw: 3 for kw in MID_VALUE})
SCORES.update({kw: 2 for kw in LOW_VALUE})
SCORES.update({kw: -5 for kw in NEGATIVE})

# ─────────────────────────────────────────────
# CORE FUNCTIONS
# ─────────────────────────────────────────────

def score_article(title: str, summary: str) -> tuple[int, list[str]]:
    """Score an article based on keyword matching."""
    text = (title + " " + summary).lower()
    total = 0
    matched = []
    for kw, points in SCORES.items():
        if kw.lower() in text:
            total += points
            matched.append(kw)
    return max(0, total), matched


def parse_date(entry) -> datetime | None:
    """Parse published date from feed entry."""
    for field in ["published_parsed", "updated_parsed"]:
        t = getattr(entry, field, None)
        if t:
            import time
            return datetime(*t[:6], tzinfo=timezone.utc)
    return None


def fetch_source(name: str, url: str, hours: int) -> list[dict]:
    """Fetch and parse a single RSS source."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    articles = []

    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            pub_date = parse_date(entry)
            if pub_date and pub_date < cutoff:
                continue  # Too old

            title   = getattr(entry, "title", "")
            summary = getattr(entry, "summary", "") or getattr(entry, "description", "")
            link    = getattr(entry, "link", "")

            # Filter: minimum content length
            if len(summary) < 300:
                continue

            score, matched = score_article(title, summary)

            articles.append({
                "source": name,
                "title": title,
                "summary": summary[:600],  # Truncate for JSON
                "url": link,
                "published_at": pub_date.isoformat() if pub_date else None,
                "score": score,
                "keywords_matched": matched,
            })
    except Exception as e:
        print(f"[WARN] Failed to fetch {name}: {e}")

    return articles


def fetch_all(hours: int = 6, top_n: int = 15) -> dict:
    """Fetch from all sources, score, and return top N stories."""
    all_articles = []

    for name, url in SOURCES.items():
        print(f"[FETCH] {name}...")
        articles = fetch_source(name, url, hours)
        all_articles.extend(articles)
        print(f"        → {len(articles)} articles")

    # Sort by score descending
    all_articles.sort(key=lambda x: x["score"], reverse=True)

    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "hours_window": hours,
        "total_fetched": len(all_articles),
        "top_stories": all_articles[:top_n],
    }


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="COREMI News Fetcher")
    parser.add_argument("--hours",  type=int, default=6,     help="Lookback window in hours")
    parser.add_argument("--top",    type=int, default=15,    help="Number of top stories to return")
    parser.add_argument("--output", type=str, default="filtered_news.json", help="Output JSON file")
    args = parser.parse_args()

    print(f"\n🔍 COREMI News Fetcher — last {args.hours}h\n")
    result = fetch_all(hours=args.hours, top_n=args.top)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Done. {result['total_fetched']} articles fetched.")
    print(f"   Top {args.top} saved to {args.output}")
    print(f"\nTop 3 stories:")
    for i, story in enumerate(result["top_stories"][:3], 1):
        print(f"  {i}. [{story['score']}pt] {story['title'][:80]}")


if __name__ == "__main__":
    main()
