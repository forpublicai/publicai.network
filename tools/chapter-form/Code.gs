var SHEET_NAME = 'Sheet1';
var REQUIRED_FIELDS = [
  'university', 'country', 'chapter_name', 'lead_name', 'lead_email',
  'adviser_name', 'member_count', 'activities', 'referral', 'consent'
];
var FIELD_ORDER = [
  'university', 'country', 'chapter_name', 'lead_name', 'lead_email',
  'adviser_name', 'adviser_email', 'member_count', 'activities', 'referral', 'consent'
];
var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
var MAX_LEN = 2000;

function doPost(e) {
  var params = (e && e.parameter) || {};

  if (params.website) {
    return jsonResponse({ ok: true });
  }

  for (var i = 0; i < REQUIRED_FIELDS.length; i++) {
    var key = REQUIRED_FIELDS[i];
    if (!params[key] || String(params[key]).trim() === '') {
      return jsonResponse({ ok: false, error: 'missing_field', field: key });
    }
  }

  if (!EMAIL_RE.test(params.lead_email)) {
    return jsonResponse({ ok: false, error: 'invalid_email', field: 'lead_email' });
  }
  if (params.adviser_email && !EMAIL_RE.test(params.adviser_email)) {
    return jsonResponse({ ok: false, error: 'invalid_email', field: 'adviser_email' });
  }

  var row = [new Date()];
  for (var j = 0; j < FIELD_ORDER.length; j++) {
    var value = params[FIELD_ORDER[j]] || '';
    row.push(String(value).substring(0, MAX_LEN));
  }

  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  sheet.appendRow(row);

  return jsonResponse({ ok: true });
}

function jsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
