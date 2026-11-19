# Handoff: state on 18 Nov 2026

Notes for whoever picks this up next, human or agent. Delete the file once it's out of date.

## Where things stand

- `/progress` is live on publicai.ch and publicai.co. Both pages are `noindex`.
- **Subtree move done on 19 Nov 2026**, on branch `claude/bold-bohr-fo3g32` in both repos. It is not merged yet.
  - publicai.ch re-exports the shared components from `src/components/mdx/progress.tsx`. `ProgressPillars` and `ProgressTimeline` are registered in both MDX registries. `tools/progress/`, `src/data/progress.json` and the `.progress-*` CSS were removed. All gates pass.
  - publicai.co re-exports from `src/components/progress/Progress.tsx`. Its CSS module keeps only page typography and sets `--progress-mono` to Overpass Mono. `npm run build` passes.
  - Neither page uses the pillars or the timeline yet.
- Topline monthly averages use full months in the past year. So the tokens average is 1.70B in the pillar cards, against 1.89B (past-year total ÷ 12) in the page text.

## Next steps, in order

1. **publicai.network** (Jekyll, forpublicai/publicai.network). Two options:
   - Add `progress/data/progress.json` as a Jekyll data file and write a Liquid page.
   - Have `build.py` also emit a static HTML fragment, by rendering the React components with Node, and `{% include %}` it. This one keeps all three sites identical.
2. **Restructure the page** into the three pillars:
   - `ProgressPillars` at the top
   - then a section per pillar with its charts and tables
   - then `ProgressTimeline`
   - then the coverage table, grouped by pillar
3. **Idea collectors.** These need the **"Public AI progress"** cloud environment, which allows api.openalex.org, api.gdeltproject.org, public.api.bsky.app, api.semanticscholar.org, hansard-api.parliament.uk and publicai.substack.com.
   - GDELT DOC API: `mode=timelinevolraw`, exact phrase `"public AI"`, monthly. Check a sample of articles by hand: the phrase catches "public AI tools" and companies called PublicAI.
   - OpenAlex: works with the exact phrase, grouped by `publication_year`.
   - Hansard: spoken contributions containing the phrase.
   - Bluesky: `app.bsky.feed.searchPosts`, counts per month.
   - Substack: posts per month from `https://publicai.substack.com/feed`. Subscriber counts are not public: type them into `records/audience.json`.
4. **Keys in the new environment.** The LiteLLM key (host api-internal.publicai.co, `Authorization: Bearer`) and Open WebUI admin key (host chat.publicai.co) were saved on the Default environment only. Add them again as network secrets.
5. **Public AI Slack.** Josh is creating a bot token. The connected Slack connector is **Current AI's**, not Public AI's, so don't use it. The same goes for the connected Notion. Counts only: distinct posters per week, joins per month.
6. **Fill `records/`** with milestones, partners, events and notable mentions. One example to add: Mistral's full-page ad in The Times that named public AI (Nov 2026; the date and URL still need to be found). The publications list on publicai.network stops at Sep 2025 and needs updating, otherwise the Idea topline reads near zero.
7. **Weekly refresh.** A GitHub Action in this repo can run the collectors that have API access and `build.py`. Sites then `git subtree pull`.

## Open problems

- **LiteLLM API returns HTTP 500** for every authenticated request, on every route, including `/v1/models` and from Josh's own terminal.
  - The proxy is api-internal.publicai.co, which runs LiteLLM v1.92.0 behind Cloudflare and an ALB.
  - The admin UI also shows no data.
  - The custom auth hook is the likely cause: `charts/platform/charts/litellm/custom_auth.py` in forpublicai/chat.publicai.co.
  - Until it's fixed, data comes from the admin UI's CSV export, through `litellm_usage.py --csv` and then `litellm_daily.py`.
- **Cloudflare error 1010** blocks Python's default user agent, so every collector must send its own `User-Agent`.
- **publicai.ch visitors:** no source. Infomaniak has no API connector; the options are a CSV export or a cookieless analytics script.
- **dialogue.publicai.ch:** the host didn't resolve, and the survey was paused in Apr 2026.
- **support@:** only threads that also reached hello@ are counted. Joseph's inbox isn't included.

## Anomalies worth a human look

- **Open WebUI team traffic.** LiteLLM tokens per chat message on the Open WebUI team jumped from Sep 2026, so something other than chat is likely using that team's key.
- **Sign-up spike.** Nov 2026 had about 2,200 sign-ups in 16 days while active users fell, which may be bots.
- **Visitors.** publicai.co traffic roughly halved in Apr 2026.
- **Failed requests.** About 17% of LiteLLM requests failed in the last 30 days.

## Privacy

- **Public page.** The live pages show LiteLLM spend, team names, the key anomaly note and support counts. Decide whether those stay public.
- **What snapshots hold.** Snapshots keep dates and counts only. The GitHub snapshot also has public issue titles.
