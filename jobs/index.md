---
layout: page
title: Jobs
nav_title: Jobs
permalink: /jobs/
---

Open roles at the Public AI Network. These opportunities are funded by and offered in collaboration with [Current AI](https://currentai.org), a Paris-based nonprofit.

<style>
.job-list {
  list-style: none;
  padding: 0;
  margin: 2rem 0;
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
</style>

<ul class="job-list">
{% assign sorted_jobs = site.jobs | sort: "order" %}
{% for job in sorted_jobs %}
  <li>
    <a href="{{ job.url | relative_url }}">{{ job.title }}</a>
    <span class="job-meta">{{ job.location }} · {{ job.commitment }}</span>
    {% if job.summary %}
    <p class="job-summary">{{ job.summary }}</p>
    {% endif %}
  </li>
{% endfor %}
</ul>

Questions? Email [josh@publicai.co](mailto:josh@publicai.co).
