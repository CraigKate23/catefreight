"""About, Contact, FAQ, Coverage, Process, Privacy, 404."""


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    faq_block = ctx["faq_block"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]
    email = ctx["email"]

    out = []

    # ---------------- ABOUT ---------------- #
    crumbs_about = [("Home", "/"), ("About", "")]
    about_hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">About Cate Freight</span>
    <h1>A drayage company built by people who used to be the receiver.</h1>
    <p>Most drayage carriers were built around the truck. Cate Freight came out of the warehouse and 3PL world. We know what an inbound SOP looks like, what a customs broker needs back, and what a dock manager wishes drayage drivers understood.</p>
    <div class="actions">
      <a class="btn btn-primary" href="/quote/">Request a quote</a>
    </div>
  </div>
</section>
"""
    about_body = """
<section class="section">
  <div class="container narrow prose">
    <h2>What we are</h2>
    <p>Cate Freight is a Charleston, SC drayage carrier. We move ocean containers between the SCPA terminals — Wando Welch, North Charleston, and Hugh Leatherman — and warehouses, transload yards, and shipper facilities across South Carolina and the Southeast.</p>
    <p>That's the entire business. We don't run truckload freight elsewhere. We don't broker flatbed. We don't dabble in air or international. Drayage is the only thing we do, and it's the only thing we want to do.</p>

    <h2>What we are not</h2>
    <p>We are not a 700-truck mega-carrier. We're not a national 3PL. We don't have a fancy customer portal or a name partner on the building. What we have is operational discipline, a Charleston address, and a phone someone actually answers.</p>

    <h2>Why we started this</h2>
    <p>Greg Cate spent years running warehouses and 3PL operations on the receiver side of Charleston imports. The pattern was the same week after week: brilliant freight forwarders and customs brokers, doing real work, getting torpedoed by drayage carriers who didn't check releases, didn't return calls, and didn't get PODs back without three follow-ups.</p>
    <p>The opportunity was obvious. Build a drayage operation that runs the way receivers wish it would — releases verified before dispatch, paperwork clean and named correctly, communication that doesn't go silent the moment a problem shows up. That's Cate Freight.</p>

    <h2>How we run</h2>
    <p>Our operation is intentionally simple:</p>
    <ul>
      <li>One dispatcher per file — the person who quoted runs the whole move</li>
      <li>Releases (customs, freight, line) verified before any truck moves</li>
      <li>Daily morning ETA updates to the receiver on in-flight containers</li>
      <li>Same-day POD imaging with files named to your reference</li>
      <li>Clean accessorials — quoted up front, no surprise lines</li>
      <li>Equipment match: tri-axle, genset, flat-rack scheduled in advance, not at the gate</li>
    </ul>

    <h2>Where we operate</h2>
    <p>Cate Freight is based in Charleston, SC. We pull from all three SCPA container terminals every shift and run regional drays into the rest of South Carolina, Georgia, and the Carolinas. Most of our work is local Charleston drayage; a meaningful share is regional Southeast lanes. See the <a href="/coverage/">coverage page</a> for specifics.</p>

    <h2>Who we work with</h2>
    <p>We work with 3PLs, freight forwarders, customs brokers, and direct importers and exporters. The common thread isn't the org chart — it's that they care about how the move runs, not just the rate. If you've ever tracked down a dispatcher to find your container or argued with a carrier about an accessorial you didn't see coming, you'll like working with us.</p>

    <h2>Get in touch</h2>
    <p>Email <a href="mailto:greg@catefreight.com">greg@catefreight.com</a> or call dispatch at <a href="tel:""" + phone_tel + """">""" + phone_display + """</a>. The fastest way to a quote is the <a href="/quote/">quote form</a>.</p>
  </div>
</section>
"""
    about_schema = [{
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": "About Cate Freight",
        "url": f"{site_url}/about/",
    }]
    out.append((
        "/about/index.html",
        render(
            slug="about",
            path="/about/",
            title="About Cate Freight | Charleston Drayage Carrier",
            meta_description="Cate Freight is a Charleston, SC drayage carrier built by warehouse and 3PL operators. We pull from every SCPA terminal and run drays across the Southeast.",
            h1="A drayage company built by people who used to be the receiver.",
            body_html=breadcrumb_bar(crumbs_about) + about_hero + about_body + cta_banner(),
            breadcrumbs=crumbs_about,
            schema=about_schema,
            nav_active="about",
        ),
    ))

    # ---------------- CONTACT ---------------- #
    crumbs_contact = [("Home", "/"), ("Contact", "")]
    contact_hero = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Charleston dispatch</span>
    <h1>Contact Cate Freight.</h1>
    <p>Email and phone both go to humans. The fastest path to a number is the quote form, but we're happy to take a call if you'd rather talk first.</p>
  </div>
