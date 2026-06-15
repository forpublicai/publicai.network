---
title: SAIL Cases
layout: page
description: Annotated cases of sovereign AI claims - reading the interest behind the headline.
permalink: /sail/cases/
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

.case {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.75rem 2rem;
  margin: 2rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.case h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 1.4rem;
}

.case-tags {
  margin: 0.75rem 0 1.25rem 0;
}

.tag {
  display: inline-block;
  padding: 3px 12px;
  border-radius: 14px;
  font-size: 0.8rem;
  font-weight: 600;
  margin: 2px 4px 2px 0;
}

.tag.security { background: #f8d7da; color: #842029; }
.tag.industrial { background: #fff3cd; color: #664d03; }
.tag.enterprise { background: #d1e7dd; color: #0f5132; }
.tag.values { background: #e2d9f3; color: #432874; }
.tag.alliance { background: #cfe2ff; color: #084298; }

.case p {
  line-height: 1.7;
  color: #444;
}

.case .reads,
.case .limits {
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin: 1rem 0;
}

.case .reads {
  background: #f8f9fa;
  border-left: 4px solid #667eea;
}

.case .limits {
  background: #fdf2f3;
  border-left: 4px solid #dc3545;
}

.case .reads h4,
.case .limits h4 {
  margin: 0 0 0.4rem 0;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.case .reads h4 { color: #667eea; }
.case .limits h4 { color: #dc3545; }

.case .reads p,
.case .limits p {
  margin: 0;
}

.layer-link {
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

.layer-link:hover {
  background: #5568d3;
  color: white;
}

.case-links {
  margin-top: 1rem;
  font-size: 0.95rem;
}
</style>

<nav class="sail-nav">
  <a href="/sail">Home</a>
  <a href="/sail/interests">Interests</a>
  <a href="/sail/cases" class="current">Cases</a>
  <a href="/sail/spec">Specification</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries">Countries</a>
</nav>

# Cases: reading the interest behind the headline

<p class="lede">Each case below takes a widely reported sovereign AI move and asks the SAIL question: what interest is actually driving it, which parts of the stack does it touch, and what does it leave unsolved? The tags map to the <a href="/sail/interests">five interests</a>; the layer links point into the <a href="/sail/spec">specification</a>.</p>

<div class="case">
  <h3>Microsoft's source-code vault in Switzerland</h3>
  <div class="case-tags">
    <span class="tag security">Security &amp; weaponization</span>
  </div>
  <p>To reassure European governments, Microsoft has offered arrangements that keep a copy of source code in a hardened Swiss facility, so that customers retain access even if the commercial relationship breaks down. It is the security interest made literal: a guarantee against a foreign kill-switch.</p>
  <div class="reads">
    <h4>What it reads as</h4>
    <p>A pure security and continuity play. It addresses the fear that a vendor or its home government could one day cut off a system that critical services depend on.</p>
  </div>
  <div class="limits">
    <h4>What it cannot solve</h4>
    <p>Holding the source proves you could inspect or, in extremis, run it. It does not give you the talent, data, or compute to actually rebuild and operate the system. Escrow is continuity insurance, not sovereign capability.</p>
  </div>
  <div>
    <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural" class="layer-link">Layer 6: Compute</a>
    <a href="/sail/spec#layer-7-legal-governance--exit-sovereignty" class="layer-link">Layer 7: Legal &amp; Exit</a>
  </div>
</div>

<div class="case">
  <h3 id="mistral-and-french-ai">Mistral and "French AI"</h3>
  <div class="case-tags">
    <span class="tag values">Cultural identity &amp; values</span>
    <span class="tag industrial">Industrial policy</span>
  </div>
  <p>Mistral is celebrated as French AI: a national champion that is also a statement about European capability and culture. Two interests overlap here. One is industrial - a flagship lab, jobs, and a foothold in the frontier. The other is about values - the sense that a French system should reflect French language, law, and norms.</p>
  <div class="reads">
    <h4>What it reads as</h4>
    <p>Industrial policy with a cultural overlay. The state benefits from a credible domestic lab; the public benefits from a model that feels like theirs.</p>
  </div>
  <div class="limits">
    <h4>What it cannot solve</h4>
    <p>The values dimension cannot be reached through productization. A model "feeling French" is a question of governance, representation, and recognition, not of headquarters location or shareholder nationality. The industrial dimension is real and assessable; the cultural one resists any checklist.</p>
  </div>
  <div>
    <a href="/sail/spec#layer-4-model-sovereignty-reproducibility--capability" class="layer-link">Layer 4: Model</a>
    <a href="/sail/spec#layer-5-training--post-training-sovereignty" class="layer-link">Layer 5: Training</a>
    <a href="/sail/models#france" class="layer-link">Model profile</a>
  </div>
</div>

<div class="case">
  <h3 id="cohere-aleph-alpha-and-franco-german-tension">Cohere, Aleph Alpha, and Franco-German tension</h3>
  <div class="case-tags">
    <span class="tag industrial">Industrial policy</span>
    <span class="tag alliance">Middle-power alliance</span>
  </div>
  <p>National champions are meant to reduce dependence. They can also fragment the alliances middle powers need. When one country backs its own flagship lab, neighbors read it as a reason to reduce their dependence in turn: "now we don't have to rely on the French." The result is parallel champions competing for the same chips and the same researchers, rather than pooling them.</p>
  <div class="reads">
    <h4>What it reads as</h4>
    <p>Industrial policy that quietly works against a middle-power alliance. Each national champion is rational on its own terms and corrosive to coordination in aggregate.</p>
  </div>
  <div class="limits">
    <h4>What it cannot solve</h4>
    <p>Going it alone does not deliver the scale that competing with hyperscalers requires. The interest that would actually help - pooled, federated capacity - is the one champion-building undermines.</p>
  </div>
  <div>
    <a href="/sail/spec#layer-6-compute--infrastructure-sovereignty-structural" class="layer-link">Layer 6: Compute</a>
    <a href="/sail/interests#middle-power-alliance" class="layer-link">Alliance interest</a>
  </div>
</div>

<div class="case">
  <h3>Declining an "OpenAI for Countries" deal</h3>
  <div class="case-tags">
    <span class="tag security">Security &amp; weaponization</span>
    <span class="tag industrial">Industrial policy</span>
    <span class="tag enterprise">Enterprise &amp; procurement</span>
    <span class="tag values">Cultural identity &amp; values</span>
  </div>
  <p>When a government turns down a hyperscaler's national-AI offer, it is reported as an act of sovereignty. But the refusal can be driven by any of several interests, and the right response depends entirely on which one.</p>
  <div class="reads">
    <h4>What it reads as</h4>
    <p>Any of four things: vendor diversification (enterprise), protecting a domestic champion (industrial), a security red line on foreign control, or electoral and values signaling where the refusal is itself the point. Decode before responding.</p>
  </div>
  <div class="limits">
    <h4>What it cannot solve</h4>
    <p>If the driver is signaling, no technical strategy follows at all - and treating it as a stack problem wastes the effort. If it is diversification or security, the spec has direct answers.</p>
  </div>
  <div>
    <a href="/sail/interests#decoder-is-this-about-refusing-the-openai-for-countries-deal" class="layer-link">See the decoder</a>
  </div>
</div>

<div class="case">
  <h3 id="sea-lion-apertus-and-the-public-ai-inference-utility">SEA-LION, Apertus, and the Public AI Inference Utility</h3>
  <div class="case-tags">
    <span class="tag alliance">Middle-power alliance</span>
    <span class="tag values">Cultural identity &amp; values</span>
  </div>
  <p>Singapore's SEA-LION and Switzerland's Apertus are openly governed models served to users worldwide through the Public AI Inference Utility. They point to a different answer than national autarky: shared, transparent infrastructure that many parties can draw on and govern.</p>
  <div class="reads">
    <h4>What it reads as</h4>
    <p>Sovereignty as governance and access rather than ownership and borders. SEA-LION serves regional languages; Apertus is fully open and reproducible. Both are credited under SAIL's federated-sovereignty principle.</p>
  </div>
  <div class="limits">
    <h4>What it cannot solve</h4>
    <p>This model depends on partners resisting the pull toward national champions. It is the strongest answer to the alliance interest and the most fragile, because it only works if enough actors choose it together.</p>
  </div>
  <div>
    <a href="/sail/spec#layer-4-model-sovereignty-reproducibility--capability" class="layer-link">Layer 4: Model</a>
    <a href="/sail/models#singapore" class="layer-link">SEA-LION profile</a>
    <a href="/sail/models#switzerland" class="layer-link">Apertus profile</a>
  </div>
</div>

<p class="case-links"><a href="/sail/interests">Back to the interest decoder &rarr;</a></p>
