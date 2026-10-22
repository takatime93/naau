"""Shared building blocks for the naʻau concept site (v3).

Artboards: print and social pieces are drawn on a 1000-unit-wide board. Write sizes
as [[n]] and they become container units, so a piece keeps its proportions at any size.
Stills: SVG still-life scenes stand in for photography, lit and propped per direction.
"""
import os, re
import ink

SITE = None

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Shippori+Mincho+B1:wght@500;700'
         '&family=Zen+Old+Mincho:wght@400;600;700&family=Zen+Kaku+Gothic+New:wght@300;400;500;700&family=Klee+One:wght@400;600&family=Yomogi'
         '&family=Inter:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

FIT = ('<script>function fit(){document.querySelectorAll("[data-fit]").forEach(function(p){var f=p.querySelector("iframe");'
       'f.style.transform="scale("+(p.clientWidth/+p.dataset.fit)+")";});}addEventListener("resize",fit);addEventListener("load",fit);fit();</script>')

D = {
 "current": dict(key="current", cls="d-current", nav="Current identity", name="Current identity", logo="current-lockup", small="current-naau", ink="1e1e1e",
                 glass=["#8E4E1F", "#6F3B17", "#A8692A"], cap="#1E1E1E"),
 "lenora": dict(key="lenora", cls="d-lenora", nav="Concept A · Lenora", name="Concept A · Lenora", logo="lenora", small="lenora", ink="2b2926",
                glass=["#9C5B22", "#7A4519", "#B57A3C"], cap="#141312"),
 "ogg": dict(key="ogg", cls="d-ogg", nav="Concept B · Ogg", name="Concept B · Ogg", logo="ogg", small="ogg", ink="3a3631",
             glass=["#A8692A", "#8A5220", "#C08040"], cap="#3A3631"),
}
ORDER = ["current", "lenora", "ogg"]
LOGO_RATIO = {"current-lockup": 1047 / 402, "current-naau": 613 / 162, "lenora": 1600 / 459, "ogg": 1230 / 440}

def U(html):
    return re.sub(r"\[\[(-?\d+(?:\.\d+)?)\]\]", lambda m: f"{float(m.group(1)) / 10:g}cqw", html)

def L(d, color, width, small=False, style=""):
    name = d["small"] if small else d["logo"]
    return f'<img src="assets/logos/{name}-{color}.png" alt="naʻau" style="width:{width}; {style}">'

# ------------------------------------------------------------------ page chrome
def nav(active):
    items = [("index", "Overview")] + [(k, D[k]["nav"]) for k in ORDER] + [("collab", "naʻau × Ivycoast")]
    lis = "".join(f'<li><a href="{f}.html"' + (' aria-current="page"' if f == active else '') + f'>{t}</a></li>' for f, t in items)
    return (f'<nav class="sitenav" aria-label="Concept sections"><div class="wrap"><a class="brand" href="index.html">naʻau <span>brand concepts</span></a>'
            f'<ul>{lis}</ul></div></nav>')

def page(fname, title, cls, body, script="", extra_head=""):
    html = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title>{FONTS}<link rel="stylesheet" href="assets/css/site.css">{extra_head}</head>'
            f'<body class="{cls}">{ink.DEFS}{body}{script}</body></html>\n')
    open(os.path.join(SITE, fname), "w").write(U(html))

def sec(num, title, desc, content, cls="", sid=""):
    idattr = f' id="{sid}"' if sid else ""
    return (f'<section class="sec {cls}"{idattr}><div class="wrap"><header class="sh"><span class="sh-n">{num}</span><h2>{title}</h2>'
            f'<p>{desc}</p></header>{content}</div></section>')

def pf(inner, title, spec="", ratio=None, plate=True, style="", pstyle=""):
    """A plate (asset on its backdrop) with a two-line caption."""
    ar = f"aspect-ratio:{ratio};" if ratio else ""
    body = f'<div class="plate" style="{ar}{pstyle}">{inner}</div>' if plate else inner
    cap = f'<figcaption><b>{title}</b>' + (f'<span>{spec}</span>' if spec else '') + '</figcaption>'
    return f'<figure class="pf" style="{style}">{body}{cap}</figure>'

