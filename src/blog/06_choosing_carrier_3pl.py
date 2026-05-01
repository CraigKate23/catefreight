"""Article: What 3PLs should look for in a Charleston drayage carrier."""

from datetime import date


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("Choosing a drayage carrier", "")]

    article_html = """
<section class="page-hero compact">
  <div class="container">
    <span class="hero-eyebrow">Buyer's guide &middot; 7 min read</span>
    <h1>What 3PLs should look for in a Charleston drayage carrier.</h1>
    <p>Eleven specific operational criteria a 3PL receiver should grade their drayage carriers against — and the questions to ask in the interview.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <article class="prose">
      <p class="meta">Published April 2026 &middot; Cate Freight Charleston operations team</p>

      <p>If you run a 3PL warehouse that takes inbound containers from Charleston, your drayage carrier is one of your most important upstream suppliers. The good ones make your inbound dock run; the bad ones make your inbound dock the bottleneck. Here's how to tell which is which before they're already scheduled at your dock door.</p>

      <h2>1. Release verification before dispatch</h2>
      <p><strong>The question to ask:</strong> "What do you check before you put a truck on a container?"</p>
      <p>The answer should mention customs release, freight release, and line holds, and should not include the words "we deal with that at the gate." If they don't proactively verify releases, your dock manager will eventually wait three hours for a truck that turned around at the terminal.</p>

      <h2>2. Communication standards</h2>
      <p><strong>The question to ask:</strong> "What's your standard for ETA updates and POD turnaround?"</p>
      <p>Acceptable answer: daily ETA updates while in transit, inbound notification before arrival, signed POD imaged and emailed back the same day, named with our reference. Unacceptable answer: "We'll let you know when something changes."</p>

      <h2>3. Dispatcher continuity</h2>
      <p><strong>The question to ask:</strong> "Who's running my account?"</p>
      <p>You want one named dispatcher per file, ideally per account. Bouncing between people on a shared inbox is how containers get forgotten and your dock supervisor's calls go unanswered.</p>

      <h2>4. Drop-and-hook capability</h2>
      <p><strong>The question to ask:</strong> "Can you drop on chassis at our dock and bobtail away?"</p>
      <p>For 3PLs with steady inbound volume, drop-and-hook beats live unload almost every time. The carrier needs chassis pool relationships, equipment commitment, and the dispatch discipline to schedule the empty pickup against your unload schedule.</p>

      <h2>5. Filename and reference discipline</h2>
      <p><strong>The question to ask:</strong> "How do you name PODs and BOLs?"</p>
      <p>You should be able to specify a filename pattern — typically your reference number, plus the container number, plus the date. If the carrier's PODs come back as "Image_8743.pdf" and force your team to manually rename them, that's a thousand pieces of friction per year.</p>

      <h2>6. SCPA terminal coverage</h2>
      <p><strong>The question to ask:</strong> "Do you pull from all three terminals every shift?"</p>
      <p>If your inbound mix includes Wando Welch, North Charleston, and Hugh Leatherman, your carrier should run all three. Carriers that specialize in one terminal will struggle when your service string moves.</p>

      <h2>7. Equipment match</h2>
      <p><strong>The question to ask:</strong> "What's your tri-axle and reefer chassis availability?"</p>
      <p>If you take overweight containers, you need a carrier with tri-axle chassis ready to go, not one that has to schedule it three days in advance. Same for genset reefer chassis if you take temperature-controlled.</p>

      <h2>8. Accessorial transparency</h2>
      <p><strong>The question to ask:</strong> "Can I see a sample invoice with line items?"</p>
      <p>You want to see linehaul, chassis, fuel surcharge, and accessorials broken out. If the only line on the invoice is "container drayage — $850," you can't audit, you can't compare, and you can't push back on a single charge. Demand transparent invoicing.</p>

      <h2>9. Demurrage and detention awareness</h2>
      <p><strong>The question to ask:</strong> "How do you handle pre-pull and free time?"</p>
      <p>The right answer mentions tracking free time on every container, recommending pre-pull when the math says to, and quoting pre-pull + storage as a single package against demurrage exposure. The wrong answer is silence.</p>

      <h2>10. Capacity and flex</h2>
      <p><strong>The question to ask:</strong> "How do you handle peak weeks?"</p>
      <p>You want a carrier that's honest about their size. A 5-truck carrier saying "we can take 50 containers a day" is lying. A 5-truck carrier saying "we can do 8 a day reliably; for 50 we'd need a partner" is your better bet — they'll perform on the 8 instead of failing on the 50.</p>

      <h2>11. Familiarity with your customer's audit standards</h2>
      <p><strong>The question to ask:</strong> "Have you worked with a 3PL whose customer audits inbound receiving?"</p>
      <p>3PL customers (especially big-box retailers, automotive, and pharma) audit receiving. The drayage carrier's documentation, photos at delivery, and signature discipline have to hold up. Carriers who've passed those audits before will know what you need without being told.</p>

      <h2>How to interview a Charleston drayage carrier</h2>
      <ul>
        <li>Send them a sample request with all the fields and time their response.</li>
        <li>Ask for two recent customer references — preferably 3PL or warehouse customers.</li>
        <li>Ask for a sample BOL and POD from a recent move.</li>
        <li>Ask for their list of accessorials and how each is calculated.</li>
        <li>Ask who answers the phone after 4 PM.</li>
      </ul>

      <h2>Cate Freight's pitch</h2>
      <p>We were built by people who came out of the warehouse and 3PL world, so the eleven criteria above aren't aspirational for us — they're how we run by default. If you're a 3PL operator looking at Charleston drayage carriers, <a href="/quote/">send us a typical move</a> and run the interview. We'll do well or we'll save you time.</p>
    </article>
  </div>
</section>
"""

    schema = [{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "What 3PLs should look for in a Charleston drayage carrier",
        "description": "Eleven operational criteria for evaluating a Charleston drayage carrier — and the specific questions to ask before signing.",
        "author": {"@type": "Organization", "name": "Cate Freight"},
        "publisher": {"@id": f"{site_url}/#org"},
        "datePublished": "2026-04-28",
        "dateModified": date.today().isoformat(),
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{site_url}/resources/choosing-a-drayage-carrier-3pl/"},
    }]

    html = render(
        slug="choosing-a-drayage-carrier-3pl",
        path="/resources/choosing-a-drayage-carrier-3pl/",
        title="What 3PLs Should Look for in a Charleston Drayage Carrier | Cate Freight",
        meta_description="Eleven specific operational criteria for evaluating a Charleston drayage carrier from a 3PL receiver's point of view, plus the questions to ask in the interview.",
        h1="What 3PLs should look for in a Charleston drayage carrier.",
        body_html=breadcrumb_bar(crumbs) + article_html + cta_banner(),
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/choosing-a-drayage-carrier-3pl/index.html", html)
