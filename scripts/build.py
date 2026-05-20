#!/usr/bin/env python3
"""
Cate Freight static site builder.

Reads page content from src/pages/*.py, applies the shared layout
defined in src/templates/layout.py, and emits production HTML to the
project root for Vercel to serve.

Run:  python3 scripts/build.py
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PAGES_DIR = SRC / "pages"
BLOG_DIR = SRC / "blog"
TEMPLATES = SRC / "templates"

SITE_URL = "https://catefreight.com"
SITE_NAME = "Cate Freight"
PHONE_DISPLAY = "(843) 998-7820"
PHONE_TEL = "+18439987820"
EMAIL = "greg@catefreight.com"
ADDRESS_CITY = "Charleston"
ADDRESS_REGION = "SC"
ADDRESS_COUNTRY = "US"
USDOT = "USDOT 3688555"
MC = "MC-1285884"
BUILD_DATE = datetime.utcnow().strftime("%Y-%m-%d")
# Google Search Console — URL-prefix verification via HTML tag.
# Paste the content="..." value Google provides in Search Console here.
# Empty string = tag is omitted from the build.
GOOGLE_SITE_VERIFICATION = ""

# Canonical Organization entity for Cate Freight. Emitted on EVERY page by
# render() so that the per-page Service / Article schema `provider` and
# `publisher` references to "{SITE_URL}/#org" resolve to a complete node.
# Without this, those pages carry a dangling @id reference and Google sees an
# incomplete provider/publisher. Defined here once to keep it consistent.
ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "MovingCompany",
    "@id": f"{SITE_URL}/#org",
    "name": SITE_NAME,
    "alternateName": "C8FR8",
    "url": SITE_URL,
    "email": EMAIL,
    "telephone": PHONE_TEL,
    "image": f"{SITE_URL}/og-default.png",
    "logo": f"{SITE_URL}/favicon.svg",
    "description": (
        "Charleston, SC drayage carrier moving import and export containers "
        "from all SCPA terminals — Wando Welch, North Charleston, and Hugh "
        "Leatherman — to warehouses and consignees across the Southeast."
    ),
    "address": {
        "@type": "PostalAddress",
        "addressLocality": ADDRESS_CITY,
        "addressRegion": ADDRESS_REGION,
        "addressCountry": ADDRESS_COUNTRY,
    },
    "areaServed": [
        {"@type": "City", "name": "Charleston"},
        {"@type": "City", "name": "North Charleston"},
        {"@type": "City", "name": "Mount Pleasant"},
        {"@type": "City", "name": "Summerville"},
        {"@type": "City", "name": "Goose Creek"},
        {"@type": "City", "name": "Hanahan"},
        {"@type": "City", "name": "Ladson"},
        {"@type": "City", "name": "Moncks Corner"},
        {"@type": "City", "name": "Columbia"},
        {"@type": "State", "name": "South Carolina"},
        {"@type": "State", "name": "Georgia"},
        {"@type": "State", "name": "North Carolina"},
    ],
    "knowsAbout": [
        "Wando Welch Terminal",
        "North Charleston Terminal",
        "Hugh Leatherman Terminal",
        "Container drayage",
        "Import drayage",
        "Export drayage",
        "Reefer drayage",
        "Overweight container transport",
        "Hazmat drayage",
        "Transloading",
        "South Carolina Ports Authority",
    ],
    "identifier": [
        {"@type": "PropertyValue", "propertyID": "USDOT", "value": "3688555"},
        {"@type": "PropertyValue", "propertyID": "MC", "value": "1285884"},
    ],
    "sameAs": [],
}


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ----------------------------- shared partials ---------------------------- #

LOGO_SVG = (ROOT / "C8FR8_Main_Logo.svg").read_text()


def header(active: str = "") -> str:
    """Site header. `active` is the slug of the active top-level page."""
    nav = [
        ("/charleston-drayage/", "Charleston Drayage", "charleston-drayage"),
        ("/services/", "Services", "services"),
        ("/who-we-serve/", "Who We Serve", "who-we-serve"),
        ("/coverage/", "Coverage", "coverage"),
        ("/process/", "Process", "process"),
        ("/resources/", "Resources", "resources"),
        ("/about/", "About", "about"),
    ]
    items = "".join(
        '<li><a href="{href}"{ac}>{label}</a></li>'.format(
            href=href,
            label=label,
            ac=' aria-current="page"' if active == slug else "",
        )
        for href, label, slug in nav
    )
    return f"""
<header class="site-nav" role="banner">
  <div class="container nav-inner">
    <a href="/" class="nav-logo" aria-label="Cate Freight home">
      <svg viewBox="0 0 575.62 347.66" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
        <use href="#cf-logo"/>
      </svg>
      <span class="nav-wordmark">Cate Freight</span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-controls="primary-nav" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-primary" id="primary-nav" aria-label="Primary">
      <ul>{items}</ul>
      <a href="tel:{PHONE_TEL}" class="nav-call">{PHONE_DISPLAY}</a>
      <a href="/quote/" class="btn btn-primary nav-cta">Request a Quote</a>
    </nav>
  </div>
