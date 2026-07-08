"""Charleston Drayage — primary SEO wedge."""

def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    faq_block = ctx["faq_block"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]
    email = ctx["email"]

    crumbs = [("Home", "/"), ("Charleston Drayage", "")]

    hero = f"""
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Charleston, SC</span>
    <h1>Charleston drayage, run by people who know what a release looks like before they roll a truck.</h1>
    <p>We pull import and export containers out of every SCPA container terminal — Wando Welch, North Charleston, and Hugh Leatherman — and run them to warehouses, transload yards, and consignees across South Carolina and the Southeast. Cate Freight is built to make Charleston drayage feel boring on purpose. Booking in. Container moves. POD back same day.</p>
    <div class="actions">
      <a class="btn btn-primary" href="/quote/">Request a Charleston drayage quote</a>
      <a class="btn btn-ghost" href="tel:{phone_tel}">{phone_display} dispatch</a>
    </div>
    <div class="meta-row">
      <span>USCHA — Wando Welch</span>
      <span>USNCH — North Charleston</span>
      <span>USCHL — Hugh Leatherman</span>
    </div>
  </div>
</section>
"""

    intro = """
<section class="section">
  <div class="container narrow">
    <div class="kpi-row">
      <div class="kpi"><strong>3</strong><span>SCPA terminals</span></div>
      <div class="kpi"><strong>52'</strong><span>Deepest E.C. harbor</span></div>
      <div class="kpi"><strong>60 min</strong><span>Avg quote turn</span></div>
      <div class="kpi"><strong>24/7</strong><span>Email coverage</span></div>
    </div>
    <div class="prose">
      <h2>The Port of Charleston: built for drayage</h2>
      <p>Charleston is the second-largest container port on the East Coast and the only major one without on-dock or near-dock rail (the Navy Base Intermodal Facility is finally arriving in 2026, but until then drayage is the only mode that moves a Charleston container). That makes Charleston a drayage town in a way Norfolk, Savannah, and New York are not.</p>
      <p>It also means the ground game matters. The carrier who knows which gate is moving today, which chassis pool is closest to your container, and when SCPA has a holiday "no work day" that doesn't accrue free time — that carrier saves you real money. Cate Freight is built to be that carrier.</p>
    </div>
  </div>
</section>
"""

    services = """
<section class="section bg-surface">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Charleston drayage services</p>
      <h2>Every drayage move that goes through Charleston, we do.</h2>
    </div>
    <div class="card-grid">
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-anchor"/></svg></div><h3>Port pickup &amp; return</h3><p>Loaded import pickup and empty returns at all three SCPA terminals.</p><a class="card-link" href="/services/port-drayage/">Port drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-import"/></svg></div><h3>Import container drayage</h3><p>Release-checked imports from Charleston to your DC, dock, or transload.</p><a class="card-link" href="/services/import-container-drayage/">Import drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-export"/></svg></div><h3>Export container drayage</h3><p>Loaded export delivery to terminal, ERD-aware scheduling, VGM coordination.</p><a class="card-link" href="/services/export-container-drayage/">Export drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-warehouse"/></svg></div><h3>Port-to-warehouse</h3><p>Direct moves from terminal to warehouse with appointments confirmed at both ends.</p><a class="card-link" href="/services/port-to-warehouse-drayage/">Port-to-warehouse</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-transload"/></svg></div><h3>Transload &amp; coordination</h3><p>Container delivery to a transload yard plus the warehouse coordination.</p><a class="card-link" href="/services/transload-drayage/">Transload</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-clock"/></svg></div><h3>Pre-pull service</h3><p>Pull from the terminal early to stop the demurrage clock when free time is tight.</p><a class="card-link" href="/services/import-container-drayage/#pre-pull">Pre-pull info</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-snowflake"/></svg></div><h3>Reefer drayage</h3><p>Genset chassis, set-point verification, pre-trip inspection on every move.</p><a class="card-link" href="/services/reefer-drayage/">Reefer</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-weight"/></svg></div><h3>Overweight &amp; OOG</h3><p>Tri-axle chassis, route permits, and the experience to handle 60,000+ lb containers.</p><a class="card-link" href="/services/overweight-drayage/">Overweight</a></div>
    </div>
  </div>
</section>
"""

    coverage = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Charleston coverage area</p>
      <h2>Local Charleston drays plus regional Southeast lanes.</h2>
      <p class="lead" style="margin: 0 auto;">Most of our work is local Charleston drayage. We also run regional lanes inside South Carolina and into Georgia and the Carolinas. If your delivery ZIP is east of the Mississippi, we can probably get it there.</p>
    </div>
    <div class="split-2">
      <div>
        <h3>Local Charleston drayage zones</h3>
        <ul class="checklist">
          <li>Charleston &amp; downtown peninsula</li>
          <li>North Charleston, Hanahan, Goose Creek, Ladson</li>
          <li>Mount Pleasant, Daniel Island, Cainhoy</li>
          <li>Summerville, Lincolnville, Moncks Corner</li>
          <li>Ravenel, Hollywood, Adams Run</li>
          <li>James Island &amp; Johns Island</li>
          <li>Walterboro, Yemassee, St. George</li>
        </ul>
      </div>
      <div>
        <h3>Regional Southeast lanes we run</h3>
        <ul class="checklist">
          <li>Columbia, Cayce, Lexington, Lugoff</li>
          <li>Greenville, Spartanburg, Anderson, Inman</li>
          <li>Florence, Darlington, Hartsville</li>
          <li>Hilton Head, Bluffton, Beaufort</li>
          <li>Savannah, Augusta, Atlanta metro</li>
          <li>Charlotte, Concord, Gastonia, Statesville</li>
          <li>Wilmington NC, Fayetteville NC</li>
        </ul>
      </div>
    </div>
    <h3 style="margin-top: 2rem;">Port-to-door drayage within about 250 miles of Charleston</h3>
    <p>Every lane above is a <strong>port-to-door drayage</strong> move: we pull the loaded container at Wando Welch, North Charleston, or Hugh Leatherman, deliver it to your dock, and return the empty to the terminal — one round-trip container movement, one driver, one rate. Inside roughly 250 road miles of the Port of Charleston, keeping freight in the ocean container is usually the cheapest way to move it: Columbia and the Midlands up <strong>I-26</strong>, Greenville–Spartanburg where I-26 meets <strong>I-85</strong>, Charlotte via <strong>I-77</strong>, Augusta on <strong>I-20</strong>, and Savannah down <strong>US-17/I-95</strong> all sit inside that radius. Past it, ocean per-diem and chassis days start losing to domestic truck rates, and a <a href="/services/transload-drayage/">Charleston transload</a> onto a 53' van usually wins — we'll do the math both ways on any quote. For the local leg itself, see <a href="/services/port-to-warehouse-drayage/">port-to-warehouse drayage</a>.</p>
    <div class="callout">
      <strong>Don't see your destination?</strong> Send us the ZIP. If it's a one-off we don't run regularly, we'll either quote it directly or hand you a clean referral to a carrier who does. We don't pretend to cover lanes we can't run well.
    </div>
  </div>
