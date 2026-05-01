# catefreight.com

Static, multi-page Charleston drayage site for Cate Freight. Built from a small Python pipeline so each page is fully pre-rendered HTML — no client-side framework, no hydration, no slow first paint.

## Stack

- Pure static HTML/CSS/JS, served from disk
- Python 3 build step (no Node, no npm)
- Optional: `cairosvg` to re-render the OG card from SVG to PNG
- Deployed to Vercel as a static site

## Project layout

```
.
├── src/
│   ├── pages/             one .py file per top-level page (homepage, services, etc.)
│   ├── blog/              one .py file per resource article
│   └── templates/
│       ├── styles.css     shared design system
│       └── site.js        tiny mobile-nav script
├── public/                static binary assets (OG image, future photos)
├── scripts/
│   ├── build.py           the renderer: emits all pages + sitemap + robots
│   └── render_og.py       optional: rebuilds public/og-default.png from public/og-default.svg
├── C8FR8_Main_Logo.svg    brand logo (inlined as <symbol> in every page)
├── vercel.json            clean URLs, security headers, cache rules
├── STRATEGY.md            full positioning + SEO + content strategy
└── README.md              this file
```

The HTML files at the project root (`index.html`, `services/index.html`, etc.) are the build artifacts. Vercel serves them directly.

## Build

```bash
python3 scripts/build.py
```

That writes every page, the sitemap, robots.txt, the favicon, and copies `public/*` into the root. Vercel runs the same command via `vercel-build` if you want it on the platform; today the artifacts are committed to git so Vercel can also serve them as-is.

## Re-render the OG card

```bash
pip install --user cairosvg
python3 scripts/render_og.py
```

Edit `public/og-default.svg`, run the script, and `public/og-default.png` is regenerated at 1200×630.

## Local preview

```bash
python3 -m http.server 8000
open http://localhost:8000/
```

## Deploying to Vercel

1. Connect the GitHub repo at `CraigKate23/catefreight` to a new Vercel project.
2. Framework preset: **Other** (or "No framework detected").
3. Root directory: leave as default (project root).
4. Build command: leave **empty** (or `python3 scripts/build.py` if you want Vercel to rebuild on every deploy).
5. Output directory: **`./`** (current dir).
6. Domain: point `catefreight.com` and `www.catefreight.com` at Vercel.

Vercel reads `vercel.json` for clean URLs, trailing slashes, security headers, and asset caching.

## Things to swap before launch

These placeholders live in the build:

- `phone_tel` / `phone_display` in `scripts/build.py` — real dispatch number
- `USDOT` / `MC` in `scripts/build.py` — actual numbers
- `YOUR_FORM_ID` in `src/pages/05_quote.py` — Formspree (or Web3Forms / Basin) endpoint
- The `sameAs` array in the home `MovingCompany` schema — Google Business Profile URL, LinkedIn, etc., once they exist
- The footer business address (currently "Charleston, SC" — add street)

## Adding pages

A new article is one Python file under `src/blog/`:

```python
def build(ctx):
    render = ctx["render"]
    breadcrumb_bar = ctx["breadcrumb_bar"]
    cta_banner = ctx["cta_banner"]
    crumbs = [("Home", "/"), ("Resources", "/resources/"), ("My new article", "")]
    body = breadcrumb_bar(crumbs) + "<section class='page-hero'>...</section>" + cta_banner()
    html = render(
        slug="my-new-article",
        path="/resources/my-new-article/",
        title="...",
        meta_description="...",
        h1="...",
        body_html=body,
        breadcrumbs=crumbs,
        nav_active="resources",
    )
    return ("/resources/my-new-article/index.html", html)
```

The build picks up new files automatically.
