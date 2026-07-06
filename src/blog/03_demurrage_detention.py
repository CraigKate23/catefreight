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
      <p>If your dock isn't ready and your free time is about to expire, the smartest move is a <a href="/services/import-container-drayage/#pre-pull">pre-pull</a>. The drayage carrier pulls the container off the terminal early, stages it at their yard, and delivers when your warehouse is free. Terminal demurrage stops cold; daily yard storage replaces it at a fraction of the cost (often 1/4 to 1/8 the demurrage rate).</p>

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

      <p>If you want a <a href="/charleston-drayage/">Charleston drayage</a> carrier that thinks about cost control the way you do, <a href="/quote/">send us your next move</a>.</p>
    </article>
  </div>
</section>

<section class="section faq">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">People also ask</p>
      <h2>Demurrage and detention questions</h2>
    </div>
    <div class="faq-list">
      <details class="faq-item"><summary>What is the difference between demurrage and detention?</summary><div class="faq-answer">Demurrage is charged by the terminal (at Charleston, SCPA) when a loaded container sits on terminal grounds past its free time. Detention — often called per diem — is charged by the steamship line when their container is held outside the terminal too long after pickup. A third fee, chassis per diem, is billed separately by the chassis provider. All three can run on the same container at the same time.</div></details>
      <details class="faq-item"><summary>How much free time do I get before demurrage starts at the Port of Charleston?</summary><div class="faq-answer">Free time is set by the steamship line on the bill of lading, not by SCPA — typically 3-5 calendar days from when the container becomes available. SCPA also publishes a holiday "no work day" calendar; those days don't accrue free time. Once free time expires, demurrage starts and the daily rate escalates the longer the container sits.</div></details>
      <details class="faq-item"><summary>What is a pre-pull and when is it worth it?</summary><div class="faq-answer">A pre-pull is when your drayage carrier pulls the container off the terminal before free time expires, stages it at their yard, and delivers when your dock is ready. Yard storage typically runs 1/4 to 1/8 the terminal demurrage rate, so it's worth it almost any time your warehouse can't receive before free time runs out. <a href="/services/import-container-drayage/">Our import container drayage service</a> flags pre-pull candidates before the clock starts.</div></details>
      <details class="faq-item"><summary>Who charges chassis per diem in Charleston?</summary><div class="faq-answer">The chassis provider — TRAC Intermodal, DCLI, or Flexi-Van at Charleston — bills daily rental for the chassis itself, separate from terminal demurrage and steamship-line detention. On a drop &amp; hook delivery, chassis per diem keeps running until the empty is picked up and returned, so it's the clock to watch when you unload on your own schedule.</div></details>
      <details class="faq-item"><summary>Can demurrage charges be disputed?</summary><div class="faq-answer">Sometimes. Disputes hinge on documentation: if the container wasn't actually available (vessel delay, customs hold not caused by you, terminal closure), or free time was miscalculated across a holiday no-work day, a documented timeline supports a waiver request to the line. The stronger play is prevention — a carrier that tracks release status and free-time expiration on every container rarely needs to dispute anything. Terminal-by-terminal details are in our <a href="/resources/charleston-port-drayage-guide/">Charleston port drayage guide</a>.</div></details>
    </div>
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
        "image": f"{site_url}/og-default.png",
        "datePublished": "2026-04-29",
        "dateModified": ctx["last_modified"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/avoid-demurrage-detention/"},
    }]

    faq_items = [
        ("What is the difference between demurrage and detention?", "Demurrage is charged by the terminal (at Charleston, SCPA) when a loaded container sits on terminal grounds past its free time. Detention — often called per diem — is charged by the steamship line when their container is held outside the terminal too long after pickup. A third fee, chassis per diem, is billed separately by the chassis provider. All three can run on the same container at the same time."),
        ("How much free time do I get before demurrage starts at the Port of Charleston?", "Free time is set by the steamship line on the bill of lading, not by SCPA — typically 3-5 calendar days from when the container becomes available. SCPA also publishes a holiday \"no work day\" calendar; those days don't accrue free time. Once free time expires, demurrage starts and the daily rate escalates the longer the container sits."),
        ("What is a pre-pull and when is it worth it?", "A pre-pull is when your drayage carrier pulls the container off the terminal before free time expires, stages it at their yard, and delivers when your dock is ready. Yard storage typically runs 1/4 to 1/8 the terminal demurrage rate, so it's worth it almost any time your warehouse can't receive before free time runs out."),
        ("Who charges chassis per diem in Charleston?", "The chassis provider — TRAC Intermodal, DCLI, or Flexi-Van at Charleston — bills daily rental for the chassis itself, separate from terminal demurrage and steamship-line detention. On a drop & hook delivery, chassis per diem keeps running until the empty is picked up and returned, so it's the clock to watch when you unload on your own schedule."),
        ("Can demurrage charges be disputed?", "Sometimes. Disputes hinge on documentation: if the container wasn't actually available (vessel delay, customs hold not caused by you, terminal closure), or free time was miscalculated across a holiday no-work day, a documented timeline supports a waiver request to the line. The stronger play is prevention — a carrier that tracks release status and free-time expiration on every container rarely needs to dispute anything."),
    ]

    schema.append({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_items
        ],
    })

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
