---
title: SAIL Specification
layout: page
description: Detailed specification of the SAIL rating system methodology and evaluation criteria.
permalink: /sail/spec/
---

<style>
.spec-nav {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.spec-nav a {
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

.spec-nav a:hover {
  background: #667eea;
  color: white;
}

.dimension-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.dimension-card h3 {
  color: #667eea;
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dimension-card h3::before {
  content: '';
  width: 4px;
  height: 24px;
  background: #667eea;
  border-radius: 2px;
}

.metric-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

.metric-table th,
.metric-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.metric-table th {
  background: #f8f9fa;
  font-weight: 600;
  color: #333;
}

.metric-table tr:hover {
  background: #f8f9fa;
}

.weight-badge {
  display: inline-block;
  padding: 4px 8px;
  background: #667eea;
  color: white;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-left: 8px;
}

.scoring-scale {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.score-level {
  text-align: center;
  padding: 1rem;
  border-radius: 8px;
  border: 2px solid;
}

.score-level.excellent {
  background: #d4edda;
  border-color: #28a745;
  color: #155724;
}

.score-level.good {
  background: #d1ecf1;
  border-color: #17a2b8;
  color: #0c5460;
}

.score-level.fair {
  background: #fff3cd;
  border-color: #ffc107;
  color: #856404;
}

.score-level.poor {
  background: #f8d7da;
  border-color: #dc3545;
  color: #721c24;
}

.toc {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin: 2rem 0;
}

.toc ul {
  list-style: none;
  padding-left: 0;
}

.toc li {
  margin: 0.5rem 0;
}

.toc a {
  color: #667eea;
  text-decoration: none;
}

.toc a:hover {
  text-decoration: underline;
}
</style>

<nav class="spec-nav">
  <a href="/sail">🏠 Home</a>
  <a href="/sail/models">🤖 Models</a>
  <a href="/sail/countries">🌍 Countries</a>
</nav>

## SAIL Rating System Specification

This document provides the complete specification for the SAIL (Sovereign AI Index & Leadership) rating system, including evaluation criteria, scoring methodology, and certification requirements.

### Table of Contents

<div class="toc">
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#dimensions">Rating Dimensions</a></li>
  <li><a href="#scoring">Scoring Methodology</a></li>
  <li><a href="#certification">Certification Process</a></li>
  <li><a href="#updates">Version History</a></li>
</ul>
</div>

## Overview {#overview}

The SAIL rating system evaluates sovereign AI initiatives on a scale of 0-10 across five key dimensions. The overall SAIL score is a weighted average of these dimensions, providing a comprehensive assessment of a country's sovereign AI capabilities.

### Overall Score Calculation

```
SAIL Score = (I×0.25) + (G×0.25) + (R×0.20) + (P×0.20) + (S×0.10)

Where:
I = Infrastructure & Capacity (25%)
G = Governance & Policy (25%)
R = Innovation & Research (20%)
P = Public Access & Benefit (20%)
S = Sustainability & Resilience (10%)
```

## Rating Dimensions {#dimensions}

### 1. Infrastructure & Capacity (25% weight)

Evaluates the technical infrastructure and computational resources available for sovereign AI development and deployment.

<table class="metric-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Description</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Compute Infrastructure</strong></td>
      <td>Availability of high-performance computing resources, GPUs, and cloud infrastructure</td>
      <td>30%</td>
    </tr>
    <tr>
      <td><strong>Data Infrastructure</strong></td>
      <td>Quality and accessibility of training data, data governance frameworks, and data sovereignty</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Technical Capabilities</strong></td>
      <td>Expertise in AI/ML development, model training capabilities, and technical talent pool</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Deployment Infrastructure</strong></td>
      <td>Ability to deploy and serve AI models at scale, inference infrastructure, and edge capabilities</td>
      <td>20%</td>
    </tr>
  </tbody>
</table>

### 2. Governance & Policy (25% weight)

Assesses the regulatory frameworks, ethical guidelines, and governance structures for sovereign AI.

<table class="metric-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Description</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Regulatory Framework</strong></td>
      <td>Existence and quality of AI regulations, data protection laws, and policy frameworks</td>
      <td>30%</td>
    </tr>
    <tr>
      <td><strong>Ethical Guidelines</strong></td>
      <td>Adoption of ethical AI principles, bias mitigation, and fairness standards</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Public Oversight</strong></td>
      <td>Transparency, accountability mechanisms, and public participation in AI governance</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>International Cooperation</strong></td>
      <td>Participation in international AI governance initiatives and standards bodies</td>
      <td>20%</td>
    </tr>
  </tbody>
</table>

### 3. Innovation & Research (20% weight)

Measures investment in AI research, development, and innovation capabilities.

<table class="metric-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Description</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>R&D Investment</strong></td>
      <td>Public and private investment in AI research and development</td>
      <td>30%</td>
    </tr>
    <tr>
      <td><strong>Academic Partnerships</strong></td>
      <td>Collaboration with universities, research institutions, and academic excellence in AI</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Innovation Output</strong></td>
      <td>Publications, patents, and technological breakthroughs in AI</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Startup Ecosystem</strong></td>
      <td>Vibrant AI startup ecosystem and innovation hubs</td>
      <td>20%</td>
    </tr>
  </tbody>
</table>

### 4. Public Access & Benefit (20% weight)

Evaluates how accessible and beneficial sovereign AI is to the public.

<table class="metric-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Description</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Accessibility</strong></td>
      <td>Ease of access to AI services for citizens, affordability, and digital inclusion</td>
      <td>30%</td>
    </tr>
    <tr>
      <td><strong>Public Services</strong></td>
      <td>Integration of AI in public services, government applications, and civic technology</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Open Source & Open Data</strong></td>
      <td>Commitment to open source models, open data initiatives, and public goods</td>
      <td>25%</td>
    </tr>
    <tr>
      <td><strong>Public Benefit</strong></td>
      <td>Demonstrated positive impact on society, addressing public needs, and social good</td>
      <td>20%</td>
    </tr>
  </tbody>
</table>

### 5. Sustainability & Resilience (10% weight)

Assesses long-term viability, security, and independence of sovereign AI initiatives.

<table class="metric-table">
  <thead>
    <tr>
      <th>Metric</th>
      <th>Description</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Long-term Viability</strong></td>
      <td>Sustainable funding models, maintenance capacity, and long-term planning</td>
      <td>35%</td>
    </tr>
    <tr>
      <td><strong>Security & Privacy</strong></td>
      <td>Cybersecurity measures, data protection, and privacy safeguards</td>
      <td>30%</td>
    </tr>
    <tr>
      <td><strong>Independence</strong></td>
      <td>Reduced dependence on foreign technology, supply chain resilience, and sovereignty</td>
      <td>35%</td>
    </tr>
  </tbody>
</table>

## Scoring Methodology {#scoring}

### Score Scale

<div class="scoring-scale">
  <div class="score-level excellent">
    <strong>9.0 - 10.0</strong><br>
    Excellent<br>
    World-leading capabilities
  </div>
  <div class="score-level good">
    <strong>7.0 - 8.9</strong><br>
    Good<br>
    Strong capabilities
  </div>
  <div class="score-level fair">
    <strong>5.0 - 6.9</strong><br>
    Fair<br>
    Developing capabilities
  </div>
  <div class="score-level poor">
    <strong>0.0 - 4.9</strong><br>
    Poor<br>
    Limited capabilities
  </div>
</div>

### Evaluation Process

1. **Data Collection**: Gather information from public sources, official reports, and verified submissions
2. **Expert Review**: Independent experts evaluate each dimension based on established criteria
3. **Peer Review**: Findings are reviewed by a panel of international experts
4. **Public Comment**: Draft ratings are published for public comment and feedback
5. **Final Rating**: Ratings are finalized and published with detailed justifications

### Data Sources

- Government reports and official documentation
- Academic publications and research papers
- Industry reports and analysis
- Verified submissions from countries and organizations
- Public data and open government initiatives

## Certification Process {#certification}

### SAIL Certification Levels

- **SAIL Certified** (Score ≥ 8.0): Recognizes excellence in sovereign AI development
- **SAIL Compliant** (Score ≥ 6.0): Meets minimum standards for sovereign AI
- **SAIL Developing** (Score < 6.0): Acknowledges ongoing development efforts

### Certification Requirements

To achieve SAIL certification, initiatives must:

1. Meet minimum thresholds across all five dimensions
2. Demonstrate commitment to public benefit and accessibility
3. Provide transparent documentation of capabilities and governance
4. Commit to continuous improvement and regular updates
5. Participate in peer review and public accountability processes

### Application Process

1. Submit application with comprehensive documentation
2. Initial review by SAIL evaluation team
3. Independent expert assessment
4. Public comment period
5. Certification decision and publication

## Version History {#updates}

- **v1.0** (2024): Initial specification release
- **v1.1** (2025): Enhanced sustainability metrics, updated weighting scheme

---

*This specification is maintained by the Public AI Network. For questions or suggestions, please contact [info@publicai.network](mailto:info@publicai.network).*
