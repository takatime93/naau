"""Shared building blocks for the naʻau concept site (v3).

Artboards: print and social pieces are drawn on a 1000-unit-wide board. Write sizes
as [[n]] and they become container units, so a piece keeps its proportions at any size.
Stills: SVG still-life scenes stand in for photography, lit and propped per direction.
"""
import os, re, atexit
import ink
from ja import JA
import hashlib
CSS_V = hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'css', 'site.css'), 'rb').read()).hexdigest()[:8]

# ---------------------------------------------------------------- language: Japanese first, English on toggle
MISSING = set()

_LATIN = re.compile(r"[A-Za-z0-9ʻ’'][A-Za-z0-9ʻ’'×·:%./\-\s]*[A-Za-z0-9’%.]|[A-Za-z]")

def _mark_latin(ja):
    """Inside Japanese text, wrap Latin runs so they can be set a touch larger than the kana and kanji around them."""
    out = []
    for part in re.split(r"(<[^>]+>)", ja):
        if part.startswith("<"):
            out.append(part)
        elif re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", part):
            out.append(_LATIN.sub(lambda m: f'<span class="lx">{m.group(0)}</span>' if re.search(r"[A-Za-z]{2,}", m.group(0)) else m.group(0), part))
        else:
            out.append(part)
    return "".join(out)

def T(ja, en):
    """Both languages, one shown at a time."""
    return f'<span class="l-ja" lang="ja">{_mark_latin(ja)}</span><span class="l-en" lang="en">{en}</span>'

def t(en):
    """Translate a presentation string through JA; untranslated strings are logged."""
    if not en or not isinstance(en, str):
        return en
    if en in JA:
        return T(JA[en], en)
    if re.search(r"[A-Za-z]{3,}", re.sub(r"<[^>]+>", "", en)):
        MISSING.add(en)
    return en

@atexit.register
def _dump_missing():
    if MISSING and os.environ.get("NAAU_MISSING"):
        with open(os.environ["NAAU_MISSING"], "a") as f:
            for m in sorted(MISSING):
                f.write(m.replace("\n", " ") + "\n")

from html.parser import HTMLParser

class _Texts(HTMLParser):
    """Collect presentation text nodes: outside artboards, shop mockups, SVG and already-translated spans."""
    SKIP = ("ab", "shop", "l-en", "l-ja", "kb-wm")
    def __init__(self):
        super().__init__(convert_charrefs=False); self.stack = []; self.found = set()
    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "input", "meta", "link", "i", "use", "path", "circle", "rect", "polygon", "line", "image"):
            return
        cls = dict(attrs).get("class") or ""
        skip = tag in ("svg", "script", "style", "title", "code") or any(c in cls.split() for c in self.SKIP)
        self.stack.append(skip or (self.stack[-1] if self.stack else False))
    def handle_endtag(self, tag):
        if tag in ("br", "img", "input", "meta", "link", "i", "use", "path", "circle", "rect", "polygon", "line", "image"):
            return
        if self.stack: self.stack.pop()
    def handle_data(self, data):
        d = data.strip()
        if d and not (self.stack and self.stack[-1]) and re.search(r"[A-Za-z]{3,}", d):
            self.found.add(d)

def localize(html):
    """Wrap every presentation text node that has a translation; log the rest."""
    def sub(m):
        txt = m.group(1)
        key = txt.strip()
        if key in JA:
            lead, trail = txt[:len(txt) - len(txt.lstrip())], txt[len(txt.rstrip()):]
            return f">{lead}{T(JA[key], key)}{trail}<"
        return m.group(0)
    body_start = html.find("<body")
    head, body = html[:body_start], html[body_start:]
    # only text directly between tags; artboard text is protected because its keys are never added to JA
    body = re.sub(r">([^<>]*[A-Za-z][^<>]*)<", sub, body)
    p = _Texts(); p.feed(body)
    for f in p.found:
        if f not in JA: MISSING.add(f)
    return head + body

LANG_TOGGLE = ('<button class="lang" type="button" onclick="naauLang(document.documentElement.lang===\'ja\'?\'en\':\'ja\')">'
               '<span class="l-ja">EN</span><span class="l-en">日本語</span></button>')
LANG_SCRIPT = ('<script>function naauLang(l){document.documentElement.lang=l;try{localStorage.setItem("naau-lang",l)}catch(e){}}'
               '(function(){var l="ja";try{l=localStorage.getItem("naau-lang")||"ja"}catch(e){}document.documentElement.lang=l})();</script>')

