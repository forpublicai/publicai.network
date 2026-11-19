// The /progress page on publicai.network, rendered to static HTML by
// render.mjs. Laid out by pillar: toplines first, then a section per pillar,
// then the timeline and what each metric still needs.
// Spend, team names and the key anomaly are left out here on purpose.
import data from "../data/progress.json";
import {
  ProgressChart,
  ProgressFigure,
  ProgressGrid,
  ProgressPillars,
  ProgressTable,
  ProgressTimeline,
} from "../react/Progress";

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];
const longDate = (d: string) => `${Number(d.slice(8, 10))} ${MONTHS[Number(d.slice(5, 7)) - 1]} ${d.slice(0, 4)}`;

const coverageColumns = [
  { key: "metric", label: "Metric", format: "text" },
  { key: "status", label: "Status", format: "status" },
  { key: "have", label: "What we have", format: "text" },
  { key: "next", label: "Next step", format: "text" },
] as const;

const partial = "partial month";

export default function NetworkProgress() {
  return (
    <div className="progress-page">
      <p>
        Public AI has three things to show for itself. People use the products. People and organisations join the
        movement. And the idea of public AI spreads. This page tracks all three, from launch on{" "}
        {longDate(data.launch)} to {longDate(data.asOf)}.
      </p>

      <ProgressPillars
        d30Label="last 30 days"
        avgLabel="Avg month, past year"
        launchLabel="Since launch"
        notConnected="Not connected yet"
        coverageLabel="{n} of {total} metrics connected"
      />

      <h2>Products</h2>
      <p>
        In the last 30 days the Public AI Inference Utility served <ProgressFigure name="tokens_30" format="big" />{" "}
        tokens.
        chat.publicai.co had <ProgressFigure name="active_30" /> active users and gained{" "}
        <ProgressFigure name="users_30" /> sign-ups.
      </p>
      <ProgressGrid>
        <ProgressChart series="tokens" title="Tokens served per month" unit="tokens" format="big" partialLabel={partial} />
        <ProgressChart series="active_users" title="chat.publicai.co active users" unit="active users" partialLabel={partial} />
        <ProgressChart series="visitors" title="publicai.co visitors" unit="visitors" partialLabel={partial} />
      </ProgressGrid>

      <h2>Movement</h2>
      <p>
        Partners, community members and events are not counted yet. For now the movement shows up in mail and code:{" "}
        <ProgressFigure name="hello_30" /> new threads to hello@publicai.co and{" "}
        <ProgressFigure name="issues_30" /> GitHub issues in the last 30 days.
      </p>
      <ProgressGrid>
        <ProgressChart series="hello" title="Threads to hello@publicai.co" unit="threads" partialLabel={partial} />
        <ProgressChart series="issues" title="GitHub issues opened" unit="issues" partialLabel={partial} />
      </ProgressGrid>
      <ProgressTable
        table="repos"
        label="GitHub issues by repository"
        columns={[
          { key: "name", label: "Repository", format: "text" },
          { key: "opened", label: "Opened since launch", format: "int" },
          { key: "open", label: "Still open", format: "int" },
        ]}
      />

      <h2>Idea</h2>
      <p>
        Publications come from the <a href="/publications/">publications list</a>, which needs updating. News, papers,
        policy documents and social posts that use the phrase "public AI" are next.
      </p>
      <ProgressGrid>
        <ProgressChart series="publications" title="Publications per month" unit="publications" partialLabel={partial} />
      </ProgressGrid>

      <h2>Milestones</h2>
      <ProgressTimeline label="Milestones" />

      <h2>What we count</h2>
      <p>
        <ProgressFigure name="missing" /> of the <ProgressFigure name="total" /> metrics have no data source yet. The
        figures are built by the scripts in{" "}
        <a href="https://github.com/forpublicai/progress">forpublicai/progress</a>. Counts only: no names, emails or
        message text.
      </p>
      <h3>Products</h3>
      <ProgressTable table="coverage" pillar="products" label="Products coverage" columns={coverageColumns} />
      <h3>Movement</h3>
      <ProgressTable table="coverage" pillar="movement" label="Movement coverage" columns={coverageColumns} />
      <h3>Idea</h3>
      <ProgressTable table="coverage" pillar="idea" label="Idea coverage" columns={coverageColumns} />
    </div>
  );
}
