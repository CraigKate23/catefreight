"""Cate Freight homepage."""

def build(ctx):
    render = ctx["render"]
    cta_banner = ctx["cta_banner"]
    faq_block = ctx["faq_block"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]
    email = ctx["email"]

    # ---------- HERO ---------- #
    hero = f"""
<section class="hero">
  <div class="container">
    <div class="hero-split">
      <div>
        <span class="hero-eyebrow">Charleston, SC drayage</span>
        <h1>Charleston drayage from all three SCPA terminals — <span class="accent">quote in under an hour, releases checked before we roll.</span></h1>
        <p class="lead">Cate Freight pulls import and export containers from Wando Welch, North Charleston, and Hugh Leatherman to warehouses, transload yards, and consignees across South Carolina and the Southeast. One dispatcher per file. Same-day POD. Honest accessorials.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/quote/">Request a drayage quote</a>
          <a class="btn btn-ghost" href="tel:{phone_tel}">{phone_display} dispatch</a>
        </div>
        <div class="hero-trust">
          <span>All three SCPA terminals</span>
          <span>Quote inside the hour</span>
          <span>Reefer, overweight, OOG</span>
          <span>3PL &amp; forwarder friendly</span>
        </div>
      </div>
      <div class="hero-card">
        <h3>What we need to quote you</h3>
        <p>Four fields and we can come back with a real number — usually inside an hour during business hours.</p>
        <form class="hero-microform" action="/quote/" method="GET">
          <label class="field"><span>Booking number</span><input name="booking" placeholder="e.g. MAERSK 1234567" autocomplete="off"></label>
          <label class="field"><span>Container size</span>
            <select name="container_size">
              <option>20' Dry</option><option selected>40' High Cube</option><option>40' Dry</option><option>40' Reefer</option><option>20' Reefer</option><option>Other</option>
            </select>
          </label>
          <label class="field"><span>Pickup terminal</span>
            <select name="terminal">
              <option>Wando Welch</option><option>North Charleston</option><option>Hugh Leatherman</option><option>Not sure yet</option>
            </select>
          </label>
          <label class="field"><span>Delivery ZIP</span><input name="delivery_zip" inputmode="numeric" pattern="[0-9]{{5}}" placeholder="29401" required></label>
          <button type="submit" class="btn btn-primary" style="width:100%; margin-top:6px;">Start the quote (4 fields &rarr; number)</button>
        </form>
        <div class="stats">
          <div><strong>3</strong><small>SCPA terminals</small></div>
          <div><strong>60 min</strong><small>Avg quote turn</small></div>
          <div><strong>Same day</strong><small>POD turnaround</small></div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    # ---------- WHO WE MOVE FOR ---------- #
    audience = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Who we move for</p>
      <h2>Built for the people who book drayage every week.</h2>
      <p class="lead" style="margin-left:auto; margin-right:auto;">If you've ever had a driver no-show on a release, lost a free day to a dispatcher who didn't return the email, or paid demurrage because nobody pre-pulled — you're the kind of customer Cate Freight is built for.</p>
    </div>
    <div class="card-grid">
      <div class="card">
        <div class="icon" aria-hidden="true">🏭</div>
        <h3>3PLs &amp; warehouses</h3>
        <p>Drop-and-hook coordination, ASN-friendly arrival windows, and a dispatcher who answers when the dock is waiting on a 40HC.</p>
        <a class="card-link" href="/who-we-serve/3pls/">3PL drayage details</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">🌐</div>
        <h3>Freight forwarders</h3>
        <p>Booking visibility, terminal-aware pickup timing, and clean PODs back fast so you can close the file the day it's delivered.</p>
        <a class="card-link" href="/who-we-serve/freight-forwarders/">Forwarder workflow</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">📋</div>
        <h3>Customs brokers</h3>
        <p>Release-status checks before the truck rolls. Nothing rolls until customs and freight are released and the line lifts the hold.</p>
        <a class="card-link" href="/who-we-serve/customs-brokers/">Broker handoff</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">📦</div>
        <h3>Importers &amp; exporters</h3>
        <p>You ship volume in or out of Charleston and want one number to call. Direct, no broker layer — unless you want one.</p>
        <a class="card-link" href="/who-we-serve/importers-exporters/">Direct shipper details</a>
      </div>
    </div>
  </div>
</section>
"""

    # ---------- CORE SERVICES ---------- #
    services = """
<section class="section bg-surface">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Core drayage services</p>
      <h2>Containers in. Containers out. Containers anywhere they need to go inside the Southeast.</h2>
    </div>
    <div class="card-grid">
      <div class="card">
        <div class="icon" aria-hidden="true">⚓</div>
        <h3>Port drayage</h3>
        <p>Pickup or return at all three SCPA container terminals — Wando Welch, North Charleston, and Hugh Leatherman.</p>
        <a class="card-link" href="/services/port-drayage/">Port drayage</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">⬇️</div>
        <h3>Import container drayage</h3>
        <p>Release-checked, customs-cleared imports from Charleston to your DC — live unload, drop, or pre-pull to our yard.</p>
        <a class="card-link" href="/services/import-container-drayage/">Import drayage</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">⬆️</div>
        <h3>Export container drayage</h3>
        <p>Loaded export delivery to terminal, ERD-aware scheduling, and SOLAS VGM coordination on every move.</p>
        <a class="card-link" href="/services/export-container-drayage/">Export drayage</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">🏬</div>
        <h3>Port-to-warehouse</h3>
        <p>Direct port-to-DC moves with appointments confirmed at both ends. We don't roll until your dock is ready.</p>
        <a class="card-link" href="/services/port-to-warehouse-drayage/">Port-to-warehouse</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">↔️</div>
        <h3>Transload &amp; coordination</h3>
        <p>Container delivery to a transload yard, plus the warehouse muscle to coordinate the cross-dock if you need it.</p>
        <a class="card-link" href="/services/transload-drayage/">Transload</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">🏋️</div>
        <h3>Overweight &amp; OOG</h3>
        <p>Tri-axle chassis, route permits, and the experience to pull 60,000+ lb containers without breaking the chain.</p>
        <a class="card-link" href="/services/overweight-drayage/">Overweight drayage</a>
      </div>
      <div class="card">
        <div class="icon" aria-hidden="true">🥶</div>
        <h3>Reefer drayage</h3>
        <p>Genset chassis, set-point verification on pickup, and pre-trip inspection so the box stays in temp the whole way.</p>
        <a class="card-link" href="/services/reefer-drayage/">Reefer drayage</a>
      </div>
      <div class="card dark">
        <div class="icon" aria-hidden="true">⚙️</div>
        <h3>Specialty &amp; project</h3>
        <p>Hazmat, flat-rack, open-top, and project moves with proper permits, escort coordination, and clean documentation.</p>
        <a class="card-link" href="/services/" style="color:#7ce5cb;">All services</a>
      </div>
    </div>
  </div>
</section>
"""

    # ---------- WHY CATE ---------- #
    why = """
<section class="section">
  <div class="container">
    <div class="feature-row">
      <div>
        <p class="eyebrow">Why Cate Freight</p>
        <h2>Drayage that thinks like the receiver.</h2>
        <p class="lead">Most drayage carriers were built around the truck. We were built around the receiver — the warehouse manager who needs containers in the right order, the broker who needs the release confirmed before the chassis leaves the yard, the 3PL who needs an ETA they can actually post.</p>
        <p>Greg Cate ran warehouses and 3PL operations for years before starting Cate Freight. That experience shows up in the way every container is handled: paperwork before the wheels turn, terminal status checked before dispatch, and one number to call when something changes.</p>
        <a class="btn btn-outline" href="/about/">More about Cate Freight</a>
      </div>
      <div class="panel">
        <h3>What you get on every move</h3>
        <ul>
          <li><div><strong>Release checked before dispatch</strong><span>Customs, freight, and line holds verified — no dry runs.</span></div></li>
          <li><div><strong>Quote inside the hour</strong><span>During business hours, you'll have a number on your screen before lunch.</span></div></li>
          <li><div><strong>One dispatcher per file</strong><span>You aren't bouncing between people. The person who quoted is the person who runs the move.</span></div></li>
          <li><div><strong>Clean PODs back same day</strong><span>Signed BOL emailed back the day of delivery. Imaged, named, filed.</span></div></li>
          <li><div><strong>Honest accessorials</strong><span>Chassis splits, detention, overweight permits — quoted upfront. No surprise lines on the invoice.</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    # ---------- TERMINALS ---------- #
    terminals = """
