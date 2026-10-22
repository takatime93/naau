"""Shared building blocks for the naʻau concept site (v3).

Artboards: print and social pieces are drawn on a 1000-unit-wide board. Write sizes
as [[n]] and they become container units, so a piece keeps its proportions at any size.
Stills: SVG still-life scenes stand in for photography, lit and propped per direction.
"""
import os, re

SITE = None

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Shippori+Mincho+B1:wght@500;700'
         '&family=Zen+Old+Mincho:wght@400;600;700&family=Zen+Kaku+Gothic+New:wght@300;400;500;700&family=Klee+One:wght@400;600'
         '&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">')

FIT = ('<script>function fit(){document.querySelectorAll("[data-fit]").forEach(function(p){var f=p.querySelector("iframe");'
       'f.style.transform="scale("+(p.clientWidth/+p.dataset.fit)+")";});}addEventListener("resize",fit);addEventListener("load",fit);fit();</script>')

D = {
 "current": dict(key="current", cls="d-current", nav="naʻau today", name="Shiro", kanji="白", logo="current-lockup", small="current-naau", ink="1e1e1e",
                 glass=["#8E4E1F", "#6F3B17", "#A8692A"], cap="#1E1E1E"),
 "lenora": dict(key="lenora", cls="d-lenora", nav="Lenora", name="Ippon", kanji="一本", logo="lenora", small="lenora", ink="2b2926",
                glass=["#9C5B22", "#7A4519", "#B57A3C"], cap="#141312"),
 "ogg": dict(key="ogg", cls="d-ogg", nav="Ogg", name="Ma", kanji="間", logo="ogg", small="ogg", ink="3a3631",
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
    items = [("index", "Overview")] + [(k, f'{D[k]["kanji"]} {D[k]["name"]}') for k in ORDER] + [("collab", "naʻau × Ivycoast")]
    lis = "".join(f'<li><a href="{f}.html"' + (' aria-current="page"' if f == active else '') + f'>{t}</a></li>' for f, t in items)
    return (f'<nav class="sitenav" aria-label="Concept sections"><div class="wrap"><a class="brand" href="index.html">naʻau <span>brand concepts</span></a>'
            f'<ul>{lis}</ul></div></nav>')

def page(fname, title, cls, body, script="", extra_head=""):
    html = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title>{FONTS}<link rel="stylesheet" href="assets/css/site.css">{extra_head}</head>'
            f'<body class="{cls}">{body}{script}</body></html>\n')
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

# ------------------------------------------------------------------ still life (photography direction)
_uid = [0]
BOTTLE = "M9 300 H91 Q100 300 100 291 V122 C100 94 74 82 68 62 V26 H32 V62 C26 82 0 94 0 122 V291 Q0 300 9 300 Z"
SCENES = {
 "current": dict(wall=("#F8F7F4", "#EDEBE6"), table=("#FCFBF9", "#ECEAE5"), shadow=.13, contact=.30, rim="#FFFFFF", glass_line="#FFFFFF", cap_ink="#9A968F"),
 "lenora": dict(wall=("#1B1A18", "#242220"), table=("#2E2B28", "#1A1917"), shadow=.45, contact=.6, rim="#F2E6D0", glass_line="#E9DFCB", cap_ink="#8C867C"),
 "ogg": dict(wall=("#F2EBDD", "#E7DDC9"), table=("#DCC7A3", "#C9AF86"), shadow=.17, contact=.32, rim="#FFF8EA", glass_line="#FFFFFF", cap_ink="#8C7C64"),
 "collab": dict(wall=("#F5DECD", "#EFD2BE"), table=("#F2E7DB", "#E3D3C2"), shadow=.15, contact=.3, rim="#FFFFFF", glass_line="#FFFFFF", cap_ink="#9B7F6C"),
}

def _shade(h, f):
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    if f < 1:
        r, g, b = (int(c * f) for c in (r, g, b))
    else:
        r, g, b = (int(c + (255 - c) * (f - 1)) for c in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"

def _shadow(n, x, w, by, h, s):
    L, t = h * 0.85, h * 0.13
    pts = f"{x + .12 * w:.0f},{by} {x + w:.0f},{by} {x + w + L:.0f},{by - t:.0f} {x + .12 * w + L * .92:.0f},{by - t - 6:.0f}"
    return (f'<polygon points="{pts}" fill="#000" opacity="{s["shadow"]}" filter="url(#bl{n})"/>'
            f'<ellipse cx="{x + w / 2:.0f}" cy="{by - 2}" rx="{w * .56:.0f}" ry="7" fill="#000" opacity="{s["contact"]}" filter="url(#bs{n})"/>')

def _label(dk, fl, no):
    if dk == "current":
        return (f'<circle cx="50" cy="214" r="33" fill="#FFFFFF"/><image href="assets/logos/current-naau-1e1e1e.png" x="25" y="199" width="50" height="13.2"/>'
                f'<text x="50" y="228" font-family="Zen Kaku Gothic New" font-size="4.6" letter-spacing="1" text-anchor="middle" fill="#1E1E1E">{fl}</text>')
    if dk == "lenora":
        return (f'<rect x="32" y="36" width="36" height="13" fill="#141312"/><text x="50" y="45" font-family="EB Garamond" font-size="5.4" letter-spacing=".6" text-anchor="middle" fill="#EFEBE2">No.{no}</text>'
                f'<rect x="11" y="138" width="78" height="146" fill="#EFEBE2"/><rect x="15" y="142" width="70" height="138" fill="none" stroke="#2B2926" stroke-width=".7"/>'
                f'<rect x="17.5" y="144.5" width="65" height="133" fill="none" stroke="#2B2926" stroke-width=".45"/>'
                f'<image href="assets/logos/lenora-2b2926.png" x="23" y="164" width="54" height="15.5"/>'
                f'<text x="50" y="198" font-family="EB Garamond" font-style="italic" font-size="6.4" text-anchor="middle" fill="#2B2926">kombucha</text>'
                f'<text x="50" y="222" font-family="Zen Old Mincho" font-size="4.6" letter-spacing=".8" text-anchor="middle" fill="#2B2926">{fl}</text>'
                f'<line x1="30" y1="256" x2="70" y2="256" stroke="#2B2926" stroke-width=".5"/>'
                f'<text x="50" y="267" font-family="Zen Old Mincho" font-size="5" text-anchor="middle" fill="#2B2926">［お名前］様</text>')
    if dk == "ogg":
        return (f'<rect x="0" y="176" width="100" height="62" fill="#FAF7F1"/>'
                f'<text x="11" y="200" font-family="Zen Old Mincho" font-size="13" text-anchor="middle" fill="#3A3631">間</text>'
                f'<image href="assets/logos/ogg-3a3631.png" x="23" y="190" width="50" height="17.9"/>'
                f'<text x="48" y="222" font-family="Klee One" font-size="5.2" text-anchor="middle" fill="#3A3631">{fl}</text>'
                f'<text x="91" y="187" font-family="Klee One" font-size="4.4" fill="#3A3631" style="writing-mode:vertical-rl">10/22 kimy</text>')
    if dk == "plain":
        return ""
    return ""

def _bottle(n, i, x, by, sc, glass, dk, cap, fl="［フレーバー］", no="027", s=None):
    w, h = 100 * sc, 300 * sc
    gid = f"am{n}_{i}"
    grad = (f'<linearGradient id="{gid}" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{_shade(glass, .5)}"/><stop offset=".16" stop-color="{_shade(glass, .86)}"/>'
            f'<stop offset=".34" stop-color="{_shade(glass, 1.18)}"/><stop offset=".52" stop-color="{glass}"/><stop offset=".86" stop-color="{_shade(glass, .7)}"/><stop offset="1" stop-color="{_shade(glass, .42)}"/></linearGradient>')
    body = (f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})"><path d="{BOTTLE}" fill="url(#{gid})"/>'
            f'<path d="M15 130 C15 114 22 103 31 95 L31 99 C24 107 19 117 19 130 V280 Q19 285 17 285 Q15 285 15 280 Z" fill="#FFFFFF" opacity=".26"/>'
            f'<path d="M93 130 V284" stroke="{s["rim"]}" stroke-width="1.2" opacity=".22"/>'
            f'<rect x="29" y="0" width="42" height="24" rx="3" fill="{cap}"/><rect x="31" y="24" width="38" height="4" fill="{_shade(cap, .7) if cap != "#141312" else "#0E0D0C"}"/>'
            f'<rect x="31" y="2" width="6" height="20" fill="#FFFFFF" opacity=".08"/>'
            f'{_label(dk, fl, no)}</g>')
    return grad, _shadow(n, x - w / 2, w, by, h, s) + body

def _glass(n, x, by, sc, s, liquid="#C9883A"):
    w, h = 80 * sc, 110 * sc
    return (f'<ellipse cx="{x + w * .9:.0f}" cy="{by - 6}" rx="{w * .8:.0f}" ry="{10 * sc:.0f}" fill="{liquid}" opacity=".22" filter="url(#bl{n})"/>'
            + _shadow(n, x - w / 2, w, by, h * .8, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})">'
            f'<path d="M7.6 40 H72.4 L70 105 Q69.4 110 64 110 H16 Q10.6 110 10 105 Z" fill="{liquid}" opacity=".88"/>'
            f'<ellipse cx="40" cy="40" rx="32.4" ry="2.6" fill="{_shade(liquid, 1.35)}"/>'
            f'<path d="M4 0 H76 L70 105 Q69.4 110 64 110 H16 Q10.6 110 10 105 Z" fill="#FFFFFF" opacity=".10" stroke="{s["glass_line"]}" stroke-opacity=".7" stroke-width="1"/>'
            f'<path d="M10 6 L15 100" stroke="#FFFFFF" stroke-width="2.4" opacity=".35" stroke-linecap="round"/>'
            f'<circle cx="30" cy="70" r="1.1" fill="#FFF" opacity=".5"/><circle cx="46" cy="84" r=".9" fill="#FFF" opacity=".5"/><circle cx="52" cy="60" r="1.2" fill="#FFF" opacity=".45"/></g>')

