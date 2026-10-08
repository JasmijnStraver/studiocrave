#!/usr/bin/env python3
"""
Studio Crave / The Branding Kitchen — static site generator.

Every page's SEO metadata (title, description, canonical, OG, keywords) lives
in the page-builder functions below so it stays easy to edit without digging
through markup. Run: python3 scripts/generate_site.py

Copy is based on Jasmijn's own draft (Jasmijn_Branding_Kitchen_Website.html)
and the brand system from the brandingkitchendashboard repo (colors, type).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Global config — update BASE_URL once the real domain is live.
# ---------------------------------------------------------------------------
BASE_URL = "https://www.studiocrave.nl"
SITE_NAME = "The Branding Kitchen"
LOCALITY = "Breda"
REGION = "Noord-Brabant"
COUNTRY = "NL"
DEFAULT_OG_IMAGE = "/images/og-default.svg"

COURSES = [
    {
        "n": "01", "roman": "I", "slug": "raw-ingredients", "name": "Raw Ingredients",
        "short": "Wie ben je echt en wat breng je mee? Je energie, je verhaal, je expertise en je rafelrandjes.",
        "menu_desc": "Wie je echt bent: verhaal, energie, expertise, rafelrandjes",
        "what": "We brengen in kaart wie je bent, wat je al weet, en wat je meeneemt uit alles wat je al hebt opgebouwd — voordat er iets veranderd wordt.",
        "receive": "Een helder beeld van je ruwe ingrediënten: je sterktes, je verhaal, en de gaten die het echt waard zijn om te dichten.",
        "why": "De meeste rebrands gaan hier al mis. Je kunt geen sterk merk bouwen op ingrediënten waar nog niemand goed naar heeft gekeken.",
        "status": "done",
    },
    {
        "n": "02", "roman": "II", "slug": "flavor-profile", "name": "Flavor Profile",
        "short": "De smaak van je merk: tone of voice, energie en vibe. Wat maakt jou herkenbaar na één zin?",
        "menu_desc": "Tone of voice, energie en vibe",
        "what": "We bepalen hoe je merk klinkt en voelt — de woorden, de toon en de energie die overal terugkomen.",
        "receive": "Een tone-of-voice-gids: hoe je wel schrijft, hoe je nooit schrijft, en de taal die onmiskenbaar van jou is.",
        "why": "Zonder uitgesproken smaak ben je gewoon... correct. En correct wordt niet onthouden.",
        "status": "active",
    },
    {
        "n": "03", "roman": "III", "slug": "signature-sauce", "name": "Signature Sauce",
        "short": "Jouw methode, visie en frameworks. Het ding waar mensen voor terugkomen.",
        "menu_desc": "Jouw unieke methode, visie en frameworks",
        "what": "We halen eruit wat jij anders doet dan ieder ander, en zetten dat om in taal en een framework dat klanten herkennen.",
        "receive": "Jouw signature positioneringszin, plus de bewijsstukken die hem onderbouwen.",
        "why": "Dit is waar klanten voor terugkomen, en wat ze doorvertellen als ze je aanbevelen.",
        "status": "open",
    },
    {
        "n": "04", "roman": "IV", "slug": "positioning-cut", "name": "Positioning Cut",
        "short": "Waar snijd je jezelf los van de massa? Je niche, je claims en je grenzen.",
        "menu_desc": "Niche, claims en grenzen + voorbereiding brand shoot",
        "what": "We beslissen wat je merk niet is — welke doelgroep, diensten en taal je bewust achterlaat.",
        "receive": "Een scherpe positionering: je niche, je claim, en de grenzen die hem helder houden.",
        "why": "Een merk dat iedereen wil bedienen, wordt door niemand gekozen. Snijden is wat de rest van het menu logisch maakt.",
        "status": "open",
    },
    {
        "n": "05", "roman": "V", "slug": "plating", "name": "Plating",
        "short": "Hoe je jezelf serveert: je brand shoot, je contentformats, je hooks en je verhalen.",
        "menu_desc": "Content formats, hooks en storytelling + brand shoot",
        "what": "Logo, kleur, typografie en art direction — gebouwd vanuit de strategie, niet ervoor.",
        "receive": "Een complete visuele identiteit: je merktekens, kleurenpalet, typografie en gebruiksrichtlijnen.",
        "why": "Plating is presentatie, geen decoratie. Het is het eerste dat mensen zien, en het moet meteen het juiste zeggen.",
        "status": "open",
    },
    {
        "n": "06", "roman": "VI", "slug": "pairing", "name": "Pairing",
        "short": "Klopt alles samen? Je aanbod, je prijs en je klantreis passen bij het merk dat je neerzet.",
        "menu_desc": "Aanbod, prijs en klantreis",
        "what": "We checken of je prijs, je aanbod en de ervaring van je klant allemaal hetzelfde zeggen als je nieuwe merk.",
        "receive": "Een aanbod en klantreis die kloppen met het merk dat je net hebt neergezet.",
        "why": "Een premium merk met een budget-aanbod verwart mensen. Pairing is waar merk en business elkaar ontmoeten.",
        "status": "open",
    },
    {
        "n": "07", "roman": "VII", "slug": "the-experience", "name": "The Experience",
        "short": "Hoe voelt het om met jou te werken? Beleving, energie en exclusiviteit, van eerste DM tot testimonial.",
        "menu_desc": "Hoe samenwerken met jou voelt",
        "what": "Brand fotografie, launch-content en de kleine details die het werken met jou onvergetelijk maken.",
        "receive": "Launch-klare content, een richting voor je brand fotografie, en een plan om het nieuwe merk de wereld in te brengen.",
        "why": "Mensen onthouden nooit alleen de smaak... ze onthouden hoe jij ze liet voelen.",
        "status": "open",
    },
]

PORTFOLIO = [
    {
        "slug": "maison-de-vintage", "name": "Maison de Vintage",
        "client": "Noor", "industry": "Curated vintage fashion label",
        "challenge": "Noor had trouwe klanten, maar een visuele identiteit die leek op elke andere tweedehands-shop op Instagram — niets liet zien dat de stukken binnen gecureerd waren, niet zomaar ingekocht.",
        "strategy": "We positioneerden Maison de Vintage weg van “vintage shop” en naar “gecureerd archief” — een verschuiving waardoor Noor kon vragen voor curatie, niet alleen voor kleding.",
        "positioning": "Maison de Vintage is er voor mensen die één uitzonderlijk stuk willen, geen stapel opties. Schaarste werd het verkoopargument, niet een bijeffect.",
        "voice": "De merkstem leent van hospitality: warm, precies, een tikje formeel — dichter bij een conciërge dan bij een marktkraam.",
        "visual": "Grand-hotel-luxe: mahonie, goud en branded packaging, geserveerd vanaf een bellboy cart in plaats van een verzenddoos.",
        "shoot": "We bouwden een signature brand shoot rond het uitpak-moment zelf — het openmaken van de verpakking werd net zo'n onderdeel van het merk als het product.",
        "launch": "De rebrand lanceerde samen met een beperkte herbevoorrading, zodat de nieuwe identiteit het eerste was dat terugkerende klanten zagen.",
        "result": "De relaunch was binnen 48 uur uitverkocht, en klanten bewaren de verpakking nu als onderdeel van het product.",
        "quote": "Klanten bewaren mijn tasjes. Dat zegt genoeg over het merk dat Jasmijn heeft gebouwd.",
    },
    {
        "slug": "old-money-power", "name": "Old Money Power",
        "client": "Lina", "industry": "Business strateeg & leadership coach",
        "challenge": "Lina's expertise was hoogwaardig, maar haar merk zag eruit als elk ander coach-merk — zachte kleuren, stockfoto's, niets dat paste bij het niveau van haar klanten.",
        "strategy": "We positioneerden Lina rond quiet confidence: een merk dat geen expertise hoeft te performen, omdat het dat niet nodig heeft.",
        "positioning": "Old Money Power spreekt leiders aan die al invloed hebben en een coach willen die hun register matcht, niet eentje die indruk probeert te maken.",
        "voice": "Ingetogen, direct, ongehaast — een stem die nooit oververkoopt omdat het niet hoeft.",
        "visual": "Een wit maatpak, een vintage cabrio en wijngaarden op de achtergrond: visuele cues geleend van oud geld, niet van nieuwe hustle.",
        "shoot": "De brand shoot draaide om stilte — Lina gefotografeerd in rust, nooit middenin een pitch.",
        "launch": "Het nieuwe merk rolde uit via één rustige aankondiging in plaats van een lanceercampagne — consistent met de positionering zelf.",
        "result": "Lina verdrievoudigde haar prijzen na de lancering en bouwde binnen zes weken een wachtlijst van drie maanden.",
        "quote": "Mijn klanten boeken nu zonder twijfel. Het merk doet het werk.",
    },
    {
        "slug": "editorial-noir", "name": "Editorial Noir",
        "client": "Senna", "industry": "Luxe PR- & communicatiebureau",
        "challenge": "Senna's bureau leverde editorial-niveau werk voor klanten, maar oogde online volledig conventioneel — niets verraadde het smaakniveau achter het werk.",
        "strategy": "We positioneerden Editorial Noir als een point of view, niet als een dienstenlijst — het bureau dat klanten inhuren om hoe het kijkt, niet alleen om wat het doet.",
        "positioning": "Editorial Noir leest nu als een klein editorial huis met een uitgesproken mening, wat precies de klanten filtert die een perspectief willen, geen leverancier.",
        "voice": "Precies, een beetje mysterieus, editorial in plaats van promotioneel — dichter bij de stem van een tijdschrift dan van een bureau.",
        "visual": "Een Parijse editorial-wereld: zijden hoofddoeken, rode lippen en een krant als terugkerend prop.",
        "shoot": "In één shoot werden ruim zestig editorial-beelden geproduceerd, goed voor een jaar aan content.",
        "launch": "De herpositionering lanceerde met één editorial-achtige post die meteen de toon zette voor alles wat volgde.",
        "result": "High-end klanten benaderen Senna nu rechtstreeks, zonder pitch-traject.",
        "quote": "Jasmijn zag wie ik was voordat ik het zelf durfde uit te spreken.",
    },
    {
        "slug": "la-dolce-vita", "name": "La Dolce Vita",
        "client": "Eva", "industry": "Luxury travel & lifestyle ondernemer",
        "challenge": "Eva draaide vijf verschillende aanbiedingen onder één vage identiteit — niemand kon in één zin uitleggen wat ze eigenlijk deed.",
        "strategy": "We sneden het aanbod terug tot één duidelijke focus, en bouwden het merk rond die ene belofte in plaats van vijf concurrerende.",
        "positioning": "La Dolce Vita staat nu voor één ding: een gecureerde, Amalfi-kust-manier van zakendoen en reizen, geen algemeen lifestyle-merk.",
        "voice": "Zonovergoten en ongehaast, geschreven zoals een goede lange lunch aanvoelt.",
        "visual": "Strohoeden, wit linnen en een glas wijn met uitzicht — een visuele wereld volledig gebouwd rond mediterrane gemakzucht.",
        "shoot": "De shoot diende meteen als contentbank, goed voor een heel seizoen aan beeldmateriaal vanuit één locatie.",
        "launch": "Het versmalde aanbod lanceerde samen met het nieuwe merk, zodat positionering en product tegelijk veranderden.",
        "result": "Het gerichte aanbod kostte 80% minder werk om te leveren en bracht drie keer zoveel boekingen op.",
        "quote": "Mensen zeggen: 'ik wil het leven dat jouw merk uitstraalt.' Dat is precies het punt.",
    },
]

MENU_ITEMS = [
    {
        "name": "Brand Audit", "price": "€77", "href": "/contact/", "cta": "Bekijk de Audit",
        "desc": "Een mini-cursus in zeven modules, één per gang, plus een persoonlijke Loom van twintig minuten waarin ik jouw merk doorlicht en een richting voorstel. Maximaal vijftien per week, omdat ik ze zelf maak.",
    },
    {
        "name": "Craveable Identity", "price": "€395", "href": "/contact/", "cta": "Bekijk Craveable Identity",
        "desc": "Jouw visuele identiteit: logo, kleurenpalet, typografie en gebruiksrichtlijnen, gebouwd op wat je al hebt in plaats van vanaf nul.",
    },
    {
        "name": "Branded Templates", "price": "€450", "href": "/contact/", "cta": "Bekijk de templates",
        "desc": "Een complete templateset voor content, voorstellen en documenten in jouw huisstijl. Zelf doorkoken, zonder ooit los van je merk te raken.",
    },
    {
        "name": "Be Your Own Chef", "price": "€25 / maand", "href": "/contact/", "cta": "Meer over Be Your Own Chef",
        "desc": "Doorlopende toegang tot de Branding Dashboard: jouw merk, je documenten en de skills die je elke week helpen zelf door te koken.",
    },
]

BRAND_EXPERIENCE = {
    "name": "7-Course Brand Experience", "price": "€2.500",
    "desc": "Het volledige menu, done-with-you: alle zeven gangen van positionering tot launch, inclusief je eigen shootdag, stem, visuele identiteit en een launchplan.",
    "note": "Het complete traject van The Branding Kitchen™, in deze volgorde.",
}

ADDONS = [
    ("Kick Off Shoot", "€347", "Een korte brand shoot om je nieuwe merk mee te lanceren."),
    ("Full Shoot Day", "€847", "Een volledige shootdag: genoeg beeldmateriaal voor maanden aan content."),
    ("Andere shoots en campagnes", "Op aanvraag", "Van productshoots tot campagnes op maat."),
    ("Losse gang bijboeken", "In overleg", "Eén specifieke gang opnieuw of extra, los van een volledig traject."),
    ("Website op maat", "In overleg", "Een website die klopt met de identiteit die we samen hebben gebouwd."),
    ("Iets anders", "In overleg", "Past je vraag niet in het menu? Vertel me waar je naar zoekt."),
]

FAQ = [
    ("Waar begin ik?", "Met de gratis Signature Dish Quiz. Daarna weet je welk archetype je bent en welke gang de meeste aandacht vraagt. Wil je direct verder, plan dan een kennismaking van 15 minuten."),
    ("Zit de shoot bij de 7-Course Brand Experience inbegrepen?", "Ja. Je krijgt een eigen shootdag. Omdat ik zowel de strategie als de fotografie doe, sluiten je beelden direct aan op je positionering."),
    ("Hoe lang duurt een traject?", "De 7-Course Brand Experience duurt acht weken. De Audit doe je in één middag; je persoonlijke Loom ontvang je binnen 48 uur nadat je je antwoorden hebt ingestuurd."),
    ("Krijg ik ook templates om zelf mee verder te werken?", "Ja. Via Branded Templates en Be Your Own Chef kook je zelf door in jouw huisstijl, zodat je merk na de launch niet verwatert."),
    ("Wat is het verschil tussen Studio Crave en The Branding Kitchen?", "Studio Crave is mijn creative studio voor visuele identiteit, brand visuals en content. The Branding Kitchen™ is de methode: het complete merktraject in zeven gangen."),
]

ARCHETYPES = [
    ("The Classic", "Tijdloos, betrouwbaar, expert-energie. Valkuil: te voorzichtig geprijsd."),
    ("The Signature", "Gedurfd en herkenbaar aan één element. Valkuil: inconsistent over tijd."),
    ("Chef's Special", "De diepe specialist met autoriteit. Valkuil: te bescheiden."),
    ("The Fusion", "Verbindt werelden die niemand samenbracht. Valkuil: verwarrend voor klanten."),
]

SERVICE_LINKS = [
    ("Brand Strategie", "/brand-strategy/"),
    ("Visuele Identiteit", "/visual-identity/"),
    ("Branding Fotografie", "/branding-photography/"),
    ("Branding in Breda", "/branding-breda/"),
]

NAV_LINKS = [
    ("De Keuken", "/the-branding-kitchen/"),
    ("De 7 Gangen", "/7-course-branding-experience/"),
    ("Branding", "/branding/"),
    ("Werk", "/portfolio/"),
    ("Over Jasmijn", "/about/"),
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
        "name": "Studio Crave",
        "alternateName": "The Branding Kitchen",
        "url": BASE_URL + "/",
        "image": BASE_URL + DEFAULT_OG_IMAGE,
        "description": "Studio Crave / The Branding Kitchen is een branding studio in Breda voor ambitieuze vrouwelijke ondernemers, van strategie tot visuele identiteit, fotografie en launch.",
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
        "name": SITE_NAME,
        "inLanguage": "nl-NL",
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
    return '<nav class="breadcrumbs" aria-label="Kruimelpad">' + '<span class="crumb-sep">/</span>'.join(parts) + '</nav>'


def nav_html(current_path):
    items = []
    for label, path in NAV_LINKS:
        cls = ' class="active"' if path == current_path else ""
        items.append(f'<li><a href="{path}"{cls}>{esc(label)}</a></li>')
    return f"""
