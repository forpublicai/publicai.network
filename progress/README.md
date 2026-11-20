# Public AI progress

Shared data and components for the `/progress` page on publicai.ch, publicai.co and publicai.network.

The dashboard has three pillars, each with one or two topline stats:

| Pillar | Question | Toplines |
|---|---|---|
| Products | Is the utility being used? | Tokens served; chat.publicai.co active users |
| Movement | Are people and organisations joining? | Partner organisations; active community members |
| Idea | Is public AI spreading as an idea? | News articles using "public AI"; publications on public AI |

Every metric, its pillar, its source and what it takes to connect it are listed in [`metrics.json`](metrics.json). Toplines are set there too.

## Layout

| Path | What it is | Edited by |
|---|---|---|
| `metrics.json` | Pillars, toplines and every metric with its status and next step | hand |
| `collectors/` | Scripts that pull counts from APIs into `snapshots/`. Python standard library only. | code |
| `snapshots/` | Pulled counts. Dates and totals only: no names, emails or message text. | collectors, connectors |
| `records/` | Hand-kept lists: milestones, events, partners, notable mentions, monthly audience counts | pull requests |
| `build.py` | Builds `data/progress.json` from all of the above | code |
| `data/progress.json` | The one file every site renders | `build.py` only |
| `react/` | `Progress.tsx` and `progress.css`, framework-neutral static React | code |

## Refresh

```bash
python3 collectors/litellm_usage.py --csv export.csv --out raw/litellm_usage.json   # or --api https://api-internal.publicai.co
python3 collectors/litellm_daily.py --raw raw/litellm_usage.json --out snapshots/litellm_daily.json
python3 collectors/openwebui_stats.py --api https://chat.publicai.co --as-of 2026-11-16 --out snapshots/openwebui_stats.json
python3 collectors/publications.py --md ../publicai.network/publications.md --out snapshots/publications.json
python3 collectors/slack_analytics.py --csv "Slack analytics export.csv" --out snapshots/slack_daily.json
python3 collectors/idea_openalex.py --until 2026-11-16 --out snapshots/idea_openalex.json   # key injected by the proxy, or OPENALEX_API_KEY
python3 collectors/idea_trends.py --api --until 2026-11-16 --out snapshots/idea_trends.json  # or --csv multiTimeline.csv
python3 collectors/idea_hansard.py --out snapshots/idea_hansard.json
python3 collectors/idea_substack.py --out snapshots/idea_substack.json
python3 collectors/idea_gdelt.py --until 2026-11-16 --out snapshots/idea_gdelt.json        # slow; refused from shared cloud IPs
python3 build.py --as-of 2026-11-16
npm install && npm run static   # rebuilds static/dist/ for publicai.network
```

Idea counts follow the exact phrase "public AI", so they also catch "public AI tools" and companies named PublicAI. Read them as trends. Google Trends is an index (100 = peak week in the range), not a count of searches.

`litellm_usage.py` writes per-model rows to `raw/` (gitignored, about 2 MB). `collectors/litellm_daily.py` sums it by date, team and model family into `snapshots/litellm_daily.json`, the committed version.

Keys come from `LITELLM_API_KEY` and `OPENWEBUI_API_KEY`, or from a network proxy that injects them. Never commit keys.

Visitors (Vercel), email thread dates (Gmail) and GitHub issues are pulled through Claude connectors into `snapshots/` for now.

## Using it in a site

Each site vendors this repo as a git subtree at `progress/`:

```bash
git subtree add --prefix=progress https://github.com/forpublicai/progress main --squash
git subtree pull --prefix=progress https://github.com/forpublicai/progress main --squash
```

- **React sites** (publicai.ch on React Router, publicai.co on Next.js) import `progress/react/Progress.tsx` and `progress/react/progress.css`. Every visible label is a prop, so each locale supplies its own wording.
- **Jekyll** (publicai.network) can read `progress/data/progress.json` as a data file, or include a prebuilt static HTML fragment. Not done yet.

## Records format

Each file in `records/` is `{"about": "...", "rows": [...]}`. The `about` field describes the fields. Only add public information. Events and community data are counts, never names.
