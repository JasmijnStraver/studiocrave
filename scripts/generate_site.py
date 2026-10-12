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
        "detail": "Wie je echt bent: je verhaal, je energie, je expertise en je rafelrandjes, want daar zit de smaak. We starten met een kick-off call. Alles wat je meebrengt, komt in je persoonlijke merkgeheugen. Daar bouwt de rest op.",
        "what": "We brengen in kaart wie je bent, wat je al weet, en wat je meeneemt uit alles wat je al hebt opgebouwd — voordat er iets veranderd wordt.",
        "receive": "Een helder beeld van je ruwe ingrediënten: je sterktes, je verhaal, en de gaten die het echt waard zijn om te dichten.",
        "why": "De meeste rebrands gaan hier al mis. Je kunt geen sterk merk bouwen op ingrediënten waar nog niemand goed naar heeft gekeken.",
        "status": "done",
    },
    {
        "n": "02", "roman": "II", "slug": "flavor-profile", "name": "Flavor Profile",
        "short": "De smaak van je merk: tone of voice, energie en vibe. Wat maakt jou herkenbaar na één zin?",
        "menu_desc": "Tone of voice, energie en vibe",
        "detail": "Hoe je klinkt als niemand meekijkt. Je toon, je woorden wél en je woorden nooit. Vanaf hier klinkt alles wat je schrijft als jou.",
        "what": "We bepalen hoe je merk klinkt en voelt — de woorden, de toon en de energie die overal terugkomen.",
        "receive": "Een tone-of-voice-gids: hoe je wel schrijft, hoe je nooit schrijft, en de taal die onmiskenbaar van jou is.",
        "why": "Zonder uitgesproken smaak ben je gewoon... correct. En correct wordt niet onthouden.",
        "status": "active",
    },
    {
        "n": "03", "roman": "III", "slug": "signature-sauce", "name": "Signature Sauce",
        "short": "Jouw methode, visie en frameworks. Het ding waar mensen voor terugkomen.",
        "menu_desc": "Jouw unieke methode, visie en frameworks",
        "detail": "Je werkwijze, helder gemaakt. Een methode met een naam, stappen en een belofte. Die komt later terug in je beelden en templates.",
        "what": "We halen eruit wat jij anders doet dan ieder ander, en zetten dat om in taal en een framework dat klanten herkennen.",
        "receive": "Jouw signature positioneringszin, plus de bewijsstukken die hem onderbouwen.",
        "why": "Dit is waar klanten voor terugkomen, en wat ze doorvertellen als ze je aanbevelen.",
        "status": "open",
    },
    {
        "n": "04", "roman": "IV", "slug": "positioning-cut", "name": "Positioning Cut",
        "short": "Waar snijd je jezelf los van de massa? Je niche, je claims en je grenzen.",
        "menu_desc": "Niche, claims en grenzen + voorbereiding brand shoot",
        "detail": "Kiezen, en nee durven zeggen. Je belofte, je doelgroep en wat je níet bent. Hier krijgt je merk ook een gezicht: je Craveable Identity, met logo, kleuren, lettertypen en beeldstijl. En we bereiden je brand shoot voor.",
        "what": "We beslissen wat je merk niet is — welke doelgroep, diensten en taal je bewust achterlaat.",
        "receive": "Een scherpe positionering: je niche, je claim, en de grenzen die hem helder houden.",
        "why": "Een merk dat iedereen wil bedienen, wordt door niemand gekozen. Snijden is wat de rest van het menu logisch maakt.",
        "status": "open",
    },
    {
        "n": "05", "roman": "V", "slug": "plating", "name": "Plating",
        "short": "Hoe je jezelf serveert: je brand shoot, je contentformats, je hooks en je verhalen.",
        "menu_desc": "Content formats, hooks en storytelling + brand shoot",
        "detail": "De gang waar je merk zichtbaar wordt. Je brand shoot, geregisseerd op jouw verhaal. Daarna ruim 100 social templates met je eigen foto's, en een contentplan waarin je pijlers en je funnel samenkomen.",
        "what": "Logo, kleur, typografie en art direction — gebouwd vanuit de strategie, niet ervoor.",
        "receive": "Een complete visuele identiteit: je merktekens, kleurenpalet, typografie en gebruiksrichtlijnen.",
        "why": "Plating is presentatie, geen decoratie. Het is het eerste dat mensen zien, en het moet meteen het juiste zeggen.",
        "status": "open",
    },
    {
        "n": "06", "roman": "VI", "slug": "pairing", "name": "Pairing",
        "short": "Klopt alles samen? Je aanbod, je prijs en je klantreis passen bij het merk dat je neerzet.",
        "menu_desc": "Aanbod, prijs en klantreis",
        "detail": "Verkopen zonder dat het voelt als verkopen. Je aanbod en prijs, en een salespagina die je klanten laat knikken.",
        "what": "We checken of je prijs, je aanbod en de ervaring van je klant allemaal hetzelfde zeggen als je nieuwe merk.",
        "receive": "Een aanbod en klantreis die kloppen met het merk dat je net hebt neergezet.",
        "why": "Een premium merk met een budget-aanbod verwart mensen. Pairing is waar merk en business elkaar ontmoeten.",
        "status": "open",
    },
    {
        "n": "07", "roman": "VII", "slug": "the-experience", "name": "The Experience",
        "short": "Hoe voelt het om met jou te werken? Beleving, energie en exclusiviteit, van eerste DM tot testimonial.",
        "menu_desc": "Hoe samenwerken met jou voelt",
        "detail": "Hoe het voelt om met jou te werken. Je klantreis, je welkomstmail, je signature touch en hoe je om een review vraagt.",
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
]

# Cases nog aan te vullen (echte klanten, nog geen casetekst — geen content verzinnen).
PORTFOLIO_PLACEHOLDERS = [
    {"slug": "personal-brand", "name": "Personal brand positionering", "industry": "Positionering"},
    {"slug": "luve", "name": "LUVÉ", "industry": "Craveable Identity"},
    {"slug": "lamare-professional", "name": "LAMARE Professional", "industry": "Branded Templates"},
    {"slug": "nailsroom-breda", "name": "Nailsroom Breda", "industry": "Brand shoot"},
]

MENU_ITEMS = [
    {
        "name": "Brand Audit", "price": "€77", "href": "/contact/", "cta": "Start met een audit",
        "desc": "Ik proef je merk zoals het nu is. Per gang (je verhaal, je toon en je positionering) krijg je een score, wat ik zie en je eerste stap. Plus je top 3 acties, mijn advies en een persoonlijke video waarin ik je audit doorloop. Twee weken, plus vier weken toegang tot je portaal.",
    },
    {
        "name": "Be Your Own Chef", "price": "€25 / maand (binnenkort)", "href": "/contact/", "cta": "Meer info",
        "desc": "Alle zeven gangen in je eigen tempo, met tools die je merk kennen, je sous-chef en je workflow. Zelf bouwen, zo lang je wilt.",
    },
]

BRAND_EXPERIENCE = {
    "name": "7-Course Brand Experience", "price": "€2.500",
    "desc": "Drie maanden traject plus drie maanden toegang tot je portaal. Alle zeven gangen, van je rauwe ingrediënten tot je Signature Dish.",
    "note": "Introductieprijs (later €3.500). Los geboekt kost dit samen €5.162 — jij betaalt €2.500.",
}

# Brand shoots (Shoots & Designs)
SHOOTS = [
    ("Kick Off Shoot", "€347", "€297 met templates", "1 uur, minimaal 15 foto's. Voor je eerste set eigen beelden: je profielfoto, je website, je eerste posts."),
    ("Full Shoot Day", "€847", "€797 met templates", "3 tot 4 uur, 60 tot 80 foto's. Voor maanden aan content: meerdere looks, locaties en momenten."),
]

