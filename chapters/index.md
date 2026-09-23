---
title: Public AI University Chapters
layout: page
nav_title: Chapters
description: Start a Public AI chapter at your university.
permalink: /chapters/
---

A Public AI chapter is a student-led group that learns, builds, and serves with public-interest AI. Chapters are independent campus communities connected to the Public AI Network. They do not speak for Public AI, promise model performance, or collect sensitive data.

## Minimum requirements

- Three currently enrolled students, including a named coordinator.
- One faculty or staff adviser who agrees to support the group and campus compliance.

## First 90 days

- **Weeks 1-4**: run the four-week [Public AI handbook](https://publicai.network/handbook) course as a reading group. It covers foundations, political economy, national strategies and building public AI locally, and ends with a local action plan.
- **Weeks 5-8**: hold a hands-on session with [chat.publicai.co](https://chat.publicai.co), and try the API at [platform.publicai.co](https://platform.publicai.co) in a small hackathon or a local-language model evaluation.
- **Weeks 9-13**: carry out one piece of your action plan, for example an AI-literacy session with a library, school or nonprofit, and share a short write-up with the network.

The first Public AI chapter started at the University of Manchester. New chapters are welcome to build on that model and to improve the handbook.

Registration below is recognition and coordination, not incorporation or endorsement. Keep personal information to the minimum necessary.

## Register a chapter

<form id="chapter-form" class="chapter-form" method="POST" action="https://script.google.com/macros/s/AKfycbyuQxaAzDsZUNapNuJyoEE-OYN1JBzOJS0WJf3o6HHXJNvyg-qa7kR0J8q-H_BI8ybC/exec" novalidate>

  <div class="form-field" style="position: absolute; left: -9999px;" aria-hidden="true">
    <label for="website">Website</label>
    <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
  </div>

  <div class="form-field">
    <label for="university">University or institution</label>
    <input type="text" id="university" name="university" required>
  </div>

  <div class="form-field">
    <label for="country">Country</label>
    <input type="text" id="country" name="country" required>
  </div>

  <div class="form-field">
    <label for="chapter_name">Chapter or group name</label>
    <input type="text" id="chapter_name" name="chapter_name" required>
  </div>

  <div class="form-field">
    <label for="lead_name">Student coordinator name</label>
    <input type="text" id="lead_name" name="lead_name" required>
  </div>

  <div class="form-field">
    <label for="lead_email">Student coordinator email</label>
    <input type="email" id="lead_email" name="lead_email" required>
  </div>

  <div class="form-field">
    <label for="adviser_name">Faculty or staff adviser name</label>
    <input type="text" id="adviser_name" name="adviser_name" required>
  </div>

  <div class="form-field">
    <label for="adviser_email">Faculty or staff adviser email (optional)</label>
    <input type="email" id="adviser_email" name="adviser_email">
  </div>

  <div class="form-field">
    <label for="member_count">Number of members</label>
    <input type="number" id="member_count" name="member_count" min="3" required>
  </div>

  <div class="form-field">
    <label for="activities">Planned first-90-day activities</label>
    <textarea id="activities" name="activities" rows="5" required></textarea>
  </div>

  <div class="form-field">
    <label for="referral">How did you hear about us?</label>
    <input type="text" id="referral" name="referral" required>
  </div>

  <div class="form-field form-field-checkbox">
    <label for="consent">
      <input type="checkbox" id="consent" name="consent" required>
      I agree to be contacted by Public AI about this chapter registration.
    </label>
  </div>

  <p id="form-error" class="form-error" hidden>Please fill in all required fields, use a valid email address, and check the consent box before submitting.</p>
  <p id="form-success" class="form-success" hidden>Thank you for registering your chapter! We'll be in touch soon.</p>

  <button type="submit" class="button">Submit registration</button>

</form>

<script>
(function () {
  var form = document.getElementById('chapter-form');
  var error = document.getElementById('form-error');
  var success = document.getElementById('form-success');

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    var valid = true;

    var required = form.querySelectorAll('[required]');
    required.forEach(function (field) {
      if (field.type === 'checkbox') {
        if (!field.checked) valid = false;
      } else if (!field.value.trim()) {
        valid = false;
      }
    });

    if (form.lead_email.value && !isValidEmail(form.lead_email.value)) valid = false;
    if (form.adviser_email.value && !isValidEmail(form.adviser_email.value)) valid = false;

    if (Number(form.member_count.value) < 3) valid = false;

    if (!valid) {
      success.hidden = true;
      error.hidden = false;
      return;
    }

    error.hidden = true;

    var formData = new FormData(form);
    var body = new URLSearchParams(formData);

    fetch(form.action, {
      method: 'POST',
      mode: 'no-cors',
      body: body
    }).then(function () {
      error.hidden = true;
      success.hidden = false;
      form.reset();
    }).catch(function () {
      success.hidden = true;
      error.textContent = 'Something went wrong submitting your registration. Please try again in a moment.';
      error.hidden = false;
    });
  });
})();
</script>