def ab(ratio_w, ratio_h, inner, width, style="", cls="sheet"):
    """An artboard: fixed proportions, contents in [[units]] of a 1000-wide board."""
    return f'<div class="ab {cls}" style="width:{width}; aspect-ratio:{ratio_w}/{ratio_h}; {style}">{inner}</div>'

def fitw(plate, board, hfrac):
    """Width (%) for a board of ratio `board` (w/h) filling hfrac of a plate's height (plate = w/h)."""
    return f"{hfrac / plate * board * 100:.2f}%"

def chips(items, note=""):
    total = sum(w for *_, w in items)
    dark = lambda h: sum(int(h[i:i + 2], 16) for i in (1, 3, 5)) < 3 * 140
    bars = "".join(f'<div class="sw" style="flex:{w}; background:{h}; color:{"#FFFFFF" if dark(h) else "#1E1E1E"}"><b>{n}</b><span>{h}</span><em>{role}</em></div>'
                   for n, h, role, w in items)
    return f'<div class="swatches">{bars}</div>' + (f'<p class="swnote">{note}</p>' if note else "")

def previews(d):
    k = d["key"]
    return ('<div class="pv">'
            f'<figure class="pf pv-desk"><div class="browser"><div class="browser-bar"><i></i><i></i><i></i><span>［website］</span></div>'
            f'<div class="browser-view" data-fit="1440"><iframe src="{k}-home.html" title="Home page preview" loading="lazy" tabindex="-1" style="width:1440px; height:2000px"></iframe></div></div>'
            f'<figcaption><b>Home page</b><span>Responsive and working. <a href="{k}-home.html">Open full size →</a></span></figcaption></figure>'
            f'<figure class="pf pv-phone"><div class="phone"><div class="phone-view" data-fit="390"><iframe src="{k}-product.html" title="Product page preview" loading="lazy" tabindex="-1" style="width:390px; height:1690px"></iframe></div></div>'
            f'<figcaption><b>Product page, on a phone</b><span>Price with tax, クール便 cost and date beside the cart. <a href="{k}-product.html">Open →</a></span></figcaption></figure>'
            '</div>')

ICHI = [("名称", "清涼飲料水（発酵茶飲料）"), ("原材料名", "［　］"), ("内容量", "330 ml"), ("賞味期限", "枠内に記載"),
        ("保存方法", "要冷蔵（10℃以下）"), ("製造者", "［事業者名］<br>愛知県名古屋市［　］")]
HANDLING = "開栓注意：振らないでください。沈殿物は原料由来のものです。"

def ichi_rows(gap="[[10]]"):
    return "".join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in ICHI)

def legal_links():
    return ''.join(f'<a href="#">{t}</a>' for t in ("ショップ", "わたしたち", "ワークショップ", "特定商取引法に基づく表記", "配送・返品について", "プライバシーポリシー", "LINE · Instagram"))

def commerce(style):
    return f'<div class="jp commerce" style="{style}">クール便（冷蔵）· 送料 ¥［　］<br>最短お届け ［月日］· 日時指定できます</div>'

def accordions(border):
    return "".join(f'<details style="border-top:1px solid {border}"><summary class="jp">{t}</summary><p class="jp">{c}</p></details>'
                   for t, c in [("原材料・アレルゲン", "［原材料名］／アレルゲン：［　］"),
                                ("保存方法・賞味期限", "要冷蔵（10℃以下）。振らずに静かに開けてください。沈殿物は原料由来のものです。"),
                                ("配送・返品", "クール便（冷蔵）でお届けします。送料 ¥［　］。日時指定ができます。生ものにつき、お客様都合の返品はお受けできません。"),
                                ("作り手について", "kimy — 看護師として働きながら、名古屋でコンブチャを仕込んでいます。")])