def _yunomi(n, x, by, sc, s):
    w, h = 104 * sc, 74 * sc
    return (_shadow(n, x - w / 2, w, by, h, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})"><defs><linearGradient id="yu{n}" x1="0" x2="1"><stop offset="0" stop-color="#A89676"/><stop offset=".34" stop-color="#E4D7BE"/><stop offset=".7" stop-color="#C9B794"/><stop offset="1" stop-color="#8F7C5D"/></linearGradient></defs>'
            f'<path d="M3 3 Q52 -1 101 3 Q100 46 88 64 Q84 70 74 70 H30 Q20 70 16 64 Q4 46 3 3 Z" fill="url(#yu{n})"/>'
            f'<path d="M3 3 Q52 -1 101 3 L100.6 12 Q52 8 3.4 12 Z" fill="#6B5638" opacity=".75"/><path d="M34 70 H70 V74 H34 Z" fill="#8F7C5D"/>'
            f'<ellipse cx="52" cy="3" rx="49" ry="2.6" fill="#4A3A26" opacity=".85"/><path d="M14 18 Q16 44 26 60" stroke="#FFF" stroke-width="3" opacity=".25" fill="none" stroke-linecap="round"/></g>')

def _jar(n, x, by, sc, s, cloth="#ECE4D3"):
    w, h = 190 * sc, 330 * sc
    return (_shadow(n, x - w / 2, w, by, h, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})">'
            f'<path d="M8 128 H182 V300 Q182 322 160 322 H30 Q8 322 8 300 Z" fill="#B87A35" opacity=".92"/><rect x="8" y="118" width="174" height="15" rx="5" fill="#E6D6B4"/>'
            f'<rect x="8" y="131" width="174" height="5" fill="#C9A66B" opacity=".5"/>'
            f'<path d="M30 40 H160 Q160 66 176 74 Q190 82 190 104 V300 Q190 330 160 330 H30 Q0 330 0 300 V104 Q0 82 14 74 Q30 66 30 40 Z" fill="#FFFFFF" opacity=".12" stroke="{s["glass_line"]}" stroke-opacity=".65" stroke-width="2"/>'
            f'<path d="M14 110 V300" stroke="#FFFFFF" stroke-width="6" opacity=".3" stroke-linecap="round"/>'
            f'<path d="M14 18 Q95 4 176 18 L178 58 Q176 66 166 62 Q95 52 24 62 Q14 66 12 58 Z" fill="{cloth}"/><path d="M22 60 Q30 76 26 92 M168 60 Q160 78 166 94" stroke="{cloth}" stroke-width="10" fill="none" stroke-linecap="round"/>'
            f'<path d="M24 46 Q95 36 166 46" stroke="#8B6B45" stroke-width="3" fill="none"/></g>')