# Craveable Identity + Branded Templates (Shoots & Designs)
SHOOTS_ITEMS = [
    {
        "name": "Craveable Identity", "price": "€395", "note": "later €450", "href": "/contact/", "cta": "Bekijk Craveable Identity",
        "desc": "Je merk in de basis neergezet. Een logo-set, je kleurpalet, lettertypen, beeldstijl en grafische elementen die samen één gevoel oproepen. In een brandbook en een ingerichte Brand Kit in Canva, met basistoepassingen zoals je profielfoto en mailhandtekening. Eén maand, plus een maand toegang tot je portaal.",
    },
    {
        "name": "Branded Templates", "price": "€450", "note": "later €550", "href": "/contact/", "cta": "Bekijk de templates",
        "desc": "Ruim 100 social templates in jouw kleuren en lettertypen, zo goed passend dat je ze niet meer als template herkent. Afgestemd op wat je nodig hebt: zichtbaarheid, een lancering of verkoop. Met je brandbook en Brand Kit in Canva, zodat je zelf in een paar minuten post. Eén maand, plus een maand toegang tot je portaal.",
    },
]

ADDONS = [
    ("Andere shoots en campagnes", "Op aanvraag", "Van productshoots tot campagnes op maat."),
    ("Website op maat", "In overleg", "Een website die klopt met de identiteit die we samen hebben gebouwd."),
    ("Iets anders", "In overleg", "Past je vraag niet in het menu? Vertel me waar je naar zoekt."),
]

FAQ = [
    ("Voor wie is Studio Crave?", "Voor coaches, consultants en andere ondernemers die goed zijn in hun vak, maar online nog niet laten zien wie ze zijn. Je hebt klanten, je hebt een verhaal, en je bent klaar om op te vallen."),
    ("Wat is het verschil tussen de 7-Course en losse onderdelen?", "Losse onderdelen geven je een sterk stuk: een identiteit, templates of een shoot. De 7-Course geeft je een merk waarin alles op elkaar aansluit, van je verhaal tot je beelden en je aanbod. Daarom raad ik bijna altijd het hele menu aan."),
    ("Ik heb al een logo of kleuren. Betaal ik daar dubbel voor?", "Nee. Heb je een onderdeel al, dan vullen we die gang met uitbreidend werk van gelijke waarde, zoals een extra templateset of een uitgebreid moodboard."),
    ("Hoeveel tijd kost het mij?", "Gemiddeld een paar uur per gang: de onboarding invullen, aanleveren wat je hebt, met de tools aan de slag en feedback geven. De shoot plannen we samen, op een moment dat bij je past."),
    ("Hoe lang duurt de 7-Course?", "Drie maanden. De gang met je brand shoot en templates duurt soms wat langer, omdat het plannen van de shoot en het bewerken tijd kosten."),
    ("Heb ik professionele foto's nodig voor Branded Templates?", "Ja. Templates werken alleen met beelden die net zo goed zijn als je merk. Heb je ze nog niet? Combineer je templates met een Kick Off shoot of Full Shoot Day, met €50 korting."),
    ("Waar vindt de shoot plaats?", "Op een buitenlocatie die bij je verhaal past, gratis. Liever een studio of een andere ruimte? Dat kan, voor eigen kosten. Reiskosten komen erbij."),
    ("Hoe vaak spreken we elkaar?", "In de 7-Course drie keer persoonlijk: bij de start, halverwege en bij de afronding. Daartussen stel je je vraag in je portaal, of app of mail je me."),
    ("Wat gebeurt er na mijn traject?", "Je portaal blijft nog een tijd open: 3 maanden na de 7-Course, 1 maand na Branded Templates of Craveable Identity, en 4 weken na een Brand Audit. Je Signature Dish en je documenten blijven altijd van jou. Wil je langer met je tools en sous-chef werken? Laat het me weten, dan regel ik het."),
    ("Zijn de tools in het portaal AI?", "Ja, de tools en de sous-chef werken met Claude. Het verschil met een losse chatbot: ze kennen jouw merk. Je toon, je doelgroep, je verhaal en je methode gaan altijd mee. Daarom klinkt wat eruit komt als jou, niet als iedereen."),
    ("Wat gebeurt er met mijn gegevens?", "Je gegevens staan veilig opgeslagen in de EU, en alleen jij en ik zien ze. Wil je dat ik alles verwijder? Dan regel ik dat persoonlijk."),
]

ARCHETYPES = [
    ("The Classic", "Tijdloos, betrouwbaar, expert-energie. Valkuil: te voorzichtig geprijsd."),
    ("The Signature", "Gedurfd en herkenbaar aan één element. Valkuil: inconsistent over tijd."),
    ("Chef's Special", "De diepe specialist met autoriteit. Valkuil: te bescheiden."),
    ("The Fusion", "Verbindt werelden die niemand samenbracht. Valkuil: verwarrend voor klanten."),
]

SERVICE_LINKS = [
    ("7-Course Brand Experience", "/7-course-branding-experience/"),
    ("Shoots & Designs", "/shoots-designs/"),
    ("Portfolio", "/portfolio/"),
    ("Plan kennismaking", "/plan-kennismaking/"),
]