SITE = None

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=Cormorant+Garamond:wght@400;500&family=Shippori+Mincho+B1:wght@500;700;800'
         '&family=Zen+Old+Mincho:wght@400;600;700&family=Zen+Kaku+Gothic+New:wght@300;400;500;700&family=Klee+One:wght@400;600&family=Yomogi&family=Courier+Prime'
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
    full = {"index": T("概要", "Overview"), "current": T("現在のロゴ", "Current identity"), "lenora": T("A案 · Lenora", "Concept A · Lenora"),
            "ogg": T("B案 · Ogg", "Concept B · Ogg"), "collab": "naʻau × Ivycoast"}
    short = {"index": T("概要", "Overview"), "current": T("現在", "Current"), "lenora": T("A案", "A · Lenora"), "ogg": T("B案", "B · Ogg"), "collab": T("コラボ", "Collab")}
    lis = "".join(f'<li><a href="{f}.html"' + (' aria-current="page"' if f == active else '') + f'><span class="nl">{full[f]}</span><span class="ns">{short[f]}</span></a></li>'
                  for f in ["index"] + ORDER + ["collab"])
    return (f'<nav class="sitenav" aria-label="Concept sections"><div class="wrap"><a class="brand" href="index.html">naʻau <span>{T("ブランドコンセプト", "brand concepts")}</span></a>'
            f'<ul>{lis}</ul>{LANG_TOGGLE}</div></nav>')

def page(fname, title, cls, body, script="", extra_head=""):
    if '</div></footer>' in body:
        head, tail = body.rsplit('</div></footer>', 1)
        body = head + credits(body) + '</div></footer>' + tail
    html = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title>{FONTS}<link rel="stylesheet" href="assets/css/site.css?v={CSS_V}">{LANG_SCRIPT}{extra_head}</head>'
            f'<body class="{cls}">{ink.DEFS}{body}{script}</body></html>\n')
    open(os.path.join(SITE, fname), "w").write(localize(U(html)))

def sec(num, title, desc, content, cls="", sid=""):
    idattr = f' id="{sid}"' if sid else ""
    return (f'<section class="sec {cls}"{idattr}><div class="wrap"><header class="sh"><span class="sh-n">{num}</span><h2>{t(title)}</h2>'
            + (f'<p>{t(desc)}</p>' if desc else '') + f'</header>{content}</div></section>')

def pf(inner, title, spec="", ratio=None, plate=True, style="", pstyle=""):
    """A plate (asset on its backdrop) with a two-line caption."""
    ar = f"aspect-ratio:{ratio};" if ratio else ""
    body = f'<div class="plate" style="{ar}{pstyle}">{inner}</div>' if plate else inner
    cap = f'<figcaption><b>{t(title)}</b>' + (f'<span>{t(spec)}</span>' if spec else '') + '</figcaption>'
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
    bars = "".join(f'<div class="sw" style="flex:{w}; background:{h}; color:{"#FFFFFF" if dark(h) else "#1E1E1E"}"><b>{n}</b><span>{h}</span><em>{t(role)}</em></div>'
                   for n, h, role, w in items)
    return f'<div class="swatches">{bars}</div>' + (f'<p class="swnote">{t(note)}</p>' if note else "")

def previews(d):
    """The home page in a browser and the product page on a phone; each frame is a link to the working page."""
    k = d["key"]
    go = T("サイトを開く →", "Open the site →")
    return ('<div class="pv">'
            f'<figure class="pf pv-desk"><a class="pv-go" href="{k}-home.html" aria-label="{d["name"]}: home page"><div class="browser"><div class="browser-bar"><i></i><i></i><i></i><span>naau / {k}-home</span><b class="pv-chip">{go}</b></div>'
            f'<div class="browser-view" data-fit="1440"><iframe src="{k}-home.html" title="Home page preview" loading="lazy" tabindex="-1" style="width:1440px; height:2000px"></iframe></div></div></a>'
            f'<figcaption><b>{T("ホームページ", "Home page")}</b><span>{T("レスポンシブで、実際に動きます。", "Responsive and working.")} <a href="{k}-home.html">{T("全画面で見る →", "Open full size →")}</a></span></figcaption></figure>'
            f'<figure class="pf pv-phone"><a class="pv-go" href="{k}-product.html" aria-label="{d["name"]}: product page"><div class="phone"><div class="phone-view" data-fit="390"><iframe src="{k}-product.html" title="Product page preview" loading="lazy" tabindex="-1" style="width:390px; height:1690px"></iframe></div></div></a>'
            f'<figcaption><b>{T("商品ページ（スマートフォン）", "Product page, on a phone")}</b><span>{T("税込価格、クール便の送料とお届け日をカートの横に。", "Price with tax, クール便 cost and date beside the cart.")} <a href="{k}-product.html">{T("開く →", "Open →")}</a></span></figcaption></figure>'
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
                                ("配送・返品", "クール便（冷蔵）でお届けします。送料 ¥［　］。日時指定ができます。生ものにつき、お客様都合の返品はお受けできません。")])

