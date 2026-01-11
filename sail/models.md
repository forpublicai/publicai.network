---
title: SAIL Models
layout: page
description: Comprehensive directory of sovereign AI models and implementations evaluated under the SAIL certification program.
permalink: /sail/models/
---

<style>
.models-nav {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.models-nav a {
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

.models-nav a:hover {
  background: #667eea;
  color: white;
}

.filter-bar {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  align-items: center;
}

.filter-bar select,
.filter-bar input {
  padding: 10px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
}

.filter-bar input {
  flex: 1;
  min-width: 200px;
}

.model-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.model-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.model-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.model-title {
  flex: 1;
  min-width: 200px;
}

.model-title h3 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1.5rem;
}

.model-title .country-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #667eea;
  color: white;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-left: 0.5rem;
}

.model-meta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: #666;
}

.model-meta span {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.model-specs {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 6px;
}

.spec-item {
  text-align: center;
}

.spec-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #667eea;
}

.spec-label {
  font-size: 0.85rem;
  color: #666;
  margin-top: 0.25rem;
}

.model-description {
  color: #555;
  line-height: 1.6;
  margin: 1rem 0;
}

.model-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.model-links a {
  padding: 8px 16px;
  background: #667eea;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: background 0.2s ease;
}

.model-links a:hover {
  background: #5568d3;
}

.score-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 8px 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 20px;
  font-weight: 600;
  font-size: 1.1rem;
}

.score-badge.excellent {
  background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
}

.score-badge.good {
  background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
}

.score-badge.fair {
  background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
}

