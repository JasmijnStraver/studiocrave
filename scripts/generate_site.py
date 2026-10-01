#!/usr/bin/env python3
"""
Studio Crave — static site generator.

Every page's SEO metadata (title, description, canonical, OG, primary/secondary
keywords) lives in PAGES below so it stays easy to edit without touching markup.
Run: python3 scripts/generate_site.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Global config — update BASE_URL once the real domain is live.
# ---------------------------------------------------------------------------
BASE_URL = "https://www.studiocrave.nl"
ORG_NAME = "Studio Crave"
LOCALITY = "Breda"
REGION = "Noord-Brabant"
COUNTRY = "NL"
DEFAULT_OG_IMAGE = "/images/og-default.svg"

COURSES = [
    {
        "n": "01", "slug": "raw-ingredients", "name": "The Raw Ingredients",
        "short": "Who you are, and what you already bring to the table.",
        "what": "We map your story, your expertise, your audience and the parts of your business that already work — before we change anything.",
        "receive": "A clear picture of your brand's raw material: strengths, story and the gaps that are actually worth closing.",
        "why": "Most rebrands fail here. You can't build a strong brand on ingredients no one has actually looked at.",
    },
    {
        "n": "02", "slug": "flavor-profile", "name": "The Flavor Profile",
        "short": "The personality and tone of voice that make your brand recognizable.",
        "what": "We define how your brand sounds and feels — the words, tone and energy that carry across every touchpoint.",
        "receive": "A tone of voice guide: how you write, how you don't, and the language that is unmistakably yours.",
        "why": "Without a distinct flavor profile, a brand is just correct. Correct doesn't get remembered.",
    },
    {
        "n": "03", "slug": "signature-sauce", "name": "The Signature Sauce",
        "short": "The method, angle or point of view that only you have.",
        "what": "We pull out the thing you do differently and turn it into language and a framework clients can actually recognize.",
        "receive": "Your signature positioning line and the proof points that back it up.",
        "why": "This is what clients come back for, and what they repeat to other people when they recommend you.",
    },
    {
        "n": "04", "slug": "positioning-cut", "name": "The Positioning Cut",
        "short": "Where you cut away from the crowd, on purpose.",
        "what": "We decide what your brand is not — the audience, services and language you deliberately leave behind.",
        "receive": "A sharpened positioning: your niche, your claim, and the boundaries that keep it clear.",
        "why": "A brand that tries to serve everyone gets chosen by no one. Cutting is what makes the rest of the menu make sense.",
    },
    {
        "n": "05", "slug": "plating", "name": "The Plating",
        "short": "The visual identity that presents everything you've decided so far.",
        "what": "Logo, color, typography and art direction — built from the strategy, not before it.",
        "receive": "A complete visual identity system: brand marks, colour palette, typography and usage guidelines.",
        "why": "Plating is presentation, not decoration. It's the first thing people see, and it has to say the right thing instantly.",
    },
    {
        "n": "06", "slug": "pairing", "name": "The Pairing",
        "short": "Making sure your offer, pricing and client journey match the brand.",
        "what": "We check that what you charge, what you sell and how clients experience the process all say the same thing your brand now looks like.",
        "receive": "An aligned offer structure and client journey, so nothing undercuts the brand you just built.",
        "why": "A premium brand with a bargain-bin offer confuses people. Pairing is where brand and business meet.",
    },
    {
        "n": "07", "slug": "experience", "name": "The Experience",
        "short": "How the brand actually feels, from first touch to launch and beyond.",
        "what": "Brand photography, launch content and the small details that make working with you memorable.",
        "receive": "Launch-ready content, brand photography direction, and a plan for introducing the new brand to the world.",
        "why": "People remember how a brand made them feel, not just how it looked. This is where that feeling gets built in.",
    },
]

PORTFOLIO = [
    {
        "slug": "maison-de-vintage", "name": "Maison de Vintage",
        "client": "Noor", "industry": "Curated vintage fashion label",
        "challenge": "Noor's label had loyal customers but a visual identity that looked like every other secondhand shop on Instagram — nothing signalled that the pieces inside were curated, not just sourced.",
        "strategy": "We repositioned Maison de Vintage away from \"vintage shop\" and toward \"curated archive\" — a shift that let Noor charge for curation, not just for clothes.",
        "positioning": "Maison de Vintage is positioned as the label for people who want one exceptional piece, not a pile of options. Scarcity became the selling point, not a side effect.",
        "voice": "The brand voice borrows from hospitality: warm, precise, a little formal — closer to a concierge than a market stall.",
        "visual": "Grand-hotel luxury: mahogany, gold and branded packaging, delivered from a bellboy cart rather than a shipping box.",
        "shoot": "We built a signature brand shoot around the packaging moment itself — the unboxing became as much a part of the brand as the product.",
        "launch": "The rebrand launched alongside a limited restock, timed so the new identity was the first thing returning customers saw.",
        "result": "The relaunch sold out within 48 hours, and customers now keep the packaging as part of the product.",
        "quote": "Klanten bewaren mijn tasjes. Dat zegt genoeg over het merk dat Jasmijn heeft gebouwd.",
    },
    {
        "slug": "old-money-power", "name": "Old Money Power",
        "client": "Lina", "industry": "Business strategist & leadership coach",
        "challenge": "Lina's expertise was high-level, but her brand looked like every other coach's — soft colours, stock photography, nothing that matched the seniority of her clients.",
        "strategy": "We repositioned Lina around quiet confidence: a brand that doesn't perform expertise because it doesn't need to.",
        "positioning": "Old Money Power speaks to leaders who already have influence and want a coach who matches their register, not one who's trying to impress them.",
        "voice": "Understated, direct, unhurried — a voice that never oversells because it doesn't have to.",
        "visual": "A white tailored suit, a vintage convertible and vineyard backdrops: visual cues borrowed from old wealth, not new hustle.",
        "shoot": "The brand shoot was built around stillness — Lina photographed at rest, never mid-pitch.",
        "launch": "The new brand rolled out through a single, quiet announcement rather than a launch campaign — consistent with the positioning itself.",
        "result": "Lina tripled her prices after launch and built a three-month waitlist within six weeks.",
        "quote": "Mijn klanten boeken nu zonder twijfel. Het merk doet het werk.",
    },
    {
        "slug": "editorial-noir", "name": "Editorial Noir",
        "client": "Senna", "industry": "Luxury PR & communications agency",
        "challenge": "Senna's agency did editorial-calibre work for its clients but looked entirely conventional online — nothing hinted at the taste level behind the work.",
        "strategy": "We repositioned Editorial Noir as a point of view, not a service list — the agency clients hire because of how it sees things, not just what it does.",
        "positioning": "Editorial Noir now reads as a small editorial house with strong opinions, which filters for clients who want a perspective, not a vendor.",
        "voice": "Precise, slightly mysterious, editorial rather than promotional — closer to a magazine's voice than an agency's.",
        "visual": "A Parisian-editorial visual world: silk headscarves, red lips and a newspaper as recurring prop.",
        "shoot": "Over sixty editorial-style images were produced in a single shoot, giving Senna a year of on-brand content in one day.",
        "launch": "The repositioning launched with a single editorial-style post that set the tone for everything that followed.",
        "result": "High-end clients now approach Senna directly, without a pitch process.",
        "quote": "Jasmijn zag wie ik was voordat ik het zelf durfde uit te spreken.",
    },
    {
        "slug": "la-dolce-vita", "name": "La Dolce Vita",
        "client": "Eva", "industry": "Luxury travel & lifestyle entrepreneur",
        "challenge": "Eva was running five different offers under one blurry identity — nobody could explain what she actually did in one sentence.",
        "strategy": "We cut the offer back to one clear focus, and built the brand around that single promise instead of five competing ones.",
        "positioning": "La Dolce Vita now stands for one thing: a curated, Amalfi-Coast way of doing business and travel, not a general lifestyle brand.",
        "voice": "Sun-warmed and unhurried, written the way a good long lunch feels.",
        "visual": "Straw hats, white linen and a glass of wine with a view — a visual world built entirely around Mediterranean ease.",
        "shoot": "The shoot doubled as a content bank, giving Eva a full season of imagery from a single location.",
        "launch": "The narrower offer launched with the new brand attached, so the positioning and the product changed together.",
        "result": "The focused offer took 80% less work to deliver and brought in three times as many bookings.",
        "quote": "Mensen zeggen: 'ik wil het leven dat jouw merk uitstraalt.' Dat is precies het punt.",
    },
]

SERVICE_LINKS = [
    ("Brand Strategy", "/brand-strategy/"),
    ("Visual Identity", "/visual-identity/"),
    ("Branding Photography", "/branding-photography/"),
    ("Branding in Breda", "/branding-breda/"),
]

NAV_LINKS = [
    ("The Branding Kitchen", "/the-branding-kitchen/"),
    ("The 7 Courses", "/7-course-branding-experience/"),
    ("Branding", "/branding/"),
    ("Portfolio", "/portfolio/"),
    ("About", "/about/"),
    ("Contact", "/contact/"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def jsonld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


def org_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": BASE_URL + "/#organization",
        "name": ORG_NAME,
        "url": BASE_URL + "/",
        "image": BASE_URL + DEFAULT_OG_IMAGE,
        "description": "Studio Crave is a branding studio in Breda for ambitious female entrepreneurs, working from strategy through visual identity, photography and launch.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": LOCALITY,
            "addressRegion": REGION,
            "addressCountry": COUNTRY,
        },
        "areaServed": "NL",
    }


def website_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": BASE_URL + "/#website",
        "url": BASE_URL + "/",
        "name": ORG_NAME,
        "publisher": {"@id": BASE_URL + "/#organization"},
    }


def breadcrumb_jsonld(trail):
    items = []
    for i, (label, path) in enumerate(trail, start=1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": BASE_URL + path,
        })
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def service_jsonld(name, description, url):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "description": description,
        "provider": {"@id": BASE_URL + "/#organization"},
        "areaServed": "NL",
        "url": BASE_URL + url,
    }


def breadcrumbs_html(trail):
    parts = []
    for i, (label, path) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append(f'<span aria-current="page">{esc(label)}</span>')
        else:
            parts.append(f'<a href="{path}">{esc(label)}</a>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + '<span class="crumb-sep">/</span>'.join(parts) + '</nav>'


def nav_html(current_path):
    items = []
    for label, path in NAV_LINKS:
        cls = ' class="active"' if path == current_path else ""
        items.append(f'<li><a href="{path}"{cls}>{esc(label)}</a></li>')
    return f"""