NAV_LINKS = [
    ("Studio Crave", "/"),
    ("7 Course", "/7-course-branding-experience/"),
    ("Branding & Aanbod", "/shoots-designs/"),
    ("Portfolio & Werk", "/portfolio/"),
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
    last = len(NAV_LINKS) - 1
    for i, (label, path) in enumerate(NAV_LINKS):
        if i == last:
            cls = "btn-nav"
        else:
            cls = "active" if path == current_path else ""
        cls_attr = f' class="{cls}"' if cls else ""
        items.append(f'<li><a href="{path}"{cls_attr}>{esc(label)}</a></li>')
    return f"""
<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo"><img src="/images/studio-crave-logo-licht.png" alt="Studio Crave"></a>
    <ul class="nav-links" id="navLinks">
      {''.join(items)}
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

// Mobile menu: keep aria-expanded in sync, and close the menu once a link is chosen.
(function () {{
  var toggle = document.querySelector('.nav-toggle');
  var links = document.getElementById('navLinks');
  if (!toggle || !links) return;
  toggle.setAttribute('aria-expanded', 'false');
  toggle.addEventListener('click', function () {{
    var isOpen = links.classList.contains('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  }});
  links.querySelectorAll('a').forEach(function (a) {{
    a.addEventListener('click', function () {{
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }});
  }});
}})();

// Form validation: inline feedback as people type, then a mailto fallback on submit
// (this is a static site with no backend — swap data-mailto for a real endpoint later if needed).
document.querySelectorAll('.js-validate').forEach(function (form) {{
  var fields = Array.prototype.slice.call(form.querySelectorAll('input, select, textarea'));

  function messageFor(field) {{
    if (field.validity.valueMissing) return 'Dit veld is verplicht.';
    if (field.validity.typeMismatch && field.type === 'email') return 'Vul een geldig e-mailadres in.';
    return 'Controleer dit veld.';
  }}

  function validateField(field) {{
    var row = field.closest('.form-row');
    if (!row) return true;
    var errorEl = row.querySelector('.field-error');
    var ok = field.checkValidity();
    row.classList.toggle('has-error', !ok);
    row.classList.toggle('is-valid', ok && field.value.trim() !== '');
    if (errorEl) errorEl.textContent = ok ? '' : messageFor(field);
    return ok;
  }}

  fields.forEach(function (field) {{
    field.addEventListener('blur', function () {{ validateField(field); }});
    field.addEventListener('input', function () {{
      var row = field.closest('.form-row');
      if (row && row.classList.contains('has-error')) validateField(field);
    }});
  }});

  form.addEventListener('submit', function (e) {{
    e.preventDefault();
    var allOk = true;
    var firstInvalid = null;
    fields.forEach(function (field) {{
      var ok = validateField(field);
      if (!ok) {{
        allOk = false;
        if (!firstInvalid) firstInvalid = field;
      }}
    }});
    if (!allOk) {{
      if (firstInvalid) firstInvalid.focus();
      form.classList.remove('shake');
      void form.offsetWidth;
      form.classList.add('shake');
      return;
    }}
    var lines = fields.map(function (field) {{ return field.name + ': ' + field.value; }});
    var to = form.getAttribute('data-mailto') || 'info@studiocrave.nl';
    var subject = form.getAttribute('data-subject') || 'Bericht via studiocrave.nl';
    var body = encodeURIComponent(lines.join('\\n'));
    window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + body;
    var successEl = form.querySelector('.form-success');
    if (successEl) {{
      successEl.innerHTML = form.getAttribute('data-success') || 'Bedankt voor je bericht!';
      successEl.classList.add('visible');
    }}
  }});
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


# Welke gangen ook los te boeken zijn via Shoots & Designs, en waar dat staat.
LOSSE_GANGEN = {
    "positioning-cut": ("Craveable Identity", "/shoots-designs/#craveable-identity", "vanaf €395"),
    "plating": ("Brand shoot & Branded Templates", "/shoots-designs/#brand-shoots", "vanaf €347"),
}


def course_menu_card_html():
    rows = []
    for c in COURSES:
        losse = LOSSE_GANGEN.get(c["slug"])
        badge = (
            f'<a href="{losse[1]}" class="course-menu-badge">Ook los te boeken: {esc(losse[0])} &middot; {esc(losse[2])}</a>'
            if losse else ""
        )
        rows.append(f"""
      <details class="course-menu-item" id="{c['slug']}">
        <summary class="course-menu-link">
          <span class="course-menu-roman">{c['roman']}</span>
          <span class="course-menu-body">
            <span class="course-menu-name">{esc(c['name'])}</span>
            <span class="course-menu-desc">{esc(c['menu_desc'])}</span>
          </span>
          <span class="course-menu-arrow" aria-hidden="true">&rarr;</span>
        </summary>
        <div class="course-menu-detail">
          <p>{esc(c['detail'])}</p>
          {badge}
        </div>
      </details>""")
    return '<div class="course-menu-card">' + "".join(rows) + '</div>'


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
      <p class="progress-footer">Signature Dish &mdash; de plek waar je branding &amp; business in &eacute;&eacute;n oogopslag samenkomen, geserveerd na je laatste gang.</p>
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
POLAROID_CAPTIONS = {
    "maison-de-vintage": "Grand-hotel-luxe",
    "old-money-power": "Quiet confidence",
    "editorial-noir": "Parijse editorial",
    "la-dolce-vita": "Amalfi-zomer",
}


def work_slider_html():
    """Signature Dishes op de home: polaroid + tekst per case, doorbladeren met pijlen, bolletjes, swipe of toetsenbord."""
    n = len(PORTFOLIO)
    tilts = ["-2deg", "1.6deg", "-1.4deg", "1.8deg"]
    slides = []
    for i, p in enumerate(PORTFOLIO):
        caption = POLAROID_CAPTIONS.get(p["slug"], p["name"])
        slides.append(f'''<div class="work-slide" data-slide="{i}" role="group" aria-roledescription="slide" aria-label="{i+1} van {n}: {esc(p["name"])}"{"" if i == 0 else " hidden"}>
        <figure class="polaroid work-polaroid" style="--tilt:{tilts[i % len(tilts)]}">
          <img src="/images/shoot{i+1}.svg" alt="{esc(p["name"])} brand fotografie" width="900" height="1125" loading="lazy">
          <figcaption>{esc(caption)}</figcaption>
        </figure>
        <div class="work-slide-text">
          <span class="work-count">{i+1} van {n}</span>
          <h3>{esc(p["name"])}</h3>
          <p class="work-client">{esc(p["client"])}, {esc(p["industry"])}</p>
          <p>{esc(p["visual"])}</p>
          <p class="work-result"><strong>Resultaat:</strong> {esc(p["result"])}</p>
          <a class="work-link" href="/portfolio/{p["slug"]}/">Bekijk de case &rarr;</a>
        </div>
      </div>''')
    dot_parts = []
    for i, p in enumerate(PORTFOLIO):
        current_attr = ' aria-current="true"' if i == 0 else ""
        dot_parts.append(
            f'<button type="button" class="work-dot" data-dot="{i}" aria-label="Toon {esc(p["name"])}"{current_attr}><span></span></button>'
        )
    dots = "".join(dot_parts)
    return f'''<div class="work-slider" id="work-slider" role="region" aria-roledescription="carousel" aria-label="Signature Dishes" tabindex="0">
      {"".join(slides)}
      <div class="work-controls">
        <div class="work-dots">{dots}</div>
        <div class="work-arrows">
          <button type="button" class="work-arrow" id="work-prev" aria-label="Vorige case"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>
          <button type="button" class="work-arrow" id="work-next" aria-label="Volgende case"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>
    </div>
    <script>
    (function(){{
      var slider=document.getElementById('work-slider'); if(!slider) return;
      var slides=slider.querySelectorAll('[data-slide]'), dots=slider.querySelectorAll('[data-dot]'), n=slides.length, cur=0;
      function show(i){{
        cur=(i+n)%n;
        slides.forEach(function(s,k){{ s.hidden = k!==cur; }});
        dots.forEach(function(d,k){{ if(k===cur) d.setAttribute('aria-current','true'); else d.removeAttribute('aria-current'); }});
      }}
      document.getElementById('work-prev').addEventListener('click',function(){{ show(cur-1); }});
      document.getElementById('work-next').addEventListener('click',function(){{ show(cur+1); }});
      dots.forEach(function(d){{ d.addEventListener('click',function(){{ show(+d.getAttribute('data-dot')); }}); }});
      slider.addEventListener('keydown',function(e){{ if(e.key==='ArrowLeft') show(cur-1); else if(e.key==='ArrowRight') show(cur+1); }});
      var x0=null;
      slider.addEventListener('touchstart',function(e){{ x0=e.touches[0].clientX; }},{{passive:true}});
      slider.addEventListener('touchend',function(e){{ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; x0=null; if(Math.abs(dx)>40) show(dx<0?cur+1:cur-1); }});
    }})();
    </script>'''


HERO_VIDEO_PATH = "/images/hero.mp4"


def hero_video_html():
    if not os.path.exists(os.path.join(ROOT, HERO_VIDEO_PATH.lstrip("/"))):
        return ""
    return f'<video class="hero-video" autoplay muted loop playsinline poster="/images/banner-jasmijn.jpg"><source src="{HERO_VIDEO_PATH}" type="video/mp4"></video>'


def build_home():
    body = f"""
<section class="hero">
  {hero_video_html()}
  <div class="hero-bg"></div>
  <div class="hero-content">
    <div class="container">
      <div class="hero-split">
        <div class="hero-inner" style="text-align:left;">
          <h1>Ready to create <em>some cravings?</em></h1>
          <p class="hero-sub">Ik maak geen logo's. Ik serveer merken waar mensen naar verlangen.</p>
          <div class="hero-actions" style="justify-content:flex-start;">
            <a href="/7-course-branding-experience/#de-rekening" class="btn-primary">Bekijk het menu</a>
            <a href="#quiz" class="btn-outline-light">Doe de quiz: welk gerecht ben jij?</a>
          </div>
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

<section class="section-light section-overlap">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text">
        <span class="section-label">Intro</span>
        <h2 class="section-title section-title-dark">Fastfood-branding is <em>overal</em>.</h2>
        <p>Je bent goed in wat je doet. Je klanten weten het. Maar online zie je eruit als iedereen. Dezelfde templates, dezelfde zinnen, dezelfde stockfoto's. Fastfood-branding.</p>
        <p>Bij Studio Crave krijgt je merk een eigen smaak. Een verhaal dat klopt, beelden die blijven hangen, en een stem die meteen als jou klinkt. Zodat de juiste mensen niet alleen kijken, maar blijven.</p>
      </div>
      <div class="intro-image-wrap">
        <div class="intro-image">
          <img src="/images/jasmijn6.svg" alt="The Branding Kitchen, signature details" width="900" height="900" loading="lazy">
        </div>
        <div class="badge-circle top-left"><img src="/images/cloche-ornament.png" alt="Je merk, straks onthuld"></div>
      </div>
    </div>
  </div>
</section>

<section class="section-burgundy">
  <span class="bg-word bottom" aria-hidden="true">SMAAK</span>
  <div class="container">
    <span class="section-label">Waar we voor staan</span>
    <ul class="recognition-list" style="max-width:720px;margin-top:20px;">
      <li><strong style="font-family:var(--font-heading);color:var(--gold);">Aandacht.</strong> Beeld dat de duim stopt in een tijdlijn vol ruis.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--gold);">Emotie.</strong> Een sfeer die je merk een smaak geeft, geen stijl van de plank.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--gold);">Onvergetelijk.</strong> Een merkervaring die terugkomt in iemands hoofd, lang na de eerste blik.</li>
    </ul>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:620px;margin:0 auto 40px;">
      <span class="section-label">Drie ingangen</span>
      <h2 class="section-title section-title-dark">Kies hoe je aan tafel komt.</h2>
    </div>
    <div class="pillar-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="pillar-card">
        <h3><a href="/7-course-branding-experience/" style="color:inherit;text-decoration:none;">De 7-Course Brand Experience</a></h3>
        <p>Drie maanden samen aan tafel. Je hele merk, van verhaal tot beleving, met brand shoot, ruim 100 templates en je Craveable Identity.</p>
        <p style="margin-top:14px;"><a href="/7-course-branding-experience/" style="font-weight:700;font-size:14px;color:var(--pepper);text-decoration:none;">Proef het menu &rarr;</a></p>
      </div>
      <div class="pillar-card">
        <h3><a href="/shoots-designs/" style="color:inherit;text-decoration:none;">Shoots &amp; Designs</a></h3>
        <p>Een brand shoot, een Craveable Identity of Branded Templates. Een sterk stuk van je merk, los geserveerd.</p>
        <p style="margin-top:14px;"><a href="/shoots-designs/" style="font-weight:700;font-size:14px;color:var(--pepper);text-decoration:none;">Bekijk het werk &rarr;</a></p>
      </div>
      <div class="pillar-card">
        <h3><a href="/contact/" style="color:inherit;text-decoration:none;">Brand Audit &middot; &euro;77</a></h3>
        <p>Twijfel je waar je merk nu staat? Ik proef je merk zoals het is, en vertel je precies waar de smaak zit.</p>
        <p style="margin-top:14px;"><a href="/contact/" style="font-weight:700;font-size:14px;color:var(--pepper);text-decoration:none;">Start met een audit &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section-dark">
  <span class="bg-word top" aria-hidden="true">CRAVE</span>
  <div class="container" style="text-align:center;max-width:640px;margin:0 auto;">
    <span class="section-label">Twee namen, &eacute;&eacute;n keuken</span>
    <p style="color:rgba(247,240,236,0.85);font-size:17px;">Studio Crave is mijn studio. The Branding Kitchen&trade; is hoe ik kook: zeven gangen, van je rauwe ingredi&euml;nten tot een beleving waar mensen voor terugkomen.</p>
  </div>
