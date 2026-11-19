#!/usr/bin/env python3
"""Sum the per-model LiteLLM file (raw/litellm_usage.json, from litellm_usage.py)
by date, team and model family into snapshots/litellm_daily.json, the version
that is committed and read by build.py.

  python3 collectors/litellm_daily.py --raw raw/litellm_usage.json --out snapshots/litellm_daily.json
"""
import argparse
import collections
import json

FIELDS = ["requests", "successful", "failed", "prompt_tokens", "completion_tokens", "total_tokens", "spend"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    with open(a.raw, encoding="utf-8") as fh:
        doc = json.load(fh)
    cols = doc["columns"]
    acc = collections.OrderedDict()
    for values in doc["rows"]:
        r = dict(zip(cols, values))
        e = acc.setdefault((r["date"], r["team"], r["family"]), [0] * len(FIELDS))
        for i, f in enumerate(FIELDS):
            e[i] += r[f] or 0
    rows = [list(k) + [round(v, 4) if isinstance(v, float) else v for v in e] for k, e in acc.items() if any(e)]
    source = next((m["value"] for m in doc.get("meta", []) if m.get("label") == "Input"), a.raw)
    out = {"columns": ["date", "team", "family"] + FIELDS, "rows": rows,
           "source": f"{source}, summed by date, team and model family"}
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, separators=(",", ":"))
    print(f"Wrote {len(rows)} rows to {a.out}")


if __name__ == "__main__":
    main()