# ------------------------------------------------------------------ still life (photography direction, drawn flat)
_uid = [0]
# a 330 ml craft kombucha bottle: short neck, round shoulders (0..100 × 42..300)
BOTTLE = "M12 300 H88 Q100 300 100 288 V152 C100 120 72 110 67 90 V68 H33 V90 C28 110 0 120 0 152 V288 Q0 300 12 300 Z"
SCENES = {
 "current": dict(wall="#F6F5F1", table="#EAE8E2", light=None, shade="#DCD9D1", cap_ink="#9A968F"),
 "lenora":  dict(wall="#201F1D", table="#2D2A27", light="#272523", shade="#1A1917", cap_ink="#8C867C"),
 "ogg":     dict(wall="#F1E9DA", table="#D9C3A0", light="#F8F1E4", shade="#C4AB84", cap_ink="#8C7C64"),
 "collab":  dict(wall="#F4DDCC", table="#EADBCB", light=None, shade="#DCC8B5", cap_ink="#9B7F6C"),
}

def _shade(h, f):
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    if f < 1:
        r, g, b = (int(c * f) for c in (r, g, b))
    else:
        r, g, b = (int(c + (255 - c) * (f - 1)) for c in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"

def _shadow(x, w, by, h, s):
    """A hard, flat cast shadow, like cut paper."""
    L, t = h * .7, h * .1
    return f'<polygon points="{x + .1 * w:.0f},{by} {x + w:.0f},{by} {x + w + L:.0f},{by - t:.0f} {x + .1 * w + L:.0f},{by - t:.0f}" fill="{s["shade"]}"/>'

def _label(dk, fl, no):
    if dk == "current":
        return (f'<circle cx="50" cy="222" r="33" fill="#FFFFFF"/><image href="assets/logos/current-naau-1e1e1e.png" x="25" y="207" width="50" height="13.2"/>'
                f'<text x="50" y="236" font-family="Zen Kaku Gothic New" font-size="4.6" letter-spacing="1" text-anchor="middle" fill="#1E1E1E">{fl}</text>')
    if dk == "lenora":
        return (f'<rect x="0" y="168" width="100" height="90" fill="#EFEBE2"/><rect x="5" y="173" width="90" height="80" fill="none" stroke="#2B2926" stroke-width=".6"/>'
                f'<rect x="7.5" y="175.5" width="85" height="75" fill="none" stroke="#2B2926" stroke-width=".35"/>'
                f'<image href="assets/logos/lenora-2b2926.png" x="23" y="186" width="54" height="15.5"/>'
                f'<text x="50" y="213" font-family="EB Garamond" font-style="italic" font-size="6" text-anchor="middle" fill="#2B2926">kombucha</text>'
                f'<text x="14" y="242" font-family="IBM Plex Mono" font-size="3.8" letter-spacing=".6" fill="#2B2926">NO.{no} · ［お名前］様</text>'
                f'<rect x="80" y="234" width="7" height="10" rx="3.5" fill="#9B3A25"/>')
    if dk == "ogg":
        return (f'<rect x="0" y="176" width="100" height="62" fill="#FAF7F1"/>'
                f'<text x="11" y="200" font-family="Zen Old Mincho" font-size="13" text-anchor="middle" fill="#3A3631">間</text>'
                f'<image href="assets/logos/ogg-3a3631.png" x="23" y="190" width="50" height="17.9"/>'
                f'<text x="48" y="222" font-family="Klee One" font-size="5.2" text-anchor="middle" fill="#3A3631">{fl}</text>'
                f'<text x="91" y="187" font-family="Klee One" font-size="4.4" fill="#3A3631" style="writing-mode:vertical-rl">10/22 kimy</text>')
    return ""

def _bottle(n, i, x, by, sc, glass, dk, cap, fl="［フレーバー］", no="027", s=None):
    w, h = 100 * sc, 300 * sc
    body = (f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})"><path d="{BOTTLE}" fill="{glass}"/>'
            f'<path d="M14 160 C14 140 24 128 34 122 V128 C26 134 20 144 20 160 V284 H14 Z" fill="{_shade(glass, 1.14)}"/>'
            f'<rect x="30" y="42" width="40" height="24" rx="2.5" fill="{cap}"/><rect x="32" y="66" width="36" height="3" fill="{_shade(cap, .75)}"/>'
            f'{_label(dk, fl, no)}</g>')
    return "", _shadow(x - w / 2, w, by, h * .86, s) + body