</section>
"""
    contact_body = f"""
<section class="section">
  <div class="container">
    <div class="split-2">
      <div>
        <h2>Dispatch</h2>
        <p><strong>Phone</strong><br><a href="tel:{phone_tel}" style="font-size:1.4rem; font-weight:800;">{phone_display}</a></p>
        <p><strong>Email</strong><br><a href="mailto:{email}" style="font-size:1.1rem; font-weight:600;">{email}</a></p>
        <p><strong>Hours</strong><br>Monday – Friday, 7:00 AM – 6:00 PM ET<br>After hours: email response by next morning</p>
        <p><strong>Service area</strong><br>Charleston metro &middot; Lowcountry &middot; SC Midlands &middot; Upstate &middot; SE regional lanes</p>
      </div>
      <div>
        <h2>Send us your move</h2>
        <p>The fastest way to a real number is the quote form. Booking, container, terminal, and delivery ZIP — that's all we need to start.</p>
        <a class="btn btn-primary" href="/quote/" style="margin-top:8px;">Open the quote form</a>

        <h2 style="margin-top: 40px;">For 3PLs &amp; forwarders</h2>
        <p>If you're moving steady Charleston volume, set up a recurring dispatch arrangement and you'll get faster quotes, equipment commitment, and standardized handling. Email Greg directly to talk through it.</p>
      </div>
    </div>
  </div>