<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo"><img src="/images/studio-crave-logo-licht.png" alt="Studio Crave"></a>
    <ul class="nav-links" id="navLinks">
      {''.join(items)}
      <li><a href="/contact/" class="btn-nav">Plan een kennismaking</a></li>
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
        <div class="footer-logo"><img src="/images/sc-monogram-wit.png" alt="Studio Crave"></div>
        <p>The Branding Kitchen&trade; &mdash; branding voor vrouwelijke ondernemers die klaar zijn om te groeien, vanuit {LOCALITY}.</p>
        <p style="margin-top:10px;"><a href="mailto:info@studiocrave.nl">info@studiocrave.nl</a></p>
      </div>
      <div>
        <h4>Diensten</h4>
        <ul>{service_items}</ul>
      </div>
      <div>
        <h4>Studio</h4>
        <ul>{nav_items}</ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Studio Crave &mdash; The Branding Kitchen&trade;, {LOCALITY}. Alle rechten voorbehouden.</span>
      <div style="display:flex;gap:20px;"><a href="https://instagram.com/">Instagram</a><a href="/contact/">Contact</a></div>
    </div>
  </div>
</footer>
<button class="scroll-top" id="scrollTop" aria-label="Terug naar boven" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#8593;</button>
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
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{og_image_url}">
<link rel="icon" href="/images/sc-monogram-relief.png" type="image/png">
<link rel="stylesheet" href="/css/tbk.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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