</section>
"""

    pricing = """
<section class="section bg-surface">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How Charleston drayage pricing works</p>
      <h2>The line items that matter, explained.</h2>
      <p class="lead" style="margin: 0 auto;">Charleston drayage rates aren't one number. Here are the components that show up on every quote, and how Cate Freight handles each.</p>
    </div>
    <div class="card-grid">
      <div class="card"><h3>Base linehaul</h3><p>The drive itself, terminal to delivery and back. Driven by mileage, wait time, and equipment type. Set up front in your quote.</p></div>
      <div class="card"><h3>Chassis</h3><p>Daily chassis usage — TRAC, DCLI, or Flexi-Van. We avoid chassis split fees by routing to the depot that carries your line.</p></div>
      <div class="card"><h3>Fuel surcharge</h3><p>Indexed to DOE diesel prices, refreshed weekly. Fuel is a line item, not a hidden markup.</p></div>
      <div class="card"><h3>Detention &amp; per diem</h3><p>Pass-through only. We tell you when the clock starts and we work hard to stop it. Live unloads are scheduled to fit free time.</p></div>
      <div class="card"><h3>Pre-pull &amp; storage</h3><p>If your dock isn't ready, we pre-pull and store. Quoted as a single package so you see the trade vs. demurrage.</p></div>
      <div class="card"><h3>Permits &amp; specialty</h3><p>Overweight permits, hazmat handling, OOG escort. Quoted up front when known. No surprise lines.</p></div>
    </div>
    <div class="callout warning">
      <strong>Watch out for:</strong> Carriers that quote a low base and load up the invoice with chassis splits, fuel multipliers, and "admin fees" you didn't see coming. Ask any quote — ours included — for an itemized rundown. If you can't get one, that's your answer.
    </div>
  </div>
