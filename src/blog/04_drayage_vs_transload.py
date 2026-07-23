"""Article: Drayage vs transload vs intermodal."""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("Drayage vs transload vs intermodal", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Decision guide &middot; 6 min read</span>
    <h1>Drayage vs transload vs intermodal: which one do you actually need?</h1>
    <p>Three modes that move a Charleston import container inland, with the rules of thumb for which one wins on which lane.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Published April 2026 &middot; Cate Freight Charleston operations team</p>

      <p>If you're importing into Charleston with an inland destination, you have three ways to move the freight. Knowing when each one wins saves real money — and it isn't always obvious.</p>

      <h2>Definitions, fast</h2>
      <ul>
        <li><strong>Drayage (long-haul).</strong> The same ocean container is dragged the whole way to the consignee on a chassis. One handoff: terminal pickup → consignee delivery → empty return.</li>
        <li><strong>Transload.</strong> The ocean container is delivered to a Charleston-area transload facility, the contents are cross-docked onto domestic equipment (53' van, flatbed, or pallet for parcel/LTL), and the empty container is returned same day. The freight then continues inland on domestic equipment.</li>
        <li><strong>Intermodal rail.</strong> The container moves on a train for the long-haul portion. Drayage carriers handle the truck legs at each end of the rail move.</li>
      </ul>

      <h2>The decision rules</h2>

      <h3>Long-haul drayage wins when:</h3>
      <ul>
        <li>The inland destination is within ~250 miles of Charleston (Atlanta, Charlotte, Columbia, Greenville-Spartanburg).</li>
        <li>The container is going to a single consignee with one delivery address.</li>
        <li>The consignee has a dock and unloads from the ocean container directly.</li>
        <li>Time is tight and you don't want a cross-dock handoff in the middle.</li>
      </ul>

      <h3>Transload wins when:</h3>
      <ul>
        <li>The inland destination is more than ~250 miles from Charleston.</li>
        <li>The freight breaks across multiple consignees (one ocean container = several inland deliveries).</li>
        <li>You're paying ocean per diem on a slow inland leg and the math says cross-docking saves more than the extra handling cost.</li>
        <li>Your shipper-of-record needs 53' equipment for the inland leg (some big-box retailers).</li>
        <li>The freight needs to break into LTL or parcel for the last mile.</li>
      </ul>

      <h3>Intermodal rail wins when:</h3>
      <ul>
        <li>The inland destination is more than ~600-800 miles away.</li>
        <li>You're not in a hurry — rail adds days to transit.</li>
        <li>The freight is dense and rail rates beat over-the-road rates by enough to absorb the extra handling and time.</li>
        <li>You're moving steady volume to a single intermodal-served destination (Memphis, Dallas, Chicago, etc.).</li>
      </ul>

      <p>Charleston is the asterisk on intermodal — until the Navy Base Intermodal Facility opens in 2026, there's no on-dock or near-dock rail at Charleston, so intermodal moves require a long dray to a railhead before the rail leg starts. Once NBIF is open, intermodal will become a much more competitive option for Charleston imports going to the Midwest.</p>

      <h2>Worked examples</h2>

      <h3>Charleston → Greenville, SC (220 miles)</h3>
      <p>Long-haul drayage, almost always. The mileage is short enough that the dray rate is reasonable. Cross-docking adds cost without adding much value. Single consignee, single dray, done.</p>

      <h3>Charleston → Memphis, TN (700 miles)</h3>
      <p>Transload usually wins. Charleston to Memphis on the ocean container costs more in linehaul, per diem, and chassis daily than transload + 53' van or rail — and you stop the per diem clock the same day instead of in three days.</p>

      <h3>Charleston → 18 retail DCs across the Southeast</h3>
      <p>Transload, every time. One ocean container splits at the transload facility into 18 LTL or palletized loads. Trying to drag the ocean container around to all 18 stops would cost a fortune and probably violate the chassis pool's daily limits.</p>

      <h3>Charleston → Chicago, IL (950 miles)</h3>
      <p>Today, transload + 53' van. After NBIF opens, intermodal rail likely becomes the better answer — you skip the long dray to the railhead and the rail rate to Chicago is very competitive.</p>

      <h2>What the math actually looks like</h2>
      <p>The components for any inland move are:</p>
      <ul>
        <li>The dray itself (or the rail leg, plus drays at each end)</li>
        <li>Chassis daily fees</li>
        <li>Container per diem (held by the steamship line until the empty returns)</li>
        <li>Terminal demurrage if free time runs out</li>
        <li>Cross-dock or transload labor (if applicable)</li>
        <li>Inland linehaul on domestic equipment (if applicable)</li>
      </ul>
      <p>Long-haul drayage is dominated by the chassis daily and the per diem. Transload is dominated by the labor and the inland linehaul. Intermodal is dominated by rail rate plus the two end drays. The right answer is whichever option has the lowest sum of these — not whichever option has the lowest single line item.</p>

      <h2>Cate Freight's recommendation engine</h2>
      <p>For any move you give us, we'll quote the <a href="/charleston-drayage/">Charleston drayage</a> version straight up and tell you when <a href="/services/transload-drayage/">transload</a> likely beats it. We won't push you toward transload (or away from it) for our own reasons — we'd rather lose a long dray and earn a referral than hand you a quote you should have rejected.</p>
      <p><a href="/quote/">Send us a move</a> and we'll show our math.</p>
    </article>
  </div>
</section>

<section class="section faq">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">People also ask</p>
      <h2>Drayage vs transload questions</h2>
    </div>
    <div class="faq-list">
      <details class="faq-item"><summary>Is transloading cheaper than drayage?</summary><div class="faq-answer">Only past a distance and complexity threshold. Inside roughly 250 miles of Charleston — Columbia, Greenville-Spartanburg, Charlotte, Atlanta — long-haul drayage on the ocean container usually wins because cross-dock labor adds cost without adding value. Past ~250 miles, or when one container splits across multiple consignees, transload usually wins: you stop the container per diem and chassis clocks the same day instead of days later. Compare the full sum — dray, chassis daily, per diem, cross-dock labor, inland linehaul — not any single line item.</div></details>
      <details class="faq-item"><summary>How does a transload work at the Port of Charleston?</summary><div class="faq-answer">The ocean container is drayed from the SCPA terminal to a Charleston-area transload facility, the freight is cross-docked onto domestic equipment (53' van, flatbed, or pallets for LTL/parcel), and the empty container goes back to the terminal the same day the box is stripped. That same-day empty return is the whole point: it stops steamship-line per diem and chassis daily fees while the freight continues inland on domestic equipment. See our <a href="/services/transload-drayage/">transload drayage service</a> for how we coordinate the dray leg and the cross-dock.</div></details>
      <details class="faq-item"><summary>Does the Port of Charleston have on-dock rail for intermodal?</summary><div class="faq-answer">Not yet. Until the Navy Base Intermodal Facility (NBIF) opens, Charleston has no on-dock or near-dock rail, so an intermodal move requires a dray from the terminal to a railhead before the rail leg starts — which is why transload plus 53' van currently beats rail on most Charleston-to-Midwest lanes. Once NBIF is operating, intermodal becomes far more competitive for Midwest-bound Charleston imports.</div></details>
      <details class="faq-item"><summary>When should one import container be split across multiple deliveries?</summary><div class="faq-answer">Whenever one ocean container has more than one inland destination, transload is almost always the answer. Dragging the same container to several stops runs up mileage, chassis daily fees, and per diem, and can bump against chassis-pool usage limits. Cross-docking at a Charleston facility splits the freight into palletized LTL or parcel moves in one touch, and the empty returns while the freight fans out.</div></details>
    </div>
  </div>
</section>
"""

    faq_items = [
        ("Is transloading cheaper than drayage?", "Only past a distance and complexity threshold. Inside roughly 250 miles of Charleston — Columbia, Greenville-Spartanburg, Charlotte, Atlanta — long-haul drayage on the ocean container usually wins because cross-dock labor adds cost without adding value. Past ~250 miles, or when one container splits across multiple consignees, transload usually wins: you stop the container per diem and chassis clocks the same day instead of days later. Compare the full sum — dray, chassis daily, per diem, cross-dock labor, inland linehaul — not any single line item."),
        ("How does a transload work at the Port of Charleston?", "The ocean container is drayed from the SCPA terminal to a Charleston-area transload facility, the freight is cross-docked onto domestic equipment (53' van, flatbed, or pallets for LTL/parcel), and the empty container goes back to the terminal the same day the box is stripped. That same-day empty return stops steamship-line per diem and chassis daily fees while the freight continues inland on domestic equipment."),
        ("Does the Port of Charleston have on-dock rail for intermodal?", "Not yet. Until the Navy Base Intermodal Facility (NBIF) opens, Charleston has no on-dock or near-dock rail, so an intermodal move requires a dray from the terminal to a railhead before the rail leg starts — which is why transload plus 53' van currently beats rail on most Charleston-to-Midwest lanes. Once NBIF is operating, intermodal becomes far more competitive for Midwest-bound Charleston imports."),
        ("When should one import container be split across multiple deliveries?", "Whenever one ocean container has more than one inland destination, transload is almost always the answer. Dragging the same container to several stops runs up mileage, chassis daily fees, and per diem, and can bump against chassis-pool usage limits. Cross-docking at a Charleston facility splits the freight into palletized LTL or parcel moves in one touch, and the empty returns while the freight fans out."),
    ]

    schema = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Drayage vs transload vs intermodal: which one do you actually need?",
        "description": "Three modes that move a Charleston import inland, with rules of thumb for when each wins.",
        "author": {"@type": "Organization", "name": "Cate Freight"},
        "publisher": {"@id": f"{site_url}/#org"},
        "image": f"{site_url}/og-default.png",
        "datePublished": "2026-04-25",
        "dateModified": ctx["last_modified"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/drayage-vs-transload-intermodal/"},
    }]

    schema.append({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_items
        ],
    })

    html = render(
        slug="drayage-vs-transload-intermodal",
        path="/resources/drayage-vs-transload-intermodal/",
        title="Drayage vs Transload vs Intermodal — Which Do You Need? | Cate Freight",
        meta_description="When long-haul drayage wins, when transload wins, when intermodal rail wins — practical rules of thumb for Charleston imports going inland.",
        h1="Drayage vs transload vs intermodal: which one do you actually need?",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/drayage-vs-transload-intermodal/index.html", html)
