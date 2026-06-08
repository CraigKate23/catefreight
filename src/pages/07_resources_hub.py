"""Resources / blog hub. Individual articles live in src/blog/."""


def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    site_url = ctx["site_url"]

    crumbs = [("Home", "/"), ("Resources", "")]

    hero = """
<section class="page-hero">
  <div class="container">
    <span class="hero-eyebrow">Resources</span>
    <h1>Practical articles for people moving Charleston containers.</h1>
    <p>Short, specific, and useful — written for the receivers, brokers, and shippers who run <a href="/charleston-drayage/">Charleston drayage</a> through the SCPA terminals and don't want a 3,000-word SEO essay to find a single useful sentence.</p>
  </div>
</section>
"""

    articles = [
        ("4 min read", "What is drayage?", "What ocean drayage actually is, why it exists, and where it ends and other modes begin.", "/resources/what-is-drayage/"),
        ("9 min read", "The Charleston port drayage guide", "A practical reference for anyone shipping import or export through the Port of Charleston — terminals, free time, accessorials, and the chassis pool reality.", "/resources/charleston-port-drayage-guide/"),
        ("8 min read", "How to avoid demurrage and detention at the Port of Charleston", "Demurrage, detention, and per diem: what each one is, who charges it, and how to stop the clock fastest.", "/resources/avoid-demurrage-detention/"),
        ("6 min read", "Drayage vs transload vs intermodal: which one do you actually need?", "When to drag the ocean container all the way, when to cross-dock, and when to switch to rail — with real examples.", "/resources/drayage-vs-transload-intermodal/"),
        ("5 min read", "The drayage quote checklist for importers", "The exact information a Charleston drayage carrier needs from you to come back with a usable number on the first try.", "/resources/drayage-quote-checklist/"),
        ("7 min read", "What 3PLs should look for in a Charleston drayage carrier", "Eleven specific operational criteria a 3PL receiver should grade their drayage carriers against.", "/resources/choosing-a-drayage-carrier-3pl/"),
    ]
    cards = "".join(
        f'<div class="article-card"><div class="read-time">{rt}</div><h3>{title}</h3><p>{desc}</p><a class="read" href="{href}">Read the article</a></div>'
        for rt, title, desc, href in articles
    )

    body = breadcrumb_bar(crumbs) + hero + f"""
<section class="section">
  <div class="container">
    <div class="card-grid">{cards}</div>
  </div>
</section>
""" + cta_banner()

    schema = [{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Cate Freight resources — Charleston drayage articles",
        "url": f"{site_url}/resources/",
    }]

    html = render(
        slug="resources",
        path="/resources/",
        title="Charleston Drayage Articles & Guides | Cate Freight Resources",
        meta_description="Practical articles for people moving Charleston containers — drayage basics, demurrage and detention, the SCPA terminal guide, and more.",
        h1="Practical articles for people moving Charleston containers.",
        body_html=body,
        breadcrumbs=crumbs,
        schema=schema,
        nav_active="resources",
    )
    return ("/resources/index.html", html)
