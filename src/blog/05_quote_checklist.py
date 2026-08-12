"""Article: The drayage quote checklist."""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("Drayage quote checklist", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Operational checklist &middot; 5 min read</span>
    <h1>The drayage quote checklist for importers.</h1>
    <p>The exact information a <a href="/charleston-drayage/">Charleston drayage</a> carrier needs from you to come back with a usable number on the first try.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Published April 2026 &middot; Cate Freight Charleston operations team</p>

      <p>If you've ever sent a drayage carrier "can you quote a 40' import?" and gotten a four-question reply asking for everything else, this checklist is for you. Send all of this in your first email and most carriers can quote inside an hour. Send three of these and you'll be waiting on a back-and-forth thread.</p>

      <h2>The minimum-viable quote request</h2>
      <p>The faster path to a real number, with the absolute minimum data:</p>
      <ol>
        <li><strong>Booking number or MBL.</strong> So we can check release status and validate the booking.</li>
        <li><strong>Container size.</strong> 20', 40', 40HC, 45HC.</li>
        <li><strong>Pickup terminal.</strong> Wando Welch, North Charleston, or Hugh Leatherman (or "not sure yet" — we can look it up).</li>
        <li><strong>Delivery ZIP.</strong> Final destination ZIP code.</li>
      </ol>
      <p>Those four data points give us 80% of what we need to quote. We can do it. But the quote is faster, more accurate, and less likely to need adjusting if you also include:</p>

      <h2>The full checklist</h2>
      <h3>About the move</h3>
      <ul>
        <li>Move type (import, export, empty return, pre-pull only)</li>
        <li>Container size and type (20'/40'/40HC, dry/reefer/flat-rack/open-top/ISO tank)</li>
        <li>Number of containers</li>
        <li>Pickup terminal (Wando Welch USCHA, North Charleston USNCH, Hugh Leatherman USCHL)</li>
        <li>Pickup ZIP (only if origin isn't a terminal — for <a href="/services/export-container-drayage/">export container drayage</a>)</li>
        <li>Delivery ZIP and address</li>
        <li>Delivery type (live unload, drop &amp; hook, transload, pier return)</li>
        <li>Estimated container availability or pickup date</li>
      </ul>

      <h3>About the cargo</h3>
      <ul>
        <li>Steamship line</li>
        <li>Booking number / MBL</li>
        <li>Commodity (general description is fine)</li>
        <li>Approximate weight in pounds</li>
        <li>Overweight? (yes/no/not sure — we can advise if not sure; anything grossing over 80,000 lbs on the road runs as <a href="/services/overweight-drayage/">overweight container drayage</a> with a permit)</li>
        <li>Hazmat? With UN# and PG (packing group) if yes</li>
        <li>Set point and supply temperature, if the box moves as <a href="/services/reefer-drayage/">reefer drayage</a></li>
      </ul>

      <h3>About the timing</h3>
      <ul>
        <li>For imports: when does the container arrive at SCPA, what's free time look like, what's the dock readiness at the consignee</li>
        <li>For exports: ERD (earliest receiving date), cargo cut, VGM cut</li>
      </ul>

      <h3>About the parties</h3>
      <ul>
        <li>Customs broker contact (for imports)</li>
        <li>Consignee contact (for delivery scheduling)</li>
        <li>Your file reference, PO number, or whatever ID you want us to use on the BOL and POD</li>
      </ul>

      <h2>Why this matters</h2>
      <p>Drayage quoting isn't just plugging mileage into a calculator. Every one of the items above changes either the rate, the equipment we need, or the timing of how we run the move. Missing fields produce one of three outcomes:</p>
      <ul>
        <li>The carrier asks five follow-up questions, slowing you down by 24-48 hours.</li>
        <li>The carrier guesses, quotes a number that's wrong, and has to revise once you book.</li>
        <li>The carrier quotes wide to cover their risk — i.e., higher than they would have on a tight quote.</li>
      </ul>
      <p>None of those serves you. Send the full set and the carrier can give you a sharp, accurate number on the first pass.</p>

      <h2>Cate Freight's quote form</h2>
      <p>Our <a href="/quote/">quote form</a> is structured around exactly this checklist. Fill it out completely and you'll have an itemized number on your screen, usually inside an hour during business hours. If you'd rather email it, send to greg@catefreight.com — same fields, same speed.</p>
    </article>
  </div>
</section>

<section class="section faq">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">People also ask</p>
      <h2>Drayage quote questions</h2>
    </div>
    <div class="faq-list">
      <details class="faq-item"><summary>What information do I need to get a drayage quote?</summary><div class="faq-answer">Four data points get you a workable number: the booking number or MBL, the container size (20', 40', 40HC, 45HC), the pickup terminal, and the delivery ZIP code. A complete request adds move type, delivery type (live unload vs. drop &amp; hook), commodity, approximate weight, and any specialty flags — overweight, hazmat, or reefer. Our <a href="/quote/">quote form</a> is structured around exactly these fields.</div></details>
      <details class="faq-item"><summary>How long does a drayage quote take in Charleston?</summary><div class="faq-answer">With a complete request — booking number, container size, terminal, delivery ZIP, weight, and specialty flags — a <a href="/charleston-drayage/">Charleston drayage</a> carrier can typically quote inside an hour during business hours. An incomplete request triggers follow-up questions that add 24-48 hours of back-and-forth before you see a number.</div></details>
      <details class="faq-item"><summary>What drives the cost of a drayage quote?</summary><div class="faq-answer">The base rate is driven by the pickup terminal and the delivery ZIP. On top of that, accessorials move the total: overweight permits and tri-axle equipment, chassis splits when the depot doesn't hold your steamship line's chassis pool, hazmat handling, genset fuel for reefer moves, and detention if the live unload runs long. A carrier quoting without the weight, commodity, and delivery-type fields either quotes wide to cover risk or revises after booking.</div></details>
      <details class="faq-item"><summary>When is a container overweight for drayage?</summary><div class="faq-answer">When the loaded container, chassis, and tractor together gross over 80,000 lbs on the road, the move runs as <a href="/services/overweight-drayage/">overweight container drayage</a> — tri-axle chassis, an overweight permit, and route planning around bridge and road weight limits. Flag the approximate cargo weight on the quote request; if you're not sure whether it's over, say so and the carrier can advise.</div></details>
      <details class="faq-item"><summary>Do I need to know my pickup terminal before requesting a quote?</summary><div class="faq-answer">No. If you have the booking number or MBL, the carrier can look up which SCPA terminal the container routes through — Wando Welch, North Charleston, or Hugh Leatherman. Mark it "not sure yet" on the request. <a href="/services/port-drayage/">Port drayage</a> rates from the three container terminals differ, so the quote firms up once the terminal is confirmed.</div></details>
      <details class="faq-item"><summary>What are ERD, cargo cut, and VGM cut on an export quote?</summary><div class="faq-answer">Three deadlines that frame every <a href="/services/export-container-drayage/">export container drayage</a> move. ERD is the earliest receiving date — the first day the terminal accepts your loaded export. Cargo cut is the last day it accepts the loaded box for that vessel. VGM cut is the deadline to file the verified gross mass. Include all three in the quote request so the carrier can schedule the loading and terminal return inside the window.</div></details>
    </div>
  </div>
</section>
"""

    faq_items = [
        ("What information do I need to get a drayage quote?", "Four data points get you a workable number: the booking number or MBL, the container size (20', 40', 40HC, 45HC), the pickup terminal, and the delivery ZIP code. A complete request adds move type, delivery type (live unload vs. drop & hook), commodity, approximate weight, and any specialty flags — overweight, hazmat, or reefer."),
        ("How long does a drayage quote take in Charleston?", "With a complete request — booking number, container size, terminal, delivery ZIP, weight, and specialty flags — a Charleston drayage carrier can typically quote inside an hour during business hours. An incomplete request triggers follow-up questions that add 24-48 hours of back-and-forth before you see a number."),
        ("What drives the cost of a drayage quote?", "The base rate is driven by the pickup terminal and the delivery ZIP. On top of that, accessorials move the total: overweight permits and tri-axle equipment, chassis splits when the depot doesn't hold your steamship line's chassis pool, hazmat handling, genset fuel for reefer moves, and detention if the live unload runs long. A carrier quoting without the weight, commodity, and delivery-type fields either quotes wide to cover risk or revises after booking."),
        ("When is a container overweight for drayage?", "When the loaded container, chassis, and tractor together gross over 80,000 lbs on the road, the move runs as overweight container drayage — tri-axle chassis, an overweight permit, and route planning around bridge and road weight limits. Flag the approximate cargo weight on the quote request; if you're not sure whether it's over, say so and the carrier can advise."),
        ("Do I need to know my pickup terminal before requesting a quote?", "No. If you have the booking number or MBL, the carrier can look up which SCPA terminal the container routes through — Wando Welch, North Charleston, or Hugh Leatherman. Mark it \"not sure yet\" on the request. Port drayage rates from the three container terminals differ, so the quote firms up once the terminal is confirmed."),
        ("What are ERD, cargo cut, and VGM cut on an export quote?", "Three deadlines that frame every export container drayage move. ERD is the earliest receiving date — the first day the terminal accepts your loaded export. Cargo cut is the last day it accepts the loaded box for that vessel. VGM cut is the deadline to file the verified gross mass. Include all three in the quote request so the carrier can schedule the loading and terminal return inside the window."),
    ]

    schema = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "The drayage quote checklist for importers",
        "description": "The exact information a Charleston drayage carrier needs from you to come back with a usable quote on the first try.",
        "author": {"@type": "Organization", "name": "Cate Freight"},
        "publisher": {"@id": f"{site_url}/#org"},
        "image": f"{site_url}/og-default.png",
        "datePublished": "2026-04-26",
        "dateModified": ctx["last_modified"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/drayage-quote-checklist/"},
    },
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_items
        ],
    }]

    html = render(
        slug="drayage-quote-checklist",
        path="/resources/drayage-quote-checklist/",
        title="The Drayage Quote Checklist for Importers | Cate Freight",
        meta_description="Send these fields with your first email and a Charleston drayage carrier can quote in under an hour. The complete checklist for importers and forwarders.",
        h1="The drayage quote checklist for importers.",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/drayage-quote-checklist/index.html", html)
