import json, html
cfg = json.load(open('data/config.json'))
inv = json.load(open('data/inventory.json'))
stores = cfg['stores']
games = cfg['games']
socials = cfg.get('socials', [])

def head(title, desc, root):
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="https://waterenergytcg.com/"><meta name="theme-color" content="#0b1f3a">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/style.css">
</head><body>'''

def nav(root):
    links = ''.join(f'<a href="{root}stores/{s["slug"]}.html">{s["name"]}</a>' for s in stores)
    return f'''<header class="site-header"><div class="wrap bar">
<a class="brand" href="{root}index.html"><svg class="logo" viewBox="0 0 32 32" aria-hidden="true"><use href="{root}assets/favicon.svg#d"/></svg><span>Water Energy <b>TCG</b></span></a>
<button class="menu-btn" aria-label="Menu" aria-expanded="false">☰</button>
<nav class="nav" id="nav"><a href="{root}index.html#stores">Stores</a><a href="{root}index.html#follow">Follow</a><a href="{root}index.html#featured">Featured</a><a href="{root}index.html#games">Games</a><a href="{root}index.html#about">About</a><a href="{root}index.html#contact">Contact</a></nav>
</div></header>'''

def footer(root):
    sl = ''.join(f'<a href="{root}stores/{s["slug"]}.html">{s["name"]}</a>' for s in stores)
    sl += ''.join(f'<a {ext(x)}>{x["name"]}</a>' for x in socials)
    return f'''<footer class="site-footer"><div class="wrap foot">
<div><strong>Water Energy TCG</strong><p>Collect, Trade, Energize!</p></div>
<div class="flinks">{sl}<a href="{root}index.html#contact">Contact</a></div>
<p class="fine">© <span id="yr">2026</span> Water Energy TCG. Pokémon, Yu-Gi-Oh!, One Piece, Gundam and Dragon Ball are trademarks of their respective owners; Water Energy TCG is not affiliated with them.</p>
</div></footer><script src="{root}assets/main.js"></script></body></html>'''

def ext(s): return f'href="{s["url"]}" target="_blank" rel="noopener noreferrer"'

# ---- index
store_cards = ''.join(f'''<a class="card store" style="--c:{s["color"]}" {ext(s)}>
<span class="ico">{s["icon"]}</span><h3>{s["name"]}</h3><p>{s["tagline"]}</p><span class="go">Shop now ↗</span></a>''' for s in stores)
feat = ''.join(f'''<article class="card item"><div class="thumb" style="--c:{i["color"]}"><span>{i["emoji"]}</span></div>
<div class="body"><span class="tag">{i["game"]}</span><h3>{i["title"]}</h3><p>{i["note"]}</p>
<a class="link" href="{i["url"]}" target="_blank" rel="noopener noreferrer">View on {i["store"]} ↗</a></div></article>''' for i in inv['items'])
social_cards = ''.join(f'''<a class="card store" style="--c:{x["color"]}" {ext(x)}><span class="ico">{x["icon"]}</span><h3>{x["name"]}</h3><p>{x["blurb"]}</p><span class="go">Follow ↗</span></a>''' for x in socials)
game_cards = ''.join(f'<div class="card game {"primary" if g["primary"] else ""}"><h3>{g["name"]}</h3><p>{g["blurb"]}</p></div>' for g in games)

index = head('Water Energy TCG | Pokémon TCG, Gundam, Yu-Gi-Oh!, One Piece & Dragon Ball Fusion World',
 'Water Energy TCG is your hub for Pokémon TCG and more. Shop on TCGplayer, eBay, Shopify and TikTok Shop.', '') + nav('') + f'''
<main>
<section class="hero"><div class="wrap hero-in">
<p class="eyebrow">Pokémon TCG · Gundam · Yu-Gi-Oh! · One Piece · Dragon Ball Fusion World</p>
<h1>Collect. Trade. <span class="grad">Energize.</span></h1>
<p class="lead">Water Energy TCG is a Pokémon-focused trading card shop. Pick your favorite place to buy: we're on four marketplaces with the same trusted inventory.</p>
<div class="cta"><a class="btn primary" href="#stores">Choose a store</a><a class="btn ghost" href="#contact">Contact us</a></div>
<div class="drops" aria-hidden="true"><i></i><i></i><i></i></div>
</div></section>

