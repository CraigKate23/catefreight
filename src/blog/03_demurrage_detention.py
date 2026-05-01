"""Article: How to avoid demurrage and detention at the Port of Charleston."""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("Avoid demurrage & detention", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Cost control &middot; 8 min read</span>
    <h1>How to avoid demurrage and detention at the Port of Charleston.</h1>
    <p>The three clocks every Charleston importer should know, what each one charges, and the specific moves that stop them fastest.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Updated April 2026 &middot; Cate Freight Charleston operations team</p>

      <p>Demurrage and detention are the two line items most likely to surprise an importer's invoice. They're also the two line items where a sharp drayage carrier saves you the most money — sometimes thousands of dollars on a single container. Here's how to think about them and what to do.</p>

      <h2>The three clocks (not two)</h2>
      <p>Most people lump demurrage and detention together. They're actually three separate fees on three separate clocks:</p>
      <ul>
        <li><strong>Terminal demurrage</strong> — charged by SCPA when a loaded container sits on the terminal past its allotted free time.</li>
        <li><strong>Detention (per diem on the container)</strong> — charged by the steamship line when their loaded container is held outside their terminal too long after pickup.</li>
        <li><strong>Chassis per diem</strong> — charged by the chassis provider (TRAC, DCLI, Flexi-Van) for daily rental of the chassis itself.</li>
      </ul>
      <p>You can be paying all three simultaneously on the same move and not realize it. The fix starts with knowing which one is running and how to stop each.</p>

      <h2>Free time at SCPA</h2>
      <p>Free time at SCPA is set by the steamship line, not by SCPA itself. Typical free time runs 3-5 calendar days from the day the container is available. After that, terminal demurrage starts accruing — and it escalates. Day 6 might cost more than day 4. Day 10 a lot more.</p>
      <p>SCPA also publishes a holiday "no work day" calendar — specific holidays where free time does not accrue (and demurrage does not bill). Carriers that track the calendar build their plans around it. Carriers that don't can leave free time on the table.</p>

      <h2>The five moves that stop the clocks fastest</h2>

      <h3>1. Pre-pull when free time is tight</h3>
      <p>If your dock isn't ready and your free time is about to expire, the smartest move is a pre-pull. The drayage carrier pulls the container off the terminal early, stages it at their yard, and delivers when your warehouse is free. Terminal demurrage stops cold; daily yard storage replaces it at a fraction of the cost (often 1/4 to 1/8 the demurrage rate).</p>

      <h3>2. Drop &amp; hook instead of live unload</h3>
      <p>If the warehouse can't unload quickly, drop &amp; hook keeps the driver moving while you unload on your timeline. The driver doesn't sit accruing detention; you only pay chassis per diem until you call for the empty pickup. For 3PLs running steady volume this is almost always cheaper than live unload.</p>

      <h3>3. Schedule the empty return same day</h3>
      <p>The detention clock runs until the empty hits the terminal or a designated depot. If you stop unloading at 4 PM and the empty isn't returned until next morning, that's another full day of detention. Carriers that schedule the empty return same shift save that day automatically.</p>

      <h3>4. Watch holiday no-work days</h3>
      <p>SCPA's holiday no-work days don't accrue free time and don't accrue terminal demurrage on the receiver's side. Plan around them. If your free time would have expired on the Monday after Thanksgiving, the holiday window probably bought you another day or two.</p>

      <h3>5. Get releases in early</h3>
      <p>Most demurrage exposure happens because customs or freight release is late. If your customs broker can file 1C before vessel discharge (with bond and documentation in hand), the container can move the day SCPA releases it. Late entries eat free time on the front end.</p>

      <h2>What a clean drayage carrier does on your behalf</h2>
      <ul>
        <li>Tracks free time expiration on every container in their system</li>
        <li>Recommends pre-pull when free time vs. dock readiness is tight</li>
        <li>Books empty returns same shift as delivery when possible</li>
        <li>Routes to chassis depots that match your steamship line's pool to avoid splits</li>
        <li>Knows the holiday no-work calendar and uses it</li>
        <li>Tells you about exposure before you incur it, not after</li>
      </ul>

      <h2>What it looks like when it goes wrong</h2>
      <p>You receive an invoice. There's a $1,200 line for terminal demurrage. You ask why. Your carrier says they were waiting on customs release. You check with your broker; release was on file three days earlier. The carrier didn't know because nobody on their side checked. The container sat. Three days of demurrage. None of it was necessary.</p>
      <p>This happens more often than it should. The defense is a carrier whose dispatcher checks releases proactively, not reactively.</p>

      <h2>Cate Freight's approach</h2>
      <p>We track release status and free time expiration on every container in our system, recommend pre-pull when the math says to, and book empty returns the same shift as delivery whenever the consignee allows it. Demurrage and detention exposure is part of every quote we give, not something you find out about on the invoice.</p>

      <p>If you want a carrier that thinks about cost control the way you do, <a href="/quote/">send us your next move</a>.</p>
    </article>
  </div>
</section>
"""

    schema = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "How to avoid demurrage and detention at the Port of Charleston",
        "description": "The three clocks every Charleston importer should know — terminal demurrage, container detention, chassis per diem — and the specific moves that stop them fastest.",
        "author": {"@type": "Organization", "name": "Cate Freight"},
        "publisher": {"@id": f"{site_url}/#org"},
        "datePublished": "2026-04-29",
        "dateModified": date.today().isoformat(),
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/avoid-demurrage-detention/"},
    }]

    html = render(
        slug="avoid-demurrage-detention",
        path="/resources/avoid-demurrage-detention/",
        title="How to Avoid Demurrage and Detention at the Port of Charleston | Cate Freight",
        meta_description="Demurrage, detention, and per diem explained. The three clocks running on every Charleston import container, and the specific moves that stop them fastest.",
        h1="How to avoid demurrage and detention at the Port of Charleston.",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/avoid-demurrage-detention/index.html", html)