</header>
"""


def footer() -> str:
    return f"""
<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <svg class="footer-logo" viewBox="0 0 575.62 347.66" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><use href="#cf-logo"/></svg>
        <p class="footer-tag">Charleston container drayage. Confirmed releases. Clean paperwork. Trucks at the gate when they're supposed to be.</p>
        <div class="footer-contact">
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
      <div>
        <h3>Services</h3>
        <ul>
          <li><a href="/services/port-drayage/">Port drayage</a></li>
          <li><a href="/services/import-container-drayage/">Import container drayage</a></li>
          <li><a href="/services/export-container-drayage/">Export container drayage</a></li>
          <li><a href="/services/port-to-warehouse-drayage/">Port-to-warehouse</a></li>
          <li><a href="/services/transload-drayage/">Transload &amp; coordination</a></li>
          <li><a href="/services/overweight-drayage/">Overweight &amp; OOG</a></li>
          <li><a href="/services/reefer-drayage/">Reefer drayage</a></li>
        </ul>
      </div>
      <div>
        <h3>Who we serve</h3>
        <ul>
          <li><a href="/who-we-serve/3pls/">3PLs</a></li>
          <li><a href="/who-we-serve/freight-forwarders/">Freight forwarders</a></li>
          <li><a href="/who-we-serve/customs-brokers/">Customs brokers</a></li>
          <li><a href="/who-we-serve/importers-exporters/">Importers &amp; exporters</a></li>
        </ul>
        <h3 class="mt-32">Resources</h3>
        <ul>
          <li><a href="/resources/">All articles</a></li>
          <li><a href="/resources/charleston-port-drayage-guide/">Charleston port guide</a></li>
          <li><a href="/resources/avoid-demurrage-detention/">Avoid demurrage &amp; detention</a></li>
          <li><a href="/faq/">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="/about/">About</a></li>
          <li><a href="/coverage/">Coverage area</a></li>
          <li><a href="/process/">How we run a container</a></li>
          <li><a href="/contact/">Contact dispatch</a></li>
          <li><a href="/quote/">Request a quote</a></li>
        </ul>
        <p class="footer-meta">
          {('{} &middot; {}<br>'.format(USDOT, MC)) if USDOT and MC else ''}Charleston, South Carolina
        </p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; {datetime.utcnow().year} Cate Freight. All rights reserved.</p>
      <p><a href="/sitemap.xml">Sitemap</a> &middot; <a href="/privacy/">Privacy</a></p>
    </div>
  </div>
</footer>
"""


def logo_defs() -> str:
    """Inline SVG <defs> so all <use> references work site-wide."""
    inner = LOGO_SVG
    # extract just the inner content of the svg tag
    start = inner.find(">", inner.find("<svg")) + 1
    end = inner.rfind("</svg>")
    body = inner[start:end]
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs><symbol id="cf-logo" viewBox="0 0 575.62 347.66">{body}</symbol></defs></svg>'


# ------------------------------ page renderer ----------------------------- #

def render(
    *,
    slug: str,
    path: str,
    title: str,
    meta_description: str,
    h1: str,
    body_html: str,
    breadcrumbs: list[tuple[str, str]] | None = None,
    schema: list[dict] | None = None,
    og_image: str = "/og-default.png",
    nav_active: str = "",
    page_class: str = "",
    no_index: bool = False,
) -> str:
    canonical = f"{SITE_URL}{path}"
    # Emit the canonical Organization entity on every page (fresh list so the
    # BreadcrumbList append below never mutates the caller's schema list).
    schema = [ORG_SCHEMA] + list(schema or [])
    # always include BreadcrumbList if breadcrumbs supplied
    if breadcrumbs:
        bc = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": name,
                    "item": f"{SITE_URL}{href}" if href else canonical,
                }
                for i, (name, href) in enumerate(breadcrumbs)
            ],
        }
        schema.append(bc)
    schema_json = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, separators=(",", ":"))}</script>'
        for s in schema
    )
    robots = "noindex, nofollow" if no_index else "index, follow, max-image-preview:large"
    gsc_tag = (
        f'<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">\n'
        if GOOGLE_SITE_VERIFICATION else ""
    )
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta_description}">
<meta name="robots" content="{robots}">
{gsc_tag}<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en-us" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta name="theme-color" content="#0f2a3f">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_description}">
<meta name="twitter:image" content="{SITE_URL}{og_image}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" as="style">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/styles.css">
{schema_json}
</head>
<body class="{page_class}">
<a href="#main" class="skip-link">Skip to main content</a>
{logo_defs()}
{header(nav_active)}
<main id="main" role="main">
{body_html}
</main>
{footer()}
<script src="/site.js" defer></script>
</body>
</html>
"""