<section class="section bg-navy">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Charleston terminal coverage</p>
      <h2>All three SCPA container terminals. Every shift.</h2>
      <p class="lead" style="color:rgba(255,255,255,0.78); margin-left:auto; margin-right:auto;">We monitor terminal hours, gate moves, and chassis pool status across the Port of Charleston so we can route around the bottlenecks instead of waiting in them.</p>
    </div>
    <div class="terminals-grid">
      <div class="terminal" style="background:rgba(255,255,255,0.04); border-color:rgba(255,255,255,0.12); color:#fff;">
        <h3 style="color:#fff;">Wando Welch Terminal</h3>
        <span class="code" style="background:rgba(255,255,255,0.10); color:#cce8df;">USCHA &middot; Mt. Pleasant</span>
        <p style="color:rgba(255,255,255,0.76);">SCPA's highest-volume container terminal. Deep-water berths handling the largest vessels calling the East Coast.</p>
        <ul style="border-color:rgba(255,255,255,0.10);">
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Pickup &amp; return</strong> Container moves &amp; pre-pulls</li>
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Specialty</strong> Reefer, overweight, OOG</li>
        </ul>
      </div>
      <div class="terminal" style="background:rgba(255,255,255,0.04); border-color:rgba(255,255,255,0.12); color:#fff;">
        <h3 style="color:#fff;">North Charleston Terminal</h3>
        <span class="code" style="background:rgba(255,255,255,0.10); color:#cce8df;">USNCH &middot; Former Navy base</span>
        <p style="color:rgba(255,255,255,0.76);">Direct interstate access via I-26 and I-526. Diverse mix of containerized and breakbulk cargo.</p>
        <ul style="border-color:rgba(255,255,255,0.10);">
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Pickup &amp; return</strong> Container moves &amp; pre-pulls</li>
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Specialty</strong> Hazmat coordination</li>
        </ul>
      </div>
      <div class="terminal" style="background:rgba(255,255,255,0.04); border-color:rgba(255,255,255,0.12); color:#fff;">
        <h3 style="color:#fff;">Hugh Leatherman Terminal</h3>
        <span class="code" style="background:rgba(255,255,255,0.10); color:#cce8df;">USCHL &middot; North Charleston</span>
        <p style="color:rgba(255,255,255,0.76);">SCPA's newest terminal. Purpose-built for efficiency with current ship-to-shore equipment and gate technology.</p>
        <ul style="border-color:rgba(255,255,255,0.10);">
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Pickup &amp; return</strong> Container moves &amp; pre-pulls</li>
          <li style="color:rgba(255,255,255,0.7); border-color:rgba(255,255,255,0.10);"><strong style="color:#fff;">Specialty</strong> Newer ship-to-shore lines</li>
        </ul>
      </div>
    </div>
    <div style="text-align:center; margin-top:32px;">
      <a class="btn btn-ghost" href="/coverage/">See full coverage area</a>
    </div>
  </div>