</section>
"""
    contact_schema = [{
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "name": "Contact Cate Freight",
        "url": f"{site_url}/contact/",
    }]
    out.append((
        "/contact/index.html",
        render(
            slug="contact",
            path="/contact/",
            title="Contact Cate Freight Dispatch | Charleston Drayage",
            meta_description=f"Contact Cate Freight dispatch — Charleston, SC drayage carrier. Phone {phone_display}, email greg@catefreight.com. Real humans, fast responses, business hours and email overnight.",
            h1="Contact Cate Freight.",
            body_html=breadcrumb_bar(crumbs_contact) + contact_hero + contact_body + cta_banner(),
            breadcrumbs=crumbs_contact,
            schema=contact_schema,
        ),
    ))

    # ---------------- FAQ ---------------- #
    crumbs_faq = [("Home", "/"), ("FAQ", "")]
    faq_hero = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Charleston drayage FAQ</span>
    <h1>Answers to what people actually ask.</h1>
    <p>If your question isn't here, email or call. We'd rather give you a real answer than leave you guessing.</p>
  </div>
</section>
"""
    faq_html, faq_schema = faq_block([
        ("What is drayage?",
         "Drayage is the short-distance trucking of an ocean shipping container — most often between a port terminal and a nearby warehouse, transload, or rail yard. The word originally referred to a 'dray,' a heavy cart used to haul goods over short distances. Today, drayage describes the trucking layer that moves ocean containers off the port (or back to it)."),
        ("Why should I use a Charleston-based drayage carrier instead of a national one?",
         "National drayage carriers can move volume but tend to be slower on accessorial transparency and slower on communication. A local Charleston carrier knows the gates, the chassis pools, the specific terminal quirks, and answers the phone. For predictable, recurring volume out of SCPA, local usually wins on operational quality even when the rate is similar."),
        ("Which SCPA terminals do you cover?",
         "All three SCPA container terminals: Wando Welch (USCHA), North Charleston (USNCH), and Hugh Leatherman (USCHL). Plus Columbus Street (USCST) for breakbulk and RoRo when needed."),
        ("Which Charleston terminal will my container come into?",
         "The terminal is set by the steamship line and SCPA based on the vessel and that voyage's rotation — Wando Welch, North Charleston, or Hugh Leatherman. It's printed on your arrival notice and visible in the SCPA Container Availability tool once the vessel cuts. Send us the booking or container number and we'll pull it, confirm the terminal, and tell you when it's released."),
        ("Can you cross-tow a container between Charleston terminals?",
         "Yes. When an empty needs to return to a depot tied to a different chassis pool, or an export gets cut to the wrong terminal, we move it inter-terminal and quote the cross-tow as a single line item — no surprise accessorials."),
        ("How much does Charleston drayage cost?",
         "It depends on the destination ZIP, container size, weight, and any specialty handling (reefer, OW, hazmat). Local Charleston drays are typically in the few-hundred-dollar range before accessorials. Regional drays scale with mileage. Send the booking and delivery ZIP and we'll quote it."),
        ("Do you handle reefer drayage?",
         "Yes. Reefer drays use genset chassis, set point verified at pickup, and pre-trip inspection. Set point and supply temperature documented at delivery on the POD."),
        ("Do you handle overweight or out-of-gauge containers?",
         "Yes. Tri-axle chassis for overweight (up to ~60,000 lb payload with state permits). Flat-rack and open-top equipment for OOG. Permits pulled by us, billed pass-through with no markup."),
        ("Do you do hazmat drayage?",
         "Yes, on the placard classes our drivers and equipment are cleared for. We'll need the UN# and the broker's customs declaration before quoting. We document the full hazmat manifest and hand back a signed copy."),
        ("Can you pre-pull a container to avoid demurrage?",
         "Yes. When free time is tight or your dock isn't ready, we pull the container off the terminal, stage it at our yard, and deliver later. Pre-pull, daily storage, and final delivery are quoted as a single package so you can compare it against demurrage exposure."),
        ("How do you handle chassis split fees?",
         "We try to route to the depot that holds the chassis pool tied to your steamship line, eliminating the split. When a split has to happen, we quote it up front."),
        ("What's the difference between demurrage, detention, and per diem?",
         "Demurrage is what SCPA charges when a loaded container sits on the terminal past free time. Detention is what the steamship line charges when their container is held outside their terminal too long. Per diem is the daily rental fee for the chassis. They're three separate clocks; we track all of them."),
        ("How fast can you turn a quote?",
         "Inside an hour during business hours, off a complete request. After hours, by the next business morning. Faster on simple local moves where the booking and terminal are already known."),
        ("How fast can you pick up a container?",
         "Same-day pickup is possible if the container is released and we have the booking by mid-morning. Next-day is the norm and reliable. We'll be straight with you when same-day isn't realistic."),
        ("How do you communicate during a move?",
         "Daily morning ETA updates while in transit. Inbound text or email when the driver is en route to the consignee. Same-day POD scanned and emailed back, named with your reference number."),
        ("Do you support 3PL warehouse SOPs?",
         "Yes. Container number on every comm. BOL formatted to your customer's spec. Photos at delivery if required. Door assignments honored. Tell us the SOP and we'll match it."),
        ("Can you set up recurring weekly drayage?",
         "Yes. Recurring volume gets faster quotes, equipment commitment, and standardized handling. Email Greg directly to talk through the arrangement."),
        ("Do you provide tracking?",
         "GPS-tracked equipment, daily ETA updates, and ad-hoc status checks any time you ask. We can also output container status to email, EDI, or a TMS feed if your operation needs it."),
        ("What payment terms do you offer?",
         "Standard net terms for established customers; new customers typically start on prepay or COD until we have a relationship. Monthly invoicing with line-item detail available for recurring volume."),
        ("Are you bonded and insured?",
         "Yes. Cargo liability coverage, motor carrier liability, and customs bonds where applicable. Certificates available on request."),
    ])
    out.append((
        "/faq/index.html",
        render(
            slug="faq",
            path="/faq/",
            title="Charleston Drayage FAQ | Cate Freight",
            meta_description="Answers to common questions about Charleston drayage — SCPA terminals, demurrage, detention, chassis splits, reefer, overweight, hazmat, and more.",
            h1="Answers to what people actually ask.",
            body_html=breadcrumb_bar(crumbs_faq) + faq_hero + faq_html + cta_banner(),
            breadcrumbs=crumbs_faq,
            schema=[faq_schema],
        ),
    ))

    # ---------------- COVERAGE ---------------- #
    crumbs_cov = [("Home", "/"), ("Coverage", "")]
    cov_hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Service area</span>
    <h1>Charleston-based, regional reach.</h1>
    <p>We operate from Charleston, SC, with daily pickups at every SCPA terminal. Local Charleston drays are the bulk of what we run; regional Southeast lanes are an everyday part of the operation.</p>
  </div>