def menu_items_html():
    rows = []
    for item in MENU_ITEMS:
        rows.append(f"""
      <article class="menu-item">
        <div class="menu-item-head">
          <h3>{esc(item['name'])}</h3>
          <span class="menu-leader" aria-hidden="true"></span>
          <span class="menu-price">{esc(item['price'])}</span>
        </div>
        <p>{esc(item['desc'])}</p>
        <a href="{item['href']}">{esc(item['cta'])}</a>
      </article>""")
    rows.append(f"""
      <article class="menu-item menu-item-feature">
        <div class="menu-item-head">
          <h3>{esc(BRAND_EXPERIENCE['name'])}</h3>
          <span class="menu-leader menu-leader-feature" aria-hidden="true"></span>
          <span class="menu-price">{esc(BRAND_EXPERIENCE['price'])}</span>
        </div>
        <p>{esc(BRAND_EXPERIENCE['desc'])}</p>
        <p class="menu-item-note">{esc(BRAND_EXPERIENCE['note'])}</p>
        <a href="/contact/" class="btn-primary" style="margin-top:8px;">Plan een kennismaking van 15 minuten</a>
      </article>""")
    return '<div class="menu-list">' + "".join(rows) + '</div>'


def addons_html():
    rows = []
    for name, price, desc in ADDONS:
        rows.append(f"""
      <div class="addon-item">
        <div class="addon-item-head">
          <h4>{esc(name)}</h4>
          <span class="addon-price">{esc(price)}</span>
        </div>
        <p>{esc(desc)}</p>
      </div>""")
    return '<div class="addon-grid">' + "".join(rows) + '</div>'


STATUS_LABEL = {"done": "Afgerond", "active": "Bezig", "open": "Open"}


def progress_menu_html():
    served = sum(1 for c in COURSES if c["status"] == "done")
    rows = []
    for c in COURSES:
        status = c["status"]
        label = STATUS_LABEL[status]
        mark = "&check;" if status == "done" else c["n"]
        rows.append(f"""
      <div class="progress-item progress-{status}">
        <div class="progress-number">{mark}</div>
        <div class="progress-body">
          <div class="progress-name">{esc(c['name'])}</div>
          <div class="progress-desc">{esc(c['menu_desc'])}</div>
        </div>
        <span class="progress-status progress-status-{status}">{label}</span>
      </div>""")
    return f"""
    <div class="progress-menu">
      <div class="progress-menu-header">
        <div>
          <span class="accent-label">Volgens The Branding Kitchen&trade;</span>
          <h3>7-Course Brand Experience</h3>
        </div>
        <span class="progress-fraction">{served} van 7 gangen geserveerd</span>
      </div>
      <div class="progress-list">{"".join(rows)}</div>
      <p class="progress-footer">Signature Dish: wordt geserveerd na je laatste gang.</p>
    </div>"""


def faq_html():
    items = []
    for q, a in FAQ:
        items.append(f"""
      <details class="faq-item">
        <summary>{esc(q)}<span class="faq-plus" aria-hidden="true">+</span></summary>
        <p>{esc(a)}</p>
      </details>""")
    return '<div class="faq-list">' + "".join(items) + '</div>'


