// Renders static/dist/card.png, the 1200x630 social card for every site's
// /progress page: one headline number per pillar, from data/progress.json.
// Needs Playwright with Chromium (`npx playwright install chromium`); without
// it the existing card is kept and a warning is printed.
/* global console, document */
import { readFile, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";

const here = import.meta.dirname;
const require = createRequire(import.meta.url);

// Short card labels; anything else falls back to the metric name.
const LABELS = {
  tokens: "tokens served",
  active_users: "active chat users",
  partners: "partner organisations",
  community_active: "Slack members posting",
  news_mentions: "news articles using “public AI”",
  papers: "papers using “public AI”",
};
const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
  "September", "October", "November", "December"];

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const big = (n) =>
  n >= 1e9 ? `${(Math.round(n / 1e8) / 10).toFixed(1)}B` : n >= 1e6 ? `${(n / 1e6).toFixed(1)}M` : n.toLocaleString("en-US");

async function font(pkg, file) {
  const buf = await readFile(require.resolve(`@fontsource/${pkg}/files/${file}`));
  return `data:font/woff2;base64,${buf.toString("base64")}`;
}

export async function renderCard(data, out) {
  let chromium;
  try {
    ({ chromium } = require("playwright"));
  } catch {
    console.warn("card.png: Playwright not found, kept the existing card");
    return;
  }
  const d = data.asOf;
  const asOf = `${Number(d.slice(8, 10))} ${MONTHS[Number(d.slice(5, 7)) - 1]} ${d.slice(0, 4)}`;
  const pillars = data.pillars.map((p) => {
    const t = p.topline.find((x) => x.d30 !== null) ?? p.topline[0];
    const value = t.d30 === null ? "–" : t.format === "big" ? big(t.d30) : t.d30.toLocaleString("en-US");
    return `<div class="pillar"><div class="label">${esc(p.label)}</div>
      <div class="value">${esc(value)}</div><div class="metric">${esc(LABELS[t.key] ?? t.metric)}</div></div>`;
  });
  const mono = [await font("overpass-mono", "overpass-mono-latin-400-normal.woff2"),
    await font("overpass-mono", "overpass-mono-latin-600-normal.woff2")];
  const sans = [await font("public-sans", "public-sans-latin-400-normal.woff2"),
    await font("public-sans", "public-sans-latin-500-normal.woff2")];
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>
    @font-face { font-family: Mono; src: url(${mono[0]}); font-weight: 400; }
    @font-face { font-family: Mono; src: url(${mono[1]}); font-weight: 600; }
    @font-face { font-family: Sans; src: url(${sans[0]}); font-weight: 400; }
    @font-face { font-family: Sans; src: url(${sans[1]}); font-weight: 500; }
    * { box-sizing: border-box; margin: 0; }
    body { width: 1200px; height: 630px; background: #fff; color: #000; font-family: Sans;
      padding: 64px 72px 56px; display: flex; flex-direction: column; }
    header { display: flex; align-items: center; gap: 24px; }
    header svg { width: 76px; height: 70px; flex: none; }
    h1 { font-size: 64px; font-weight: 500; letter-spacing: -0.01em; line-height: 1; }
    .sub { margin-top: 20px; font-size: 26px; }
    .pillars { margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
    .pillar { background: rgba(0,0,0,0.05); border-radius: 16px; padding: 28px 30px 30px; }
    .label { font-size: 26px; font-weight: 500; }
    .value { font-family: Mono; font-size: 72px; line-height: 1; margin-top: 18px; color: #ef3c24; }
    .metric { font-size: 24px; margin-top: 14px; line-height: 1.25; }
    footer { margin-top: 22px; font-family: Mono; font-size: 18px; text-transform: uppercase; letter-spacing: 0.02em; }
  </style></head><body>
    <header>
      <svg viewBox="0 0 122.2 112.14" aria-hidden="true"><rect width="122.2" height="112.14" fill="#EF3C24"/>
        <path d="M28.556 72.0731V60.053L79.292 45.7727L28.556 31.287V19.3696L93.8265 39.3004V52.2451L28.556 72.0731ZM28.556 88.6925V77.9053H93.8265V88.6925H28.556Z" fill="#fff"/></svg>
      <h1>Public AI progress</h1>
    </header>
    <p class="sub">Products, movement and idea since launch in September 2025.</p>
    <div class="pillars">${pillars.join("")}</div>
    <footer>Last 30 days, to ${esc(asOf)}</footer>
  </body></html>`;
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
    await page.setContent(html);
    await page.evaluate(() => document.fonts.ready);
    await writeFile(out, await page.screenshot({ type: "png" }));
  } finally {
    await browser.close();
  }
  console.log(`${path.relative(path.join(here, ".."), out)}  1200x630`);
}
