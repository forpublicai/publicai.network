// Progress components: render ../data/progress.json, which build.py
// precomputes. Everything is static HTML and SVG, so they work in any React
// renderer (React Router SSG, Next.js server components). Visible labels come
// from props, so each site and locale supplies its own wording; only data
// values come from JSON. Styles: ./progress.css (plain class names).
import type { ReactNode } from "react";
import data from "../data/progress.json";

type Format = "int" | "big" | "dec" | "pct" | "usd" | "text" | "status" | "kilo";

const intFmt = new Intl.NumberFormat("en-US");
const decFmt = new Intl.NumberFormat("en-US", { maximumFractionDigits: 1 });
const usdFmt = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });

function format(value: unknown, kind: Format = "int"): string {
  if (value === null || value === undefined || value === "") return "";
  if (kind === "text" || kind === "status") return String(value);
  const n = Number(value);
  if (!Number.isFinite(n)) return String(value);
  switch (kind) {
    case "big":
      if (n >= 1e9) return `${decFmt.format(Math.round(n / 1e7) / 100)}B`;
      if (n >= 1e6) return `${decFmt.format(n / 1e6)}M`;
      return intFmt.format(n);
    case "kilo":
      return n >= 1e6 ? `${decFmt.format(n / 1e6)}M` : `${intFmt.format(Math.round(n / 1e3))}k`;
    case "dec":
      return decFmt.format(n);
    case "pct":
      return `${decFmt.format(n)}%`;
    case "usd":
      return `$${usdFmt.format(n)}`;
    default:
      return intFmt.format(n);
  }
}

function statusClass(status: string): string {
  if (status === "Counted") return "progress-pill progress-pill--ok";
  if (status === "Partial") return "progress-pill progress-pill--warn";
  return "progress-pill progress-pill--missing";
}

type Row = Record<string, unknown>;

/** One number inside a sentence, e.g. <ProgressFigure name="tokens_30" format="big" />. */
export function ProgressFigure({ name, format: kind = "int" }: { name: string; format?: Format }) {
  const figures = data.figures as Record<string, number | null>;
  return <strong className="progress-figure">{format(figures[name], kind)}</strong>;
}

export type ProgressColumn = {
  key: string;
  label: string;
  format?: Format;
  align?: "left" | "right";
};

type PillarId = "products" | "movement" | "idea";

/** Keep only rows of one pillar, when the table has a pillar field. */
const ofPillar = (rows: Row[], pillar?: PillarId) =>
  pillar ? rows.filter((r) => r.pillar === pillar) : rows;