</section>

<section class="section-dark" id="methode">
  <div class="container" style="text-align:center;max-width:620px;margin:0 auto;">
    <span class="section-label">De methode</span>
    <h2 class="section-title section-title-light">The 7-Course Method</h2>
    <p style="color:rgba(247,240,236,0.8);font-size:17px;">Zeven gangen, in deze volgorde. Een chef begint niet bij het dessert. Elke gang heeft zijn eigen plek in je traject &mdash; en je Signature Dish komt pas na de laatste.</p>
    <p style="margin-top:28px;"><a href="/7-course-branding-experience/" class="btn-primary">Bekijk het hele menu</a></p>
  </div>
</section>

<section class="section-light" id="menu">
  <div class="container">
    <div style="text-align:center;margin-bottom:48px;">
      <span class="section-label">Signature Dishes</span>
      <h2 class="section-title section-title-dark">Vier merken, vier werelden.</h2>
      <p style="color:rgba(31,19,21,0.6);max-width:600px;margin:0 auto;font-size:16px;">Wat er gebeurt als positionering, fotografie en design samenkomen.</p>
    </div>
    {work_slider_html()}
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
        <form class="quiz-form js-validate" name="quiz" novalidate
              data-mailto="info@studiocrave.nl" data-subject="Signature Dish Quiz aanvraag"
              data-success="Bedankt! Je mailprogramma opent zich zo &mdash; verstuur de mail en je krijgt de quiz zelf terug in je inbox.">
          <div class="form-row">
            <label for="quiz-naam">Voornaam</label>
            <input id="quiz-naam" name="Voornaam" type="text" autocomplete="given-name" placeholder="Je voornaam" required>
            <span class="field-error" aria-live="polite"></span>
          </div>
          <div class="form-row">
            <label for="quiz-mail">E-mailadres</label>
            <input id="quiz-mail" name="E-mailadres" type="email" autocomplete="email" placeholder="naam@jouwbedrijf.nl" required>
            <span class="field-error" aria-live="polite"></span>
          </div>
          <button type="submit" class="btn-primary" style="width:100%;">Stuur mij de quiz</button>
          <p class="form-success" aria-live="polite"></p>
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

<section class="cta-section" id="contact">
  <div class="cta-content">
    <h2>Geen losse plaatjes.<br>Een merk dat niet meer te negeren is.</h2>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Plan een kennismaking</a>
      <a href="#quiz" class="btn-outline-light">Eerst de quiz</a>
    </div>
  </div>
</section>
"""
    page(
        "/",
        "Branding Studio Breda | Studio Crave — The Branding Kitchen™",
        "Studio Crave is een branding studio in Breda. Ik maak geen logo's, ik serveer merken waar mensen naar verlangen: via de 7-Course Brand Experience, losse Shoots & Designs, of een Brand Audit.",
        "Ready to create some cravings?",
        body,
        trail=[("Home", "/")],
        extra_jsonld=[service_jsonld("Branding", "Merkstrategie, visuele identiteit, branding fotografie en brand launch voor vrouwelijke ondernemers.", "/")],
    )


# ---------------------------------------------------------------------------
# 7-COURSE BRAND EXPERIENCE (methode + traject + portaal + prijs, in één)
# ---------------------------------------------------------------------------
def build_seven_courses():
    body = f"""
<section class="section-light">
  <div class="container" style="text-align:center;max-width:720px;margin:0 auto;">
    <span class="section-label">De signature route</span>
    <h1 class="section-title section-title-dark">Zeven gangen. &Eacute;&eacute;n merk dat je niet meer vergeet.</h1>
    <p style="font-size:17px;color:rgba(31,19,21,0.6);">The Branding Kitchen&trade; serveert je merk in zeven gangen, in drie maanden. Voor ondernemers die willen opvallen als een Michelin-ster in een markt vol fastfood-branding.</p>
    <div class="hero-actions" style="justify-content:center;margin-top:24px;">
      <a href="#de-rekening" class="btn-primary">Proef het menu</a>
      <a href="/plan-kennismaking/" class="btn-outline-dark">Plan een kennismaking</a>
    </div>
  </div>
