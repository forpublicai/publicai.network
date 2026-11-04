#!/usr/bin/env python3
"""Refresh `_data/updates.yml` for the site-wide updates bar.

Sources:
- Open jobs in `_jobs/` with a recent `date_posted`
- Newly created public repos in the GitHub org
- Upcoming events on the homepage and seminar page
- Posts from https://publicai.substack.com/feed
- Dated rows on `news.md`
- Recent press headlines that mention "public AI"

Usage:
    python3 scripts/sync_updates.py
"""

from __future__ import annotations

import datetime as dt
import email.utils
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Any, Iterable

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(ROOT, "_data", "updates.yml")
DEFAULT_ORG = "forpublicai"
USER_AGENT = "publicai.network-updates-sync/1.0"
API_ACCEPT = "application/vnd.github+json"
API_VERSION = "2022-11-28"
SUBSTACK_FEED = "https://publicai.substack.com/feed"
GOOGLE_NEWS_QUERY = '"public AI" OR "Public AI Network" OR publicai.network'
MAX_ITEMS = 16
TITLE_MAX = 88

JOB_LOOKBACK_DAYS = 90
REPO_LOOKBACK_DAYS = 90
NEWSLETTER_LOOKBACK_DAYS = 180
NEWS_LOOKBACK_DAYS = 120
PRESS_LOOKBACK_DAYS = 21
EVENT_PAST_GRACE_DAYS = 2
EVENT_AHEAD_DAYS = 60
MAX_UPCOMING_EVENTS = 2
MAX_PRESS_ITEMS = 3
MAX_NEWSLETTER_ITEMS = 4

MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


@dataclass(frozen=True)
class Update:
    kind: str
    kind_label: str
    title: str
    url: str
    date: dt.date
    item_id: str


def today() -> dt.date:
    return dt.datetime.now(dt.timezone.utc).date()


