"""Article: What is drayage?"""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("What is drayage?", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Drayage 101 &middot; 4 min read</span>
    <h1>What is drayage?</h1>
    <p>The simplest accurate definition, why the word exists, and where drayage ends and other transport modes begin.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Published April 2026 &middot; Cate Freight Charleston operations team</p>

      <p><strong>Drayage is the short-distance trucking of an ocean shipping container.</strong> Almost always, it's the move that takes a container from a port marine terminal to a nearby destination — a warehouse, transload yard, intermodal rail ramp, or shipper's loading dock — or the move that takes the container back to the port. That's it.</p>

      <h2>Where the word comes from</h2>
      <p>"Drayage" is from the word "dray," a heavy cart used to haul goods in the era before motor trucks. When ports needed a word for the short-haul carting of containers between the docks and the city behind them, "drayage" already existed and stuck. It's still the term every steamship line, freight forwarder, customs broker, and shipper uses today.</p>

      <h2>What drayage is not</h2>
      <ul>
        <li><strong>It's not long-haul trucking.</strong> A 1,800-mile freight move from Los Angeles to New York is not drayage. Drayage is short by definition.</li>
        <li><strong>It's not intermodal rail.</strong> Intermodal is when the container moves on a train; drayage is the truck legs at either end of an intermodal move.</li>
        <li><strong>It's not the ocean leg.</strong> Drayage starts when the container hits the chassis at the port — never on the water.</li>
      </ul>

      <h2>The two main flavors</h2>
      <h3>Import drayage</h3>
      <p>The container is unloaded from a vessel, released by customs and the steamship line, picked up by a drayage truck, and delivered to its inland destination. Empty container goes back to the line later.</p>

      <h3>Export drayage</h3>
      <p>The empty container is picked up at the port (or a depot), driven to the shipper's facility for loading, then driven back to the port and dropped at the terminal before the vessel's cut-off.</p>

      <h2>Why drayage matters more than people realize</h2>
      <p>Sea freight is dominated by economies of scale — gigantic ships moving thousands of containers at a time. Drayage is the opposite: a single tractor pulling a single chassis with a single container. It's the most expensive leg of the journey per mile, and it's the leg most likely to determine whether the whole shipment runs on time. The ocean carrier can't fix a missed delivery window. The drayage carrier can.</p>

      <p>It's also where most accessorial costs accumulate. Demurrage, detention, chassis splits, fuel surcharges, overweight permits, hazmat charges — these all happen at the drayage layer. A sharp drayage carrier prevents most of them. A sloppy one creates them.</p>

      <h2>What "drayage" looks like in Charleston</h2>
      <p>At the Port of Charleston, drayage is the only mode that moves your container at all — Charleston is the only major East Coast port without on-dock or near-dock rail (the Navy Base Intermodal Facility is finally arriving in 2026). Every container in or out of Charleston is on a dray truck for at least the first or last 5–500 miles of its journey. That makes Charleston a more drayage-intensive port than Norfolk, Savannah, or New York — and makes the difference between a sharp drayman and a sloppy one painfully visible.</p>

      <h2>Cate Freight's role</h2>
      <p>We're a Charleston, SC drayage carrier. We pull from all three SCPA container terminals — Wando Welch, North Charleston, and Hugh Leatherman — and run drays into warehouses, transload yards, and consignees across South Carolina, Georgia, and the Carolinas. Read our <a href="/charleston-drayage/">Charleston drayage page</a> for specifics on how the operation runs.</p>
    </article>
  </div>
</section>

<section class="section faq">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">People also ask</p>
      <h2>Drayage questions, answered</h2>
    </div>
    <div class="faq-list">
      <details class="faq-item"><summary>What is the difference between drayage and trucking?</summary><div class="faq-answer">Drayage is a specific kind of trucking: the short-haul move of a loaded or empty ocean shipping container to or from a port, rail ramp, or container yard. It requires a chassis, a TWIC-carded driver, and familiarity with terminal appointment systems. Over-the-road trucking is the broader category and usually involves a dry van or flatbed moving palletized freight between warehouses.</div></details>
      <details class="faq-item"><summary>What is the difference between drayage and intermodal?</summary><div class="faq-answer">Intermodal is when an ocean container moves on rail between two inland points. Drayage is the truck leg at either end of that rail move — the dray from the port to the rail ramp, and the dray from the destination ramp to the consignee. A pure drayage move skips the rail entirely and runs the whole route by truck.</div></details>
      <details class="faq-item"><summary>Who pays for drayage?</summary><div class="faq-answer">The party arranging the inland move pays the drayage invoice — usually the importer or exporter (BCO), or a 3PL, freight forwarder, or customs broker acting on their behalf. The drayage charge is separate from the ocean freight bill of lading. Accessorials (chassis, fuel surcharge, demurrage, detention, chassis split, overweight, hazmat) bill on the same drayage invoice.</div></details>
      <details class="faq-item"><summary>How is drayage priced?</summary><div class="faq-answer">Most Charleston drayage carriers quote a per-container linehaul rate based on the ZIP code of the pickup and delivery, plus a fuel surcharge percentage. Accessorials are quoted separately and only apply when triggered: chassis day rate, chassis split fee, pre-pull and storage, overweight permits, hazmat handling, driver detention, and demurrage pass-through.</div></details>
      <details class="faq-item"><summary>Is drayage the same as cartage?</summary><div class="faq-answer">The two terms overlap and are often used interchangeably, but they're not identical. "Cartage" is the older, broader term for any short-haul move of goods within a city or metro area. "Drayage" specifically refers to the short-haul move of an ocean container to or from a marine terminal or rail ramp. Every drayage move is a cartage move; not every cartage move is drayage.</div></details>
    </div>
  </div>
</section>
"""

    faq_items = [
        ("What is the difference between drayage and trucking?", "Drayage is a specific kind of trucking: the short-haul move of a loaded or empty ocean shipping container to or from a port, rail ramp, or container yard. It requires a chassis, a TWIC-carded driver, and familiarity with terminal appointment systems. Over-the-road trucking is the broader category and usually involves a dry van or flatbed moving palletized freight between warehouses."),
        ("What is the difference between drayage and intermodal?", "Intermodal is when an ocean container moves on rail between two inland points. Drayage is the truck leg at either end of that rail move — the dray from the port to the rail ramp, and the dray from the destination ramp to the consignee. A pure drayage move skips the rail entirely and runs the whole route by truck."),
        ("Who pays for drayage?", "The party arranging the inland move pays the drayage invoice — usually the importer or exporter (BCO), or a 3PL, freight forwarder, or customs broker acting on their behalf. The drayage charge is separate from the ocean freight bill of lading. Accessorials (chassis, fuel surcharge, demurrage, detention, chassis split, overweight, hazmat) bill on the same drayage invoice."),
        ("How is drayage priced?", "Most Charleston drayage carriers quote a per-container linehaul rate based on the ZIP code of the pickup and delivery, plus a fuel surcharge percentage. Accessorials are quoted separately and only apply when triggered: chassis day rate, chassis split fee, pre-pull and storage, overweight permits, hazmat handling, driver detention, and demurrage pass-through."),
        ("Is drayage the same as cartage?", "The two terms overlap and are often used interchangeably, but they're not identical. \"Cartage\" is the older, broader term for any short-haul move of goods within a city or metro area. \"Drayage\" specifically refers to the short-haul move of an ocean container to or from a marine terminal or rail ramp. Every drayage move is a cartage move; not every cartage move is drayage."),
    ]

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": "What is drayage?",
            "description": "The simplest accurate definition of drayage, why the word exists, and where drayage ends and other modes begin.",
            "author": {"@type": "Organization", "name": "Cate Freight"},
            "publisher": {"@id": f"{site_url}/#org"},
            "image": f"{site_url}/og-default.png",
            "datePublished": "2026-04-15",
            "dateModified": ctx["last_modified"],
            "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/what-is-drayage/"},
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faq_items
            ],
        },
    ]

    html = render(
        slug="what-is-drayage",
        path="/resources/what-is-drayage/",
        title="What is Drayage? A Plain-English Explanation | Cate Freight",
        meta_description="Drayage is the short-distance trucking of an ocean shipping container. Here's what that actually means, why the word exists, and how drayage works at the Port of Charleston.",
        h1="What is drayage?",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/what-is-drayage/index.html", html)
