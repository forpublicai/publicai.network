#!/usr/bin/env python3
"""Count chat.publicai.co (Open WebUI) users by country, from each user's timezone.

Open WebUI stores the timezone the browser reports (an IANA name such as
Europe/Zurich). The tz database maps each zone to a country: zone.tab first,
then links for old names (Asia/Calcutta -> Asia/Kolkata). zone.tab comes
first because newer tz data links some countries' zones to a neighbour's
(Europe/Oslo -> Europe/Berlin). So the country is where the browser's clock
was set, not where someone lives or what passport they hold, and users who
never set one are counted as unknown.

Per country: registered users, sign-ups in the last 30 days, and users active
in the last 30 days. Only these counts are written: no ids, names, emails or
timezones of individual users.

  python3 collectors/openwebui_countries.py --api https://chat.publicai.co \
      --as-of 2026-11-16 --out snapshots/openwebui_countries.json

Needs an Open WebUI admin key, injected by the network proxy or from
$OPENWEBUI_API_KEY. Reads every user, 30 to a page (about 2,000 requests for
60,000 users), 4 at a time. Standard library only.
"""
import argparse
import collections
import concurrent.futures
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import get_json, write_rows  # noqa: E402

TZDIR = os.environ.get("TZDIR", "/usr/share/zoneinfo")


def tz_countries():
    zone = {}
    with open(os.path.join(TZDIR, "zone.tab"), encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("#"):
                cc, _, tz = line.split("\t")[:3]
                zone[tz.strip()] = cc
    links = {}
    with open(os.path.join(TZDIR, "tzdata.zi"), encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("L "):
                _, target, name = line.split()
                links[name] = target
    names = {}
    with open(os.path.join(TZDIR, "iso3166.tab"), encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("#"):
                cc, name = line.rstrip("\n").split("\t")[:2]
                names[cc] = name

    def country(tz):
        seen = 0
        while tz and tz not in zone and tz in links and seen < 5:
            tz, seen = links[tz], seen + 1
        return zone.get(tz)

    return country, names


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api", default="https://chat.publicai.co")
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    key = os.environ.get("OPENWEBUI_API_KEY")
    headers = {"Accept": "application/json"}
    if key:
        headers["Authorization"] = key if key.startswith("Bearer ") else f"Bearer {key}"
    base = a.api.rstrip("/") + "/api/v1/users/?order_by=created_at&direction=asc&page="

    def page(n):
        return get_json(base + str(n), headers=headers, retries=5, backoff=5)["users"]

    first = get_json(base + "1", headers=headers)
    pages = -(-first["total"] // 30)
    end = dt.datetime.combine(dt.date.fromisoformat(a.as_of), dt.time.max, dt.timezone.utc).timestamp()
    start30 = end - 30 * 86400
    country, names = tz_countries()
    reg, new, active = collections.Counter(), collections.Counter(), collections.Counter()
    unmapped = collections.Counter()

    def tally(users):
        for u in users:
            if u["created_at"] > end:
                continue
            tz = (u.get("timezone") or "").strip()
            cc = country(tz) if tz else None
            if tz and not cc:
                unmapped[tz] += 1
            cc = cc or "unknown"
            reg[cc] += 1
            if u["created_at"] > start30:
                new[cc] += 1
            if start30 < (u.get("last_active_at") or 0) <= end:
                active[cc] += 1

    tally(first["users"])
    with concurrent.futures.ThreadPoolExecutor(4) as pool:
        for i, users in enumerate(pool.map(page, range(2, pages + 1)), 2):
            tally(users)
            if i % 200 == 0:
                print(f"page {i}/{pages}", file=sys.stderr)
    if unmapped:
        print("Timezones with no country (counted as unknown):", dict(unmapped), file=sys.stderr)

    rows = [{"country": cc, "name": names.get(cc, "Timezone not set" if cc == "unknown" else cc),
             "users": reg[cc], "new_30": new[cc], "active_30": active[cc]}
            for cc in sorted(reg, key=lambda c: (-reg[c], c))]
    about = (f"chat.publicai.co users by country, as of {a.as_of}, from the timezone each user's browser "
             "reported (IANA zone mapped to a country with the tz database). users = registered; new_30 = "
             "signed up in the last 30 days; active_30 = active in the last 30 days. 'unknown' = no timezone set.")
    write_rows(a.out, about, rows)


if __name__ == "__main__":
    main()
