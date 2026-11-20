// The /progress page on publicai.network, rendered to static HTML by
// render.mjs. Laid out by pillar: toplines first, then a section per pillar,
// then the timeline and what each metric still needs.
// Spend, team names and the key anomaly are left out here on purpose.
import data from "../data/progress.json";
import {
  ProgressBars,
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
      <p>
        chat.publicai.co has registered users in <ProgressFigure name="countries_launch" /> countries, and people in <ProgressFigure name="countries_30" /> of them were active in the last 30 days. <ProgressFigure name="country_outside_ch_pct" />% of users with a known country are outside Switzerland.
      </p>
      <ProgressBars table="countries" labelKey="name" valueKey="users" shareKey="share" title="Registered chat users by country" />
      <p>
        The country comes from the timezone each user’s browser reported, mapped with the tz database. It is where their clock is set, not their nationality or exact location. <ProgressFigure name="country_known_pct" />% of users have a timezone with a country; the rest set none, or set UTC.
      </p>

      <h2>Movement</h2>
      <p>
        The Public AI Slack has <ProgressFigure name="slack_members" /> members.{" "}
        <ProgressFigure name="slack_posting_30" /> of them posted in the last 30 days and{" "}
        <ProgressFigure name="slack_active_30" /> were active, reading or posting.{" "}
        <ProgressFigure name="slack_joined_30" /> people joined. Partners and events are not counted yet.
      </p>
      <ProgressGrid>
        <ProgressChart series="slack_posting" title="Slack members posting, past 30 days" unit="people" partialLabel="to date" />
        <ProgressChart series="slack_joined" title="New Slack members per month" unit="new members" partialLabel={partial} />
        <ProgressChart series="slack_messages" title="Slack messages per month" unit="messages" partialLabel={partial} />
      </ProgressGrid>
      <p>
        Posting and active counts are Slack&apos;s own rolling 30-day figures, taken on the last day of each month. Mail
        and code show the movement too: <ProgressFigure name="hello_30" /> new threads to hello@publicai.co and{" "}
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
        In the last 30 days, <ProgressFigure name="papers_30" /> new papers used the phrase “public AI” in their title or abstract, against <ProgressFigure name="papers_y1" /> in the past year. Google search interest in the phrase averaged <ProgressFigure name="search_30" />, against <ProgressFigure name="search_y1" /> over the past year.
      </p>
      <ProgressGrid>
        <ProgressChart series="papers" title="Papers using “public AI”" unit="papers" partialLabel={partial} />
        <ProgressChart series="search_interest" title="Google search interest in “public AI”" unit="index" partialLabel={partial} />
        <ProgressChart series="newsletter_posts" title="Public AI newsletter posts" unit="posts" partialLabel={partial} />
        <ProgressChart series="publications" title="publicai.network publications list" unit="publications" partialLabel={partial} />
      </ProgressGrid>
      <p>
        Papers come from OpenAlex. It counts the phrase, so it also catches “public AI tools” and companies named PublicAI: read it as a trend. News articles from GDELT are next. Google search interest is an index where 100 is the peak week since January 2024, not a number of searches. UK Parliament has used the phrase <ProgressFigure name="hansard_total" /> times in Hansard, all in the Lords.
      </p>

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
