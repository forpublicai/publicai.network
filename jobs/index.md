---
layout: page
title: Jobs
nav_title: Jobs
permalink: /jobs/
---

The movement for public AI (often capitalized as just Public AI) is a political movement and open-source community working to foster public AI. As part of our work, we offer some roles which are traditionally funded and others of which are more informal and independent (but no less important), as in a typical open-source community.

Also take a look at the [“help wanted” issues on our GitHub](https://github.com/forpublicai/publicai.network/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22).

<style>
.job-section {
  margin: 2.5rem 0 1rem;
}

.job-section h2 {
  margin-bottom: 0.5rem;
}

.job-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
}

.job-list li {
  border-bottom: 1px solid #e9ecef;
  padding: 1.25rem 0;
}

.job-list li:first-child {
  border-top: 1px solid #e9ecef;
}

.job-list a {
  color: #007bff;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
}

.job-list a:hover {
  text-decoration: underline;
}

.job-list--filled a {
  color: #495057;
}

.job-meta {
  display: block;
  margin-top: 0.35rem;
  font-size: 0.9rem;
  color: #6c757d;
}

.job-summary {
  margin: 0.5rem 0 0;
  color: #495057;
  line-height: 1.5;
}

.job-badge {
  display: inline-block;
  margin-left: 0.5rem;
  padding: 0.1rem 0.45rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #6c757d;
  background: #f1f3f5;
  border-radius: 4px;
  vertical-align: middle;
}
</style>

<div class="job-section">
  <h2 id="funded-roles">Funded roles</h2>
  <ul class="job-list">
  {% assign funded_open = site.jobs | where: "status", "open" | where: "category", "funded" | sort: "order" | sort: "date_posted" %}
  {% for job in funded_open %}
    <li>
      <a href="{{ job.url | relative_url }}">{{ job.title }}</a>
      {% if job.status == "filled" %}<span class="job-badge">Filled</span>{% endif %}
      <span class="job-meta">
        {% if job.host %}{{ job.host }} · {% endif %}{{ job.location }} · {{ job.commitment }}{% if job.compensation %} · {{ job.compensation }}{% endif %}
      </span>
      {% if job.summary %}
      <p class="job-summary">{{ job.summary }}</p>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
</div>

<div class="job-section">
  <h2 id="open-roles">Open roles in public AI</h2>
  <p>Volunteer positions with the movement for public AI, not associated to any hosting organization. Part-time and unpaid.</p>
  <ul class="job-list">
  {% assign volunteer_open = site.jobs | where: "status", "open" | where: "category", "volunteer" | sort: "order" | sort: "date_posted" %}
  {% for job in volunteer_open %}
    <li>
      <a href="{{ job.url | relative_url }}">{{ job.title }}</a>
      <span class="job-meta">
        {% if job.host %}{{ job.host }} · {% endif %}{{ job.location }} · {{ job.commitment }}
      </span>
      {% if job.summary %}
      <p class="job-summary">{{ job.summary }}</p>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
</div>

<div class="job-section">
  <h2 id="filled-roles">Filled roles</h2>
  <ul class="job-list job-list--filled">
  {% assign filled_jobs = site.jobs | where: "status", "filled" | sort: "order" | sort: "date_posted" %}
  {% for job in filled_jobs %}
    <li>
      {% if job.external_url %}
      <a href="{{ job.external_url }}" target="_blank" rel="noopener noreferrer">{{ job.title }}</a>
      {% else %}
      <a href="{{ job.url | relative_url }}">{{ job.title }}</a>
      {% endif %}
      <span class="job-badge">Filled</span>
      <span class="job-meta">
        {% if job.host %}{{ job.host }} · {% endif %}{{ job.location }}{% if job.commitment %} · {{ job.commitment }}{% endif %}{% if job.compensation %} · {{ job.compensation }}{% endif %}
      </span>
      {% if job.summary %}
      <p class="job-summary">{{ job.summary }}</p>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
</div>
