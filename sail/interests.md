---
title: SAIL Interests
layout: page
description: Decoding what policymakers and institutions actually want when they invoke sovereign AI.
permalink: /sail/interests/
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

.lede {
  font-size: 1.15rem;
  line-height: 1.7;
  color: #444;
  margin: 1.5rem 0;
}

.interest-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-left: 5px solid #667eea;
  border-radius: 8px;
  padding: 1.75rem 2rem;
  margin: 2rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.interest-card h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 1.5rem;
}

.interest-card .says {
  font-style: italic;
  color: #555;
  border-left: 3px solid #e0e0e0;
  padding-left: 1rem;
  margin: 1rem 0;
}

.interest-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 1.25rem 0;
}

@media (min-width: 700px) {
  .interest-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.interest-field {
  background: #f8f9fa;
  border-radius: 6px;
  padding: 1rem 1.25rem;
}

.interest-field h4 {
  margin: 0 0 0.5rem 0;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #667eea;
}

.interest-field p {
  margin: 0;
  color: #555;
  line-height: 1.6;
}

.interest-field.limit {
  border-left: 4px solid #dc3545;
  background: #fdf2f3;
}

.interest-field.limit h4 {
  color: #dc3545;
}

.interest-field.coord {
  border-left: 4px solid #ffc107;
  background: #fffbf0;
}

.interest-field.coord h4 {
  color: #b8860b;
}

.layer-tags {
  margin-top: 0.5rem;
}

.layer-tag {
  display: inline-block;
  padding: 3px 10px;
  background: #667eea;
  color: white;
  border-radius: 14px;
  font-size: 0.8rem;
  font-weight: 600;
  margin: 2px 4px 2px 0;
  text-decoration: none;
}

.layer-tag:hover {
  background: #5568d3;
  color: white;
}

.decoder-box {
  background: #d1ecf1;
  border-left: 5px solid #17a2b8;
  border-radius: 6px;
  padding: 1.5rem 2rem;
  margin: 2.5rem 0;
}

.decoder-box h3 {
  margin-top: 0;
  color: #0c5460;
}

.decoder-box ul {
  margin: 0.75rem 0 0 0;
}

.decoder-box li {
  margin: 0.6rem 0;
  line-height: 1.6;
}

.section-divider {
  border: none;
  border-top: 2px solid #e0e0e0;
  margin: 3.5rem 0;
}

.related-links {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem 2rem;
  margin: 2rem 0;
}

.related-links h3 {
  margin-top: 0;
  color: #2c3e50;
}
</style>

<nav class="sail-nav">
  <a href="/sail">Home</a>
  <a href="/sail/interests" class="current">Interests</a>
  <a href="/sail/cases">Cases</a>
  <a href="/sail/spec">Specification</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries">Countries</a>
</nav>

# What do people actually want from sovereign AI?

<p class="lede">When a minister, a CIO, or an industrial-policy lead says "sovereign AI," they rarely mean the same thing. This reference guide maps the most common interests behind the slogan. For the narrative introduction, read the <a href="/sail/blog/decoding-sovereign-ai/">featured essay</a>.</p>

We are less interested in settling what sovereign AI *is* than in reading why decision-makers care. The same demand for "sovereignty" can be a bid for vendor independence, a play for chips and jobs, a data-residency requirement, or a cultural statement. Treating these as one thing is how policy debates go in circles.

<hr class="section-divider">

## Security and weaponization

<div class="interest-card">
  <h3>Security and weaponization</h3>
  <p class="says">"We cannot run critical national systems on AI that a foreign government or vendor could read, alter, or switch off."</p>

  <div class="interest-grid">
    <div class="interest-field">
      <h4>What they want</h4>
      <p>Assurance that no single foreign actor can disable, surveil, or tamper with the systems they depend on. The classic answer is source-code escrow and infrastructure control &mdash; Microsoft's offer to keep a copy of source in a hardened Swiss facility is this interest made literal.</p>
    </div>
    <div class="interest-field">
      <h4>Typical instruments</h4>
      <p>Source escrow, on-soil hosting, kill-switch audits, classified-environment deployments, supply-chain review of hardware and weights.</p>
    </div>
    <div class="interest-field">
      <h4>Where SAIL speaks to it</h4>
      <p>Compute control and the absence of unilateral kill-switches, plus legal authority to override or retire systems.</p>
      <div class="layer-tags">
        <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural" class="layer-tag">Layer 6: Compute</a>
        <a href="/sail/spec#layer-7-legal-governance--exit-sovereignty" class="layer-tag">Layer 7: Legal &amp; Exit</a>
      </div>
    </div>
    <div class="interest-field limit">
      <h4>What it cannot solve</h4>
      <p>Escrow proves you could read the source; it does not give you the talent, data, or compute to rebuild and run the system independently. Security control is necessary but not the same as capability.</p>
    </div>
  </div>
</div>

## Industrial policy

<div class="interest-card">
  <h3>Industrial policy</h3>
  <p class="says">"AI is the next growth engine. We need the chips, the fabs, the data centers, and the talent here, building national champions."</p>

  <div class="interest-grid">
    <div class="interest-field">
      <h4>What they want</h4>
      <p>Domestic economic capacity: compute hardware, energy, skilled workers, and a flagship lab or two. "Sovereign AI" is often the headline; the underlying pet interest may really be minerals, energy contracts, or jobs in a region.</p>
    </div>
    <div class="interest-field">
      <h4>Typical instruments</h4>
      <p>Subsidies and tax breaks, sovereign compute clusters, immigration lanes for researchers, procurement preferences for domestic vendors, energy and minerals deals.</p>
    </div>
    <div class="interest-field">
      <h4>Where SAIL speaks to it</h4>
      <p>Compute and infrastructure capacity is the layer that maps most directly; model and training capacity matter when the goal is a genuine domestic lab rather than a press release.</p>
      <div class="layer-tags">
        <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural" class="layer-tag">Layer 6: Compute</a>
        <a href="/sail/spec#layer-4-model-sovereignty-reproducibility--capability" class="layer-tag">Layer 4: Model</a>
        <a href="/sail/spec#layer-5-training--post-training-sovereignty" class="layer-tag">Layer 5: Training</a>
      </div>
    </div>
    <div class="interest-field coord">
      <h4>Coordination risk</h4>
      <p>High. If every country races to onshore the same chips and poach the same talent, middle powers compete instead of pooling. The backlash to Cohere and Aleph Alpha shows how quickly "national champion" becomes "now we don't have to depend on our neighbors."</p>
    </div>
  </div>
</div>

## Enterprise and procurement

<div class="interest-card">
  <h3>Enterprise and procurement</h3>
  <p class="says">"Our data cannot leave the jurisdiction, and we need a contract we can exit without rebuilding everything."</p>

  <div class="interest-grid">
    <div class="interest-field">
      <h4>What they want</h4>
      <p>Control over the data supply chain and the commercial relationship. This is the most concrete and tractable interest: it is mostly about residency, provenance, auditability, and contractual exit rights, not national identity.</p>
    </div>
    <div class="interest-field">
      <h4>Typical instruments</h4>
      <p>Data-residency clauses, provenance and deletion rights, model-agnostic architectures, vendor-substitution clauses, observability and audit logging.</p>
    </div>
    <div class="interest-field">
      <h4>Where SAIL speaks to it</h4>
      <p>This is the part of sovereign AI that SAIL was built to assess. Application portability, orchestration independence, and data control are directly scorable.</p>
      <div class="layer-tags">
        <a href="/sail/spec#layer-1-application--service-sovereignty" class="layer-tag">Layer 1: Application</a>
        <a href="/sail/spec#layer-2-orchestration-integration--distribution" class="layer-tag">Layer 2: Orchestration</a>
        <a href="/sail/spec#layer-3-data-sovereignty-origin-control-evaluation" class="layer-tag">Layer 3: Data</a>
      </div>
    </div>
    <div class="interest-field">
      <h4>Why it travels well</h4>
      <p>Because it is about capability and contracts rather than symbolism, this interest is the one where productization and certification genuinely help.</p>
    </div>
  </div>
</div>

## Cultural identity and values

<div class="interest-card">
  <h3>Cultural identity and values</h3>
  <p class="says">"A French model should be and feel French. It should reflect our language, our law, and our values."</p>

  <div class="interest-grid">
    <div class="interest-field">
      <h4>What they want</h4>
      <p>A system that represents a community's language, culture, and norms &mdash; not just one hosted on home soil. This is a question of legitimacy and representation, not infrastructure.</p>
    </div>
    <div class="interest-field">
      <h4>Typical instruments</h4>
      <p>Domestic data and evaluation sets, language and cultural fine-tuning, public oversight of training objectives, participatory governance.</p>
    </div>
    <div class="interest-field">
      <h4>Where SAIL speaks to it</h4>
      <p>Partially. Owning data, evaluations, and training objectives is relevant, but these are inputs to legitimacy, not legitimacy itself.</p>
      <div class="layer-tags">
        <a href="/sail/spec#layer-3-data-sovereignty-origin-control-evaluation" class="layer-tag">Layer 3: Data</a>
        <a href="/sail/spec#layer-5-training--post-training-sovereignty" class="layer-tag">Layer 5: Training</a>
      </div>
    </div>
    <div class="interest-field limit">
      <h4>What it cannot solve</h4>
      <p>A model feeling French cannot be certified into existence. No checklist confers cultural legitimacy; that comes from who governs the system and whether communities recognize themselves in it. Treating values as a productization problem is the most common category error in the sovereign AI debate.</p>
    </div>
  </div>
</div>

## Middle-power alliance

<div class="interest-card">
  <h3>Middle-power alliance</h3>
  <p class="says">"We cannot match the hyperscalers alone, so we pool compute, data, and models with trusted partners."</p>

  <div class="interest-grid">
    <div class="interest-field">
      <h4>What they want</h4>
      <p>Strategic autonomy without autarky. Rather than build everything domestically, they share capacity through federated compute, joint models, and allied governance &mdash; reducing dependence on any single hyperscaler or superpower.</p>
    </div>
    <div class="interest-field">
      <h4>Typical instruments</h4>
      <p>Federated compute agreements, jointly governed open models, shared evaluation infrastructure, multilateral funding (the "Airbus for AI" idea).</p>
    </div>
    <div class="interest-field">
      <h4>Where SAIL speaks to it</h4>
      <p>SAIL explicitly credits federated and allied arrangements as legitimate sovereignty, provided dependencies are acknowledged. This is the one interest the spec actively rewards over going it alone.</p>
      <div class="layer-tags">
        <a href="/sail/spec#layers" class="layer-tag">Federation principle</a>
        <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural" class="layer-tag">Layer 6: Compute</a>
      </div>
    </div>
    <div class="interest-field coord">
      <h4>Coordination risk</h4>
      <p>This is the strategy that nationalist industrial policy quietly undermines. Every country chasing its own champion erodes the trust a joint middle-power approach needs. The interest is fragile precisely because it depends on others resisting the same temptation.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="decoder-box">
  <h3 id="decoder-is-this-about-refusing-the-openai-for-countries-deal">Decoder: is this about refusing the OpenAI for Countries deal?</h3>
  <p>A government declining a hyperscaler's national-AI offer is read as a single act of sovereignty. It rarely is. The same refusal can mean very different things:</p>
  <ul>
    <li><strong>Vendor diversification</strong> &mdash; they want optionality and exit rights, and would happily sign with two vendors instead of one. This is the enterprise interest in disguise (Layers 1&ndash;3).</li>
    <li><strong>Domestic champion building</strong> &mdash; they are protecting a national lab or a planned compute build-out. This is industrial policy, and the deal is a competitor (Layers 4&ndash;6).</li>
    <li><strong>Security posture</strong> &mdash; they cannot accept a foreign kill-switch on critical systems regardless of price (Layers 6&ndash;7).</li>
    <li><strong>Electoral or values signaling</strong> &mdash; the refusal is the point; the policy substance is secondary. No layer of the spec addresses this, and pretending otherwise wastes everyone's time.</li>
  </ul>
  <p>Before designing a response, decode which of these is actually driving the decision. The strategy that follows is completely different in each case.</p>
</div>

## When sovereignty and LLMs pull apart

It is worth saying plainly: some sovereignty claims sit awkwardly with how large language models actually work. LLMs have steep fixed costs, benefit enormously from scale and shared data, and are cheap to copy once trained. That profile suits a globally provisioned public good with some decentralization far better than it suits dozens of self-sufficient national stacks.

For several of the interests above &mdash; especially middle-power alliance and the capability dimension of industrial policy &mdash; the most sovereign outcome may be a shared, openly governed system rather than a national one. That is the [public AI](/) frame: treat the model as public infrastructure, govern it accountably, and let many parties draw on it. Sovereignty becomes a question of governance and access, not of ownership and borders.

<div class="related-links">
  <h3>Read further</h3>
  <ul>
    <li><a href="/sail/cases">SAIL Cases</a> &mdash; annotated examples of these interests in the wild.</li>
    <li><a href="/sail/spec">SAIL Specification</a> &mdash; the seven-layer assessment, with a guide to when it applies.</li>
    <li><a href="https://ainowinstitute.org/publications/research/ai-nationalisms-global-industrial-policy-approaches-to-ai" target="_blank" rel="noopener">AI Nationalisms</a> (AI Now Institute) &mdash; survey of industrial-policy approaches behind sovereignty claims.</li>
    <li><a href="https://publicai.co/airbus-for-ai.pdf" target="_blank" rel="noopener">Airbus for AI</a> &mdash; the multilateral, pooled-capacity alternative to national champions.</li>
    <li><a href="/handbook">Public AI Handbook</a>, Week 3 &mdash; national strategies, sovereignty, and coordination.</li>
  </ul>
</div>