# ------------------------------------------------------------------ photography: shot cards, not drawings
# Where a photograph belongs we show what the photograph should be: subject, light and props, set in type.
SHOTS = {
 "current": dict(bg="#EDECE8", ink="#6B6B6B", light="Soft daylight · white table · amber glass"),
 "lenora":  dict(bg="#2A2826", ink="#A39E95", light="One shaft of evening light · dark wood"),
 "ogg":     dict(bg="#E5D9C3", ink="#6E655B", light="Shōji light · pale oak · the handwritings"),
 "collab":  dict(bg="#D7DAD4", ink="#59605A", light="Daylight · peach paper · both studios"),
}
SUBJECT = {"range": "The range, three bottles", "pour": "The pour", "single": "One bottle, close", "jar": "The brewing jar",
           "glass": "A glass, just poured", "gift": "Bottle and soap, together"}

# Stand-in photographs from Unsplash (free licence, no attribution required; credited in the footer and README).
# Hotlinked from images.unsplash.com at the width needed. key: (photo id, photographer, page slug)
PHOTOS = {
    "jar":      ("1583396216852-1e1d61137170", "Tim-Oliver Metz", "cZIiXRX9PqE"),
    "mother":   ("1573812914274-226dc19fbe17", "Megumi Nachev", "TcNG1talu3s"),
    "shelf":    ("1642423453295-1e21cbc95967", "Stanley Kustamin", "OhCiWCwiBkE"),
    "teabowl":  ("1567922045116-2a00fae2ed03", "Aniketh Kanukurthi", "Qaor6nxikUM"),
    "leaves":   ("1763617702099-d956f3fd8324", "晨曦 Hey", "iIgnfQ-vERM"),
    "hands":    ("1605265058749-78af14a1be2b", "Sincerely Media", "UmDfdonflT0"),
    "batter":   ("1697247079184-efb23487a172", "MeSSrro", "8aTZDhvHaVM"),
    "basin":    ("1770941326576-eb1520695ec8", "Clay Banks", "lQ6U_GSziPQ"),
    "forest":   ("1786909100019-a43467264c47", "Eva Balogh", "-up4eOuN9CY"),
    "cedar":    ("1766586049961-1eca6500ca49", "Yosuke Ota", "ChpQXg2EYY4"),
    "mandarin": ("1734894966816-9f2b7bf9c605", "alien beker", "Jw3XXq4u7NU"),
    "shadow":   ("1530177150700-84cd9a3b059b", "Augustine Wong", "T0BYurbDK_M"),
    # Concept A · Lenora, 手仕込み: hands, craft and old ways, shown in black and white
    "clay":     ("1465631494067-3e0491e95bd1", "Quino Al", "vBxlL1xpSdc"),
    "cupped":   ("1571391034628-2a2261e8273f", "Motoki Tonn", "tJ6GNCJ1gyM"),
    "whisk":    ("1759933164283-ab161f34bd02", "adrien lopes", "VhPtiipk0tE"),
    "care":     ("1773234005378-ceebf3c877b9", "Thomas Griggs", "mwGrAl1X514"),
    "oldhand":  ("1602152563796-29267eb24c0f", "Bruce Tang", "1sRJgrV4nwI"),
    "mist":     ("1578554700872-ef0e27c46d37", "Laura Thonne", "1PCoQuJspGw"),
    "grind":    ("1492552085122-36706c238263", "Katherine Hanlon", "bd_fCZhy_W8"),
    "teafield": ("1562558742-ec7adb76fe11", "Kevin Ma", "ppEq6JGLOUE"),
    "kettle":   ("1531876066433-09d3a1f79fac", "五玄土 ORIENTO", "fLZeuI-OFBc"),
    "brewjar":  ("1617854307432-13950e24ba07", "Prchi Palwe", "pdUh5igZjDQ"),
    # Concept B · Ogg: warm light, paper, persimmon, moss and amber, some shown out of focus for mood
    "shoji":    ("1767839507904-46980ac12d53", "Perry Merrity II", "jHl9eZSC9Ac"),
    "wall":     ("1529047033375-f402d3da24ca", "Alexander Possingham", "RIQ96s3Uzso"),
    "curtain":  ("1682421938316-4b186e25174c", "Saad Ahmad", "3VSa5sbvdpc"),
    "hoshigaki":("1762980623026-c22d28494369", "Madeline Liu", "zyIVA-DSiC4"),
    "amber":    ("1729457923221-34e324fec9e5", "Charly Seyler", "lUD3FNbGecQ"),
    "pourbowl": ("1562547256-2c5ee93b60b7", "CHI CHEN", "oBoELXgJR1w"),
    "pourcup":  ("1758221054731-744af4bf4d68", "Marie G.", "MQ-Vuwjcv68"),
    "moss":     ("1708022772151-26030f4a4ba4", "Nicholas Bullett", "qiWaWWhehTo"),
    "slit":     ("1602911310167-1b82343f6264", "gryffyn m", "pl5B-k_Xk8Y"),
    "dusk":     ("1686395810129-4ecb06a60f4e", "He Junhui", "7vB1eUo0BOA"),
    "washi":    ("1572037937946-ece5e3598bee", "Bernd Dittrich", "BH7H9aNJUwE"),
    "bokeh":    ("1607202563005-cbaabe636953", "Johny Goerend", "5jO5fQqSZi4"),
    "glow":     ("1608483555724-d430b692b776", "Andy Holmes", "A1WVd4snKLw"),
    "haze":     ("1604339452989-f0d369b025ac", "Thomas Lefebvre", "lXQ-bPGGDDw"),
    "ceramics": ("1612058060757-aa8f7f66e687", "Geraldine Lewa", "N_Z91Evs_oM"),
    "linen":    ("1634665810235-011d663754e7", "Kateryna Hliznitsova", "2NDtPNiLcD0"),
    "glasses":  ("1691403970049-d9ec6b27117f", "Harper Sunday", "o09l6wRwIX8"),
}
def pic(key, w=1200, pos="50% 50%", tone="", alt=""):
    """A photograph filling its box (object-fit: cover)."""
    pid = PHOTOS[key][0]
    return (f'<img class="pic" src="https://images.unsplash.com/photo-{pid}?w={w}&amp;q=78&amp;auto=format&amp;fit=crop" '
            f'loading="lazy" alt="{alt}" style="object-position:{pos}; {tone}">')