def archetypes_html():
    items = []
    for name, desc in ARCHETYPES:
        items.append(f"""
      <div class="archetype">
        <dt>{esc(name)}</dt>
        <dd>{esc(desc)}</dd>
      </div>""")
    return '<div class="archetype-grid">' + "".join(items) + '</div>'


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
          <span class="hero-eyebrow">Branding als fine dining</span>
          <h1>Een merk is geen plaatje. <em>Het is een menu.</em></h1>
          <p class="hero-sub">Ik bouw merken in zeven gangen: van wie je echt bent tot hoe het voelt om met je te werken. Positionering, stem, beeld en shoot in &eacute;&eacute;n keuken, zodat alles hetzelfde verhaal vertelt.</p>
          <div class="hero-actions" style="justify-content:flex-start;">
            <a href="#quiz" class="btn-primary">Ontdek je Signature Dish</a>
            <a href="#menu" class="btn-outline-light">Bekijk het menu</a>
          </div>
          <p style="margin-top:12px;font-size:14px;color:rgba(245,240,235,0.65);max-width:36em;">Voor coaches, consultants, therapeuten en creatieve ondernemers die al klanten hebben, maar wier merk niet meer laat zien wie ze zijn.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="marquee">
  <div class="marquee-track">
    <span>&#x1F525; BRAND STRATEGIE</span><span>&#x1F525; VISUELE IDENTITEIT</span><span>&#x1F525; BRANDING FOTOGRAFIE</span>
    <span>&#x1F525; LAUNCH</span><span>&#x1F525; GEVESTIGD IN BREDA</span><span>&#x1F525; WE CREATE CRAVINGS</span>
    <span>&#x1F525; BRAND STRATEGIE</span><span>&#x1F525; VISUELE IDENTITEIT</span><span>&#x1F525; BRANDING FOTOGRAFIE</span>
    <span>&#x1F525; LAUNCH</span><span>&#x1F525; GEVESTIGD IN BREDA</span><span>&#x1F525; WE CREATE CRAVINGS</span>
  </div>
</div>

<section class="section-light">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text">
        <span class="section-label">Het probleem</span>
        <h2 class="section-title section-title-dark">Je hebt geen nieuw logo nodig. Je merk mist smaak.</h2>
        <p><strong>Je bent gegroeid. Je merk niet.</strong> Je bio, je beelden en je aanbod komen uit een eerdere versie van je business. Je herkent jezelf er niet meer in, en je droomklant ook niet.</p>
        <p><strong>Mensen snappen het pas als je het uitlegt.</strong> Elke kennismaking begint met jou die vertelt wat je eigenlijk doet. Een sterk merk doet dat werk voordat je in gesprek gaat.</p>
        <p><strong>Je wilt premium vragen, maar je merk ondersteunt het nog niet.</strong> Je werk is het waard. Alleen ziet je merk eruit als iets dat je in een supermarktschap vindt. Dan gaat het gesprek over prijs in plaats van over waarde.</p>
      </div>
      <div class="intro-image">
        <img src="/images/jasmijn6.svg" alt="The Branding Kitchen, signature details" width="900" height="900" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section-dark" id="methode">
  <div class="container">
    <div style="text-align:center;max-width:620px;margin:0 auto 48px;">
      <span class="section-label">De methode</span>
      <h2 class="section-title section-title-light">The 7-Course Method</h2>
      <p style="color:rgba(247,240,236,0.75);font-size:17px;">Zeven gangen, in deze volgorde. Een chef begint niet bij het dessert.</p>
    </div>
    {course_cards_html()}
    <div class="dessert-card">
      <span class="accent-label">Het dessert</span>
      <h3>De Signature Dish</h3>
      <p>Na de zeven gangen volgt het dessert: jouw Signature Dish. De quiz die laat zien welk brand-archetype je bent &mdash; en het startpunt van elk traject hierna.</p>
      <p style="margin-top:18px;"><a href="#quiz" class="btn-primary">Doe de Signature Dish Quiz</a></p>
    </div>
    <p style="text-align:center;margin-top:36px;"><a href="/7-course-branding-experience/" class="btn-outline-light">Bekijk alle 7 gangen</a></p>
  </div>
</section>

<section class="section-light" id="menu-prijzen">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 48px;">
      <span class="section-label">Menu &amp; prijzen</span>
      <h2 class="section-title section-title-dark">&Agrave; la carte, of het hele menu.</h2>
      <p style="color:rgba(31,19,21,0.6);font-size:17px;">Begin met een proeverij of schuif direct aan. Elke gang staat op zichzelf en leidt logisch naar de volgende.</p>
    </div>
    {menu_items_html()}
  </div>
</section>

<section class="section-dark" id="extra-gangen">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <span class="section-label">Extra gangen</span>
      <h2 class="section-title section-title-light">À la carte, los bij te boeken.</h2>
      <p style="color:rgba(245,240,235,0.7);font-size:16px;">Naast je pakket, of los ernaast.</p>
    </div>
    {addons_html()}
  </div>
</section>

<section class="section-light" id="menu">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <span class="section-label">Signature Dishes</span>
      <h2 class="section-title section-title-dark">Vier merken, vier werelden.</h2>
      <p style="color:rgba(31,19,21,0.6);max-width:600px;margin:0 auto;font-size:16px;">Wat er gebeurt als positionering, fotografie en design samenkomen.</p>
    </div>
    <div class="portfolio-teaser-grid">
      {''.join(f'''<a class="portfolio-teaser" href="/portfolio/{p["slug"]}/">
        <img src="/images/shoot{i+1}.svg" alt="{esc(p["name"])} brand fotografie" width="900" height="1125" loading="lazy">
        <div class="portfolio-teaser-label"><span>{esc(p["name"])}</span><small>{esc(p["industry"])}</small></div>
      </a>''' for i, p in enumerate(PORTFOLIO))}
    </div>
    <p style="text-align:center;margin-top:36px;"><a href="/portfolio/" class="btn-outline-dark">Bekijk het werk</a></p>
  </div>
</section>

