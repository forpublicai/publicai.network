#!/usr/bin/env python3
"""List UK Parliament spoken contributions using the phrase "public AI", from Hansard.

Keeps the sitting date and house only. Hansard's search is word-based, so each
result is checked for the exact phrase.

  python3 collectors/idea_hansard.py --out snapshots/idea_hansard.json
"""
import argparse
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, write_rows  # noqa: E402

API = "https://hansard-api.parliament.uk/search/contributions/Spoken.json"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--phrase", default="public AI")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows, skip, take = [], 0, 50
    while True:
        q = urllib.parse.urlencode({"queryParameters.searchTerm": f'"{a.phrase}"',
                                    "queryParameters.skip": skip, "queryParameters.take": take})
        doc = get_json(f"{API}?{q}", min_interval=0.5)
        for r in doc["Results"]:
            text = (r.get("ContributionTextFull") or r.get("ContributionText") or "").lower()
            if a.phrase.lower() in text:
                rows.append({"date": r["SittingDate"][:10], "house": r["House"]})
        skip += take
        if skip >= doc["TotalResultCount"] or not doc["Results"]:
            break
    rows.sort(key=lambda r: r["date"])
    write_rows(a.out, f'UK Parliament spoken contributions (Hansard) containing "{a.phrase}". Date and house only.', rows)


if __name__ == "__main__":
    main()