def _soap(n, x, by, sc, s):
    w, h = 210 * sc, 140 * sc
    return (_shadow(n, x - w / 2, w, by, h * .55, s) +
            f'<g transform="translate({x - w / 2:.1f},{by - h:.1f}) scale({sc})"><rect width="210" height="140" fill="#F4D9C6"/><rect width="210" height="140" fill="url(#sp{n})"/>'
            f'<image href="assets/collab/kombar-artwork.svg" x="86" y="22" width="100" height="100"/>'
            f'<text x="34" y="126" font-family="Inter" font-weight="700" font-size="25" fill="#1E1E1E" transform="rotate(-90 34 126)" letter-spacing=".5">KOM’BAR</text></g>')

def _card(n, x, by, w, h, s, inner_svg, rot=-4, fill="#FBF8F2"):
    return (f'<g transform="translate({x},{by}) rotate({rot})"><rect x="6" y="8" width="{w}" height="{h}" fill="#000" opacity="{s["shadow"] * .9:.2f}" filter="url(#bs{n})"/>'
            f'<rect width="{w}" height="{h}" fill="{fill}"/>{inner_svg}</g>')

def still(dk, kind="range", ratio="4/3", cap="", flavours=("［フレーバー］", "［フレーバー］", "［限定］"), label=None, pos="50% 50%", zoom=None, cy=None, note=False):
    """An SVG still life. dk picks the light and props; label picks the bottle label (defaults to dk)."""
    _uid[0] += 1; n = _uid[0]
    s = SCENES[dk]
    lab = label or dk
    d = D.get(lab, D["current"]) if lab in D else D["current"]
    glasses = D[lab]["glass"] if lab in D else ["#9C5B22", "#7A4519", "#B57A3C"]
    capc = D[lab]["cap"] if lab in D else "#1E1E1E"
    W, H, T = 1600, 1200, 742
    defs = (f'<linearGradient id="wa{n}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{s["wall"][0]}"/><stop offset="1" stop-color="{s["wall"][1]}"/></linearGradient>'
            f'<linearGradient id="ta{n}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{s["table"][0]}"/><stop offset="1" stop-color="{s["table"][1]}"/></linearGradient>'
            f'<filter id="bl{n}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="12"/></filter>'
            f'<filter id="bs{n}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
            f'<filter id="bw{n}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="38"/></filter>')
    bg = f'<rect width="{W}" height="{T}" fill="url(#wa{n})"/><rect y="{T}" width="{W}" height="{H - T}" fill="url(#ta{n})"/>'
    if dk == "current":
        bg += f'<ellipse cx="560" cy="360" rx="520" ry="300" fill="#FFFFFF" opacity=".75" filter="url(#bw{n})"/><rect y="{T}" width="{W}" height="2" fill="#FFFFFF" opacity=".9"/>'
    elif dk == "lenora":
        bg += (f'<polygon points="380,0 760,0 1060,{T} 620,{T}" fill="#F2E6D0" opacity=".07" filter="url(#bw{n})"/>'
               f'<ellipse cx="820" cy="{T + 110}" rx="520" ry="120" fill="#F2E6D0" opacity=".10" filter="url(#bw{n})"/><rect y="{T}" width="{W}" height="1.5" fill="#F2E6D0" opacity=".12"/>')
    elif dk == "ogg":
        panes = "".join(f'<rect x="{x}" y="{y}" width="112" height="128" fill="#FFF9EE"/>' for x in range(640, 1200, 124) for y in range(150, 700, 140))
        bg += (f'<g transform="skewX(-14)" opacity=".55" filter="url(#bs{n})">{panes}</g>'
               + "".join(f'<rect y="{T + 26 + 38 * i}" width="{W}" height="1.5" fill="#8A6A3A" opacity=".10"/>' for i in range(12)) +
               f'<rect y="{T}" width="{W}" height="2" fill="#FFF8EA" opacity=".6"/>')
    elif dk == "collab":
        bg += f'<ellipse cx="560" cy="360" rx="520" ry="300" fill="#FFF4EC" opacity=".7" filter="url(#bw{n})"/>'
    grads, objs = [], []
    def add_bottle(i, x, by, sc, fl="［フレーバー］", no="027", g=None):
        gr, ob = _bottle(n, i, x, by, sc, g or glasses[i % 3], lab if lab in D else "plain", capc, fl, no, s)
        grads.append(gr); objs.append(ob)
    if kind == "range":
        for i, (x, fl, no) in enumerate(zip((622, 800, 978), flavours, ("027", "028", "029"))):
            add_bottle(i, x, 846 + (i == 1) * 6, 1.32, fl, no)
    elif kind == "pour":
        add_bottle(0, 720, 840, 1.34)
        objs.append(_glass(n, 905, 872, 1.55, s))
    elif kind == "single":
        if dk == "lenora":
            card = ('<rect x="10" y="10" width="160" height="210" fill="none" stroke="#2B2926" stroke-width="1.6"/><rect x="16" y="16" width="148" height="198" fill="none" stroke="#2B2926" stroke-width="1"/>'
                    '<text x="90" y="62" font-family="EB Garamond" font-size="13" letter-spacing="3" text-anchor="middle" fill="#6E6860">MADE OUT TO</text>'
                    '<text x="90" y="125" font-family="Zen Old Mincho" font-size="22" text-anchor="middle" fill="#2B2926">［お名前］様</text>'
                    '<text x="90" y="190" font-family="EB Garamond" font-size="15" text-anchor="middle" fill="#2B2926">No. 027</text>')
            objs.append(_card(n, 905, 640, 180, 230, s, card, rot=-6, fill="#EFEBE2"))
        add_bottle(0, 760, 870, 1.55)
        if dk == "ogg":
            objs.append(_yunomi(n, 965, 892, 1.5, s))
        if dk == "ogg" and note:
            note = '<text x="22" y="52" font-family="Klee One" font-size="21" fill="#3A3631">今日もゆっくり。</text><text x="22" y="90" font-family="Klee One" font-size="17" fill="#3A3631">— kimy</text>'
            objs.insert(0, _card(n, 540, 880, 230, 120, s, note, rot=-5))
        if dk == "current":
            objs.append(_glass(n, 930, 884, 1.4, s))
    elif kind == "jar":
        objs.append(_jar(n, 740, 870, 1.25, s, cloth="#EFEBE2" if dk == "lenora" else "#ECE4D3"))
        objs.append(_glass(n, 990, 890, 1.35, s, liquid="#C27F35"))
    elif kind == "gift":
        grads.append(f'<linearGradient id="sp{n}" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".06"/><stop offset=".4" stop-color="#FFF" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".08"/></linearGradient>')
        add_bottle(0, 700, 850, 1.3)
        objs.append(_soap(n, 920, 880, 1.45, s))
    elif kind == "glass":
        objs.append(_glass(n, 800, 880, 2.3, s))
    z = zoom or {"range": 1.75, "pour": 1.8, "single": 1.7, "jar": 1.6, "glass": 2.0, "gift": 1.7}.get(kind, 1.6)
    c = cy or {"range": 680, "pour": 690, "single": 680, "jar": 690, "glass": 760, "gift": 690}.get(kind, 700)
    rw, rh = (float(v) for v in ratio.split("/"))
    r = rw / rh
    need_h, need_w = {"range": (600, 640), "pour": (560, 520), "single": (720, 660), "jar": (560, 540), "glass": (440, 360), "gift": (600, 620)}.get(kind, (560, 560))
    z = min(z, W / (max(r, W / H) * need_h), H * min(r, W / H) / need_w)
    vw, vh = W / z, H / z
    svg = (f'<svg viewBox="{800 - vw / 2:.0f} {c - vh / 2:.0f} {vw:.0f} {vh:.0f}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Photography direction: {cap or kind}">'
           f'<defs>{defs}{"".join(grads)}</defs>{bg}{"".join(objs)}</svg>')
    capt = f'<span class="still-cap" style="color:{s["cap_ink"]}">Photo direction · {cap}</span>' if cap else ""
    return f'<div class="still" style="aspect-ratio:{ratio}; --pos:{pos}">{svg}{capt}</div>'

def ph(dk, kind, left, top, width, ratio="1/1", **kw):
    """A still placed inside an artboard."""
    return f'<div style="left:{left}; top:{top}; width:{width}">{still(dk, kind, ratio, **kw)}</div>'
