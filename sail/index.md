---
title: SAIL Rating System
layout: page
description: The most comprehensive system for evaluating sovereign AI strategies and systems.
permalink: /sail/
---

<style>
.sail-nav {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.sail-nav a {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.sail-nav a:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.hero {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 12px;
  margin: 2rem 0;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 300px;
  height: 300px;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="none" stroke="rgba(102,126,234,0.1)" stroke-width="2"/><circle cx="100" cy="100" r="60" fill="none" stroke="rgba(102,126,234,0.1)" stroke-width="2"/><circle cx="100" cy="100" r="40" fill="none" stroke="rgba(102,126,234,0.1)" stroke-width="2"/></svg>') no-repeat;
  background-size: contain;
  opacity: 0.3;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: #2c3e50;
  position: relative;
  z-index: 1;
}

.hero p {
  font-size: 1.3rem;
  color: #555;
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  line-height: 1.6;
}

.section-divider {
  border: none;
  border-top: 2px solid #e0e0e0;
  margin: 4rem 0;
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
}

.cert-level-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}

.cert-level-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

.cert-level-card.platinum::before {
  background: linear-gradient(90deg, #e8e8e8 0%, #c0c0c0 100%);
}

.cert-level-card.gold::before {
  background: linear-gradient(90deg, #ffd700 0%, #ffed4e 100%);
}

.cert-level-card.silver::before {
  background: linear-gradient(90deg, #c0c0c0 0%, #e8e8e8 100%);
}

.cert-level-card.certified::before {
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

.cert-level-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}

.cert-level-name {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.cert-level-card.platinum .cert-level-name {
  color: #666;
}

.cert-level-card.gold .cert-level-name {
  color: #b8860b;
}

.cert-level-card.silver .cert-level-name {
  color: #808080;
}

.cert-level-card.certified .cert-level-name {
  color: #667eea;
}

.cert-level-points {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1rem;
  font-weight: 600;
}

.cert-level-desc {
  font-size: 1rem;
  color: #777;
  line-height: 1.6;
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
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
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

.placeholder-image {
  width: 100%;
  height: 300px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 1.1rem;
  margin: 2rem 0;
  border: 2px dashed #ddd;
}

.placeholder-image.small {
  height: 200px;
}

.cert-table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

.cert-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.cert-table th,
.cert-table td {
  padding: 1.2rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.cert-table th {
  font-weight: 600;
  font-size: 1rem;
}

.cert-table tbody tr:last-child td {
  border-bottom: none;
}

.cert-table tbody tr:hover {
  background: #f8f9fa;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }
  
  .hero p {
    font-size: 1.1rem;
  }
  
  .cert-levels,
  .process-steps,
  .resources-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="hero">
  <h1>SAIL rating system</h1>
  <p>The most comprehensive system for evaluating sovereign AI strategies and systems.</p>
</div>

<nav class="sail-nav">
  <a href="/sail/spec">📋 Specification</a>
  <a href="/sail/models">🤖 Models</a>
  <a href="/sail/countries">🌍 Countries</a>
</nav>

<div class="placeholder-image">
  [Placeholder: SAIL-certified government building or AI infrastructure facility]
</div>

<div class="section">
  <h2>SAIL-certified sovereign AI systems are better systems</h2>
  <p>SAIL (Sovereign AI Leadership) is a rating and evaluation system that provides a structured assessment of a country's or agency's AI sovereignty across technical, legal, and governance dimensions. It offers a point-based system that signals resilience, control, and strategic leadership.</p>
  <p>SAIL serves as a globally recognized symbol of sovereignty leadership, supported by a committed community of governments, agencies, and technical partners driving market transformation toward resilient AI governance.</p>
</div>

<hr class="section-divider">

<div class="section">
  <h2>SAIL is designed for all AI governance contexts</h2>
  <p>SAIL applies to national strategies, ministries, agencies, and public programs that deploy or govern AI systems. Whether assessing sovereign capacity in applications, data, models, or infrastructure, SAIL helps governments identify strengths and dependencies, optimize capacity, and benchmark progress over time.</p>
  
  <div class="placeholder-image small">
    [Placeholder: Illustration showing different governance contexts - national, ministry, agency, program]
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>How SAIL works</h2>
  <p>SAIL is holistic. As a framework, it evaluates sovereignty across seven layers—from applications and orchestration to compute and legal governance—through a series of credit categories tailored for each assessment track. To achieve SAIL certification, an entity must first satisfy baseline prerequisites and then accrue points by fulfilling credit criteria. Assessments are independently verified and award points that correspond to a level of SAIL certification: Certified, Silver, Gold, and Platinum.</p>
</div>

<hr class="section-divider">

<div class="section">
  <h2>SAIL Certification Levels</h2>
  
  <table class="cert-table">
    <thead>
      <tr>
        <th>Level</th>
        <th>Points earned</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Platinum — Structural Sovereignty</strong></td>
        <td>80+ points</td>
      </tr>
      <tr>
        <td><strong>Gold — Strategic Sovereignty</strong></td>
        <td>60–79 points</td>
      </tr>
      <tr>
        <td><strong>Silver — Operational Sovereignty</strong></td>
        <td>50–59 points</td>
      </tr>
      <tr>
        <td><strong>Certified — Foundational Sovereignty</strong></td>
        <td>40–49 points</td>
      </tr>
    </tbody>
  </table>
  
  <p style="margin-top: 1.5rem;">Each level signals a distinct combination of capability and control across the SAIL layers, enabling nuanced comparisons among countries and agencies.</p>
  
  <div class="cert-levels">
    <div class="cert-level-card platinum">
      <div class="cert-level-name">Platinum</div>
      <div class="cert-level-points">80+ points</div>
      <div class="cert-level-desc">Structural Sovereignty — Demonstrates end-to-end control across the AI stack</div>
    </div>
    
    <div class="cert-level-card gold">
      <div class="cert-level-name">Gold</div>
      <div class="cert-level-points">60–79 points</div>
      <div class="cert-level-desc">Strategic Sovereignty — Strong control over data and model behavior</div>
    </div>
    
    <div class="cert-level-card silver">
      <div class="cert-level-name">Silver</div>
      <div class="cert-level-points">50–59 points</div>
      <div class="cert-level-desc">Operational Sovereignty — Control at application and data layers</div>
    </div>
    
    <div class="cert-level-card certified">
      <div class="cert-level-name">Certified</div>
      <div class="cert-level-points">40–49 points</div>
      <div class="cert-level-desc">Foundational Sovereignty — Initial control over AI deployment</div>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>SAIL Assessment Process</h2>
  
  <div class="process-steps">
    <div class="process-step">
      <div class="process-step-number">1</div>
      <h3>Select the appropriate SAIL track and scope</h3>
      <p>Determine whether the assessment applies to a national strategy, ministry, agency, or specific program, and review relevant prerequisites.</p>
    </div>
    
    <div class="process-step">
      <div class="process-step-number">2</div>
      <h3>Register the assessment</h3>
      <p>Provide baseline documentation and define the scope of AI systems, governance processes, and dependencies.</p>
    </div>
    
    <div class="process-step">
      <div class="process-step-number">3</div>
      <h3>Build the SAIL scorecard</h3>
      <p>Choose the credits aligned with your strategy and map responsibilities for evidence gathering and documentation.</p>
    </div>
    
    <div class="process-step">
      <div class="process-step-number">4</div>
      <h3>Implement sovereignty strategies</h3>
      <p>Execute technical, organizational, and legal actions needed to meet prerequisites and pursue credit categories.</p>
    </div>
    
    <div class="process-step">
      <div class="process-step-number">5</div>
      <h3>Submit for verification</h3>
      <p>Upload evidence to the SAIL review portal and undergo independent verification for scoring and certification.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>SAIL Tools and Resources</h2>
  <p>SAIL is supported by a suite of resources designed to help teams understand and fulfill credit requirements:</p>
  
  <div class="resources-grid">
    <div class="resource-item">
      <h4>SAIL Credit Library</h4>
      <p>Detailed descriptions of credit criteria and evidence requirements.</p>
    </div>
    
    <div class="resource-item">
      <h4>SAIL Reference Guides</h4>
      <p>Comprehensive manuals that provide interpretations, examples, and compliance pathways.</p>
    </div>
    
    <div class="resource-item">
      <h4>Scorecard Templates</h4>
      <p>Pre-formatted scorecards for rapid self-assessment.</p>
    </div>
    
    <div class="resource-item">
      <h4>Independent Review Portal</h4>
      <p>A secure platform for submission and verification of evidence.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>Understanding SAIL and Getting Started</h2>
  <p>Before pursuing SAIL certification:</p>
  
  <ul class="bullet-list">
    <li><strong>Review prerequisites</strong> – Ensure your entity meets the minimum requirements for certification (e.g., legal authority, inventory of AI use).</li>
    <li><strong>Select the relevant track</strong> – Choose the right assessment track depending on whether you are assessing national, subnational, or programmatic sovereignty.</li>
    <li><strong>Explore the credit library</strong> – Identify which credits are achievable and which require further capacity building.</li>
  </ul>
  
  <div class="placeholder-image small">
    [Placeholder: Getting started guide illustration or flowchart]
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>Certification and Recognition</h2>
  <p>Once certified, entities can:</p>
  
  <ul class="bullet-list">
    <li><strong>Showcase their sovereignty achievements</strong> through SAIL badges and scorecards.</li>
    <li><strong>Use certification results</strong> to guide policy priorities and capacity investments.</li>
    <li><strong>Participate in the SAIL community</strong> to share best practices and influence future updates.</li>
  </ul>
  
  <div class="placeholder-image small">
    [Placeholder: SAIL certification badge examples or recognition showcase]
  </div>
</div>

<hr class="section-divider">

<div class="section">
  <h2>SAIL Evolution & Versioning</h2>
  <p>SAIL evolves periodically to reflect advances in AI technologies, governance practices, and geopolitical realities. Updates to the SAIL framework are developed through a multi-stakeholder process involving public sector experts, technologists, and civil society, with opportunities for public comment and pilot testing before formal adoption.</p>
</div>

<hr class="section-divider">

<div class="section">
  <h2>About the SAIL Initiative</h2>
  <p>The SAIL program is developed and maintained by the <strong>Sovereign AI Leadership Consortium</strong>, a multi-stakeholder body of governments, research institutions, and technical partners committed to advancing sovereign and resilient AI governance. SAIL aims to make sovereignty legible, actionable, and comparable across contexts.</p>
  
  <div class="placeholder-image">
    [Placeholder: Consortium members or partner organizations logo display]
  </div>
</div>