<section id="stores" class="sec"><div class="wrap">
<h2>Shop Our Stores</h2><p class="sub">Four ways to buy. Same shop, same care.</p>
<div class="grid four">{store_cards}</div>
<p class="more">Want details on each? Visit a store page: {', '.join(f'<a href="stores/{s["slug"]}.html">{s["name"]}</a>' for s in stores)}.</p>
</div></section>

<section id="follow" class="sec alt"><div class="wrap">
<h2>Watch &amp; Follow</h2><p class="sub">Catch live shows, openings and new drops.</p>
<div class="grid four">{social_cards}</div>
</div></section>

<section id="featured" class="sec"><div class="wrap">
<h2>Featured &amp; New Inventory</h2><p class="sub">A peek at what's on the shelf. Edit <code>data/inventory.json</code> and run <code>python3 build.py</code> to update.</p>
<div class="grid three">{feat}</div>
</div></section>

<section id="games" class="sec"><div class="wrap">
<h2>What We Carry</h2><p class="sub">Pokémon is our home turf, with plenty more for every collector.</p>
<div class="grid games">{game_cards}</div>
</div></section>

<section id="about" class="sec alt"><div class="wrap about">
<div><h2>About Water Energy TCG</h2>
<p>Water Energy TCG was built by collectors, for collectors. Our focus is the <strong>Pokémon Trading Card Game</strong>: singles, sealed product, and chase cards including illustration rares and special illustration rares.</p>
<p>We also stock <strong>Gundam Card Game</strong>, <strong>Yu-Gi-Oh!</strong>, <strong>One Piece Card Game</strong> and <strong>Dragon Ball Super Card Game Fusion World</strong>, so you can fill a whole collection in one place.</p>
<p>Whether you shop on TCGplayer, eBay, our Shopify store or TikTok Shop, you get the same commitment: accurate listings, careful packing, and friendly service.</p></div>
<ul class="pillars"><li><b>Accurate listings</b><span>Condition and edition described honestly.</span></li><li><b>Careful packing</b><span>Sleeved, top-loaded and protected.</span></li><li><b>Collector-first</b><span>Fair prices and real help.</span></li></ul>
</div></section>

<section id="contact" class="sec"><div class="wrap contact">
<div><h2>Drop Us a Line!</h2><p>Questions about an order, a card, or a bulk buy or trade? Send a message and we'll get back to you.</p>
<p class="mini">Prefer a marketplace message? Reach us through any of our stores above.</p></div>
<form id="contact-form" data-email="{cfg["contact_email"]}" novalidate>
<label>Name<input name="name" required autocomplete="name"></label>
<label>Email<input name="email" type="email" required autocomplete="email"></label>
<label>Message<textarea name="message" rows="5" required></textarea></label>
<button class="btn primary" type="submit">Send message</button>
<p class="note" id="form-note" role="status"></p>
</form></div></section>
</main>''' + footer('')
open('index.html','w').write(index)

# ---- store pages
for s in stores:
    others = ''.join(f'<a class="chip" href="{o["slug"]}.html">{o["name"]}</a>' for o in stores if o is not s)
    perks = ''.join(f'<li>{p}</li>' for p in s['perks'])
    page = head(f'{s["name"]} | Water Energy TCG', s['tagline'], '../') + nav('../') + f'''
<main><section class="hero small" style="--c:{s["color"]}"><div class="wrap hero-in">
<a class="crumb" href="../index.html#stores">← All stores</a>
<span class="ico big">{s["icon"]}</span><h1>Water Energy TCG on {s["name"]}</h1>
<p class="lead">{s["desc"]}</p>
<div class="cta"><a class="btn primary" {ext(s)}>Visit our {s["name"]} store ↗</a></div></div></section>
<section class="sec"><div class="wrap two">
<div><h2>Why shop here</h2><ul class="checks">{perks}</ul></div>
<div class="card"><h3>Good to know</h3><p>{s["note"]}</p><p>Questions? <a href="../index.html#contact">Contact us</a>.</p></div>
</div></section>
<section class="sec alt"><div class="wrap"><h2>Other ways to shop</h2><div class="chips">{others}</div></div></section></main>''' + footer('../')
    open(f'stores/{s["slug"]}.html','w').write(page)
print('built')