<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo">Studio <span>Crave</span></a>
    <ul class="nav-links" id="navLinks">
      {''.join(items)}
      <li><a href="/contact/" class="btn-nav">Start your experience</a></li>
    </ul>
    <button class="nav-toggle" aria-label="Menu" onclick="document.getElementById('navLinks').classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
"""


def footer_html():
    service_items = "".join(f'<li><a href="{p}">{esc(l)}</a></li>' for l, p in SERVICE_LINKS)
    nav_items = "".join(f'<li><a href="{p}">{esc(l)}</a></li>' for l, p in NAV_LINKS)
    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div>
        <div class="footer-logo">Studio <span>Crave</span></div>
        <p>The Branding Kitchen — branding for female entrepreneurs who are ready to grow. Based in {LOCALITY}, working with ambitious women wherever they are.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{service_items}</ul>
      </div>
      <div>
        <h4>Studio</h4>
        <ul>{nav_items}</ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Studio Crave, {LOCALITY} &mdash; The Netherlands. All rights reserved.</span>
      <div style="display:flex;gap:20px;"><a href="https://instagram.com/">Instagram</a><a href="/contact/">Contact</a></div>
    </div>
  </div>
</footer>
<button class="scroll-top" id="scrollTop" aria-label="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#8593;</button>
<script>
window.addEventListener('scroll', () => {{
  const btn = document.getElementById('scrollTop');
  if (window.scrollY > 400) {{ btn.classList.add('visible'); }} else {{ btn.classList.remove('visible'); }}
}});
</script>
"""