function Table({
  rows,
  columns,
  label,
  empty,
}: {
  rows: Row[];
  columns: readonly ProgressColumn[];
  label: string;
  empty?: string;
}) {
  return (
    <div className="progress-table" role="region" aria-label={label} tabIndex={0}>
      <table>
        <thead>
          <tr>
            {columns.map((c) => (
              <th
                key={c.key}
                align={
                  c.align ??
                  (c.format && c.format !== "text" && c.format !== "status" ? "right" : "left")
                }
              >
                {c.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, i) => (
            <tr key={i}>
              {columns.map((c) => {
                const v = row[c.key];
                const numeric = c.format && c.format !== "text" && c.format !== "status";
                const kind =
                  c.key === "d30" || c.key === "y1" || c.key === "launch"
                    ? ((row.format as Format) ?? c.format)
                    : c.format;
                return (
                  <td
                    key={c.key}
                    align={c.align ?? (numeric ? "right" : "left")}
                    className={numeric ? "progress-num" : undefined}
                  >
                    {c.format === "status" ? (
                      <span className={statusClass(String(v))}>{String(v)}</span>
                    ) : v === null || v === undefined ? (
                      <span className="progress-na">{empty ?? ""}</span>
                    ) : (
                      format(v, kind)
                    )}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/** The scorecard: one row per metric, a column per window. */
export function ProgressScorecard({
  columns,
  label,
  empty,
  pillar,
}: {
  columns: readonly ProgressColumn[];
  label: string;
  empty: string;
  /** Show only one pillar's metrics. */
  pillar?: PillarId;
}) {
  return <Table rows={ofPillar(data.scorecard as Row[], pillar)} columns={columns} label={label} empty={empty} />;
}

/** Any precomputed table: llm_windows, llm_family, llm_team, repos, coverage. */
export function ProgressTable({
  table,
  columns,
  label,
  pillar,
}: {
  table: keyof typeof data.tables;
  columns: readonly ProgressColumn[];
  label: string;
  /** For tables with a pillar field (coverage): show only that pillar. */
  pillar?: PillarId;
}) {
  return <Table rows={ofPillar(data.tables[table] as Row[], pillar)} columns={columns} label={label} />;
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const monthLabel = (m: string, long = false) =>
  `${MONTHS[Number(m.slice(5, 7)) - 1]} ${long ? m.slice(0, 4) : m.slice(2, 4)}`;

/** Monthly bars for one series. The as-of month is partial and drawn lighter. */
export function ProgressChart({
  series,
  title,
  unit,
  format: kind = "int",
  partialLabel,
}: {
  series: keyof typeof data.series;
  title: string;
  unit: string;
  format?: Format;
  partialLabel: string;
}) {
  const rows = data.series[series].filter(
    (r, i, all) => r.value > 0 || i >= all.findIndex((x) => x.value > 0),
  );
  const W = 600;
  const H = 220;
  const top = 22;
  const bottom = 26;
  const step = W / rows.length;
  const bar = step * 0.72;
  const max = Math.max(1, ...rows.map((r) => r.value));
  const y = (v: number) => H - bottom - (v / max) * (H - top - bottom);
  const partial = data.asOf.slice(0, 7);
  const peak = rows.reduce((a, b) => (b.value > a.value ? b : a), rows[0]);
  const last = rows[rows.length - 1];
  const labelled = peak === last ? [peak] : [peak, last];
  // A month label every quarter, or every half-year on long series.
  const tickEvery = rows.length > 20 ? 6 : 3;
  return (
    <figure className="progress-chart">
      <figcaption className="progress-chart__title">{title}</figcaption>
      <svg
        viewBox={`0 0 ${W} ${H}`}
        width="100%"
        role="img"
        aria-label={`${title}: ${monthLabel(rows[0].month, true)} to ${monthLabel(last.month, true)}, peak ${format(peak.value, kind)} ${unit} in ${monthLabel(peak.month, true)}`}
      >
        <line x1={0} x2={W} y1={H - bottom} y2={H - bottom} className="progress-chart__axis" />
        {rows.map((r, i) => (
          <rect
            key={r.month}
            x={i * step + (step - bar) / 2}
            y={y(r.value)}
            width={bar}
            height={Math.max(0, H - bottom - y(r.value))}
            className={
              r.month === partial
                ? "progress-chart__bar progress-chart__bar--partial"
                : "progress-chart__bar"
            }
          >
            <title>{`${monthLabel(r.month, true)}${r.month === partial ? ` (${partialLabel})` : ""}: ${format(r.value, kind)} ${unit}`}</title>
          </rect>
        ))}
        {labelled.map((r) => {
          const i = rows.indexOf(r);
          return (
            <text
              key={`v-${r.month}`}
              x={i * step + step / 2}
              y={y(r.value) - 6}
              textAnchor="middle"
              className="progress-chart__value"
            >
              {format(r.value, kind)}
            </text>
          );
        })}
        {rows.map((r, i) =>
          i % tickEvery === 0 ? (
            <text
              key={`t-${r.month}`}
              x={i * step + step / 2}
              y={H - 8}
              textAnchor={i === 0 ? "start" : "middle"}
              dx={i === 0 ? -bar / 2 : 0}
              className="progress-chart__tick"
            >
              {monthLabel(r.month)}
            </text>
          ) : null,
        )}
      </svg>
    </figure>
  );
}

/** Horizontal bars for a ranked table, e.g. users by country. Rows with
 * muted: true (such as "other" or "not set") are drawn lighter and don't
 * set the scale. */
export function ProgressBars({
  table,
  labelKey,
  valueKey,
  shareKey,
  title,
  format: kind = "int",
}: {
  table: keyof typeof data.tables;
  labelKey: string;
  valueKey: string;
  /** Optional percentage shown after the value. */
  shareKey?: string;
  title: string;
  format?: Format;
}) {
  const rows = data.tables[table] as Row[];
  // Scale to the largest ranked row, so a big "other" or "not set" row
  // doesn't flatten the rest; muted rows are capped at full width.
  const ranked = rows.filter((r) => !r.muted);
  const max = Math.max(1, ...(ranked.length ? ranked : rows).map((r) => Number(r[valueKey]) || 0));
  return (
    <figure className="progress-bars">
      <figcaption className="progress-chart__title">{title}</figcaption>
      <ol>
        {rows.map((r, i) => {
          const v = Number(r[valueKey]) || 0;
          return (
            <li key={i} className={r.muted ? "progress-bars__row progress-bars__row--muted" : "progress-bars__row"}>
              <span className="progress-bars__label">{String(r[labelKey])}</span>
              <span className="progress-bars__track" aria-hidden="true">
                <span className="progress-bars__bar" style={{ width: `${Math.min(100, (100 * v) / max)}%` }} />
              </span>
              <span className="progress-bars__value">
                {format(v, kind)}
                {shareKey ? <span className="progress-bars__share">{format(r[shareKey], "pct")}</span> : null}
              </span>
            </li>
          );
        })}
      </ol>
    </figure>
  );
}

/** A responsive grid around ProgressChart blocks. */
export function ProgressGrid({ children }: { children: ReactNode }) {
  return <div className="progress-grid">{children}</div>;
}

/** The three pillars, each with its 1-2 topline stats. */
export function ProgressPillars({
  labels,
  d30Label,
  avgLabel,
  launchLabel,
  notConnected,
  coverageLabel,
}: {
  /** Optional per-locale overrides of each pillar's label and question. */
  labels?: Partial<Record<PillarId, { label: string; question: string }>>;
  d30Label: string;
  avgLabel: string;
  launchLabel: string;
  notConnected: string;
  /** e.g. "{n} of {total} metrics connected". */
  coverageLabel: string;
}) {
  return (
    <div className="progress-pillars">
      {data.pillars.map((p) => {
        const l = labels?.[p.id as PillarId];
        return (
          <section key={p.id} className="progress-pillar" aria-labelledby={`pillar-${p.id}`}>
            <h3 id={`pillar-${p.id}`} className="progress-pillar__label">
              {l?.label ?? p.label}
            </h3>
            <p className="progress-pillar__question">{l?.question ?? p.question}</p>
            {p.topline.map((t) => (
              <div key={t.key} className="progress-topline">
                <div className="progress-topline__metric">{t.metric}</div>
                {t.d30 === null ? (
                  <span className="progress-pill progress-pill--missing">{notConnected}</span>
                ) : (
                  <>
                    <div className="progress-topline__value">
                      {format(t.d30, t.format as Format)}
                      <span className="progress-topline__window">{d30Label}</span>
                    </div>
                    <dl className="progress-topline__context">
                      {t.y1_avg !== null ? (
                        <div>
                          <dt>{avgLabel}</dt>
                          <dd>{format(t.y1_avg, t.format as Format)}</dd>
                        </div>
                      ) : null}
                      {t.launch !== null ? (
                        <div>
                          <dt>{launchLabel}</dt>
                          <dd>{format(t.launch, t.format as Format)}</dd>
                        </div>
                      ) : null}
                    </dl>
                  </>
                )}
              </div>
            ))}
            <p className="progress-pillar__coverage">
              {coverageLabel.replace("{n}", String(p.connected)).replace("{total}", String(p.total))}
            </p>
          </section>
        );
      })}
    </div>
  );
}

/** Dated milestones from records/milestones.json, newest first. */
export function ProgressTimeline({ label }: { label: string }) {
  const rows = [...data.milestones].reverse();
  return (
    <ol className="progress-timeline" aria-label={label}>
      {rows.map((m, i) => (
        <li key={i}>
          <time dateTime={m.date} className="progress-timeline__date">
            {m.date}
          </time>
          <span className="progress-timeline__title">
            {m.url ? <a href={m.url}>{m.title}</a> : m.title}
          </span>
        </li>
      ))}
    </ol>
  );
}