</section>

<section class="section-dark">
  <span class="bg-word top" aria-hidden="true">FASTFOOD</span>
  <div class="container" style="max-width:780px;margin:0 auto;text-align:center;">
    <span class="section-label">Het probleem</span>
    <p style="font-size:19px;color:var(--creme);">Je bent goed in wat je doet. Echt goed. En toch kiest je ideale klant voor iemand anders. Niet omdat die beter is. Omdat die beter smaakt.</p>
    <p style="color:rgba(245,240,235,0.75);margin-top:14px;">Een goed merk bouw je niet in &eacute;&eacute;n hap. Het begint bij wat je meebrengt, krijgt smaak in je toon, en wordt pas onweerstaanbaar als alles klopt: je verhaal, je beelden, je aanbod en hoe het voelt om met je te werken.</p>
  </div>
</section>

<section class="section-light">
  <div class="container" style="text-align:center;max-width:620px;margin:0 auto 32px;">
    <span class="section-label">Het menu</span>
    <h2 class="section-title section-title-dark">Zeven gangen, in deze volgorde.</h2>
    <p style="color:rgba(31,19,21,0.6);font-size:16px;">Klik op een gang voor de uitleg. Sommige gangen zijn ook los te boeken.</p>
  </div>
  <div class="container">
    {course_menu_card_html()}
  </div>
</section>

<section class="section-burgundy">
  <span class="bg-word bottom" aria-hidden="true">DISH</span>
  <div class="container">
    <div class="intro-grid" style="align-items:center;">
      <div class="card-visual">
        <img src="/images/tray-card-ornament.png" alt="Signature Dish, geserveerd op tafel" width="596" height="796" loading="lazy">
        <div class="card-visual-text">
          <span class="card-visual-label">Signature<br>Dish</span>
          <span class="card-visual-sub">Na je laatste&nbsp;gang</span>
        </div>
      </div>
      <div>
        <span class="section-label">De Signature Dish</span>
        <p style="font-size:17px;color:rgba(245,240,235,0.9);">Na de zeven gangen serveer ik je Signature Dish: je hele merk op &eacute;&eacute;n bord. Je verhaal, je toon, je methode, je kleuren, je beelden en je templates, bij elkaar en altijd van jou. We sluiten af met een call waarin we je volgende 90 dagen uitzetten.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 32px;">
      <span class="section-label">Je eigen keuken, altijd open</span>
      <h2 class="section-title section-title-dark">Zo volg je je voortgang in de Branding Dashboard.</h2>
      <p style="color:rgba(31,19,21,0.65);font-size:16px;">Als we samenwerken, krijg je een persoonlijk portaal. Daar staat je menu klaar, vind je alles wat ik voor je opdien, en werk je met tools die je merk al kennen. Geen losse mails, mappen en WeTransfers meer. Alles op &eacute;&eacute;n plek, in jouw stijl.</p>
    </div>
    <ul class="recognition-list" style="max-width:760px;margin:0 auto 36px;">
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Je menu.</strong> Alle gangen, met wat ik opdien en wat jij aanlevert. Je geeft akkoord of feedback, en dan pas gaat de volgende gang open.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Tools die je merk kennen.</strong> Voor captions, carrousels, LinkedIn-posts, Reels, mails en meer. Ze kennen je toon, je doelgroep en je verhaal. Ik werk ze elke week bij met wat nu werkt op de kanalen.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Je sous-chef.</strong> Stel je vraag over je merk, je traject of je content, ook buiten kantoortijd.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Workflow.</strong> Focusblokken, je idee&euml;n op &eacute;&eacute;n plek, je 90-dagenplan en je Human Design als lens voor hoe jij het beste werkt.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Documenten.</strong> Je overeenkomst, je werkbladen en alles wat ik voor je klaarzet.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Mijn stijl.</strong> Je kleuren, lettertypen, logo's en beelden, klaar om te kopi&euml;ren.</li>
    </ul>
    <p style="text-align:center;color:rgba(31,19,21,0.6);max-width:640px;margin:0 auto 32px;">Je portaal blijft open tijdens je traject en nog 3 maanden daarna. Je Signature Dish en je documenten blijven altijd van jou.</p>
    {progress_menu_html()}
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div class="intro-grid" style="max-width:900px;margin:0 auto;">
      <div>
        <span class="section-label" style="text-align:left;">Drie momenten samen</span>
        <p style="color:rgba(245,240,235,0.85);font-size:17px;">We spreken elkaar drie keer persoonlijk: bij de start, halverwege en bij de afronding. Daartussen ben ik bereikbaar via je portaal, de app of mail.</p>
      </div>
      <div>
        <span class="section-label" style="text-align:left;">Heb je al iets?</span>
        <p style="font-size:17px;color:rgba(245,240,235,0.85);">Staat je logo al, of je kleuren? Dan vullen we die gang met uitbreidend werk van gelijke waarde, zoals een extra templateset of een uitgebreid moodboard. Je betaalt nooit voor iets wat je al hebt.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-dark" id="de-rekening">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 32px;">
      <span class="section-label">Je investering</span>
      <h2 class="section-title section-title-light">{esc(BRAND_EXPERIENCE['price'])}</h2>
      <p style="color:rgba(245,240,235,0.8);font-size:16px;">{esc(BRAND_EXPERIENCE['desc'])}</p>
      <p style="color:var(--gold);font-size:14px;margin-top:10px;">{esc(BRAND_EXPERIENCE['note'])}</p>
      <p style="margin-top:28px;"><a href="/plan-kennismaking/" class="btn-primary">Plan een kennismaking</a></p>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 40px;">
      <span class="section-label">Nog niet klaar voor het hele menu?</span>
      <h2 class="section-title section-title-dark">Begin kleiner.</h2>
    </div>
    {menu_items_html()}
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:780px;margin:0 auto;text-align:center;">
    <span class="section-label">Voor wie</span>
    <p style="font-size:17px;color:rgba(245,240,235,0.9);">Voor coaches, consultants en andere ondernemers die goed zijn in hun vak, maar online nog niet laten zien wie ze zijn. Je hebt klanten, je hebt een verhaal, en je bent klaar om op te vallen.</p>
    <p style="color:rgba(245,240,235,0.6);margin-top:12px;">Niet voor wie een snelle fix zoekt. Fastfood-branding is er genoeg.</p>
  </div>
</section>

<section class="cta-section">
  <div class="cta-content">
    <h2>Klaar om je merk te laten <em>craven</em>?</h2>
    <div class="hero-actions">
      <a href="/plan-kennismaking/" class="btn-primary">Plan een kennismaking</a>
      <a href="/portfolio/" class="btn-outline-light">Bekijk het in het werk</a>
    </div>
  </div>
