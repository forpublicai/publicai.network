---
title: SAIL Countries
layout: page
description: Country rankings and detailed assessments of sovereign AI initiatives evaluated under the SAIL certification program.
permalink: /sail/countries/
---

<style>
.countries-nav {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  justify-content: center;
}

.countries-nav a {
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

.countries-nav a:hover {
  background: #667eea;
  color: white;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

.ranking-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.ranking-table th,
.ranking-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.ranking-table th {
  font-weight: 600;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.ranking-table tbody tr:hover {
  background: #f8f9fa;
}

.ranking-table tbody tr:last-child td {
  border-bottom: none;
}

.rank-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-weight: bold;
  font-size: 0.9rem;
}

.rank-badge.top-3 {
  background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
  color: #856404;
}

.rank-badge.top-10 {
  background: linear-gradient(135deg, #c0c0c0 0%, #e8e8e8 100%);
  color: #555;
}

.rank-badge.other {
  background: #f0f0f0;
  color: #666;
}

.score-cell {
  font-weight: 600;
  font-size: 1.1rem;
}

.score-cell.excellent {
  color: #28a745;
}

.score-cell.good {
  color: #17a2b8;
}

.score-cell.fair {
  color: #ffc107;
}

.score-cell.poor {
  color: #dc3545;
}

.dimension-scores {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.dimension-score {
  padding: 4px 8px;
  background: #f8f9fa;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
}

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

.country-overall-score {
  margin-left: auto;
  text-align: right;
}

.overall-score-value {
  font-size: 3rem;
  font-weight: bold;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.score-breakdown {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.breakdown-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  border-left: 4px solid #667eea;
}

.breakdown-label {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.breakdown-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #667eea;
}

.filter-controls {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
  align-items: center;
}

.filter-controls select,
.filter-controls input {
  padding: 10px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
}

.filter-controls input {
  flex: 1;
  min-width: 200px;
}

@media (max-width: 768px) {
  .ranking-table {
    font-size: 0.85rem;
  }
  
  .ranking-table th,
  .ranking-table td {
    padding: 0.75rem 0.5rem;
  }
  
  .dimension-scores {
    display: none;
  }
  
  .country-header {
    flex-direction: column;
    align-items: start;
  }
  
  .country-overall-score {
    margin-left: 0;
    margin-top: 1rem;
  }
}
</style>

<nav class="countries-nav">
  <a href="/sail">🏠 Home</a>
  <a href="/sail/spec">📋 Specification</a>
  <a href="/sail/models">🤖 Models</a>
</nav>

## SAIL Country Rankings

Comprehensive rankings and assessments of sovereign AI initiatives across countries worldwide. Rankings are based on the SAIL rating system evaluating Infrastructure, Governance, Innovation, Public Access, and Sustainability.

<div class="filter-controls">
  <select id="region-filter">
    <option value="">All Regions</option>
    <option value="Europe">Europe</option>
    <option value="Asia">Asia</option>
    <option value="North America">North America</option>
    <option value="South America">South America</option>
    <option value="Africa">Africa</option>
    <option value="Oceania">Oceania</option>
  </select>
  
  <input type="text" id="country-search" placeholder="Search countries...">
  
  <select id="sort-by">
    <option value="points-desc">Points (High to Low)</option>
    <option value="points-asc">Points (Low to High)</option>
    <option value="name-asc">Name (A-Z)</option>
  </select>
</div>

### Top Rankings

<table class="ranking-table">
  <thead>
    <tr>
      <th style="width: 60px;">Rank</th>
      <th>Country</th>
      <th style="width: 120px;">SAIL Points</th>
      <th style="width: 200px;">Key Layers</th>
      <th style="width: 120px;">Certification</th>
    </tr>
  </thead>
  <tbody>
    <tr data-country="Switzerland" data-region="Europe">
      <td><span class="rank-badge top-3">1</span></td>
      <td><strong>🇨🇭 Switzerland</strong></td>
      <td class="score-cell excellent">88 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 23</span>
          <span class="dimension-score">L2: 22</span>
          <span class="dimension-score">L3: 24</span>
          <span class="dimension-score">L4: 25</span>
          <span class="dimension-score">L5: 24</span>
          <span class="dimension-score">L6: 20</span>
          <span class="dimension-score">L7: 23</span>
        </div>
      </td>
      <td><span style="color: #666; font-weight: 600;">🏆 Platinum</span></td>
    </tr>
    <tr data-country="Singapore" data-region="Asia">
      <td><span class="rank-badge top-3">2</span></td>
      <td><strong>🇸🇬 Singapore</strong></td>
      <td class="score-cell excellent">82 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 22</span>
          <span class="dimension-score">L2: 21</span>
          <span class="dimension-score">L3: 23</span>
          <span class="dimension-score">L4: 24</span>
          <span class="dimension-score">L5: 23</span>
          <span class="dimension-score">L6: 18</span>
          <span class="dimension-score">L7: 22</span>
        </div>
      </td>
      <td><span style="color: #666; font-weight: 600;">🏆 Platinum</span></td>
    </tr>
    <tr data-country="Sweden" data-region="Europe">
      <td><span class="rank-badge top-3">3</span></td>
      <td><strong>🇸🇪 Sweden</strong></td>
      <td class="score-cell good">75 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 20</span>
          <span class="dimension-score">L2: 19</span>
          <span class="dimension-score">L3: 21</span>
          <span class="dimension-score">L4: 22</span>
          <span class="dimension-score">L5: 21</span>
          <span class="dimension-score">L6: 15</span>
          <span class="dimension-score">L7: 20</span>
        </div>
      </td>
      <td><span style="color: #b8860b; font-weight: 600;">🥇 Gold</span></td>
    </tr>
    <tr data-country="United States" data-region="North America">
      <td><span class="rank-badge top-10">4</span></td>
      <td><strong>🇺🇸 United States</strong></td>
      <td class="score-cell excellent">85 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 24</span>
          <span class="dimension-score">L2: 23</span>
          <span class="dimension-score">L3: 22</span>
          <span class="dimension-score">L4: 25</span>
          <span class="dimension-score">L5: 24</span>
          <span class="dimension-score">L6: 22</span>
          <span class="dimension-score">L7: 19</span>
        </div>
      </td>
      <td><span style="color: #666; font-weight: 600;">🏆 Platinum</span></td>
    </tr>
    <tr data-country="France" data-region="Europe">
      <td><span class="rank-badge top-10">5</span></td>
      <td><strong>🇫🇷 France</strong></td>
      <td class="score-cell good">68 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 19</span>
          <span class="dimension-score">L2: 18</span>
          <span class="dimension-score">L3: 20</span>
          <span class="dimension-score">L4: 21</span>
          <span class="dimension-score">L5: 20</span>
          <span class="dimension-score">L6: 14</span>
          <span class="dimension-score">L7: 19</span>
        </div>
      </td>
      <td><span style="color: #b8860b; font-weight: 600;">🥇 Gold</span></td>
    </tr>
    <tr data-country="Germany" data-region="Europe">
      <td><span class="rank-badge top-10">6</span></td>
      <td><strong>🇩🇪 Germany</strong></td>
      <td class="score-cell good">65 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 18</span>
          <span class="dimension-score">L2: 17</span>
          <span class="dimension-score">L3: 19</span>
          <span class="dimension-score">L4: 20</span>
          <span class="dimension-score">L5: 19</span>
          <span class="dimension-score">L6: 13</span>
          <span class="dimension-score">L7: 18</span>
        </div>
      </td>
      <td><span style="color: #b8860b; font-weight: 600;">🥇 Gold</span></td>
    </tr>
    <tr data-country="Canada" data-region="North America">
      <td><span class="rank-badge top-10">7</span></td>
      <td><strong>🇨🇦 Canada</strong></td>
      <td class="score-cell good">64 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 17</span>
          <span class="dimension-score">L2: 16</span>
          <span class="dimension-score">L3: 18</span>
          <span class="dimension-score">L4: 19</span>
          <span class="dimension-score">L5: 18</span>
          <span class="dimension-score">L6: 12</span>
          <span class="dimension-score">L7: 17</span>
        </div>
      </td>
      <td><span style="color: #b8860b; font-weight: 600;">🥇 Gold</span></td>
    </tr>
    <tr data-country="Spain" data-region="Europe">
      <td><span class="rank-badge top-10">8</span></td>
      <td><strong>🇪🇸 Spain</strong></td>
      <td class="score-cell good">62 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 16</span>
          <span class="dimension-score">L2: 15</span>
          <span class="dimension-score">L3: 17</span>
          <span class="dimension-score">L4: 18</span>
          <span class="dimension-score">L5: 17</span>
          <span class="dimension-score">L6: 11</span>
          <span class="dimension-score">L7: 16</span>
        </div>
      </td>
      <td><span style="color: #b8860b; font-weight: 600;">🥇 Gold</span></td>
    </tr>
    <tr data-country="Finland" data-region="Europe">
      <td><span class="rank-badge top-10">9</span></td>
      <td><strong>🇫🇮 Finland</strong></td>
      <td class="score-cell fair">58 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 15</span>
          <span class="dimension-score">L2: 14</span>
          <span class="dimension-score">L3: 16</span>
          <span class="dimension-score">L4: 17</span>
          <span class="dimension-score">L5: 16</span>
          <span class="dimension-score">L6: 10</span>
          <span class="dimension-score">L7: 15</span>
        </div>
      </td>
      <td><span style="color: #808080; font-weight: 600;">🥈 Silver</span></td>
    </tr>
    <tr data-country="Norway" data-region="Europe">
      <td><span class="rank-badge top-10">10</span></td>
      <td><strong>🇳🇴 Norway</strong></td>
      <td class="score-cell fair">57 pts</td>
      <td>
        <div class="dimension-scores">
          <span class="dimension-score">L1: 14</span>
          <span class="dimension-score">L2: 13</span>
          <span class="dimension-score">L3: 15</span>
          <span class="dimension-score">L4: 16</span>
          <span class="dimension-score">L5: 15</span>
          <span class="dimension-score">L6: 9</span>
          <span class="dimension-score">L7: 14</span>
        </div>
      </td>
      <td><span style="color: #808080; font-weight: 600;">🥈 Silver</span></td>
    </tr>
  </tbody>
</table>

## Detailed Country Profiles

### Switzerland {#switzerland}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇨🇭</div>
    <div class="country-info">
      <h3>Switzerland</h3>
      <p style="color: #666; margin: 0;">Leading sovereign AI initiative with strong emphasis on transparency and open source</p>
    </div>
    <div class="country-overall-score">
      <div class="overall-score-value">88</div>
      <div style="color: #666; font-weight: 600;">🏆 Platinum</div>
    </div>
  </div>
  
  <div class="score-breakdown">
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 1: Application & Service</div>
      <div class="breakdown-value">23</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 2: Orchestration</div>
      <div class="breakdown-value">22</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 3: Data Sovereignty</div>
      <div class="breakdown-value">24</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 4: Model Sovereignty</div>
      <div class="breakdown-value">25</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 5: Training & Post-Training</div>
      <div class="breakdown-value">24</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 6: Compute & Infrastructure</div>
      <div class="breakdown-value">20</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 7: Legal & Governance</div>
      <div class="breakdown-value">23</div>
    </div>
  </div>
  
  <h4>Key Initiatives</h4>
  <ul>
    <li><strong>Apertus</strong> - Fully open, transparent multilingual language model by ETH Zurich</li>
    <li><strong>Swiss AI Weeks</strong> - Public AI infrastructure and community engagement</li>
    <li><strong>Public AI Inference Utility</strong> - Global access to Swiss AI models</li>
  </ul>
  
  <h4>Strengths</h4>
  <ul>
    <li>World-class research institutions (ETH Zurich, EPFL)</li>
    <li>Strong commitment to open source and transparency</li>
    <li>Excellent public-private collaboration</li>
    <li>High-quality technical infrastructure</li>
  </ul>
  
  <p><a href="/sail/models#switzerland">View Swiss AI Models →</a></p>
</div>

### Singapore {#singapore}

<div class="country-card">
  <div class="country-header">
    <div class="country-flag">🇸🇬</div>
    <div class="country-info">
      <h3>Singapore</h3>
      <p style="color: #666; margin: 0;">Regional leader in multilingual AI for Southeast Asia</p>
    </div>
    <div class="country-overall-score">
      <div class="overall-score-value">82</div>
      <div style="color: #666; font-weight: 600;">🏆 Platinum</div>
    </div>
  </div>
  
  <div class="score-breakdown">
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 1: Application & Service</div>
      <div class="breakdown-value">22</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 2: Orchestration</div>
      <div class="breakdown-value">21</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 3: Data Sovereignty</div>
      <div class="breakdown-value">23</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 4: Model Sovereignty</div>
      <div class="breakdown-value">24</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 5: Training & Post-Training</div>
      <div class="breakdown-value">23</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 6: Compute & Infrastructure</div>
      <div class="breakdown-value">18</div>
    </div>
    <div class="breakdown-item">
      <div class="breakdown-label">Layer 7: Legal & Governance</div>
      <div class="breakdown-value">22</div>
    </div>
  </div>
  
  <h4>Key Initiatives</h4>
  <ul>
    <li><strong>SEA-LION</strong> - Multilingual language models for 11 Southeast Asian languages</li>
    <li><strong>AI Singapore</strong> - National AI research and development program</li>
    <li><strong>National AI Strategy</strong> - Comprehensive government AI policy framework</li>
  </ul>
  
  <h4>Strengths</h4>
  <ul>
    <li>Strong focus on multilingual AI for regional languages</li>
    <li>Excellent coordination between government, research, and industry</li>
    <li>High-quality technical infrastructure and talent</li>
    <li>Clear strategic vision for sovereign AI</li>
  </ul>
  
  <p><a href="/sail/models#singapore">View Singapore AI Models →</a></p>
</div>

## Methodology

Country rankings are based on comprehensive evaluation using the [SAIL Specification](/sail/spec). Points are awarded across seven layers based on demonstrated capacity, legal robustness, and exit readiness. Certification levels are determined by total points earned (out of 175 possible).

**Last Updated**: September 2025  
**Next Update**: December 2025

<script>
// Filter and sort functionality
document.addEventListener('DOMContentLoaded', function() {
  const regionFilter = document.getElementById('region-filter');
  const countrySearch = document.getElementById('country-search');
  const sortBy = document.getElementById('sort-by');
  const tableBody = document.querySelector('.ranking-table tbody');
  const rows = Array.from(tableBody.querySelectorAll('tr'));
  
  function filterAndSort() {
    const regionValue = regionFilter.value.toLowerCase();
    const searchValue = countrySearch.value.toLowerCase();
    
    // Filter
    let filtered = rows.filter(row => {
      const country = row.dataset.country?.toLowerCase() || '';
      const region = row.dataset.region?.toLowerCase() || '';
      const text = row.textContent.toLowerCase();
      
      const matchesRegion = !regionValue || region.includes(regionValue);
      const matchesSearch = !searchValue || text.includes(searchValue);
      
      return matchesRegion && matchesSearch;
    });
    
    // Sort
    const sortValue = sortBy.value;
    filtered.sort((a, b) => {
      if (sortValue === 'points-desc') {
        const pointsA = parseFloat(a.querySelector('.score-cell')?.textContent?.replace(' pts', '') || 0);
        const pointsB = parseFloat(b.querySelector('.score-cell')?.textContent?.replace(' pts', '') || 0);
        return pointsB - pointsA;
      } else if (sortValue === 'points-asc') {
        const pointsA = parseFloat(a.querySelector('.score-cell')?.textContent?.replace(' pts', '') || 0);
        const pointsB = parseFloat(b.querySelector('.score-cell')?.textContent?.replace(' pts', '') || 0);
        return pointsA - pointsB;
      } else if (sortValue === 'name-asc') {
        const nameA = a.querySelector('strong')?.textContent || '';
        const nameB = b.querySelector('strong')?.textContent || '';
        return nameA.localeCompare(nameB);
      }
      return 0;
    });
    
    // Update ranks and reorder
    filtered.forEach((row, index) => {
      const rankBadge = row.querySelector('.rank-badge');
      if (rankBadge) {
        rankBadge.textContent = index + 1;
        rankBadge.className = 'rank-badge';
        if (index < 3) {
          rankBadge.classList.add('top-3');
        } else if (index < 10) {
          rankBadge.classList.add('top-10');
        } else {
          rankBadge.classList.add('other');
        }
      }
      tableBody.appendChild(row);
    });
  }
  
  regionFilter.addEventListener('change', filterAndSort);
  countrySearch.addEventListener('input', filterAndSort);
  sortBy.addEventListener('change', filterAndSort);
});
</script>
