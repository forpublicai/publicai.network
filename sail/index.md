---
title: SAIL
layout: page
description: The most comprehensive system for evaluating sovereign AI strategies and systems.
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

.sail-nav a.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

.sail-nav a.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
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
  font-size: 1rem;
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

.featured-post {
  display: block;
  background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%);
  border: 1px solid #c5cff5;
  border-left: 5px solid #667eea;
  border-radius: 8px;
  padding: 1.5rem 1.75rem;
  margin: 2rem 0 3rem 0;
  text-decoration: none;
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.featured-post:hover {
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
  transform: translateY(-2px);
}

.featured-post .label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #667eea;
  margin-bottom: 0.5rem;
}

.featured-post h3 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
  font-size: 1.35rem;
}

.featured-post p {
  margin: 0;
  color: #555;
  line-height: 1.6;
  font-size: 1rem;
}

.featured-post .read-more {
  margin-top: 0.75rem;
  color: #667eea;
  font-weight: 600;
  font-size: 0.95rem;
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

.cert-levels {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 2.5rem;
  margin: 3rem 0;
  flex-wrap: wrap;
}

.cert-level-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  min-width: 120px;
}

.cert-level-icon {
  width: 80px;
  height: 80px;
  margin-bottom: 0.75rem;
}

.cert-level-icon img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.cert-level-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.cert-level-item.platinum .cert-level-name { color: #666; }
.cert-level-item.gold .cert-level-name { color: #b8860b; }
.cert-level-item.silver .cert-level-name { color: #808080; }
.cert-level-item.certified .cert-level-name { color: #dc3545; }

.cert-level-points {
  font-size: 0.95rem;
  color: #666;
  font-weight: 500;
}

.process-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.process-step {
  background: #f8f9fa;
  border-left: 4px solid #667eea;
  padding: 1.5rem;
  border-radius: 8px;
  position: relative;
}

.process-step-number {
  position: absolute;
  top: -15px;
  left: 20px;
  background: #667eea;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
}

.process-step h3 {
  margin-top: 1rem;
  color: #2c3e50;
  font-size: 1.2rem;
}

.process-step p {
  color: #555;
  line-height: 1.6;
  margin-top: 0.5rem;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.resource-item {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  transition: box-shadow 0.2s ease;
}

.resource-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.resource-item h4 {
  color: #667eea;
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.resource-item p {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.6;
  margin: 0;
}

.resource-item a {
  font-weight: 600;
}

.bullet-list {
  list-style: none;
  padding-left: 0;
}

.bullet-list li {
  padding: 0.75rem 0;
  padding-left: 2rem;
  position: relative;
  color: #555;
  line-height: 1.6;
}

.bullet-list li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: #667eea;
  font-weight: bold;
  font-size: 1.5rem;
}

.layer-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.75rem;
  margin: 1.5rem 0;
}

.layer-list a {
  display: block;
  padding: 0.75rem 1rem;
  background: #f8f9fa;
  border-radius: 6px;
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  border-left: 3px solid #667eea;
}

.layer-list a:hover {
  background: #eef1ff;
}

@media (max-width: 768px) {
  .hero h1 { font-size: 2rem; }
  .cert-levels, .process-steps, .resources-grid { grid-template-columns: 1fr; }
}
</style>

<nav class="sail-nav">
  <a href="/sail" class="current">Home</a>
  <a href="/sail/interests">Interests</a>
  <a href="/sail/cases">Cases</a>
  <a href="/sail/spec" class="primary">Specification</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries">Countries</a>
</nav>

<div class="hero">
  <img src="/sail/assets/bsc.jpg" alt="Barcelona Supercomputing Centre" class="hero-image">
  <div class="hero-content">
    <h1>SAIL rating system</h1>
    <p>The most comprehensive system for evaluating sovereign AI strategies and systems.</p>
  </div>
</div>
<p class="image-caption">Barcelona Supercomputing Centre | SAIL-certified AI infrastructure facility</p>

<a href="/sail/blog/decoding-sovereign-ai/" class="featured-post">
  <div class="label">Featured essay</div>
  <h3>Decoding sovereign AI: same word, different interests</h3>
  <p>When policymakers say sovereign AI, they rarely mean the same thing. This essay maps the five interests behind the slogan — security, industrial policy, enterprise control, cultural identity, and middle-power alliance — and explains when the technical stack can help.</p>
  <div class="read-more">Read the essay &rarr;</div>
</a>

<div class="section">
  <h2>SAIL-certified sovereign AI systems are better systems</h2>
  <p>SAIL (Sovereign AI Leadership) is a rating and evaluation system that provides a structured assessment of a country's or agency's AI sovereignty across technical, legal, and governance dimensions. It offers a point-based system that signals resilience, control, and strategic leadership.</p>
  <p>SAIL applies to national strategies, ministries, agencies, and public programs that deploy or govern AI systems. Whether assessing sovereign capacity in applications, data, models, or infrastructure, SAIL helps governments identify strengths and dependencies, optimize capacity, and benchmark progress over time.</p>
</div>

<div class="section">
  <h2>How SAIL works</h2>
  <p>SAIL evaluates sovereignty across <strong>seven layers</strong> — from applications and orchestration to compute and legal governance — through credit categories tailored for each assessment track. An entity must first satisfy baseline prerequisites, then accrue points toward a certification level: Certified, Silver, Gold, or Platinum.</p>

  <div class="layer-list">
    <a href="/sail/spec#layer-1-application--service-sovereignty">Layer 1: Application &amp; Service</a>
    <a href="/sail/spec#layer-2-orchestration-integration--distribution">Layer 2: Orchestration</a>
    <a href="/sail/spec#layer-3-data-sovereignty-origin-control-evaluation">Layer 3: Data</a>
    <a href="/sail/spec#layer-4-model-sovereignty-reproducibility--capability">Layer 4: Model</a>
    <a href="/sail/spec#layer-5-training--post-training-sovereignty">Layer 5: Training</a>
    <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural">Layer 6: Compute</a>
    <a href="/sail/spec#layer-7-legal-governance--exit-sovereignty">Layer 7: Legal &amp; Exit</a>
  </div>

  <div class="cert-levels">
    <div class="cert-level-item platinum">
      <div class="cert-level-icon">
        <img src="/sail/assets/torch_platinum.png" alt="Platinum certification icon">
      </div>
      <div class="cert-level-name">Platinum</div>
      <div class="cert-level-points">80+ points</div>
    </div>
    <div class="cert-level-item gold">
      <div class="cert-level-icon">
        <img src="/sail/assets/torch_gold.png" alt="Gold certification icon">
      </div>
      <div class="cert-level-name">Gold</div>
      <div class="cert-level-points">60–79 points</div>
    </div>
    <div class="cert-level-item silver">
      <div class="cert-level-icon">
        <img src="/sail/assets/torch_silver.png" alt="Silver certification icon">
      </div>
      <div class="cert-level-name">Silver</div>
      <div class="cert-level-points">50–59 points</div>
    </div>
    <div class="cert-level-item certified">
      <div class="cert-level-icon">
        <img src="/sail/assets/torch_red.png" alt="Certified certification icon">
      </div>
      <div class="cert-level-name">Certified</div>
      <div class="cert-level-points">40–49 points</div>
    </div>
  </div>

  <p><a href="/sail/spec">Read the full SAIL specification &rarr;</a></p>
</div>

<div class="section">
  <h2>SAIL assessment process</h2>
  <div class="process-steps">
    <div class="process-step">
      <div class="process-step-number">1</div>
      <h3>Select track and scope</h3>
      <p>Determine whether the assessment applies to a national strategy, ministry, agency, or specific program, and review relevant prerequisites.</p>
    </div>
    <div class="process-step">
      <div class="process-step-number">2</div>
      <h3>Define the assessment</h3>
      <p>Provide baseline documentation and define the scope of AI systems, governance processes, and dependencies.</p>
    </div>
    <div class="process-step">
      <div class="process-step-number">3</div>
      <h3>Build the scorecard</h3>
      <p>Choose credits aligned with your strategy and map responsibilities for evidence gathering and documentation.</p>
    </div>
    <div class="process-step">
      <div class="process-step-number">4</div>
      <h3>Implement and document</h3>
      <p>Execute technical, organizational, and legal actions needed to meet prerequisites and pursue credit categories.</p>
    </div>
    <div class="process-step">
      <div class="process-step-number">5</div>
      <h3>Complete peer review</h3>
      <p>Submit evidence for independent review, scoring, and certification level determination.</p>
    </div>
  </div>
</div>

<div class="section">
  <h2>SAIL tools and resources</h2>
  <div class="resources-grid">
    <div class="resource-item">
      <h4><a href="/sail/spec">Specification</a></h4>
      <p>Complete methodology: seven layers, credits, flags, and control-maturity levels.</p>
    </div>
    <div class="resource-item">
      <h4><a href="/sail/models">Models</a></h4>
      <p>Sovereign AI models tagged by the interests they serve.</p>
    </div>
    <div class="resource-item">
      <h4><a href="/sail/countries">Countries</a></h4>
      <p>Interest profiles and illustrative stack-control assessments.</p>
    </div>
    <div class="resource-item">
      <h4><a href="/sail/interests">Interest decoder</a></h4>
      <p>Reference guide to the five interests behind sovereign AI claims.</p>
    </div>
    <div class="resource-item">
      <h4><a href="/sail/cases">Cases</a></h4>
      <p>Annotated examples: Mistral, OpenAI for Countries, allied public models, and more.</p>
    </div>
    <div class="resource-item">
      <h4><a href="/sail/blog/decoding-sovereign-ai/">Featured essay</a></h4>
      <p>Why decision-makers care about sovereign AI — and when the spec applies.</p>
    </div>
  </div>
</div>

<div class="section">
  <h2>Getting started</h2>
  <ul class="bullet-list">
    <li><strong>Review prerequisites</strong> — Ensure your entity meets the minimum requirements (e.g. legal authority, inventory of AI use).</li>
    <li><strong>Select the relevant track</strong> — National, subnational, or programmatic sovereignty.</li>
    <li><strong>Explore the credit library</strong> — Identify which credits are achievable and which require further capacity building.</li>
  </ul>
</div>

<div class="section">
  <h2>About SAIL</h2>
  <p>SAIL is developed and maintained by the <a href="/">Public AI Network</a> as part of its work on AI as public infrastructure.</p>
</div>