</section>
"""
    page(
        "/7-course-branding-experience/",
        "7-Course Brand Experience | The Branding Kitchen™ | Studio Crave",
        "De 7-Course Brand Experience is het complete merktraject van Studio Crave: zeven gangen, een eigen portaal en een Signature Dish aan het einde.",
        "Zeven gangen. Eén merk dat je niet meer vergeet.",
        body,
        trail=[("Home", "/"), ("7-Course Brand Experience", "/7-course-branding-experience/")],
    )


# ---------------------------------------------------------------------------
# BRANDING (overview / service hub)
# ---------------------------------------------------------------------------
def shoots_items_html():
    rows = []
    for item in SHOOTS_ITEMS:
        rows.append(f"""
      <article class="menu-item">
        <div class="menu-item-head">
          <h3>{esc(item['name'])}</h3>
          <span class="menu-leader" aria-hidden="true"></span>
          <span class="menu-price">{esc(item['price'])} <span style="font-size:15px;color:var(--burgundy);">({esc(item['note'])})</span></span>
        </div>
        <p>{esc(item['desc'])}</p>
        <a href="{item['href']}">{esc(item['cta'])}</a>
      </article>""")
    return '<div class="menu-list">' + "".join(rows) + '</div>'


def build_shoots_designs():
    shoot_rows = "".join(f"""
      <article class="menu-item">
        <div class="menu-item-head">
          <h3>{esc(name)}</h3>
          <span class="menu-leader" aria-hidden="true"></span>
          <span class="menu-price">{esc(price)} <span style="font-size:15px;color:var(--burgundy);">({esc(with_templates)})</span></span>
        </div>
        <p>{esc(desc)}</p>
      </article>""" for name, price, with_templates, desc in SHOOTS)

    overview_rows = [
        ("Kick Off shoot", "&euro;347 (&euro;297 met templates)", "1 uur shooten"),
        ("Full Shoot Day", "&euro;847 (&euro;797 met templates)", "3 tot 4 uur shooten"),
        ("Craveable Identity", "&euro;395 (later &euro;450)", "1 maand + 1 maand toegang"),
        ("Branded Templates", "&euro;450 (later &euro;550)", "1 maand + 1 maand toegang"),
        ("Andere shoots, website op maat", "In overleg", "&mdash;"),
    ]
    overview_table = "".join(
        f"<tr><td>{esc(a)}</td><td>{p}</td><td>{esc(d)}</td></tr>" for a, p, d in overview_rows
    )

    body = f"""
<section class="section-light">
  <div class="container" style="text-align:center;max-width:680px;margin:0 auto;">
    <span class="section-label">Shoots &amp; Designs</span>
    <h1 class="section-title section-title-dark">Geserveerd.</h1>
    <p style="font-size:17px;color:rgba(31,19,21,0.65);">Brand shoots, Craveable Identities en Branded Templates. Beeld dat je voelt <em>voordat</em> je het ziet.</p>
  </div>
</section>

<section class="section-burgundy section-overlap">
  <span class="bg-word top" aria-hidden="true">VERLANGEN</span>
  <div class="container" style="max-width:720px;margin:0 auto;text-align:center;">
    <span class="section-label">Intro</span>
    <p style="font-size:17px;color:rgba(245,240,235,0.9);">Elk merk hier begon met dezelfde vraag: waar moet iemand naar verlangen als hij jou ziet? Het antwoord ziet er telkens anders uit. Dat is precies de bedoeling.</p>
    <p style="color:rgba(245,240,235,0.7);margin-top:12px;">Content gaat voor mij nooit alleen over wat zichtbaar is. Het gaat over wat voelbaar wordt. Licht, sfeer, compositie, het moment net voor de lach.</p>
  </div>
</section>

<section class="section-light" id="brand-shoots">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 24px;">
      <span class="section-label">Brand shoots</span>
      <h2 class="section-title section-title-dark">Beelden die je verhaal vertellen.</h2>
      <p style="color:rgba(31,19,21,0.65);font-size:16px;">Niet alleen je gezicht. Vooraf bouwen we een concept: locatie, styling, kleur, gevoel. Op de set regisseer ik, zodat jij alleen jezelf hoeft te zijn. Je krijgt beelden in de Studio Crave-signatuur: cinematisch, warm en editorial.</p>
    </div>
    {shoot_rows and f'<div class="menu-list">{shoot_rows}</div>'}
    <p style="text-align:center;margin-top:20px;color:rgba(31,19,21,0.55);font-size:14px;">Buitenlocatie is gratis. Een studio of andere ruimte is voor eigen kosten. Prijzen exclusief reiskosten en btw.</p>
  </div>
</section>

<section class="section-dark" id="craveable-identity">
  <div class="container">
    {shoots_items_html()}
    <p style="text-align:center;margin-top:8px;color:rgba(245,240,235,0.65);font-size:14px;max-width:640px;margin-left:auto;margin-right:auto;">Templates maak ik alleen met professionele beelden. Heb je die nog niet? Combineer ze met een shoot en je krijgt &euro;50 korting: Kick Off &euro;297, Full Shoot Day &euro;797.</p>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;text-align:center;">
    <span class="section-label">Editorial &amp; portret</span>
    <p style="color:rgba(31,19,21,0.75);font-size:17px;">Naast merken fotografeer ik mensen. Portretten en koppels, cinematisch, warm en dichtbij.</p>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 32px;">
      <span class="section-label">Op maat</span>
      <h2 class="section-title section-title-light">Past je vraag niet in het menu?</h2>
    </div>
    {addons_html()}
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div style="text-align:center;max-width:640px;margin:0 auto 32px;">
      <span class="section-label">Overzicht</span>
    </div>
    <div class="tablewrap" style="overflow-x:auto;">
      <table style="width:100%;border-collapse:collapse;color:var(--creme);">
        <thead><tr style="text-align:left;border-bottom:1px solid rgba(245,240,235,0.25);">
          <th style="padding:10px 14px;">Aanbod</th><th style="padding:10px 14px;">Prijs</th><th style="padding:10px 14px;">Looptijd</th>
        </tr></thead>
        <tbody>{overview_table}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:720px;margin:0 auto 20px;">
      <span class="section-label">Portfolio</span>
      <h2 class="section-title section-title-dark">Geserveerd &mdash; voor hen.</h2>
      <p style="color:rgba(31,19,21,0.6);">Filters: Brand shoots &middot; Branded Templates &middot; Craveable Identity &middot; 7-Course merken &middot; Editorial &amp; portret.</p>
    </div>
    <p style="text-align:center;"><a href="/portfolio/" class="btn-outline-dark">Bekijk het portfolio</a></p>
  </div>
</section>

<section class="cta-section">
  <div class="cta-content">
    <h2>Zin in <em>dit soort</em> merk?</h2>
    <div class="hero-actions">
      <a href="/7-course-branding-experience/" class="btn-primary">Bekijk het menu</a>
      <a href="/plan-kennismaking/" class="btn-outline-light">Plan een kennismaking</a>
    </div>
  </div>
</section>
"""
    page(
        "/shoots-designs/",
        "Shoots & Designs | Brand Shoots, Craveable Identity & Templates | Studio Crave",
        "Brand shoots, Craveable Identity en Branded Templates in Breda. Beeld en visuele identiteit die je voelt voordat je het ziet.",
        "Geserveerd.",
        body,
        trail=[("Home", "/"), ("Shoots & Designs", "/shoots-designs/")],
        extra_jsonld=[service_jsonld("Shoots & Designs", "Brand shoots, Craveable Identity en Branded Templates voor ondernemers, gevestigd in Breda.", "/shoots-designs/")],
    )


# ---------------------------------------------------------------------------
# PORTFOLIO INDEX + CASE STUDIES
# ---------------------------------------------------------------------------
PORTFOLIO_FILTERS = ["Brand shoots", "Branded Templates", "Craveable Identity", "7-Course merken", "Editorial & portret"]


def build_portfolio_index():
    tilts = ["-2deg", "1.6deg", "-1.4deg", "1.8deg", "-1deg"]
    cards = []
    for i, p in enumerate(PORTFOLIO):
        cards.append(f"""
      <a class="portfolio-polaroid" href="/portfolio/{p['slug']}/" style="--tilt:{tilts[i % len(tilts)]}">
        <img src="/images/shoot{i+1}.svg" alt="{esc(p['name'])} brand fotografie, {esc(p['industry'])}" width="900" height="1125" loading="lazy">
        <span class="ppf-name">{esc(p['name'])}</span>
        <span class="ppf-meta">{esc(p['client'])} &mdash; {esc(p['industry'])}</span>
      </a>""")
    for i, p in enumerate(PORTFOLIO_PLACEHOLDERS):
        cards.append(f"""
      <div class="portfolio-polaroid is-placeholder" style="--tilt:{tilts[(i + len(PORTFOLIO)) % len(tilts)]}">
        <div class="ppf-placeholder">Case volgt</div>
        <span class="ppf-name">{esc(p['name'])}</span>
        <span class="ppf-meta">{esc(p['industry'])}</span>
      </div>""")
    filters = "".join(f'<span class="chip" style="display:inline-block;border:1px solid var(--burgundy);border-radius:2px;padding:7px 16px;margin:0 8px 8px 0;font-size:14px;color:var(--burgundy);">{esc(f)}</span>' for f in PORTFOLIO_FILTERS)
    body = f"""
