---
title: SAIL Specification
layout: page
description: Detailed specification of the SAIL certification system methodology and evaluation criteria.
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

.layer-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 2rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.layer-card h3 {
  color: #667eea;
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border-bottom: 2px solid #667eea;
  padding-bottom: 0.5rem;
}

.layer-card h3::before {
  content: '';
  width: 4px;
  height: 24px;
  background: #667eea;
  border-radius: 2px;
}

.credit-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

.credit-table th,
.credit-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.credit-table th {
  background: #f8f9fa;
  font-weight: 600;
  color: #333;
}

.credit-table tr:hover {
  background: #f8f9fa;
}

.points-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #667eea;
  color: white;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  min-width: 50px;
  text-align: center;
}

.cert-level {
  background: white;
  border: 2px solid;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
}

.cert-level.platinum {
  border-color: #e8e8e8;
  background: linear-gradient(135deg, #f8f8f8 0%, #ffffff 100%);
}

.cert-level.gold {
  border-color: #ffd700;
  background: linear-gradient(135deg, #fff9e6 0%, #ffffff 100%);
}

.cert-level.silver {
  border-color: #c0c0c0;
  background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
}

.cert-level.certified {
  border-color: #667eea;
  background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%);
}

.cert-level h3 {
  margin-top: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cert-level.platinum h3 {
  color: #666;
}

.cert-level.gold h3 {
  color: #b8860b;
}

.cert-level.silver h3 {
  color: #808080;
}

.cert-level.certified h3 {
  color: #667eea;
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

.flag-box {
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 1rem;
  margin: 1.5rem 0;
  border-radius: 4px;
}

.constraint-box {
  background: #f8d7da;
  border-left: 4px solid #dc3545;
  padding: 1rem;
  margin: 1.5rem 0;
  border-radius: 4px;
}

.key-principles {
  background: #d1ecf1;
  border-left: 4px solid #17a2b8;
  padding: 1.5rem;
  margin: 2rem 0;
  border-radius: 4px;
}

.key-principles ul {
  margin: 0.5rem 0;
}
</style>

<nav class="spec-nav">
  <a href="/sail">Home</a>
  <a href="/sail/interests">Interests</a>
  <a href="/sail/cases">Cases</a>
  <a href="/sail/models">Models</a>
  <a href="/sail/countries">Countries</a>
</nav>

## SAIL Specification

This document provides the complete specification for the **Sovereign AI Leadership (SAIL)** assessment, including evaluation criteria, point-based scoring methodology, and control-maturity levels.

### Table of Contents

<div class="toc">
<ul>
  <li><a href="#when-to-use">When to use this spec</a></li>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#levels">Control-Maturity Levels</a></li>
  <li><a href="#layers">The Seven Layers</a></li>
  <li><a href="#flags">Flags & Constraints</a></li>
  <li><a href="#process">Assessment Process</a></li>
</ul>
</div>

## When to use this spec {#when-to-use}

This specification assesses one specific thing: **how much control an entity has over its AI stack, and how readily it could exit a dependency.** That is exactly what some sovereign AI interests are about, and beside the point for others.

<div class="key-principles">
<h4>Use this spec when</h4>
<ul>
  <li>Your primary interest is <strong>control, dependency transparency, or exit readiness</strong> - typical of enterprise, procurement, and security concerns.</li>
  <li>You need to compare strategies on capability actually demonstrated, not intent declared.</li>
</ul>
<h4>Do not use this spec as a proxy for</h4>
<ul>
  <li><strong>Cultural legitimacy</strong> - whether a model "feels French" is a question of governance and representation, not a score.</li>
  <li><strong>Industrial-policy success</strong> - jobs, fabs, and regional investment are real goals the stack does not measure.</li>
</ul>
</div>

Before applying the spec, decode the interest driving the request. The [interest decoder](/sail/interests) explains the five common interests behind sovereign AI claims; the table below routes each layer to the interests that care most about it.

<table class="credit-table">
  <thead>
    <tr>
      <th>Layer</th>
      <th>Interests that care most</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#layer-1-application--service-sovereignty">Layer 1: Application</a></td>
      <td>Enterprise &amp; procurement</td>
    </tr>
    <tr>
      <td><a href="#layer-2-orchestration-integration--distribution">Layer 2: Orchestration</a></td>
      <td>Enterprise &amp; procurement</td>
    </tr>
    <tr>
      <td><a href="#layer-3-data-sovereignty-origin-control-evaluation">Layer 3: Data</a></td>
      <td>Enterprise &amp; procurement; cultural identity &amp; values</td>
    </tr>
    <tr>
      <td><a href="#layer-4-model-sovereignty-reproducibility--capability">Layer 4: Model</a></td>
      <td>Industrial policy; cultural identity &amp; values</td>
    </tr>
    <tr>
      <td><a href="#layer-5-training--post-training-sovereignty">Layer 5: Training</a></td>
      <td>Industrial policy; cultural identity &amp; values</td>
    </tr>
    <tr>
      <td><a href="#layer-6-compute--infrastructure-sovereignty-structural">Layer 6: Compute</a></td>
      <td>Security &amp; weaponization; industrial policy; middle-power alliance</td>
    </tr>
    <tr>
      <td><a href="#layer-7-legal-governance--exit-sovereignty">Layer 7: Legal &amp; Exit</a></td>
      <td>Security &amp; weaponization; enterprise &amp; procurement</td>
    </tr>
  </tbody>
</table>

## Overview {#overview}

SAIL uses a **point-based system** for evaluating national and governmental AI strategies. As a framework, SAIL assesses AI sovereignty across the full AI stack from applications and data governance to training pipelines and compute dependencies.

To achieve SAIL certification, a country or public agency must:
1. First satisfy all **baseline prerequisites** (minimum governance, control, and transparency requirements) across each layer
2. Then earn **points** by meeting additional conditions aligned with its strategic goals

The framework is designed to reward realistic, optimized sovereignty strategies, including federated and allied approaches. It penalizes dependency and especially unacknowledged dependencies.

<div class="key-principles">
<h4>Key Principles</h4>
<ul>
  <li><strong>Sovereignty may be partial, federated, or optimized</strong>, but dependencies must be explicit.</li>
  <li><strong>Certain layers</strong> (compute, legal environment) act as structural constraints and may cap achievable tiers.</li>
  <li><strong>Credit is awarded</strong> for real capacity, legal robustness, and exit readiness, not stated intent.</li>
</ul>
</div>

<div class="key-principles">
<h4>Coordination &amp; federation</h4>
<p>SAIL treats <strong>federated and allied capacity as legitimate sovereignty</strong>, not a consolation prize. A country that pools compute and models with trusted partners, with dependencies acknowledged, can score as highly as one that builds everything alone - and more realistically, given the economics of frontier models.</p>
<p>The corollary is a <strong>fragmentation flag</strong>: strategies that duplicate chip and talent competition without allied benefit are scored as weaker on coordination. Building a national champion that erodes a viable middle-power alliance is a cost, not just a neutral choice. (This is a narrative flag for now, used in assessment commentary rather than as a fixed point deduction.) See the <a href="/sail/cases#cohere-aleph-alpha-and-franco-german-tension">Cohere / Aleph Alpha case</a> for the dynamic this guards against.</p>
</div>

**Note**: SAIL does not evaluate technical excellence, cultural legitimacy, or industrial-policy success, though it does look at publicly available adoption levels of sovereign products and artifacts.

## Control-Maturity Levels {#levels}

These levels describe how much control an entity has demonstrated over its stack. They measure control maturity, not national prestige - a Platinum result is a statement about dependency and exit readiness, not a ranking of whose AI is most sovereign.

### Platinum — End-to-End Control
**80+ points earned**

Demonstrates end-to-end control across the AI stack, including model adaptation and pre-training (individually or through credible allied/federated arrangements).

<div class="cert-level platinum">
  <h3>🏆 Platinum Certification</h3>
  <p><strong>Requirements:</strong> 80+ points with strong performance across all layers, especially Layers 4-6 (Model, Training, and Compute sovereignty).</p>
  <p><strong>Constraint:</strong> If Layer 6 (Compute) score < 10, Platinum certification is capped unless credible federated arrangements exist.</p>
</div>

### Gold — Strategic Sovereignty
**60–79 points earned**

Demonstrates strong control over data and model behavior, with limited but well-managed external dependencies.

<div class="cert-level gold">
  <h3>🥇 Gold Certification</h3>
  <p><strong>Requirements:</strong> 60-79 points with demonstrated control at Layers 1-4 (Application through Model sovereignty).</p>
</div>

### Silver — Operational Sovereignty
**50–59 points earned**

Demonstrates control at the application and data layers, with meaningful but unresolved dependencies at deeper layers.

<div class="cert-level silver">
  <h3>🥈 Silver Certification</h3>
  <p><strong>Requirements:</strong> 50-59 points with baseline control at Layers 1-3 (Application, Orchestration, Data sovereignty).</p>
</div>

### Certified — Baseline Sovereignty
**40–49 points earned**

Meets baseline prerequisites and demonstrates initial control over AI deployment and governance, but remains highly dependent on external providers.

<div class="cert-level certified">
  <h3>✓ Certified</h3>
  <p><strong>Requirements:</strong> 40-49 points meeting all baseline prerequisites across layers.</p>
</div>

## The Seven Layers {#layers}

### Layer 1: Application & Service Sovereignty
**Max points: 25**

This layer evaluates whether AI-enabled public services can be modified, migrated, or withdrawn without reliance on a specific vendor, model, or jurisdiction.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>A1</strong></td>
      <td>Model-agnostic service design - Core service logic decoupled from specific models or APIs</td>
      <td><span class="points-badge">6</span></td>
    </tr>
    <tr>
      <td><strong>A2</strong></td>
      <td>Public ownership of application logic - State owns or controls source code and workflows</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>A3</strong></td>
      <td>Vendor substitution feasibility - Demonstrated ability to swap AI providers within 6–12 months</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>A4</strong></td>
      <td>Decision traceability & auditability - AI-assisted decisions are logged and reviewable</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>A5</strong></td>
      <td>Domestic service maintenance capacity - In-country teams can modify and redeploy services</td>
      <td><span class="points-badge">5</span></td>
    </tr>
  </tbody>
</table>

### Layer 2: Orchestration, Integration & Distribution
**Max points: 25**

This layer assesses control over how AI components are composed, routed, monitored, and distributed to users.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>O1</strong></td>
      <td>Provider-independent orchestration - Ability to route workloads across models/providers</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>O2</strong></td>
      <td>Institution-controlled policy layer - Safety, usage, and routing rules defined locally</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>O3</strong></td>
      <td>System observability - Prompts, outputs, failures are inspectable</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>O4</strong></td>
      <td>Independent rollback & suspension - Systems can be paused or reverted without vendor approval</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>O5</strong></td>
      <td>Distribution sovereignty - Control over primary model/service distribution channels</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>O6</strong></td>
      <td>Migration-ready hosting - Ability to mirror or migrate hosting jurisdiction</td>
      <td><span class="points-badge">3</span></td>
    </tr>
  </tbody>
</table>

### Layer 3: Data Sovereignty (Origin, Control, Evaluation)
**Max points: 25**

This layer evaluates control over the data AI systems learn from, remember, and are evaluated against—emphasizing provenance and legal robustness.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>D1</strong></td>
      <td>Legal ownership of datasets - Enforceable public rights over AI-relevant data</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>D2</strong></td>
      <td>Data curation & deletion authority - Ability to modify, filter, and delete data</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>D3</strong></td>
      <td>Data provenance balance - Meaningful share of data from domestic or allied sources</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>D4</strong></td>
      <td>Legally robust openness - Data reusable under clear, defensible licenses</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>D5</strong></td>
      <td>Evaluation & benchmark sovereignty - Ownership/control of eval and post-training datasets</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>D6</strong></td>
      <td>Prevention of irreversible leakage - Safeguards against uncontrolled embedding/gradient reuse</td>
      <td><span class="points-badge">3</span></td>
    </tr>
  </tbody>
</table>

### Layer 4: Model Sovereignty (Reproducibility & Capability)
**Max points: 25**

This layer measures the ability to shape, reproduce, and rely on models as sovereign infrastructure, not just artifacts.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>M1</strong></td>
      <td>Access to weights or adapters - Meaningful ability to modify model behavior</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>M2</strong></td>
      <td>Reproducibility completeness - Training data, recipes, scripts documented</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>M3</strong></td>
      <td>Independent fine-tuning capacity - Domestic ability to adapt models</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>M4</strong></td>
      <td>Task-level competitiveness - Models competitive in priority public-sector tasks</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>M5</strong></td>
      <td>Version control & forkability - Ability to freeze, fork, or maintain versions</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>M6</strong></td>
      <td>Dependency-adjusted integrity - No opaque external components in core models</td>
      <td><span class="points-badge">3</span></td>
    </tr>
  </tbody>
</table>

### Layer 5: Training & Post-Training Sovereignty
**Max points: 25**

This layer assesses control over alignment, instruction tuning, and improvement processes after pretraining.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>T1</strong></td>
      <td>Control over training objectives - Public authority defines reward/alignment goals</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>T2</strong></td>
      <td>Vendor-independent post-training - Fine-tuning without external approval</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>T3</strong></td>
      <td>Reproducibility of adaptations - Training outcomes can be reproduced</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>T4</strong></td>
      <td>Transparency of interventions - Post-training changes are documented</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>T5</strong></td>
      <td>Institutional oversight - Formal oversight of alignment decisions</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>T6</strong></td>
      <td>In-region execution - Post-training physically executed domestically/allied</td>
      <td><span class="points-badge">3</span></td>
    </tr>
  </tbody>
</table>

### Layer 6: Compute & Infrastructure Sovereignty (Structural)
**Max points: 25**

This layer evaluates reliable, governable access to compute and infrastructure required to train and run AI systems.

<div class="constraint-box">
<strong>Structural Constraint:</strong> If Layer 6 score < 10, Platinum certification is capped unless credible federated arrangements exist.
</div>

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>C1</strong></td>
      <td>Guaranteed compute access - Domestic or allied compute under public control</td>
      <td><span class="points-badge">6</span></td>
    </tr>
    <tr>
      <td><strong>C2</strong></td>
      <td>Priority & crisis allocation - Ability to reprioritize workloads in emergencies</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>C3</strong></td>
      <td>Time-to-availability - Capacity available now or within 12 months</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>C4</strong></td>
      <td>Absence of unilateral kill-switches - No single foreign actor can disable access</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>C5</strong></td>
      <td>Supply chain resilience - Plans for hardware/energy disruption</td>
      <td><span class="points-badge">3</span></td>
    </tr>
    <tr>
      <td><strong>C6</strong></td>
      <td>Inference/training separation - Dedicated inference capacity for public services</td>
      <td><span class="points-badge">2</span></td>
    </tr>
  </tbody>
</table>

### Layer 7: Legal, Governance & Exit Sovereignty
**Max points: 25**

This layer measures legal authority, institutional mandate, and the ability to override or exit AI systems.

<table class="credit-table">
  <thead>
    <tr>
      <th>Credit</th>
      <th>Description</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>G1</strong></td>
      <td>Legal override authority - Clear authority to suspend or retire AI systems</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>G2</strong></td>
      <td>Contractual exit rights - Explicit migration/fork rights in contracts</td>
      <td><span class="points-badge">5</span></td>
    </tr>
    <tr>
      <td><strong>G3</strong></td>
      <td>Documented exit playbooks - Layer-by-layer exit strategies</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>G4</strong></td>
      <td>Oversight with technical competence - Independent oversight bodies</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>G5</strong></td>
      <td>Legal stability outlook - AI-enabling rights stable or improving</td>
      <td><span class="points-badge">4</span></td>
    </tr>
    <tr>
      <td><strong>G6</strong></td>
      <td>Policy alignment - AI strategy aligned with IP/copyright law</td>
      <td><span class="points-badge">3</span></td>
    </tr>
  </tbody>
</table>

## Flags & Constraints {#flags}

### Compute Constraint Flag
**Triggered if Layer 6 < 10**

If compute sovereignty is insufficient, Platinum certification is capped unless credible federated arrangements exist.

### Legal Trajectory Flag
**Triggered if G5 = 0 or 1**

Indicates concerns about legal stability and the sustainability of AI-enabling rights.

### Distribution Dependency Flag
**Triggered if O5 = 0 or 1**

Indicates lack of control over primary model/service distribution channels.

## Assessment Process {#process}

1. **Decode the interest**: Establish which sovereign AI [interest](/sail/interests) is actually driving the request, and confirm the spec is the right tool for it
2. **Baseline Assessment**: Verify all baseline prerequisites are met across each layer
3. **Point Evaluation**: Assess each credit criterion and award points based on demonstrated capacity
4. **Flag Review**: Identify and document any structural constraints, coordination, or fragmentation flags
5. **Maturity Level**: Determine the control-maturity level based on total points and constraints
6. **Public Review**: Publish the assessment for public comment and peer review

---

**Total Possible Points: 175**

*This specification is maintained by the Public AI Network. For questions or suggestions, please contact [info@publicai.network](mailto:info@publicai.network).*

*Acknowledgements: Jan Hajic's presentation to OSFM.*
