#!/usr/bin/env python3
"""Turn a Public AI Slack analytics export into snapshots/slack_daily.json.

Slack has no analytics API below Enterprise Grid, so the input is the CSV
from Workspace settings > Analytics > Overview > Export CSV (one row per day).
Only workspace-wide daily counts are kept: no names, channels or messages.
Rows already in the snapshot are kept, and dates in the new export replace
them, so a short recent export extends the history.

  python3 collectors/slack_analytics.py --csv "Analytics ... .csv" \
      --out snapshots/slack_daily.json
"""
import argparse
import csv
import json
import os

# Snapshot column -> Slack CSV header.
COLUMNS = {
    "date": "Date",
    "members": "Total Members",  # every account ever created, deactivated included
    "enabled_members": "Total Enabled Membership",
    "daily_active": "Daily active people",
    "daily_posting": "Daily people posting messages",
    "weekly_active": "Weekly active people",
    "weekly_posting": "Weekly people posting messages",
    "monthly_active": "Monthly active people",  # rolling 30 days, as Slack counts it
    "monthly_posting": "Monthly people posting messages",
    "messages": "Messages posted by members",
    "messages_public": "Messages in public channels",
}
ABOUT = ("Daily workspace totals from the Slack analytics CSV export (Overview). "
         "monthly_* and weekly_* are Slack's rolling 30- and 7-day unique counts. "
         "members counts every account ever created, deactivated included, so its "
         "daily increase is new accounts.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    rows = {}
    if os.path.exists(a.out):
        with open(a.out, encoding="utf-8") as fh:
            old = json.load(fh)
        rows = {r[0]: r for r in old["rows"]}
    with open(a.csv, encoding="utf-8-sig", newline="") as fh:
        for rec in csv.DictReader(fh):
            missing = [h for h in COLUMNS.values() if h not in rec]
            if missing:
                raise SystemExit(f"Not the Overview export? Missing columns: {missing}")
            row = [rec["Date"]] + [int(float(rec[h] or 0)) for k, h in COLUMNS.items() if k != "date"]
            rows[rec["Date"]] = row
    out = {"about": ABOUT, "columns": list(COLUMNS), "rows": [rows[d] for d in sorted(rows)]}
    # One day per line, so refreshes diff cleanly.
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write('{"about": %s,\n "columns": %s,\n "rows": [\n' % (json.dumps(ABOUT), json.dumps(out["columns"])))
        fh.write(",\n".join("  " + json.dumps(r) for r in out["rows"]))
        fh.write("\n ]}\n")
    print(f"Wrote {a.out}: {len(rows)} days, {out['rows'][0][0]} to {out['rows'][-1][0]}")


if __name__ == "__main__":
    main()