</section>
"""

    why = """
<section class="section">
  <div class="container">
    <div class="feature-row">
      <div>
        <p class="eyebrow">Why customers stay</p>
        <h2>Smaller, sharper, and built around the receiver.</h2>
        <p>Charleston has good drayage carriers. It also has a lot of bad ones. The bad ones don't check releases, can't reach a dispatcher after 4 PM, and don't email PODs back without three follow-ups. We were built to be the opposite of that.</p>
        <p>The advantage is operational, not magical. Cate Freight came out of the warehouse and 3PL world. We know what a clean ASN looks like, what a customs broker needs back, and what a dock manager wishes drayage drivers understood. That experience is the whole differentiator.</p>
        <a class="btn btn-outline" href="/about/">More about us</a>
      </div>
      <div class="panel">
        <h3>What "operationally sharp" actually means</h3>
        <ul>
          <li><div><strong>Release verification</strong><span>Customs, freight, and line holds checked before dispatch.</span></div></li>
          <li><div><strong>Live terminal status</strong><span>Gate moves and chassis pool tracked daily.</span></div></li>
          <li><div><strong>Quote within an hour</strong><span>Business hours. Off hours, by next morning.</span></div></li>
          <li><div><strong>Same-day POD</strong><span>Signed BOL imaged, named, emailed.</span></div></li>
          <li><div><strong>Honest accessorials</strong><span>Chassis, fuel, OW permits — all up front.</span></div></li>
          <li><div><strong>One dispatcher per file</strong><span>You don't get bounced. You get a person.</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    compare = """
<section class="section bg-surface">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Shopping the market</p>
      <h2>How to compare drayage companies in Charleston, SC.</h2>
      <p class="lead" style="margin: 0 auto;">Most drayage companies in Charleston will tell you they cover all three SCPA terminals and quote fast. The differences show up on the invoice and in the inbox. Grade any carrier — us included — on these five checks before you tender a container.</p>
    </div>
    <div class="card-grid">
      <div class="card"><h3>Release discipline</h3><p>Ask when they verify customs, freight, and line holds. "At dispatch" means a truck can roll to Wando Welch for a box that isn't released — and you pay for the dry run.</p></div>
      <div class="card"><h3>Chassis pool access</h3><p>A carrier without interchange access to your line's pool — TRAC, DCLI, or Flexi-Van — eats a chassis split fee on every move and passes it to you.</p></div>
      <div class="card"><h3>Itemized accessorials</h3><p>Get the linehaul, fuel percentage, chassis day rate, and pre-pull cost as separate lines before you book. A single blended number hides the markup.</p></div>
      <div class="card"><h3>POD turnaround</h3><p>Same-day signed POD should be standard, not a favor. If closing a file takes three follow-up emails, that cost lands on your ops team every week.</p></div>
      <div class="card"><h3>Dispatch reachability</h3><p>Call the dispatch line at 4:30 PM before you sign up. Whoever answers — or doesn't — is who you'll be calling when a container hits detention on a Friday.</p></div>
      <div class="card"><h3>Put it to work</h3><p>The full 11-point version of this checklist is in our guide to <a href="/resources/choosing-a-drayage-carrier-3pl/">choosing a Charleston drayage carrier</a> — or skip ahead and <a href="/quote/">grade us on a live quote</a>.</p></div>
    </div>
  </div>