def page(path, title, description, h1, body, trail, extra_jsonld=None, og_image=None):
    canonical = BASE_URL + path
    og_image_url = BASE_URL + (og_image or DEFAULT_OG_IMAGE)
    ld_objects = [website_jsonld(), org_jsonld(), breadcrumb_jsonld(trail)]
    if extra_jsonld:
        ld_objects.extend(extra_jsonld)
    ld_html = "\n".join(jsonld(o) for o in ld_objects)
    breadcrumb_block = breadcrumbs_html(trail) if len(trail) > 1 else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ORG_NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_image_url}">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/css/tbk.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{ld_html}
</head>
<body>
{nav_html(path)}
{breadcrumb_block}
{body}
{footer_html()}
</body>
</html>
"""
    out_dir = os.path.join(ROOT, path.strip("/"))
    if path == "/":
        out_dir = ROOT
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def course_cards_html(link_prefix="/7-course-branding-experience/#"):
    cards = []
    for c in COURSES:
        cards.append(f"""
      <a href="{link_prefix}{c['slug']}" class="course-item course-link">
        <div class="course-number">{c['n']}</div>
        <div>
          <div class="course-name">{esc(c['name'])}</div>
          <div class="course-desc">{esc(c['short'])}</div>
        </div>
      </a>""")
    return '<div class="course-grid">' + "".join(cards) + '</div>'


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def build_home():
    body = f"""
<section class="hero">
  <div class="hero-bg"></div>
  <div class="hero-content">
    <div class="container">
      <div class="hero-split">
        <div class="hero-inner" style="text-align:left;">
          <span class="hero-eyebrow">Branding Studio &middot; Breda</span>
          <h1>Brands worth <em>craving.</em></h1>
          <p class="hero-sub">Branding for female entrepreneurs who are ready to grow. Studio Crave builds strategic and visual brands for ambitious women taking their business to its next phase.</p>
          <div class="hero-actions" style="justify-content:flex-start;">
            <a href="/contact/" class="btn-primary">Start your branding experience</a>
            <a href="/the-branding-kitchen/" class="btn-outline-light">Explore The Branding Kitchen</a>
          </div>
        </div>
        <div class="hero-image">
          <img src="/images/jasmijn1.svg" alt="Jasmijn, founder of Studio Crave, in her Breda studio" width="900" height="1100" loading="eager">
        </div>
      </div>
    </div>
  </div>
</section>

<div class="marquee">
  <div class="marquee-track">
    <span>&#x1F525; BRAND STRATEGY</span><span>&#x1F525; VISUAL IDENTITY</span><span>&#x1F525; BRANDING PHOTOGRAPHY</span>
    <span>&#x1F525; LAUNCH</span><span>&#x1F525; BASED IN BREDA</span><span>&#x1F525; BRANDS WORTH CRAVING</span>
    <span>&#x1F525; BRAND STRATEGY</span><span>&#x1F525; VISUAL IDENTITY</span><span>&#x1F525; BRANDING PHOTOGRAPHY</span>
    <span>&#x1F525; LAUNCH</span><span>&#x1F525; BASED IN BREDA</span><span>&#x1F525; BRANDS WORTH CRAVING</span>
  </div>
</div>

<section class="section-light">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text">
        <span class="section-label">Who this is for</span>
        <h2 class="section-title section-title-dark">Built for women whose business has outgrown its brand.</h2>
        <p>Studio Crave works with founders, coaches, consultants and creatives &mdash; women running service-based, beauty, wellness and lifestyle businesses who are visually conscious, quality-focused and ready to invest.</p>
        <p>You're not looking for a prettier logo. You're looking for a brand that can carry the next phase of your business, and clients who choose you before they ever ask about price.</p>
        <div class="highlight">Based in Breda. Working with ambitious female entrepreneurs wherever they are.</div>
      </div>
      <div class="intro-image">
        <img src="/images/jasmijn6.svg" alt="Studio Crave signature branding details" width="900" height="900" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <span class="section-label">The Method</span>
    <h2 class="section-title section-title-light">Welcome to <em>The Branding Kitchen.</em></h2>
    <p style="max-width:640px;margin:0 auto 40px;text-align:center;color:rgba(245,240,235,0.75);font-size:17px;">
      A strong brand is built the way a great dish is built: your business already has the ingredients. We develop the recipe, create the flavour, present the dish and launch it into the world.
    </p>
    <div class="pos-table">
      <div class="pos-row"><div class="pos-label">Ingredients</div><div class="pos-value">Understanding the business behind the brand</div></div>
      <div class="pos-row"><div class="pos-label">Recipe</div><div class="pos-value">Strategy and positioning</div></div>
      <div class="pos-row" style="border-bottom:1px solid var(--crave-red);"><div class="pos-label" style="color:var(--crave-red);">Serve &#x2728;</div><div class="pos-value" style="color:var(--creme);font-weight:600;">A launched brand people recognize and crave</div></div>
    </div>
    <p style="text-align:center;margin-top:36px;"><a href="/the-branding-kitchen/" class="btn-outline-light">Explore The Branding Kitchen</a></p>
  </div>
</section>

