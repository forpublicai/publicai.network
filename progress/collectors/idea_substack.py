#!/usr/bin/env python3
"""List posts on publicai.substack.com from Substack's archive API.

Subscriber counts are not public: type them into records/audience.json.

  python3 collectors/idea_substack.py --out snapshots/idea_substack.json
"""
import argparse
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, write_rows  # noqa: E402

API = "https://publicai.substack.com/api/v1/archive?sort=new&limit=25"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows, cursor = [], None
    while True:  # pages by cursor; the API rejects offset
        doc = get_json(API + (f"&cursor={urllib.parse.quote(cursor)}" if cursor else ""), min_interval=1)
        rows += [{"date": p["post_date"][:10], "type": p.get("type"), "title": p["title"]} for p in doc["posts"]]
        cursor = doc.get("nextCursor")
        if not cursor or not doc["posts"]:
            break
    rows.sort(key=lambda r: r["date"])
    write_rows(a.out, "Posts on publicai.substack.com (Public AI's newsletter), from the archive API.", rows)


if __name__ == "__main__":
    main()