<section class="section-dark" id="quiz">
  <div class="container">
    <div class="intro-grid" style="align-items:start;">
      <div>
        <span class="section-label">Signature Dish Quiz</span>
        <h2 class="section-title section-title-light">Wat is jouw Signature Dish?</h2>
        <p style="color:rgba(247,240,236,0.8);margin-bottom:22px;">Er bestaat geen fout archetype. Wel een merk dat iets anders uitstraalt dan wie je bent. De quiz laat zien welk archetype jij bent en waar die mismatch zit.</p>
        {archetypes_html()}
      </div>
      <div class="quiz-card">
        <p class="quiz-card-title">Zes vragen. Drie minuten. Gratis.</p>
        <form class="quiz-form" name="quiz" method="POST" data-netlify="true" netlify-honeypot="bot-field">
          <input type="hidden" name="form-name" value="quiz">
          <p class="visually-hidden"><label>Niet invullen: <input name="bot-field"></label></p>
          <div class="form-row">
            <label for="quiz-naam">Voornaam</label>
            <input id="quiz-naam" name="naam" type="text" autocomplete="given-name" placeholder="Je voornaam" required>
          </div>
          <div class="form-row">
            <label for="quiz-mail">E-mailadres</label>
            <input id="quiz-mail" name="email" type="email" autocomplete="email" placeholder="naam@jouwbedrijf.nl" required>
          </div>
          <button type="submit" class="btn-primary" style="width:100%;">Stuur mij de quiz</button>
          <p class="quiz-form-note">Je krijgt de quiz direct in je inbox. Daarna af en toe een gang uit de keuken; afmelden kan altijd.</p>
        </form>
        <p class="quiz-card-alt">Liever via Instagram? Stuur <strong>MENU</strong> in een DM.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div class="intro-grid" style="align-items:center;">
      <div class="intro-image"><img src="/images/jasmijn3.svg" alt="Jasmijn achter de camera tijdens een brand shoot" width="900" height="900" loading="lazy"></div>
      <div class="intro-text">
        <span class="section-label">Over Jasmijn</span>
        <h2 class="section-title section-title-dark">De chef achter de keuken.</h2>
        <p>Ik ben Jasmijn Straver: creative director, merkstrateeg en fotograaf. Bij mij zitten de strategie en de camera in dezelfde keuken, waardoor het beeld altijd klopt met het verhaal.</p>
        <blockquote style="font-family:var(--font-heading);font-size:22px;font-weight:700;color:var(--burgundy);border-left:3px solid var(--pepper);padding-left:20px;margin:20px 0;">Content gaat nooit alleen over wat zichtbaar is. Het gaat over wat voelbaar wordt.</blockquote>
        <a href="/about/" class="btn-outline-dark">Lees het hele verhaal</a>
      </div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <h2 class="section-title section-title-light" style="max-width:16em;margin-bottom:40px;">Niet elke gast hoort aan deze tafel.</h2>
    <div class="intro-grid">
      <div>
        <h3 style="font-family:var(--font-heading);font-size:18px;font-weight:700;color:var(--pepper);margin-bottom:14px;">Wel voor jou als je</h3>
        <ul class="recognition-list">
          <li>al minimaal een jaar onderneemt en klanten hebt</li>
          <li>voelt dat je merk achterloopt op wie je nu bent</li>
          <li>premium wilt vragen en een merk wilt dat dat rechtvaardigt</li>
          <li>strategie &eacute;n beeld in &eacute;&eacute;n hand wilt, zonder vijf partijen te managen</li>
        </ul>
      </div>
      <div>
        <h3 style="font-family:var(--font-heading);font-size:18px;font-weight:700;color:var(--pepper);margin-bottom:14px;">Niet voor jou als je</h3>
        <ul class="recognition-list">
          <li>alleen even snel een logo zoekt</li>
          <li>nog aan het ontdekken bent wat je wilt aanbieden</li>
          <li>het liefst iedereen wilt aanspreken</li>
          <li>geen zin hebt om zelf in beeld te komen</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:880px;">
    <span class="section-label" style="text-align:left;">Vragen van tafel</span>
    <h2 class="section-title section-title-dark" style="text-align:left;margin-bottom:32px;">Veelgestelde vragen</h2>
    {faq_html()}
  </div>
</section>

<section class="cta-section" id="contact">
  <div class="cta-content">
    <h2>Klaar om <em>aan tafel</em> te gaan?</h2>
    <p>Plan een kennismaking van 15 minuten. Geen pitch: we kijken samen of jouw merk klaar is voor het hele menu.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Plan een kennismaking</a>
      <a href="#quiz" class="btn-outline-light">Eerst de quiz</a>
    </div>
    <span class="cta-tagline">Ready to create some cravings?</span>
  </div>
</section>
"""
    page(
        "/",
        "Branding Studio Breda | The Branding Kitchen — Studio Crave",
        "The Branding Kitchen (Studio Crave) is een branding studio in Breda voor vrouwelijke ondernemers. Positionering, merkstrategie, visuele identiteit en branding fotografie in zeven gangen.",
        "Een merk is geen plaatje. Het is een menu.",
        body,
        trail=[("Home", "/")],
        extra_jsonld=[service_jsonld("Branding", "Merkstrategie, visuele identiteit, branding fotografie en brand launch voor vrouwelijke ondernemers.", "/")],
    )


# ---------------------------------------------------------------------------
# THE BRANDING KITCHEN
# ---------------------------------------------------------------------------
def build_branding_kitchen():
    body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 56px;">
      <span class="section-label">De methode</span>
      <h1 class="section-title section-title-dark">The Branding Kitchen</h1>
      <p style="font-size:18px;color:rgba(31,19,21,0.6);">Je merk is geen plaatje. Het is een menu &mdash; en elk merk verdient zijn eigen signature dish.</p>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>The Branding Kitchen is de methode van Studio Crave: een branding-traject in zeven gangen, van wie je echt bent tot hoe het voelt om met je te werken.</p>
        <p>Niets wordt uit het niets verzonnen. Je verhaal, je expertise, je visie en je bestaande publiek zijn de ingredi&euml;nten. Wij ontwikkelen het recept, bepalen de smaak, zorgen voor de juiste plating en lanceren het de wereld in &mdash; in die volgorde, niet andersom.</p>
        <p>Elke klant doorloopt dezelfde route: <a href="/7-course-branding-experience/">de 7-Course Branding Experience</a>. Zeven gangen, &eacute;&eacute;n proces, geen stap overgeslagen.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn6.svg" alt="The Branding Kitchen ingrediënten" width="900" height="900" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <span class="section-label">Van ingredi&euml;nt tot launch</span>
    <h2 class="section-title section-title-light">&Eacute;&eacute;n doorlopend proces, zeven gangen.</h2>
    <div class="pos-table">
      {"".join(f'<div class="pos-row"><div class="pos-label">{c["roman"]}</div><div class="pos-value">{esc(c["name"])} &mdash; {esc(c["short"])}</div></div>' for c in COURSES)}
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    {course_cards_html()}
    <p style="text-align:center;margin-top:36px;"><a href="/7-course-branding-experience/" class="btn-primary">Plan een kennismaking</a></p>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <span class="section-label">Samenwerken</span>
      <h2 class="section-title section-title-light">Zo volg je je voortgang in de Branding Dashboard.</h2>
      <p style="color:rgba(245,240,235,0.7);font-size:16px;">Elke klant ziet dit bovenaan Samenwerken, onder &ldquo;Wat je al hebt&rdquo;. Dit is een voorbeeld.</p>
    </div>
    {progress_menu_html()}
  </div>
</section>
"""
    page(
        "/the-branding-kitchen/",
        "The Branding Kitchen | Branding Methode | Studio Crave",
        "The Branding Kitchen is de eigen methode van Studio Crave: branding in zeven gangen, van ingrediënten en recept tot plating en launch.",
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
        <h2 class="{title_cls}" style="font-size:clamp(28px,3.4vw,42px);font-weight:600;margin-bottom:10px;">{esc(c['name'])}</h2>
        <p style="color:var(--pepper);font-size:18px;font-weight:700;margin-bottom:20px;">{esc(c['short'])}</p>
        <p style="margin-bottom:14px;max-width:640px;"><strong>Wat er gebeurt:</strong> {esc(c['what'])}</p>
        <p style="margin-bottom:14px;max-width:640px;"><strong>Wat je krijgt:</strong> {esc(c['receive'])}</p>
        <p style="max-width:640px;"><strong>Waarom het telt:</strong> {esc(c['why'])}</p>
      </div>
    </div>
  </div>
</section>""")
    body = f"""
<section class="section-light">
  <div class="container" style="text-align:center;max-width:720px;margin:0 auto;">
    <span class="section-label">De signature route</span>
    <h1 class="section-title section-title-dark">The 7-Course Branding Experience</h1>
    <p style="font-size:17px;color:rgba(31,19,21,0.6);">Zeven gangen, in deze volgorde. Een chef begint niet bij het dessert. Onderdeel van <a href="/the-branding-kitchen/">The Branding Kitchen</a>.</p>
  </div>
</section>
{''.join(course_sections)}
<section class="cta-section">
  <div class="cta-content">
    <h2>Klaar voor <em>jouw</em> zeven gangen?</h2>
    <p>Elke klant doorloopt hetzelfde proces, in dezelfde volgorde. Geen gang overgeslagen, niets gebouwd op giswerk.</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Plan een kennismaking</a>
      <a href="/portfolio/" class="btn-outline-light">Bekijk het in het werk</a>
    </div>
  </div>
</section>
"""
    page(
        "/7-course-branding-experience/",
        "7-Course Branding Experience | The Branding Kitchen",
        "De 7-Course Branding Experience is het complete merktraject van Studio Crave: van Raw Ingredients tot The Experience, gang voor gang naar een merk dat klopt.",
        "The 7-Course Branding Experience",
        body,
        trail=[("Home", "/"), ("7-Course Branding Experience", "/7-course-branding-experience/")],
    )


# ---------------------------------------------------------------------------
# BRANDING (overview / service hub)
# ---------------------------------------------------------------------------
def build_branding():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 48px;">
      <span class="section-label">Branding</span>
      <h1 class="section-title section-title-dark">Branding voor vrouwen die klaar zijn om te groeien.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Een logo geeft je een merkteken. Een huisstijl geeft je een systeem. Branding is geen van beide &mdash; het is de strategie die bepaalt wat dat merkteken en dat systeem eigenlijk moeten zeggen.</p>
        <p>Studio Crave werkt vanuit strategie, altijd eerst. Voordat er &eacute;&eacute;n kleur gekozen wordt, weten we voor wie je merk is, wat het belooft, en wat het anders maakt dan de tien andere opties die je droomklant overweegt.</p>
        <p>Het resultaat is <a href="/the-branding-kitchen/">The Branding Kitchen</a> in de praktijk: een complete branding-oplossing via <a href="/7-course-branding-experience/">de 7-Course Branding Experience</a>, van het eerste strategiegesprek tot de dag van de launch.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Branding voor vrouwelijke ondernemers bij Studio Crave" width="900" height="1100" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <span class="section-label">Compleet pakket</span>
      <h2 class="section-title section-title-light">Drie onderdelen, &eacute;&eacute;n proces.</h2>
    </div>
    <div class="pillar-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="pillar-card"><h3><a href="/brand-strategy/" style="color:inherit;text-decoration:none;">Brand Strategie</a></h3><p>Positionering, doelgroep en boodschap &mdash; het fundament waar de rest op gebouwd wordt.</p></div>
      <div class="pillar-card"><h3><a href="/visual-identity/" style="color:inherit;text-decoration:none;">Visuele Identiteit</a></h3><p>Logo, kleur, typografie en een systeem dat de strategie goed presenteert.</p></div>
      <div class="pillar-card"><h3><a href="/branding-photography/" style="color:inherit;text-decoration:none;">Branding Fotografie</a></h3><p>Beeldmateriaal dat de strategie en de identiteit voor de camera brengt.</p></div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container" style="text-align:center;">
    <p style="max-width:600px;margin:0 auto 28px;color:rgba(31,19,21,0.6);">Branding voor vrouwelijke ondernemers werkt het best als &eacute;&eacute;n proces, niet als drie losse aankopen.</p>
    <a href="/the-branding-kitchen/" class="btn-outline-dark">Ontdek The Branding Kitchen</a>
  </div>
</section>
"""
    page(
        "/branding/",
        "Branding voor Vrouwelijke Ondernemers | Studio Crave",
        "Complete branding voor vrouwelijke ondernemers: merkstrategie, visuele identiteit en branding fotografie, gebouwd als één proces via The Branding Kitchen.",
        "Branding voor vrouwen die klaar zijn om te groeien.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/")],
        extra_jsonld=[service_jsonld("Branding", "Complete branding voor vrouwelijke ondernemers, van strategie tot visuele identiteit, fotografie en launch.", "/branding/")],
    )


