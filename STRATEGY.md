# Cate Freight — Charleston Drayage Website Strategy

## 1. Positioning

**One-line positioning.** Cate Freight is the Charleston drayage carrier that runs every container the way a freight forwarder, 3PL, or warehouse manager *wishes* their drayman would: confirmed releases, clean paperwork, dispatch you can reach, and trucks at the gate when they're supposed to be.

**Why this works.** The Charleston drayage market is full of family-owned trucking companies whose websites read like brochures from 2012. Larger national carriers (IMC, Averitt, Gulf Winds) win on scale but feel impersonal. There's a clear gap for a local carrier that *thinks like the receiver* — and Cate Freight's warehouse and 3PL background is the credible foundation for that promise. The site should never apologize for being smaller; it should make smaller feel like a feature: every container gets attention, every email gets a reply, every container gets a release-status check before the truck rolls.

**Brand attributes (used to QA every line of copy):**
- Operationally sharp, not folksy
- Numbers and specifics over adjectives
- Honest about what we don't do (we don't pretend to be a 700-truck carrier)
- Confident, not boastful — let the receivers who hate sloppy paperwork feel home

## 2. Primary SEO Wedge

Per Greg's directive and what the search-volume reality looks like, the wedge is **"Charleston drayage."** Buyer-intent keywords stack on top of that:

**Primary cluster (homepage + Charleston Drayage page):**
- charleston drayage
- charleston port drayage
- port of charleston drayage
- charleston container drayage
- drayage charleston sc
- drayage carrier charleston
- container trucking charleston sc

**Secondary clusters (each gets its own service page):**
- *Import:* import container drayage charleston, import drayage carrier sc, port to warehouse charleston
- *Export:* export container drayage charleston, export loaded delivery scpa
- *Specialty:* overweight container drayage charleston, reefer drayage charleston, hazmat drayage charleston
- *Audience:* drayage for 3pls, drayage for freight forwarders, drayage for customs brokers
- *Geographic expansion:* southeast drayage, savannah charleston drayage corridor, columbia sc container delivery

**Long-tail content cluster (resource articles):**
- what is drayage / what is port drayage
- charleston port terminals guide
- how to avoid demurrage and detention
- pre-pull container charleston
- chassis split fees explained
- drayage vs transload vs intermodal
- what info do I need for a drayage quote
- import container release timeline charleston

## 3. Site Architecture

```
/                              Homepage — Charleston drayage primary wedge
/charleston-drayage/           City-pillar page targeting "charleston drayage"
/services/                     Service hub
  /port-drayage/               Port drayage pillar
  /import-container-drayage/   Import-specific
  /export-container-drayage/   Export-specific
  /port-to-warehouse-drayage/  Port-to-warehouse
  /transload-drayage/          Transload + warehouse coordination
  /overweight-drayage/         Overweight & OOG
  /reefer-drayage/             Reefer + genset
/who-we-serve/                 Audience hub
  /drayage-for-3pls/
  /drayage-for-freight-forwarders/
  /drayage-for-customs-brokers/
  /drayage-for-importers-exporters/
/coverage/                     Service area + terminals page
/process/                      How we run a container (operational story)
/about/                        Company / story
/quote/                        Full quote form (the conversion machine)
/contact/                      Contact + dispatch
/faq/                          Long-form FAQ (FAQ schema)
/resources/                    Article hub
  /resources/what-is-drayage/
  /resources/charleston-port-drayage-guide/
  /resources/avoid-demurrage-detention/
  /resources/drayage-vs-transload-intermodal/
  /resources/drayage-quote-checklist/
  /resources/choosing-a-drayage-carrier-3pl/
/sitemap.xml
/robots.txt
/404.html
```

**Internal linking rules:**
- Every service page links *up* to /charleston-drayage/ and *across* to two related services.
- Every audience page links to the two most relevant services.
- Every resource article links to one matching service page and to /quote/.
- Footer carries the full sitemap so depth is never more than two clicks.

## 4. Conversion Strategy

**Primary CTA, used everywhere:** *Request a Drayage Quote* → `/quote/`
**Secondary CTA, mobile-prominent:** *Call dispatch* → `tel:+18435760000` *(Greg to confirm number; placeholder in code)*
**Tertiary CTA on resource articles:** *Download the drayage quote checklist*