def _glass(n, x, by, sc, s, liquid="#C9883A"):
    w, h = 80 * sc, 110 * sc
    return (_shadow(x - w / 2, w, by, h * .8, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})">'
            f'<path d="M4 0 H76 L70 105 Q69.4 110 64 110 H16 Q10.6 110 10 105 Z" fill="#FFFFFF" opacity=".45"/>'
            f'<path d="M7.6 40 H72.4 L70 105 Q69.4 110 64 110 H16 Q10.6 110 10 105 Z" fill="{liquid}"/>'
            f'<rect x="7.6" y="38" width="64.8" height="4" fill="{_shade(liquid, 1.3)}"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="{_shade(liquid, 1.35)}"/>' for cx, cy in ((30, 70), (46, 84), (52, 58), (36, 92))) + '</g>')

def _yunomi(n, x, by, sc, s):
    w, h = 104 * sc, 74 * sc
    return (_shadow(x - w / 2, w, by, h, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})">'
            f'<path d="M3 3 H101 Q100 46 88 64 Q84 70 74 70 H30 Q20 70 16 64 Q4 46 3 3 Z" fill="#D8C9AC"/>'
            f'<path d="M3 3 H101 L100.6 13 H3.4 Z" fill="#7D6849"/><rect x="34" y="70" width="36" height="4" fill="#A8977A"/></g>')

def _jar(n, x, by, sc, s, cloth="#ECE4D3"):
    w, h = 190 * sc, 330 * sc
    return (_shadow(x - w / 2, w, by, h, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})">'
            f'<path d="M30 40 H160 Q160 66 176 74 Q190 82 190 104 V300 Q190 330 160 330 H30 Q0 330 0 300 V104 Q0 82 14 74 Q30 66 30 40 Z" fill="#FFFFFF" opacity=".42"/>'
            f'<path d="M8 128 H182 V300 Q182 322 160 322 H30 Q8 322 8 300 Z" fill="#B87A35"/><rect x="8" y="118" width="174" height="14" fill="#E6D6B4"/>'
            f'<path d="M14 18 Q95 6 176 18 L178 58 Q95 50 12 58 Z" fill="{cloth}"/><path d="M24 46 Q95 38 166 46" stroke="#8B6B45" stroke-width="3" fill="none"/></g>')

def _soap(n, x, by, sc, s):
    w, h = 210 * sc, 103 * sc
    return (_shadow(x - w / 2, w, by, h, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})"><rect width="210" height="103" fill="#F4D9C6"/>'
            f'<image href="assets/collab/kombar-artwork.svg" x="34" y="9" width="85" height="85"/>'
            f'<text x="20" y="96" font-family="Inter" font-weight="700" font-size="15" fill="#1E1E1E" transform="rotate(-90 20 96)">KOM’BAR</text></g>')

def _card(n, x, by, w, h, s, inner_svg, rot=-4, fill="#FBF8F2"):
    return (f'<g transform="translate({x},{by}) rotate({rot})"><rect x="7" y="7" width="{w}" height="{h}" fill="{s["shade"]}"/>'
            f'<rect width="{w}" height="{h}" fill="{fill}"/>{inner_svg}</g>')