# ---------------------------------------------------------------------------
# BRAND STRATEGY
# ---------------------------------------------------------------------------
def build_brand_strategy():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 48px;">
      <span class="section-label">Brand Strategie</span>
      <h1 class="section-title section-title-dark">Bouw het merk achter de business.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Merkstrategie is het denkwerk dat gebeurt v&oacute;&oacute;rdat er iets ontworpen wordt: voor wie je bent, wat je belooft, en waarom iemand jou zou kiezen boven elke andere optie.</p>
        <p>Bij Studio Crave omvat merkstrategie positionering, doelgroep, onderscheidend vermogen, merkpersoonlijkheid, waarden, boodschap en tone of voice. Het is het werk achter Gang 01 t/m 04 van <a href="/7-course-branding-experience/">de 7-Course Branding Experience</a>.</p>
        <h2 style="font-size:26px;margin:32px 0 16px;color:var(--midnight);font-weight:700;">Vragen die dit beantwoordt</h2>
        <ul class="recognition-list">
          <li>Voor wie is dit merk eigenlijk, en voor wie bewust niet?</li>
          <li>Wat maakt deze business anders dan de opties waar je klant tussen kiest?</li>
          <li>Hoe klinkt het merk, en hoe klinkt het nooit?</li>
          <li>Waar staat het merk voor als er niemand kijkt?</li>
        </ul>
        <p style="margin-top:20px;">Zodra de strategie staat, wordt die het briefing-document voor de <a href="/visual-identity/">visuele identiteit</a> &mdash; zodat er niets ontworpen wordt op gevoel.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn4.svg" alt="Brand strategiesessie bij Studio Crave" width="900" height="900" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/7-course-branding-experience/" class="btn-outline-dark">Bekijk waar dit past in de 7 gangen</a></p>
  </div>
</section>
"""
    page(
        "/brand-strategy/",
        "Brand Strategie & Positionering | Studio Crave",
        "Merkstrategie en positionering voor vrouwelijke ondernemers: doelgroep, onderscheidend vermogen, merkpersoonlijkheid en tone of voice, vóór er iets ontworpen wordt.",
        "Bouw het merk achter de business.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Brand Strategie", "/brand-strategy/")],
        extra_jsonld=[service_jsonld("Brand Strategie", "Merkstrategie, positionering en boodschap voor vrouwelijke ondernemers.", "/brand-strategy/")],
    )


# ---------------------------------------------------------------------------
# VISUAL IDENTITY
# ---------------------------------------------------------------------------
def build_visual_identity():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 48px;">
      <span class="section-label">Visuele Identiteit</span>
      <h1 class="section-title section-title-dark">Maak je merk onmogelijk te verwarren.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Visuele identiteit &mdash; logo, kleurenpalet, typografie, art direction en het grafische systeem dat alles samenbrengt &mdash; is geen decoratie. Het is de strategie, zichtbaar gemaakt.</p>
        <p>Elke visuele keuze bij Studio Crave komt voort uit het werk dat eerst in <a href="/brand-strategy/">brand strategie</a> is gedaan. Een kleurenpalet wordt niet gekozen omdat het trending is; het wordt gekozen omdat het zegt wat het merk moet zeggen. Hetzelfde geldt voor de huisstijl, beeldtaal en social templates die daarna volgen.</p>
        <h2 style="font-size:26px;margin:32px 0 16px;color:var(--midnight);font-weight:700;">Wat erbij hoort</h2>
        <ul class="recognition-list">
          <li>Logo en merktekens</li>
          <li>Kleurenpalet en typografie</li>
          <li>Art direction en beeldtaal</li>
          <li>Grafische elementen en een bruikbare huisstijlgids</li>
          <li>Social templates die je dagelijks kunt gebruiken</li>
        </ul>
        <p style="margin-top:20px;">De identiteit loopt vervolgens door in <a href="/branding-photography/">branding fotografie</a>, zodat het merk er op een foto hetzelfde uitziet als op een visitekaartje.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn5.svg" alt="Visuele identiteit ontwerpproces bij Studio Crave" width="900" height="900" loading="lazy"></div>
    </div>
  </div>
</section>
"""
    page(
        "/visual-identity/",
        "Visuele Identiteit & Huisstijl | Studio Crave",
        "Visuele identiteit en huisstijl voortkomend uit merkstrategie: logo, kleurenpalet, typografie, art direction en een bruikbare huisstijlgids.",
        "Maak je merk onmogelijk te verwarren.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Visuele Identiteit", "/visual-identity/")],
        extra_jsonld=[service_jsonld("Visuele Identiteit", "Visuele identiteit en huisstijl, voortkomend uit merkstrategie.", "/visual-identity/")],
    )