<section class="section-light" id="courses">
  <div class="container">
    <div style="text-align:center;margin-bottom:56px;">
      <span class="section-label">The Signature Journey</span>
      <h2 class="section-title section-title-dark">The 7 Course Branding Experience</h2>
      <p style="color:rgba(61,20,25,0.6);max-width:600px;margin:0 auto;font-size:16px;">A complete branding process taking your business from strategy to launch, one deliberate course at a time.</p>
    </div>
    {course_cards_html()}
    <p style="text-align:center;margin-top:36px;"><a href="/7-course-branding-experience/" class="btn-primary">See all 7 courses</a></p>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <span class="section-label">What we create</span>
      <h2 class="section-title section-title-light">One brand, built end to end.</h2>
    </div>
    <div class="pillar-grid">
      <div class="pillar-card"><h3><a href="/brand-strategy/" style="color:inherit;text-decoration:none;">Brand Strategy</a></h3><p>Positioning, audience and messaging that give your brand a reason to be chosen.</p></div>
      <div class="pillar-card"><h3><a href="/visual-identity/" style="color:inherit;text-decoration:none;">Visual Identity</a></h3><p>Logo, colour, typography and a system built from the strategy, not before it.</p></div>
      <div class="pillar-card"><h3><a href="/branding-photography/" style="color:inherit;text-decoration:none;">Branding Photography</a></h3><p>Imagery that puts the new brand in front of the camera, on purpose.</p></div>
      <div class="pillar-card"><h3><a href="/7-course-branding-experience/" style="color:inherit;text-decoration:none;">Launch</a></h3><p>A considered introduction of the new brand to the people who need to see it.</p></div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div style="text-align:center;margin-bottom:56px;">
      <span class="section-label">Signature Dishes</span>
      <h2 class="section-title section-title-dark">Selected work.</h2>
    </div>
    <div class="portfolio-teaser-grid">
      {''.join(f'''<a class="portfolio-teaser" href="/portfolio/{p["slug"]}/">
        <img src="/images/shoot{i+1}.svg" alt="{esc(p["name"])} brand photography" width="900" height="1125" loading="lazy">
        <div class="portfolio-teaser-label"><span>{esc(p["name"])}</span><small>{esc(p["industry"])}</small></div>
      </a>''' for i, p in enumerate(PORTFOLIO))}
    </div>
    <p style="text-align:center;margin-top:36px;"><a href="/portfolio/" class="btn-outline-dark">View the work</a></p>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div class="intro-grid" style="align-items:center;">
      <div>
        <span class="section-label">Why Studio Crave</span>
        <h2 class="section-title section-title-light">We turn what makes your business different into a brand people can recognize.</h2>
        <p style="color:rgba(245,240,235,0.7);margin-bottom:16px;">Every project starts with strategy, not mood boards. That's why the brands we build hold up under a price increase, a bigger audience, or a completely new offer.</p>
        <ul class="recognition-list">
          <li>Strategy first, visuals second &mdash; always</li>
          <li>One connected process, not seven separate services</li>
          <li>Built to support your next phase, not just this one</li>
        </ul>
      </div>
      <div class="intro-image">
        <img src="/images/jasmijn3.svg" alt="Jasmijn directing a Studio Crave branding shoot" width="900" height="900" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container" style="text-align:center;">
    <span class="section-label">Location</span>
    <h2 class="section-title section-title-dark">Based in Breda. Working with women everywhere.</h2>
    <p style="max-width:640px;margin:0 auto;color:rgba(61,20,25,0.65);font-size:16px;">Studio Crave is a branding studio in Breda, Noord-Brabant &mdash; and most of the work happens over video calls with clients across the Netherlands. If you're in Breda or Brabant, in-person strategy sessions and shoots are part of the experience.</p>
    <p style="margin-top:28px;"><a href="/branding-breda/" class="btn-outline-dark">Branding in Breda</a></p>
  </div>
</section>

<section class="cta-section" id="contact">
  <div class="cta-content">
    <span class="section-label">Ready?</span>
    <h2>Let's build a brand people <em>crave.</em></h2>
    <p>Start with a conversation about where your business is now, and where the brand needs to take it next.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Start your branding experience</a>
      <a href="/7-course-branding-experience/" class="btn-outline-light">See the 7 courses</a>
    </div>
  </div>
</section>
"""
    page(
        "/",
        "Branding Studio Breda | Studio Crave",
        "Studio Crave is a branding studio in Breda for ambitious female entrepreneurs. From brand strategy and positioning to visual identity, photography and launch.",
        "Brands worth craving.",
        body,
        trail=[("Home", "/")],
        extra_jsonld=[service_jsonld("Branding", "Brand strategy, visual identity, branding photography and brand launch for female entrepreneurs.", "/")],
    )


# ---------------------------------------------------------------------------
# THE BRANDING KITCHEN
# ---------------------------------------------------------------------------
def build_branding_kitchen():
    body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 56px;">
      <span class="section-label">The Method</span>
      <h1 class="section-title section-title-dark">The Branding Kitchen</h1>
      <p style="font-size:18px;color:rgba(61,20,25,0.65);">Your business has the ingredients. We create the recipe.</p>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>The Branding Kitchen is Studio Crave's proprietary approach to branding &mdash; a methodology built on one idea: a strong brand is made the same way a great dish is made.</p>
        <p>Nothing gets invented from scratch. Your story, your expertise, your point of view and your existing audience are the ingredients. Our job is to develop the recipe, create the flavour, present the dish properly and launch it into the world &mdash; in that order, not the other way around.</p>
        <p>Every client goes through the same connected journey: <a href="/7-course-branding-experience/">the 7 Course Branding Experience</a>. Seven courses, one process, no step skipped.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn6.svg" alt="The Branding Kitchen ingredients" width="900" height="900" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <span class="section-label">From ingredients to launch</span>
    <h2 class="section-title section-title-light">One connected process, seven courses.</h2>
    <div class="pos-table">
      <div class="pos-row"><div class="pos-label">Ingredients</div><div class="pos-value">Understanding the business &mdash; Course 01</div></div>
      <div class="pos-row"><div class="pos-label">Flavour</div><div class="pos-value">Personality &amp; tone of voice &mdash; Course 02</div></div>
      <div class="pos-row"><div class="pos-label">Sauce</div><div class="pos-value">Your unique method &mdash; Course 03</div></div>
      <div class="pos-row"><div class="pos-label">Cut</div><div class="pos-value">Positioning &amp; focus &mdash; Course 04</div></div>
      <div class="pos-row"><div class="pos-label">Plating</div><div class="pos-value">Visual identity &amp; presentation &mdash; Course 05</div></div>
      <div class="pos-row"><div class="pos-label">Pairing</div><div class="pos-value">Offer, price &amp; client journey &mdash; Course 06</div></div>
      <div class="pos-row" style="border-bottom:1px solid var(--crave-red);"><div class="pos-label" style="color:var(--crave-red);">Serve &#x2728;</div><div class="pos-value" style="color:var(--creme);font-weight:600;">Launch &mdash; Course 07</div></div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    {course_cards_html()}
    <p style="text-align:center;margin-top:36px;"><a href="/7-course-branding-experience/" class="btn-primary">Start your branding experience</a></p>
  </div>
</section>
"""
    page(
        "/the-branding-kitchen/",
        "The Branding Kitchen | Branding Method | Studio Crave",
        "The Branding Kitchen is Studio Crave's proprietary branding methodology: your business has the ingredients, we create the recipe, flavour, plating and launch.",
        "The Branding Kitchen",
        body,
        trail=[("Home", "/"), ("The Branding Kitchen", "/the-branding-kitchen/")],
    )