</section>
"""

    # ---------- PROCESS ---------- #
    process = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How a container actually runs</p>
      <h2>The five steps every move passes through.</h2>
      <p class="lead" style="margin-left:auto; margin-right:auto;">No magic. Just discipline. Here's exactly what happens between "we got the booking" and "your POD is in your inbox."</p>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Booking received</h3>
        <p>You send a booking, MBL, or release notice. We confirm size, line, terminal, weight, and any specialty (reefer, hazmat, OOG).</p>
      </div>
      <div class="step">
        <h3>Releases verified</h3>
        <p>We check freight release, customs release, and line holds before we put a truck on it. No dry runs.</p>
      </div>
      <div class="step">
        <h3>Appointment booked</h3>
        <p>Terminal slot booked when required. Delivery appointment confirmed at the consignee. Driver gets a clean dispatch.</p>
      </div>
      <div class="step">
        <h3>Container moves</h3>
        <p>Driver pulls, GPS-tracked. We watch gate transactions and chassis pool status — and route around them when needed.</p>
      </div>
      <div class="step">
        <h3>POD &amp; close</h3>
        <p>Signed POD imaged, named with your reference, and emailed back same day. Empty returned and per diem clock stopped.</p>
      </div>
    </div>
    <div style="text-align:center; margin-top:32px;">
      <a class="btn btn-outline" href="/process/">Full operational walkthrough</a>
    </div>
  </div>
</section>
"""

    # ---------- LOCAL EXPERTISE ---------- #
    local = """
<section class="section bg-surface">
  <div class="container">
    <div class="feature-row swap">
      <div>
        <p class="eyebrow">Charleston-specific intelligence</p>
        <h2>The Port of Charleston has its own rhythms. We work them.</h2>
        <p class="lead">Charleston is the only major East Coast port without on-dock or near-dock rail. That makes drayage the dominant mode here — and makes the difference between a sharp drayman and a sloppy one painfully visible.</p>
        <ul class="checklist">
          <li>Pre-pull when free time is tight to avoid Terminal Demurrage</li>
          <li>Chassis pool awareness across TRAC, DCLI, and Flexi-Van</li>
          <li>Holiday "no work day" calendar tracked so you don't burn free time</li>
          <li>Tri-axle equipment for the heavy SE manufacturing flows</li>
          <li>Connections to Charleston transload yards and CFS facilities</li>
          <li>Same-day return coordination to stop per diem fast</li>
        </ul>
      </div>
      <div class="panel">
        <h3>Charleston port intel</h3>
        <p>Real numbers and rules that affect your container, not generic logistics talk.</p>
        <ul>
          <li><div><strong>3 SCPA container terminals</strong><span>Wando Welch, North Charleston, Hugh Leatherman</span></div></li>
          <li><div><strong>52' deepest harbor on the East Coast</strong><span>Largest vessels call here directly</span></div></li>
          <li><div><strong>Free time varies by line</strong><span>Typically 3-5 days at SCPA — we track it</span></div></li>
          <li><div><strong>Chassis splits cost real money</strong><span>$25-$75 per move in the wrong configuration</span></div></li>
          <li><div><strong>Navy Base intermodal arriving</strong><span>Near-dock rail finally landing in 2026 — we'll route to it day one</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

    # ---------- TRUST / DOCUMENTATION ---------- #
    documentation = """
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Documentation</p>
      <h2>Paperwork that doesn't slow you down.</h2>
    </div>
    <div class="kpi-row">
      <div class="kpi"><strong>BOL</strong><span>signed &amp; imaged</span></div>
      <div class="kpi"><strong>POD</strong><span>back same day</span></div>
      <div class="kpi"><strong>EIR</strong><span>tracked &amp; archived</span></div>
      <div class="kpi"><strong>VGM</strong><span>SOLAS submission</span></div>
      <div class="kpi"><strong>Hazmat</strong><span>placards &amp; manifest</span></div>
      <div class="kpi"><strong>Permits</strong><span>OW &amp; OOG handled</span></div>
    </div>
    <p class="lead text-center muted" style="margin: 0 auto;">Every document is named with your reference number, archived for the file, and emailed back when the move closes — so your auditors and your customs broker never have to chase us.</p>
  </div>