# ---------------------------------------------------------------------------
# BRANDING PHOTOGRAPHY
# ---------------------------------------------------------------------------
def build_branding_photography():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 48px;">
      <span class="section-label">Branding Fotografie</span>
      <h1 class="section-title section-title-dark">Breng je merk tot leven.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Een merk is niet af voordat het in een foto bestaat. Branding fotografie &mdash; soms personal branding fotografie genoemd &mdash; is waar strategie en visuele identiteit getoetst worden aan een echte ruimte, echt licht en een echt persoon.</p>
        <p>Studio Crave plant elke shoot rond het merk, niet andersom: creative direction, locatie, styling en een shotlist die aansluit op <a href="/visual-identity/">de visuele identiteit</a> die al is vastgesteld.</p>
        <h2 style="font-size:26px;margin:32px 0 16px;color:var(--midnight);font-weight:700;">Een branding shoot met Studio Crave omvat</h2>
        <ul class="recognition-list">
          <li>Creative direction, gekoppeld aan je merkstrategie</li>
          <li>Locatie- en stylingplanning</li>
          <li>Een shotlist die past bij hoe je de beelden echt gaat gebruiken</li>
          <li>Brand- en contentbeelden, samen opgeleverd</li>
        </ul>
        <p style="margin-top:20px;">Shoots vinden plaats in en rond Breda, met klanten die uit heel Brabant en daarbuiten komen &mdash; branding fotografie Nederland-breed, op aanvraag.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn3.svg" alt="Branding fotoshoot in Breda" width="900" height="900" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/portfolio/" class="btn-outline-dark">Bekijk branding fotografie in het portfolio</a></p>
  </div>
