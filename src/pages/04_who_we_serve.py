"""Who-we-serve hub + audience pages."""


def _audience_page(ctx, *, slug, path, eyebrow, title, meta, h1, intro_html, sections_html, faqs, related):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    faq_block = ctx["faq_block"]
    site_url = ctx["site_url"]
    phone_tel = ctx["phone_tel"]
    phone_display = ctx["phone_display"]

    crumbs = [("Home", "/"), ("Who We Serve", "/who-we-serve/"), (eyebrow, "")]
    hero = f"""
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Charleston, SC drayage</span>
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
        f'<div class="card"><h3>{n}</h3><p>{d}</p><a class="card-link" href="{h}">Read more</a></div>'
        for n, d, h in related
    )
    related_block = f"""
<section class="section bg-surface">
  <div class="container">
    <div class="section-head"><p class="eyebrow">Related services</p><h2>How this works inside Cate Freight.</h2></div>
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
            "serviceType": "Container drayage",
            "audience": {"@type": "Audience", "audienceType": eyebrow},
            "provider": {"@id": f"{site_url}/#org"},
            "areaServed": {"@type": "City", "name": "Charleston, SC"},
            "description": meta,
        },
        faq_schema,
    ]

    html = render(
        slug=slug,
        path=path,
        title=title,
        meta_description=meta,
        h1=h1,
        body_html=body,
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="who-we-serve",
    )
    return (path + "index.html", html)


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    out = []

    # Hub
    crumbs_hub = [("Home", "/"), ("Who We Serve", "")]
    hub_hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Built around the receiver</span>
    <h1>Who Cate Freight is built for.</h1>
    <p>Drayage is a relationship business — and the people running drayage every week have specific needs. Here's how Cate Freight shapes its <a href="/charleston-drayage/">Charleston drayage</a> operation around 3PLs, freight forwarders, customs brokers, and direct importers and exporters.</p>
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
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-warehouse"/></svg></div><h2>3PLs &amp; warehouses</h2><p>Drop-and-hook coordination, ASN-friendly windows, dispatcher who answers when the dock is waiting on a 40HC.</p><a class="card-link" href="/who-we-serve/3pls/">Drayage for 3PLs</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-globe"/></svg></div><h2>Freight forwarders</h2><p>Booking visibility, terminal-aware pickup timing, clean PODs back fast.</p><a class="card-link" href="/who-we-serve/freight-forwarders/">Drayage for forwarders</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-clipboard"/></svg></div><h2>Customs brokers</h2><p>Release-status discipline. We don't roll until customs and freight are released.</p><a class="card-link" href="/who-we-serve/customs-brokers/">Drayage for brokers</a></div>
      <div class="card"><div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><use href="#i-package"/></svg></div><h2>Importers &amp; exporters</h2><p>Direct-shipper relationships with one number to call.</p><a class="card-link" href="/who-we-serve/importers-exporters/">Direct shippers</a></div>
    </div>
  </div>
