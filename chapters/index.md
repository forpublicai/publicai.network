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

- **Days 1-30**: hold an orientation workshop and demonstrate [chat.publicai.co](https://chat.publicai.co).
- **Days 31-60**: run a hackathon using the API at [platform.publicai.co](https://platform.publicai.co), and start a local-language model evaluation.
- **Days 61-90**: volunteer with a library, school, or nonprofit to teach AI literacy, then publish a short report.

Registration below is recognition and coordination, not incorporation or endorsement. Keep personal information to the minimum necessary.

## Register a chapter

<form id="chapter-form" class="chapter-form" method="POST" action="CONFIG_FORM_ACTION_URL" novalidate>

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

  <button type="submit" class="button">Submit registration</button>

</form>

<script>
(function () {
  var form = document.getElementById('chapter-form');
  var error = document.getElementById('form-error');

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  form.addEventListener('submit', function (event) {
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
      event.preventDefault();
      error.hidden = false;
    } else {
      error.hidden = true;
    }
  });
})();
</script>