# ------------------------------ page sections ----------------------------- #

def breadcrumb_bar(crumbs: list[tuple[str, str]]) -> str:
    items = " &rsaquo; ".join(
        f'<a href="{href}">{name}</a>' if href else f'<span aria-current="page">{name}</span>'
        for name, href in crumbs
    )
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="container">{items}</div></nav>'


def cta_banner(title: str = "Need a container moved?", sub: str = "Send the booking, terminal, and delivery ZIP. We'll come back with a quote — usually inside the hour during business hours.") -> str:
    return f"""
<section class="cta-banner">
  <div class="container">
    <div class="cta-banner-inner">
      <div>
        <h2>{title}</h2>
        <p>{sub}</p>
      </div>
      <div class="cta-banner-actions">
        <a class="btn btn-primary" href="/quote/">Request a quote</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">Call dispatch</a>
      </div>
    </div>
  </div>
</section>
"""


def faq_block(items: list[tuple[str, str]], add_schema: bool = True) -> tuple[str, dict | None]:
    rows = "\n".join(
        f"<details class=\"faq-item\"><summary>{q}</summary><div class=\"faq-answer\">{a}</div></details>"
        for q, a in items
    )
    schema = None
    if add_schema:
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": _strip_tags(a)},
                }
                for q, a in items
            ],
        }
    html = f"""
<section class="section faq">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Common questions</p>
      <h2>Charleston drayage FAQ</h2>
    </div>
    <div class="faq-list">{rows}</div>
  </div>
</section>
"""
    return html, schema


def _strip_tags(s: str) -> str:
    import re
    return re.sub(r"<[^>]+>", "", s).strip()


# --------------------------------- build ---------------------------------- #

OUTPUTS: list[tuple[str, str]] = []  # (path, html)


def emit(path: str, html: str):
    OUTPUTS.append((path, html))


def write_output():
    # write all rendered outputs (overwriting; we don't try to delete, since
    # some hosted environments restrict unlink in mounted dirs).
    for path, html in OUTPUTS:
        target = ROOT / path.lstrip("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)
    # static assets from public/
    public = ROOT / "public"
    if public.exists():
        for src in public.rglob("*"):
            if src.is_file():
                rel = src.relative_to(public)
                dst = ROOT / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(src.read_bytes())


def gather_pages():
    """Each page module under src/pages must expose a `build()` returning (path, html)."""
    for py in sorted(PAGES_DIR.glob("*.py")):
        mod = load_module(py)
        if hasattr(mod, "build"):
            results = mod.build({
                "render": render,
                "breadcrumb_bar": breadcrumb_bar,
                "cta_banner": cta_banner,
                "faq_block": faq_block,
                "site_url": SITE_URL,
                "phone_display": PHONE_DISPLAY,
                "phone_tel": PHONE_TEL,
                "email": EMAIL,
                "site_name": SITE_NAME,
            })
            if isinstance(results, tuple):
                results = [results]
            for path, html in results:
                emit(path, html)
    for py in sorted(BLOG_DIR.glob("*.py")):
        mod = load_module(py)
        if hasattr(mod, "build"):
            results = mod.build({
                "render": render,
                "breadcrumb_bar": breadcrumb_bar,
                "cta_banner": cta_banner,
                "site_url": SITE_URL,
            })
            if isinstance(results, tuple):
                results = [results]
            for path, html in results:
                emit(path, html)


def write_sitemap():
    paths = [p for p, _ in OUTPUTS if p.endswith("/index.html")]
    urls = []
    for p in paths:
        clean = p[:-len("index.html")]
        if clean == "/":
            urls.append((SITE_URL + "/", "1.0"))
        else:
            depth = clean.count("/") - 1
            priority = max(0.5, 0.9 - depth * 0.1)
            urls.append((SITE_URL + clean, f"{priority:.1f}"))
    body = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, prio in urls:
        body += f"  <url><loc>{u}</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>weekly</changefreq><priority>{prio}</priority></url>\n"
    body += "</urlset>\n"
    emit("/sitemap.xml", body)


def write_robots():
    body = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    emit("/robots.txt", body)


def write_styles():
    css = (TEMPLATES / "styles.css").read_text()
    emit("/styles.css", css)


def write_site_js():
    js = (TEMPLATES / "site.js").read_text()
    emit("/site.js", js)


def write_favicon():
    # use the logo as favicon
    logo = LOGO_SVG
    emit("/favicon.svg", logo)


def main():
    gather_pages()
    write_sitemap()
    write_robots()
    write_styles()
    write_site_js()
    write_favicon()
    write_output()
    print(f"Built {len(OUTPUTS)} files")


if __name__ == "__main__":
    main()