**Quote form fields** (matches the brief, plus operational depth):
1. Name (required)
2. Company (required)
3. Email (required)
4. Phone (required)
5. Move type — Import / Export / Empty return / Other (required)
6. Container size & type — 20/40/40HC + Dry/Reefer/OT/FR/OOG (required)
7. Number of containers
8. Pickup terminal — Wando Welch / North Charleston / Hugh Leatherman / Other / Not sure
9. Pickup ZIP (optional, used for export pre-pulls)
10. Delivery ZIP (required)
11. Delivery type — Live unload / Drop & hook / Transload / Pier return
12. Steamship line / booking #
13. Estimated pickup date
14. Commodity
15. Approximate weight (and overweight Y/N flag)
16. Hazmat? (with UN# field if Y)
17. Reefer set point (if reefer)
18. Notes

The form is split into a 2-step layout so the buyer commits before being asked the longer technical fields. Every field has an `aria-label` and visible label. Submit posts to Formspree (placeholder `YOUR_FORM_ID`); Greg swaps the endpoint at deploy time. After submit, a thank-you page tells the buyer "expect a quote within 60 minutes during business hours."

**Trust signals stacked on every page:**
- Concrete service-area copy ("All three SCPA container terminals — Wando Welch, North Charleston, Hugh Leatherman")
- Equipment specifics (chassis types, weight ceilings)
- Operational language (release status, pre-pull, demurrage clock, paperwork)
- Response-time commitment (quote within the hour during business hours)
- Direct contact (greg@catefreight.com + dispatch phone)
- USDOT / MC numbers in footer (placeholders to fill at deploy time)

## 5. Tone Rules

**Banned phrases:** "your trusted partner," "go the extra mile," "best-in-class," "seamless," "world-class," "industry-leading," "white-glove."
**Preferred verbs:** check, confirm, dispatch, pull, return, unload, monitor, file, route.
**Preferred nouns:** terminal, release, booking, chassis, genset, paperwork, demurrage, free time.
**Sentence length:** mostly short. Mix in one longer sentence when the topic deserves explanation, then snap back.

## 6. Local SEO Plan

**Google Business Profile:**
- Name: *Cate Freight*
- Primary category: *Trucking company*
- Secondary categories: *Logistics service*, *Freight forwarding service*, *Container terminal*
- Service area: Charleston, North Charleston, Mount Pleasant, Summerville, Goose Creek, Hanahan, Ladson, Moncks Corner, Hollywood, Ravenel, Walterboro, Columbia metro
- Description (no keyword stuffing): "Cate Freight is a Charleston-based drayage carrier moving import and export containers from all three SCPA terminals — Wando Welch, North Charleston, and Hugh Leatherman — to warehouses, transload facilities, and customers across South Carolina and the Southeast."
- Photos: trucks at terminal, containers on chassis, equipment shots, dispatch desk
- Review strategy: every customer gets a one-line review request 48 hours after delivery (template included in deploy notes)
- Citations: NAP consistent on Yelp, Yellow Pages, Manta, BBB, FreightWaves directory, drayage.com directory, loadmatch.com, SCPA carrier list, Better Business Bureau, ThomasNet, Industrynet

**Schema deployed:**
- LocalBusiness + TransportationService on homepage and /charleston-drayage/
- Service schema on each service page
- BreadcrumbList on every interior page
- FAQPage on /faq/ and on relevant service pages
- Article schema on every blog post

## 7. Technical SEO Checklist

- Static HTML output, no client-side rendering required for content
- Single critical CSS file inlined per page; one shared external CSS for non-critical
- No render-blocking JS; only a tiny inline mobile-nav handler
- Single Google Font preconnect with `font-display: swap`
- All images served as `width`/`height` set + `loading="lazy"` for non-hero
- Canonical tag every page
- OG + Twitter card meta every page
- robots.txt allowing all, pointing at sitemap
- sitemap.xml generated by build script
- 404 page included
- Vercel `vercel.json` config: clean URLs, force trailing slash off, security headers, long-cache CSS/SVG

## 8. Future Content Plan (90 days)

Weeks 1-2 launch articles (already written):
- What is drayage?
- The Charleston port drayage guide
- How to avoid demurrage and detention at the Port of Charleston
- Drayage vs transload vs intermodal: which one do you actually need?
- The drayage quote checklist for importers
- What 3PLs should look for in a Charleston drayage carrier

Weeks 3-12 cadence — one article per week, alternating clusters:
- Charleston import container release timeline (terminal-by-terminal)
- Pre-pull at Wando Welch: when it pays off and when it doesn't
- Reefer drayage in Charleston: gensets, set points, and pre-trip
- Overweight container drayage in SC: permits, axle config, route limits
- Chassis split fees in Charleston: who charges what and how to avoid them
- Hazmat drayage from Charleston: paperwork, placards, escort rules
- Drayage from Charleston to Atlanta, Greenville, Charlotte, Columbia
- Per diem vs detention: the difference that's costing you
- Customs broker workflows that make drayage smoother
- How a freight forwarder should book a Charleston drayage carrier
- Empty container returns at SCPA terminals
- Out-of-gauge from Columbus Street: what to expect
- The Navy Base Intermodal Facility update for Charleston shippers
- Holiday no-work-day calendar at SCPA and what it means for free time
- A 3PL's drayage SOP template

## 9. Future Improvement Roadmap

After launch, in priority order:
1. Wire Formspree → Slack/email so quotes hit Greg's phone
2. Add a Plausible (or GA4) install + Search Console
3. Build a "/track/?ref=" mini-page where Cate emails customers a tracking link
4. Add real customer logos to homepage (anonymized testimonials acceptable for v1)
5. Add a /pricing/ page with transparent local-dray base, accessorial table
6. Add a /careers/ page (driver app form) — these convert cheap with the local SEO juice
7. Add Spanish-language landing page for /charleston-drayage-camionero/ — half of Charleston dispatch is bilingual; almost no competitor has Spanish content
8. Quarterly content audit; refresh service pages with current SCPA hours, free-time policies, and rate-environment notes.
