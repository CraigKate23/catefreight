"""Services hub + all individual service pages."""


def _service_page(ctx, *, slug, path, title, meta, h1, eyebrow, intro_html, sections_html, faqs, related, schema_extra=None):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    faq_block = ctx["faq_block"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]

    crumbs = [("Home", "/"), ("Services", "/services/"), (eyebrow, "")]
    hero = f"""
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Charleston, SC service</span>
    <h1>{h1}</h1>
    <p>{intro_html}</p>
    <div class="actions">
      <a class="btn btn-primary" href="/quote/">Request a quote</a>
      <a class="btn btn-ghost" href="tel:{phone_tel}">{phone_display} dispatch</a>
    </div>
  </div>
</section>
"""

    related_cards = "".join(
        f'<div class="card"><h3>{name}</h3><p>{desc}</p><a class="card-link" href="{href}">Read more</a></div>'
        for name, desc, href in related
    )
    related_block = f"""
<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Pairs well with</p><h2>Other Charleston drayage services we run.</h2></div>
    <div class="card-grid">{related_cards}</div>
  </div>
</section>
"""

    faq_html, faq_schema = faq_block(faqs)
    body = breadcrumb_bar(crumbs) + hero + sections_html + related_block + faq_html + cta_banner()

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": eyebrow,
            "serviceType": eyebrow,
            "provider": {"@id": f"{site_url}/#org"},
            "areaServed": {"@type": "City", "name": "Charleston, SC"},
            "description": meta,
        },
        faq_schema,
    ]
    if schema_extra:
        schema.extend(schema_extra)

    html = render(
        slug=slug,
        path=path,
        title=title,
        meta_description=meta,
        h1=h1,
        body_html=body,
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="services",
    )
    return (path + "index.html", html)


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    out = []

    # ---------------- Services hub ---------------- #
    crumbs_hub = [("Home", "/"), ("Services", "")]
    hub_hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Drayage services</span>
    <h1>Every drayage service we run, plain English.</h1>
    <p>Cate Freight is a <a href="/charleston-drayage/">Charleston drayage</a> carrier first. Within that, we work imports and exports, reefer and dry, overweight and OOG, port-to-warehouse and pier returns, transload coordination and pre-pull staging. Pick the move you need to make.</p>
    <div class="actions">
      <a class="btn btn-primary" href="/quote/">Request a quote</a>
    </div>
  </div>
</section>
"""

    hub_grid = """
<section class="section">
  <div class="container">
    <div class="card-grid">
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-anchor"/></svg></div><h3>Port drayage</h3><p>Pickup and return at all three SCPA container terminals.</p><a class="card-link" href="/services/port-drayage/">Port drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-import"/></svg></div><h3>Import container drayage</h3><p>Release-checked, customs-cleared imports from Charleston to your destination.</p><a class="card-link" href="/services/import-container-drayage/">Import drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-export"/></svg></div><h3>Export container drayage</h3><p>Loaded export delivery to terminal with ERD-aware scheduling.</p><a class="card-link" href="/services/export-container-drayage/">Export drayage</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-warehouse"/></svg></div><h3>Port-to-warehouse</h3><p>Direct port-to-DC moves with appointments confirmed at both ends.</p><a class="card-link" href="/services/port-to-warehouse-drayage/">Port-to-warehouse</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-transload"/></svg></div><h3>Transload &amp; coordination</h3><p>Container delivery to a transload yard plus warehouse coordination.</p><a class="card-link" href="/services/transload-drayage/">Transload</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-snowflake"/></svg></div><h3>Reefer drayage</h3><p>Genset chassis, verified set points, pre-trip inspection on every move.</p><a class="card-link" href="/services/reefer-drayage/">Reefer</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-weight"/></svg></div><h3>Overweight &amp; OOG</h3><p>Tri-axle chassis, route permits, 60,000+ lb experience.</p><a class="card-link" href="/services/overweight-drayage/">Overweight</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-clock"/></svg></div><h3>Pre-pull service</h3><p>Stage containers off-port to stop the demurrage clock when free time is tight.</p><a class="card-link" href="/services/import-container-drayage/#pre-pull">Pre-pull info</a></div>
    </div>
  </div>