</section>
"""

    out.append((
        "/who-we-serve/index.html",
        render(
            slug="who-we-serve",
            path="/who-we-serve/",
            title="Drayage for 3PLs, Forwarders, Brokers, and Direct Shippers | Cate Freight",
            meta_description="Cate Freight serves 3PLs, freight forwarders, customs brokers, and direct importers and exporters with Charleston drayage built around how each group actually operates.",
            h1="Who Cate Freight is built for.",
            body_html=breadcrumb_bar(crumbs_hub) + hub_hero + hub_grid + cta_banner(),
            breadcrumbs=crumbs_hub,
            nav_active="who-we-serve",
        ),
    ))

    # 3PL
    out.append(_audience_page(
        ctx,
        slug="3pls",
        path="/who-we-serve/3pls/",
        eyebrow="3PLs & warehouses",
        title="Drayage for 3PLs and Warehouses in Charleston, SC | Cate Freight",
        meta="Charleston drayage built for 3PLs and warehouse operators. ASN-friendly windows, drop-and-hook discipline, container number on every comm, PODs back same day.",
        h1="Drayage for 3PLs that actually fits warehouse operations.",
        intro_html="Most drayage carriers were built around the truck. Cate Freight came out of the warehouse and 3PL world, so our <a href=\"/charleston-drayage/\">Charleston drayage</a> operation is built around how receiving actually runs. We know what an inbound SOP looks like, why dock managers care about appointment punctuality, and how a 3PL's customer judges them on receiving accuracy.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What 3PL receivers should expect from a Charleston drayage carrier</h2>
      <ul>
        <li><strong>Container number on every comm.</strong> Email subject lines lead with the container number. Every PDF is named with the container number. Your receiving system can match without manual rework.</li>
        <li><strong>ASN-friendly arrival windows.</strong> If you give us a window, we hit it. If we can't, we tell you the day before, not the morning of.</li>
        <li><strong>Drop-and-hook discipline.</strong> Drops are scheduled. Empty pickups are scheduled. Nothing sits on your yard guessing.</li>
        <li><strong>Same-day POD imaging.</strong> Signed BOL imaged, named with the container number, emailed back the day of delivery.</li>
        <li><strong>One dispatcher per file.</strong> Your warehouse manager isn't bouncing between people. The person who quoted runs the whole move.</li>
      </ul>

      <h2>How we plug into your inbound SOP</h2>
      <p>Tell us how your receiving runs. We'll match it. That includes:</p>
      <ul>
        <li>Container number on email subjects, PDFs, and ETA notifications</li>
        <li>BOL formatted to your customer's spec (line-itemed, palletized count, etc.)</li>
        <li>Photos at delivery if your customer requires them</li>
        <li>Door assignment honored when you provide it on the appointment</li>
        <li>Visibility data into your TMS — we can output container status to email, EDI, or a feed your TMS reads</li>
      </ul>

      <h2>The drop-and-hook playbook</h2>
      <p>Drop-and-hook is the cleanest delivery model for a 3PL with steady inbound volume. The driver drops the loaded container on a chassis at your dock, bobtails away, and we come back for the empty per your schedule. Zero driver detention. You unload on your timeline. Chassis per-diem accrues; we'll quote daily.</p>

      <h2>Drayage to warehouses across Charleston's industrial corridors</h2>
      <p>Most of the 3PL and contract-warehouse floor space in the Charleston market sits along a handful of corridors, and we run them daily: Palmetto Commerce Parkway and the Ashley Phosphate corridor in North Charleston, Ladson, the Jedburg Road cluster outside Summerville, the Camp Hall build-out near Ridgeville, and Bushy Park in Goose Creek. From Wando Welch, North Charleston, or Hugh Leatherman terminal, these are short, repeatable drays — the kind where a carrier that confirms releases and holds ASN windows earns the standing appointment. If your building sits further out — Orangeburg, Columbia, or up the I-26 corridor toward the Upstate — see our <a href="/coverage/">coverage area</a> for lane-by-lane turn times.</p>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Can you match our 3PL's customer SOP at delivery?",
             "Yes. Container number on the BOL, photos at delivery, dock-door assignments, signature requirements — tell us the SOP and we'll run it. If your 3PL customer audits, we'll fit the audit."),
            ("Do you support drop-and-hook for steady-volume 3PLs?",
             "Yes. We carry chassis pool relationships across TRAC, DCLI, and Flexi-Van. For dedicated drop-and-hook customers we'll hold equipment to keep your operation flowing."),
            ("Will you communicate ETAs ahead of arrival?",
             "Daily morning ETA update for in-flight containers. Inbound text or email when the driver is en route. Same-day POD."),
            ("Can you handle peak-season volume?",
             "We're sized to flex. We'll be honest with you about capacity — if a peak push is too much for us alone, we'll tell you up front rather than miss a window."),
            ("Can you run drayage to my warehouse in Charleston?",
             "Almost certainly — we deliver daily along every major Charleston warehouse corridor: Palmetto Commerce Parkway, Ashley Phosphate, Ladson, Jedburg, Camp Hall near Ridgeville, and Bushy Park in Goose Creek. Send the address and we'll confirm the lane and quote it inside the hour during business hours."),
        ],
        related=[
            ("Port-to-warehouse drayage", "Appointments confirmed at both ends.", "/services/port-to-warehouse-drayage/"),
            ("Import container drayage", "Releases verified before dispatch.", "/services/import-container-drayage/"),
            ("Transload coordination", "Cross-dock for inland legs over 250 miles.", "/services/transload-drayage/"),
        ],
    ))

    # Forwarders
    out.append(_audience_page(
        ctx,
        slug="freight-forwarders",
        path="/who-we-serve/freight-forwarders/",
        eyebrow="Freight forwarders",
        title="Charleston Drayage for Freight Forwarders | Cate Freight",
        meta="Charleston drayage built for freight forwarders. Booking visibility, release-aware pickup timing, clean PODs back the day of delivery, and one point of contact per file.",
        h1="A drayage carrier your forwarder operations can actually plan around.",
        intro_html="Forwarders live and die by file accuracy. The <a href=\"/charleston-drayage/\">Charleston drayage</a> leg of a move is where files get sloppy: missed releases, ETAs that don't update, PODs that take three follow-ups to retrieve. Cate Freight runs the dray side cleanly so you can close the file the same day delivery happens.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What forwarders need that most carriers don't deliver</h2>
      <ul>
        <li><strong>Release awareness.</strong> We don't just check the booking — we check freight, customs, and line holds, and we tell you when something is missing.</li>
        <li><strong>HBL/MBL tracking.</strong> File references match yours. Container number, MBL, and your HBL on every comm.</li>
        <li><strong>Predictable POD turnaround.</strong> Signed POD imaged and emailed back the day of delivery. Imaged copies named with your file reference.</li>
        <li><strong>Direct dispatcher contact.</strong> One person runs the file. You don't get bounced.</li>
        <li><strong>Honest accessorials.</strong> Chassis splits, fuel, OW permits — quoted up front. Detention pass-through. No surprise lines.</li>
      </ul>

      <h2>How we work with forwarder operations teams</h2>
      <p>Most forwarders we work with email a delivery order with the booking, container, MBL, and consignee. We confirm release status against the line, book the terminal appointment, schedule the delivery, and run the move. We can also pull from your TMS or operations system if you have one — give us the access spec and we'll match it.</p>

      <h2>What happens when something goes wrong</h2>
      <p>It will. Vessels are late. Releases get held up. Equipment doesn't show. The point isn't perfection; it's communication. You'll hear about it the moment we hear about it, with a recommendation rather than a question.</p>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Will you accept delivery orders directly from our ops team?",
             "Yes. Email or TMS, whichever your team uses. We'll match your file reference format and return PODs against it."),
            ("Can you handle multiple file references per move?",
             "Yes. HBL, MBL, your file number, the customer's PO — give us all of them and we'll carry them through to the BOL and POD."),
            ("Do you charge accessorials we won't see coming?",
             "No. Chassis splits and overweight permits are quoted up front. Detention is pass-through and only billed when actually triggered. You see the breakdown."),
            ("Can you support a forwarder with multiple Charleston imports per week?",
             "Yes. Recurring forwarder volume is exactly what we're sized for. Set up a standing dispatch arrangement and you'll get faster quotes and predictable handling."),
        ],
        related=[
            ("Import container drayage", "Releases verified before dispatch.", "/services/import-container-drayage/"),
            ("Export container drayage", "ERD-aware scheduling and VGM coordination.", "/services/export-container-drayage/"),
            ("Drayage for customs brokers", "Release discipline upstream of the dray.", "/who-we-serve/customs-brokers/"),
        ],
    ))

    # Customs brokers
    out.append(_audience_page(
        ctx,
        slug="customs-brokers",
        path="/who-we-serve/customs-brokers/",
        eyebrow="Customs brokers",
        title="Charleston Drayage for Customs Brokers | Cate Freight",
        meta="Charleston drayage that respects the customs release. We don't roll until customs, freight, and line holds are clear. Clean handoffs to your importer customers.",
        h1="Drayage that respects the customs file.",
        intro_html="Customs brokers spend a lot of time fixing problems caused by <a href=\"/charleston-drayage/\">Charleston drayage</a> carriers who didn't wait for the release. Cate Freight is the opposite — we don't dispatch until 1C is on file, freight is released, and line holds are lifted. Boring, predictable, and exactly what your importer customers need.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>How we coordinate with your customs entry</h2>
      <ul>
        <li><strong>1C verification before dispatch.</strong> No truck rolls until customs release is in. Period.</li>
        <li><strong>Direct broker contact.</strong> If you're our customer's broker we'll deal directly with you on release timing and any exam issues.</li>
        <li><strong>Hold awareness.</strong> Freight holds, line holds, demurrage holds — we check before sending the driver to the gate.</li>
        <li><strong>EIR back to you.</strong> Equipment Interchange Receipt back the same day so your file closes cleanly.</li>
      </ul>

      <h2>What we won't do</h2>
      <ul>
        <li>Pretend release is in when it isn't to take the move</li>
        <li>Run on a "we'll deal with it at the gate" basis</li>
        <li>Hand the importer a sloppy file your team has to clean up</li>
      </ul>

      <h2>Exam (CET, MET) handling</h2>
      <p>If a container is selected for exam, we route it to the assigned facility, capture the EIR, and coordinate the post-exam pickup so demurrage exposure stays bounded. We'll also notify you immediately so the file can be flagged on your side.</p>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Will you wait for customs release before dispatching?",
             "Always. We don't run dry. If 1C isn't in, we don't put a truck on it."),
            ("Can you handle CET / MET exams?",
             "Yes. We route to the assigned exam facility, capture the EIR, and coordinate the post-exam pickup."),
            ("Will you communicate directly with us as the broker?",
             "Yes. If your importer asks us to coordinate with their broker, we'll work the release-status piece directly with you. EIR comes back same day."),
            ("How do you handle a hold we didn't see coming?",
             "We check freight, customs, and line holds before dispatch. If something appears between our check and the gate, the driver waits or returns dry — billed as a dry-run accessorial — and we work the hold with you before the next attempt."),
        ],
        related=[
            ("Import container drayage", "Releases checked, demurrage managed.", "/services/import-container-drayage/"),
            ("Drayage for forwarders", "When the broker is part of a forwarder file.", "/who-we-serve/freight-forwarders/"),
            ("Port drayage", "Pickup discipline at every SCPA terminal.", "/services/port-drayage/"),
        ],
    ))

    # Direct shippers
    out.append(_audience_page(
        ctx,
        slug="importers-exporters",
        path="/who-we-serve/importers-exporters/",
        eyebrow="Importers & exporters",
        title="Charleston Drayage for Direct Importers and Exporters | Cate Freight",
        meta="Charleston drayage for direct importers and exporters. One number to call. No middleman. Releases verified, paperwork clean, PODs back the day of delivery.",
        h1="Drayage for shippers who'd rather call the carrier directly.",
        intro_html="Some importers and exporters work through a forwarder or 3PL. Some prefer to deal directly with the <a href=\"/charleston-drayage/\">Charleston drayage</a> carrier. Cate Freight handles both — but we're particularly good for direct shippers who want operational visibility, no broker layer in the way, and a single dispatcher who knows their account.",
        sections_html="""
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What direct shippers get with Cate Freight</h2>
      <ul>
        <li><strong>One dispatcher per account.</strong> The person who quoted is the person who runs the move.</li>
        <li><strong>Quote inside the hour.</strong> Business hours. Off-hours, by next morning.</li>
        <li><strong>Operational visibility.</strong> Where the container is, when it's gating, when it's delivering — all in one email thread.</li>
        <li><strong>Direct customs broker handoff.</strong> If you have a broker, we'll work directly with them on release timing.</li>
        <li><strong>Honest accessorials.</strong> Chassis, fuel, OW permits — quoted up front, no surprise lines.</li>
      </ul>

      <h2>Setting up a recurring drayage relationship</h2>
      <p>If you're moving Charleston volume every week, set up a standing dispatch arrangement and you'll get:</p>
      <ul>
        <li>Faster quotes (we already know your typical fields)</li>
        <li>Equipment commitment for steady drop-and-hook flows</li>
        <li>Standardized POD format matched to your records system</li>
        <li>One monthly invoice with line-item detail</li>
        <li>A direct line to dispatch — not a routing tree</li>
      </ul>
    </div>
  </div>
</section>
""",
        faqs=[
            ("Do you work with direct importers without a freight forwarder?",
             "Yes. Many of our customers are direct importers and exporters. The dispatch process is the same — booking, release check, terminal appointment, delivery — minus the forwarder layer."),
            ("Can you handle our customs broker handoff for us?",
             "Yes. Tell us your broker's contact details and we'll work the release-status piece directly with them."),
            ("Can we set up recurring weekly drayage with Cate Freight?",
             "Absolutely. Recurring volume gets faster quotes, equipment commitment, and standardized handling. Tell us your typical move profile and we'll structure the arrangement."),
            ("Do you offer monthly invoicing with line-item detail?",
             "Yes. Monthly aging by reference, with chassis, fuel, accessorial, and detention broken out so AP and your customs broker can audit cleanly."),
        ],
        related=[
            ("Import container drayage", "Releases checked before dispatch.", "/services/import-container-drayage/"),
            ("Export container drayage", "ERD and VGM handled.", "/services/export-container-drayage/"),
            ("Port-to-warehouse drayage", "Direct port-to-DC moves.", "/services/port-to-warehouse-drayage/"),
        ],
    ))

    return out