# ---------------------------------------------------------------------------
# 7 COURSE BRANDING EXPERIENCE
# ---------------------------------------------------------------------------
def build_seven_courses():
    course_sections = []
    for i, c in enumerate(COURSES):
        bg = "section-light" if i % 2 == 0 else "section-dark"
        title_cls = "section-title-dark" if i % 2 == 0 else "section-title-light"
        course_sections.append(f"""
<section class="{bg}" id="{c['slug']}">
  <div class="container">
    <div class="course-detail">
      <div class="course-detail-number">{c['n']}</div>
      <div>
        <h2 class="{title_cls}" style="font-family:var(--font-heading);font-size:clamp(28px,3.4vw,42px);font-weight:800;margin-bottom:10px;">{esc(c['name'])}</h2>
        <p style="font-family:var(--font-heading);color:var(--crave-red);font-size:18px;font-weight:700;margin-bottom:20px;">{esc(c['short'])}</p>
        <p style="margin-bottom:14px;max-width:640px;"><strong>What happens:</strong> {esc(c['what'])}</p>
        <p style="margin-bottom:14px;max-width:640px;"><strong>What you receive:</strong> {esc(c['receive'])}</p>
        <p style="max-width:640px;"><strong>Why it matters:</strong> {esc(c['why'])}</p>
      </div>
    </div>
  </div>
</section>""")
    body = f"""
<section class="section-light">
  <div class="container" style="text-align:center;max-width:760px;margin:0 auto;">
    <span class="section-label">The Signature Journey</span>
    <h1 class="section-title section-title-dark">The 7 Course Branding Experience</h1>
    <p style="font-size:17px;color:rgba(61,20,25,0.65);">A complete branding experience taking your business from strategy to launch &mdash; part of <a href="/the-branding-kitchen/">The Branding Kitchen</a>.</p>
  </div>
</section>
{''.join(course_sections)}
<section class="cta-section">
  <div class="cta-content">
    <h2>Ready for <em>your</em> seven courses?</h2>
    <p>Every client goes through the same process, in the same order. No course skipped, nothing built on guesswork.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Start your branding experience</a>
      <a href="/portfolio/" class="btn-outline-light">See it in the work</a>
    </div>
  </div>
</section>
"""
    page(
        "/7-course-branding-experience/",
        "7 Course Branding Experience | Studio Crave",
        "The 7 Course Branding Experience is Studio Crave's complete branding process, taking a business from strategy to launch, one deliberate course at a time.",
        "The 7 Course Branding Experience",
        body,
        trail=[("Home", "/"), ("The 7 Course Branding Experience", "/7-course-branding-experience/")],
    )


# ---------------------------------------------------------------------------
# BRANDING (overview / service hub)
# ---------------------------------------------------------------------------
def build_branding():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 48px;">
      <span class="section-label">Branding</span>
      <h1 class="section-title section-title-dark">Branding for women who are ready to grow.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Logo design gives you a mark. Visual identity gives you a system. Branding is neither &mdash; it's the strategy that decides what that mark and that system should say in the first place.</p>
        <p>Studio Crave works from strategy first. Before a single colour is chosen, we know who your brand is for, what it promises, and what makes it different from the ten other options your ideal client is comparing you to.</p>
        <p>The result is <a href="/the-branding-kitchen/">The Branding Kitchen</a> in practice: a complete branding solution delivered through <a href="/7-course-branding-experience/">the 7 Course Branding Experience</a>, from the first strategy conversation to the day the new brand goes live.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Studio Crave branding for female entrepreneurs" width="900" height="1100" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <span class="section-label">Complete branding</span>
      <h2 class="section-title section-title-light">Three pieces, one process.</h2>
    </div>
    <div class="pillar-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="pillar-card"><h3><a href="/brand-strategy/" style="color:inherit;text-decoration:none;">Brand Strategy</a></h3><p>Positioning, audience and messaging &mdash; the decisions everything else is built on.</p></div>
      <div class="pillar-card"><h3><a href="/visual-identity/" style="color:inherit;text-decoration:none;">Visual Identity</a></h3><p>Logo, colour, typography and a system that presents the strategy properly.</p></div>
      <div class="pillar-card"><h3><a href="/branding-photography/" style="color:inherit;text-decoration:none;">Branding Photography</a></h3><p>Imagery that puts the strategy and the identity in front of a camera.</p></div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container" style="text-align:center;">
    <p style="max-width:600px;margin:0 auto 28px;color:rgba(61,20,25,0.65);">Branding for female entrepreneurs works best as one process, not three separate purchases.</p>
    <a href="/the-branding-kitchen/" class="btn-outline-dark">Explore The Branding Kitchen</a>
  </div>