</section>
"""

    out.append((
        "/services/index.html",
        render(
            slug="services",
            path="/services/",
            title="Charleston Drayage Services | Cate Freight",
            meta_description="Drayage services from Cate Freight — port drayage, import and export container moves, port-to-warehouse, transload, reefer, overweight, hazmat, and pre-pull staging from Charleston, SC.",
            h1="Every drayage service we run, plain English.",
            body_html=breadcrumb_bar(crumbs_hub) + hub_hero + hub_grid + cta_banner(),
            breadcrumbs=crumbs_hub,
            nav_active="services",
        ),
    ))

    # ---------------- Port Drayage ---------------- #
    out.append(_service_page(
        ctx,
        slug="port-drayage",
        path="/services/port-drayage/",
        title="Port Drayage Services in Charleston, SC | Cate Freight",
        meta="Port drayage from Charleston, SC. Pickup and return at every SCPA container terminal — Wando Welch, North Charleston, Hugh Leatherman. Same-day and next-day scheduling.",
        eyebrow="Port drayage",
        h1="Port drayage at the Port of Charleston, terminal by terminal.",
        intro_html="Cate Freight runs every SCPA container terminal — Wando Welch, North Charleston, and Hugh Leatherman — with operational discipline tuned to each gate's rhythms. We monitor terminal status, chassis pool location, and gate moves so your container moves on the first attempt.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What "port drayage" actually means at SCPA</h2>
      <p>Port drayage is short-haul trucking of an ocean container between a marine terminal and a nearby destination. At Charleston, "nearby" can mean a Mount Pleasant warehouse five miles from Wando Welch, or a Greenville DC two hundred and forty miles up I-26. Both are drayage moves; both run through the same SCPA gate process.</p>
      <p>The job has three phases regardless of distance: <strong>pickup at the terminal</strong>, <strong>linehaul</strong>, and <strong>empty return</strong>. Most of the carrier-side complexity lives in phase one and three — the gate transactions, chassis split avoidance, and per-diem clock management that quietly determine whether your invoice ends up clean or messy.</p>

      <h2>How Cate Freight runs each SCPA terminal</h2>
      <h3>Wando Welch Terminal (USCHA)</h3>
      <p>SCPA's flagship container terminal in Mount Pleasant. Wando handles the largest vessels calling the port and runs the highest container volume. Gate appointment discipline matters more here than anywhere else in Charleston — and we pull from Wando every single shift.</p>

      <h3>North Charleston Terminal (USNCH)</h3>
      <p>The original North Charleston terminal on the former Navy base. Direct interstate access (I-526 / I-26), strong for hazmat coordination and traditional dry container flows. Pickup and empty returns work cleanly here when the gate is moving.</p>

      <h3>Hugh K. Leatherman Terminal (USCHL)</h3>
      <p>SCPA's newest terminal, in North Charleston. Newer ship-to-shore lines, modern gate technology, and increasing share of Charleston's container moves as more services rotate in. We pull and return here on the same daily cadence as Wando.</p>
    </div>
    <div class="kpi-row" style="margin-top: 36px;">
      <div class="kpi"><strong>Wando Welch</strong><span>USCHA</span></div>
      <div class="kpi"><strong>North Charleston</strong><span>USNCH</span></div>
      <div class="kpi"><strong>Hugh Leatherman</strong><span>USCHL</span></div>
      <div class="kpi"><strong>Columbus St.</strong><span>USCST (RoRo/breakbulk)</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="prose">
      <h2>Highway corridors and counties we run from each SCPA terminal</h2>
      <p>Charleston drayage is a corridor business as much as a terminal business. Where your container is going decides which interstate and which surface highways the driver runs, which in turn decides chassis routing, gate timing, and how clean the empty return looks. Here's how the lanes actually work out of each <a href="/charleston-drayage/">Charleston drayage</a> terminal:</p>

      <h3>From Wando Welch Terminal (Mount Pleasant — Charleston County)</h3>
      <p>Wando sits in Mount Pleasant, east of the Cooper River. Outbound containers leave via the Don Holt Bridge or the Mark Clark Expressway (<strong>I-526</strong>), then split to <strong>US-17</strong> for East Cooper and Lowcountry deliveries, or to <strong>I-26</strong> for everything west and north. Local Mount Pleasant DCs are five-mile drays. Daniel Island, Cainhoy, and Hanahan are usually I-526 moves. Summerville and Goose Creek industrial parks come off I-26 once we're across the Cooper.</p>

      <h3>From North Charleston Terminal (North Charleston — Charleston County)</h3>
      <p>The original North Charleston terminal sits on the former Navy base with direct ramps to <strong>I-526</strong> and <strong>I-26</strong>. From here we run <strong>US-52</strong> and <strong>US-78</strong> into Berkeley and Dorchester County warehouses (Goose Creek, Hanahan, Ladson, Summerville, Moncks Corner), and we take I-26 west for Columbia and the Upstate. For points south — Walterboro, Yemassee, Beaufort — it's I-526 to US-17, or I-26 to I-95 depending on consignee ZIP.</p>

      <h3>From Hugh Leatherman Terminal (North Charleston — Charleston County)</h3>
      <p>Leatherman shares North Charleston's interstate access pattern — straight onto I-526, with I-26 a short connector away. Most Leatherman containers we pull are heading to tri-county warehouses in <strong>Berkeley County</strong>, <strong>Dorchester County</strong>, and <strong>Charleston County</strong>, or up I-26 into the Midlands. Empty returns route back the same way.</p>

      <h3>Regional corridor reference</h3>
      <ul>
        <li><strong>I-26 north and west</strong> — Summerville, Columbia, Newberry, Spartanburg, Greenville, and onward to I-85 for Charlotte and Atlanta drays.</li>
        <li><strong>I-95 north and south</strong> — Florence, Lumberton, and Fayetteville to the north; Walterboro, Yemassee, and the Florida border to the south.</li>
        <li><strong>US-17 corridor</strong> — Mount Pleasant, McClellanville, Georgetown, and the Lowcountry; also Ravenel and Hollywood to the south of Charleston.</li>
        <li><strong>US-78 / US-52 corridor</strong> — the Ladson, Summerville, Goose Creek, and Moncks Corner warehouse cluster where most Berkeley and Dorchester County drays terminate.</li>
        <li><strong>I-526 (Mark Clark) ring</strong> — connects all three SCPA container terminals to North Charleston, West Ashley, and Mount Pleasant industrial property.</li>
      </ul>

      <p>If your delivery ZIP is on one of these corridors, the route is settled. If it's not, send the ZIP and we'll walk the lane on the map before we quote. See the full <a href="/coverage/">Charleston drayage coverage area</a> for every metro we touch on a normal week.</p>
    </div>
  </div>
</section>

<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Equipment</p><h2>Equipment we run for port drayage.</h2></div>
    <div class="card-grid">
      <div class="card"><h3>Standard chassis</h3><p>20', 40', 40HC dry containers up to legal weight (typically 44,000 lb on 5-axle).</p></div>
      <div class="card"><h3>Tri-axle chassis</h3><p>Heavy import/export containers up to 58,000-60,000 lb with state permits.</p></div>
      <div class="card"><h3>Genset reefer chassis</h3><p>For reefer pickup, set-point verification, and pre-trip.</p></div>
      <div class="card"><h3>Flat-rack &amp; open-top capability</h3><p>OOG and breakbulk-style cargo via container equipment.</p></div>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Which Charleston port terminals do you serve for drayage?",
             "All three SCPA container terminals — Wando Welch (USCHA), North Charleston (USNCH), and Hugh Leatherman (USCHL) — plus Columbus Street for breakbulk and RoRo when needed."),
            ("Can you handle same-day port drayage in Charleston?",
             "Often yes, when the booking is released and we have the move in our hands by mid-morning. Otherwise next-day is the norm and reliable. We'll be straight with you when same-day isn't realistic."),
            ("Do you charge a chassis split fee?",
             "Only when a true split is unavoidable. We try to route to the depot that holds the chassis pool tied to your steamship line, eliminating the split. When a split has to happen, we tell you up front what it costs."),
            ("Can you pre-pull the container if our dock isn't ready?",
             "Yes. We'll pre-pull off the terminal to stop Terminal Demurrage, stage the container, and deliver when your dock is free. Pre-pull, daily storage, and final delivery are quoted as a single package."),
        ],
        related=[
            ("Import container drayage", "Releases checked, customs cleared, delivery scheduled.", "/services/import-container-drayage/"),
            ("Export container drayage", "Loaded delivery to terminal with ERD and VGM coordination.", "/services/export-container-drayage/"),
            ("Port-to-warehouse drayage", "Direct port-to-DC moves with appointments at both ends.", "/services/port-to-warehouse-drayage/"),
        ],
    ))

    # ---------------- Import Container Drayage ---------------- #
    out.append(_service_page(
        ctx,
        slug="import-container-drayage",
        path="/services/import-container-drayage/",
        title="Import Container Drayage from Port of Charleston | Cate Freight",
        meta="Import container drayage from Charleston, SC. We check customs, freight, and line releases before dispatch — and pre-pull when free time is tight to stop demurrage.",
        eyebrow="Import container drayage",
        h1="Import container drayage from Charleston, with the releases checked before the truck rolls.",
        intro_html="Importing through Charleston means working three releases — customs, freight, and any line hold — and beating the demurrage clock. Cate Freight verifies all three before we put a truck on your container, then runs it to your dock, transload, or our yard if a pre-pull saves you money.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>The import drayage timeline at Charleston</h2>
      <p>Once a vessel discharges and SCPA releases the container at the gate, the line-up of events is:</p>
      <ol>
        <li><strong>Container available.</strong> SCPA shows the container as discharged and ready for pickup at one of the three terminals.</li>
        <li><strong>Customs release.</strong> Either entered ahead of arrival (most common) or filed against the in-bond. Until ABI 1C is on file, no truck rolls.</li>
        <li><strong>Freight release.</strong> The steamship line lifts its freight hold once payment / OBL release is in.</li>
        <li><strong>Line hold check.</strong> Last review for any other line hold (demurrage, exam, equipment).</li>
        <li><strong>Free time clock starts.</strong> SCPA Terminal Free Time begins; demurrage accrues after expiration.</li>
        <li><strong>Pickup, linehaul, delivery.</strong> Terminal appointment booked, container moves, POD signed.</li>
        <li><strong>Empty return.</strong> Per diem clock continues until empty hits the terminal or designated depot.</li>
      </ol>

      <h2 id="pre-pull">When a pre-pull saves you money</h2>
      <p>If your dock isn't ready when the demurrage clock is about to expire, the smart play is a <strong>pre-pull</strong>: pull the container off the terminal early, stage it at our yard, and deliver when your warehouse is free. The pre-pull stops Terminal Demurrage cold; daily yard storage replaces it at a fraction of the cost.</p>
      <p>We quote pre-pull, daily storage, and final delivery as a single package so you can compare it to the demurrage exposure and make the call with your eyes open.</p>

      <blockquote>"The carrier who pre-pulls when free time is tight will save you more than the carrier with the cheapest base linehaul. Every time."</blockquote>

      <h2>Live unload, drop &amp; hook, or transload</h2>
      <p>Three delivery models, three different cost profiles:</p>
      <ul>
        <li><strong>Live unload.</strong> Driver waits while you unload. Best when you have a dock and a quick crew.</li>
        <li><strong>Drop &amp; hook.</strong> Driver drops the container on a chassis at your facility and bobtails away. You unload on your schedule and we come back for the empty. Stops driver detention; chassis per diem applies.</li>
        <li><strong>Transload.</strong> Container delivered to a transload facility, contents cross-docked onto domestic equipment, empty returned the same day. Best when the inland leg is much longer than the dray.</li>
      </ul>
      <p>If you don't know which one to ask for, tell us your unload speed and the destination — we'll do the math.</p>
    </div>
  </div>
</section>

<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Information we need to start</p><h2>The faster you give us this, the faster you get a number.</h2></div>
    <div class="split-2">
      <div>
        <ul class="checklist">
          <li>Booking number or MBL</li>
          <li>Container size &amp; type (20', 40', 40HC, reefer)</li>
          <li>Pickup terminal — Wando Welch, North Charleston, Leatherman</li>
          <li>Steamship line</li>
          <li>Estimated container availability date</li>
        </ul>
      </div>
      <div>
        <ul class="checklist">
          <li>Delivery ZIP and address</li>
          <li>Live unload, drop &amp; hook, or transload</li>
          <li>Approximate weight (and overweight Y/N)</li>
          <li>Hazmat (UN# if yes), reefer set point if reefer</li>
          <li>Customs broker contact, if known</li>
        </ul>
      </div>
    </div>
  </div>
</section>
""",
        faqs=[
            ("How does demurrage work at the Port of Charleston?",
             "SCPA Terminal Demurrage starts accruing after free time expires. Free time at SCPA is set by the steamship line and typically runs three to five days, with carve-outs for holiday 'no work days' that don't accrue. Once you're past free time, demurrage is billed by the terminal day, regardless of the cause of delay."),
            ("What's the difference between demurrage, detention, and per diem?",
             "Demurrage is what SCPA charges when a loaded container sits on the terminal past free time. Detention is what the steamship line charges when their container is held outside their terminal too long. Per diem is the daily rental fee for the chassis. They're often confused; they're three separate clocks."),
            ("Can you pre-pull and store containers in Charleston?",
             "Yes. When free time is running out and your dock isn't ready, we pull the container off the terminal early and stage it. The Terminal Demurrage clock stops; daily yard storage replaces it at a much lower cost. We quote pre-pull, storage, and delivery as a single package."),
            ("Do you handle the customs broker handoff?",
             "Yes. We work directly with your customs broker — or in-house if you have one — to confirm 1C release before dispatch. We'll also share the container's pickup status and EIR back as soon as the gate transaction completes."),
            ("How do you handle import drayage for 3PL receivers?",
             "We treat the 3PL like the customer. ASN-friendly arrival windows, container number on every email, BOLs named to your reference, and PODs back the day of delivery. If you have a TMS or visibility tool, we'll match its data fields."),
        ],
        related=[
            ("Port-to-warehouse drayage", "Direct moves with appointments at both ends.", "/services/port-to-warehouse-drayage/"),
            ("Transload coordination", "Container delivery to transload yards across Charleston and Columbia.", "/services/transload-drayage/"),
            ("Drayage for 3PLs", "Built around how warehouse receivers actually run.", "/who-we-serve/3pls/"),
        ],
    ))

    # ---------------- Export Container Drayage ---------------- #
    out.append(_service_page(
        ctx,
        slug="export-container-drayage",
        path="/services/export-container-drayage/",
        title="Export Container Drayage at Port of Charleston | Cate Freight",
        meta="Export container drayage in Charleston, SC. Loaded export delivery to SCPA terminals with ERD-aware scheduling and SOLAS VGM coordination.",
        eyebrow="Export container drayage",
        h1="Export container drayage that hits the cut, every time.",
        intro_html="Charleston export drayage is a deadlines game — earliest receiving date, vessel cut-off, and the SOLAS VGM submission window. Cate Freight schedules pickups against the line's actual cut, not a guess, and submits VGM through the right channel before the chassis leaves your yard.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>Export drayage timing — what actually matters</h2>
      <p>Export bookings have three time windows that decide whether your container makes the vessel or rolls to the next one:</p>
      <ul>
        <li><strong>Earliest Receiving Date (ERD).</strong> The earliest the terminal will accept your loaded export. Drop too early and you get turned away. Drop after ERD and the container can sit safely waiting on the vessel.</li>
        <li><strong>Cargo cut-off.</strong> The hard deadline for the loaded container at the gate.</li>
        <li><strong>VGM cut-off.</strong> The deadline for submitting the SOLAS Verified Gross Mass — sometimes the same as the cargo cut, sometimes earlier.</li>
      </ul>
      <p>We schedule pickup of an empty, loading at your facility, and delivery to terminal against all three windows — never just the cargo cut. That's the difference between making the vessel and watching it sail.</p>

      <h2>SOLAS VGM coordination</h2>
      <p>Verified Gross Mass is a SOLAS regulatory requirement. The carrier submits the certified weight before the cut-off so the line can stow the vessel. Cate Freight can submit VGM via the line's portal or via INTTRA, and we'll capture the certified scale weight at pickup if you don't have a certified scale on site.</p>

      <h2>Empty pickup &amp; pre-load staging</h2>
      <p>Export drays usually start with an empty pickup at the terminal or chassis depot. If you need the empty staged at your dock before loading day — for instance because you're loading at 6 AM and the gate doesn't open early enough — we'll pre-pull the empty and drop it overnight. Same idea as an import pre-pull, just upstream.</p>

      <h2>What we need to quote an export drayage move</h2>
      <ul>
        <li>Booking number and steamship line</li>
        <li>Container size, type, and any specialty (reefer set point, OW, OOG)</li>
        <li>Pickup origin (where loading happens)</li>
        <li>Return terminal at SCPA</li>
        <li>ERD, cargo cut, VGM cut</li>
        <li>Commodity, weight, hazmat (with UN# if applicable)</li>
      </ul>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Do you submit VGM for export containers?",
             "Yes. We submit VGM through the line's preferred channel (carrier portal or INTTRA) before the cut-off. If you don't have a certified scale, we'll route through one and capture the weight."),
            ("Can you pre-pull and stage an empty for early-morning export loads?",
             "Yes. Empty pre-pull and overnight staging at your facility is routine for early-morning loaders. We'll pull the empty during the prior gate, drop it on chassis at your dock, and bobtail away."),
            ("What if our export load is overweight?",
             "Tri-axle chassis and state-issued overweight permits handle most overweight export drays in SC. We quote the permit cost up front."),
            ("Can you stage the loaded export if we miss our delivery window?",
             "Yes. If a load runs late or the gate is closed, we can hold the loaded container on chassis at our yard and drop it at the terminal next morning. We'll tell you whether that risks the cut-off or the next vessel."),
        ],
        related=[
            ("Port drayage", "Pickup and return at every SCPA container terminal.", "/services/port-drayage/"),
            ("Overweight drayage", "Tri-axle chassis and permits for heavy exports.", "/services/overweight-drayage/"),
            ("Drayage for forwarders", "Booking visibility and clean PODs back fast.", "/who-we-serve/freight-forwarders/"),
        ],
    ))

    # ---------------- Port-to-warehouse ---------------- #
    out.append(_service_page(
        ctx,
        slug="port-to-warehouse-drayage",
        path="/services/port-to-warehouse-drayage/",
        title="Port-to-Warehouse Drayage in Charleston, SC | Cate Freight",
        meta="Port-to-warehouse drayage from Charleston, SC. Direct moves from SCPA terminals to your DC with appointments confirmed at both ends. Live unload or drop and hook.",
        eyebrow="Port-to-warehouse",
        h1="Port-to-warehouse drayage with appointments confirmed at both ends.",
        intro_html="Most Charleston imports end at a warehouse dock — yours or a 3PL's. Cate Freight runs port-to-warehouse drayage with the appointment booked on both sides before the truck rolls, so the container shows up when your dock is ready and not before.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>Why "port-to-warehouse" deserves its own service</h2>
      <p>Most carriers treat the warehouse delivery like an afterthought — show up, hope for a dock, push the appointment if it slips. That's how containers end up sitting on chassis with the per-diem clock running, or how drivers get bounced from one DC to another all afternoon.</p>
      <p>Cate Freight comes from the warehouse side. We know what an ASN window means, what a dock manager needs to schedule a live unload, and how 3PL receivers expect to be notified. So we book the delivery slot at the consignee, confirm it before the terminal pickup, and tell you the moment something changes.</p>

      <h2>Live unload vs. drop &amp; hook</h2>
      <p>The right choice depends on your unload speed and your chassis cost tolerance:</p>
      <ul>
        <li><strong>Live unload.</strong> Driver stays for the unload. Best when you can crack the doors within an hour of arrival and have crew on dock. No chassis per-diem exposure.</li>
        <li><strong>Drop &amp; hook.</strong> Driver drops on a chassis. You unload on your timeline. Chassis per-diem accrues; we'll quote daily so you can decide.</li>
      </ul>

      <h2>Charleston port-to-warehouse lanes we run constantly</h2>
      <ul>
        <li>Wando Welch / North Charleston / Leatherman → North Charleston, Hanahan, and Ladson DCs along the I-526 corridor</li>
        <li>Wando → Mount Pleasant and Daniel Island 3PL warehouses</li>
        <li>SCPA → Summerville, Goose Creek, and Moncks Corner industrial parks (Berkeley and Dorchester counties)</li>
        <li>SCPA → Ridgeville and the Camp Hall Commerce Park megasite up the I-26 corridor</li>
        <li>SCPA → Columbia distribution-center cluster via I-26</li>
        <li>SCPA → Greenville and Spartanburg manufacturing on I-85</li>
        <li>SCPA → Florence, Hartsville, and the I-95 corridor</li>
      </ul>
      <p>Most of our daily port-to-warehouse work stays inside the tri-county — Charleston, Berkeley, and Dorchester counties — where the receiving docks sit minutes off I-526 and I-26. When the consignee is farther out, the same dispatcher who handles a five-mile run to a North Charleston DC handles the I-26 leg to Ridgeville or the longer pull to the Midlands. It's all <a href="/charleston-drayage/">Charleston drayage</a> to us, whether the box drops in Hanahan or in Berkeley County.</p>
    </div>
  </div>
</section>

<section class="section bg-surface">
  <div class="container">
    <div class="feature-row">
      <div>
        <h2>Communication you can build a plan around</h2>
        <p>Port-to-warehouse drayage breaks down most often at the comms layer — the dispatch that doesn't return calls, the driver whose ETA is "soon." Cate Freight treats communication as part of the move:</p>
        <ul class="checklist">
          <li>Daily morning ETA update for in-flight containers</li>
          <li>Inbound text or email when the driver is en route to the consignee</li>
          <li>POD scanned and emailed back the same day</li>
          <li>One dispatcher per file — you talk to the same person all the way through</li>
        </ul>
      </div>
      <div class="panel">
        <h3>What you should expect on a port-to-warehouse move</h3>
        <ul>
          <li><div><strong>Day -1</strong><span>Release verified, terminal appointment booked, delivery slot confirmed.</span></div></li>
          <li><div><strong>Pickup morning</strong><span>Container pulled, gate transaction captured, driver dispatched.</span></div></li>
          <li><div><strong>In transit</strong><span>GPS-tracked. ETA shared. Any change communicated immediately.</span></div></li>
          <li><div><strong>Delivery</strong><span>Live unload or drop &amp; hook per your spec. Driver waits on signature.</span></div></li>
          <li><div><strong>Same day</strong><span>Signed POD imaged, named to your reference, emailed back.</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Do you book the appointment at the consignee for me?",
             "Yes. If you give us the warehouse contact (or it's on the BOL), we book the delivery slot, confirm it before pickup, and notify you of any change."),
            ("What's the difference between live unload and drop and hook?",
             "Live unload means the driver waits while your team unloads. Drop and hook means the driver leaves the loaded container on a chassis at your dock and bobtails away — you unload on your timeline. Live unload risks driver detention; drop and hook accrues chassis per-diem."),
            ("Can you do port-to-warehouse drayage outside Charleston metro?",
             "Yes. We run regional lanes into Columbia, Greenville, Spartanburg, Florence, Charlotte, Atlanta, and Savannah. Beyond the immediate Southeast we'll quote case by case."),
            ("Do you support 3PL warehouse receiving SOPs?",
             "Yes. We adapt to your inbound SOP — appointment system, ASN format, container number on every comm, photos at delivery if you require them. Tell us what you need and we'll match it."),
        ],
        related=[
            ("Import container drayage", "Releases checked before dispatch, pre-pull when free time is tight.", "/services/import-container-drayage/"),
            ("Drayage for 3PLs", "Built around how warehouse receivers actually run.", "/who-we-serve/3pls/"),
            ("Transload coordination", "When the inland leg is longer than the dray.", "/services/transload-drayage/"),
        ],
    ))

    # ---------------- Transload ---------------- #
    out.append(_service_page(
        ctx,
        slug="transload-drayage",
        path="/services/transload-drayage/",
        title="Transload Drayage and Coordination in Charleston, SC | Cate Freight",
        meta="Transload drayage in Charleston, SC. Container delivery to transload yards plus warehouse coordination — best when the inland leg is much longer than the port-side dray.",
        eyebrow="Transload coordination",
        h1="Transload drayage that closes the per-diem clock the same day.",
        intro_html="Transloading is the right answer when your inland leg is much longer than the dray, when your shipper-of-record needs floor-loaded freight inside a 53', or when you want to return the empty fast and stop per diem cold. Cate Freight delivers to Charleston transload yards and coordinates the cross-dock — including same-day empty return.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What transload looks like in practice</h2>
      <p>A transload is a planned cross-dock: the ocean container is delivered to a transload facility, the contents are unloaded and reloaded onto domestic equipment (53' van, flatbed, or pallet for parcel/LTL), and the empty container is returned same day. The freight then moves inland on a domestic carrier — often cheaper, often faster, almost always more flexible than dragging the ocean box another 800 miles.</p>

      <h2>When transload beats a long-haul dray</h2>
      <ul>
        <li>Inland delivery is more than ~250 miles from Charleston</li>
        <li>You're paying ocean per diem on a slow inland leg</li>
        <li>Your shipper-of-record needs 53' equipment</li>
        <li>The freight breaks down across multiple consignees</li>
        <li>You want palletized freight on parcel or LTL for the last mile</li>
      </ul>

      <h2>How Cate Freight coordinates a transload</h2>
      <ul>
        <li><strong>Drayage to transload yard.</strong> Container delivered with appointment booked.</li>
        <li><strong>Cross-dock coordination.</strong> We work the transload facility on your behalf — pallet count, equipment match, BOL handoff.</li>
        <li><strong>Empty return same day.</strong> Per diem clock stops the same shift the contents come off.</li>
        <li><strong>Inland handoff.</strong> Domestic carrier dispatched against your TMS or via our partners.</li>
        <li><strong>Documentation.</strong> Container EIR, transload BOL, and inland POD all back to you in one package.</li>
      </ul>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Do you operate your own transload warehouse?",
             "Cate Freight is a drayage carrier. We coordinate with established Charleston-area transload facilities and warehouse partners. The advantage is that we treat the warehouse like a customer — because that's the world we came from — so the cross-dock side runs cleanly."),
            ("Can you handle the inland leg after transload?",
             "We'll dispatch the inland leg through our partners or we'll integrate with your TMS so your domestic carrier picks it up. Either way, you get one set of paperwork back."),
            ("How fast does the empty return after transload?",
             "Same day in almost every case. The per-diem clock stops the moment the empty hits the terminal or the line's depot."),
            ("Is transload cheaper than long-haul drayage?",
             "Often, especially over 250 miles, when inland equipment is cheaper than ocean per diem and chassis daily costs combined. We'll do the math both ways for any move you ask us to quote."),
        ],
        related=[
            ("Port-to-warehouse drayage", "Direct delivery when transload doesn't pencil.", "/services/port-to-warehouse-drayage/"),
            ("Import container drayage", "Releases checked before dispatch.", "/services/import-container-drayage/"),
            ("Drayage for 3PLs", "Coordination across inbound and inland.", "/who-we-serve/3pls/"),
        ],
    ))

    # ---------------- Reefer ---------------- #
    out.append(_service_page(
        ctx,
        slug="reefer-drayage",
        path="/services/reefer-drayage/",
        title="Reefer Container Drayage in Charleston, SC | Cate Freight",
        meta="Reefer container drayage in Charleston, SC. Genset chassis, set-point verification, pre-trip inspection. Cold chain stays unbroken from terminal to dock.",
        eyebrow="Reefer drayage",
        h1="Reefer drayage that doesn't break the cold chain.",
        intro_html="Reefer containers don't tolerate sloppy drayage. A wrong set point, a missed pre-trip, or a genset that runs out of fuel mid-haul, and you've got a temperature claim. Cate Freight runs reefer drays with verified set points, pre-trip inspection, and genset chassis sized for the lane.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>How we handle a Charleston reefer drayage</h2>
      <ol>
        <li><strong>Set point verified at terminal.</strong> Driver checks the unit display matches the set point on the booking before the chassis leaves the terminal. Documented.</li>
        <li><strong>Genset checked.</strong> Fuel level, run hours, alarm history. If anything looks off we route to a different genset rather than risk a fail in transit.</li>
        <li><strong>Pre-trip inspection.</strong> Reefer set, supply temperature, and return air noted. Photo record on file.</li>
        <li><strong>In transit.</strong> Genset monitored at any required fuel stops. Set point not changed without written customer instruction.</li>
        <li><strong>Delivery.</strong> Set point and supply temperature confirmed again at the consignee. Noted on the POD.</li>
      </ol>

      <h2>Specialty reefer scenarios we handle</h2>
      <ul>
        <li>Plug-to-plug moves where shore power must be maintained on both sides</li>
        <li>Frozen-to-fresh transitions with controlled set-point ramp</li>
        <li>USDA-monitored cold chain documentation</li>
        <li>Pharma reefer with strict tolerance bands</li>
        <li>Reefer transload with same-day cold-side cross-dock</li>
      </ul>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Do you carry genset chassis for Charleston reefer drayage?",
             "Yes. We use genset chassis configurations sized for the lane. For long lanes we'll specify a higher fuel capacity or plan a fueling stop in advance."),
            ("How is the set point verified?",
             "At pickup, the driver matches the unit display to the booking set point and supply temperature. We document it before the chassis leaves the gate. The same check happens again at delivery and is recorded on the POD."),
            ("What if the reefer fails in transit?",
             "We have alarm protocols and contact you immediately if the unit alarms. We don't change the set point without written instruction from the shipper or consignee."),
            ("Can you run plug-to-plug reefer drays?",
             "Yes. When shore power must be maintained on both ends, we plan the move so power-down time is minimized and document the plug-out and plug-in times."),
        ],
        related=[
            ("Import container drayage", "Releases checked before dispatch.", "/services/import-container-drayage/"),
            ("Port-to-warehouse drayage", "Appointments confirmed at both ends.", "/services/port-to-warehouse-drayage/"),
            ("Overweight drayage", "When reefer cargo runs heavy.", "/services/overweight-drayage/"),
        ],
    ))

    # ---------------- Overweight ---------------- #
    out.append(_service_page(
        ctx,
        slug="overweight-drayage",
        path="/services/overweight-drayage/",
        title="Overweight & OOG Container Drayage in Charleston, SC | Cate Freight",
        meta="Overweight container drayage in Charleston, SC. Tri-axle chassis, state permits, and the experience to handle 60,000+ lb containers without breaking the chain.",
        eyebrow="Overweight drayage",
        h1="Overweight container drayage with the right chassis and the right permits.",
        intro_html="Overweight drayage isn't just a heavier load — it's a different equipment configuration, a permit, and sometimes a route restriction. Cate Freight runs tri-axle chassis, pulls state permits where required, and routes around the bridges and roads that don't accept the weight.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What "overweight" means in Charleston drayage</h2>
      <p>A standard 5-axle tractor-chassis combination in South Carolina is legal up to 80,000 lb gross — translating to roughly 44,000 lb of payload in a 40' container. Anything above that gross is overweight, and most 20' containers loaded to international spec end up there.</p>
      <p>Tri-axle chassis push the legal weight up to roughly 60,000 lb of payload with state permits, depending on configuration. We carry tri-axle equipment specifically because Southeast manufacturing flows (paper, metals, ceramics, food ingredients) regularly run heavy.</p>

      <h2>Permits, routes, and the boring details that matter</h2>
      <ul>
        <li>South Carolina overweight permits — pulled by us, billed pass-through</li>
        <li>Bridge restriction awareness on heavy lanes (we route around weight-restricted bridges)</li>
        <li>Tri-axle availability scheduled in advance, not at the gate</li>
        <li>Driver match — overweight runs go to the drivers used to handling the equipment</li>
      </ul>

      <h2>The SCDOT 100,000 lb permit — Charleston's overweight container ceiling</h2>
      <p>South Carolina carries one of the highest container weight allowances on the East Coast. SCDOT's Oversize/Overweight Permit Office issues a permit that lets an international shipping container move by truck at up to <strong>100,000 lb gross vehicle weight</strong> — well above the 80,000 lb standard legal limit, and up from the 90,000 lb ceiling the state allowed before. For an importer or 3PL routing heavy cargo, that headroom is one of the quieter advantages of <a href="/charleston-drayage/">Charleston drayage</a>.</p>
      <p>On an overweight container transport move out of Charleston, the mechanics are straightforward: a tri-axle chassis carries the extra weight, we pull the SCDOT container permit before dispatch, and we bill it pass-through with no markup. A loaded box that would be illegal on a standard 5-axle then moves legally to a Berkeley, Dorchester, or Charleston County warehouse, or up the I-26 corridor toward Columbia and the Upstate. If a container is heavy enough to clear even the 100,000 lb permit, it crosses into superload territory — a separate permit, a route survey, and usually an escort — and we flag that before you book, not after.</p>

      <h2>Out-of-gauge (OOG) containers</h2>
      <p>OOG cargo — loads that exceed the standard container's internal dimensions and ride flat-rack or open-top — need extra coordination: tarping if open-top, tie-down inspection on flat-rack, sometimes pilot car or escort if oversized. We handle the equipment match and the route plan, and we'll tell you upfront when escort costs are on the bill.</p>
    </div>
  </div>
</section>
""",
        faqs=[
            ("How heavy can a Charleston drayage container legally be?",
             "On a standard 5-axle, payload is roughly 44,000 lb. Tri-axle chassis with state-issued overweight permits push that to roughly 60,000 lb. Above that, you're into specialty equipment territory."),
            ("Do you pull the overweight permit yourself?",
             "Yes. We pull the SC permit when required and bill it pass-through with no markup."),
            ("Does South Carolina allow heavier containers than the 80,000 lb legal limit?",
             "Yes. SCDOT's Oversize/Overweight Permit Office issues a permit that allows international shipping containers to move by truck at up to 100,000 lb gross vehicle weight — raised from the previous 90,000 lb ceiling. On a tri-axle chassis with that permit pulled, a heavy import or export container moves legally out of the Port of Charleston. We pull the permit before dispatch and bill it pass-through."),
            ("Can you run flat-rack or open-top containers?",
             "Yes. We pull flat-rack and open-top equipment for OOG cargo, including tarping for open-top and tie-down inspection for flat-rack."),
            ("What if my route has bridge weight restrictions?",
             "We route around them. We monitor SC and adjacent-state bridge restrictions and adjust the lane plan when an overweight move can't take the direct interstate route."),
        ],
        related=[
            ("Port drayage", "Pickup and return at every SCPA terminal.", "/services/port-drayage/"),
            ("Export container drayage", "Heavy exports with VGM and ERD coordination.", "/services/export-container-drayage/"),
            ("Reefer drayage", "Heavy reefer freight on tri-axle.", "/services/reefer-drayage/"),
        ],
    ))

    return out
