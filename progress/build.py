#!/usr/bin/env python3
"""Build data/progress.json, the data behind every site's /progress page.

Reads metrics.json (the list of metrics and pillars), snapshots/ (pulled
counts) and records/ (hand-kept lists), and precomputes every figure the
page shows: pillar toplines, window totals, monthly series and tables.
Sites render this file at build time, so they need no API access.

  python3 build.py --as-of 2026-11-16

Windows: last 30 days and past 12 months end on --as-of (inclusive);
since launch starts on 2 Sep 2025.
"""
import argparse
import collections
import datetime as dt
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "snapshots")
REC = os.path.join(HERE, "records")
LAUNCH = "2025-09-02"
SERIES_FOR = {"users": "signups", "visitors_co": "visitors", "news_mentions": "news",
              "community_active": "slack_posting", "community_joined": "slack_joined"}


def load(name, folder=SNAP):
    with open(os.path.join(folder, name), encoding="utf-8") as fh:
        return json.load(fh)


def rows_of(doc):
    return doc["rows"] if isinstance(doc, dict) else doc


def litellm_rows(path):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    cols = doc["columns"]
    return [dict(zip(cols, r)) for r in doc["rows"]]


def months(first, last):
    y, m = int(first[:4]), int(first[5:7])
    while f"{y:04d}-{m:02d}" <= last:
        yield f"{y:04d}-{m:02d}"
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--as-of", required=True)
    ap.add_argument("--litellm", default=os.path.join(SNAP, "litellm_daily.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "data", "progress.json"))
    a = ap.parse_args()

    as_of = dt.date.fromisoformat(a.as_of)
    d30 = (as_of - dt.timedelta(days=29)).isoformat()
    y1 = (as_of - dt.timedelta(days=365)).isoformat()
    end = a.as_of
    windows = {"d30": d30, "y1": y1, "launch": LAUNCH}
    last_month = end[:7]

    def in_window(day, start):
        return start <= day <= end

    def count(dates, start):
        return sum(1 for d in dates if in_window(d, start))

    hello = [r["date"] for r in rows_of(load("hello_threads.json"))]
    support = [r["date"] for r in rows_of(load("support_threads.json"))]
    issues = rows_of(load("github_issues.json"))
    co_windows = {r["window"]: r for r in rows_of(load("co_windows.json"))}
    co_monthly = rows_of(load("co_monthly.json"))
    owui = load("openwebui_stats.json")
    owui_windows = {r["window"]: r for r in owui["windows"]}
    owui_key = {"d30": "Last 30 days", "y1": "Past 12 months", "launch": "Since launch"}
    spec = load("metrics.json", HERE)
    coverage = spec["metrics"]
    pubs = [r["date"] for r in rows_of(load("publications.json"))]
    records = {n: rows_of(load(f"{n}.json", REC)) for n in ("milestones", "events", "partners", "mentions", "audience")}
    llm = litellm_rows(a.litellm)
    def optional(name):
        return rows_of(load(name)) if os.path.exists(os.path.join(SNAP, name)) else []

    gdelt, openalex, trends = optional("idea_gdelt.json"), optional("idea_openalex.json"), optional("idea_trends.json")
    hansard, substack = optional("idea_hansard.json"), optional("idea_substack.json")

    def monthly_sum(rows, field, start):
        """Window total from a monthly series, pro-rated by the days of each month
        inside the window. The as-of month only has data up to the as-of date."""
        if not rows:
            return None
        s0, e0, total = dt.date.fromisoformat(start), as_of, 0.0
        for r in rows:
            m0 = dt.date.fromisoformat(r["month"] + "-01")
            m1 = min((m0 + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1), e0)
            if m1 < m0:
                continue
            overlap = (min(m1, e0) - max(m0, s0)).days + 1
            if overlap > 0:
                total += r[field] * overlap / ((m1 - m0).days + 1)
        return round(total)

    def mean_index(start):
        vals = [r["index"] for r in trends if start <= r["week"] <= end]
        return round(sum(vals) / len(vals)) if vals else None

    slack = litellm_rows(os.path.join(SNAP, "slack_daily.json"))  # same columns/rows shape
    slack = [r for r in slack if r["date"] <= end]
    slack_on = {r["date"]: r for r in slack}

    def slack_at(day, field):
        """Value on the last exported day on or before `day`, or None before the export starts."""
        prior = [r for r in slack if r["date"] <= day]
        return prior[-1][field] if prior and day >= slack[0]["date"] else None

    def slack_joined(start):
        before = (dt.date.fromisoformat(start) - dt.timedelta(days=1)).isoformat()
        a0, a1 = slack_at(before, "members"), slack_at(end, "members")
        return a1 - a0 if a0 is not None and a1 is not None else None

    def llm_sum(field, start):
        return sum(float(r[field] or 0) for r in llm if in_window(r["date"], start))

    values = {
        "visitors_co": {k: co_windows[k]["visitors"] if k in co_windows else None for k in windows},
        "users": {k: owui_windows[owui_key[k]]["new_users"] for k in windows},
        "active_users": {k: owui_windows[owui_key[k]]["active_users"] for k in windows},
        "chat_messages": {k: owui_windows[owui_key[k]]["messages"] for k in windows},
        "tokens": {k: int(llm_sum("total_tokens", s)) for k, s in windows.items()},
        "llm_requests": {k: int(llm_sum("requests", s)) for k, s in windows.items()},
        "hello": {k: count(hello, s) for k, s in windows.items()},
        "support": {k: count(support, s) for k, s in windows.items()},
        "issues": {k: count([i["created"] for i in issues], s) for k, s in windows.items()},
        "issues_open": {k: count([i["created"] for i in issues if i["state"] == "open"], s) for k, s in windows.items()},
        "publications": {k: count(pubs, s) for k, s in windows.items()},
        # Slack's rolling 30-day count of people who posted; no 12-month or since-launch equivalent.
        "community_active": {"d30": slack_at(end, "monthly_posting"), "y1": None, "launch": None},
        "community_joined": {k: slack_joined(s) for k, s in windows.items()},
        # GDELT and OpenAlex are monthly: a window counts the months it touches,
        # so "last 30 days" is the as-of month plus the one before.
        "news_mentions": {k: monthly_sum(gdelt, "articles", s) for k, s in windows.items()},
        "papers": {k: monthly_sum(openalex, "works", s) for k, s in windows.items()},
        "search_interest": {k: mean_index(s) for k, s in windows.items()},
        "policy": {k: count([r["date"] for r in hansard], s) for k, s in windows.items()},
    }
    if records["partners"]:
        values["partners"] = {k: count([p["joined"] for p in records["partners"]], s) for k, s in windows.items()}
    if records["events"]:
        values["events"] = {k: count([e["date"] for e in records["events"]], s) for k, s in windows.items()}
    if records["mentions"]:
        values["notable_mentions"] = {k: count([m["date"] for m in records["mentions"]], s) for k, s in windows.items()}
    big = {"tokens"}
    scorecard = []
    for c in coverage:
        v = values.get(c["key"], {})
        scorecard.append({"key": c["key"], "pillar": c["pillar"], "metric": c["metric"], "status": c["status"],
                          "format": "big" if c["key"] in big else "int",
                          **{k: v.get(k) for k in windows}})

    # Monthly series, Sep 2025 to the as-of month.
    span = list(months("2025-09", last_month))
    by_month = collections.defaultdict(lambda: collections.Counter())
    for d in hello:
        by_month["hello"][d[:7]] += 1
    for d in support:
        by_month["support"][d[:7]] += 1
    for i in issues:
        by_month["issues"][i["created"][:7]] += 1
    for d in pubs:
        by_month["publications"][d[:7]] += 1
    for r in co_monthly:
        by_month["visitors"][r["month"]] = r["visitors"]
    for r in owui["months"]:
        by_month["signups"][r["month"]] = r["new_users"]
        by_month["active_users"][r["month"]] = r["active_users"]
        by_month["chat_messages"][r["month"]] = r["messages"]
    # Slack: rolling counts at each month's last exported day; joins and
    # messages only for months the export covers in full.
    for mo in span:
        last = max((r["date"] for r in slack if r["date"][:7] == mo), default=None)
        if not last:
            continue
        by_month["slack_posting"][mo] = slack_on[last]["monthly_posting"]
        by_month["slack_active"][mo] = slack_on[last]["monthly_active"]
        if slack[0]["date"] <= f"{mo}-01":
            by_month["slack_messages"][mo] = sum(r["messages"] for r in slack if r["date"][:7] == mo)
            before = (dt.date.fromisoformat(f"{mo}-01") - dt.timedelta(days=1)).isoformat()
            start = slack_at(before, "members")
            if start is not None:
                by_month["slack_joined"][mo] = slack_on[last]["members"] - start
    for r in gdelt:
        by_month["news"][r["month"]] = r["articles"]
    for r in openalex:
        by_month["papers"][r["month"]] = r["works"]
    weeks = collections.defaultdict(list)
    for r in trends:
        weeks[r["week"][:7]].append(r["index"])
    for mo, vals in weeks.items():
        by_month["search_interest"][mo] = round(sum(vals) / len(vals))
    for r in substack:
        by_month["newsletter_posts"][r["date"][:7]] += 1
    for r in hansard:
        by_month["hansard"][r["date"][:7]] += 1
    owui_tokens = collections.Counter()
    for r in llm:
        by_month["tokens"][r["date"][:7]] += float(r["total_tokens"] or 0)
        by_month["llm_requests"][r["date"][:7]] += float(r["requests"] or 0)
        if r["team"] == "Open WebUI":
            owui_tokens[r["date"][:7]] += float(r["total_tokens"] or 0)
    for mo, n in by_month["chat_messages"].items():
        if n:
            by_month["tokens_per_message"][mo] = round(owui_tokens[mo] / n)
    # Idea series start in 2024, to show the trend before launch.
    long_span = list(months("2024-01", last_month))
    pre_launch = {"news", "papers", "search_interest"}
    series = {name: [{"month": mo, "value": int(by_month[name].get(mo, 0))}
                     for mo in (long_span if name in pre_launch else span)] for name in by_month}

    # LiteLLM tables.
    llm_windows = []
    for label, start in [("Last 30 days", d30), ("Past 12 months", y1), ("Since launch", LAUNCH)]:
        row = {"window": label}
        for f in ["total_tokens", "prompt_tokens", "completion_tokens", "requests", "failed", "spend"]:
            row[f] = round(llm_sum(f, start), 2) if f == "spend" else int(llm_sum(f, start))
        llm_windows.append(row)

    def breakdown(col):
        acc, total = {}, 0
        for r in llm:
            t = float(r["total_tokens"] or 0)
            if not t or not in_window(r["date"], LAUNCH):
                continue
            e = acc.setdefault(r[col], {"name": r[col], "d30": 0, "y1": 0, "launch": 0})
            e["launch"] += t
            total += t
            if r["date"] >= y1:
                e["y1"] += t
            if r["date"] >= d30:
                e["d30"] += t
        out = sorted(acc.values(), key=lambda e: -e["launch"])
        for e in out:
            e["share"] = round(100 * e["launch"] / total, 1)
            for k in ("d30", "y1", "launch"):
                e[k] = int(e[k])
        return out

    repos = collections.OrderedDict()
    for i in issues:
        e = repos.setdefault(i["repo"], {"name": i["repo"], "opened": 0, "open": 0})
        e["opened"] += 1
        e["open"] += i["state"] == "open"
    repo_rows = sorted(repos.values(), key=lambda e: -e["opened"])

    pv = values
    figures = {
        "visitors_30": pv["visitors_co"]["d30"],
        "visitors_avg": round(sum(r["visitors"] for r in co_monthly if y1[:7] < r["month"] < last_month)
                              / max(1, sum(1 for r in co_monthly if y1[:7] < r["month"] < last_month))),
        "tokens_30": pv["tokens"]["d30"],
        "tokens_avg": round(pv["tokens"]["y1"] / 12),
        "users_30": pv["users"]["d30"],
        "active_30": pv["active_users"]["d30"],
        "hello_30": pv["hello"]["d30"],
        "hello_avg": round(pv["hello"]["y1"] / 12, 1),
        "issues_30": pv["issues"]["d30"],
        "issues_avg": round(pv["issues"]["y1"] / 12, 1),
        "slack_posting_30": pv["community_active"]["d30"],
        "slack_active_30": slack_at(end, "monthly_active"),
        "slack_joined_30": pv["community_joined"]["d30"],
        "slack_members": slack_at(end, "enabled_members"),
        "news_30": pv["news_mentions"]["d30"],
        "papers_30": pv["papers"]["d30"],
        "papers_y1": pv["papers"]["y1"],
        "search_y1": pv["search_interest"]["y1"],
        "search_30": pv["search_interest"]["d30"],
        "hansard_total": len(hansard),
        "missing": sum(1 for c in coverage if c["status"] == "Not connected"),
        "total": len(coverage),
    }

    # Pillars: 1-2 topline metrics each, with the past-year monthly average.
    by_key = {r["key"]: r for r in scorecard}
    pillars = []
    for p in spec["pillars"]:
        tops = []
        for key in p["topline"]:
            r = by_key[key]
            # Average of the full months in the past year, from the monthly series.
            # Window totals of unique counts (active users) can't be divided by 12.
            ser = series.get(SERIES_FOR.get(key, key))
            full = [x["value"] for x in ser or [] if y1[:7] < x["month"] < last_month]
            tops.append({"key": key, "metric": r["metric"], "status": r["status"], "format": r["format"],
                         "d30": r.get("d30"), "y1_avg": round(sum(full) / len(full)) if full else None,
                         "launch": r.get("launch")})
        pillars.append({"id": p["id"], "label": p["label"], "question": p["question"], "topline": tops,
                        "connected": sum(1 for c in coverage if c["pillar"] == p["id"] and c["status"] != "Not connected"),
                        "total": sum(1 for c in coverage if c["pillar"] == p["id"])})

    out = {
        "asOf": a.as_of,
        "launch": LAUNCH,
        "windows": {"d30": [d30, end], "y1": [y1, end], "launch": [LAUNCH, end]},
        "figures": figures,
        "pillars": pillars,
        "scorecard": scorecard,
        "milestones": sorted(records["milestones"], key=lambda m: m["date"]),
        "series": series,
        "tables": {
            "llm_windows": llm_windows,
            "llm_family": breakdown("family"),
            "llm_team": breakdown("team"),
            "repos": repo_rows,
            "coverage": [{"pillar": c["pillar"], "metric": c["metric"], "status": c["status"], "source": c["source"],
                          "have": c["have"], "next": c["next"]}
                         for c in coverage],
        },
    }
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("Wrote", os.path.normpath(a.out))


if __name__ == "__main__":
    main()
