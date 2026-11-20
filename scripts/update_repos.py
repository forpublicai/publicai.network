#!/usr/bin/env python3
"""Refresh _data/forpublicai_repos.yml from the GitHub API.

The navbar "Repos" menu (_includes/nav-items.html) groups these repos into
Recently active / Active / Quiet using pushed_at, computed at site build time.

Lists every public, non-archived repo in the forpublicai org, newest push first.
Uses GITHUB_TOKEN if set (higher rate limit); works unauthenticated too.

If the only change is this site's own repo (whose pushed_at moves every time
this script's output is committed), the file is left alone so the scheduled
workflow doesn't commit to itself every day.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

ORG = "forpublicai"
SELF_REPO = "publicai.network"
OUT = Path(__file__).resolve().parent.parent / "_data" / "forpublicai_repos.yml"


def fetch_repos():
    repos, page = [], 1
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "repo-list-updater"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    while True:
        url = f"https://api.github.com/orgs/{ORG}/repos?type=public&per_page=100&page={page}"
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as resp:
            batch = json.load(resp)
        if not batch:
            return repos
        repos.extend(batch)
        page += 1


def q(value):
    # JSON strings are valid YAML double-quoted scalars.
    return json.dumps(value, ensure_ascii=False)


def entry(repo):
    lines = [f"- name: {q(repo['name'])}", f"  url: {repo['html_url']}"]
    if (repo.get("description") or "").strip():
        lines.append(f"  description: {q(repo['description'].strip())}")
    if (repo.get("homepage") or "").strip():
        lines.append(f"  homepage: {q(repo['homepage'].strip())}")
    lines.append(f"  pushed_at: {repo['pushed_at']}")
    lines.append(f"  updated_at: {repo['updated_at']}")
    return "\n".join(lines)


def render(repos):
    return "\n\n".join(entry(r) for r in repos) + "\n"


def main():
    repos = [r for r in fetch_repos() if not r["private"] and not r["archived"]]
    repos.sort(key=lambda r: r["pushed_at"], reverse=True)
    new = render(repos)
    old = OUT.read_text() if OUT.exists() else ""

    def without_self(text):
        return {b for b in text.split("\n\n") if not b.startswith(f'- name: "{SELF_REPO}"')}

    if new == old or ("--force" not in sys.argv and without_self(new) == without_self(old)):
        print("No meaningful changes.")
        return
    OUT.write_text(new)
    print(f"Wrote {len(repos)} repos to {OUT.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