</section>
"""

    # ---------- FAQ ---------- #
    faq_html, faq_schema = faq_block([
        ("What is drayage and what does Cate Freight specifically do?",
         "Drayage is the short-distance transport of an ocean container — most often from a port terminal to a nearby warehouse, transload, or rail yard, or in reverse from a shipper's facility back to the terminal. Cate Freight specializes in port drayage out of the SCPA terminals at Charleston: Wando Welch, North Charleston, and Hugh Leatherman. We move loaded import containers inland, deliver loaded exports to the terminal, and run empties both directions."),
        ("Which Charleston terminals do you serve?",
         "All three SCPA container terminals — Wando Welch (Mount Pleasant), North Charleston Terminal (former Navy base), and Hugh Leatherman Terminal in North Charleston. We also work Columbus Street for breakbulk and RoRo when a customer needs it."),
        ("How fast can you turn a quote?",
         "During business hours, the typical turn from a complete booking to a quote on your screen is under an hour. After hours or on weekends, we'll respond by the next business morning. The fastest quotes start from a clean booking number, container size, terminal, and delivery ZIP — those four data points are usually enough."),
        ("Do you handle reefer, overweight, and hazmat containers?",
         "Yes to all three. Reefer moves use genset chassis with verified set points and pre-trip inspection. Overweight moves run on tri-axle chassis with state permits where required. Hazmat moves go on driver and equipment configurations cleared for the relevant placard class — including documentation handed back to your customs broker."),
        ("Can you do a pre-pull to avoid demurrage?",
         "Yes. When free time is tight or your dock isn't ready, we can pre-pull the container from the terminal and stage it before delivery. That stops the Terminal Demurrage clock at SCPA. We'll quote the pre-pull, the daily yard storage, and the eventual delivery as a single package so there are no surprises."),
        ("What information do you need to start a quote?",
         "Booking number or MBL, container size and type (20'/40'/40HC/reefer/etc.), pickup terminal, delivery ZIP, estimated availability date, weight, and any specialty notes (hazmat, overweight, OOG, live unload vs. drop). The faster you can give us those, the faster you'll get a real number back."),
        ("Do you serve customers outside Charleston?",
         "Yes. Most moves stay inside South Carolina — we run regularly to Columbia, Greenville, Spartanburg, Florence, Charleston metro, Summerville, Goose Creek, Walterboro, and Hilton Head. We also pull longer regional drays into Georgia, North Carolina, Tennessee, and the Florida panhandle. If you have a specific origin/destination question, send it and we'll tell you fast."),
        ("How are accessorials handled?",
         "Accessorials are quoted up front whenever they're predictable: chassis splits, fuel, overweight permits, hazmat surcharges, terminal access fees, and after-hours dispatch. Detention and per diem are pass-through and only billed when triggered — and we'll always tell you when the clock starts."),
    ])

    body = (
        hero
        + audience
        + services
        + why
        + terminals
        + process
        + local
        + documentation
        + faq_html
        + cta_banner(
            title="Got a booking? Send the four fields.",
            sub="Booking number, container size, terminal, delivery ZIP. We'll come back with a real itemized number — usually before lunch during business hours."
        )
    )

    # ---------- SCHEMA ---------- #
    org_schema = {
        "@context": "https://schema.org",
        "@type": "MovingCompany",
        "@id": f"{site_url}/#org",
        "name": "Cate Freight",
        "alternateName": "C8FR8",
        "url": site_url,
        "email": email,
        "telephone": phone_tel,
        "image": f"{site_url}/og-default.png",
        "logo": f"{site_url}/favicon.svg",
        "description": "Charleston, SC drayage carrier moving import and export containers from all SCPA terminals — Wando Welch, North Charleston, and Hugh Leatherman — to warehouses and consignees across the Southeast.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Charleston",
            "addressRegion": "SC",
            "addressCountry": "US",
        },
        "areaServed": [
            {"@type": "City", "name": "Charleston"},
            {"@type": "City", "name": "North Charleston"},
            {"@type": "City", "name": "Mount Pleasant"},
            {"@type": "City", "name": "Summerville"},
            {"@type": "City", "name": "Columbia"},
            {"@type": "State", "name": "South Carolina"},
            {"@type": "State", "name": "Georgia"},
            {"@type": "State", "name": "North Carolina"},
        ],
        "knowsAbout": [
            "Wando Welch Terminal",
            "North Charleston Terminal",
            "Hugh Leatherman Terminal",
            "Container drayage",
            "Import drayage",
            "Export drayage",
            "Reefer drayage",
            "Overweight container transport",
            "Hazmat drayage",
            "Transloading",
            "South Carolina Ports Authority",
        ],
        "identifier": [
            {"@type": "PropertyValue", "propertyID": "USDOT", "value": "3688555"},
            {"@type": "PropertyValue", "propertyID": "MC", "value": "1285884"},
        ],
        "sameAs": [],
    }
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Container drayage",
        "provider": {"@id": f"{site_url}/#org"},
        "areaServed": {"@type": "AdministrativeArea", "name": "South Carolina"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Drayage Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Port drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Import container drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Export container drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Port-to-warehouse drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Reefer container drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Overweight container drayage"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Transload coordination"}},
            ],
        },
    }
    schema = [org_schema, service_schema, faq_schema]

    html = render(
        slug="home",
        path="/",
        title="Cate Freight — Charleston Drayage. Containers in. Containers out.",
        meta_description="Charleston, SC drayage carrier moving import and export containers from Wando Welch, North Charleston, and Hugh Leatherman terminals to warehouses across the Southeast. Releases checked. Paperwork clean. Quote in under an hour.",
        h1="Charleston container drayage that runs the way receivers wish it would.",
        body_html=body,
        schema=schema,
        og_image="/og-default.png",
        nav_active="",
        page_class="page-home",
    )
    return ("/index.html", html)