</section>
"""

    faq_html, faq_schema = faq_block([
        ("What is Charleston drayage?",
         "Charleston drayage is the trucking of ocean shipping containers between the SCPA terminals at the Port of Charleston (Wando Welch, North Charleston, and Hugh Leatherman) and a nearby destination — typically a warehouse, transload facility, or a shipper's loading dock. Drayage is what moves a container its 'last mile' on or off the port."),
        ("How much does Charleston drayage cost?",
         "A Charleston local dray (terminal to a Charleston-metro consignee) is generally a few hundred dollars before accessorials, with the exact number depending on the destination ZIP, container size, weight, and any specialty handling. Regional drays into Columbia, Greenville, Charlotte, or Savannah are quoted by mileage. Send your booking and delivery ZIP for a real number."),
        ("Which Charleston terminals does Cate Freight cover?",
         "All three SCPA container terminals: Wando Welch in Mount Pleasant, North Charleston Terminal on the former Navy base, and the Hugh Leatherman Terminal in North Charleston. We also work Columbus Street when needed for breakbulk and RoRo."),
        ("Can you drayage overweight containers from Charleston?",
         "Yes. We run tri-axle chassis configurations and pull state-issued overweight permits where required. Overweight drays are quoted up front including the permit cost so there are no surprise line items."),
        ("Do you handle reefer drayage in Charleston?",
         "Yes. We run reefer drays with genset chassis, verified set points on pickup, and a pre-trip inspection. Reefer set point and supply temperature are confirmed at pickup and again at delivery, then noted on the POD."),
        ("How quickly can you pick up a container from a Charleston terminal?",
         "Same-day pickup is possible if the container is released and the booking is in our hands by mid-morning. Next-day pickup is the norm. Pre-pull service is available when free time is tight or your dock isn't ready."),
    ])

    body = (
        breadcrumb_bar(crumbs)
        + hero
        + intro
        + services
        + coverage
        + pricing
        + why
        + compare
        + faq_html
        + cta_banner(title="Quote a Charleston drayage move", sub="Booking, terminal, delivery ZIP — that's all we need to start.")
    )

    # The Organization entity ({SITE_URL}/#org) is emitted on every page by
    # render() via ORG_SCHEMA in build.py — no need to define it inline here.
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Charleston Drayage",
        "serviceType": "Container drayage",
        "provider": {"@id": f"{site_url}/#org"},
        "areaServed": [
            {"@type": "City", "name": "Charleston, SC"},
            {"@type": "City", "name": "North Charleston, SC"},
            {"@type": "City", "name": "Mount Pleasant, SC"},
            {"@type": "City", "name": "Summerville, SC"},
            {"@type": "City", "name": "Goose Creek, SC"},
            {"@type": "City", "name": "Hanahan, SC"},
            {"@type": "City", "name": "Ladson, SC"},
            {"@type": "City", "name": "Moncks Corner, SC"},
        ],
        "audience": {
            "@type": "BusinessAudience",
            "audienceType": "3PLs, freight forwarders, customs brokers, and direct importers",
        },
        "description": "Container drayage between the SCPA terminals at the Port of Charleston — Wando Welch (USCHA), North Charleston (USNCH), and Hugh Leatherman (USCHL) — and warehouses, transload facilities, and consignees in South Carolina and the Southeast.",
    }
    schema = [service_schema, faq_schema]

    html = render(
        slug="charleston-drayage",
        path="/charleston-drayage/",
        title="Charleston Drayage Carrier | SCPA Terminals | Cate Freight",
        meta_description="Charleston drayage carrier covering all three SCPA terminals — Wando Welch, North Charleston, Hugh Leatherman. Releases checked, quote in under an hour.",
        h1="Charleston drayage, run by people who know what a release looks like before they roll a truck.",
        body_html=body,
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="charleston-drayage",
    )
    return ("/charleston-drayage/index.html", html)