</section>
"""
    page(
        "/branding-photography/",
        "Branding Fotograaf Breda | Personal Branding | Studio Crave",
        "Branding fotografie en personal branding shoots in Breda: creative direction, styling en beeld dat aansluit op je merkstrategie en visuele identiteit.",
        "Breng je merk tot leven.",
        body,
        trail=[("Home", "/"), ("Branding", "/branding/"), ("Branding Fotografie", "/branding-photography/")],
        extra_jsonld=[service_jsonld("Branding Fotografie", "Branding en personal branding fotografie voor vrouwelijke ondernemers, gevestigd in Breda.", "/branding-photography/")],
    )


# ---------------------------------------------------------------------------
# BRANDING BREDA
# ---------------------------------------------------------------------------
def build_branding_breda():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 48px;">
      <span class="section-label">Breda</span>
      <h1 class="section-title section-title-dark">Branding studio in Breda voor vrouwen die klaar zijn om te groeien.</h1>
    </div>
    <div class="intro-grid">
      <div class="intro-text">
        <p>Studio Crave is gevestigd in Breda, Noord-Brabant, en werkt met vrouwelijke ondernemers, founders en creatieven uit de regio &mdash; en, via video, door heel Nederland.</p>
        <p>Lokale klanten krijgen de volledige studio-ervaring in persoon: strategiesessies, reviews van de visuele identiteit en branding shoots in en rond Breda. Klanten verderop krijgen hetzelfde 7-gangen-proces, via calls en gedeelde boards, met shootdagen ingepland wanneer reizen zinvol is.</p>
        <h2 style="font-size:26px;margin:32px 0 16px;color:var(--midnight);font-weight:700;">Zo ziet werken met Studio Crave vanuit Breda eruit</h2>
        <ul class="recognition-list">
          <li>Een strategiesessie op locatie in de studio, of een koffietentje in de buurt</li>
          <li>Branding fotografie op locatie in Breda of Brabant</li>
          <li>De volledige <a href="/7-course-branding-experience/">7-Course Branding Experience</a>, van ingredi&euml;nt tot launch</li>
          <li>Een merk dat meegroeit met je business, niet alleen goed oogt op dag &eacute;&eacute;n</li>
        </ul>
        <p style="margin-top:20px;">Waarom merkstrategie hier telt, is dezelfde reden waarom het overal telt: een groeiende business in een compacte, competitieve stad als Breda heeft een merk nodig dat meteen duidelijk is, niet eentje dat twee keer uitgelegd moet worden.</p>
      </div>
      <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Studio Crave, branding studio in Breda" width="900" height="1100" loading="lazy"></div>
    </div>
    <p style="text-align:center;margin-top:40px;"><a href="/contact/" class="btn-primary">Werk met Studio Crave</a></p>
  </div>
</section>
"""
    page(
        "/branding-breda/",
        "Branding Breda | Branding Studio & Merkstrategie | Studio Crave",
        "Studio Crave is een branding studio in Breda voor vrouwelijke ondernemers die klaar zijn om te groeien. Merkstrategie, positionering, visuele identiteit, fotografie en launch.",
        "Branding studio in Breda voor vrouwen die klaar zijn om te groeien.",
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
        <img src="/images/shoot{i+1}.svg" alt="{esc(p['name'])} brand fotografie, {esc(p['industry'])}" width="900" height="1125" loading="lazy">
        <div class="portfolio-teaser-label"><span>{esc(p['name'])}</span><small>{esc(p['client'])} &mdash; {esc(p['industry'])}</small></div>
      </a>""")
    body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:680px;margin:0 auto 48px;">
      <span class="section-label">Signature Dishes</span>
      <h1 class="section-title section-title-dark">Geselecteerd werk.</h1>
      <p style="color:rgba(31,19,21,0.6);">Elk project hieronder doorliep de volledige <a href="/7-course-branding-experience/">7-Course Branding Experience</a> &mdash; strategie, positionering, stem, visuele identiteit, fotografie en launch.</p>
    </div>
    <div class="portfolio-teaser-grid">{''.join(cards)}</div>
  </div>
</section>
"""
    page(
        "/portfolio/",
        "Portfolio | Branding Cases | Studio Crave",
        "Branding cases van Studio Crave: strategie, positionering, visuele identiteit en fotografie voor vrouwelijke ondernemers, van eerste concept tot launch.",
        "Geselecteerd werk.",
        body,
        trail=[("Home", "/"), ("Portfolio", "/portfolio/")],
    )


def build_portfolio_cases():
    for i, p in enumerate(PORTFOLIO):
        body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 40px;">
      <span class="section-label">{esc(p['client'])} &mdash; {esc(p['industry'])}</span>
      <h1 class="section-title section-title-dark">{esc(p['name'])}</h1>
    </div>
    <div class="polaroid polaroid-main" style="max-width:560px;margin:0 auto 56px;">
      <img src="/images/shoot{i+1}.svg" alt="{esc(p['name'])} branding shoot" width="900" height="1125" loading="eager">
    </div>
    <div class="case-study">
      <div class="case-block"><h2>De uitdaging</h2><p>{esc(p['challenge'])}</p></div>
      <div class="case-block"><h2>De strategie</h2><p>{esc(p['strategy'])}</p></div>
      <div class="case-block"><h2>De positionering</h2><p>{esc(p['positioning'])}</p></div>
      <div class="case-block"><h2>De stem</h2><p>{esc(p['voice'])}</p></div>
      <div class="case-block"><h2>De visuele identiteit</h2><p>{esc(p['visual'])}</p></div>
      <div class="case-block"><h2>De shoot</h2><p>{esc(p['shoot'])}</p></div>
      <div class="case-block"><h2>De launch</h2><p>{esc(p['launch'])}</p></div>
      <div class="case-block"><h2>Het resultaat</h2><p>{esc(p['result'])}</p></div>
    </div>
    <blockquote class="case-quote" style="display:block;max-width:640px;margin:48px auto 0;">&ldquo;{esc(p['quote'])}&rdquo;</blockquote>
    <p style="text-align:center;margin-top:48px;">
      <a href="/portfolio/" class="btn-outline-dark">Terug naar portfolio</a>
      &nbsp; <a href="/7-course-branding-experience/" class="btn-outline-dark">Bekijk de 7 gangen</a>
    </p>
  </div>
</section>
"""
        page(
            f"/portfolio/{p['slug']}/",
            f"{p['name']} | Branding Case | Studio Crave",
            f"Hoe Studio Crave {p['name']} ({p['industry']}) herpositioneerde via merkstrategie, visuele identiteit en fotografie, als onderdeel van de 7-Course Branding Experience.",
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
      <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Jasmijn Straver, oprichter van Studio Crave" width="900" height="1100" loading="eager"></div>
      <div class="intro-text">
        <span class="section-label">Over Jasmijn</span>
        <h1 class="section-title section-title-dark">De chef achter de keuken.</h1>
        <p>Ik ben Jasmijn Straver: creative director, merkstrateeg en fotograaf. Mijn achtergrond loopt van marketing en communicatie via events en NLP naar fotografie. De rode draad was altijd dezelfde: creativiteit als manier om te voelen, te verbinden en impact te maken.</p>
        <p>Die draad liep via Selfcare Studio en Bold Visuals naar Studio Crave, mijn creative studio. The Branding Kitchen is de methode die daaruit ontstond: alles wat ik weet over merken, in zeven gangen.</p>
        <p>De meeste branding-trajecten sturen je voor de foto's door naar iemand anders. Bij mij zitten de strategie en de camera in dezelfde keuken. Daardoor klopt het beeld met het verhaal.</p>
        <blockquote style="font-family:var(--font-heading);font-size:22px;font-weight:700;color:var(--burgundy);border-left:3px solid var(--pepper);padding-left:20px;margin:20px 0;">Content gaat nooit alleen over wat zichtbaar is. Het gaat over wat voelbaar wordt.</blockquote>
      </div>
    </div>
  </div>
</section>
"""
    page(
        "/about/",
        "Over Jasmijn Straver | Studio Crave — Branding Studio Breda",
        "Jasmijn Straver is creative director, merkstrateeg en fotograaf achter Studio Crave en The Branding Kitchen — branding studio in Breda voor vrouwelijke ondernemers.",
        "De chef achter de keuken.",
        body,
        trail=[("Home", "/"), ("Over Jasmijn", "/about/")],
    )


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def build_contact():
    body = """
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:680px;margin:0 auto 48px;">
      <span class="section-label">Contact</span>
      <h1 class="section-title section-title-dark">Klaar om je merk craveable te maken?</h1>
      <p style="color:rgba(31,19,21,0.6);">Vertel waar je business nu staat, en waar je merk hem naartoe moet brengen.</p>
    </div>
    <form class="contact-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="contact">
      <p class="visually-hidden"><label>Niet invullen: <input name="bot-field"></label></p>
      <div class="form-row">
        <label for="name">Naam</label>
        <input id="name" name="name" type="text" required autocomplete="name">
      </div>
      <div class="form-row">
        <label for="business">Bedrijfsnaam</label>
        <input id="business" name="business" type="text" required autocomplete="organization">
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="website">Website</label>
          <input id="website" name="website" type="url" placeholder="https://">
        </div>
        <div class="form-row">
          <label for="instagram">Instagram</label>
          <input id="instagram" name="instagram" type="text" placeholder="@jouwbedrijf">
        </div>
      </div>
      <div class="form-row">
        <label for="what">Wat doe je?</label>
        <textarea id="what" name="what" rows="3" required></textarea>
      </div>
      <div class="form-row">
        <label for="struggle">Wat werkt er nu niet aan je merk?</label>
        <textarea id="struggle" name="struggle" rows="3" required></textarea>
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="stage">Waar sta je in je business?</label>
          <select id="stage" name="stage" required>
            <option value="">Kies een optie</option>
            <option>Net begonnen</option>
            <option>Gevestigd, klaar om te groeien</option>
            <option>Succesvol, merk heeft het niet bijgehouden</option>
          </select>
        </div>
        <div class="form-row">
          <label for="support">Waar ben je naar op zoek?</label>
          <select id="support" name="support" required>
            <option value="">Kies een optie</option>
            <option>Volledige 7-Course Branding Experience</option>
            <option>Alleen brand strategie</option>
            <option>Alleen visuele identiteit</option>
            <option>Alleen branding fotografie</option>
            <option>Nog niet zeker</option>
          </select>
        </div>
      </div>
      <div class="form-row-group">
        <div class="form-row">
          <label for="investment">Investeringsrange</label>
          <select id="investment" name="investment">
            <option value="">Liever niet zeggen</option>
            <option>&euro;1.500 &ndash; &euro;3.000</option>
            <option>&euro;3.000 &ndash; &euro;6.000</option>
            <option>&euro;6.000+</option>
          </select>
        </div>
        <div class="form-row">
          <label for="timeline">Tijdlijn</label>
          <select id="timeline" name="timeline">
            <option value="">Kies een optie</option>
            <option>Zo snel mogelijk</option>
            <option>Binnen 3 maanden</option>
            <option>Ik oriënteer me nog</option>
          </select>
        </div>
      </div>
      <button type="submit" class="btn-primary" style="border:none;cursor:pointer;">Stuur je aanvraag</button>
    </form>
    <div style="text-align:center;margin-top:48px;color:rgba(31,19,21,0.5);font-size:14px;">
      Studio Crave &middot; The Branding Kitchen &middot; Breda, Noord-Brabant
    </div>
  </div>
</section>
"""
    page(
        "/contact/",
        "Werk met Studio Crave | Branding Studio Breda",
        "Plan een kennismaking met Studio Crave / The Branding Kitchen, een branding studio in Breda. Vertel over je business en waar je merk naartoe moet.",
        "Klaar om je merk craveable te maken?",
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