def credits(html):
    """Footer line naming the photographers whose photographs appear in this page."""
    names = sorted({who for pid, who, _ in PHOTOS.values() if f"photo-{pid}?" in html})
    return ('<p class="credits">' + T("仮の写真：", "Stand-in photographs: ") + ", ".join(names) + " / Unsplash</p>") if names else ""

BW = "filter:grayscale(1) contrast(1.18) brightness(.94)"
BW_FLIP = BW + "; transform:scaleX(-1)"   # mirrored, so the subject sits left of the type
TONE = {"current": "", "lenora": BW,
        "ogg": "", "collab": ""}
PICK = {("current", "range"): "shelf", ("current", "pour"): "teabowl", ("current", "jar"): "jar", ("current", "single"): "jar",
        ("lenora", "jar"): "grind", ("lenora", "pour"): "cupped", ("lenora", "range"): "clay",
        ("ogg", "pour"): "pourcup", ("ogg", "jar"): "amber", ("ogg", "range"): "glasses"}

def still(dk, kind="range", ratio="4/3", cap="", subject=None, **_):
    """A stand-in photograph where one fits; otherwise a shot card describing the photograph to be taken."""
    if (dk, kind) in PICK:
        return (f'<div class="still photo" style="aspect-ratio:{ratio}">{pic(PICK[dk, kind], tone=TONE[dk])}'
                f'<span class="pic-note">{T("仮の写真", "Stand-in photo")}</span></div>')
    s = SHOTS[dk]
    return (f'<div class="still shot" style="aspect-ratio:{ratio}; background:{s["bg"]}; color:{s["ink"]}">'
            f'<i class="cm tl"></i><i class="cm tr"></i><i class="cm bl"></i><i class="cm br"></i>'
            f'<div class="shot-t"><span class="shot-k">Photograph</span><span class="shot-s">{subject or SUBJECT.get(kind, kind)}</span>'
            f'<span class="shot-l">{cap or s["light"]}</span></div></div>')

def ph(dk, kind, left, top, width, ratio="1/1", **kw):
    """A still placed inside an artboard."""
    return f'<div style="left:{left}; top:{top}; width:{width}">{still(dk, kind, ratio, **kw)}</div>'