</section>
"""
    page(
        "/branding/",
        "Branding for Female Entrepreneurs | Studio Crave",
        "Complete branding for female entrepreneurs: brand strategy, visual identity and branding photography, built as one process through The Branding Kitchen.",
        "Branding for women who are ready to grow.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/")],
        extra_jsonld=[service_jsonld("Branding", "Complete branding for female entrepreneurs, from strategy through visual identity, photography and launch.", "/branding/")],
    )


# ---------------------------------------------------------------------------
# BRAND STRATEGY
# ---------------------------------------------------------------------------
def build_brand_strategy():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 48px;">
      <span class="section-label">Brand Strategy</span>
      <h1 class="section-title section-title-dark">Build the brand behind the business.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Brand strategy is the thinking that happens before anything gets designed: who you're for, what you're promising, and why someone should choose you over every other option they're considering.</p>
        <p>At Studio Crave, brand strategy &mdash; what some call <em>merkstrategie</em> &mdash; covers positioning, target audience, differentiation, brand personality, values, messaging and tone of voice. It's the work behind Course 01 through Course 04 of <a href="/7-course-branding-experience/">the 7 Course Branding Experience</a>.</p>
        <h2 style="font-family:var(--font-heading);font-size:26px;margin:32px 0 16px;color:var(--bordeaux-dark);font-weight:700;">Questions this answers</h2>
        <ul class="recognition-list">
          <li>Who is this brand actually for, and who is it deliberately not for?</li>
          <li>What makes this business different from the others your client is comparing?</li>
          <li>What does the brand sound like, and what does it never sound like?</li>
          <li>What does the brand stand for when nobody's watching?</li>
        </ul>
        <p style="margin-top:20px;">Once the strategy is set, it becomes the brief for <a href="/visual-identity/">visual identity</a> &mdash; so nothing gets designed on a hunch.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn4.svg" alt="Brand strategy session at Studio Crave" width="900" height="900" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/7-course-branding-experience/" class="btn-outline-dark">See where this fits in the 7 courses</a></p>
  </div>
</section>
"""
    page(
        "/brand-strategy/",
        "Brand Strategy & Positioning | Studio Crave",
        "Brand strategy and positioning for female entrepreneurs: target audience, differentiation, brand personality, values and tone of voice, built before any design starts.",
        "Build the brand behind the business.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Brand Strategy", "/brand-strategy/")],
        extra_jsonld=[service_jsonld("Brand Strategy", "Brand strategy, positioning and messaging for female entrepreneurs.", "/brand-strategy/")],
    )


# ---------------------------------------------------------------------------
# VISUAL IDENTITY
# ---------------------------------------------------------------------------
def build_visual_identity():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 48px;">
      <span class="section-label">Visual Identity</span>
      <h1 class="section-title section-title-dark">Make your brand impossible to mistake.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Visual identity &mdash; logo, colour palette, typography, art direction and the graphic system that ties it together &mdash; is not decoration. It's the strategy, made visible.</p>
        <p>Every visual decision at Studio Crave is derived from the work done in <a href="/brand-strategy/">brand strategy</a> first. A colour palette isn't picked because it's trending; it's picked because it says what the brand needs to say. The same goes for the <em>huisstijl</em>, image direction and social templates that come after it.</p>
        <h2 style="font-family:var(--font-heading);font-size:26px;margin:32px 0 16px;color:var(--bordeaux-dark);font-weight:700;">What's included</h2>
        <ul class="recognition-list">
          <li>Logo and brand marks</li>
          <li>Colour palette and typography</li>
          <li>Art direction and image direction</li>
          <li>Graphic elements and a usable brand guideline</li>
          <li>Social templates built for daily use</li>
        </ul>
        <p style="margin-top:20px;">The identity then carries into <a href="/branding-photography/">branding photography</a>, so the brand looks the same in a photo as it does on a business card.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn5.svg" alt="Studio Crave visual identity design process" width="900" height="900" loading="lazy"></div>
    </div>
  </div>
</section>
"""
    page(
        "/visual-identity/",
        "Visual Identity & Brand Design | Studio Crave",
        "Visual identity and brand design derived from strategy: logo, colour palette, typography, art direction and a usable brand guideline for female entrepreneurs.",
        "Make your brand impossible to mistake.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Visual Identity", "/visual-identity/")],
        extra_jsonld=[service_jsonld("Visual Identity", "Visual identity and brand design derived from brand strategy.", "/visual-identity/")],
    )


# ---------------------------------------------------------------------------
# BRANDING PHOTOGRAPHY
# ---------------------------------------------------------------------------
def build_branding_photography():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 48px;">
      <span class="section-label">Branding Photography</span>
      <h1 class="section-title section-title-dark">Bring your brand to life.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>A brand isn't finished until it exists in a photo. Branding photography &mdash; sometimes called personal branding photography &mdash; is where strategy and visual identity get tested against a real room, real light and a real person.</p>
        <p>Studio Crave plans every shoot around the brand, not the other way around: creative direction, location, styling and a shot list built to match <a href="/visual-identity/">the visual identity</a> already agreed on.</p>
        <h2 style="font-family:var(--font-heading);font-size:26px;margin:32px 0 16px;color:var(--bordeaux-dark);font-weight:700;">A branding shoot with Studio Crave covers</h2>
        <ul class="recognition-list">
          <li>Creative direction, tied to your brand strategy</li>
          <li>Location and styling planning</li>
          <li>A shot list built for how you'll actually use the images</li>
          <li>Brand imagery and content imagery, delivered together</li>
        </ul>
        <p style="margin-top:20px;">Shoots take place in and around Breda, with clients travelling in from across Brabant and beyond &mdash; branding photography Netherlands-wide, on request.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn3.svg" alt="Branding photography shoot in Breda" width="900" height="900" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/portfolio/" class="btn-outline-dark">See branding photography in the portfolio</a></p>
  </div>
</section>
"""
    page(
        "/branding-photography/",
        "Branding Photography & Personal Branding | Studio Crave",
        "Branding photography and personal branding shoots in Breda: creative direction, styling and imagery built to match your brand strategy and visual identity.",
        "Bring your brand to life.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Branding Photography", "/branding-photography/")],
        extra_jsonld=[service_jsonld("Branding Photography", "Branding and personal branding photography for female entrepreneurs, based in Breda.", "/branding-photography/")],
    )


