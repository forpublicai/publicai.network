---
layout: page
title: Contributors
nav_title: Contributors
permalink: /contributors/
---

The **Public AI Network** brings together a diverse coalition of researchers, practitioners, policymakers, and organizations, all advancing public AI. Our community spans academia, civil society, government, and industry, united by a shared vision of AI that serves the public good. [Join us](#join-the-movement)!


<style>
/* Card Catalog Styling */
.catalog {
  display: flex;
  gap: 30px;
  margin: 2em 0;
  padding: 1em;
  position: relative;
  flex-wrap: wrap;
  justify-content: center;
}

.catalog-column {
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
  flex: 1;
  min-width: 230px;
  max-width: 250px;
}

.card {
  width: 225px;
  height: 147px;  /* 60% of width for 3x5 proportion */
  background: linear-gradient(180deg, #f4e8d0 0%, #e8dcc0 100%);
  border: 1px solid #c4b5a0;
  border-bottom: 1px solid #a89880;
  position: relative;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  overflow: hidden;
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-12px);  /* Just move up slightly */
}

/* Stack effect - each card indented more and showing only top portion */
.card:nth-child(1) { margin-left: 0px; }
.card:nth-child(2) { margin-left: 1px; margin-top: -120px; }
.card:nth-child(3) { margin-left: 2px; margin-top: -120px; }
.card:nth-child(4) { margin-left: 3px; margin-top: -120px; }
.card:nth-child(5) { margin-left: 4px; margin-top: -120px; }
.card:nth-child(6) { margin-left: 5px; margin-top: -120px; }
.card:nth-child(7) { margin-left: 6px; margin-top: -120px; }
.card:nth-child(8) { margin-left: 7px; margin-top: -120px; }
.card:nth-child(9) { margin-left: 8px; margin-top: -120px; }
.card:nth-child(10) { margin-left: 9px; margin-top: -120px; }
.card:nth-child(n+11) { margin-left: 10px; margin-top: -120px; }

/* Card drawer front - covers the last card */
.drawer-front {
  width: 245px;
  height: 120px;
  background: linear-gradient(180deg, #e8c8b8 0%, #d0b8a8 100%);
  border: 2px solid #a89880;
  border-radius: 2px;
  position: relative;
  margin-top: -120px;
  margin-left: -7px;  
  box-shadow: 0 3px 8px rgba(0,0,0,0.3);
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.drawer-label {
  background: #f4d8c0;
  border: 1px solid #a89880;
  padding: 4px 12px;
  font-size: 16px;
  font-family: 'Courier New', monospace;
  color: #605040;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);
}

/* Card tab (always visible) */
.tab {
  padding: 2px 10px;
  font-size: 17px;
  font-weight: 600;
  color: #494080;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 28px;
  font-family: 'Courier New', monospace;
}

/* Content (hidden, used for popup) */
.content {
  display: none;
}

/* Popup card (separate element) */
.popup {
  display: none;
  position: fixed;
  width: 300px;
  background: #f4e8d0;
  background-image: repeating-linear-gradient(
    180deg,
    transparent,
    transparent 24px,
    #d4c4a8 24px,
    #d4c4a8 25px
  );
  border: 1px solid #a89880;
  border-radius: 2px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  z-index: 10000;
  padding: 20px 15px 15px 15px;
  pointer-events: auto;
  font-family: 'Georgia', serif;
}

/* Style adjustments for content inside popup */
.popup .name {
  font-weight: 600;
  font-size: 15px;
  margin-bottom: 4px;
  color: #3a2f20;
  font-family: 'Courier New', monospace;
}

.popup .aff {
  font-size: 13px;
  color: #5a4a3a;
  margin-bottom: 8px;
  font-style: italic;
}

.popup .details {
  font-size: 13px;
  color: #4a3f30;
  line-height: 24px;  /* Match the line spacing */
}

.popup .details b {
  color: #3a2f20;
  display: block;
  margin-top: 6px;
}

.popup .details a {
  color: #6a5040;
  text-decoration: underline;
}

.popup .details a:hover {
  color: #4a3020;
}

.popup .joined {
  position: absolute;
  bottom: 2px;
  right: 8px;
  font-size: 11px;
  color: #8a7a6a;
  font-style: italic;
}

/* Avatar styles */
.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  float: left;
  margin-right: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 14px;
}

/* Avatar colors */
.c1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.c2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.c3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.c4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
.c5 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
.c6 { background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); }

.name {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 4px;
  color: #2c3e50;
}

.aff {
  font-size: 11px;
  color: #666;
  margin-bottom: 8px;
  font-style: italic;
}

.details {
  font-size: 11px;
  color: #555;
  line-height: 1.4;
}

.details b {
  color: #333;
  display: block;
  margin-top: 6px;
}

.details a {
  color: #4a90e2;
  text-decoration: none;
}

.details a:hover {
  text-decoration: underline;
}

.joined {
  position: absolute;
  bottom: 8px;
  right: 8px;
  font-size: 9px;
  color: #999;
}

/* Enhanced Organization grid styling */
.org-grid {
  display: flex;
  flex-direction: column;
  margin: 2em auto;
  padding: 20px 0;
  max-width: 900px;
}

.org-category {
  margin-bottom: 2em;
}

.org-category h4 {
  color: #605040;
  font-family: 'Georgia', serif;
  margin-bottom: 1em;
  padding-bottom: 0.5em;
  border-bottom: 2px solid #e8dcc0;
}

.org-row {
  display: flex;
  justify-content: center;
  margin: 10px 0;
  flex-wrap: wrap;
  gap: 15px;
}

.org-row.offset {
  margin-left: 50px;
}

.org-logo {
  width: 80px;
  height: 80px;
  margin: 0 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 8px;
  transition: all 0.3s ease;
  cursor: pointer;
  font-size: 24px;
  font-weight: bold;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.org-logo:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.org-logo img {
  max-width: 70px;
  max-height: 70px;
  object-fit: contain;
}

/* Search/Filter Box */
.search-box {
  margin: 2em 0;
  text-align: center;
}

.search-input {
  width: 300px;
  padding: 10px 15px;
  border: 2px solid #e8dcc0;
  border-radius: 25px;
  font-size: 14px;
  font-family: 'Georgia', serif;
  background: #faf8f4;
}

.search-input:focus {
  outline: none;
  border-color: #c4b5a0;
  background: white;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .stats-bar {
    gap: 1em;
  }
  
  .stat {
    min-width: 45%;
    margin-bottom: 1em;
  }
  
  .catalog {
    flex-direction: column;
    align-items: center;
  }
  
  .card {
    width: 220px;
    height: 147px;
  }
  
  .org-logo {
    width: 60px;
    height: 60px;
    margin: 0 10px;
    font-size: 18px;
  }
  
  .search-input {
    width: 90%;
  }
}
</style>

<!-- Simple search : see function at end -->
<div class="search-box">
  <input type="text" class="search-input" id="peopleSearch" placeholder="Search by name, project, or affiliation">
</div>

## Contributors

*Contributors to our collective work, from publications and advocacy to technical projects and events.  This list is under construction - add yourself!*

<div class="catalog">
  
  <!-- A-D -->
  <div class="catalog-column">


<div class="card">
  <div class="tab">Albert Cañigueral</div>
  <div class="content">
    <div class="avatar c1">AC</div>
    <div class="name">Albert Cañigueral</div>
    <div class="aff">Barcelona Supercomputing Center (BSC)</div>
    <div class="details">
    <b>Focus:</b> Airbus for AI
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Alex Krasodomski</div>
      <div class="content">
        <div class="avatar c5">AK</div>
        <div class="name">Alex Krasodomski</div>
        <div class="aff">Chatham House, UK</div>
        <div class="details">
          Community Organizer<br/>
          <b>Focus:</b> Digital public infrastructure, partnerships
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>

    <div class="card">
  <div class="tab">Alexander Schneider</div>
  <div class="content">
    <div class="avatar c3">AS</div>
    <div class="name">Alexander Schneider</div>
    <div class="aff">Colorado, USA</div>
    <div class="details">
      <b>Focus:</b> State capacity + AI alignment
    </div>
    <div class="joined">2025</div>
  </div>
  </div>


    <div class="card">
      <div class="tab">Alek Tarkowski</div>
      <div class="content">
        <div class="avatar c6">AT</div>
        <div class="name">Alek Tarkowski</div>
        <div class="aff">Open Future, EU</div>
        <div class="details">
          Community Organizer<br/>
          <b>Focus:</b>
          • Digital commons advocacy, open licensing, data governance 
        </div>
        <div class="joined">2023</div>
      </div>
    </div>

 <div class="card">
  <div class="tab">Antoine McGrath</div>
  <div class="content">
    <div class="avatar c3">AM</div>
    <div class="name">Antoine McGrath</div>
    <div class="aff">Archive.org, SF</div>
    <div class="details">
      <b>Focus:</b> Open data, <a href="https://EOTArchive.org">EOTArchive</a><br/>
      <b>Vision:</b> Robust open base LLM for global public use
    </div>
    <div class="joined">2024</div>
  </div>
 </div>

<div class="card">
  <div class="tab">Avani Wildani</div>
  <div class="content">
    <div class="avatar c3">AW</div>
    <div class="name">Avani Wildani</div>
    <div class="aff">Cloudflare, SF</div>
    <div class="details">
      <b>Focus:</b> Data pipelines, distributed systems
    </div>
    <div class="joined">2023</div>
  </div>
</div>

    <div class="card">
      <div class="tab">B Cavello</div>
      <div class="content">
        <div class="avatar c2">BC</div>
        <div class="name">B Cavello</div>
        <div class="aff">Aspen Digital, DC</div>
        <div class="details">
          Community Organizer 
          <b>Focus:</b>
          Benchmarks lead, Policy strategy, AI governance, public interest tech
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>

    <div class="card">
     <div class="tab">Beatrice Murch</div>
     <div class="content">
        <div class="avatar c4">BM</div>
        <div class="name">Beatrice Murch</div>
        <div class="aff">Internet Archive Europe</div>
        <div class="details">
        <b>Focus:</b> Cultural heritage preservation, libraries
        </div>
        <div class="joined">2025</div>
     </div>
    </div>

   <div class="card">
  <div class="tab">Benjamin de la Peña</div>
  <div class="content">
    <div class="avatar c5">BP</div>
    <div class="name">Benjamin de la Peña</div>
    <div class="aff">Shared Use Mobility Center, Chicago</div>
    <div class="details">
      <b>Focus:</b> Transportation, informality in cities, systems change<br/>
      <b>Vision:</b> Assistive Intelligence, not Artificial Intelligence
    </div>
    <div class="joined">2024</div>
  </div>
  </div>

  <div class="card">
  <div class="tab">Bettina Warburg</div>
  <div class="content">
    <div class="avatar c4">BW</div>
    <div class="name">Bettina Warburg</div>
    <div class="aff">📚</div>
    <div class="details">
      <b>Focus:</b> Web3, strategic innovation, knowledge integrity
    </div>
    <div class="joined">2024</div>
  </div>
  </div>

    <div class="card">
     <div class="tab">Bobbi Rakova</div>
     <div class="content">
        <div class="avatar c5">BR</div>
        <div class="name">Bobbi Rakova</div>
        <div class="aff">Responsible AI, SF</div>
        <div class="details">
        <b>Focus:</b> Responsible AI, mechanism design
        </div>
        <div class="joined">2024</div>
     </div>
    </div>

    <div class="card">
      <div class="tab">Brandon Jackson</div>
      <div class="content">
        <div class="avatar c1">BJ</div>
        <div class="name">Brandon Jackson</div>
        <div class="aff"> 🎨 </div>
        <div class="details">
          <b>Focus:</b>
          Whitepaper lead, product design, creative applications of AI
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>


    <div class="card">
     <div class="tab">Catherine Geanuracos</div>
     <div class="content">
        <div class="avatar c1">CG</div>
        <div class="name">Catherine Geanuracos</div>
        <div class="aff">Civic Tech, LA</div>
        <div class="details">
          <b>Focus:</b> Civic technology, speculative fiction
        </div>
        <div class="joined">2024</div>
     </div>
    </div>

  <div class="card">
  <div class="tab">Chad Kohalyk</div>
  <div class="content">
    <div class="avatar c6">CK</div>
    <div class="name">Chad Kohalyk</div>
    <div class="aff">Vancouver, BC</div>
    <div class="details">
      <b>Focus:</b> Future of computing, standards, governance<br/>
      <b>Vision:</b> AI as DPI independent of corp/state interests
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Dave Buckley</div>
  <div class="content">
    <div class="avatar c1">DB</div>
    <div class="name">Dave Buckley</div>
    <div class="aff">OpenMined, UK</div>
    <div class="details">
      <b>Focus:</b> Data infrastructure, governed access to protected data<br/>
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">David Pham</div>
  <div class="content">
    <div class="avatar c6">DP</div>
    <div class="name">David Pham</div>
    <div class="aff">Simon Fraser University, Canada</div>
    <div class="details">
      <b>Focus:</b> Data economics, safety
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Diane Coyle</div>
      <div class="content">
        <div class="avatar c6">DC</div>
        <div class="name">Diane Coyle</div>
        <div class="aff">University of Cambridge, UK</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-coyle">Public policy for tech</a> (<a href="https://docs.google.com/document/d/1n3DcShalIqN0drYMJbbZBANNWbKznAtiT5n3jtsz0tM">summary</a>)<br>
          <b>Focus:</b> Economics, digital policy
        </div>
        <div class="joined">2024</div>
      </div>
    </div>


    <div class="drawer-front">
      <div class="drawer-label">MEMBERS A-D</div>
    </div>
  </div>

<!-- F-L -->
  <div class="catalog-column">

<div class="card">
  <div class="tab">Don Means</div>
  <div class="content">
    <div class="avatar c5">DM</div>
    <div class="name">Don Means</div>
    <div class="aff">Gigabit Libraries Network, US</div>
    <div class="details">
      <b>Focus:</b> Libraries, digital infrastructure
    </div>
    <div class="joined">2024</div>
  </div>
</div>

 <div class="card">
      <div class="tab">Eleanor Tursman</div>
      <div class="content">
        <div class="avatar c3">ET</div>
        <div class="name">Eleanor Tursman</div>
        <div class="aff">The Aspen Institute, US</div>
        <div class="details">
          <b>Focus:</b>
          Program development, tech policy, digital equity
        </div>
        <div class="joined">2024</div>
      </div>
    </div>

 <div class="card">
  <div class="tab">Ella Shoup</div>
  <div class="content">
    <div class="avatar c2">ES</div>
    <div class="name">Ella Shoup</div>
    <div class="aff">London, UK</div>
    <div class="details">
      <b>Focus:</b> AI ethics, policy, geopolitics
    </div>
    <div class="joined">2024</div>
  </div>
 </div>

<div class="card">
  <div class="tab">Felix Sieker</div>
  <div class="content">
    <div class="avatar c3">FS</div>
    <div class="name">Felix Sieker</div>
    <div class="aff">Bertelsmann Foundation, Germany</div>
    <div class="details">
      <b>Focus:</b> Common good, social policy, innovation strategy
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Flynn Devine</div>
      <div class="content">
        <div class="avatar c2">FD</div>
        <div class="name">Flynn Devine</div>
        <div class="aff">Boundary Object Studio, US</div>
        <div class="details">
          <b>Focus:</b>
          Research, sociotechnical systems, participatory design
        </div>
        <div class="joined">2023</div>
      </div>
    </div>
    
    <div class="card">
      <div class="tab">Gideon Lichfield</div>
      <div class="content">
        <div class="avatar c5">GL</div>
        <div class="name">Gideon Lichfield</div>
        <div class="aff">Journalist</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/3UVfaegU2vk">Past and future narratives for tech</a> (<a href="https://docs.google.com/document/d/1vWZQPKtWbtQM0AfJCjsSxNSZsZiSVBJ0f-V146nJ5DM">summary</a>)<br>
          • June 3, 2025<br/>
          <b>Focus:</b> Tech journalism, narrative building
        </div>
        <div class="joined">2024</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Jacob Taylor</div>
  <div class="content">
    <div class="avatar c1">JT</div>
    <div class="name">Jacob Taylor</div>
    <div class="aff">Brookings Institution, US</div>
    <div class="details">
      <b>Focus:</b> Collective intelligence, sustainable development
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Jake Hirsch-Allen</div>
  <div class="content">
    <div class="avatar c3">JH</div>
    <div class="name">Jake Hirsch-Allen</div>
    <div class="aff">The Dais, Canada</div>
    <div class="details">
    <b>Focus:</b> Canadian policy, partnerships
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Jean Garcia Periche</div>
  <div class="content">
    <div class="avatar c2">JG</div>
    <div class="name">Jean Garcia Periche</div>
    <div class="aff">Public Intelligence AI</div>
    <div class="details">
      <b>Focus:</b> DPI, agentic government, LATAM AI ecosystems<br/>
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">Joseph Low</div>
  <div class="content">
    <div class="avatar c4">JL</div>
    <div class="name">Joseph Low</div>
    <div class="aff">Product Design, Singapore</div>
    <div class="details">
      <b>Focus:</b> Product design
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Joshua Hewson</div>
  <div class="content">
    <div class="avatar c4">JH</div>
    <div class="name">Joshua Hewson</div>
    <div class="aff">Brown, US</div>
    <div class="details">
      <b>Focus:</b> Alignment, cognitive enhancement, neuroscience
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Joshua Tan</div>
      <div class="content">
        <div class="avatar c1">JT</div>
        <div class="name">Joshua Tan</div>
        <div class="aff">Oxford, Metagov</div>
        <div class="details">
          Community Organizer<br/>
          <b>Focus:</b> Computational governance, collective intelligence <br/>
          <b>Projects:</b> Airbus for AI, Inference Utility, Public AI for Libraries
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Katherine Elkins</div>
  <div class="content">
    <div class="avatar c2">KE</div>
    <div class="name">Katherine Elkins</div>
    <div class="aff">Interdisciplinary AI, US</div>
    <div class="details">
      <b>Focus:</b> Storytelling, interdisciplinary AI
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Katherine Gorman</div>
  <div class="content">
    <div class="avatar c4">KG</div>
    <div class="name">Katherine Gorman</div>
    <div class="aff">🛜, US</div>
    <div class="details">
      <b>Focus:</b> Communications, alignment
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">Larry Williams</div>
  <div class="content">
    <div class="avatar c2">LW</div>
    <div class="name">Larry Williams</div>
    <div class="aff">UnionBase, DC</div>
    <div class="details">
      <b>Focus:</b> Labor and economics
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Lorelei Kelly</div>
  <div class="content">
    <div class="avatar c1">LK</div>
    <div class="name">Lorelei Kelly</div>
    <div class="aff">Smart Congress, DC</div>
    <div class="details">
      <b>Focus:</b> Democracy, government modernization
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Luca Cominassi</div>
  <div class="content">
    <div class="avatar c5">LC</div>
    <div class="name">Luca Cominassi</div>
    <div class="aff">Parti Collective, Italy</div>
    <div class="details">
    <b>Focus:</b> Airbus for AI
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="drawer-front">
      <div class="drawer-label">MEMBERS E-L</div>
    </div>
 </div>


<!-- M-Z -->
  <div class="catalog-column">

    <div class="card">
      <div class="tab">Magnus Sahlgren</div>
      <div class="content">
        <div class="avatar c5">MS</div>
        <div class="name">Magnus Sahlgren</div>
        <div class="aff">AI Sweden</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://www.youtube.com/watch?v=0ak4vcFCjSA">GPT-SW3</a> (<a href="https://docs.google.com/document/d/1zp2mVGcPRIUPe_h4GqT12-tyCkVO-RTj3LSugiPv3ek/edit?tab=t.0">summary</a>)<br>
          • September 24, 2024<br/>
          <b>Focus:</b> Swedish language model development
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Max Gahntz</div>
  <div class="content">
    <div class="avatar c4">MG</div>
    <div class="name">Max Gahntz</div>
    <div class="aff">Mozilla</div>
    <div class="details">
      <b>Focus:</b> AI policy
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">Melissa Regan</div>
  <div class="content">
    <div class="avatar c3">MR</div>
    <div class="name">Melissa Regan</div>
    <div class="aff">Writer, SF</div>
    <div class="details">
      <b>Focus:</b> Speculative fiction
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Meredith Whipple</div>
  <div class="content">
    <div class="avatar c2">MW</div>
    <div class="name">Meredith Whipple</div>
    <div class="aff">Public Knowledge, US</div>
    <div class="details">
    <b>Focus:</b> Policy, civic technology
    </div>
    <div class="joined">2024</div>
  </div>
</div>

<div class="card">
  <div class="tab">Mohsin Y. K. Yousufi</div>
  <div class="content">
    <div class="avatar c2">MY</div>
    <div class="name">Mohsin Y. K. Yousufi</div>
    <div class="aff">Georgia Tech</div>
    <div class="details">
    <b>Focus:</b> Public AI for Libraries, Civic Tech
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">Natalie Buda Smith</div>
  <div class="content">
    <div class="avatar c6">NB</div>
    <div class="name">Natalie Buda Smith</div>
    <div class="aff">Library of Congress, US</div>
    <div class="details">
    <b>Focus:</b> Libraries, government, humans in the loop. (<a href="https://aicenterforgovernment.org/2025/07/03/ai-spotlight-pairing-human-and-artificial-intelligence-at-the-library-of-congress/">interview</a>)
    </div>
    <div class="joined">2024</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Nick Garcia</div>
      <div class="content">
        <div class="avatar c3">NG</div>
        <div class="name">Nick Garcia</div>
        <div class="aff">Public Knowledge, DC</div>
        <div class="details">
          Community Organizer<br/>
          <b>Focus:</b> 
          Policy advocacy, community governance digital rights, libraries <br/>
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Nick Vincent</div>
      <div class="content">
        <div class="avatar c5">NV</div>
        <div class="name">Nick Vincent</div>
        <div class="aff">Simon Fraser University, Canada</div>
        <div class="details">
          <b>Focus:</b> Data contribution systems, platform cooperatives, labor, data flywheel 
        </div>
        <div class="joined">2024</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Nicolas Flores-Herr</div>
  <div class="content">
    <div class="avatar c5">NF</div>
    <div class="name">Nicolas Flores-Herr</div>
    <div class="aff">Fraunhofer, Germany</div>
    <div class="details">
      <b>Focus:</b> Conversational AI, training, neuroscience
    </div>
    <div class="joined">2025</div>
  </div>
</div>

<div class="card">
  <div class="tab">Oleg Lavrovsky</div>
  <div class="content">
    <div class="avatar c4">OL</div>
    <div class="name">Oleg Lavrovsky</div>
    <div class="aff">Datalets, Switzerland</div>
    <div class="details">
      <b>Focus:</b> Open source/data/hardware/AI/collaboration<br/>
      <b>Project:</b> Swiss {ai} Weeks, Apertus
    </div>
    <div class="joined">2025</div>
  </div>
</div>

  <div class="card">
      <div class="tab">Philip Tomei</div>
      <div class="content">
        <div class="avatar c5">PT</div>
        <div class="name">Philiip Tomei</div>
        <div class="aff">AI Objectives Institute, UK</div>
        <div class="details">
          <b>Focus:</b> Art and AI, labor and societal impacts <br/>
        </div>
        <div class="joined">2024</div>
      </div>
    </div>

  <div class="card">
  <div class="tab">Robert Gehorsam</div>
  <div class="content">
    <div class="avatar c4">RG</div>
    <div class="name">Robert Gehorsam</div>
    <div class="aff">LA/NYC</div>
    <div class="details">
      <b>Focus:</b> Democracy innovation, security, climate
    </div>
    <div class="joined">2025</div>
  </div>
  </div>

    <div class="card">
      <div class="tab">Sam Klein</div>
      <div class="content">
        <div class="avatar c4">SK</div>
        <div class="name">Sam Klein</div>
        <div class="aff">Harvard Berkman Klein Center, Boston</div>
        <div class="details">
          Community Organizer
          <b>Focus:</b> Decentralized infrastructure, universal library, <br/> Wiki AI 
        </div>
        <div class="joined">Founding Member</div>
      </div>
    </div>

  <div class="card">
   <div class="tab">Sarah Mackenzie</div>
   <div class="content">
    <div class="avatar c1">SM</div>
    <div class="name">Sarah Mackenzie</div>
    <div class="aff">Montreal</div>
    <div class="details">
      <b>Focus:</b> Arts technologies, AI ethics, data justice<br/>
      <b>Project:</b> <a href="https://sporobole.org/en/project/artia-project/">ARTIA Project</a>
    </div>
    <div class="joined">2025</div>
  </div>
  </div> 

    <div class="card">
      <div class="tab">Sarah Schwettmann</div>
      <div class="content">
        <div class="avatar c4">SS</div>
        <div class="name">Sarah Schwettmann</div>
        <div class="aff">Transluce, MIT</div>
        <div class="details">
          <b>Focus:</b> Interpretability, third-party audits
        </div>
        <div class="joined">2024</div>
      </div>
    </div>
    
    <div class="card">
  <div class="tab">Thomas Renkert</div>
  <div class="content">
    <div class="avatar c5">TR</div>
    <div class="name">Thomas Renkert</div>
    <div class="aff">PH Heidelberg, Germany</div>
    <div class="details">
      <b>Focus:</b> AI in education, AI sovereignty, educational equity<br/>
      <b>Project:</b> <a href="https://www.uni-heidelberg.de/en/research/research-profile/fields-of-focus/field-of-focus-iii/research-focus-areas/heidelberg-center-for-digital-humanities-hcdh">ParzivAI</a> (historic languages LLM)
    </div>
    <div class="joined">2024</div>
  </div>
  </div>

    <div class="drawer-front">
      <div class="drawer-label">MEMBERS M-Z</div>
    </div>
  </div>

</div>

<br/>

## Speakers &amp; Collaborators

*Speakers, collaborators, and sources of inspiration. Check out their work!*

<div class="catalog">

  <!-- A-I -->
  <div class="catalog-column">
    
    <div class="card">
      <div class="tab">Aza Raskin</div>
      <div class="content">
        <div class="avatar c2">AR</div>
        <div class="name">Aza Raskin</div>
        <div class="aff">Center for Humane Technology, Earth Species Project, SF</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://www.youtube.com/watch?v=gmtHT2zt-4g">The AI Dilemma</a> (<a href="https://docs.google.com/document/d/1ATwQxTheRL7QOFGSbVO2Di2TCdbEr-GlVKBj3ldAR6U">summary</a>)<br>
          • October 8, 2024<br/>
          <b>Focus:</b> Humane AI, attention economy
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Beth Noveck</div>
  <div class="content">
    <div class="avatar c2">BN</div>
    <div class="name">Beth Noveck</div>
    <div class="aff">GovLab, NEU, Chief AI Strategist for NJ</div>
    <div class="details">
      <b>Speaker:</b> Government innovation, AI strategy (LOC event)
    </div>
    <div class="joined">Multiple events</div>
  </div>
</div>

    <div class="card">
      <div class="tab">Bruce Schneier</div>
      <div class="content">
        <div class="avatar c5">BS</div>
        <div class="name">Bruce Schneier</div>
        <div class="aff">Harvard, Boston</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-schneier">Public options for AI</a> (<a href="https://docs.google.com/document/d/1j0foQVDe0ELYJCrZxOM7ueSiXFVvWr84Hycl2ZdeWFE/edit">summary</a>)<br>
          • January 9, 2024<br/>
          <b>Focus:</b> Security, public interest technology
        </div>
        <div class="joined">Season 1</div>
      </div>
    </div>

<div class="card">
  <div class="tab">Dan Zhao</div>
  <div class="content">
    <div class="avatar c1">DZ</div>
    <div class="name">Dan Zhao</div>
    <div class="aff">MIT, Boston</div>
    <div class="details">
      <b>Seminar:</b>
      • <a href="https://www.youtube.com/watch?v=wZ23B9ohMvQ">Agent Strategy</a> (<a href="https://docs.google.com/document/d/1eVaVJVkwHw3HIKePBsfTVd_q6h4mawnsnXXql6NHqc8/edit?tab=t.0#heading=h.2uwjflbphywn">notes</a>) <br/>
      • August 21, 2025<br/>
      <b>Focus:</b> Multimodal agents, benchmarks
    </div>
    <div class="joined">Season 3</div>
  </div>
</div>

    <div class="card">
      <div class="tab">David Bau</div>
      <div class="content">
        <div class="avatar c5">DB</div>
        <div class="name">David Bau</div>
        <div class="aff">Northeastern, Boston</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/y6DZloFMZT4">The National Deep Inference Fabric</a> (<a href="https://docs.google.com/document/d/1gCCvDQN54xjcgXu8X5BHSIqvEIkXrVDPe-UaiQwLO4g">summary</a>)<br>
          • July 11, 2025<br/>
          <b>Focus:</b> Neural network interpretability
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">David Eaves</div>
      <div class="content">
        <div class="avatar c2">DE</div>
        <div class="name">David Eaves</div>
        <div class="aff">UCL, London</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-eaves">Lessons from digital public infrastructure</a> (<a href="https://docs.google.com/document/d/1kuVO1-7o_RQCMk6USywjrlX-31q3beOAWDChAFvJIAk">summary</a>)<br>
          • February 20, 2024<br/>
          <b>Focus:</b> Digital government, open data
        </div>
        <div class="joined">Season 1</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Divya Siddarth</div>
      <div class="content">
        <div class="avatar c4">DS</div>
        <div class="name">Divya Siddarth</div>
        <div class="aff">Collective Intelligence Project, SF</div>
        <div class="details">
          <b>Seminar:</b>
          • Democratic AI (<a href="https://docs.google.com/document/d/1z0OOK7lwcwXBU59hqwFMR6_Plycdri52n01E89zhNm4">summary</a>)<br>
          • September 17, 2024<br/>
          <b>Focus:</b> Participatory governance, collective intelligence
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">EM Lewis-Jong</div>
      <div class="content">
        <div class="avatar c3">EL</div>
        <div class="name">EM Lewis-Jong</div>
        <div class="aff">Mozilla</div>
        <div class="details">
          <b>Seminar:</b>
          • Community data and Common Voice (<a href="#">summary</a>)<br>
          • May 6, 2025<br/>
          <b>Focus:</b> Common Voice dataset
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Ganesh Sitaraman</div>
      <div class="content">
        <div class="avatar c4">GS</div>
        <div class="name">Ganesh Sitaraman</div>
        <div class="aff">Vanderbilt, US</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-sitaraman">Industrial organization and antimonopoly</a> (<a href="https://docs.google.com/document/d/1tJMZ0QHDO2fn1R_Ilftpx9nwliBy_CIufxFfPIgAltU">summary</a>)<br>
          • February 13, 2024<br/>
          <b>Focus:</b> Antitrust, constitutional law
        </div>
        <div class="joined">Season 1</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Irene Solaiman</div>
      <div class="content">
        <div class="avatar c3">IS</div>
        <div class="name">Irene Solaiman</div>
        <div class="aff">HuggingFace</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-solaiman">The role of openness in AI</a> (<a href="https://docs.google.com/document/d/1qV-1StRDlSFpVPXtusmXAxNIgGtR6CTpno9dUe8tiZY">summary</a>)<br>
          • September 10, 2024<br/>
          <b>Focus:</b> AI safety, responsible release
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>


    <div class="drawer-front">
      <div class="drawer-label">SPEAKERS A-I</div>
    </div>

  </div>
  <!-- J-M -->
  <div class="catalog-column">

    <div class="card">
      <div class="tab">Jeni Tennison</div>
      <div class="content">
        <div class="avatar c3">JT</div>
        <div class="name">Jeni Tennison</div>
        <div class="aff">Connected by Data</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://www.youtube.com/watch?v=C6lUBq59m5M">Community power in AI</a> (<a href="https://docs.google.com/document/d/1uHOgx85q3v1mgO_xOfelYU5nlsFYgk7nlshmLt7qAKo">summary</a>)<br>
          • October 1, 2024<br/>
          <b>Focus:</b> Data governance, collective consent
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Julia Angwin</div>
      <div class="content">
        <div class="avatar c1">JA</div>
        <div class="name">Julia Angwin</div>
        <div class="aff">New York Times / Harvard</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-angwin">The politics of AI</a> (<a href="https://docs.google.com/document/d/14KkrfR7dLQcrUotxhXDQhoTHSV0wg6ehWpPddt6gyko">summary</a>)<br>
          • February 6, 2024<br/>
          <b>Focus:</b> Algorithmic accountability journalism
        </div>
        <div class="joined">Season 1</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Julia Lane</div>
      <div class="content">
        <div class="avatar c6">JL</div>
        <div class="name">Julia Lane</div>
        <div class="aff">NYU Wagner School</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-lane-leonard">AI and the labor market</a> (<a href="https://docs.google.com/document/d/1pD3Ytmjgd7eTvAqfhLsm9IXkzdg60yA0uqHGSsdSr5I">summary</a>)<br>
          • Library of Congress Speaker<br/>
          <b>Focus:</b> Data science, labor economics
        </div>
        <div class="joined">Multiple Events</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Katie Antypas</div>
      <div class="content">
        <div class="avatar c1">KA</div>
        <div class="name">Katie Antypas</div>
        <div class="aff">National Science Foundation</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-decario-antypas">Public compute</a> (<a href="https://docs.google.com/document/d/1Dr3UlH9Orb7GD0wYga94xNIVKOrEkjH2P_A1qqvBWZ4">summary</a>)<br>
          • AI in the Agencies Panel - LoC<br/>
          <b>Focus:</b> Research computing infrastructure
        </div>
        <div class="joined">Multiple Events</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Kim Stanley Robinson</div>
      <div class="content">
        <div class="avatar c2">KR</div>
        <div class="name">Kim Stanley Robinson</div>
        <div class="aff">Author</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/qQe7H9CY5Bw">The near possible future of AI</a> (<a href="https://docs.google.com/document/d/1POa6jdSMKxWt-ktxoyxezLKu8PD4GtAxUshSAdbtgU8">summary</a>)<br>
          • June 10, 2025<br/>
          <b>Notable:</b> Science fiction, climate futures
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Lawrence Lessig</div>
      <div class="content">
        <div class="avatar c2">LL</div>
        <div class="name">Lawrence Lessig</div>
        <div class="aff">Harvard Law School</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-lessig">AI and democracy</a> (<a href="https://docs.google.com/document/d/1jHePFaAw_0MJSBqZ84Toep1GS3HR5DftpyHTzTTL8qk">summary</a>)<br>
          • Library of Congress: <a href="https://rebootdemocracy.ai/blog/building-a-more-public-ai-ecosystem-lawrence-lessig">Why This is the Moment for Public AI</a><br/>
          <b>Focus:</b> Democracy, regulation, institutional corruption
        </div>
        <div class="joined">Multiple Events</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Leslie Teo</div>
      <div class="content">
        <div class="avatar c4">LT</div>
        <div class="name">Leslie Teo</div>
        <div class="aff">AI Singapore</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-teo">SEA-LION</a> (<a href="https://docs.google.com/document/d/18TPtkUfRmhZbpvuQPgrmr_kCiK9R_mBhHa6aDKYekMI">summary</a>)<br>
          • August 27, 2024<br/>
          <b>Focus:</b> Southeast Asian language models
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Martin Tisné</div>
      <div class="content">
        <div class="avatar c6">MT</div>
        <div class="name">Martin Tisné</div>
        <div class="aff">AI Collaborative, Current AI, Omidyar</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/3kd39SvaOr8">Public interest AI</a> (<a href="https://docs.google.com/document/d/1mFQvRwSY3ou9eVSEdnJJrgI61g-I3rRs_kWbmmWU-S0">summary</a>)<br>
          • May 20, 2025<br/>
          <b>Focus:</b> Data rights, philanthropy
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Mat Dryhurst</div>
      <div class="content">
        <div class="avatar c4">MD</div>
        <div class="name">Mat Dryhurst</div>
        <div class="aff">Artist</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/PTXqXvWh5jk">Do Not Train</a> (<a href="https://docs.google.com/document/d/1dA6y01RaEvgApO6VrCAEjd4K-eZl5U9oN_2xP40GzNs">summary</a>)<br>
          • April 22, 2025<br/>
          <b>Focus:</b> Spawning AI, artist rights
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>


    <div class="drawer-front">
      <div class="drawer-label">SPEAKERS J-M</div>
    </div>

  </div>
  <!-- N-Z -->
  <div class="catalog-column">

    <div class="card">
      <div class="tab">Nicole DeCario</div>
      <div class="content">
        <div class="avatar c1">ND</div>
        <div class="name">Nicole DeCario</div>
        <div class="aff">Allen Institute (AI2)</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-decario-antypas">Public compute</a> (<a href="https://docs.google.com/document/d/1Dr3UlH9Orb7GD0wYga94xNIVKOrEkjH2P_A1qqvBWZ4/edit?usp=sharing">summary</a>)<br>
          • August 20, 2024<br/>
          <b>Focus:</b> AI2 compute infrastructure
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Reema Selhi</div>
      <div class="content">
        <div class="avatar c6">RS</div>
        <div class="name">Reema Selhi</div>
        <div class="aff">DACS, British Copyright Council</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/PTXqXvWh5jk">AI and copyright</a> (<a href="https://docs.google.com/document/d/1dA6y01RaEvgApO6VrCAEjd4K-eZl5U9oN_2xP40GzNs/edit?tab=t.0">summary</a>)<br>
          • April 22, 2025<br/>
          <b>Focus:</b> Copyright law, artist rights
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Rick Stevens</div>
      <div class="content">
        <div class="avatar c2">RS</div>
        <div class="name">Rick Stevens</div>
        <div class="aff">Argonne National Labs</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-stevens-orourke">Case study: AuroraGPT</a> (<a href="https://docs.google.com/document/d/1B2hpWIP-8kXCHuMuJ9ocr3Nk-R-M37OavXLyefiWiUQ/edit">summary</a>)<br>
          • January 23, 2024<br/>
          <b>Focus:</b> Science-focused language models
        </div>
        <div class="joined">Season 1</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Sarah Myers West</div>
      <div class="content">
        <div class="avatar c3">SW</div>
        <div class="name">Sarah Myers West</div>
        <div class="aff">AI Now</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/_fqbtIQtHFE">AI Nationalisms</a> (<a href="https://docs.google.com/document/d/10o_fJVzRHsSxcSMJuyp4UmG9IlYMB-dO8EDs8Vqa6Uc/edit?tab=t.0">summary</a>)<br>
          • October 15, 2024<br/>
          <b>Focus:</b> AI policy, geopolitics
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Ted Chiang</div>
      <div class="content">
        <div class="avatar c3">TC</div>
        <div class="name">Ted Chiang</div>
        <div class="aff">Author</div>
        <div class="details">
          <b>Seminar:</b>
          • Generative AI is not useful for making art<br>
          • April 29, 2025<br/>
          <b>Notable:</b> Science fiction, AI criticism
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Taylor Jo Isenberg</div>
      <div class="content">
        <div class="avatar c4">TI</div>
        <div class="name">Taylor Jo Isenberg</div>
        <div class="aff">Economic Security Project</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://youtu.be/HorkM5CndtE">A Vision for Public AI in California</a> (<a href="https://docs.google.com/document/d/1rjO6enuPU7YlCb_RCnAmhfs9nW_v7CNy9suXTlTSOjE">summary</a>)<br>
          • May 13, 2025<br/>
          <b>Focus:</b> Economic policy, public options
        </div>
        <div class="joined">Season 3</div>
      </div>
    </div>

    <div class="card">
      <div class="tab">Yoshua Bengio</div>
      <div class="content">
        <div class="avatar c1">YB</div>
        <div class="name">Yoshua Bengio</div>
        <div class="aff">MILA, LawZero</div>
        <div class="details">
          <b>Seminar:</b>
          • <a href="https://archive.org/details/public-ai-bengio">Towards a network of publicly-funded AI labs</a> (<a href="https://docs.google.com/document/d/1na9xHK95XLW9TaUOx5DF_bpTu9mgTQYSAT7bWzWAMHM/edit">summary</a>)<br>
          • August 13, 2024<br/>
          <b>Focus:</b> AI safety advocacy, <a href="https://lawzero.org">LawZero</a>
        </div>
        <div class="joined">Season 2</div>
      </div>
    </div>

    <div class="drawer-front">
      <div class="drawer-label">SPEAKERS N-Z</div>
    </div>
  </div>

</div>

*Other facilitators and speakers at past Public AI events include:* 
* [*AI in the Agencies*](https://www.aspendigital.org/event/building-a-more-public-ai-ecosystem/) panel, Library of Congress, 2024-08-11: Travis Hoppe (AI R&D, White House OSTP), Victoria Houed (AI Policy, Commerce; now at POPVOX), Zach  Whitman (Chief AI Officer, GSA). Caroyln Dee (NY State AI policy) gave a presentation about the state of Empire AI.
* [**Public AI Congress**](https://www.ai-inthecity.ens.psl.eu/en/programme/67892dde5474c438e5a4c5b0), Paris, 2025-02-11: Adriana Groh, [Sovereign Tech Agency](https://www.sovereign.tech/) (Germany); Alexander Ilic, ETH AI Center (Switzerland); Marta Villegas, BSC (Spain); Petri Myllymäki, Ellis Institute (Finland) 
* [**AI Action II**](https://docs.google.com/document/d/1IyP2jGob6Zxp1V7jjN1Ax--r45FHGYBgDhK31eoMNVU/edit?tab=t.0), Fey, 2025-02-12/13: Brewster Kahle (Internet Archive), Peter Wang (Anaconda), Primavera De Filippi (Alien), Pedro Ortiz Suarez (Common Crawl), Vincent Ginis (VUB)

<br/>

## Supporting Organizations

*We gratefully acknowledge operational support and collaboration from:*

<div class="org-grid">
    <div class="org-row">
      <div class="org-logo" title="Metagov - Computational governance research">
        <a href="https://metagov.org" style="color: #49e;">MG</a>
      </div>
      <div class="org-logo" title="Aspen Digital - Tech policy and digital rights">
        <a href="https://www.aspendigital.org/"  style="color: #e54;">AD</a>
      </div>
      <div class="org-logo" title="Public Knowledge - Open internet advocacy">
        <a href="https://publicknowledge.org"  style="color: #fa1;">PK</a>
      </div>
      <div class="org-logo" title="Chatham House - International affairs think tank">
        <a href="https://chathamhouse.org"  style="color: #579;">CH</a>
      </div>
    </div>
  
    <div class="org-row">
      <div class="org-logo" title="Code for Science & Society - Open science">
        <a href="https://codeforscience.org" style="color: #6be;">CS&S</a>
      </div>
      <div class="org-logo" title="Berkman Klein Center - Internet & society research">
        <a href="https://cyber.harvard.edu"  style="color: #a2f;">BKC</a>
      </div>
      <div class="org-logo" title="Rockefeller Foundation - Equity & resilience">
       <a href="https://www.rockefellerfoundation.org/" style="color: #d69;">RF</a>
      </div>
    </div>

    <div class="org-row">
      <div class="org-logo" title="Mozilla Foundation - Internet health">
        <a href="https://www.mozillafoundation.org/" style="color: #f84;">MF</a>
      </div>
      <div class="org-logo" title="Patrick J. McGovern Foundation - AI for humanity">
        <a href="https://www.mcgovern.org" style="color: #c13;">PMF</a>
      </div>
      <div class="org-logo" title="Siegel Family Endowment">
        <a href="https://www.siegelendowment.org"  style="color: #1b6;">SE</a>
      </div>
      <div class="org-logo" title="Open Future - Digital commons advocacy">
        <a href="https://openfuture.eu"  style="color: #696;">OF</a>
      </div>
    </div>
  
    <div class="org-row">
      <div class="org-logo" title="Internet Archive - Universal access to knowledge">
        <a href="https://archive.org" style="color: #36b;">IA</a>
      </div>
      <div class="org-logo" title="Library of Congress - National library">
        <a href="https://loc.gov" style="color: #941;">LoC</a>
      </div>
      <div class="org-logo" title="Bertelsmann Foundation - Digital society">
        <a href="https://bfna.org" style="color: #06c;">BF</a>
      </div>  
      <div class="org-logo" title="Creative Commons - Open licensing">
        <a href="https://creativecommons.org/" style="color: #fd4;">CC</a>
      </div>
    </div>
  
  <div style="text-align:center; color:#999; font-size:14px"> <br/> 
  Metagov · Aspen Digital · Public Knowledge · Chatham House <br/>
  Code for Science and Society · Berkman Klein Center · Rockefeller Foundation <br/>
  Mozilla Foundation · Patrick J. McGovern Foundation · Siegel Family Endowment · Open Future<br/>
  Internet Archive · Library of Congress · Bertelsmann Foundation · Creative Commons 
  </div>
</div>


<!--  easier to find "get involved" links -->
## Join the Movement

We are always looking for people and organizations committed to ensuring AI serves the public good. Whether you're a researcher, policymaker, technologist, or advocate, there's a place for you in our community.

We host a Slack for active community members and partners, and host regular events including a [seminar series](../seminar.html) to share insights from and foster discussion with leaders in various fields.

<div style="text-align: center; margin: 3em 0;">
  <a href="mailto:hello@publicai.network" style="display: inline-block; padding: 12px 30px; background: #667eea; color: white; text-decoration: none; border-radius: 25px; font-weight: bold; margin: 0 10px;">Get Involved</a>
  <a href="https://publicai.substack.com" style="display: inline-block; padding: 12px 30px; border: 2px solid #667eea; color: #667eea; text-decoration: none; border-radius: 25px; font-weight: bold; margin: 0 10px;">Subscribe</a>
</div>
<!-- -->

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Randomize avatar colors
  const avatars = document.querySelectorAll('.avatar');
  avatars.forEach(avatar => {
    const randomColor = Math.floor(Math.random() * 6) + 1;
    avatar.className = 'avatar c' + randomColor;
  });
  
  // Create popup element
  const popup = document.createElement('div');
  popup.className = 'popup';
  document.body.appendChild(popup);
  
  let currentCard = null;
  let popupTimer = null;

  // Handle card hover
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', function(e) {
      
      // Clear any existing timer
      if (popupTimer) {
        clearTimeout(popupTimer);
        popupTimer = null;
      }

      currentCard = this;
      const content = this.querySelector('.content').innerHTML;
      popup.innerHTML = content;
      popup.style.display = 'block';
      
      const rect = this.getBoundingClientRect();
      let left = rect.right - 5;  // Position to the right of the card
      let top = rect.top - 30;    // Align card name w/ popup icon
      
      // Keep popup on screen
      if (left + 300 > window.innerWidth) {
        left = rect.left - 40;  // Show on left if no room on right
        top = rect.top + 30;
      }
      if (top < 10) top = 10;
      
      // Adjust height dynamically based on content
      popup.style.height = 'auto';
      popup.style.left = left + 'px';
      popup.style.top = top + 'px';
    });    

    card.addEventListener('mouseleave', function(e) {
      // Only hide if not moving to popup
      const related = e.relatedTarget;
      if (!popup.contains(related)) {
        popupTimer = setTimeout(() => {
          popup.style.display = 'none';
          currentCard = null;
        }, 100);  // Small delay to allow moving to popup
      }
    });
  });
  

  // Hide popup when leaving it
  popup.addEventListener('mouseleave', function(e) {
    // Check if we're not going back to the original card
    const related = e.relatedTarget;
    if (!currentCard || !currentCard.contains(related)) {
      popup.style.display = 'none';
      currentCard = null;
    }
  });
  
  // Search functionality
  const searchInput = document.getElementById('peopleSearch');
  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const searchTerm = e.target.value.toLowerCase();
      const allCards = document.querySelectorAll('.card');
      
      allCards.forEach(card => {
        const tab = card.querySelector('.tab').textContent.toLowerCase();
        const content = card.querySelector('.content').textContent.toLowerCase();
        
        if (tab.includes(searchTerm) || content.includes(searchTerm)) {
          card.style.opacity = '1';
          card.style.pointerEvents = 'auto';
        } else {
          card.style.opacity = '0.3';
          card.style.pointerEvents = 'none';
        }
      });
    });
  }
});
</script>