@media (max-width: 768px) {
  .model-header {
    flex-direction: column;
  }
  
  .model-specs {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

<nav class="models-nav">
  <a href="/sail">🏠 Home</a>
  <a href="/sail/spec">📋 Specification</a>
  <a href="/sail/countries">🌍 Countries</a>
</nav>

## Sovereign AI Models Directory

A comprehensive directory of sovereign AI language models, foundation models, and AI systems developed by countries around the world.

<div class="filter-bar">
  <select id="country-filter">
    <option value="">All Countries</option>
    <option value="Sweden">Sweden</option>
    <option value="Singapore">Singapore</option>
    <option value="Switzerland">Switzerland</option>
    <option value="France">France</option>
    <option value="Germany">Germany</option>
    <option value="Spain">Spain</option>
    <option value="Finland">Finland</option>
    <option value="Norway">Norway</option>
    <option value="Canada">Canada</option>
    <option value="United States">United States</option>
  </select>
  
  <select id="type-filter">
    <option value="">All Types</option>
    <option value="Language Model">Language Model</option>
    <option value="Foundation Model">Foundation Model</option>
    <option value="Multimodal">Multimodal</option>
  </select>
  
  <input type="text" id="search-input" placeholder="Search models...">
</div>

### Featured Models

<div class="model-card" data-country="Sweden" data-type="Language Model">
  <div class="model-header">
    <div class="model-title">
      <h3>GPT-SW3 <span class="country-badge">🇸🇪 Sweden</span></h3>
      <div class="model-meta">
        <span>📅 Released: 2023</span>
        <span>🏢 AI Sweden</span>
        <span>📊 SAIL: <span class="score-badge good">Gold (65 pts)</span></span>
      </div>
    </div>
  </div>
  
  <div class="model-description">
    GPT-SW3 is a large language model trained on Swedish text data, developed by AI Sweden in collaboration with RISE and the Wallenberg AI, Autonomous Systems and Software Program (WASP). It represents one of the first major sovereign AI initiatives in the Nordic region.
  </div>
  
  <div class="model-specs">
    <div class="spec-item">
      <div class="spec-value">40B</div>
      <div class="spec-label">Parameters</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Swedish</div>
      <div class="spec-label">Primary Language</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Open</div>
      <div class="spec-label">License</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Decoder</div>
      <div class="spec-label">Architecture</div>
    </div>
  </div>
  
  <div class="model-links">
    <a href="https://www.ai.se/en/project/gpt-sw3" target="_blank">Official Site</a>
    <a href="https://huggingface.co/AI-Sweden-Models" target="_blank">Hugging Face</a>
    <a href="/sail/countries#sweden">Country Profile</a>
  </div>
</div>

<div class="model-card" data-country="Singapore" data-type="Language Model">
  <div class="model-header">
    <div class="model-title">
      <h3>SEA-LION <span class="country-badge">🇸🇬 Singapore</span></h3>
      <div class="model-meta">
        <span>📅 Released: 2024</span>
        <span>🏢 AI Singapore</span>
        <span>📊 SAIL: <span class="score-badge excellent">Platinum (82 pts)</span></span>
      </div>
    </div>
  </div>
  
  <div class="model-description">
    SEA-LION (Southeast Asian Languages in One Network) is a family of large language models designed specifically for Southeast Asian languages. Developed by AI Singapore, it supports 11 languages including Malay, Indonesian, Thai, Vietnamese, and Tagalog.
  </div>
  
  <div class="model-specs">
    <div class="spec-item">
      <div class="spec-value">7B-128B</div>
      <div class="spec-label">Parameters</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">11 Languages</div>
      <div class="spec-label">Multilingual</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Apache 2.0</div>
      <div class="spec-label">License</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Decoder</div>
      <div class="spec-label">Architecture</div>
    </div>
  </div>
  
  <div class="model-links">
    <a href="https://sea-lion.ai/" target="_blank">Official Site</a>
    <a href="https://huggingface.co/aisingapore" target="_blank">Hugging Face</a>
    <a href="/sail/countries#singapore">Country Profile</a>
  </div>
</div>

<div class="model-card" data-country="Switzerland" data-type="Language Model">
  <div class="model-header">
    <div class="model-title">
      <h3>Apertus <span class="country-badge">🇨🇭 Switzerland</span></h3>
      <div class="model-meta">
        <span>📅 Released: 2025</span>
        <span>🏢 ETH Zurich</span>
        <span>📊 SAIL: <span class="score-badge excellent">Platinum (88 pts)</span></span>
      </div>
    </div>
  </div>
  
  <div class="model-description">
    Apertus is a fully open, transparent, multilingual language model developed by ETH Zurich. It represents a significant advancement in open-source sovereign AI, with complete transparency in training data, methodology, and deployment.
  </div>
  
  <div class="model-specs">
    <div class="spec-item">
      <div class="spec-value">70B</div>
      <div class="spec-label">Parameters</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Multilingual</div>
      <div class="spec-label">Languages</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Fully Open</div>
      <div class="spec-label">License</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Decoder</div>
      <div class="spec-label">Architecture</div>
    </div>
  </div>
  
  <div class="model-links">
    <a href="https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html" target="_blank">Official Announcement</a>
    <a href="https://publicai.co/" target="_blank">Public AI Inference Utility</a>
    <a href="/sail/countries#switzerland">Country Profile</a>
  </div>
</div>

<div class="model-card" data-country="France" data-type="Foundation Model">
  <div class="model-header">
    <div class="model-title">
      <h3>Mistral AI Models <span class="country-badge">🇫🇷 France</span></h3>
      <div class="model-meta">
        <span>📅 Released: 2023-2024</span>
        <span>🏢 Mistral AI</span>
        <span>📊 SAIL: <span class="score-badge good">Gold (68 pts)</span></span>
      </div>
    </div>
  </div>
  
  <div class="model-description">
    Mistral AI has developed a series of high-performance language models including Mistral 7B, Mixtral 8x7B, and Mistral Large. While a private company, Mistral AI represents significant French sovereign AI capabilities and has received substantial public support.
  </div>
  
  <div class="model-specs">
    <div class="spec-item">
      <div class="spec-value">7B-70B</div>
      <div class="spec-label">Parameters</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Multilingual</div>
      <div class="spec-label">Languages</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Mixed</div>
      <div class="spec-label">License</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Decoder</div>
      <div class="spec-label">Architecture</div>
    </div>
  </div>
  
  <div class="model-links">
    <a href="https://mistral.ai/" target="_blank">Official Site</a>
    <a href="https://huggingface.co/mistralai" target="_blank">Hugging Face</a>
    <a href="/sail/countries#france">Country Profile</a>
  </div>
</div>

<div class="model-card" data-country="United States" data-type="Foundation Model">
  <div class="model-header">
    <div class="model-title">
      <h3>AuroraGPT <span class="country-badge">🇺🇸 United States</span></h3>
      <div class="model-meta">
        <span>📅 Released: 2023</span>
        <span>🏢 Argonne National Laboratory</span>
        <span>📊 SAIL: <span class="score-badge excellent">Platinum (85 pts)</span></span>
      </div>
    </div>
  </div>
  
  <div class="model-description">
    AuroraGPT is a science-focused language model developed by Argonne National Laboratory. It's designed specifically for scientific applications and represents a significant public sector AI initiative in the United States.
  </div>
  
  <div class="model-specs">
    <div class="spec-item">
      <div class="spec-value">Science</div>
      <div class="spec-label">Domain Focus</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">English</div>
      <div class="spec-label">Primary Language</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Open</div>
      <div class="spec-label">License</div>
    </div>
    <div class="spec-item">
      <div class="spec-value">Research</div>
      <div class="spec-label">Use Case</div>
    </div>
  </div>
  
  <div class="model-links">
    <a href="https://auroragpt.anl.gov/" target="_blank">Official Site</a>
    <a href="/sail/countries#united-states">Country Profile</a>
  </div>
</div>

## Statistics

- **Total Models Tracked**: 50+
- **Countries Represented**: 25+
- **Platinum Certified**: 8
- **Gold Certified**: 15
- **Silver Certified**: 12
- **Open Source Models**: 35+
- **Multilingual Models**: 20+

## Contributing

Know of a sovereign AI model that should be included? [Submit information](mailto:info@publicai.network) or make a pull request to add it to this directory.

<script>
// Filter functionality
document.addEventListener('DOMContentLoaded', function() {
  const countryFilter = document.getElementById('country-filter');
  const typeFilter = document.getElementById('type-filter');
  const searchInput = document.getElementById('search-input');
  const modelCards = document.querySelectorAll('.model-card');
  
  function filterModels() {
    const countryValue = countryFilter.value.toLowerCase();
    const typeValue = typeFilter.value.toLowerCase();
    const searchValue = searchInput.value.toLowerCase();
    
    modelCards.forEach(card => {
      const country = card.dataset.country?.toLowerCase() || '';
      const type = card.dataset.type?.toLowerCase() || '';
      const text = card.textContent.toLowerCase();
      
      const matchesCountry = !countryValue || country.includes(countryValue);
      const matchesType = !typeValue || type.includes(typeValue);
      const matchesSearch = !searchValue || text.includes(searchValue);
      
      if (matchesCountry && matchesType && matchesSearch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
  
  countryFilter.addEventListener('change', filterModels);
  typeFilter.addEventListener('change', filterModels);
  searchInput.addEventListener('input', filterModels);
});
</script>
