#!/usr/bin/env python3
"""
Sync homepage events in index.md.

What this script does:
1) Moves old entries from "Upcoming events" to "Past events".
2) Adds new upcoming entries by scraping a public Luma calendar page.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import List, Optional


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_MD_PATH = os.path.join(ROOT, "index.md")
DEFAULT_LUMA_PUBLIC_CALENDAR_URL = "https://luma.com/forpublicai"


MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


@dataclass
class MarkdownEventRow:
    raw_line: str
    date_text: str
    event_cell: str
    location_cell: str
    start_date: Optional[dt.date]

    @property
    def key(self) -> str:
        url = extract_first_url(self.event_cell)
        if url:
            return f"url:{url.lower()}"
        return f"title:{strip_markdown(self.event_cell).lower()}|date:{self.date_text.lower()}"


@dataclass
class LumaEvent:
    start_date: dt.date
    title: str
    url: Optional[str]
    location: str

    @property
    def key(self) -> str:
        if self.url:
            return f"url:{self.url.lower()}"
        return f"title:{self.title.lower()}|date:{self.start_date.isoformat()}"


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def find_section(lines: List[str], heading: str) -> int:
    for i, line in enumerate(lines):
        if line.strip() == heading:
            return i
    raise ValueError(f"Heading not found: {heading}")


def parse_table_rows(lines: List[str], start_idx: int, end_idx: int) -> List[MarkdownEventRow]:
    rows: List[MarkdownEventRow] = []
    for line in lines[start_idx:end_idx]:
        if not line.startswith("|"):
            continue
        if line.startswith("| Date |") or line.startswith("|------|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 3:
            continue
        date_text, event_cell, location_cell = parts[0], parts[1], parts[2]
        rows.append(
            MarkdownEventRow(
                raw_line=line,
                date_text=date_text,
                event_cell=event_cell,
                location_cell=location_cell,
                start_date=parse_event_start_date(date_text),
            )
        )
    return rows


def parse_event_start_date(text: str) -> Optional[dt.date]:
    s = text.strip().replace("—", "-").replace("–", "-")

    # Example: Feb 17-21, 2026
    m = re.match(r"^([A-Za-z]{3})\s+(\d{1,2})-\d{1,2},\s*(\d{4})$", s)
    if m:
        mon = MONTHS.get(m.group(1))
        if mon:
            return dt.date(int(m.group(3)), mon, int(m.group(2)))

    # Example: Feb 21, 2026
    m = re.match(r"^([A-Za-z]{3})\s+(\d{1,2}),\s*(\d{4})$", s)
    if m:
        mon = MONTHS.get(m.group(1))
        if mon:
            return dt.date(int(m.group(3)), mon, int(m.group(2)))

    # Example: Feb 21 2026
    m = re.match(r"^([A-Za-z]{3})\s+(\d{1,2})\s+(\d{4})$", s)
    if m:
        mon = MONTHS.get(m.group(1))
        if mon:
            return dt.date(int(m.group(3)), mon, int(m.group(2)))

    # Example: Apr-Jun, 2025 (use first month / day 1)
    m = re.match(r"^([A-Za-z]{3})-[A-Za-z]{3},\s*(\d{4})$", s)
    if m:
        mon = MONTHS.get(m.group(1))
        if mon:
            return dt.date(int(m.group(2)), mon, 1)

    return None


def extract_first_url(text: str) -> Optional[str]:
    m = re.search(r"\((https?://[^)]+)\)", text)
    if m:
        return m.group(1).strip()
    return None


def strip_markdown(text: str) -> str:
    out = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    out = out.replace("*", "")
    out = out.replace("`", "")
    return out.strip()


def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "text/plain,text/calendar,text/html,application/json",
            "User-Agent": "publicai-network-events-sync/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_iso_to_date(value: str) -> Optional[dt.date]:
    if not value:
        return None
    value = value.strip()
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value).date()
    except ValueError:
        return None


def parse_public_luma_initial_data(html: str) -> Optional[dict]:
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, flags=re.S)
    if not m:
        return None
    try:
        payload = json.loads(m.group(1))
    except json.JSONDecodeError:
        return None
    return payload.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data")


def fetch_public_luma_entries(calendar_api_id: str, limit: int = 100) -> List[dict]:
    endpoint = "https://api2.luma.com/calendar/get-items"
    query = f"{endpoint}?calendar_api_id={calendar_api_id}&limit={limit}"
    try:
        raw = fetch_text(query)
        parsed = json.loads(raw)
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"Warning: failed to fetch public calendar items: {e}", file=sys.stderr)
        return []
    entries = parsed.get("entries")
    if isinstance(entries, list):
        return entries
    return []


def derive_event_url(item: dict, event: dict) -> Optional[str]:
    url = item.get("url") or event.get("url")
    if isinstance(url, str) and url.startswith("http"):
        return url

    slug = item.get("slug") or event.get("slug") or event.get("url_slug")
    if isinstance(slug, str) and slug:
        slug = slug.lstrip("/")
        if slug.startswith("http"):
            return slug
        return f"https://lu.ma/{slug}"
    return None


def derive_location(item: dict, event: dict) -> str:
    for key in ("location_name", "location", "venue_name"):
        value = event.get(key) or item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    geo_info = event.get("geo_address_info")
    if isinstance(geo_info, dict):
        pieces = [geo_info.get("city"), geo_info.get("region"), geo_info.get("country")]
        text = ", ".join([p for p in pieces if isinstance(p, str) and p.strip()])
        if text:
            return text

    geo_json = event.get("geo_address_json")
    if isinstance(geo_json, str) and geo_json.strip():
        try:
            parsed = json.loads(geo_json)
            pieces = [parsed.get("city"), parsed.get("region"), parsed.get("country")]
            text = ", ".join([p for p in pieces if isinstance(p, str) and p.strip()])
            if text:
                return text
        except json.JSONDecodeError:
            pass

    if event.get("zoom_meeting_url") or event.get("meeting_url"):
        return "Online"
    return "Online"


def parse_luma_events_from_entries(entries: List[dict]) -> List[LumaEvent]:
    results: List[LumaEvent] = []
    for item in entries:
        if not isinstance(item, dict):
            continue
        event = item.get("event")
        if not isinstance(event, dict):
            event = item

        start_date = parse_iso_to_date(event.get("start_at") or item.get("start_at") or "")
        title = event.get("name") or item.get("name")
        if not start_date or not isinstance(title, str) or not title.strip():
            continue

        results.append(
            LumaEvent(
                start_date=start_date,
                title=title.strip(),
                url=derive_event_url(item, event),
                location=derive_location(item, event),
            )
        )
    return results


def fetch_luma_events() -> List[LumaEvent]:
    public_url = os.getenv("LUMA_PUBLIC_CALENDAR_URL", DEFAULT_LUMA_PUBLIC_CALENDAR_URL).strip()
    if not public_url:
        public_url = DEFAULT_LUMA_PUBLIC_CALENDAR_URL

    try:
        html = fetch_text(public_url)
    except urllib.error.URLError as e:
        print(f"Warning: failed to fetch public Luma calendar page: {e}", file=sys.stderr)
        return []

    initial_data = parse_public_luma_initial_data(html)
    if not initial_data:
        print("Warning: public Luma page parsed but no initial data found.", file=sys.stderr)
        return []

    calendar = initial_data.get("calendar", {})
    calendar_api_id = calendar.get("api_id")
    if not isinstance(calendar_api_id, str) or not calendar_api_id:
        print("Warning: no calendar_api_id found on public Luma page.", file=sys.stderr)
        return []

    entries = fetch_public_luma_entries(calendar_api_id=calendar_api_id, limit=100)
    events = parse_luma_events_from_entries(entries)
    if not events:
        has_upcoming = bool(initial_data.get("has_upcoming_events"))
        if has_upcoming:
            print(
                "Warning: calendar reports upcoming events but no event entries were returned.",
                file=sys.stderr,
            )
    return events


def format_date_for_row(d: dt.date) -> str:
    return d.strftime("%b %d, %Y").replace(" 0", " ")


def sanitize_cell(text: str) -> str:
    return text.replace("|", "\\|").strip()


def build_markdown_row(event: LumaEvent) -> str:
    date_text = format_date_for_row(event.start_date)
    title = sanitize_cell(event.title)
    location = sanitize_cell(event.location or "Online")
    if event.url:
        event_cell = f"[{title}]({event.url})" + "{:target=\"_blank\" rel=\"noopener\"}"
    else:
        event_cell = title
    return f"| {date_text} | {event_cell} | {location} |\n"


def main() -> int:
    text = read_file(INDEX_MD_PATH)
    lines = text.splitlines(keepends=True)

    upcoming_heading = find_section(lines, "### Upcoming events")
    past_heading = find_section(lines, "### Past events")

    # Upcoming table starts after heading and blank line, with header + separator + rows.
    upcoming_table_start = upcoming_heading + 1
    while upcoming_table_start < len(lines) and not lines[upcoming_table_start].startswith("| Date |"):
        upcoming_table_start += 1
    if upcoming_table_start >= len(lines):
        raise ValueError("Upcoming events table header not found.")

    upcoming_rows_start = upcoming_table_start + 2
    upcoming_rows_end = past_heading
    while upcoming_rows_end > upcoming_rows_start and lines[upcoming_rows_end - 1].strip() == "":
        upcoming_rows_end -= 1

    past_table_start = past_heading + 1
    while past_table_start < len(lines) and not lines[past_table_start].startswith("| Date |"):
        past_table_start += 1
    if past_table_start >= len(lines):
        raise ValueError("Past events table header not found.")

    past_rows_start = past_table_start + 2
    past_rows_end = len(lines)
    # Past events ends when the next level-2 heading starts.
    for i in range(past_rows_start, len(lines)):
        if lines[i].startswith("## "):
            past_rows_end = i
            break

    upcoming_rows = parse_table_rows(lines, upcoming_rows_start, upcoming_rows_end)
    past_rows = parse_table_rows(lines, past_rows_start, past_rows_end)
    today = dt.date.today()

    moved_to_past: List[MarkdownEventRow] = []
    kept_upcoming: List[MarkdownEventRow] = []
    for row in upcoming_rows:
        if row.start_date and row.start_date < today:
            moved_to_past.append(row)
        else:
            kept_upcoming.append(row)

    existing_keys = {r.key for r in kept_upcoming}
    luma_events = [e for e in fetch_luma_events() if e.start_date >= today and e.start_date.year < 2100]

    for ev in sorted(luma_events, key=lambda e: e.start_date):
        if ev.key in existing_keys:
            continue
        kept_upcoming.append(
            MarkdownEventRow(
                raw_line=build_markdown_row(ev),
                date_text=format_date_for_row(ev.start_date),
                event_cell=ev.title,
                location_cell=ev.location,
                start_date=ev.start_date,
            )
        )
        existing_keys.add(ev.key)

    # Sort upcoming ascending by date when known, keep unknowns at bottom.
    kept_upcoming.sort(key=lambda r: (r.start_date is None, r.start_date or dt.date.max))

    # Place moved rows at top of past events (most recent first), then existing past.
    moved_to_past.sort(key=lambda r: r.start_date or dt.date.min, reverse=True)
    new_past_rows = moved_to_past + past_rows

    new_lines = []
    new_lines.extend(lines[:upcoming_rows_start])
    new_lines.extend([r.raw_line if r.raw_line.endswith("\n") else r.raw_line + "\n" for r in kept_upcoming])
    new_lines.extend(lines[upcoming_rows_end:past_rows_start])
    new_lines.extend([r.raw_line if r.raw_line.endswith("\n") else r.raw_line + "\n" for r in new_past_rows])
    new_lines.extend(lines[past_rows_end:])

    new_text = "".join(new_lines)
    if new_text != text:
        write_file(INDEX_MD_PATH, new_text)
        print("Updated index.md events.")
    else:
        print("No event updates needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
