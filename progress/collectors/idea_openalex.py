#!/usr/bin/env python3
"""Count scholarly works using the phrase "public AI" in title or abstract, per month, from OpenAlex.

OpenAlex needs an API key, which the network proxy injects (or set
OPENALEX_API_KEY). Phrase search in OpenAlex is stemmed, so "public AI" also
matches "public AIs". Recent months grow for a while as OpenAlex indexes works.

  python3 collectors/idea_openalex.py --since 2023-01 --until 2026-11-16 \
      --out snapshots/idea_openalex.json
"""
import argparse
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, month_end, months, write_rows  # noqa: E402

API = "https://api.openalex.org/works"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", default="2023-01")
    ap.add_argument("--until", required=True)
    ap.add_argument("--phrase", default="public AI")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    key = os.environ.get("OPENALEX_API_KEY")
    headers = {"Authorization": f"Bearer {key}"} if key else None
    rows = []
    for mo in months(a.since, a.until):
        f = (f'title_and_abstract.search:"{a.phrase}",from_publication_date:{mo}-01,'
             f"to_publication_date:{min(month_end(mo), a.until)}")
        doc = get_json(f"{API}?{urllib.parse.urlencode({'filter': f, 'per_page': 1, 'select': 'id'})}",
                       headers=headers, min_interval=0.2)
        rows.append({"month": mo, "works": doc["meta"]["count"]})
    about = (f'Works in OpenAlex with the phrase "{a.phrase}" in the title or abstract, by publication '
             f"month, through {a.until}. Papers, preprints, reports and book chapters. Recent months fill in "
             "as OpenAlex indexes new works.")
    write_rows(a.out, about, rows)


if __name__ == "__main__":
    main()