<section class="section-light">
  <div class="container">
    <div style="text-align:center;max-width:680px;margin:0 auto 32px;">
      <span class="section-label">Signature Dishes</span>
      <h1 class="section-title section-title-dark">Geselecteerd werk.</h1>
      <p style="color:rgba(31,19,21,0.65);font-size:16px;">Elk project hieronder doorliep de volledige <a href="/7-course-branding-experience/">7-Course Brand Experience</a>, of een losse gang via <a href="/shoots-designs/">Shoots &amp; Designs</a>.</p>
    </div>
    <div style="text-align:center;margin-bottom:12px;">{filters}</div>
    <p class="portfolio-scroll-hint">&larr; Scroll door het werk &rarr;</p>
    <div class="portfolio-scroll">{''.join(cards)}</div>
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
    <blockquote class="case-quote" style="display:block;max-width:640px;margin:48px auto 0;">
      &ldquo;{esc(p['quote'])}&rdquo;
      <footer style="margin-top:14px;font-family:var(--font-body);font-style:normal;font-size:14px;font-weight:600;color:var(--burgundy);">&mdash; {esc(p['client'])}, {esc(p['industry'])}</footer>
    </blockquote>
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
            f"Hoe Studio Crave {p['name']} ({p['industry']}) herpositioneerde via merkstrategie, visuele identiteit en fotografie, als onderdeel van de 7-Course Brand Experience.",
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
      <div class="intro-image-wrap">
        <div class="intro-image"><img src="/images/jasmijn2.svg" alt="Jasmijn Straver, oprichter van Studio Crave" width="900" height="1100" loading="eager"></div>
        <div class="badge-circle bottom-right"><img src="/images/sc-monogram-relief.png" alt="Studio Crave monogram"></div>
      </div>
      <div class="intro-text">
        <span class="section-label">Over Jasmijn</span>
        <h1 class="section-title section-title-dark">Ik ben Jasmijn. Bold, eigenwijs en diepzinnig.</h1>
        <p>Creative director, visual storyteller en merkstrateeg. Founder van Studio Crave en The Branding Kitchen&trade;.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Mijn verhaal</span>
    <p style="font-size:17px;color:rgba(245,240,235,0.9);">Als kind schilderde ik stenen op de camping, maakte ik sieraden en stond ik op het toneel. Creativiteit was nooit een hobby. Het was mijn manier om te voelen en te verbinden.</p>
    <p style="color:rgba(245,240,235,0.75);margin-top:14px;">Ik groeide op met twee ondernemende ouders en ging op mijn achttiende op mezelf wonen, in een studentenhuis met zeventien meiden. Daarna deed ik van alles: marketing, communicatie, events, branding, NLP en fotografie. Sommigen noemden het jobhoppen. Ik noem het mijn mise en place. Elke baan, elk avontuur leverde een ingredi&euml;nt op dat ik nu elke dag gebruik.</p>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">De rode draad</span>
    <p style="font-size:17px;color:rgba(31,19,21,0.75);">Samen met een vriendin richtte ik Selfcare Studio Breda op, waar het draaide om rust en esthetiek. Daarna kwam Bold Visuals, waar commerci&euml;le impact centraal stond. Vandaag komt alles samen in Studio Crave. Een studio gebouwd rond &eacute;&eacute;n principe: mensen laten verlangen.</p>
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Ambitie, geclaimd</span>
    <p style="font-size:17px;color:rgba(245,240,235,0.9);">Iemand die dichtbij me staat zei ooit: &ldquo;De meeste mensen onderschatten jouw ambitie.&rdquo; Hij had gelijk. Ik ook, lange tijd. Nu niet meer. En precies dat gun ik jou: een merk dat net zo groot denkt als jij.</p>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Hoe ik werk</span>
    <p style="font-size:17px;color:rgba(31,19,21,0.75);">Achter de camera ben ik op mijn best. Mijn stijl is cinematisch, warm en editorial: sterke compositie, sfeer, en een gevoel voor wat werkt. Ik vertaal identiteit naar beeld op een manier die luxe, verlangen en echtheid samenbrengt.</p>
    <p style="color:rgba(31,19,21,0.6);margin-top:14px;">Content gaat voor mij nooit alleen over wat zichtbaar is. Het gaat over wat voelbaar wordt. Wat blijft hangen. En wat ervoor zorgt dat een merk niet meer vergeten wordt.</p>
    <p style="color:rgba(31,19,21,0.6);margin-top:14px;">Ik werk bewust op 80%. Zo houd ik ruimte voor de 100% die ertoe doet: jouw merk, op de momenten dat het telt.</p>
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:720px;margin:0 auto;text-align:center;">
    <span class="section-label">Studio Crave en The Branding Kitchen&trade;</span>
    <p style="font-size:17px;color:rgba(245,240,235,0.9);">Studio Crave is mijn studio. The Branding Kitchen&trade; is hoe ik kook: zeven gangen, van je rauwe ingredi&euml;nten tot een beleving waar mensen voor terugkomen.</p>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Naast het werk</span>
    <p style="font-size:17px;color:rgba(31,19,21,0.75);">Ik zet me in voor jongeren via R-Newt en Next Up. Omdat iedereen het verdient om gezien te worden, en dat begint jong.</p>
  </div>
</section>

<section class="cta-section">
  <div class="cta-content">
    <h2>Ik maak geen logo's.<br>Ik serveer merken waar mensen naar verlangen.</h2>
    <div class="hero-actions">
      <a href="/plan-kennismaking/" class="btn-primary">Plan een kennismaking</a>
    </div>
  </div>
