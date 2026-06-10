"""Comprehensive Charleston drayage quote form."""


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]
    email = ctx["email"]

    crumbs = [("Home", "/"), ("Request a quote", "")]

    hero = f"""
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Charleston drayage quote</span>
    <h1>Tell us about the move. We'll come back with a number.</h1>
    <p>Five fields gets you a number — the move, the box, and where to send the quote. Add detail if you have it; skip it if you don't. During business hours, you'll have a quote on your screen — usually inside an hour. Need to talk now? <a href="tel:{phone_tel}" style="color:#7ce5cb;">{phone_display}</a> or <a href="mailto:{email}" style="color:#7ce5cb;">{email}</a>.</p>
  </div>
</section>
"""

    form = f"""
<section class="quote-section">
  <div class="container">
    <form class="quote-form" action="/api/quote" method="POST" novalidate>
      <div aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;">
        <label>Don't fill this in: <input type="text" name="bot_field" tabindex="-1" autocomplete="off"></label>
      </div>

      <fieldset class="fieldset">
        <legend>The essentials</legend>
        <div class="row">
          <div class="field">
            <label for="line">Booking # / steamship line</label>
            <input id="line" name="line" type="text" placeholder="e.g. MAERSK / 1234567">
          </div>
          <div class="field">
            <label for="container_size">Container size &amp; type<span class="req">*</span></label>
            <select id="container_size" name="container_size" required>
              <option value="">Choose one</option>
              <option>20' Dry</option>
              <option>40' Dry</option>
              <option>40' High Cube</option>
              <option>45' High Cube</option>
              <option>20' Reefer</option>
              <option>40' Reefer</option>
              <option>Flat Rack</option>
              <option>Open Top</option>
              <option>ISO Tank</option>
              <option>Other</option>
            </select>
          </div>
        </div>
        <div class="row">
          <div class="field">
            <label for="terminal">Pickup terminal (or origin)<span class="req">*</span></label>
            <select id="terminal" name="terminal" required>
              <option value="">Choose one</option>
              <option>Wando Welch (USCHA)</option>
              <option>North Charleston (USNCH)</option>
              <option>Hugh Leatherman (USCHL)</option>
              <option>Columbus Street (USCST)</option>
              <option>Outside terminal — origin facility</option>
              <option>Not sure yet</option>
            </select>
          </div>
          <div class="field">
            <label for="delivery_zip">Delivery ZIP<span class="req">*</span></label>
            <input id="delivery_zip" name="delivery_zip" type="text" autocomplete="postal-code" inputmode="numeric" pattern="[0-9]{{5}}" required placeholder="29401">
          </div>
        </div>
        <div class="row full">
          <div class="field">
            <label for="email">Email — where the quote goes<span class="req">*</span></label>
            <input id="email" name="email" type="email" required autocomplete="email" placeholder="you@yourcompany.com">
          </div>
        </div>
      </fieldset>

      <details class="quote-optional">
        <summary>Add detail — optional, but it speeds up the quote</summary>
        <fieldset class="fieldset">
          <legend>Who you are</legend>
          <div class="row">
            <div class="field">
              <label for="name">Your name</label>
              <input id="name" name="name" type="text" autocomplete="name">
            </div>
            <div class="field">
              <label for="company">Company</label>
              <input id="company" name="company" type="text" autocomplete="organization">
            </div>
          </div>
          <div class="row">
            <div class="field">
              <label for="phone">Phone</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel">
            </div>
            <div class="field">
              <label for="role">What kind of customer are you?</label>
              <select id="role" name="role">
                <option value="">Choose one</option>
                <option>3PL / warehouse</option>
                <option>Freight forwarder</option>
                <option>Customs broker</option>
                <option>Direct importer or exporter</option>
                <option>Other</option>
              </select>
            </div>
          </div>
        </fieldset>

        <fieldset class="fieldset">
          <legend>The move</legend>
          <div class="row">
            <div class="field">
              <label for="move_type">Move type</label>
              <select id="move_type" name="move_type">
                <option value="">Choose one</option>
                <option>Import — port to consignee</option>
                <option>Export — origin to port</option>
                <option>Empty return only</option>
                <option>Pre-pull / yard storage</option>
                <option>Transload coordination</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field">
              <label for="container_count">Containers</label>
              <input id="container_count" name="container_count" type="number" min="1" value="1">
            </div>
          </div>
          <div class="row">
            <div class="field">
              <label for="pickup_zip">Pickup ZIP (if not terminal)</label>
              <input id="pickup_zip" name="pickup_zip" type="text" autocomplete="postal-code" inputmode="numeric" pattern="[0-9]{{5}}" placeholder="29405">
            </div>
            <div class="field">
              <label for="pickup_date">Estimated pickup date</label>
              <input id="pickup_date" name="pickup_date" type="date">
            </div>
          </div>
          <div class="row full">
            <div class="field">
              <label for="delivery_type">Delivery type</label>
              <select id="delivery_type" name="delivery_type">
                <option value="">Choose one</option>
                <option>Live unload</option>
                <option>Drop &amp; hook</option>
                <option>Transload yard</option>
                <option>Pier return / empty</option>
                <option>Other</option>
              </select>
            </div>
          </div>
        </fieldset>

        <fieldset class="fieldset">
          <legend>The cargo</legend>
          <div class="row three">
            <div class="field">
              <label for="commodity">Commodity</label>
              <input id="commodity" name="commodity" type="text" placeholder="e.g. apparel, ceramics, frozen poultry">
            </div>
            <div class="field">
              <label for="weight">Approx weight (lb)</label>
              <input id="weight" name="weight" type="number" min="0" placeholder="44000">
            </div>
            <div class="field">
              <label for="overweight">Overweight?</label>
              <select id="overweight" name="overweight">
                <option>No</option>
                <option>Yes</option>
                <option>Not sure</option>
              </select>
            </div>
          </div>
          <div class="row three">
            <div class="field">
              <label for="hazmat">Hazmat?</label>
              <select id="hazmat" name="hazmat">
                <option>No</option>
                <option>Yes</option>
              </select>
            </div>
            <div class="field">
              <label for="hazmat_un">UN# (if hazmat)</label>
              <input id="hazmat_un" name="hazmat_un" type="text" placeholder="e.g. UN1993">
            </div>
            <div class="field">
              <label for="reefer_setpoint">Reefer set point (if reefer)</label>
              <input id="reefer_setpoint" name="reefer_setpoint" type="text" placeholder="e.g. -10°F or +5°C">
            </div>
          </div>
          <div class="row full">
            <div class="field">
              <label for="notes">Anything else we should know?</label>
              <textarea id="notes" name="notes" placeholder="Customs broker contact, special equipment, dock instructions, multi-stop notes, ERD/VGM cuts for exports, anything else."></textarea>
            </div>
          </div>
        </fieldset>
      </details>

      <button type="submit" class="form-submit">Send my quote request</button>
      <p class="privacy-note">We don't share your information. We don't sell it. We'll only use it to quote and run your move. <a href="/privacy/">Privacy policy</a>.</p>
    </form>
  </div>
</section>
"""

    info = """
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">What happens after you submit</p><h2>The next 24 hours, in order.</h2></div>
    <div class="card-grid">
      <div class="card"><h3>1. We confirm receipt</h3><p>You'll get an automatic confirmation immediately, and a reply from a real dispatcher inside the hour during business hours.</p></div>
      <div class="card"><h3>2. We check the move</h3><p>Booking validity, terminal status, equipment availability, route. If we have questions we ask them once, not five times.</p></div>
      <div class="card"><h3>3. You get a number</h3><p>An itemized quote with linehaul, chassis, fuel, and any predictable accessorials. Plain English.</p></div>
      <div class="card"><h3>4. You decide</h3><p>If it's a yes, we book the appointment and run the move. If you have questions, we'll talk through them. No pressure.</p></div>
    </div>
  </div>
</section>
"""

    body = breadcrumb_bar(crumbs) + hero + form + info + cta_banner(
        title="Prefer to call?",
        sub=f"Dispatch is reachable at {phone_display}. Or email greg@catefreight.com — both go to a human."
    )

    schema = [{
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "name": "Request a Charleston drayage quote",
        "url": f"{site_url}/quote/",
    }]

    html = render(
        slug="quote",
        path="/quote/",
        title="Request a Charleston Drayage Quote | Cate Freight",
        meta_description="Send Cate Freight a Charleston drayage quote request. Booking, container, terminal, delivery ZIP — we'll come back with a number, usually inside an hour during business hours.",
        h1="Tell us about the move. We'll come back with a number.",
        body_html=body,
        breadcrumbs=crumbs,
        schema=schema,
    )

    # ---------- /thank-you/ post-submit page ---------- #
    ty_crumbs = [("Home", "/"), ("Quote received", "")]
    ty_hero = f"""
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Quote request received</span>
    <h1>Got it. Your quote is on the way.</h1>
    <p>Your request landed in dispatch. During business hours, you'll have a number on screen — usually inside the hour. After hours and weekends, first thing the next business morning. If a container is already on the demurrage clock, call <a href="tel:{phone_tel}" style="color:#7ce5cb;">{phone_display}</a> and we'll work it now.</p>
  </div>
</section>
"""
    ty_next = """
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">What happens next</p><h2>Three steps, in order.</h2></div>
    <div class="card-grid">
      <div class="card"><h3>1. Dispatcher reviews the move</h3><p>Booking validity, terminal status, equipment availability, route. If we have a question, we ask it once — by reply email — not five times.</p></div>
      <div class="card"><h3>2. You get an itemized number</h3><p>Linehaul, chassis, fuel, and any predictable accessorials, in plain English. No surprise per-line charges added later.</p></div>
      <div class="card"><h3>3. You decide</h3><p>If it's a yes, we book the appointment and run the move. If it's a maybe, we'll talk it through. No pressure either way.</p></div>
    </div>
  </div>
</section>
"""
    ty_resources = """
<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">While you wait</p><h2>A few things worth reading.</h2></div>
    <div class="card-grid">
      <div class="card"><h3>The drayage quote checklist</h3><p>The exact information a Charleston drayage carrier needs from you to come back with a usable number on the first try.</p><a class="card-link" href="/resources/drayage-quote-checklist/">Read the checklist</a></div>
      <div class="card"><h3>Avoid demurrage and detention</h3><p>What demurrage, detention, and per diem actually are, who charges them at SCPA, and how to stop the clock fastest.</p><a class="card-link" href="/resources/avoid-demurrage-detention/">Read the guide</a></div>
      <div class="card"><h3>Charleston port drayage guide</h3><p>A practical reference covering all three SCPA terminals — Wando Welch, North Charleston, Hugh Leatherman — and the operational rules that go with each.</p><a class="card-link" href="/resources/charleston-port-drayage-guide/">Open the guide</a></div>
    </div>
  </div>
</section>
"""
    ty_body = breadcrumb_bar(ty_crumbs) + ty_hero + ty_next + ty_resources + cta_banner(
        title="Need to talk to dispatch right now?",
        sub=f"Call {phone_display} or email greg@catefreight.com — both go to a human."
    )
    ty_html = render(
        slug="thank-you",
        path="/thank-you/",
        title="Quote request received | Cate Freight",
        meta_description="Your Charleston drayage quote request was received. A dispatcher replies within the hour during business hours.",
        h1="Got it. Your quote is on the way.",
        body_html=ty_body,
        breadcrumbs=ty_crumbs,
        no_index=True,
    )

    return [
        ("/quote/index.html", html),
        ("/thank-you/index.html", ty_html),
    ]
