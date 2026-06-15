---
title: SAIL Countries
layout: page
description: Country profiles reading the interests behind national sovereign AI strategies, with an illustrative stack-control assessment.
permalink: /sail/countries/
---

<style>
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

.lede {
  font-size: 1.15rem;
  line-height: 1.7;
  color: #444;
  margin: 1.5rem 0;
}

.profiles-table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

.profiles-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.profiles-table th,
.profiles-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
  vertical-align: top;
}

.profiles-table th {
  font-weight: 600;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.profiles-table tbody tr:last-child td {
  border-bottom: none;
}

.profiles-table tbody tr:hover {
  background: #f8f9fa;
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 14px;
  font-size: 0.78rem;
  font-weight: 600;
  margin: 2px 4px 2px 0;
}

.badge.security { background: #f8d7da; color: #842029; }
.badge.industrial { background: #fff3cd; color: #664d03; }
.badge.enterprise { background: #d1e7dd; color: #0f5132; }
.badge.values { background: #e2d9f3; color: #432874; }
.badge.alliance { background: #cfe2ff; color: #084298; }

.posture {
  font-weight: 600;
  font-size: 0.85rem;
}

.posture.allied { color: #084298; }
.posture.mixed { color: #b8860b; }
.posture.national { color: #842029; }

.country-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 2rem;
  margin: 2rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.country-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #e0e0e0;
}

.country-flag {
  font-size: 3rem;
}

.country-info h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.8rem;
  color: #333;
}

.country-info p {
  color: #666;
  margin: 0;
}

.country-card h4 {
  color: #2c3e50;
  margin: 1.5rem 0 0.5rem 0;
}

.posture-box {
  background: #fffbf0;
  border-left: 4px solid #ffc107;
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin: 1.25rem 0;
}

.posture-box.allied {
  background: #f0f5ff;
  border-left-color: #084298;
}

.posture-box p {
  margin: 0;
  line-height: 1.6;
  color: #444;
}

.control-assessment {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin: 1.25rem 0;
}

.control-assessment .score {
  font-size: 1.4rem;
  font-weight: 700;
  color: #667eea;
}

.control-assessment .layers {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.control-assessment .layer-chip {
  padding: 4px 10px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 0.82rem;
  font-weight: 500;
  color: #555;
}

@media (max-width: 768px) {
  .country-header {
    flex-direction: column;
    align-items: start;
  }
}
</style>

<nav class="sail-nav">
  <a href="/sail">Home</a>
  <a href="/sail/interests">Interests</a>
  <a href="/sail/cases">Cases</a>
  <a href="/sail/spec">Specification</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries" class="current">Countries</a>
</nav>

# Country profiles

<p class="lede">These profiles read national sovereign AI strategies through the <a href="/sail/interests">interest decoder</a>: which interests each country is really pursuing, where its strategy creates tension with neighbors, and how it positions itself between going alone and pooling capacity. An illustrative stack-control assessment, drawn from the <a href="/sail/spec">seven-layer specification</a>, sits underneath the interest reading - not above it.</p>

<p>This is a deliberately small, well-documented set rather than a global leaderboard. A ranking would imply that more sovereignty is always better and that all these countries want the same thing. They do not. The point is to compare interests and coordination postures, not to crown a winner.</p>

<table class="profiles-table">
  <thead>
    <tr>
      <th>Country</th>
      <th>Primary interests</th>
      <th>Coordination posture</th>
      <th>Stack control</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>🇨🇭 <a href="#switzerland">Switzerland</a></strong></td>
      <td>
        <span class="badge alliance">Alliance</span>
        <span class="badge values">Values</span>
      </td>
      <td><span class="posture allied">Allied / open</span></td>
      <td>Illustrative: high</td>
    </tr>
    <tr>
      <td><strong>🇸🇬 <a href="#singapore">Singapore</a></strong></td>
      <td>
        <span class="badge alliance">Alliance</span>
        <span class="badge enterprise">Enterprise</span>
        <span class="badge values">Values</span>
      </td>
      <td><span class="posture allied">Allied / regional</span></td>
      <td>Illustrative: high</td>
    </tr>
    <tr>
      <td><strong>🇫🇷 <a href="#france">France</a></strong></td>
      <td>
        <span class="badge industrial">Industrial</span>
        <span class="badge values">Values</span>
      </td>
      <td><span class="posture mixed">Mixed</span></td>
      <td>Illustrative: medium-high</td>
    </tr>
    <tr>
      <td><strong>🇩🇪 <a href="#germany">Germany</a></strong></td>
      <td>
        <span class="badge industrial">Industrial</span>
        <span class="badge enterprise">Enterprise</span>
      </td>
      <td><span class="posture mixed">Mixed</span></td>
      <td>Illustrative: medium-high</td>
    </tr>
  </tbody>
</table>

## Detailed profiles

### Switzerland {#switzerland}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇨🇭</div>
    <div class="country-info">
      <h3>Switzerland</h3>
      <p>
        <span class="badge alliance">Middle-power alliance</span>
        <span class="badge values">Cultural identity &amp; values</span>
      </p>
    </div>
  </div>

  <p>Switzerland's strategy reads as sovereignty through openness rather than enclosure. Apertus, built at ETH Zurich and EPFL, is fully open and reproducible, and is served globally through the Public AI Inference Utility. The interest is less about national control of a private champion and more about anchoring a trusted, openly governed alternative that others can also draw on.</p>

  <div class="posture-box allied">
    <p><strong>Coordination posture: allied / open.</strong> By making its flagship model open and shared, Switzerland builds capacity that strengthens rather than fragments a middle-power approach. It is closer to the alliance interest than to national-champion industrial policy.</p>
  </div>

  <h4>What it does not resolve</h4>
  <p>An open, multilingual model advances the values interest but cannot by itself confer cultural legitimacy for every community that uses it. Compute remains the structural dependency, as it does almost everywhere outside the largest economies.</p>

  <div class="control-assessment">
    <div class="score">Illustrative stack control: high</div>
    <p style="margin:0.5rem 0 0 0; color:#666; font-size:0.95rem;">Strong on model and data sovereignty (open weights, reproducibility); compute is the main constraint, partly addressed through allied arrangements.</p>
    <div class="layers">
      <span class="layer-chip">Strong: Model</span>
      <span class="layer-chip">Strong: Data</span>
      <span class="layer-chip">Constraint: Compute</span>
    </div>
  </div>

  <p><a href="/sail/models#switzerland">View Apertus model profile &rarr;</a> &nbsp; <a href="/sail/cases#sea-lion-apertus-and-the-public-ai-inference-utility">See the allied-public case &rarr;</a></p>
</div>

### Singapore {#singapore}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇸🇬</div>
    <div class="country-info">
      <h3>Singapore</h3>
      <p>
        <span class="badge alliance">Middle-power alliance</span>
        <span class="badge enterprise">Enterprise &amp; procurement</span>
        <span class="badge values">Cultural identity &amp; values</span>
      </p>
    </div>
  </div>

  <p>Singapore pursues regional rather than purely national sovereignty. SEA-LION serves eleven Southeast Asian languages, addressing a values interest that no global frontier lab prioritizes, while AI Singapore coordinates government, research, and industry around a pragmatic capability agenda. The framing is regional capability and representation, not autarky.</p>

  <div class="posture-box allied">
    <p><strong>Coordination posture: allied / regional.</strong> By building models for a language region rather than a single country, Singapore creates shared infrastructure neighbors can use - an alliance-building rather than fragmenting move.</p>
  </div>

  <h4>What it does not resolve</h4>
  <p>As a small economy, Singapore faces the same compute constraint as other middle powers. Its strength is coordination and applied capability, not frontier-scale infrastructure.</p>

  <div class="control-assessment">
    <div class="score">Illustrative stack control: high</div>
    <p style="margin:0.5rem 0 0 0; color:#666; font-size:0.95rem;">Strong on data and model control for regional languages and on institutional coordination; compute capacity is the structural limit.</p>
    <div class="layers">
      <span class="layer-chip">Strong: Data</span>
      <span class="layer-chip">Strong: Model</span>
      <span class="layer-chip">Constraint: Compute</span>
    </div>
  </div>

  <p><a href="/sail/models#singapore">View SEA-LION model profile &rarr;</a></p>
</div>

### France {#france}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇫🇷</div>
    <div class="country-info">
      <h3>France</h3>
      <p>
        <span class="badge industrial">Industrial policy</span>
        <span class="badge values">Cultural identity &amp; values</span>
      </p>
    </div>
  </div>

  <p>France's strategy centers on a national champion, Mistral, and the idea that European AI capability should have a French anchor. Two interests overlap: an industrial bid for jobs, investment, and a frontier foothold, and a values claim that a French model should reflect French language and norms.</p>

  <div class="posture-box">
    <p><strong>Coordination posture: mixed.</strong> A national champion can strengthen Europe's collective position or fragment it, depending on whether it is framed as a shared European asset or a purely national one. France's framing leans European, but the champion model carries fragmentation risk.</p>
  </div>

  <h4>What it does not resolve</h4>
  <p>The values dimension cannot be productized: a model "feeling French" is a matter of governance and recognition, not of headquarters or shareholders. And a single national champion does not, on its own, reach the scale needed to compete with hyperscalers.</p>

  <div class="control-assessment">
    <div class="score">Illustrative stack control: medium-high</div>
    <p style="margin:0.5rem 0 0 0; color:#666; font-size:0.95rem;">Real model and training capability through Mistral; mixed licensing and the usual compute constraint temper full-stack control.</p>
    <div class="layers">
      <span class="layer-chip">Strong: Model</span>
      <span class="layer-chip">Strong: Training</span>
      <span class="layer-chip">Constraint: Compute</span>
    </div>
  </div>

  <p><a href="/sail/models#france">View Mistral model profile &rarr;</a> &nbsp; <a href="/sail/cases#mistral-and-french-ai">See the Mistral case &rarr;</a></p>
</div>

### Germany {#germany}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇩🇪</div>
    <div class="country-info">
      <h3>Germany</h3>
      <p>
        <span class="badge industrial">Industrial policy</span>
        <span class="badge enterprise">Enterprise &amp; procurement</span>
      </p>
    </div>
  </div>

  <p>Germany combines an industrial interest - supporting a domestic lab such as Aleph Alpha and protecting its strong enterprise base - with a procurement interest rooted in data protection and the needs of its industrial firms. Its sovereign AI debate is often shaped in reaction to neighbors: a French champion can become an argument for reducing dependence on France rather than deepening European cooperation.</p>

  <div class="posture-box">
    <p><strong>Coordination posture: mixed.</strong> This is the clearest illustration of the fragmentation dynamic. When a national champion next door reads as a dependency to escape, the result is parallel champions competing for the same chips and talent - exactly what a joint middle-power strategy needs to avoid.</p>
  </div>

  <h4>What it does not resolve</h4>
  <p>Reacting to neighbors' champions with one's own does not address the underlying scale problem, and erodes the trust that pooled capacity depends on. The enterprise interest (data residency, exit rights) is tractable and well served by the stack; the industrial-champion interest is where coordination is most at risk.</p>

  <div class="control-assessment">
    <div class="score">Illustrative stack control: medium-high</div>
    <p style="margin:0.5rem 0 0 0; color:#666; font-size:0.95rem;">Strong on application, data, and legal control for enterprise needs; model and compute capacity depend heavily on how the champion strategy and European cooperation evolve.</p>
    <div class="layers">
      <span class="layer-chip">Strong: Application</span>
      <span class="layer-chip">Strong: Data &amp; Legal</span>
      <span class="layer-chip">Constraint: Compute</span>
    </div>
  </div>

  <p><a href="/sail/cases#cohere-aleph-alpha-and-franco-german-tension">See the Cohere / Aleph Alpha case &rarr;</a></p>
</div>

## Methodology

These profiles lead with an interest reading and treat the stack-control assessment as secondary context. The control assessment draws on the [SAIL Specification](/sail/spec), which scores demonstrated capacity, dependency transparency, and exit readiness across seven layers. Control levels are described qualitatively here ("illustrative") rather than as precise scores, because the interesting comparison is between interests and coordination postures, not between point totals.

*Last reviewed: 2026. Profiles are illustrative and maintained by the [Public AI Network](/).*
