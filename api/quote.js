// api/quote.js — Cate Freight quote handler.
//
// Receives a POST from /quote/, validates, sends an email to dispatch via
// Resend, then 303-redirects the browser to /thank-you/. Replaces Formspree.
//
// Required Vercel environment variables:
//   RESEND_API_KEY     Resend API key (https://resend.com/api-keys)
//
// Optional Vercel environment variables:
//   QUOTE_TO_EMAIL     Inbox where quote requests land.
//                      Default: greg@catefreight.com
//   QUOTE_FROM_EMAIL   Verified sender. Default: 'Cate Freight Quotes <onboarding@resend.dev>'
//                      For production, verify catefreight.com on Resend and set this to e.g.
//                      'Cate Freight Quotes <quotes@catefreight.com>'.

const REQUIRED_FIELDS = [
  'name', 'company', 'email', 'phone',
  'move_type', 'container_size', 'terminal', 'delivery_zip',
];

const FIELD_ORDER = [
  'name', 'company', 'email', 'phone', 'role',
  'move_type', 'container_count', 'container_size',
  'terminal', 'pickup_zip', 'delivery_zip',
  'delivery_type', 'pickup_date',
  'line', 'commodity',
  'weight', 'overweight', 'hazmat', 'hazmat_un', 'reefer_setpoint',
  'notes',
];

const FIELD_LABELS = {
  name: 'Name',
  company: 'Company',
  email: 'Email',
  phone: 'Phone',
  role: 'Customer type',
  move_type: 'Move type',
  container_count: 'Containers',
  container_size: 'Container size & type',
  terminal: 'Pickup terminal',
  pickup_zip: 'Pickup ZIP',
  delivery_zip: 'Delivery ZIP',
  delivery_type: 'Delivery type',
  pickup_date: 'Pickup date',
  line: 'Steamship / booking #',
  commodity: 'Commodity',
  weight: 'Approx weight (lb)',
  overweight: 'Overweight?',
  hazmat: 'Hazmat?',
  hazmat_un: 'UN# (hazmat)',
  reefer_setpoint: 'Reefer set point',
  notes: 'Notes',
};

function escapeHtml(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function parseBodyIfNeeded(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') {
    try { return Object.fromEntries(new URLSearchParams(req.body)); }
    catch { return {}; }
  }
  return {};
}

function htmlError(res, status, title, body) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.end(`<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeHtml(title)} | Cate Freight</title></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:560px;margin:60px auto;padding:0 20px;color:#0f2a3f;line-height:1.55;">
<h1 style="font-size:28px;margin:0 0 16px;">${escapeHtml(title)}</h1>
${body}
<p style="margin-top:32px;"><a href="/quote/" style="color:#1ea889;font-weight:600;">Return to the quote form</a></p>
</body></html>`);
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return htmlError(res, 405, 'Method not allowed',
      '<p>This endpoint only accepts POST submissions from the quote form.</p>');
  }

  const body = parseBodyIfNeeded(req);

  // Honeypot. Bots fill every field; humans never see this one.
  if (body.bot_field && body.bot_field.toString().trim()) {
    res.statusCode = 303;
    res.setHeader('Location', '/thank-you/');
    return res.end();
  }

  // Required-field validation.
  const missing = REQUIRED_FIELDS.filter(
    (f) => !(body[f] && body[f].toString().trim())
  );
  if (missing.length) {
    const labels = missing.map((f) => FIELD_LABELS[f] || f).join(', ');
    return htmlError(res, 400, "We're missing a few fields",
      `<p>The form needs: <strong>${escapeHtml(labels)}</strong>.</p>`);
  }

  // Email shape check.
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(body.email.toString().trim())) {
    return htmlError(res, 400, 'Email looks off',
      '<p>Double-check the email address and resubmit.</p>');
  }

  const apiKey = process.env.RESEND_API_KEY;
  const toEmail = process.env.QUOTE_TO_EMAIL || 'greg@catefreight.com';
  const fromEmail = process.env.QUOTE_FROM_EMAIL || 'Cate Freight Quotes <onboarding@resend.dev>';

  if (!apiKey) {
    console.error('RESEND_API_KEY missing');
    return htmlError(res, 500, "Quote couldn't be delivered",
      '<p>We had a config issue on our end. Please call dispatch at <a href="tel:+18439987820" style="color:#1ea889;">(843) 998-7820</a> so we don\'t lose your move.</p>');
  }

  // Build email.
  const lines = [];
  const rows = [];
  for (const k of FIELD_ORDER) {
    const v = (body[k] ?? '').toString().trim();
    if (!v) continue;
    lines.push(`${FIELD_LABELS[k]}: ${v}`);
    rows.push(
      `<tr><td style="padding:6px 16px 6px 0;color:#666;vertical-align:top;white-space:nowrap;">${escapeHtml(FIELD_LABELS[k])}</td><td style="padding:6px 0;">${escapeHtml(v).replace(/\n/g, '<br>')}</td></tr>`
    );
  }

  const subject = `New Charleston drayage quote — ${body.company || body.name} — ${body.move_type}`;
  const text = lines.join('\n');
  const html = `<p style="font-family:-apple-system,sans-serif;">New drayage quote request via catefreight.com.</p>
<table style="border-collapse:collapse;font-family:-apple-system,sans-serif;font-size:14px;">${rows.join('')}</table>
<p style="font-family:-apple-system,sans-serif;color:#666;margin-top:16px;font-size:13px;">Reply to this email to respond directly to the customer.</p>`;

  try {
    const resp = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [toEmail],
        reply_to: body.email.toString().trim(),
        subject,
        text,
        html,
      }),
    });
    if (!resp.ok) {
      const errBody = await resp.text();
      console.error('Resend non-2xx', resp.status, errBody);
      return htmlError(res, 502, "Quote couldn't be delivered",
        '<p>Email service returned an error. Please call dispatch at <a href="tel:+18439987820" style="color:#1ea889;">(843) 998-7820</a> or email <a href="mailto:greg@catefreight.com" style="color:#1ea889;">greg@catefreight.com</a>.</p>');
    }
  } catch (err) {
    console.error('Email send failed', err);
    return htmlError(res, 502, "Quote couldn't be delivered",
      '<p>Network error contacting our email provider. Please call dispatch at <a href="tel:+18439987820" style="color:#1ea889;">(843) 998-7820</a>.</p>');
  }

  res.statusCode = 303;
  res.setHeader('Location', '/thank-you/');
  res.end();
};
