#!/usr/bin/env python3
"""Count the publications listed on publicai.network/publications.

Reads publications.md from a checkout of forpublicai/publicai.network (a
markdown table: Date | Title | Description) and writes one row per entry with
its date, type tag and title. Dates like "May 2025" are dated to the 1st.

  python3 collectors/publications.py --md ../publicai.network/publications.md \
      --out snapshots/publications.json
"""
import argparse
import datetime as dt
import json
import re

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATE = re.compile(r"^\|\s*([A-Za-z]{3})[a-z]*\.?\s+(?:(\d{1,2}),\s*)?(\d{4})")
TAG = re.compile(r'<span class="tag">([^<]+)</span>')
TITLE = re.compile(r"\[([^\]]+)\]\(")


def parse(text):
    for line in text.splitlines():
        m = DATE.match(line)
        if not m or m.group(1).lower() not in MONTHS:
            continue
        day = int(m.group(2) or 1)
        date = dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], day).isoformat()
        tag = TAG.search(line)
        title = TITLE.search(line)
        yield {"date": date, "type": tag.group(1).strip() if tag else "Other",
               "title": title.group(1).strip() if title else ""}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    with open(a.md, encoding="utf-8") as fh:
        rows = sorted(parse(fh.read()), key=lambda r: r["date"])
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump({"source": "publicai.network/publications.md", "rows": rows}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"Wrote {len(rows)} publications to {a.out}")


if __name__ == "__main__":
    main()