def still(dk, kind="range", ratio="4/3", cap="", flavours=("［フレーバー］", "［フレーバー］", "［限定］"), label=None, pos="50% 50%", zoom=None, cy=None, note=False, tone=None):
    """A flat, cut-paper still life that stands in for photography. dk picks the light and props; label picks the bottle label."""
    _uid[0] += 1; n = _uid[0]
    s = SCENES[dk]
    lab = label or dk
    glasses = D[lab]["glass"] if lab in D else ["#9C5B22", "#7A4519", "#B57A3C"]
    capc = D[lab]["cap"] if lab in D else "#1E1E1E"
    W, H, T = 1600, 1200, 742
    bg = f'<rect width="{W}" height="{T}" fill="{s["wall"]}"/><rect y="{T}" width="{W}" height="{H - T}" fill="{s["table"]}"/>'
    if dk == "lenora":
        bg += f'<polygon points="520,0 760,0 1000,{T} 640,{T}" fill="{s["light"]}"/><polygon points="640,{T} 1000,{T} 1180,{H} 700,{H}" fill="{_shade(s["table"], 1.06)}"/>'
    elif dk == "ogg":
        bg += f'<g transform="skewX(-14)">' + "".join(f'<rect x="{x}" y="{y}" width="112" height="128" fill="{s["light"]}"/>' for x in range(640, 1200, 124) for y in range(150, 700, 140)) + '</g>'
    objs = []
    def add_bottle(i, x, by, sc, fl="［フレーバー］", no="027", g=None):
        objs.append(_bottle(n, i, x, by, sc, g or glasses[i % 3], lab if lab in D else "plain", capc, fl, no, s)[1])
    if kind == "range":
        for i, (x, fl, no) in enumerate(zip((622, 800, 978), flavours, ("027", "028", "029"))):
            add_bottle(i, x, 846, 1.32, fl, no)
    elif kind == "pour":
        add_bottle(0, 720, 840, 1.34)
        objs.append(_glass(n, 905, 872, 1.55, s))
    elif kind == "single":
        if dk == "lenora":
            card = ('<rect x="10" y="10" width="160" height="110" fill="none" stroke="#2B2926" stroke-width="1.2"/>'
                    '<text x="22" y="40" font-family="IBM Plex Mono" font-size="10" letter-spacing="2" fill="#6E6860">FOR</text>'
                    '<text x="22" y="78" font-family="Zen Old Mincho" font-size="20" fill="#2B2926">［お名前］様</text>'
                    '<text x="22" y="106" font-family="IBM Plex Mono" font-size="10" letter-spacing="1" fill="#2B2926">NO.027 · 14 DAYS</text>'
                    '<rect x="142" y="86" width="14" height="20" rx="7" fill="#9B3A25"/>')
            objs.append(_card(n, 880, 860, 180, 130, s, card, rot=-4, fill="#EFEBE2"))
        add_bottle(0, 760, 870, 1.55)
        if dk == "ogg":
            objs.append(_yunomi(n, 965, 892, 1.5, s))
        if dk == "ogg" and note:
            note_svg = '<text x="22" y="52" font-family="Klee One" font-size="21" fill="#3A3631">今日もゆっくり。</text><text x="22" y="90" font-family="Klee One" font-size="17" fill="#3A3631">— kimy</text>'
            objs.insert(0, _card(n, 540, 880, 230, 120, s, note_svg, rot=-5))
        if dk == "current":
            objs.append(_glass(n, 930, 884, 1.4, s))
    elif kind == "jar":
        objs.append(_jar(n, 740, 870, 1.25, s, cloth="#EFEBE2" if dk == "lenora" else "#ECE4D3"))
        objs.append(_glass(n, 990, 890, 1.35, s, liquid="#C27F35"))
    elif kind == "gift":
        add_bottle(0, 700, 850, 1.3)
        objs.append(_soap(n, 930, 880, 1.45, s))
    elif kind == "glass":
        objs.append(_glass(n, 800, 880, 2.3, s))
    z = zoom or {"range": 1.75, "pour": 1.8, "single": 1.7, "jar": 1.6, "glass": 2.0, "gift": 1.7}.get(kind, 1.6)
    c = cy or {"range": 680, "pour": 690, "single": 690, "jar": 690, "glass": 760, "gift": 700}.get(kind, 700)
    rw, rh = (float(v) for v in ratio.split("/"))
    r = rw / rh
    need_h, need_w = {"range": (560, 640), "pour": (520, 520), "single": (640, 660), "jar": (560, 540), "glass": (440, 360), "gift": (560, 620)}.get(kind, (560, 560))
    z = min(z, W / (max(r, W / H) * need_h), H * min(r, W / H) / need_w)
    vw, vh = W / z, H / z
    svg = (f'<svg viewBox="{800 - vw / 2:.0f} {c - vh / 2:.0f} {vw:.0f} {vh:.0f}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Photography direction: {cap or kind}">'
           f'{bg}{"".join(objs)}</svg>')
    capt = f'<span class="still-cap" style="color:{s["cap_ink"]}">Photo direction · {cap}</span>' if cap else ""
    return f'<div class="still" style="aspect-ratio:{ratio}; --pos:{pos}">{svg}{capt}</div>'

def ph(dk, kind, left, top, width, ratio="1/1", **kw):
    """A still placed inside an artboard."""
    return f'<div style="left:{left}; top:{top}; width:{width}">{still(dk, kind, ratio, **kw)}</div>'