</section>
"""
    cov_body = """
<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">SCPA terminal coverage</p><h2>Every Charleston container terminal, every shift.</h2></div>
    <div class="terminals-grid">
      <div class="terminal">
        <h3>Wando Welch Terminal</h3>
        <span class="code">USCHA</span>
        <p>1 Wando Drive, Mount Pleasant, SC. SCPA's flagship container terminal — highest volume, deepest berths, biggest vessels.</p>
        <ul>
          <li><strong>Type</strong> Container / breakbulk</li>
          <li><strong>Cate Freight ops</strong> Daily pickup, return, pre-pull</li>
        </ul>
      </div>
      <div class="terminal">
        <h3>North Charleston Terminal</h3>
        <span class="code">USNCH</span>
        <p>2300 7th Street, North Charleston, SC. Original North Charleston terminal on the former Navy base. Direct I-526 / I-26 access.</p>
        <ul>
          <li><strong>Type</strong> Container / breakbulk</li>
          <li><strong>Cate Freight ops</strong> Daily pickup, return, pre-pull</li>
        </ul>
      </div>
      <div class="terminal">
        <h3>Hugh Leatherman Terminal</h3>
        <span class="code">USCHL</span>
        <p>100 Leatherman Boulevard, North Charleston, SC. SCPA's newest terminal. Modern ship-to-shore lines and gate technology.</p>
        <ul>
          <li><strong>Type</strong> Container / breakbulk</li>
          <li><strong>Cate Freight ops</strong> Daily pickup, return, pre-pull</li>
        </ul>
      </div>
      <div class="terminal">
        <h3>Columbus Street Terminal</h3>
        <span class="code">USCST</span>
        <p>200 Columbus Street, Charleston, SC. RoRo and breakbulk facility. We work it on demand for breakbulk and project moves.</p>
        <ul>
          <li><strong>Type</strong> RoRo / breakbulk</li>
          <li><strong>Cate Freight ops</strong> On-demand</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Local Charleston drayage</p><h2>The metro lanes we run constantly.</h2></div>
    <div class="split-2">
      <div>
        <ul class="checklist">
          <li>Charleston peninsula and downtown</li>
          <li>North Charleston, Hanahan, Goose Creek</li>
          <li>Mount Pleasant, Daniel Island, Cainhoy</li>
          <li>Summerville, Ladson, Lincolnville</li>
          <li>Moncks Corner, Bonneau</li>
        </ul>
      </div>
      <div>
        <ul class="checklist">
          <li>Ravenel, Hollywood, Adams Run</li>
          <li>James Island, Johns Island, Folly Beach</li>
          <li>Walterboro, Round O</li>
          <li>St. George, Harleyville</li>
          <li>Yemassee, Beaufort</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Regional Southeast lanes</p><h2>Where else we run drays out of Charleston.</h2></div>
    <div class="split-2">
      <div>
        <h3>South Carolina</h3>
        <ul class="checklist">
          <li>Columbia, Cayce, Lexington</li>
          <li>Greenville, Spartanburg, Anderson, Inman</li>
          <li>Florence, Darlington, Hartsville</li>
          <li>Hilton Head, Bluffton, Beaufort</li>
          <li>Sumter, Camden, Lugoff</li>
        </ul>
      </div>
      <div>
        <h3>Adjacent states</h3>
        <ul class="checklist">
          <li>Savannah, Augusta, Atlanta metro (Georgia)</li>
          <li>Charlotte, Concord, Gastonia, Statesville (North Carolina)</li>
          <li>Wilmington, Fayetteville, Lumberton (NC)</li>
          <li>Knoxville and east Tennessee</li>
          <li>Florida panhandle on request</li>
        </ul>
      </div>
    </div>
    <div class="callout">
      <strong>Don't see your destination?</strong> Send us the ZIP. If it's a one-off we don't run regularly, we'll either quote it or hand you a clean referral. We don't pretend to cover lanes we can't run well.
    </div>
  </div>
