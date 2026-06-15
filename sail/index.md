---
title: SAIL
layout: page
description: A decoder for sovereign AI - mapping what decision-makers actually want when they invoke it, and where the technical stack can help.
permalink: /sail/
---

<style>
.post-header,
.post-title {
  display: none !important;
}

.sail-nav {
  display: flex;
  gap: 0.75rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.sail-nav a {
  display: inline-block;
  padding: 10px 20px;
  background: #f8f9fa;
  color: #667eea;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 500;
  border: 2px solid #667eea;
  transition: all 0.2s ease;
}

.sail-nav a:hover {
  background: #667eea;
  color: white;
}

.sail-nav a.current {
  background: #667eea;
  color: white;
}

.hero {
  position: relative;
  width: 100%;
  margin: 0 0 0.5rem 0;
  overflow: hidden;
  border-radius: 8px;
}

.hero-image {
  width: 100%;
  height: auto;
  display: block;
  margin: 0;
}

.hero-content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2.5rem 2rem 1.5rem 2rem;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.75) 0%, rgba(0, 0, 0, 0.5) 40%, rgba(0, 0, 0, 0) 100%);
  color: white;
}

.hero h1 {
  font-size: 2.25rem;
  font-weight: 700;
  margin: 0 0 0.75rem 0;
  color: white;
  line-height: 1.3;
}

.hero p {
  font-size: 1.05rem;
  margin: 0;
  color: white;
  line-height: 1.5;
  font-weight: 400;
}

.image-caption {
  font-size: 0.8rem;
  color: #666;
  font-style: italic;
  text-align: center;
  margin-bottom: 2rem;
  padding: 0 1rem;
}

.section {
  margin: 3rem 0;
}

.section h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  border-bottom: 3px solid #667eea;
  padding-bottom: 0.5rem;
}

.section p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 1rem;
}

.forks {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 2rem 0;
}

@media (min-width: 760px) {
  .forks {
    grid-template-columns: repeat(3, 1fr);
  }
}

.fork {
  background: #f8f9fa;
  border-top: 4px solid #667eea;
  border-radius: 8px;
  padding: 1.5rem;
}

.fork h4 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.fork p {
  font-size: 0.98rem;
  line-height: 1.6;
  color: #555;
  margin: 0;
}

.interest-table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border-radius: 8px;
  overflow: hidden;
}

.interest-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.interest-table th,
.interest-table td {
  padding: 1rem 1.2rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
  vertical-align: top;
}

.interest-table th {
  font-weight: 600;
}

.interest-table tbody tr:last-child td {
  border-bottom: none;
}

.interest-table tbody tr:hover {
  background: #f8f9fa;
}

.interest-table .relevance {
  font-size: 0.92rem;
  color: #666;
}

.paths {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin: 2rem 0;
}

@media (min-width: 700px) {
  .paths {
    grid-template-columns: 1fr 1fr;
  }
}

.path-card {
  display: block;
  background: white;
  border: 2px solid #667eea;
  border-radius: 8px;
  padding: 1.75rem;
  text-decoration: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.path-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(102, 126, 234, 0.25);
}

.path-card h3 {
  margin: 0 0 0.5rem 0;
  color: #667eea;
}

.path-card p {
  margin: 0;
  color: #555;
  line-height: 1.6;
}

details.tech-assessment {
  margin: 2rem 0;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: #f8f9fa;
  padding: 0 1.5rem;
}

details.tech-assessment summary {
  cursor: pointer;
  font-weight: 600;
  font-size: 1.2rem;
  color: #2c3e50;
  padding: 1.25rem 0;
}

details.tech-assessment[open] summary {
  border-bottom: 1px solid #e0e0e0;
  margin-bottom: 1rem;
}

.cert-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  background: white;
  border-radius: 8px;
  overflow: hidden;
}

