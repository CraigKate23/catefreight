"""Article: The Charleston port drayage guide."""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("Charleston port drayage guide", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Reference &middot; 9 min read</span>
    <h1>The Charleston port drayage guide.</h1>
    <p>A practical reference for anyone shipping import or export through the Port of Charleston — terminals, free time, accessorials, and the chassis pool reality.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Updated April 2026 &middot; Cate Freight Charleston operations team</p>

      <div class="toc">
        <h4>What's in this guide</h4>
        <ol>
          <li>The Port of Charleston in one paragraph</li>
          <li>The four SCPA terminals you might touch</li>
          <li>Free time, demurrage, and detention</li>
          <li>The chassis pool reality</li>
          <li>What "Charleston-specific" actually means for drayage</li>
          <li>The Navy Base Intermodal Facility</li>
          <li>How to set up a clean drayage relationship</li>
        </ol>
      </div>

      <h2 id="port-overview">1. The Port of Charleston in one paragraph</h2>
      <p>Charleston is the second-largest container port on the East Coast and one of the busiest in the United States. It's operated by the South Carolina Ports Authority (SCPA), which runs three container terminals (Wando Welch, North Charleston, Hugh Leatherman) plus a RoRo/breakbulk terminal at Columbus Street. Charleston has the deepest harbor on the East Coast at 52 feet, meaning it can take the largest vessels calling US East Coast service strings directly. Until the Navy Base Intermodal Facility opens, Charleston is also the only major East Coast port without on-dock or near-dock rail — meaning drayage is the only mode that moves a Charleston container.</p>

      <h2 id="terminals">2. The four SCPA terminals you might touch</h2>
      <h3>Wando Welch Terminal (USCHA)</h3>
      <p>Mount Pleasant, on the east side of the Cooper River. SCPA's flagship container terminal — the highest-volume, with the deepest berths and the largest cranes. If you're tracking a major service string into Charleston, it's almost certainly calling Wando.</p>

      <h3>North Charleston Terminal (USNCH)</h3>
      <p>The original North Charleston terminal on the former Navy base property. Direct interstate access via I-526 and I-26. Diverse mix of containerized and breakbulk cargo. Strong for hazmat coordination and certain steamship line operations.</p>

      <h3>Hugh K. Leatherman Terminal (USCHL)</h3>
      <p>SCPA's newest terminal, built specifically for modern container operations. Near North Charleston Terminal but operationally distinct. Modern ship-to-shore lines, modern gate technology. Increasing share of Charleston's container moves as service strings rotate in.</p>

      <h3>Columbus Street Terminal (USCST)</h3>
      <p>RoRo and breakbulk facility on the Charleston peninsula. Not a container terminal in the conventional sense — but if you're moving project cargo, vehicles, or breakbulk, this is the gate.</p>

      <h2 id="free-time">3. Free time, demurrage, and detention</h2>
      <p>Three different fees, three different parties, three different clocks. Confusing them is how customers end up paying $4,000 in surprise charges on a $600 dray.</p>

      <h3>Terminal demurrage (charged by SCPA)</h3>
      <p>What SCPA charges when a loaded container sits on the terminal past its allotted free time. Free time at SCPA is set by the steamship line and typically runs 3-5 days. Demurrage rates escalate the longer the container sits. SCPA also publishes a holiday "no work day" calendar — those days don't accrue free time, but they also don't accrue demurrage on the receiver's side.</p>

      <h3>Detention (charged by the steamship line)</h3>
      <p>What the steamship line charges when their loaded container is held outside their terminal too long after pickup. Once you've picked up the loaded import and you're staging or unloading slowly, this is the clock you're racing.</p>

      <h3>Per diem (charged by the chassis provider)</h3>
      <p>The daily rental fee for the chassis itself. Different from detention. If you've ever seen a "$70/day" line item on an invoice, that's per diem.</p>

      <p>The cleanest drayage operations watch all three clocks at once and route around the most expensive one. Pre-pull is the most common tool — pulling a container off the terminal early to stop demurrage cold, then staging it at the carrier's yard until the dock is ready.</p>

      <h2 id="chassis">4. The chassis pool reality</h2>
      <p>Most ports have multiple chassis pools — typically TRAC Intermodal, DCLI, and Flexi-Van — and they don't always interchange. If your steamship line uses TRAC chassis but the only available chassis at the depot is DCLI, the trucker has to travel to the right depot, pick up a TRAC chassis, then go get the container. That's a "chassis split," and it costs $25-$75 per container in extra time, miles, and fuel.</p>
      <p>The fix isn't avoiding chassis fees entirely — it's awareness. Sharp drayage carriers route to the depot that holds your line's chassis pool. Sloppy ones don't, and your invoice tells the story.</p>

      <h2 id="charleston-specific">5. What "Charleston-specific" actually means for drayage</h2>
      <p>Charleston has its own rhythms that affect every dray:</p>
      <ul>
        <li><strong>No on-dock rail (yet).</strong> Until Navy Base Intermodal opens, every container moves out by truck.</li>
        <li><strong>Hurricane-season schedules.</strong> SCPA closes for hurricanes, sometimes with little warning. Free time freezes; per diem doesn't always.</li>
        <li><strong>Holiday no-work days.</strong> SCPA observes specific holidays as no-work days where free time doesn't accrue. Smart drayage carriers track the calendar.</li>
        <li><strong>Heavy export flows.</strong> Charleston is a major export port for Southeast manufacturing — paper, ceramics, automotive, metals. Many of these are overweight loads requiring tri-axle equipment.</li>
        <li><strong>Bridges and routes.</strong> The Cooper River Bridge, Don Holt Bridge, and access roads have weight restrictions worth knowing if you're running heavy.</li>
      </ul>

      <h2 id="nbif">6. The Navy Base Intermodal Facility (NBIF)</h2>
      <p>SCPA's near-dock rail facility was originally targeted for July 2025 and pushed to early 2026. When it opens, it'll be the first time Charleston has anything resembling on-dock rail, and it will redistribute drayage flows: some moves currently running long drays to inland markets will shift to rail. We expect this to be a structural change for the Charleston market, not a marginal one.</p>
      <p>Until NBIF is live, drayage is doing all the work — and is doing it by itself.</p>

      <h2 id="setup">7. How to set up a clean drayage relationship</h2>
      <p>If you're shipping recurring volume into or out of Charleston, the difference between a clean drayage relationship and a messy one comes down to a few setup choices:</p>
      <ol>
        <li><strong>Pick a carrier sized for your volume.</strong> Don't fight a 700-truck carrier for an account-management priority you won't get. Don't put 50 containers a week with a one-truck operation that can't flex.</li>
        <li><strong>Standardize the booking handoff.</strong> Same fields every time. Container, MBL, terminal, delivery, weight, specialty. Faster quotes, fewer mistakes.</li>
        <li><strong>Agree on accessorials in advance.</strong> Chassis splits, fuel surcharge methodology, overweight permit pass-through, detention thresholds. Get it in writing.</li>
        <li><strong>Define the POD process.</strong> Filename format, your reference number, who gets the email, and how fast.</li>
        <li><strong>Build a backup plan.</strong> Even sharp carriers have weeks where a vessel runs late, a driver calls out, or chassis are tight. Know what your second option is.</li>
      </ol>

      <p>That's the guide. If you have questions specific to a Charleston move, <a href="/quote/">send us the booking</a> and we'll either run it or tell you who should.</p>
    </article>
  </div>
</section>
"""

    schema = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "The Charleston port drayage guide",
        "description": "Practical reference for anyone shipping through the Port of Charleston — terminals, free time, accessorials, chassis pools.",
        "author": {"@type": "Organization", "name": "Cate Freight"},
        "publisher": {"@id": f"{site_url}/#org"},
        "datePublished": "2026-04-22",
        "dateModified": date.today().isoformat(),
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/charleston-port-drayage-guide/"},
    }]

    html = render(
        slug="charleston-port-drayage-guide",
        path="/resources/charleston-port-drayage-guide/",
        title="The Charleston Port Drayage Guide | Cate Freight",
        meta_description="Practical reference for shipping through the Port of Charleston — SCPA terminals, free time and demurrage, chassis pools, and what's Charleston-specific about drayage here.",
        h1="The Charleston port drayage guide.",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/charleston-port-drayage-guide/index.html", html)
