#!/usr/bin/env python3
"""Count online news articles using the exact phrase "public AI", per month, from GDELT.

GDELT's DOC 2.0 API (timelinevolraw) gives the number of matching articles in
its worldwide news crawl, and the total it crawled, per day. The phrase also
catches "public AI tools" and companies named PublicAI, so read it as a trend,
not a count of articles about Public AI. GDELT allows one request every 5
seconds and drops connections often, so this is slow and retries. Months
already in --out are kept and skipped, except the last two, which are
refetched; so an interrupted run picks up where it stopped. From a shared
cloud IP GDELT can refuse every request (HTTP 429): run it from a GitHub
Action or a laptop instead.

  python3 collectors/idea_gdelt.py --since 2024-01 --until 2026-11-16 \
      --out snapshots/idea_gdelt.json
"""
import argparse
import json
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, month_end, months, write_rows  # noqa: E402

API = "https://api.gdeltproject.org/api/v2/doc/doc"


def month_counts(month, until, phrase):
    start = month.replace("-", "") + "01000000"
    end = min(month_end(month), until).replace("-", "") + "235959"
    q = urllib.parse.urlencode({"query": f'"{phrase}"', "mode": "timelinevolraw", "format": "json",
                                "startdatetime": start, "enddatetime": end, "timelinesmooth": 0})
    doc = get_json(f"{API}?{q}", min_interval=6, retries=8, backoff=20)
    data = (doc.get("timeline") or [{"data": []}])[0]["data"]
    return sum(d["value"] for d in data), sum(d["norm"] for d in data)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", default="2024-01")
    ap.add_argument("--until", required=True, help="last day to count, YYYY-MM-DD")
    ap.add_argument("--phrase", default="public AI")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    done = {}
    if os.path.exists(a.out):
        with open(a.out, encoding="utf-8") as fh:
            done = {r["month"]: r for r in json.load(fh)["rows"]}
    todo = list(months(a.since, a.until))
    keep = set(todo[:-2])
    about = (f'Online news articles in GDELT\'s crawl using the exact phrase "{a.phrase}", per month, '
             f"through {a.until}. all_articles is everything GDELT crawled that month, for normalising. "
             "The phrase also matches \"public AI tools\" and companies named PublicAI.")
    for mo in todo:
        if mo in keep and mo in done:
            continue
        n, total = month_counts(mo, a.until, a.phrase)
        done[mo] = {"month": mo, "articles": n, "all_articles": total}
        print(mo, n, file=sys.stderr)
        write_rows(a.out, about, [done[m] for m in sorted(done)])  # save as we go


if __name__ == "__main__":
    main()
