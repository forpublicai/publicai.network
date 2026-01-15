---
title: SAIL Rating System
layout: page
description: The most comprehensive system for evaluating sovereign AI strategies and systems.
permalink: /sail/
---

<style>
/* Hide the auto-generated page title */
.post-header,
.post-title {
  display: none !important;
}

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

.sail-nav a.disabled {
  background: #e0e0e0;
  color: #999;
  cursor: not-allowed;
  opacity: 0.6;
  pointer-events: none;
}

.sail-nav a.disabled:hover {
  transform: none;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.hero {
  text-align: center;
  padding: 6rem 2rem;
  background-image: /assets/bsc.jpg;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 12px;
  margin: 2rem 0;
  position: relative;
  overflow: hidden;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 1;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: white;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero p {
  font-size: 1.3rem;
  color: white;
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  line-height: 1.6;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
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

.cert-level-item.platinum .cert-level-name {
  color: #666;
}

.cert-level-item.gold .cert-level-name {
  color: #b8860b;
}

.cert-level-item.silver .cert-level-name {
  color: #808080;
}

.cert-level-item.certified .cert-level-name {
  color: #dc3545;
}

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
  border-radius: 8px;
  margin: 2rem 0 0.5rem 0;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.placeholder-image.small {
  height: 200px;
}

.placeholder-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-caption {
  font-size: 0.8rem;
  color: #666;
  font-style: italic;
  text-align: center;
  margin-bottom: 2rem;
  padding: 0 1rem;
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
<p class="image-caption">Barcelona Supercomputing Centre | SAIL-certified AI infrastructure facility</p>

<div class="section">
  <h2>SAIL-certified sovereign AI systems are better systems</h2>
  <p>SAIL (Sovereign AI Leadership) is a rating and evaluation system that provides a structured assessment of a country's or agency's AI sovereignty across technical, legal, and governance dimensions. It offers a point-based system that signals resilience, control, and strategic leadership.</p>
  <p>SAIL serves as a globally recognized symbol of sovereignty leadership, supported by a committed community of governments, agencies, and technical partners driving market transformation toward resilient AI governance.</p>
</div>

<div class="section">
  <h2>SAIL is designed for all AI governance contexts</h2>
  <p>SAIL applies to national strategies, ministries, agencies, and public programs that deploy or govern AI systems. Whether assessing sovereign capacity in applications, data, models, or infrastructure, SAIL helps governments identify strengths and dependencies, optimize capacity, and benchmark progress over time.</p>
  
  <div class="placeholder-image small">
    <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=800&fit=crop" alt="AI governance contexts - national, ministry, agency, program">
  </div>
  <p class="image-caption">AI governance contexts - national, ministry, agency, program</p>
</div>

<div class="section">
  <h2>How SAIL works</h2>
  <p>SAIL is holistic. As a framework, it evaluates sovereignty across seven layers—from applications and orchestration to compute and legal governance—through a series of credit categories tailored for each assessment track. To achieve SAIL certification, an entity must first satisfy baseline prerequisites and then accrue points by fulfilling credit criteria. Assessments are independently verified and award points that correspond to a level of SAIL certification: Certified, Silver, Gold, and Platinum.</p>
  
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
</div>

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

<div class="section">
  <h2>SAIL Tools and Resources</h2>
  <p>SAIL is supported by a suite of resources designed to help teams understand and fulfill credit requirements:</p>
  
  <nav class="sail-nav">
    <a href="/sail/spec">📋 Specification</a>
    <a href="#" class="disabled">🤖 Models</a>
    <a href="#" class="disabled">🌍 Countries</a>
  </nav>
</div>

<div class="section">
  <h2>Understanding SAIL and Getting Started</h2>
  <p>Before pursuing SAIL certification:</p>
  
  <ul class="bullet-list">
    <li><strong>Review prerequisites</strong> – Ensure your entity meets the minimum requirements for certification (e.g., legal authority, inventory of AI use).</li>
    <li><strong>Select the relevant track</strong> – Choose the right assessment track depending on whether you are assessing national, subnational, or programmatic sovereignty.</li>
    <li><strong>Explore the credit library</strong> – Identify which credits are achievable and which require further capacity building.</li>
  </ul>
  
  <div class="placeholder-image small">
    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=800&fit=crop" alt="Getting started guide - SAIL assessment flowchart">
  </div>
  <p class="image-caption">Getting started guide - SAIL assessment flowchart</p>
</div>

<div class="section">
  <h2>Certification and Recognition</h2>
  <p>Once certified, projects have joined a select group of leaders in AI. They can then order or download a certificate for display, and share the news through a coordinated press release.</p>
  <div class="placeholder-image small">
    <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1200&h=800&fit=crop" alt="SAIL certification badges and recognition showcase">
  </div>
  <p class="image-caption">SAIL certification badges and recognition showcase</p>
</div>

<div class="section">
  <h2>About SAIL</h2>
  <p>The SAIL program is developed and maintained by the <strong>Public AI Regular Council</strong>.</p>
  
  <div class="placeholder-image">
    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&h=600&fit=crop" alt="Sovereign AI Leadership Consortium partners and members">
  </div>
  <p class="image-caption">Sovereign AI Leadership Consortium partners and members</p>
</div>
