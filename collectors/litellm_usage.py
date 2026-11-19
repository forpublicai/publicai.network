#!/usr/bin/env python3
"""Build the LiteLLM usage file for the Public AI Progress dashboard.

One row per (date, team, model) with requests, tokens and spend, plus a model
family that groups LiteLLM's many aliases of the same model.

Two sources, same output:
  --csv PATH   the "team usage daily with models" export from the LiteLLM admin UI
  --api URL    the LiteLLM proxy (e.g. https://api-internal.publicai.co), read with
               GET /team/daily/activity. The key comes from $LITELLM_API_KEY, or is
               injected by a network proxy. Needs a proxy_admin_viewer key.

  python3 litellm_usage.py --csv export.csv --out litellm_usage.json
  python3 litellm_usage.py --api https://api-internal.publicai.co \
      --start 2025-08-30 --end 2026-11-17 --out litellm_usage.json

Standard library only, so a scheduled task can run it anywhere.
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import urllib.parse
import urllib.request

FIELDS = ["requests", "successful", "failed", "prompt_tokens", "completion_tokens",
          "total_tokens", "spend"]

# First match wins. Matched against the lowercased model name.
FAMILIES = [
    (r"apertus.*(v1\.?5|v15).*70b", "Apertus 1.5 70B"),
    (r"apertus.*(v1\.?5|v15).*8b", "Apertus 1.5 8B"),
    (r"apertus.*70b", "Apertus 70B"),
    (r"apertus.*8b", "Apertus 8B"),
    (r"apertus", "Apertus (unsized alias)"),
    (r"sea-?lion", "SEA-LION"),
    (r"olmo|molmo", "OLMo / Molmo"),
    (r"llama", "Llama"),
    (r"mistral|ministral", "Mistral"),
    (r"dictalm", "DictaLM"),
    (r"bielik", "Bielik"),
    (r"eurollm", "EuroLLM"),
    (r"salamandra|alia-", "ALIA / Salamandra"),
    (r"embed", "Cohere Embed"),
    (r"command", "Cohere Command"),
    (r"gpt-oss", "gpt-oss"),
    (r"qwen", "Qwen"),
    (r"glm", "GLM"),
    (r"kimi", "Kimi"),
]


def family(model, total_tokens):
    name = model.lower()
    for pattern, label in FAMILIES:
        if re.search(pattern, name):
            return label
    return "Other" if total_tokens > 0 else "Unknown model (no tokens)"


def num(value):
    """Parse '1,465.7139' or '' into a number."""
    text = str(value if value is not None else "").replace(",", "").strip()
    if not text:
        return 0
    n = float(text)
    return int(n) if n.is_integer() else n


def from_csv(path):
    cols = {"Requests": "requests", "Successful": "successful", "Failed": "failed",
            "Prompt Tokens": "prompt_tokens", "Completion Tokens": "completion_tokens",
            "Total Tokens": "total_tokens", "Spend ($)": "spend"}
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            row = {"date": r["Date"], "team": r["Team"], "team_id": r["Team ID"],
                   "model": r["Model"]}
            for src, dst in cols.items():
                row[dst] = num(r.get(src))
            yield row


def _get(base, path, params):
    url = base.rstrip("/") + path + "?" + urllib.parse.urlencode(params)
    # Cloudflare refuses Python's default user agent (error 1010).
    headers = {"Accept": "application/json", "User-Agent": "publicai-progress-dashboard/1.0"}
    key = os.environ.get("LITELLM_API_KEY")
    if key:
        headers["Authorization"] = key if key.startswith("Bearer ") else "Bearer " + key
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120) as resp:
        return json.load(resp)


def _pages(base, params):
    page = 1
    while True:
        body = _get(base, "/team/daily/activity", dict(params, page=page, page_size=1000))
        yield body
        meta = body.get("metadata") or {}
        if not meta.get("has_more") and page >= int(meta.get("total_pages") or 1):
            return
        page += 1


def _metrics(m):
    m = m or {}
    return {"requests": num(m.get("api_requests")),
            "successful": num(m.get("successful_requests")),
            "failed": num(m.get("failed_requests")),
            "prompt_tokens": num(m.get("prompt_tokens")),
            "completion_tokens": num(m.get("completion_tokens")),
            "total_tokens": num(m.get("total_tokens")),
            "spend": num(m.get("spend"))}


def from_api(base, start, end):
    """Team x model rows. The endpoint breaks a day down by team or by model, not
    both, so first list the teams, then ask for each team's model breakdown."""
    window = {"start_date": start, "end_date": end}
    teams = {}
    for body in _pages(base, window):
        for day in body.get("results", []):
            for team_id, ent in ((day.get("breakdown") or {}).get("entities") or {}).items():
                alias = ((ent or {}).get("metadata") or {}).get("team_alias")
                teams[team_id] = alias or teams.get(team_id) or team_id
    for team_id, alias in sorted(teams.items()):
        for body in _pages(base, dict(window, team_ids=team_id)):
            for day in body.get("results", []):
                models = (day.get("breakdown") or {}).get("models") or {}
                for model, m in models.items():
                    row = {"date": day["date"], "team": alias, "team_id": team_id, "model": model}
                    row.update(_metrics((m or {}).get("metrics")))
                    yield row


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--csv")
    src.add_argument("--api")
    ap.add_argument("--start", default="2025-08-30")
    ap.add_argument("--end", default=dt.date.today().isoformat())
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    rows = list(from_csv(a.csv) if a.csv else from_api(a.api, a.start, a.end))
    for r in rows:
        r["family"] = family(r["model"], r["total_tokens"])
    rows.sort(key=lambda r: (r["date"], r["team"], r["model"]))
    if not rows:
        sys.exit("No rows read; nothing written.")

    with open(__file__, encoding="utf-8") as fh:
        code = fh.read()
    meta = [
        {"label": "litellm_usage.py", "value": code, "type": "code", "lang": "python"},
        {"label": "Input", "value": os.path.basename(a.csv) if a.csv else f"{a.api} /team/daily/activity, {a.start} to {a.end}"},
        {"label": "Rows", "value": str(len(rows))},
        {"label": "Dates", "value": f"{rows[0]['date']} to {rows[-1]['date']}"},
        {"label": "Generated", "value": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")},
    ]
    cols = ["date", "team", "team_id", "model", "family"] + FIELDS
    out = {"columns": cols, "rows": [[r[c] for c in cols] for r in rows], "meta": meta}
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, separators=(",", ":"))
    print(f"Wrote {len(rows)} rows to {a.out}")


if __name__ == "__main__":
    main()