# ---------------------------------------------------------------------------
# BRANDING BREDA
# ---------------------------------------------------------------------------
def build_branding_breda():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 48px;">
      <span class="section-label">Breda</span>
      <h1 class="section-title section-title-dark">Branding studio in Breda for women ready to grow.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Studio Crave is based in Breda, Noord-Brabant, and works with female entrepreneurs, founders and creatives across the region &mdash; and, over video, across the Netherlands.</p>
        <p>Local clients get the full studio experience in person: strategy sessions, visual identity reviews and branding shoots around Breda and the wider Brabant area. Clients further afield get the same 7-course process, run over calls and shared boards, with shoot days scheduled when it makes sense to travel.</p>
        <h2 style="font-family:var(--font-heading);font-size:26px;margin:32px 0 16px;color:var(--bordeaux-dark);font-weight:700;">What working with Studio Crave from Breda looks like</h2>
        <ul class="recognition-list">
          <li>An in-person strategy session at the studio, or a local coffee shop, if you're nearby</li>
          <li>Branding photography shot on location in Breda or Brabant</li>
          <li>The full <a href="/7-course-branding-experience/">7 Course Branding Experience</a>, from ingredients to launch</li>
          <li>A brand built to grow with a business, not just to look good on day one</li>
        </ul>
        <p style="margin-top:20px;">Why strategic branding matters here is the same reason it matters anywhere: a growing business in a compact, competitive city like Breda needs a brand that's instantly clear, not one that needs explaining twice.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn1.svg" alt="Studio Crave, branding studio in Breda" width="900" height="1100" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/contact/" class="btn-primary">Work with Studio Crave</a></p>
  </div>
</section>
"""
    page(
        "/branding-breda/",
        "Branding Breda | Branding Studio & Brand Strategy | Studio Crave",
        "Studio Crave is a branding studio in Breda for female entrepreneurs ready to grow. Brand strategy, positioning, visual identity, photography and launch.",
        "Branding studio in Breda for women ready to grow.",
        body,
        trail=[("Home", "/"), ("Branding in Breda", "/branding-breda/")],
        extra_jsonld=[org_jsonld()],
    )


# ---------------------------------------------------------------------------
# PORTFOLIO INDEX + CASE STUDIES
# ---------------------------------------------------------------------------
def build_portfolio_index():
    cards = []
    for i, p in enumerate(PORTFOLIO):
        cards.append(f"""
      <a class="portfolio-teaser" href="/portfolio/{p['slug']}/">
        <img src="/images/shoot{i+1}.svg" alt="{esc(p['name'])} brand photography, {esc(p['industry'])}" width="900" height="1125" loading="lazy">
        <div class="portfolio-teaser-label"><span>{esc(p['name'])}</span><small>{esc(p['client'])} &mdash; {esc(p['industry'])}</small></div>
      </a>""")
    body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:700px;margin:0 auto 48px;">
      <span class="section-label">Signature Dishes</span>
      <h1 class="section-title section-title-dark">Selected work.</h1>
      <p style="color:rgba(61,20,25,0.6);">Every project below went through the full <a href="/7-course-branding-experience/">7 Course Branding Experience</a> &mdash; strategy, positioning, voice, visual identity, photography and launch.</p>
    </div>
    <div class="portfolio-teaser-grid">{''.join(cards)}</div>
  </div>
</section>
"""
    page(
        "/portfolio/",
        "Portfolio | Branding Case Studies | Studio Crave",
        "Branding case studies from Studio Crave: strategy, positioning, visual identity and photography for female entrepreneurs, from first concept to launch.",
        "Selected work.",
        body,
        trail=[("Home", "/"), ("Portfolio", "/portfolio/")],
    )


def build_portfolio_cases():
    for i, p in enumerate(PORTFOLIO):
        body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:760px;margin:0 auto 40px;">
      <span class="section-label">{esc(p['client'])} &mdash; {esc(p['industry'])}</span>
      <h1 class="section-title section-title-dark">{esc(p['name'])}</h1>
    </div>
    <div class="polaroid polaroid-main" style="max-width:560px;margin:0 auto 56px;">
      <img src="/images/shoot{i+1}.svg" alt="{esc(p['name'])} branding shoot" width="900" height="1125" loading="eager">
    </div>
    <div class="case-study">
      <div class="case-block"><h2>The Challenge</h2><p>{esc(p['challenge'])}</p></div>
      <div class="case-block"><h2>The Strategy</h2><p>{esc(p['strategy'])}</p></div>
      <div class="case-block"><h2>The Positioning</h2><p>{esc(p['positioning'])}</p></div>
      <div class="case-block"><h2>The Voice</h2><p>{esc(p['voice'])}</p></div>
      <div class="case-block"><h2>The Visual Identity</h2><p>{esc(p['visual'])}</p></div>
      <div class="case-block"><h2>The Shoot</h2><p>{esc(p['shoot'])}</p></div>
      <div class="case-block"><h2>The Launch</h2><p>{esc(p['launch'])}</p></div>
      <div class="case-block"><h2>The Result</h2><p>{esc(p['result'])}</p></div>
    </div>
    <blockquote class="case-quote" style="display:block;max-width:640px;margin:48px auto 0;">&ldquo;{esc(p['quote'])}&rdquo;</blockquote>
    <p style="text-align:center;margin-top:48px;">
      <a href="/portfolio/" class="btn-outline-dark">Back to portfolio</a>
      &nbsp; <a href="/7-course-branding-experience/" class="btn-outline-dark">See the 7 courses</a>
    </p>
  </div>
</section>
"""
        page(
            f"/portfolio/{p['slug']}/",
            f"{p['name']} | Branding Case Study | Studio Crave",
            f"How Studio Crave repositioned {p['name']} ({p['industry']}) through brand strategy, visual identity and photography as part of the 7 Course Branding Experience.",
            p["name"],
            body,
            trail=[("Home", "/"), ("Portfolio", "/portfolio/"), (p["name"], f"/portfolio/{p['slug']}/")],
            og_image=f"/images/shoot{i+1}.svg",
        )


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def build_about():
    body = """
