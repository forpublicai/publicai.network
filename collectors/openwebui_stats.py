#!/usr/bin/env python3
"""Build the chat.publicai.co (Open WebUI) user file for the Public AI Progress dashboard.

Per month: new sign-ups, total registered users at month end, and active users
(people who sent at least one message), messages and chats. The same figures
for three windows: last 30 days, past 12 months, since launch.

Reads only counts. No names, emails or other personal fields are kept.

  python3 openwebui_stats.py --api https://chat.publicai.co --as-of 2026-11-16 --out openwebui_stats.json

Needs an admin API key, from $OPENWEBUI_API_KEY or injected by a network proxy.
Uses:
  GET /api/v1/users/?page=N&order_by=created_at&direction=asc   (30 users a page)
  GET /api/v1/analytics/summary?start_date=&end_date=            (epoch seconds)
Sign-ups are counted by binary search over the sorted user list, so each date
boundary costs about 15 requests instead of reading every user.
Standard library only.
"""
import argparse
import datetime as dt
import json
import math
import os
import urllib.parse
import urllib.request

PAGE = 30
LAUNCH = "2025-09-02"


def get(base, path, params=None):
    url = base.rstrip("/") + path + ("?" + urllib.parse.urlencode(params) if params else "")
    # Cloudflare refuses Python's default user agent (error 1010).
    headers = {"Accept": "application/json", "User-Agent": "publicai-progress-dashboard/1.0"}
    key = os.environ.get("OPENWEBUI_API_KEY")
    if key:
        headers["Authorization"] = key if key.startswith("Bearer ") else "Bearer " + key
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=180) as resp:
        return json.load(resp)


class Users:
    """Sign-up timestamps from the user list sorted oldest first, fetched lazily."""

    def __init__(self, base):
        self.base, self.pages = base, {}
        first = self.page(1)
        self.total = first["total"]
        self.npages = math.ceil(self.total / PAGE)

    def page(self, n):
        if n not in self.pages:
            body = get(self.base, "/api/v1/users/", {"page": n, "order_by": "created_at", "direction": "asc"})
            self.pages[n] = {"total": body["total"], "created": [int(u["created_at"]) for u in body["users"]]}
        return self.pages[n]

    def count_before(self, ts):
        """How many users signed up before epoch second ts."""
        lo, hi = 1, self.npages
        if self.page(hi)["created"][-1] < ts:
            return self.total
        while lo < hi:  # first page whose last sign-up is at or after ts
            mid = (lo + hi) // 2
            if self.page(mid)["created"][-1] < ts:
                lo = mid + 1
            else:
                hi = mid
        return (lo - 1) * PAGE + sum(1 for c in self.page(lo)["created"] if c < ts)


def epoch(day):
    return int(dt.datetime.fromisoformat(day).replace(tzinfo=dt.timezone.utc).timestamp())


def month_starts(first, last):
    y, m = first.year, first.month
    while (y, m) <= (last.year, last.month):
        yield dt.date(y, m, 1)
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api", required=True)
    ap.add_argument("--as-of", default=dt.date.today().isoformat(), help="last day counted, inclusive")
    ap.add_argument("--first-month", default="2025-08-01")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    as_of = dt.date.fromisoformat(a.as_of)
    end = as_of + dt.timedelta(days=1)  # exclusive
    users = Users(a.api)

    def summary(start, stop):
        s = get(a.api, "/api/v1/analytics/summary", {"start_date": epoch(start), "end_date": epoch(stop) - 1})
        return {"active_users": s["total_users"], "messages": s["total_messages"], "chats": s["total_chats"]}

    months = []
    for start in month_starts(dt.date.fromisoformat(a.first_month), as_of):
        stop = min(dt.date(start.year + start.month // 12, start.month % 12 + 1, 1), end)
        before, after = users.count_before(epoch(start.isoformat())), users.count_before(epoch(stop.isoformat()))
        row = {"month": start.isoformat()[:7], "new_users": after - before, "total_users": after}
        row.update(summary(start.isoformat(), stop.isoformat()))
        months.append(row)
        print(row)

    windows = []
    for name, start in [("Last 30 days", as_of - dt.timedelta(days=29)),
                        ("Past 12 months", as_of - dt.timedelta(days=365)),
                        ("Since launch", dt.date.fromisoformat(LAUNCH))]:
        row = {"window": name, "from": start.isoformat(), "to": as_of.isoformat(),
               "new_users": users.count_before(epoch(end.isoformat())) - users.count_before(epoch(start.isoformat()))}
        row.update(summary(start.isoformat(), end.isoformat()))
        windows.append(row)
        print(row)

    with open(__file__, encoding="utf-8") as fh:
        code = fh.read()
    meta = [
        {"label": "openwebui_stats.py", "value": code, "type": "code", "lang": "python"},
        {"label": "Input", "value": f"{a.api} user list and analytics summary, through {a.as_of}"},
        {"label": "Registered users at run time", "value": str(users.total)},
        {"label": "Requests made", "value": f"{len(users.pages)} user-list pages, {len(months) + len(windows)} summaries"},
        {"label": "Generated", "value": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")},
    ]
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump({"months": months, "windows": windows, "meta": meta}, fh, indent=1)
    print("Wrote", a.out)


if __name__ == "__main__":
    main()
