#!/usr/bin/env python3
"""Google search interest in "public AI", per week, from Google Trends.

Google Trends has no public API. --api uses the endpoints its own web page
calls, which Google rate-limits and can change without notice; if it fails,
download the CSV from trends.google.com (search "public AI" in quotes,
worldwide, the date range you want, then the download icon) and pass --csv.

The values are an index, not searches: 100 is the peak week in the range and
the rest are relative to it. So the snapshot is rewritten whole each time, and
a longer range rescales every week.

  python3 collectors/idea_trends.py --api --since 2024-01-01 --until 2026-11-16 \
      --out snapshots/idea_trends.json
  python3 collectors/idea_trends.py --csv multiTimeline.csv --out snapshots/idea_trends.json
"""
import argparse
import csv
import datetime as dt
import http.cookiejar
import json
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import write_rows  # noqa: E402

BROWSER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
BASE = "https://trends.google.com/trends"


def from_api(phrase, since, until, geo):
    jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    opener.addheaders = [("User-Agent", BROWSER)]

    def call(url):
        with opener.open(url, timeout=60) as resp:
            body = resp.read().decode("utf-8")
        return json.loads(body[body.index("{"):])  # strips the )]}' guard

    opener.open(f"{BASE}/?geo={geo}", timeout=60).read()  # sets the NID cookie
    req = {"comparisonItem": [{"keyword": f'"{phrase}"', "geo": geo, "time": f"{since} {until}"}],
           "category": 0, "property": ""}
    explore = call(f"{BASE}/api/explore?" + urllib.parse.urlencode({"hl": "en-US", "tz": 0, "req": json.dumps(req)}))
    w = next(x for x in explore["widgets"] if x["id"] == "TIMESERIES")
    data = call(f"{BASE}/api/widgetdata/multiline?" + urllib.parse.urlencode(
        {"hl": "en-US", "tz": 0, "req": json.dumps(w["request"]), "token": w["token"]}))
    return [{"week": dt.datetime.fromtimestamp(int(p["time"]), dt.timezone.utc).date().isoformat(),
             "index": p["value"][0]} for p in data["default"]["timelineData"]]


def from_csv(path):
    rows = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for rec in csv.reader(fh):
            if len(rec) == 2 and rec[0][:4].isdigit():
                rows.append({"week": rec[0][:10], "index": 0 if rec[1].startswith("<") else int(rec[1])})
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--api", action="store_true")
    src.add_argument("--csv")
    ap.add_argument("--since", default="2024-01-01")
    ap.add_argument("--until", default=dt.date.today().isoformat())
    ap.add_argument("--geo", default="", help="'' for worldwide, or a country code such as CH")
    ap.add_argument("--phrase", default="public AI")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = from_api(a.phrase, a.since, a.until, a.geo) if a.api else from_csv(a.csv)
    where = a.geo or "worldwide"
    about = (f'Google Trends search interest in "{a.phrase}" (exact phrase), {where}, per week starting on '
             f"the date shown. An index: 100 is the peak week in {rows[0]['week']} to {rows[-1]['week']}, "
             "not a number of searches. Values under 1 are stored as 0.")
    write_rows(a.out, about, rows)


if __name__ == "__main__":
    main()