<section class="section-light">
  <div class="container">
    <div class="intro-grid" style="align-items:center;">
      <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Jasmijn, founder of Studio Crave" width="900" height="1100" loading="eager"></div>
      <div class="intro-text">
        <span class="section-label">About</span>
        <h1 class="section-title section-title-dark">Your brand should feel like you &mdash; only clearer.</h1>
        <p>Studio Crave is a branding studio based in Breda, built on one belief: female entrepreneurs don't need louder marketing, they need a brand that's already saying the right thing before they open their mouth.</p>
        <p>That belief became <a href="/the-branding-kitchen/">The Branding Kitchen</a> &mdash; a methodology that treats branding the way a kitchen treats a great dish: ingredients first, recipe second, presentation last. Every client moves through the same <a href="/7-course-branding-experience/">7 Course Branding Experience</a>, because skipping a course is how brands end up looking finished but feeling unfinished.</p>
        <p>Studio Crave works with founders, coaches, consultants and creatives &mdash; women who are visually conscious, quality-focused, and ready to invest in a brand that supports where their business is going next, not just where it is today.</p>
      </div>
    </div>
  </div>
</section>
"""
    page(
        "/about/",
        "About Studio Crave | Branding Studio Breda",
        "Studio Crave is a branding studio in Breda built on The Branding Kitchen methodology and the 7 Course Branding Experience, for female entrepreneurs ready to grow.",
        "Your brand should feel like you — only clearer.",
        body,
        trail=[("Home", "/"), ("About", "/about/")],
    )


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def build_contact():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:700px;margin:0 auto 48px;">
      <span class="section-label">Contact</span>
      <h1 class="section-title section-title-dark">Ready to make your brand craveable?</h1>
      <p style="color:rgba(61,20,25,0.6);">Tell us where your business is now, and where the brand needs to take it next.</p>
    </div>
    <form class="contact-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="contact">
      <p class="visually-hidden"><label>Don't fill this out if you're human: <input name="bot-field"></label></p>
      <div class="form-row">
        <label for="name">Name</label>
        <input id="name" name="name" type="text" required autocomplete="name">
      </div>
      <div class="form-row">
        <label for="business">Business name</label>
        <input id="business" name="business" type="text" required autocomplete="organization">
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="website">Website</label>
          <input id="website" name="website" type="url" placeholder="https://">
        </div>
        <div class="form-row">
          <label for="instagram">Instagram</label>
          <input id="instagram" name="instagram" type="text" placeholder="@yourbusiness">
        </div>
      </div>
      <div class="form-row">
        <label for="what">What do you do?</label>
        <textarea id="what" name="what" rows="3" required></textarea>
      </div>
      <div class="form-row">
        <label for="struggle">What's currently not working about your brand?</label>
        <textarea id="struggle" name="struggle" rows="3" required></textarea>
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="stage">Where are you in your business?</label>
          <select id="stage" name="stage" required>
            <option value="">Choose one</option>
            <option>Just starting out</option>
            <option>Established, ready to grow</option>
            <option>Successful, brand hasn't kept up</option>
          </select>
        </div>
        <div class="form-row">
          <label for="support">What are you looking for?</label>
          <select id="support" name="support" required>
            <option value="">Choose one</option>
            <option>Full 7 Course Branding Experience</option>
            <option>Brand strategy only</option>
            <option>Visual identity only</option>
            <option>Branding photography only</option>
            <option>Not sure yet</option>
          </select>
        </div>
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="investment">Investment range</label>
          <select id="investment" name="investment">
            <option value="">Prefer not to say</option>
            <option>&euro;1,500 &ndash; &euro;3,000</option>
            <option>&euro;3,000 &ndash; &euro;6,000</option>
            <option>&euro;6,000+</option>
          </select>
        </div>
        <div class="form-row">
          <label for="timeline">Timeline</label>
          <select id="timeline" name="timeline">
            <option value="">Choose one</option>
            <option>As soon as possible</option>
            <option>Within 3 months</option>
            <option>Just exploring</option>
          </select>
        </div>
      </div>
      <button type="submit" class="btn-primary" style="border:none;cursor:pointer;">Send your enquiry</button>
    </form>
    <div style="text-align:center;margin-top:48px;color:rgba(61,20,25,0.55);font-size:14px;">
      Studio Crave &middot; Breda, Noord-Brabant, The Netherlands
    </div>
  </div>
</section>
"""
    page(
        "/contact/",
        "Work With Studio Crave | Branding Studio Breda",
        "Start your branding experience with Studio Crave, a branding studio in Breda. Tell us about your business and where your brand needs to go next.",
        "Ready to make your brand craveable?",
        body,
        trail=[("Home", "/"), ("Contact", "/contact/")],
        extra_jsonld=[org_jsonld()],
    )


# ---------------------------------------------------------------------------
# ROBOTS + SITEMAP
# ---------------------------------------------------------------------------
def build_robots_and_sitemap(all_paths):
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")

    urls = "\n".join(
        f"  <url><loc>{BASE_URL}{p}</loc></url>" for p in all_paths
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)


def main():
    build_home()
    build_branding_kitchen()
    build_seven_courses()
    build_branding()
    build_brand_strategy()
    build_visual_identity()
    build_branding_photography()
    build_branding_breda()
    build_portfolio_index()
    build_portfolio_cases()
    build_about()
    build_contact()

    all_paths = [
        "/", "/the-branding-kitchen/", "/7-course-branding-experience/",
        "/branding/", "/brand-strategy/", "/visual-identity/", "/branding-photography/",
        "/branding-breda/", "/portfolio/",
    ] + [f"/portfolio/{p['slug']}/" for p in PORTFOLIO] + ["/about/", "/contact/"]
    build_robots_and_sitemap(all_paths)
    print(f"Generated {len(all_paths)} pages + robots.txt + sitemap.xml")


if __name__ == "__main__":
    main()