def within_days(date: dt.date, days: int, *, now: dt.date | None = None) -> bool:
    now = now or today()
    return (now - date).days <= days


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": API_ACCEPT,
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": USER_AGENT,
    }
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_bytes(url: str, headers: dict[str, str] | None = None) -> bytes:
    req_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/xml, text/xml, application/json, */*",
    }
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    for part in link_header.split(","):
        section = part.strip()
        if 'rel="next"' not in section:
            continue
        start = section.find("<")
        end = section.find(">", start + 1)
        if start != -1 and end != -1:
            return section[start + 1 : end]
    return None


def fetch_json(url: str) -> tuple[Any, str | None]:
    req = urllib.request.Request(url, headers=github_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            return payload, parse_next_link(resp.headers.get("Link"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {e.code} for {url}: {detail}") from e


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:60] or "item"


def truncate_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip()
    if len(title) <= TITLE_MAX:
        return title
    clipped = title[: TITLE_MAX - 1]
    if " " in clipped:
        clipped = clipped.rsplit(" ", 1)[0]
    return clipped.rstrip(" ,;:-") + "…"


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*{1,2}([^*]+)\*{1,2}", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\{:[^}]+\}", "", text)
    return re.sub(r"\s+", " ", text).strip()


def first_url(text: str) -> str | None:
    match = re.search(r"\((https?://[^)\s]+)\)", text)
    if match:
        return match.group(1)
    match = re.search(r"(https?://[^\s)>\"]+)", text)
    if match:
        return match.group(1).rstrip(".,;")
    return None


def parse_front_matter(text: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.S)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def parse_iso_date(value: str) -> dt.date | None:
    value = value.strip()
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value).date()
    except ValueError:
        pass
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def parse_rfc822_date(value: str) -> dt.date | None:
    try:
        parsed = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc).date()


def parse_named_date(text: str) -> dt.date | None:
    text = text.strip().replace("—", "-").replace("–", "-")
    match = re.search(r"([A-Za-z]{3})\s+(\d{1,2})(?:-\d{1,2})?,?\s+(\d{4})", text)
    if match:
        month = MONTHS.get(match.group(1)[:3].lower())
        if month:
            return dt.date(int(match.group(3)), month, int(match.group(2)))
    match = re.search(r"(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", text)
    if match:
        month = MONTHS.get(match.group(2)[:3].lower())
        if month:
            return dt.date(int(match.group(3)), month, int(match.group(1)))
    return None


def yaml_scalar(value: str) -> str:
    if value == "":
        return '""'
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value
    needs_quotes = (
        value != value.strip()
        or value[0] in "-?:{}[]|>&*!%@`'\","
        or any(ch in value for ch in ":#{}[]&*!|>%@`'\"\n")
        or value.lower() in {"true", "false", "null", "yes", "no", "on", "off"}
    )
    if needs_quotes:
        return json.dumps(value, ensure_ascii=False)
    return value


def collect_jobs(now: dt.date) -> list[Update]:
    jobs_dir = os.path.join(ROOT, "_jobs")
    items: list[Update] = []
    if not os.path.isdir(jobs_dir):
        return items
    for name in sorted(os.listdir(jobs_dir)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(jobs_dir, name)
        meta = parse_front_matter(read_text(path))
        if meta.get("status") != "open":
            continue
        posted = parse_iso_date(meta.get("date_posted", ""))
        if posted is None or not within_days(posted, JOB_LOOKBACK_DAYS, now=now):
            continue
        title = meta.get("title") or name.replace(".md", "").replace("-", " ")
        host = meta.get("host")
        if host:
            title = f"{title} ({host})"
        slug = name[: -len(".md")]
        items.append(
            Update(
                kind="job",
                kind_label="Job",
                title=truncate_title(f"Hiring: {title}"),
                url=f"/jobs/{slug}/",
                date=posted,
                item_id=f"job:{slug}",
            )
        )
    return items


def collect_site_news(now: dt.date) -> list[Update]:
    path = os.path.join(ROOT, "news.md")
    if not os.path.exists(path):
        return []
    items: list[Update] = []
    year: int | None = None
    for line in read_text(path).splitlines():
        year_match = re.match(r"^\|\s*\*\*(\d{4})\*\*", line)
        if year_match:
            year = int(year_match.group(1))
            continue
        row = re.match(r"^\|\s*(\d{1,2})/(\d{1,2})(?:-\d{1,2})?\s*\|\s*(.+?)\s*\|?\s*$", line)
        if not row or year is None:
            continue
        try:
            date = dt.date(year, int(row.group(1)), int(row.group(2)))
        except ValueError:
            continue
        if not within_days(date, NEWS_LOOKBACK_DAYS, now=now):
            continue
        body = row.group(3).strip()
        body = re.sub(r"^\[[^\]]+\]\s*", "", body)
        title = truncate_title(strip_markdown(body))
        if not title:
            continue
        url = first_url(row.group(3)) or "/news/"
        items.append(
            Update(
                kind="news",
                kind_label="News",
                title=title,
                url=url,
                date=date,
                item_id=f"news:{date.isoformat()}:{slugify(title)}",
            )
        )
    return items


def _event_window(date: dt.date, now: dt.date) -> bool:
    delta = (date - now).days
    return -EVENT_PAST_GRACE_DAYS <= delta <= EVENT_AHEAD_DAYS


def _limit_events(items: list[Update], now: dt.date) -> list[Update]:
    upcoming = sorted((item for item in items if item.date >= now), key=lambda item: item.date)
    recent_past = [item for item in items if item.date < now]
    return upcoming[:MAX_UPCOMING_EVENTS] + recent_past


def collect_homepage_events(now: dt.date) -> list[Update]:
    path = os.path.join(ROOT, "index.md")
    if not os.path.exists(path):
        return []
    text = read_text(path)
    upcoming_match = re.search(
        r"### Upcoming events\n(.*?)(?:\n### |\n## |\Z)",
        text,
        flags=re.S,
    )
    if not upcoming_match:
        return []
    section = upcoming_match.group(1)
    items: list[Update] = []
    for match in re.finditer(
        r"<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>",
        section,
        flags=re.S,
    ):
        date = parse_named_date(re.sub(r"<[^>]+>", "", match.group(1)))
        if date is None or not _event_window(date, now):
            continue
        raw_title = match.group(2)
        title = truncate_title(strip_markdown(re.sub(r"<[^>]+>", "", raw_title)))
        href = re.search(r'href="([^"]+)"', raw_title)
        url = href.group(1) if href else "/#events"
        if not title:
            continue
        items.append(
            Update(
                kind="event",
                kind_label="Event",
                title=title,
                url=url,
                date=date,
                item_id=f"event:{date.isoformat()}:{slugify(title)}",
            )
        )
    return _limit_events(items, now)


def collect_seminars(now: dt.date) -> list[Update]:
    path = os.path.join(ROOT, "seminar.md")
    if not os.path.exists(path):
        return []
    items: list[Update] = []
    for line in read_text(path).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        date = parse_named_date(cells[0])
        if date is None or not _event_window(date, now):
            continue
        seminar = cells[1]
        heading = re.search(r"\*\*([^*]+?)\*\*", seminar)
        if heading:
            title = heading.group(1).rstrip(":")
        else:
            title = strip_markdown(seminar).split(".")[0]
        title = truncate_title(f"Seminar: {title}")
        items.append(
            Update(
                kind="event",
                kind_label="Event",
                title=title,
                url="/seminar/",
                date=date,
                item_id=f"seminar:{date.isoformat()}:{slugify(title)}",
            )
        )
    return _limit_events(items, now)


def collect_posts(now: dt.date) -> list[Update]:
    posts_dir = os.path.join(ROOT, "_posts")
    items: list[Update] = []
    if not os.path.isdir(posts_dir):
        return items
    for name in sorted(os.listdir(posts_dir)):
        if not name.endswith(".md"):
            continue
        meta = parse_front_matter(read_text(os.path.join(posts_dir, name)))
        date_match = re.match(r"^(\d{4}-\d{2}-\d{2})", name)
        date = parse_iso_date(date_match.group(1) if date_match else "")
        if date is None or not within_days(date, NEWS_LOOKBACK_DAYS, now=now):
            continue
        title = meta.get("title") or name
        url = meta.get("permalink") or f"/{name[:11].replace('-', '/')}/{name[11:].replace('.md', '')}/"
        items.append(
            Update(
                kind="news",
                kind_label="News",
                title=truncate_title(title),
                url=url,
                date=date,
                item_id=f"post:{date.isoformat()}:{slugify(title)}",
            )
        )
    return items


def collect_new_repos(now: dt.date) -> list[Update]:
    org = os.getenv("GITHUB_ORG", DEFAULT_ORG).strip() or DEFAULT_ORG
    url = f"https://api.github.com/orgs/{org}/repos?per_page=100&sort=created&direction=desc"
    repos: list[dict[str, Any]] = []
    while url:
        page, next_url = fetch_json(url)
        if not isinstance(page, list):
            raise RuntimeError(f"Unexpected GitHub API response for {url}")
        repos.extend(item for item in page if isinstance(item, dict))
        url = next_url
    items: list[Update] = []
    for repo in repos:
        name = repo.get("name")
        html_url = repo.get("html_url")
        created = parse_iso_date(str(repo.get("created_at") or ""))
        if not isinstance(name, str) or not isinstance(html_url, str) or created is None:
            continue
        if name == ".github" or repo.get("fork") or repo.get("archived") or repo.get("disabled"):
            continue
        if not within_days(created, REPO_LOOKBACK_DAYS, now=now):
            continue
        description = repo.get("description")
        title = f"New repo: {name}"
        if isinstance(description, str) and description.strip():
            title = f"New repo: {name} — {description.strip()}"
        items.append(
            Update(
                kind="repo",
                kind_label="Repo",
                title=truncate_title(title),
                url=html_url,
                date=created,
                item_id=f"repo:{name}",
            )
        )
    return items


def parse_rss_items(raw: bytes) -> list[tuple[str, str, dt.date]]:
    root = ET.fromstring(raw)
    found: list[tuple[str, str, dt.date]] = []
    channel_items = root.findall("./channel/item")
    atom_items = root.findall("{http://www.w3.org/2005/Atom}entry")
    for item in channel_items or atom_items:
        title = html.unescape((item.findtext("title") or item.findtext("{http://www.w3.org/2005/Atom}title") or "").strip())
        link = (item.findtext("link") or "").strip()
        if not link:
            atom_link = item.find("{http://www.w3.org/2005/Atom}link")
            if atom_link is not None:
                link = (atom_link.get("href") or "").strip()
        pub = item.findtext("pubDate") or item.findtext("{http://www.w3.org/2005/Atom}updated") or item.findtext("{http://www.w3.org/2005/Atom}published") or ""
        date = parse_rfc822_date(pub) or parse_iso_date(pub)
        if title and link and date:
            found.append((title, link, date))
    return found


def collect_substack(now: dt.date) -> list[Update]:
    items: list[Update] = []
    for title, link, date in parse_rss_items(fetch_bytes(SUBSTACK_FEED)):
        if not within_days(date, NEWSLETTER_LOOKBACK_DAYS, now=now):
            continue
        items.append(
            Update(
                kind="newsletter",
                kind_label="Newsletter",
                title=truncate_title(title),
                url=link,
                date=date,
                item_id=f"newsletter:{slugify(title)}",
            )
        )
        if len(items) >= MAX_NEWSLETTER_ITEMS:
            break
    return items


def press_score(title: str) -> int:
    text = title.lower()
    if "public ai" not in text:
        return -1
    score = 1
    if "public ai network" in text or "publicai" in text:
        score += 4
    if any(word in text for word in ("infrastructure", "inference", "utility", "project", "service", "dataset", "switzerland", "apertus")):
        score += 2
    if any(word in text for word in ("newsroom", "resume scores", "tools to prepare", "trade secrets")):
        score -= 3
    return score


def collect_press(now: dt.date) -> list[Update]:
    query = urllib.parse.urlencode(
        {
            "q": GOOGLE_NEWS_QUERY,
            "hl": "en-US",
            "gl": "US",
            "ceid": "US:en",
        }
    )
    url = f"https://news.google.com/rss/search?{query}"
    ranked: list[tuple[int, Update]] = []
    for title, link, date in parse_rss_items(fetch_bytes(url, headers={"User-Agent": "Mozilla/5.0 (compatible; publicai.network-sync/1.0)"})):
        score = press_score(title)
        if score < 0 or not within_days(date, PRESS_LOOKBACK_DAYS, now=now):
            continue
        ranked.append(
            (
                score,
                Update(
                    kind="press",
                    kind_label="Press",
                    title=truncate_title(title),
                    url=link,
                    date=date,
                    item_id=f"press:{date.isoformat()}:{slugify(title)}",
                ),
            )
        )
    ranked.sort(key=lambda pair: (pair[0], pair[1].date), reverse=True)
    return [item for _score, item in ranked[:MAX_PRESS_ITEMS]]


def normalize_key(update: Update) -> str:
    return re.sub(r"[^a-z0-9]+", "", update.title.lower())[:48]


def merge_updates(groups: Iterable[list[Update]]) -> list[Update]:
    merged: list[Update] = []
    seen_ids: set[str] = set()
    seen_external_urls: set[str] = set()
    seen_titles: set[str] = set()
    for group in groups:
        for item in group:
            title_key = normalize_key(item)
            external_url = item.url if item.url.startswith("http") else None
            if item.item_id in seen_ids or title_key in seen_titles:
                continue
            if external_url and external_url in seen_external_urls:
                continue
            seen_ids.add(item.item_id)
            seen_titles.add(title_key)
            if external_url:
                seen_external_urls.add(external_url)
            merged.append(item)
    now = today()

    def sort_key(item: Update) -> tuple:
        if item.kind == "event" and item.date >= now:
            return (0, item.date.toordinal(), item.title)
        return (1, -item.date.toordinal(), item.title)

    merged.sort(key=sort_key)
    return merged[:MAX_ITEMS]


def render_yaml(items: list[Update]) -> str:
    lines = [
        "# Auto-generated by scripts/sync_updates.py.",
        "# Do not edit by hand. Re-run the script or the sync-site-data workflow.",
        "",
    ]
    if not items:
        lines.append("[]")
        lines.append("")
        return "\n".join(lines)
    fields = ("kind", "kind_label", "title", "url", "date", "id")
    for i, item in enumerate(items):
        record = {
            "kind": item.kind,
            "kind_label": item.kind_label,
            "title": item.title,
            "url": item.url,
            "date": item.date.isoformat(),
            "id": item.item_id,
        }
        if i:
            lines.append("")
        first = True
        for field in fields:
            prefix = "- " if first else "  "
            lines.append(f"{prefix}{field}: {yaml_scalar(record[field])}")
            first = False
    lines.append("")
    return "\n".join(lines)


def safe_collect(name: str, collector) -> list[Update]:
    try:
        items = collector()
        print(f"{name}: {len(items)} item(s)")
        return items
    except Exception as e:
        print(f"Warning: {name} failed: {e}", file=sys.stderr)
        return []


def main() -> int:
    now = today()
    grouped = [
        safe_collect("jobs", lambda: collect_jobs(now)),
        safe_collect("repos", lambda: collect_new_repos(now)),
        safe_collect("events", lambda: collect_homepage_events(now)),
        safe_collect("seminars", lambda: collect_seminars(now)),
        safe_collect("posts", lambda: collect_posts(now)),
        safe_collect("news.md", lambda: collect_site_news(now)),
        safe_collect("substack", lambda: collect_substack(now)),
        safe_collect("press", lambda: collect_press(now)),
    ]
    items = merge_updates(grouped)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    new_text = render_yaml(items)
    old_text = ""
    if os.path.exists(OUTPUT_PATH):
        old_text = read_text(OUTPUT_PATH)
    if new_text == old_text:
        print(f"No updates-bar changes needed ({len(items)} items).")
        return 0
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Updated {os.path.relpath(OUTPUT_PATH, ROOT)} with {len(items)} items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
