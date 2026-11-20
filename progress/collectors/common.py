"""Shared helpers for the collectors: polite HTTP with retries, and snapshot output.

Standard library only. Every request sends its own User-Agent, because
Cloudflare (error 1010) blocks Python's default one. Keys are never read here:
they come from the network proxy, or from the caller as headers.
"""
import datetime as dt
import json
import time
import urllib.error
import urllib.request

UA = "publicai-progress/0.1 (+https://github.com/forpublicai/progress)"
_last = {}


def get(url, headers=None, min_interval=0.0, retries=5, backoff=10.0, timeout=90):
    """GET a URL and return the body as text. Waits min_interval seconds between
    calls to the same host, and backs off on 429, 5xx and dropped connections."""
    host = url.split("/")[2]
    for attempt in range(retries):
        wait = min_interval - (time.time() - _last.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        _last[host] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code != 429 and e.code < 500:
                raise
            err = f"HTTP {e.code}"
        except (urllib.error.URLError, ConnectionError, TimeoutError) as e:
            err = str(e)
        if attempt == retries - 1:
            raise RuntimeError(f"{url}: gave up after {retries} tries ({err})")
        time.sleep(backoff * (attempt + 1))


def get_json(url, **kw):
    return json.loads(get(url, **kw))


def write_rows(path, about, rows):
    """Write {"about", "rows"} with one row per line, so refreshes diff cleanly."""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write('{"about": %s,\n "rows": [\n' % json.dumps(about, ensure_ascii=False))
        fh.write(",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in rows))
        fh.write("\n ]}\n")
    print(f"Wrote {path}: {len(rows)} rows")


def months(first, last):
    """Yield YYYY-MM from first to last inclusive."""
    y, m = int(first[:4]), int(first[5:7])
    while f"{y:04d}-{m:02d}" <= last[:7]:
        yield f"{y:04d}-{m:02d}"
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def month_end(month):
    y, m = int(month[:4]), int(month[5:7])
    nxt = f"{y + 1:04d}-01" if m == 12 else f"{y:04d}-{m + 1:02d}"
    return (dt.date.fromisoformat(nxt + "-01") - dt.timedelta(days=1)).isoformat()
