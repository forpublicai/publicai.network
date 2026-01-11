---
title: SAIL Rating System
layout: page
description: A comprehensive rating system and certification program for sovereign AI initiatives worldwide.
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
  padding: 3rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 12px;
  margin: 2rem 0;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  text-align: center;
  transition: transform 0.2s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: #667eea;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.feature-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.feature-card h3 {
  color: #667eea;
  margin-top: 0;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }
  
  .stats-grid,
  .features {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="hero">
  <h1>SAIL Rating System</h1>
  <p style="font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto;">
    A comprehensive rating system and certification program for sovereign AI initiatives worldwide. 
    Evaluate, compare, and improve sovereign AI capabilities across nations.
  </p>
</div>

<nav class="sail-nav">
  <a href="/sail/spec">📋 Specification</a>
  <a href="/sail/models">🤖 Models</a>
  <a href="/sail/countries">🌍 Countries</a>
</nav>

## Overview

The **SAIL (Sovereign AI Index & Leadership)** Rating System provides a standardized framework for evaluating sovereign AI initiatives. It assesses countries' capabilities across multiple dimensions including infrastructure, governance, innovation, and public benefit.

## Key Metrics

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number" id="countries-count">-</div>
    <div class="stat-label">Countries Evaluated</div>
  </div>
  <div class="stat-card">
    <div class="stat-number" id="models-count">-</div>
    <div class="stat-label">Models Tracked</div>
  </div>
  <div class="stat-card">
    <div class="stat-number" id="avg-score">-</div>
    <div class="stat-label">Average SAIL Score</div>
  </div>
  <div class="stat-card">
    <div class="stat-number" id="certified-count">-</div>
    <div class="stat-label">Certified Initiatives</div>
  </div>
</div>

## Core Features

<div class="features">
  <div class="feature-card">
    <h3>📊 Comprehensive Evaluation</h3>
    <p>Multi-dimensional assessment covering technical capabilities, governance frameworks, public accessibility, and ethical standards.</p>
  </div>
  
  <div class="feature-card">
    <h3>🌐 Global Comparison</h3>
    <p>Compare sovereign AI initiatives across different countries and regions to identify best practices and areas for improvement.</p>
  </div>
  
  <div class="feature-card">
    <h3>✅ Certification Program</h3>
    <p>Recognize initiatives that meet high standards for sovereign AI development and deployment.</p>
  </div>
  
  <div class="feature-card">
    <h3>📈 Continuous Monitoring</h3>
    <p>Track progress over time as countries develop and enhance their sovereign AI capabilities.</p>
  </div>
  
  <div class="feature-card">
    <h3>🔍 Transparency</h3>
    <p>Open methodology and scoring criteria ensure accountability and enable peer review.</p>
  </div>
  
  <div class="feature-card">
    <h3>🤝 Collaboration</h3>
    <p>Foster international cooperation and knowledge sharing in sovereign AI development.</p>
  </div>
</div>

## Rating Dimensions

The SAIL rating system evaluates sovereign AI initiatives across five key dimensions:

1. **Infrastructure & Capacity** - Compute resources, data infrastructure, and technical capabilities
2. **Governance & Policy** - Regulatory frameworks, ethical guidelines, and public oversight
3. **Innovation & Research** - R&D investments, academic partnerships, and technological advancement
4. **Public Access & Benefit** - Accessibility, affordability, and public good orientation
5. **Sustainability & Resilience** - Long-term viability, security, and independence

## Getting Started

- **Learn about the methodology**: Read the [SAIL Specification](/sail/spec) to understand how ratings are calculated
- **Explore models**: Browse [Sovereign AI Models](/sail/models) from different countries
- **Compare countries**: View [Country Rankings](/sail/countries) and detailed assessments

## Contributing

The SAIL rating system is an open, collaborative effort. We welcome contributions from researchers, policymakers, and practitioners working on sovereign AI initiatives.

- Submit updates to country or model information
- Propose improvements to the rating methodology
- Share case studies and best practices

<script>
// Dynamic stats loading (placeholder - would be replaced with actual data)
document.addEventListener('DOMContentLoaded', function() {
  // These would typically be loaded from an API or data file
  setTimeout(() => {
    document.getElementById('countries-count').textContent = '25+';
    document.getElementById('models-count').textContent = '50+';
    document.getElementById('avg-score').textContent = '7.2';
    document.getElementById('certified-count').textContent = '12';
  }, 300);
});
</script>