</section>
"""
    out.append((
        "/coverage/index.html",
        render(
            slug="coverage",
            path="/coverage/",
            title="Cate Freight Drayage Coverage Area | Charleston, SC and the Southeast",
            meta_description="Cate Freight covers all three SCPA container terminals and runs Charleston drayage across South Carolina, Georgia, and the Carolinas. Local and regional lanes both routine.",
            h1="Charleston-based, regional reach.",
            body_html=breadcrumb_bar(crumbs_cov) + cov_hero + cov_body + cta_banner(),
            breadcrumbs=crumbs_cov,
            nav_active="coverage",
        ),
    ))

    # ---------------- PROCESS ---------------- #
    crumbs_proc = [("Home", "/"), ("Process", "")]
    proc_hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">How we run a container</span>
    <h1>The operational walkthrough, end to end.</h1>
    <p>No mystery, no special sauce. Just the actual sequence of steps every Charleston drayage move passes through, and what we commit to at each step.</p>
  </div>
</section>
"""
    proc_body = """
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>1. Booking received</h2>
      <p>You send us a booking, MBL, or release notice — typically by email or directly through your TMS. We confirm container size, type, steamship line, terminal, weight, and any specialty notes (reefer, hazmat, OOG, OW). If anything is missing, we ask once.</p>

      <h2>2. Releases verified</h2>
      <p>Three releases get checked before any truck rolls: <strong>customs release</strong> (1C on file), <strong>freight release</strong> (line lifts the freight hold), and <strong>line holds</strong> (any other hold — exam, demurrage, equipment). If any of the three are missing, we don't dispatch. We tell you what's missing and we wait.</p>

      <h2>3. Appointment booked</h2>
      <p>SCPA terminal slot booked when required. Delivery appointment confirmed at the consignee — we contact the warehouse, confirm a window, and lock it. If the consignee uses an appointment system (OneRail, Opendock, etc.) we book through it.</p>

      <h2>4. Driver dispatched</h2>
      <p>Driver gets a clean dispatch pack: container, terminal, gate appointment, delivery address, contact info, special instructions, and your reference number. The driver is matched to the equipment — overweight goes to drivers used to tri-axle, reefer goes to drivers experienced with genset.</p>

      <h2>5. Container moves</h2>
      <p>Driver arrives at the terminal, runs the gate transaction, hooks the chassis. We capture the EIR. GPS tracks the move. We monitor terminal status and chassis pool location in real time and route around problems instead of getting stuck in them.</p>

      <h2>6. Delivery</h2>
      <p>Live unload, drop-and-hook, or transload, per your spec. Driver waits on signature for live; bobtails away after drop. We text or email the moment delivery completes.</p>

      <h2>7. Empty return</h2>
      <p>Empty container returned the same day when possible — that's the lever that stops per diem fastest. Empty receipt captured and forwarded.</p>

      <h2>8. POD &amp; close</h2>
      <p>Signed BOL imaged and emailed back the day of delivery. The PDF is named with your reference number, the container number, and the delivery date. The file gets archived in our records, ready for any audit pull.</p>

      <h2>What you get back from us, every move</h2>
      <ul>
        <li>EIR / gate transaction at pickup</li>
        <li>ETA updates while in transit</li>
        <li>Signed BOL / POD at delivery, same-day imaged</li>
        <li>Empty return receipt</li>
        <li>Itemized invoice with linehaul, chassis, fuel, accessorials clearly broken out</li>
      </ul>
    </div>
  </div>
</section>
"""
    out.append((
        "/process/index.html",
        render(
            slug="process",
            path="/process/",
            title="How Cate Freight Runs a Charleston Drayage Move | Process Walkthrough",
            meta_description="The step-by-step operational walkthrough of how Cate Freight handles a Charleston drayage move — from booking to POD and empty return.",
            h1="The operational walkthrough, end to end.",
            body_html=breadcrumb_bar(crumbs_proc) + proc_hero + proc_body + cta_banner(),
            breadcrumbs=crumbs_proc,
            nav_active="process",
        ),
    ))

    # ---------------- PRIVACY ---------------- #
    crumbs_priv = [("Home", "/"), ("Privacy", "")]
    privacy_body = f"""
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Legal</span>
    <h1>Privacy policy.</h1>
    <p>The short version: we collect what we need to quote and run your drayage. We don't sell it. We don't share it with anyone outside our operations and the carriers/permits required to do the move.</p>
  </div>
</section>

<section class="section">
  <div class="container narrow prose">
    <h2>What we collect</h2>
    <ul>
      <li>Information you submit through the quote form: name, company, email, phone, container details, addresses, and notes.</li>
      <li>Email content you send us when you contact dispatch.</li>
      <li>Standard server logs (IP, browser, page) for security and analytics.</li>
    </ul>

    <h2>How we use it</h2>
    <ul>
      <li>To quote, schedule, and run the drayage move.</li>
      <li>To communicate with you about that move.</li>
      <li>To fulfill regulatory requirements (USDOT, customs, hazmat manifests, state permits).</li>
    </ul>

    <h2>Who we share it with</h2>
    <ul>
      <li>Your customs broker, when relevant to the move.</li>
      <li>SCPA terminal operators and steamship lines, as required for gate transactions.</li>
      <li>Permitting agencies, for OW and hazmat moves.</li>
      <li>No one else. We don't sell or rent your information.</li>
    </ul>

    <h2>Cookies &amp; analytics</h2>
    <p>This site uses minimal first-party cookies and may use a privacy-friendly analytics tool (e.g. Plausible) to understand site usage. No third-party advertising trackers.</p>

    <h2>Your rights</h2>
    <p>You can ask for a copy of your data, ask us to correct it, or ask us to delete it. Email <a href="mailto:{email}">{email}</a> and we'll respond.</p>

    <h2>Contact</h2>
    <p>Cate Freight &middot; Charleston, SC<br>Email: <a href="mailto:{email}">{email}</a><br>Phone: <a href="tel:{phone_tel}">{phone_display}</a></p>
  </div>
</section>
"""
    out.append((
        "/privacy/index.html",
        render(
            slug="privacy",
            path="/privacy/",
            title="Privacy Policy | Cate Freight",
            meta_description="Cate Freight privacy policy — what we collect, how we use it, who we share it with, and your rights.",
            h1="Privacy policy.",
            body_html=breadcrumb_bar(crumbs_priv) + privacy_body,
            breadcrumbs=crumbs_priv,
        ),
    ))

    # ---------------- 404 ---------------- #
    not_found_body = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">404</span>
    <h1>That page didn't survive the dray.</h1>
    <p>The link you followed doesn't exist — maybe it moved, maybe it was a typo. Try one of these instead.</p>
    <div class="actions">
      <a class="btn btn-primary" href="/">Home</a>
      <a class="btn btn-ghost" href="/charleston-drayage/">Charleston drayage</a>
      <a class="btn btn-ghost" href="/quote/">Request a quote</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid">
      <div class="card"><h3>Services</h3><p>Every drayage service we run.</p><a class="card-link" href="/services/">See services</a></div>
      <div class="card"><h3>Coverage</h3><p>Where we run drays out of Charleston.</p><a class="card-link" href="/coverage/">Coverage area</a></div>
      <div class="card"><h3>FAQ</h3><p>Common questions, real answers.</p><a class="card-link" href="/faq/">Read FAQ</a></div>
      <div class="card"><h3>Resources</h3><p>Articles on Charleston drayage operations.</p><a class="card-link" href="/resources/">Articles</a></div>
    </div>
  </div>
</section>
"""
    out.append((
        "/404.html",
        render(
            slug="404",
            path="/404.html",
            title="Page not found | Cate Freight",
            meta_description="The page you followed doesn't exist. Find Charleston drayage services, coverage, or a quote on Cate Freight.",
            h1="That page didn't survive the dray.",
            body_html=not_found_body,
            no_index=True,
        ),
    ))

    return out