</section>
"""
    page(
        "/about/",
        "Over Jasmijn Straver | Studio Crave — Branding Studio Breda",
        "Jasmijn Straver is creative director, visual storyteller en merkstrateeg. Founder van Studio Crave en The Branding Kitchen™.",
        "Ik ben Jasmijn. Bold, eigenwijs en diepzinnig.",
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
      <h1 class="section-title section-title-dark">Klaar om op te vallen?</h1>
      <p style="color:rgba(31,19,21,0.65);font-size:16px;">Je hoeft niet harder te roepen. Je hoeft alleen te laten zien wie je bent, zo goed dat mensen niet meer kunnen wegkijken. Stuur me je vraag, je idee of die shoot die al maanden in je hoofd zit. Ik lees alles zelf.</p>
    </div>
    <div class="intro-grid" style="margin-bottom:48px;">
      <div>
        <h2 style="font-size:20px;color:var(--midnight);font-weight:700;margin-bottom:14px;">Contactgegevens</h2>
        <ul class="recognition-list">
          <li><strong>Mail of app</strong> &mdash; <a href="mailto:info@studiocrave.nl">info@studiocrave.nl</a></li>
          <li><strong>Instagram</strong> &mdash; <a href="https://instagram.com/studiocrave.nl">@studiocrave.nl</a></li>
          <li><strong>Locatie</strong> &mdash; Breda, Nederland</li>
          <li><strong>KvK</strong> &mdash; [KvK-nummer]</li>
        </ul>
      </div>
      <div>
        <h2 style="font-size:20px;color:var(--midnight);font-weight:700;margin-bottom:14px;">Kort</h2>
        <p style="color:rgba(31,19,21,0.65);">Liever direct aan tafel? <a href="/plan-kennismaking/">Plan een kennismaking</a> en we kijken samen welk menu bij jou past.</p>
      </div>
    </div>
    <form class="contact-form js-validate" name="contact" novalidate
          data-mailto="info@studiocrave.nl" data-subject="Nieuw bericht via studiocrave.nl"
          data-success="Bedankt! Je mailprogramma opent zich zo &mdash; verstuur de mail en ik lees hem zelf, binnen 48 uur hoor je van me.">
      <div class="form-row">
        <label for="name">Naam</label>
        <input id="name" name="Naam" type="text" required autocomplete="name">
        <span class="field-error" aria-live="polite"></span>
      </div>
      <div class="form-row">
        <label for="email">E-mailadres</label>
        <input id="email" name="E-mailadres" type="email" required autocomplete="email">
        <span class="field-error" aria-live="polite"></span>
      </div>
      <div class="form-row">
        <label for="instagram">Instagram of website</label>
        <input id="instagram" name="Instagram-of-website" type="text" placeholder="@jouwbedrijf of je website">
        <span class="field-error" aria-live="polite"></span>
      </div>
      <div class="form-row">
        <label for="topic">Waar gaat het over?</label>
        <select id="topic" name="Onderwerp" required>
          <option value="">Kies een optie</option>
          <option>7-Course Brand Experience</option>
          <option>Brand Audit</option>
          <option>Brand shoot</option>
          <option>Craveable Identity</option>
          <option>Branded Templates</option>
          <option>Iets anders</option>
        </select>
        <span class="field-error" aria-live="polite"></span>
      </div>
      <div class="form-row">
        <label for="what">Vertel me over je merk. Wie ben je, wat doe je, en wat wil je dat mensen voelen?</label>
        <textarea id="what" name="Bericht" rows="4" required></textarea>
        <span class="field-error" aria-live="polite"></span>
      </div>
      <button type="submit" class="btn-primary" style="border:none;cursor:pointer;">Verstuur</button>
      <p class="form-success" aria-live="polite"></p>
      <p style="font-size:14px;color:rgba(31,19,21,0.55);margin-top:10px;">Je gegevens staan veilig opgeslagen in de EU, en alleen jij en ik zien ze.</p>
    </form>
    <div style="text-align:center;margin-top:40px;color:rgba(31,19,21,0.5);font-size:14px;">
      Studio Crave &middot; We create cravings
    </div>
  </div>
</section>
"""
    page(
        "/contact/",
        "Contact | Studio Crave — Branding Studio Breda",
        "Klaar om op te vallen? Stuur Jasmijn je vraag, idee of shoot, of plan direct een kennismaking met Studio Crave.",
        "Klaar om op te vallen?",
        body,
        trail=[("Home", "/"), ("Contact", "/contact/")],
        extra_jsonld=[org_jsonld()],
    )


# ---------------------------------------------------------------------------
# PLAN KENNISMAKING
# ---------------------------------------------------------------------------
def build_plan_kennismaking():
    body = f"""
<section class="section-light">
  <div class="container" style="text-align:center;max-width:680px;margin:0 auto;">
    <span class="section-label">Plan kennismaking</span>
    <h1 class="section-title section-title-dark">Eerst proeven. Dan kiezen.</h1>
    <p style="font-size:17px;color:rgba(31,19,21,0.65);">In een kennismaking van 20 minuten kijken we samen waar je merk nu staat en welk menu bij je past. Gratis en vrijblijvend.</p>
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Wat je krijgt</span>
    <ul class="recognition-list" style="margin-top:16px;">
      <li>Een eerlijke eerste blik op je merk, je beeld en je boodschap</li>
      <li>Helderheid over welke gang je nu het hardst nodig hebt</li>
      <li>Een advies op maat: het hele menu, een losse gang, of eerst een Brand Audit</li>
    </ul>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Zo verloopt het daarna</span>
    <ol style="margin-top:16px;padding-left:20px;display:flex;flex-direction:column;gap:14px;color:rgba(31,19,21,0.75);">
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Kennismaken.</strong> We bespreken waar je staat en welk menu bij je past.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Aan tafel.</strong> Na je boeking krijg je een welkomstmail. Je kiest zelf je wachtwoord, en je portaal staat open.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Proeven.</strong> Je doet een korte quiz (welk gerecht ben jij?) en de onboarding over jou en je business. Hoe meer je vertelt, hoe persoonlijker alles wordt.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Gang voor gang.</strong> Je menu gaat open. Per gang zie je wat ik doe, wat jij ermee kunt en wat je aanlevert. Je geeft akkoord of feedback, en dan pas gaat de volgende gang open.</li>
      <li><strong style="font-family:var(--font-heading);color:var(--burgundy);">Je Signature Dish.</strong> Na de laatste gang serveer ik je hele merk op &eacute;&eacute;n bord.</li>
    </ol>
  </div>
</section>

<section class="section-dark">
  <div class="container" style="max-width:720px;margin:0 auto;">
    <span class="section-label">Korte intake</span>
    <ul class="recognition-list" style="margin-top:16px;">
      <li>Wie ben je en wat doe je?</li>
      <li>Waar staat je merk nu?</li>
      <li>Wat wil je dat mensen voelen als ze jouw merk zien?</li>
      <li>Waar loop je tegenaan?</li>
    </ul>
  </div>
</section>

<section class="section-light">
  <div class="container" style="max-width:720px;margin:0 auto;text-align:center;">
    <span class="section-label">Agenda</span>
    <p style="color:rgba(31,19,21,0.5);font-size:15px;">[Hier komt de agenda-embed, bijvoorbeeld Calendly]</p>
  </div>
</section>

<section class="cta-section">
  <div class="cta-content">
    <h2>Je tafel staat klaar.<br>Schuif aan.</h2>
    <div class="hero-actions">
      <a href="/contact/" class="btn-primary">Plan een kennismaking</a>
      <a href="/#quiz" class="btn-outline-light">Doe eerst de quiz: welk gerecht ben jij?</a>
    </div>
  </div>
</section>

<section class="section-light" id="faq">
  <div class="container" style="max-width:880px;">
    <span class="section-label" style="text-align:left;">Veelgestelde vragen</span>
    <h2 class="section-title section-title-dark" style="text-align:left;margin-bottom:32px;">Nog vragen?</h2>
    {faq_html()}
  </div>
</section>
"""
    page(
        "/plan-kennismaking/",
        "Plan een Kennismaking | Studio Crave",
        "Plan een gratis kennismaking van 20 minuten met Studio Crave. We kijken samen waar je merk nu staat en welk menu bij je past.",
        "Eerst proeven. Dan kiezen.",
        body,
        trail=[("Home", "/"), ("Plan kennismaking", "/plan-kennismaking/")],
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
    build_seven_courses()
    build_shoots_designs()
    build_portfolio_index()
    build_portfolio_cases()
    build_about()
    build_contact()
    build_plan_kennismaking()

    all_paths = [
        "/", "/7-course-branding-experience/", "/shoots-designs/", "/portfolio/",
    ] + [f"/portfolio/{p['slug']}/" for p in PORTFOLIO] + ["/about/", "/contact/", "/plan-kennismaking/"]
    build_robots_and_sitemap(all_paths)
    print(f"Generated {len(all_paths)} pages + robots.txt + sitemap.xml")


if __name__ == "__main__":
    main()
