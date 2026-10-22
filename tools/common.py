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

# ------------------------------------------------------------------ photography: shot cards, not drawings
# Where a photograph belongs we show what the photograph should be: subject, light and props, set in type.
SHOTS = {
 "current": dict(bg="#EDECE8", ink="#6B6B6B", light="Soft daylight · white table · amber glass"),
 "lenora":  dict(bg="#2A2826", ink="#A39E95", light="One shaft of evening light · dark wood"),
 "ogg":     dict(bg="#E5D9C3", ink="#6E655B", light="Shōji light · pale oak · kimy’s hands"),
 "collab":  dict(bg="#EAD8C8", ink="#7A6555", light="Daylight · peach paper · both studios"),
}
SUBJECT = {"range": "The range, three bottles", "pour": "The pour", "single": "One bottle, close", "jar": "The brewing jar",
           "glass": "A glass, just poured", "gift": "Bottle and soap, together"}

def still(dk, kind="range", ratio="4/3", cap="", subject=None, **_):
    """A shot card: the photograph to be taken, described in type inside crop marks."""
    s = SHOTS[dk]
    return (f'<div class="still shot" style="aspect-ratio:{ratio}; background:{s["bg"]}; color:{s["ink"]}">'
            f'<i class="cm tl"></i><i class="cm tr"></i><i class="cm bl"></i><i class="cm br"></i>'
            f'<div class="shot-t"><span class="shot-k">Photograph</span><span class="shot-s">{subject or SUBJECT.get(kind, kind)}</span>'
            f'<span class="shot-l">{cap or s["light"]}</span></div></div>')

def ph(dk, kind, left, top, width, ratio="1/1", **kw):
    """A still placed inside an artboard."""
    return f'<div style="left:{left}; top:{top}; width:{width}">{still(dk, kind, ratio, **kw)}</div>'