.cert-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.cert-table th,
.cert-table td {
  padding: 0.9rem 1.2rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.cert-table tbody tr:last-child td {
  border-bottom: none;
}

.section-divider {
  border: none;
  border-top: 2px solid #e0e0e0;
  margin: 3.5rem 0;
}
</style>

<nav class="sail-nav">
  <a href="/sail" class="current">Home</a>
  <a href="/sail/interests">Interests</a>
  <a href="/sail/cases">Cases</a>
  <a href="/sail/spec">Specification</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries">Countries</a>
</nav>

<div class="hero">
  <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&h=700&fit=crop" alt="Global network infrastructure at night" class="hero-image">
  <div class="hero-content">
    <h1>SAIL: a decoder for sovereign AI</h1>
    <p>What do decision-makers actually want when they say "sovereign AI" - and where can the technical stack help?</p>
  </div>
</div>

<div class="section">
  <h2>The question SAIL asks</h2>
  <p>"Sovereign AI" is a banner that very different interests march under. A security ministry, an industrial-policy lead, an enterprise CIO, and a culture minister can all demand it while wanting completely different things. SAIL (Sovereign AI Leadership) is less interested in settling what sovereign AI <em>is</em> than in reading <strong>why decision-makers care</strong> - and then asking whether their strategy matches that interest.</p>
  <p>When a minister invokes sovereign AI, what are they really optimizing for?</p>

  <div class="forks">
    <div class="fork">
      <h4>Refusing a deal?</h4>
      <p>Declining an "OpenAI for Countries"-style offer can mean vendor diversification, protecting a domestic champion, a security red line, or pure electoral signaling. Four different strategies wear the same headline.</p>
    </div>
    <div class="fork">
      <h4>A news hook for something else?</h4>
      <p>Sometimes the real pet interest is minerals, energy contracts, or regional jobs, and sovereign AI is the framing that gets the press release written.</p>
    </div>
    <div class="fork">
      <h4>A values statement?</h4>
      <p>"A French model should feel French." This is a question of legitimacy and representation that no amount of productization or on-soil hosting can settle.</p>
    </div>
  </div>
</div>

<div class="section">
  <h2>Five interests behind one slogan</h2>
  <p>Most sovereign AI demands resolve into a handful of distinct interests. Each maps to a different part of the technical stack - and some are poorly served by any checklist at all.</p>

  <table class="interest-table">
    <thead>
      <tr>
        <th>Interest</th>
        <th>What they usually want</th>
        <th>Where the stack helps</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Security &amp; weaponization</strong></td>
        <td>No foreign actor can read, alter, or switch off critical systems (e.g. Microsoft's Swiss source-code vault).</td>
        <td class="relevance">Layers 6&ndash;7: compute control and legal override.</td>
      </tr>
      <tr>
        <td><strong>Industrial policy</strong></td>
        <td>Chips, fabs, energy, talent, and a national champion built at home.</td>
        <td class="relevance">Layer 6 capacity; high coordination risk.</td>
      </tr>
      <tr>
        <td><strong>Enterprise &amp; procurement</strong></td>
        <td>Data residency, provenance, and contractual exit rights.</td>
        <td class="relevance">Layers 1&ndash;3: the part SAIL scores best.</td>
      </tr>
      <tr>
        <td><strong>Cultural identity &amp; values</strong></td>
        <td>A model that represents a community's language and norms.</td>
        <td class="relevance">Partial only; legitimacy cannot be certified.</td>
      </tr>
      <tr>
        <td><strong>Middle-power alliance</strong></td>
        <td>Pooled compute, data, and models with trusted partners.</td>
        <td class="relevance">Rewarded as federated sovereignty.</td>
      </tr>
    </tbody>
  </table>

  <p><a href="/sail/interests">Read the full interest decoder &rarr;</a></p>
</div>

<div class="section">
  <h2>Why the framing matters</h2>
  <p>When interests conflict, "sovereignty" stops being a specification and becomes a contest. Parallel nationalist races - everyone onshoring the same chips, everyone poaching the same researchers - can quietly undermine a joint middle-power strategy. The backlash to national champions like Cohere and Aleph Alpha is the pattern in miniature: one country's flagship becomes another country's reason to say "now we don't have to depend on them."</p>
  <p>There is a deeper tension too. Large language models have steep fixed costs, thrive on scale and shared data, and are cheap to copy once trained. That profile fits a globally provisioned <a href="/">public good with some decentralization</a> far better than dozens of self-sufficient national stacks. For some actors, the most sovereign outcome is a shared, openly governed system - sovereignty as governance and access, not ownership and borders.</p>
</div>

<div class="section">
  <h2>Two ways to use SAIL</h2>
  <div class="paths">
    <a href="/sail/interests" class="path-card">
      <h3>Understand the interests &rarr;</h3>
      <p>Decode what a sovereign AI claim is really asking for, what each interest can and cannot achieve, and where coordination breaks down.</p>
    </a>
    <a href="/sail/spec" class="path-card">
      <h3>Assess stack control &rarr;</h3>
      <p>When the real goal is control, dependency transparency, or exit readiness, use the seven-layer specification to assess it.</p>
    </a>
  </div>
</div>

<hr class="section-divider">

<details class="tech-assessment">
  <summary>Technical assessment: the seven-layer certification</summary>

  <p>For interests that are genuinely about control and exit readiness - mostly enterprise, procurement, and security - SAIL offers a structured, point-based assessment across seven layers of the AI stack, from applications and data through to compute and legal governance. It is a tool for measuring stack control maturity, not a badge of national prestige.</p>

  <p>An assessment satisfies baseline prerequisites first, then accrues points toward a control-maturity level:</p>

  <table class="cert-table">
    <thead>
      <tr>
        <th>Level</th>
        <th>Points</th>
        <th>Reading</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Platinum</strong></td>
        <td>80+</td>
        <td>End-to-end control, individually or through credible allied arrangements.</td>
      </tr>
      <tr>
        <td><strong>Gold</strong></td>
        <td>60&ndash;79</td>
        <td>Strong control over data and model behavior, with managed dependencies.</td>
      </tr>
      <tr>
        <td><strong>Silver</strong></td>
        <td>50&ndash;59</td>
        <td>Application and data control, with unresolved deeper dependencies.</td>
      </tr>
      <tr>
        <td><strong>Certified</strong></td>
        <td>40&ndash;49</td>
        <td>Baseline control, still highly dependent on external providers.</td>
      </tr>
    </tbody>
  </table>

  <p>Crucially, the spec does not try to measure cultural legitimacy or industrial-policy success - interests it cannot assess. See the <a href="/sail/spec">full specification</a> for the layers, credits, flags, and a guide to when the framework applies.</p>
</details>

<div class="section">
  <h2>About SAIL</h2>
  <p>SAIL is developed and maintained by the <a href="/">Public AI Network</a> as part of its work on AI as public infrastructure. It draws on the network's <a href="/seminar">seminar series</a>, <a href="/publications">publications</a>, and <a href="/handbook">handbook</a> on national strategies and coordination.</p>
</div>
