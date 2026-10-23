"""The three direction pages, each with its own home and product mockups.

Current identity: white, centred, photo-led, round sticker labels.
Concept A (Lenora): 手仕込み, brewed by hand. Black and white, linocut prints and photographs of hands; one red.
Concept B (Ogg): 間, the pause. Gofun and ōdo, vertical Japanese and handwritten notes, with a deep board per flavour and framed photographs.
"""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
import ink as K
from common import D, L, ab, fitw, pf, ph, still, sec, chips
C.SITE = sys.argv[1]

FL = ("［フレーバー］", "［フレーバー］", "［限定］")

def social(k, posts, story):
    tiles = "".join(pf(f'<div style="position:relative">{p}<span class="safe"></span></div>', t, sp, plate=False) for p, t, sp in posts)
    tiles += pf(story, "Story", "9:16 · 1080 × 1920", plate=False)
    return (f'<div id="soc-{k}"><div class="sub" style="margin-top:0"><h3>Feed and story</h3><button class="toggle" type="button" aria-pressed="false" '
            f'onclick="var s=document.getElementById(\'soc-{k}\');s.classList.toggle(\'show-safe\');this.setAttribute(\'aria-pressed\',s.classList.contains(\'show-safe\'))">Show 4:5 safe area</button></div>'
            f'<div class="soc">{tiles}</div></div>')

def spec(items):
    return '<div class="spec">' + "".join(f'<div><p class="eyebrow">{a}</p>{b}<p class="muted" style="font-size:13px">{c}</p></div>' for a, b, c in items) + '</div>'

def notes(lines):
    return '<div class="notes"><span>Notes</span><div>' + "".join(f'<p>{l}</p>' for l in lines) + '</div></div>'

SITE_BASE = {
    "current": "Base theme, the daylight shop: white, colour photographs in daylight, rounded cards and the round sticker as the shop’s own shape. Friendly and quick to buy from.",
    "lenora": "Base theme, the stone shop: black-and-white photographs, small mono type on a grid, numbered batches and the wordmark set huge at the foot. Quiet and exact.",
    "ogg": "Base theme, the slow journal: gofun paper, photographs set between the words, handwriting over photographs, a typed page and a journal. Poetic and personal.",
}

def direction_page(d, hero, idn, pal, typ, pack, prt, soc, nts):
    k = d["key"]
    body = (C.nav(k) + hero +
            sec("01", "Identity", "The mark on its ground, the moods it can take, colour and type.", idn + f'<div class="sub"><h3>Colour</h3><p>{pal[1]}</p></div>' + pal[0] + typ) +
            sec("02", "Packaging", "330 ml amber glass, matte water-resistant labels, and the 一括表示 panel on the back.", pack) +
            sec("03", "Print", "An A5 workshop flyer and a 91 × 55 mm shop card.", prt) +
            sec("04", "Social", "Feed posts at 3:4 (1080 × 1440) with key content inside the 4:5 crop; stories at 9:16.", soc) +
            sec("05", "Website", SITE_BASE[k], C.previews(d)) +
            f'<section class="sec"><div class="wrap">{nts}</div></section>'
            '<footer class="site"><div class="wrap">naʻau kombucha · brand concepts by Ivycoast · text in ［brackets］ is for naʻau to fill in · photography is shown as direction, not final images.</div></footer>')
    C.page(f"{k}.html", f'{d["name"]} — naʻau brand concepts', d["cls"], body, C.FIT)

# ====================================================================== SHIRO
S = D["current"]

def s_dir():
    hero = (f'<header class="wrap" style="padding-top:clamp(64px,9vw,120px); text-align:center; display:flex; flex-direction:column; align-items:center; gap:22px">'
            f'<p class="eyebrow">Current identity · the script logo</p>{L(S, "1e1e1e", "min(62%,340px)")}'
            f'<h1 style="margin:22px 0 0; font-weight:400; font-size:clamp(30px,3.6vw,46px); line-height:1.15">The brand as it is</h1>'
            f'<p style="max-width:560px; color:var(--muted)">The script logo, on white. Black ink, small centred type, nothing added. The colour comes from the amber glass and the light in the photographs.</p></header>')

    pr, pb = 4 / 3, 1
    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 3, f'<div class="fill" style="display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "40%")}</div>', "100%", cls="flat"), "Plain", "The lockup, centred and small, on white."),
        pf(ab(4, 3, ph("current", "pour", "0", "0", "100%", "4/3.4") + f'<div style="left:0; right:0; bottom:0; height:[[110]]; background:#fff; display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "16%", small=True)}</div>', "100%", cls="flat"), "Photo-led", "The photograph carries the colour; the mark sits beneath it."),
        pf(ab(4, 3, f'<div style="left:50%; top:50%; width:[[380]]; transform:translate(-50%,-50%) rotate(-4deg); filter:drop-shadow(0 [[10]] [[18]] rgba(0,0,0,.12))">{s_tile("［フレーバー］", "1/1", "transparent", "100%")}</div>', "100%", "background:#F1F1EF", cls="flat"), "Sticker", "The round sticker is the brand’s main surface: the script, small, on white."),
    ]) + '</div>'
    pal = (chips([("White", "#FFFFFF", "Ground", 3), ("Ink", "#1E1E1E", "Text · 16.9:1", 2), ("Grey", "#6B6B6B", "Small text · 5.3:1", 1), ("Mist", "#F1F1EF", "Photo backdrops", 2), ("Amber glass", "#8E4E1F", "From the bottle only", 1.2)]),
           "Plain white and ink, as naʻau looks today.")
    typ = spec([("Wordmark", L(S, "1e1e1e", "160px"), "The script logo, as it is"),
                ("Japanese", '<p style="font-family:var(--sans); font-weight:300; font-size:20px; line-height:1.9">飲むだけじゃない。<br>自分の身体に気づく、kombucha。</p>', "Zen Kaku Gothic New, Light"),
                ("Latin", '<p style="font-family:var(--sans); font-weight:300; font-size:20px; letter-spacing:.14em">NO. 027 · 330 ML</p>', "Same family, tracked, small")])
    sticker = ab(1, 1, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[46]]">{L(S, "1e1e1e", "62%")}<span style="position:static; font-family:var(--sans); font-size:[[40]]; letter-spacing:.24em">［フレーバー］· 330 ml</span></div>', fitw(1, 1, .7), "border-radius:50%")
    back = ab(3, 4, f'<div class="fill col" style="padding:[[80]] [[76]]; font-family:var(--sans); font-size:[[42]]; line-height:1.75; gap:[[40]]"><dl style="position:static; column-gap:[[40]]">{C.ichi_rows()}</dl>'
              f'<p style="position:static">{C.HANDLING}</p><div style="position:static; margin-top:auto; border:1px dashed currentColor; padding:[[24]] [[30]]; display:flex; justify-content:space-between"><span>Batch ＿＿</span><span>瓶詰め日 ＿＿</span></div></div>', fitw(1, .75, .8))
    box = ab(4, 3, f'<div class="fill" style="display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "38%")}</div><span style="left:0; right:0; bottom:[[60]]; text-align:center; font-family:var(--sans); font-size:[[30]]; letter-spacing:.3em">要冷蔵 · クール便</span>', "74%")
    trio = "".join(f'<div style="width:24%; transform:rotate({r}deg)">{sticker.replace(fit_w := fitw(1, 1, .7), "100%").replace("［フレーバー］", fl)}</div>' for r, fl in ((-3, "［フレーバー］"), (2, "［フレーバー］"), (-1, "［限定］")))
    pack = (pf(trio, "The range", "Three round stickers, Ø 60 mm, on 330 ml amber glass. The glass is the only colour.", "21/9", pstyle="gap:4%") +
            '<div class="grid g3" style="margin-top:clamp(20px,3vw,36px)">' +
            pf(sticker, "Front sticker", "Matte, water-resistant, Ø 60 mm.", "1/1") +
            pf(back, "Back label", "一括表示 in light Gothic, 8 pt minimum, with a stamp box.", "1/1") +
            pf(box, "Shipping box", "Plain white, the mark centred, 要冷蔵 in small type.", "1/1") + '</div>')
    a5w = fitw(4 / 3, 148 / 210, .82)
    fl_f = ab(148, 210, f'<div style="left:0; right:0; top:[[90]]; display:flex; justify-content:center">{L(S, "1e1e1e", "30%")}</div>' + ph("current", "pour", "[[110]]", "[[330]]", "[[780]]", "1/1", zoom=2.1) +
              f'<p style="left:0; right:0; top:[[1170]]; text-align:center; font-family:var(--sans); font-size:[[46]]; letter-spacing:.16em">コンブチャ ワークショップ</p>'
              f'<p style="left:0; right:0; top:[[1260]]; text-align:center; font-family:var(--sans); font-size:[[32]]; letter-spacing:.2em; color:#6B6B6B">［月日（曜）］· 名古屋</p>', a5w)
    fl_b = ab(148, 210, f'<div class="fill col" style="align-items:center; text-align:center; padding:[[120]] [[90]] [[90]]; font-family:var(--sans); gap:[[40]]">'
              f'<p style="position:static; font-size:[[44]]; letter-spacing:.14em; margin-bottom:[[20]]">ワークショップのご案内</p>' +
              "".join(f'<p style="position:static; font-size:[[36]]; line-height:1.6"><span style="color:#6B6B6B; font-size:[[28]]; letter-spacing:.2em">{a}</span><br>{b}</p>' for a, b in [("日時", "［月日（曜）時間］"), ("場所", "名古屋市［　］"), ("定員", "［　］名（先着順）"), ("参加費", "¥［　］（税込）"), ("申込方法", "Instagram DM / LINE")]) +
              f'<div style="position:static; margin-top:auto; display:flex; gap:[[40]]">' + "".join(f'<span style="width:[[150]]; aspect-ratio:1; border:1px solid currentColor; display:flex; align-items:center; justify-content:center; font-size:[[24]]; letter-spacing:.2em">{q}</span>' for q in ("LINE", "IG")) + '</div></div>', a5w)
    cw = fitw(4 / 3, 91 / 55, .34)
    card_f = ab(91, 55, f'<div class="fill" style="display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "40%")}</div>', cw)
    card_b = ab(91, 55, f'<p class="fill" style="display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:var(--sans); font-size:[[40]]; line-height:1.9; letter-spacing:.1em">名古屋市［　］<span>@naau_kombucha</span></p>', cw)
    prt = ('<div class="grid g2">' + pf(fl_f + fl_b, "A5 workshop flyer", "White and centred, one photograph; details in the standard order on the back.", "4/3") +
           pf(card_f + card_b, "Shop card, 91 × 55 mm", "White on both sides.", "4/3", pstyle="flex-direction:column; gap:7%") + '</div>')
    posts = [
        (ab(3, 4, f'<div style="left:[[200]]; top:[[230]]; width:[[600]]; filter:drop-shadow(0 [[14]] [[24]] rgba(0,0,0,.12))">{s_tile("［フレーバー］", "1/1", "transparent", "100%")}</div>' + '<p style="left:0; right:0; bottom:[[90]]; text-align:center; font-family:var(--sans); font-size:[[36]]; letter-spacing:.16em">No. 027 · ［フレーバー］</p>', "100%", "background:#F1F1EF", cls="flat post"), "Batch post", "This week’s sticker, one line beneath."),
        (ab(3, 4, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[80]]"><p style="position:static; font-family:var(--sans); font-weight:300; font-size:[[50]]; line-height:2.1; text-align:center">飲むだけじゃない。<br>自分の身体に気づく、kombucha。</p>{L(S, "1e1e1e", "[[200]]", small=True)}</div>', "100%", cls="flat post", style="outline:1px solid var(--rule)"), "Words post", "Small centred type on white."),
        (ab(3, 4, "".join(f'<div style="left:[[{x}]]; top:[[{y}]]; width:[[380]]; transform:rotate({r}deg); filter:drop-shadow(0 [[10]] [[18]] rgba(0,0,0,.12))">{s_tile(fl, "1/1", "transparent", "100%")}</div>' for x, y, r, fl in ((90, 170, -6, "［フレーバー］"), (500, 420, 4, "［限定］"), (150, 760, 2, "［フレーバー］"))),
              "100%", "background:#FFFFFF; outline:1px solid var(--rule)", cls="flat post"), "Range post", "The three stickers, scattered on white."),
    ]
    story = ab(9, 16, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[90]]; text-align:center">{L(S, "1e1e1e", "[[300]]", small=True)}'
               f'<p style="position:static; font-family:var(--sans); font-size:[[64]]; line-height:1.9">今日のおなか、<br>どうですか？</p><div style="position:static; display:flex; gap:[[24]]">' +
               "".join(f'<span style="border:1px solid #1E1E1E; border-radius:999px; padding:[[18]] [[40]]; font-family:var(--sans); font-size:[[40]]">{w}</span>' for w in ("軽い", "重い", "ふつう")) + '</div></div>', "100%", cls="flat story", style="outline:1px solid var(--rule)")
    nts = notes(["The current logo uses a straight apostrophe (na'au). Hawaiian spelling uses the ʻokina (ʻ); worth correcting at the next reprint.",
                 "White and ink are kept deliberately plain. The research favours warm off-whites, so a warmer palette can be added later without changing the look."])
    direction_page(S, hero, idn, pal, typ, pack, prt, social("current", posts, story), nts)

# ---------------------------------------------------------------- the Current website: a bright daylight shop
# White, soft colour photographs in daylight, rounded cards, and the round sticker as the shop's own shape:
# stuck on photographs, used for numbers and buttons. The amber of the glass is the only colour.
AMB = "#8E4E1F"
SFL = ("［フレーバー］", "［フレーバー］", "［限定］", "［3本セット］")

def sticker(fl="［フレーバー］", w="100%"):
    return f'<div class="dl-stk" style="width:{w}">{ab(1, 1, f"""<div class="fill col" style="align-items:center; justify-content:center; gap:[[46]]">{L(S, "1e1e1e", "62%")}<span style="position:static; font-family:var(--sans); font-size:[[40]]; letter-spacing:.24em">{fl}· 330 ml</span></div>""", "100%", "border-radius:50%; background:#fff")}</div>'

def s_shell(content):
    head = (f'<header class="dl-head"><a href="current-home.html" aria-label="naʻau home">{L(S, "1e1e1e", "112px")}</a>'
            '<nav class="dl-nav" aria-label="Shop"><a href="current-product.html">お店</a><a href="current-home.html#how">楽しみかた</a><a href="current-home.html#about">naʻau について</a><a href="#">ワークショップ</a></nav>'
            '<a class="dl-cart" href="#">かご <span>0</span></a></header>')
    foot = (f'<footer class="dl-foot"><div class="dl-foot-card"><div class="dl-foot-top">{L(S, "1e1e1e", "150px")}'
            '<form class="dl-news" onsubmit="return false"><label><span>新しい仕込みと、ワークショップのお知らせ</span><input type="email" placeholder="you@example.com"></label><button class="dl-btn" type="submit">登録する</button><a class="dl-btn dl-ghost" href="#">LINE</a></form></div>'
            f'<div class="dl-foot-links">{C.legal_links()}</div><p class="dl-small">© 2026 naʻau kombucha · concept mockup</p></div></footer>')
    return f'<div class="shop dl">{head}<main>{content}</main>{foot}</div>'

def dl_card(i):
    fl = SFL[i]
    return (f'<a class="dl-card" href="current-product.html"><div class="dl-card-img">{sticker(fl.replace("［3本セット］", "［セット］"), "58%")}</div>'
            f'<div class="dl-card-meta"><div><p>{fl}</p><p class="dl-small">¥［　］（税込）· 330 ml</p></div><span class="dl-plus" aria-label="かごに入れる">+</span></div></a>')

def s_home():
    hero = (f'<section class="dl-hero"><div class="dl-hero-txt"><p class="dl-pill-l">今週の仕込み · No. 027</p>'
            '<h1>飲むだけじゃない。<br>自分の身体に気づく、<span>kombucha。</span></h1>'
            '<p class="dl-lead">naʻau（ナアウ）は、ハワイ語で「腸・心・内なる声」。名古屋の台所で、ひと瓶ずつ仕込んでいます。</p>'
            '<div class="dl-row"><a class="dl-btn" href="current-product.html">お店をのぞく</a><a class="dl-btn dl-ghost" href="#how">楽しみかた</a></div></div>'
            f'<div class="dl-hero-pic">{C.pic("pourbowl", 1600, "50% 50%")}<div class="dl-hero-stk">{sticker("［フレーバー］")}</div></div></section>')
    ticker = '<div class="dl-ticker" aria-hidden="true"><div>' + ("<span>今週の仕込み</span><span>［フレーバー］</span><span>［フレーバー］</span><span>［限定］</span><span>クール便でお届け</span><span>名古屋の台所から</span>" * 2) + '</div></div>'
    shop = ('<section class="dl-sec" id="shop"><div class="dl-sec-h"><h2>今週のコンブチャ</h2><a href="current-product.html">すべて見る →</a></div>'
            '<div class="dl-grid">' + "".join(dl_card(i) for i in range(4)) + '</div></section>')
    how = [("冷やす", "よく冷やして。開けるときは、ゆっくりと。", "glasses"), ("ひと口目は、そのまま", "まずは何も足さずに。酸味と香りを。", "amber"), ("その日の気分で", "炭酸で割っても、食事と一緒でも。", "teabowl")]
    howto = ('<section class="dl-sec dl-how" id="how"><div class="dl-sec-h"><h2>楽しみかた</h2></div><div class="dl-steps">'
             + "".join(f'<div class="dl-step"><div class="dl-step-pic">{C.pic(k, 900, "50% 50%")}<span class="dl-num">{n}</span></div><p class="dl-step-t">{t}</p><p class="dl-small">{b}</p></div>'
                       for n, (t, b, k) in enumerate(how, 1)) + '</div></section>')
    about = (f'<section class="dl-about" id="about"><div class="dl-about-pic">{C.pic("jar", 1400, "35% 50%")}</div>'
             '<div class="dl-about-txt"><p class="dl-pill-l">naʻau について</p><p class="dl-quote">名前は、<br>直感で決めました。</p>'
             '<p>大好きなハワイの言葉で「直感」は naʻau。腸と感情、内なる声を感じるという意味もあると知って、これしかないと決めました。</p>'
             '<p class="dl-small">名古屋の台所で、ひと瓶ずつ仕込んでいます。</p></div></section>')
    feed = [("shelf", "50% 50%"), ("teabowl", "50% 50%"), ("glasses", "50% 50%"), ("jar", "30% 50%"), ("linen", "50% 50%"), ("leaves", "50% 50%")]
    insta = ('<section class="dl-sec"><div class="dl-sec-h"><h2>@naau_kombucha</h2><a href="#">Instagram →</a></div><div class="dl-feed">'
             + "".join(f'<div class="dl-feed-i">{C.pic(k, 600, p)}' + (f'<div class="dl-feed-stk">{sticker(SFL[j % 3])}</div>' if j in (1, 4) else '') + '</div>' for j, (k, p) in enumerate(feed)) + '</div></section>')
    return s_shell(hero + ticker + shop + howto + about + insta)

def s_product():
    content = (f'<section class="dl-pd"><div class="dl-pd-media"><div class="dl-pd-main">{sticker("［フレーバー］", "52%")}</div>'
               f'<div class="dl-pd-thumbs"><div class="dl-pd-t">{C.pic("pourbowl", 700, "50% 50%")}</div><div class="dl-pd-t">{C.pic("amber", 700, "50% 50%")}</div><div class="dl-pd-t">{C.pic("jar", 700, "35% 50%")}</div></div></div>'
               '<div class="dl-pd-info"><p class="dl-pill-l">No. 027 · 330 ml</p><h1>［フレーバー］</h1><p class="dl-price">¥［　］<span>（税込）</span></p>'
               '<p class="dl-lead">紅茶と［素材］を、酵母と酢酸菌でゆっくり発酵させました。［味わいの説明］。</p>'
               '<fieldset class="dl-opt"><legend class="dl-small">本数</legend><label><input type="radio" name="q" checked><span>1本</span></label><label><input type="radio" name="q"><span>3本セット</span></label><label><input type="radio" name="q"><span>6本セット</span></label></fieldset>'
               '<fieldset class="dl-opt"><legend class="dl-small">お届け</legend><label><input type="radio" name="d" checked><span>今回のみ</span></label><label><input type="radio" name="d"><span>2週間ごとの定期便</span></label></fieldset>'
               '<div class="dl-row"><input class="dl-qty" type="number" value="1" min="1" aria-label="数量"><button type="button" class="dl-btn" style="flex:1">カートに入れる</button></div>'
               + C.commerce("background:#F1F1EF; border-radius:14px; padding:14px 18px; font-family:var(--sans); font-size:13px; line-height:1.9")
               + f'<div>{C.accordions("#E4E4E1")}</div><p class="dl-small">※本品は清涼飲料水です。医薬品ではありません。</p></div></section>'
               '<section class="dl-sec"><div class="dl-sec-h"><h2>ほかの仕込み</h2><a href="current-home.html#shop">すべて見る →</a></div><div class="dl-grid">' + "".join(dl_card(i) for i in (1, 2, 3)) + '</div></section>')
    return s_shell(content)

# ====================================================================== IPPON
P = D["lenora"]
INK, KIN, SUMI, MUTE = "#2B2926", "#EFEBE2", "#1F1E1C", "#6E6860"

def frame(inner, pad="[[50]]", gap="[[24]]", rule=None, inner_pad="[[70]] [[60]]", just="space-between"):
    col = rule or "currentColor"
    return (f'<div class="fill" style="padding:{pad}"><div style="position:relative; height:100%; '
            f'display:flex; flex-direction:column; align-items:center; justify-content:{just}; text-align:center; padding:{inner_pad}; gap:{gap}">{inner}</div></div>')

SEAL = "#9B3A25"
SHIP = "'Shippori Mincho B1'"

def spread(words, size, extra=""):
    return (f'<div class="spread" style="position:static; width:100%; font-size:{size}; letter-spacing:.14em; {extra}">'
            + "".join(f'<span>{w}</span>' for w in words) + '</div>')

def specrows(rows, size, col, pad="[[14]]", extra=""):
    return (f'<dl class="spec-rows" style="position:static; width:100%; font-size:{size}; letter-spacing:.06em; text-align:left; border-bottom:1px solid {col}; {extra}">'
            + "".join(f'<dt style="padding:{pad} [[34]] {pad} 0; border-color:{col}; opacity:.7">{a}</dt><dd style="padding:{pad} 0; border-color:{col}">{b}</dd>' for a, b in rows) + '</dl>')

def seal(w, style="", text="一本"):
    return f'<div style="position:absolute; {style}">{K.hanko(w, text)}</div>'

# Mixed media: real paper scans under the print, real torn edges, tape cut from a scan.
TEX = "assets/textures/"
KIN_P = f"background:{KIN} url({TEX}paper-crease.jpg) center/cover; background-blend-mode:multiply"
SUMI_P = f"background:#33302C url({TEX}paper-crease.jpg) center/cover; background-blend-mode:multiply"
SLIP_P = f"background:#F7F3EA url({TEX}paper-crease.jpg) center/180%; background-blend-mode:multiply"
KRAFT_P = f"background:url({TEX}kraft.jpg) center/cover"

def torn(rw, rh, inner, width, style, edge="b"):
    """A paper piece with a real torn edge (traced from a scan) and a soft paper shadow."""
    return f'<div class="mm-drop" style="width:{width}">' + ab(rw, rh, inner, "100%", style, cls=f"flat mm-torn-{edge}") + '</div>'

def tape(left, top, w, rot):
    return f'<img class="mm-tape" src="{TEX}tape.jpg" alt="" style="left:{left}; top:{top}; width:{w}; transform:rotate({rot}deg)">'

def slip(left, top, w, ratio, inner, rot=-1.5):
    return (f'<div class="ab flat" style="left:{left}; top:{top}; width:{w}; aspect-ratio:{ratio}; {SLIP_P}; transform:rotate({rot}deg); '
            f'box-shadow:0 1px 1px rgba(0,0,0,.12), 0 3px 6px rgba(0,0,0,.08)">{inner}</div>')

def label_mm(no="027"):
    """The front label as mixed media: the mark printed on creased kinari, a typed slip taped on, the name in pencil, the seal across both."""
    return (f'<p class="mono" style="left:[[90]]; top:[[90]]; font-size:[[30]]; letter-spacing:.24em; opacity:.7">NO. {no}</p>'
            f'<p class="mono" style="right:[[90]]; top:[[90]]; font-size:[[30]]; letter-spacing:.24em; opacity:.7">330 ML</p>'
            f'<div style="left:50%; top:[[290]]; transform:translateX(-50%); width:[[700]]">{L(P, "2b2926", "100%", style="mix-blend-mode:multiply")}</div>'
            f'<p style="left:0; right:0; top:[[520]]; text-align:center; font-family:var(--lat); font-style:italic; font-size:[[58]]">kombucha</p>'
            + slip("[[150]]", "[[740]]", "[[600]]", "600/110", f'<p class="mono" style="left:0; right:0; top:50%; transform:translateY(-50%); text-align:center; font-size:[[40]]; letter-spacing:.2em">14 DAYS · 26.10.22</p>', -1.8)
            + tape("[[110]]", "[[722]]", "[[110]]", -32)
            + f'<p class="hand" style="left:[[130]]; top:[[1060]]; font-size:[[78]]; color:#5E5953; transform:rotate(-2deg)">［お名前］様</p>'
            + seal("[[170]]", "right:[[90]]; top:[[930]]; transform:rotate(-7deg); mix-blend-mode:multiply; opacity:.92"))

def side(text, pos, size="[[20]]", font="'IBM Plex Mono', monospace"):
    return (f'<span class="vt" style="position:absolute; {pos}; top:50%; transform:translateY(-50%); font-family:{font}; font-size:{size}; letter-spacing:.32em; '
            f'text-transform:uppercase; opacity:.75; white-space:nowrap">{text}</span>')

# ---------------------------------------------------------------- 手仕込み (tejikomi): black and white, linocut prints, photographs of hands; one red
# Care by hand. Prints are cut in lino (lino.py), photographs are black and white with grain, and bengara,
# the iron-oxide red of old lacquer and seals, is the one tint. Gardenia and indigo appear only on flavour seals.
import lino as LN
BLACK, BENI, KUCHI, AI, USU = "#1A1917", "#B0472B", "#D29A2E", "#4E6B7E", "#8E8880"
MIN8 = f"font-family:{SHIP}; font-weight:800"
WIDE = "font-family:Inter, sans-serif; letter-spacing:.6em; padding-left:.6em"
INTRO = ("急がず、混ぜず、足さず。naʻau は、名古屋の台所で、ひと瓶ずつ手で仕込むコンブチャ。"
         "白と黒の版画と写真に、赤をひとつ。昔ながらの手仕事を、飾らずに見せます。",
         "No rush, nothing added. naʻau is kombucha brewed by hand, one jar at a time, in a kitchen in Nagoya. "
         "Black and white, linocut prints and photographs of hands at work, with one red. Old handwork, shown as it is.")
FLAV = [("027", "camellia", BENI, "［フレーバー］"), ("028", "leaf", KUCHI, "［フレーバー］"), ("029", "moon", AI, "［限定］")]
SET = [("hand", "手", "Hand"), ("bowl", "碗", "Bowl"), ("camellia", "椿", "Camellia"), ("mortar", "鉢", "Mortar"), ("moon", "月", "Moon"), ("leaf", "茶葉", "Tea leaf")]

_wg = [0]
def wood(ink, op=.12):
    """Woodblock grain on a printed ground."""
    _wg[0] += 1
    return LN.grain(f"wg{_wg[0]}", ink, op)

def bwp(key, pos="50% 50%", w=1400):
    """A full-bleed photograph in black and white, with film grain."""
    return f'<div class="fill grain">{C.pic(key, w, pos, C.BW)}</div>'

def bwbox(key, l, t, r, b, pos="50% 50%", w=1200):
    return f'<div class="grain" style="left:{l}; top:{t}; right:{r}; bottom:{b}">{C.pic(key, w, pos, C.BW)}</div>'

def wm(col, w, sub_size, gap="[[16]]", align="center"):
    """The Lenora mark with KOMBUCHA beneath, set in Inter and widely spaced."""
    hexcol = "efebe2" if col == "light" else "2b2926"
    return (f'<div class="col" style="position:static; align-items:{align}; gap:{gap}">{L(P, hexcol, w)}'
            f'<span style="{WIDE}; font-size:{sub_size}; line-height:1">KOMBUCHA</span></div>')

def rseal(col, fl, no):
    """A round flavour seal, printed in the flavour's colour."""
    return (f'<div style="position:relative; aspect-ratio:1; color:#F4F0E8; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:[[8]]">'
            f'<svg viewBox="0 0 100 100" style="position:absolute; inset:0; width:100%; height:100%" aria-hidden="true"><circle cx="50" cy="50" r="48" fill="{col}" filter="url(#seal)"/></svg>'
            f'<span style="position:relative; display:contents">'
            f'<span class="mono" style="position:relative; font-size:[[15]]; letter-spacing:.2em">NO. {no}</span><span style="position:relative; {MIN8}; font-size:[[26]]; white-space:nowrap">{fl}</span>'
            f'<span class="mono" style="position:relative; font-size:[[13]]; letter-spacing:.3em">BY HAND</span></span></div>')

def label(no="027", prt="camellia", col=BENI, fl="［フレーバー］"):
    """Front label: kinari paper, the mark, one print large, the batch typed, the flavour seal pressed over the print."""
    return ab(3, 4, f'<div class="fill" style="{KIN_P}"></div>'
              f'<div style="left:0; right:0; top:[[90]]; mix-blend-mode:multiply">{wm("dark", "[[520]]", "[[20]]")}</div>'
              f'<div style="left:[[160]]; right:[[160]]; top:[[370]]; mix-blend-mode:multiply">{LN.PRINTS[prt]("100%", BLACK)}</div>'
              + side("Brewed by hand · Nagoya", "left:[[34]]", "[[17]]") +
              f'<div class="col mono" style="left:[[90]]; bottom:[[84]]; gap:[[10]]; font-size:[[24]]; letter-spacing:.16em"><span>NO. {no}</span><span>330 ML</span><span>14 DAYS</span></div>'
              f'<div style="right:[[80]]; bottom:[[70]]; width:[[250]]; transform:rotate(-8deg)">{rseal(col, fl, no)}</div>',
              "100%", f"color:{BLACK}", cls="flat")

def la_tile(i=0, ratio="4/5", w="58%", rot=-2):
    """A product tile: the label on a printed black ground."""
    return (f'<div class="ab flat" style="width:100%; aspect-ratio:{ratio}; background:{BLACK}">{wood("#EFEBE2", .08)}'
            f'<div style="left:50%; top:50%; width:{w}; transform:translate(-50%,-50%) rotate({rot}deg); box-shadow:0 18px 30px -12px rgba(0,0,0,.7)">{label(*FLAV[i])}</div></div>')

def p_dir():
    hero_ab = ab(16, 9, f'<div class="fill grain">{C.pic("brewjar", 1600, "50% 72%", C.BW_FLIP)}</div>'
                 + '<div class="fill" style="background:linear-gradient(180deg, rgba(0,0,0,.5), rgba(0,0,0,0) 38%, rgba(0,0,0,0) 72%, rgba(0,0,0,.55))"></div>'
                 + f'<div style="left:0; right:0; top:[[46]]; color:{KIN}">{wm("light", "[[280]]", "[[11]]", "[[10]]")}</div>'
                 + f'<p class="vt" style="right:[[46]]; top:[[46]]; {MIN8}; font-size:[[64]]; letter-spacing:.18em; color:{BENI}">手仕込み</p>'
                 + f'<div class="row" style="right:[[46]]; top:[[392]]; gap:[[14]]">' + "".join(f'<div style="width:[[40]]">{LN.PRINTS[k]("100%", KIN)}</div>' for k, _, _ in SET) + '</div>'
                 + f'<div class="row mono" style="left:[[46]]; right:[[46]]; bottom:[[36]]; justify-content:space-between; font-size:[[12]]; letter-spacing:.3em; color:{KIN}">'
                   f'<span>NAʻAU KOMBUCHA</span><span>BREWED BY HAND · NAGOYA</span><span>NO. 027</span></div>',
                 "100%", f"background:{BLACK}", cls="flat")
    hero = (f'<header class="wrap la-hero"><p class="eyebrow">Concept A · Lenora</p>{hero_ab}'
            f'<div class="la-intro"><h1>{C.T("手仕込み", "Tejikomi, brewed by hand")}</h1><p>{C.T(*INTRO)}</p></div></header>')

    cells = "".join(f'<div class="col" style="position:static; align-items:center; gap:[[14]]"><div style="position:static; width:100%">{LN.PRINTS[k]("100%", BLACK)}</div>'
                    f'<span class="mono" style="position:static; font-size:[[17]]; letter-spacing:.22em">{jp} · {en.upper()}</span></div>' for k, jp, en in SET)
    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 5, wood(KIN, .1) + f'<div style="left:[[210]]; right:[[210]]; top:[[170]]">{LN.hand("100%", KIN)}</div>'
              f'<div style="left:0; right:0; bottom:[[170]]">{wm("light", "[[440]]", "[[17]]")}</div>', "100%", f"background:{BLACK}; color:{KIN}", cls="flat"),
           "The emblem", "An open hand holding the drop from the wordmark, cut in lino."),
        pf(ab(4, 5, bwp("clay", "50% 55%") + f'<p style="left:[[70]]; top:[[80]]; {MIN8}; font-size:[[118]]; line-height:1.3; color:{BENI}">手で、<br>つくる。</p>'
              f'<div style="left:[[70]]; bottom:[[80]]; color:{KIN}">{wm("light", "[[330]]", "[[13]]", align="flex-start")}</div>', "100%", f"background:{BLACK}", cls="flat"),
           "With photographs", "Black-and-white photographs of hands at work; the type over them in bengara red."),
        pf(ab(4, 5, f'<div class="fill" style="{KIN_P}"></div><div style="left:[[80]]; right:[[80]]; top:50%; transform:translateY(-50%); display:grid; grid-template-columns:repeat(3,1fr); gap:[[80]] [[50]]; mix-blend-mode:multiply">{cells}</div>',
              "100%", f"color:{BLACK}", cls="flat"),
           "The print set", "Six blocks: hand, bowl, camellia, mortar, moon and tea leaf. Each flavour takes one."),
    ]) + '</div>'
    pal = (chips([("Sumi", BLACK, "Ground, prints, type", 3), ("Kinari", KIN, "Paper and labels", 3), ("Bengara", BENI, "The one tint: type over photographs, seals", 1.2),
                  ("Usuzumi", USU, "Captions", .8), ("Gardenia", KUCHI, "Flavour seal only", .6), ("Indigo", AI, "Flavour seal only", .6)]),
           "Palette A, 手仕込み: black and white like a print, with bengara, the iron-oxide red of old lacquer and seals. Gardenia and indigo mark flavours only.")
    seal_demo = ab(1, 1, f'<div style="left:[[60]]; right:[[60]]; top:[[60]]">{rseal(BENI, "［フレーバー］", "027")}</div>', "96px", "background:transparent", cls="flat")
    typ = spec([("Wordmark", f'<div style="color:{KIN}">{wm("light", "170px", "8px", "8px", "flex-start")}</div>', "Lenora with a water-drop ʻokina; KOMBUCHA in Inter, widely spaced"),
                ("Japanese", f'<p style="{MIN8}; font-size:24px; line-height:1.7">手で仕込む、<br>古い知恵。</p>', "Shippori Mincho B1, ExtraBold"),
                ("Details", '<p class="mono" style="font-size:15px; letter-spacing:.08em; line-height:1.9">NO. 027 · 330 ML<br>FERMENTED 14 DAYS</p>', "IBM Plex Mono, typed"),
                ("Seal", seal_demo, "One round seal per flavour, in its colour")])

    lw = fitw(1, .75, .82)
    front = f'<div style="width:{lw}">{label()}</div>'
    back = ab(3, 4, f'<div class="fill" style="{KIN_P}"></div>' + frame(f'<dl style="position:static; text-align:left; font-family:var(--jp); font-size:[[40]]; line-height:1.75; column-gap:[[36]]; width:100%">{C.ichi_rows()}</dl>'
                          f'<p class="jp" style="position:static; font-size:[[38]]; line-height:1.7; text-align:left">{C.HANDLING}</p>'
                          + specrows([("No.", "＿＿＿"), ("瓶詰め", "＿＿＿")], "[[32]]", "rgba(26,25,23,.45)", "[[12]]"), inner_pad="[[80]] [[64]]"), lw, f"color:{BLACK}")
    notes_box = "".join(f'<div style="position:static"><p style="position:static; opacity:.6; margin-bottom:[[6]]">{a}</p><p style="position:static">{b}</p></div>'
                        for a, b in (("TASTE / 味わい", "［　］"), ("BEST / 飲みごろ", "よく冷やして、ゆっくりと。"), ("MADE / 仕込み", "名古屋で、手で。14日。")))
    gift = ab(2, 3, wood(KIN, .12) + f'<div style="left:[[-90]]; right:[[110]]; bottom:[[-170]]">{LN.hand("100%", KIN)}</div>'
              f'<div style="left:[[80]]; top:[[90]]">{wm("light", "[[470]]", "[[18]]", align="flex-start")}</div>'
              f'<p class="vt" style="right:[[80]]; top:[[90]]; {MIN8}; font-size:[[118]]; letter-spacing:.16em; color:{BENI}">手仕込み</p>'
              f'<div class="col mono" style="left:[[80]]; top:[[400]]; width:[[520]]; gap:[[30]]; font-size:[[24]]; line-height:1.6; letter-spacing:.06em">{notes_box}</div>',
              "54%", f"background:{BLACK}; color:{KIN}", cls="flat")
    trio = "".join(f'<div style="width:23%; transform:rotate({r}deg); box-shadow:0 18px 30px -12px rgba(0,0,0,.7)">{label(*f)}</div>' for f, r in zip(FLAV, (-2, 1.5, -1)))
    pack = (pf(trio, "The range", "One print and one seal colour per flavour; the mark, the batch and the days typed the same on each.", "21/9", pstyle="gap:4%") +
            '<div class="grid g3" style="margin-top:clamp(20px,3vw,36px)">' +
            pf(front, "Front label", "Kinari paper. The print is pressed by hand; the round seal goes on last, over the print.", "1/1") +
            pf(back, "Back label", "一括表示 in the legal order, 8 pt minimum, with the batch and bottling date written in.", "1/1") +
            pf(gift, "Gift box", "Black board with a wood grain, the hand cropped by the edge, 手仕込み in bengara, and tasting notes typed.", "1/1") + '</div>')

    a5w = fitw(4 / 3, 148 / 210, .82)
    fl_f = ab(148, 210, bwbox("grind", 0, 0, 0, "[[600]]", "50% 42%")
              + f'<p style="left:[[70]]; top:[[860]]; {MIN8}; font-size:[[128]]; line-height:1.2; color:{BENI}">仕込みの会</p>'
              f'<p style="left:[[70]]; top:[[1036]]; font-family:{SHIP}; font-weight:700; font-size:[[38]]; line-height:1.75">手で仕込む、昔ながらのコンブチャ。<br>お茶を淹れ、母を移し、待つまでを。</p>'
              f'<div class="row mono" style="left:[[70]]; right:[[70]]; bottom:[[70]]; justify-content:space-between; align-items:flex-end; font-size:[[22]]; letter-spacing:.2em"><span>［月日］ · 名古屋</span>{L(P, "efebe2", "[[280]]")}</div>',
              a5w, f"background:{BLACK}; color:{KIN}")
    fl_b = ab(148, 210, f'<div class="fill" style="{KIN_P}"></div>' + frame(spread(["Details", "仕込みの会"], "[[26]]", f"color:{MUTE}") + f'<div style="width:[[220]]">{LN.mortar("100%", BLACK)}</div>' +
                              specrows([("日時", "［月日（曜）時間］"), ("場所", "名古屋市［　］"), ("定員", "［　］名（先着順）"), ("内容", "仕込みの体験と試飲"), ("参加費", "¥［　］（税込）"), ("申込", "Instagram DM / LINE")], "[[34]]", "rgba(26,25,23,.4)", "[[20]]", "font-family:var(--jp)"),
                              pad="[[56]]", inner_pad="[[100]] [[80]] [[100]]"), a5w, f"color:{BLACK}")
    cw = fitw(4 / 3, 91 / 55, .34)
    card_f = ab(91, 55, wood(KIN, .12) + f'<div style="left:[[80]]; top:50%; transform:translateY(-50%); width:[[230]]">{LN.hand("100%", KIN)}</div>'
                f'<div style="right:[[90]]; top:50%; transform:translateY(-50%); color:{KIN}">{wm("light", "[[420]]", "[[18]]")}</div>', cw, f"background:{BLACK}; color:{KIN}")
    card_b = ab(91, 55, f'<div class="fill" style="{KIN_P}"></div>'
                f'<div class="col mono" style="left:[[90]]; top:50%; transform:translateY(-50%); gap:[[16]]; font-size:[[26]]; letter-spacing:.16em"><span>NAʻAU KOMBUCHA</span><span>名古屋市［　］</span><span>@naau_kombucha</span><span>［営業日・時間］</span></div>'
                f'<div style="right:[[90]]; top:50%; transform:translateY(-50%) rotate(-8deg); width:[[220]]">{rseal(BENI, "手仕込み", "027")}</div>', cw, f"color:{BLACK}")
    prt = ('<div class="grid g2">' + pf(fl_f + fl_b, "A5 workshop flyer", "A black-and-white photograph above, the event in bengara below; details typed on kinari on the back.", "4/3") +
           pf(card_f + card_b, "Shop card, 91 × 55 mm", "The hand on black; the back typed, with a seal.", "4/3", pstyle="flex-direction:column; gap:7%") + '</div>')

    posts = [
        (ab(3, 4, bwp("care", "50% 50%")
                  + f'<p style="left:0; right:0; top:[[60]]; text-align:center; {MIN8}; font-size:[[128]]; letter-spacing:.06em; line-height:1; color:{BENI}">ひと瓶ずつ、</p>'
                  + f'<p style="left:0; right:0; bottom:[[60]]; text-align:center; {MIN8}; font-size:[[118]]; letter-spacing:.06em; line-height:1; color:{BENI}">手で仕込む。</p>'
                  + side("naʻau kombucha", "left:[[34]]", "[[20]]").replace("opacity:.75", f"opacity:1; color:{KIN}")
                  + side("Brewed by hand", "right:[[34]]", "[[20]]").replace("opacity:.75", f"opacity:1; color:{KIN}"),
                  "100%", f"background:{BLACK}", cls="flat post"),
         "Photograph post", "A black-and-white photograph framed by one line in bengara, top and bottom; small type down each side."),
        (ab(3, 4, wood(KIN, .1) + f'<div style="left:[[160]]; right:[[-260]]; bottom:[[-200]]">{LN.camellia("100%", KIN)}</div>'
                  f'<div class="col mono" style="left:[[80]]; top:[[90]]; gap:[[12]]; font-size:[[28]]; letter-spacing:.18em; color:{KIN}"><span>NO. 027</span><span>CAMELLIA</span><span>14 DAYS</span></div>'
                  f'<p style="left:[[80]]; top:[[330]]; {MIN8}; font-size:[[62]]; line-height:1.5; color:{KIN}">椿の咲くころに、<br>仕込みました。</p>'
                  f'<div style="left:[[80]]; bottom:[[90]]; width:[[230]]; transform:rotate(-8deg)">{rseal(BENI, "［フレーバー］", "027")}</div>',
                  "100%", f"background:{BLACK}", cls="flat post"),
         "Batch post", "The flavour's print, large and cropped; the batch typed; its seal."),
        (ab(3, 4, bwp("mist", "50% 40%") + f'<div style="right:[[80]]; top:[[90]]; width:[[280]]">{LN.moon("100%", BLACK)}</div>'
                  f'<p class="vt" style="left:[[90]]; top:[[90]]; {MIN8}; font-size:[[84]]; letter-spacing:.16em; color:{BLACK}">急がずに、十四日。</p>'
                  f'<div style="right:[[80]]; bottom:[[80]]; color:{KIN}">{wm("light", "[[280]]", "[[12]]", align="flex-end")}</div>',
                  "100%", f"background:{BLACK}", cls="flat post"),
         "Photograph and print", "A print laid over the photograph: the moon above the forest, and one vertical line."),
    ]
    story = ab(9, 16, bwbox("kettle", 0, 0, 0, "[[700]]", "50% 40%")
               + f'<p style="left:[[70]]; top:[[960]]; {MIN8}; font-size:[[96]]; color:{BENI}">今週の仕込み</p>'
               + "".join(f'<div class="row" style="left:[[70]]; right:[[70]]; top:[[{1130 + i * 110}]]; gap:[[30]]; border-top:1px solid rgba(239,235,226,.25); padding-top:[[24]]">'
                         f'<span style="position:static; width:[[40]]; aspect-ratio:1; border-radius:50%; background:{c}"></span>'
                         f'<span class="mono" style="position:static; font-size:[[30]]; letter-spacing:.16em; color:{KIN}">NO. {n}</span><span style="position:static; font-family:{SHIP}; font-weight:700; font-size:[[40]]; color:{KIN}">{f}</span></div>'
                         for i, (n, _, c, f) in enumerate(FLAV))
               + f'<div style="left:0; right:0; bottom:[[90]]; color:{KIN}">{wm("light", "[[360]]", "[[14]]")}</div>',
               "100%", f"background:{BLACK}", cls="flat story")
    nts = notes(["Kombucha is a soft drink: no wording of effects on the body, here or in posts. 手仕込み says how it is made, nothing more.",
                 "Borrowed as principles, not copied: black-and-white photography with one spot colour for type, and a set of block prints, one per product, each with its own coloured seal. Ours: our own six prints, vertical Japanese, and bengara from lacquer and seals.",
                 "The prints are drawn for this concept; final versions would be cut in real lino, printed by hand and scanned. The photographs are stand-ins from Unsplash, to be replaced by a shoot of hands at work in the kitchen.",
                 "The wordmark is shown from your Lenora setting. License Lenora with Superior Type’s Logo and Merchandise add-ons, then reset it as vector."])
    direction_page(P, hero, idn, pal, typ, pack, prt, social("lenora", posts, story), nts)

# ---------------------------------------------------------------- the Lenora website: a quiet stone-grey shop around black-and-white photographs
# Small mono type spread across a grid, numbered batches, a justified manifesto, light taken out of focus,
# and the wordmark set huge at the foot. The brand stays black, white and bengara; the site ground is stone.
NAMES = {"camellia": ("椿", "Camellia"), "leaf": ("茶葉", "Tea leaf"), "moon": ("月", "Moon")}

def stone_tile(i=0, w="50%", ground="#D9D6CF"):
    """A batch as a product shot: its label standing on stone."""
    return (f'<div class="lx-tile" style="background:{ground}"><div style="width:{w}; box-shadow:0 18px 30px -18px rgba(26,25,23,.45)">{label(*FLAV[i])}</div></div>')

def p_shell(content, overlay=False):
    mark = "efebe2" if overlay else "2b2926"
    links = (("lenora-product.html", "Shop"), ("lenora-home.html#craft", "手仕込み"), ("lenora-home.html#workshop", "Workshop"))
    nav = (f'<header class="lx-head{" ov" if overlay else ""}"><nav class="lx-nav mono" aria-label="Shop">'
           f'<a href="lenora-home.html" aria-label="naʻau home">{L(P, mark, "92px")}</a>'
           + "".join(f'<a href="{h}">{t}</a>' for h, t in links) + '<span class="lx-hide">JPY ¥</span><a href="#">Cart (0)</a></nav></header>')
    cols = [("Shop", ("This week", "All batches", "Gift set", "Workshop")), ("naʻau", ("手仕込み", "Story", "Journal", "Instagram")),
            ("Help", ("配送・返品", "特定商取引法に基づく表記", "プライバシーポリシー", "お問い合わせ"))]
    foot = (f'<footer class="lx-foot"><div class="lx-foot-in"><div class="lx-foot-mark">{L(P, "2b2926", "100%")}</div>'
            '<div class="lx-foot-cols mono">' + "".join(f'<div><p>{h}</p>' + "".join(f'<a href="#">{x}</a>' for x in xs) + '</div>' for h, xs in cols) + '</div></div>'
            f'<div class="lx-foot-base mono"><span>© 2026 naʻau kombucha · concept mockup</span><span>Brewed by hand in Nagoya</span></div></footer>')
    return f'<div class="shop lxs">{nav}<main>{content}</main>{foot}</div>'

def lx_card(i):
    no, prt, col, fl = FLAV[i]
    jp, en = NAMES[prt]
    return (f'<a class="lx-card" href="lenora-product.html"><span class="mono lx-no">No. {no}</span>{stone_tile(i)}'
            f'<div class="lx-meta"><p><span class="lx-en">{en.upper()}</span> <b>{jp}</b></p><span class="mono">¥［　］</span></div>'
            f'<p class="lx-desc"><span class="lx-dot" style="background:{col}"></span>{fl} · 14 days · 330 ml</p></a>')

def p_home():
    caps_ = ("", "", "", "Now brewing — No. 027<br>椿 · Camellia", "Brewed by hand<br>in Nagoya", '<a href="#shop">Shop all</a>')
    hero = (f'<section class="lx-hero grain">{C.pic("brewjar", 2000, "50% 72%", C.BW_FLIP)}'
            '<div class="lx-caps mono">' + "".join(f'<span>{c}</span>' for c in caps_) + '</div>'
            f'<div class="lx-prints">' + "".join(f'<div>{LN.PRINTS[k]("100%", "#EFEBE2")}</div>' for k, _, _ in SET) + '</div>'
            f'<p class="vt lx-hero-v">手仕込み</p></section>')
    grid = (f'<section class="lx-sec" id="shop"><div class="lx-row mono"><span>今週の仕込み · This week</span><span>3 batches · ¥［　］ each</span></div>'
            '<div class="lx-grid">' + "".join(lx_card(i) for i in range(3))
            + f'<div class="lx-card lx-photo"><span class="mono lx-no">Nagoya, 6:00</span><div class="lx-tile grain" style="padding:0">{C.pic("mist", 900, "50% 40%", C.BW)}</div>'
              '<p class="lx-desc">朝いちばんに、瓶をのぞく。</p></div></div></section>')
    manifesto = ("名古屋の小さな台所で、お茶を淹れ、母を移し、十四日を待ちます。急がず、混ぜず、足さず。"
                 "一本ずつ、手で仕込み、手で瓶に詰め、手で版を刷る。昔ながらのやり方を、今日の食卓に。naʻau は、その手から生まれるコンブチャです。")
    man = (f'<section class="lx-man" id="craft"><div class="lx-man-pic grain">{C.pic("grind", 1600, "50% 45%", C.BW)}<div class="lx-man-print">{LN.hand("100%", "#EFEBE2")}</div></div>'
           f'<div class="lx-man-txt"><p class="mono lx-label">手仕込み · By hand</p><p class="lx-just">{manifesto}</p>'
           f'<div class="lx-man-foot"><p class="vt lx-v">手仕込み</p><a class="lx-btn mono" href="#workshop">Workshop →</a></div></div></section>')
    spots = [(0, 6, 14, -6), (1, 44, 46, 5), (2, 74, 8, -3)]
    tags = [("椿 · Camellia", 9, 52), ("No. 027", 22, 9), ("茶葉", 40, 30), ("Tea leaf", 58, 88), ("月", 84, 62), ("No. 029", 70, 84),
            ("14 days", 30, 76), ("手仕込み", 92, 20), ("Moon", 88, 44), ("Nagoya", 50, 12)]
    scatter = (f'<section class="lx-scatter" aria-label="This week’s batches, out of focus">'
               + "".join(f'<div class="lx-sc" style="left:{x}%; top:{y}%; transform:rotate({r}deg)"><div class="lx-sc-in">{label(*FLAV[i])}</div></div>' for i, x, y, r in spots)
               + "".join(f'<span class="mono lx-sc-t" style="left:{x}%; top:{y}%">{t}</span>' for t, x, y in tags)
               + f'<div class="lx-sc-mark">{L(P, "2b2926", "100%")}</div></section>')
    work = (f'<section class="lx-ed" id="workshop"><div class="lx-ed-txt"><p class="mono lx-label">Workshop · 仕込みの会</p>'
            f'<h2>手で仕込む、<br>昔ながらのコンブチャ。</h2>'
            f'<p class="jp">お茶を淹れ、母を移し、待つまでを一緒に。少人数で、名古屋の台所から。</p>'
            f'<dl class="lx-dl mono"><dt>Date</dt><dd>［月日］</dd><dt>Place</dt><dd>名古屋市［　］</dd><dt>Seats</dt><dd>［　］</dd><dt>Fee</dt><dd>¥［　］</dd></dl>'
            f'<a class="lx-btn mono" href="#">予約する →</a></div><div class="lx-ed-pic grain">{C.pic("clay", 1800, "50% 50%", C.BW)}</div></section>')
    return p_shell(hero + grid + man + scatter + work, overlay=True)

def p_product():
    rows = "".join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in (("No.", "027"), ("Tea", "［茶葉］"), ("Fermented", "14 days"), ("Taste", "［　］"), ("Best", "よく冷やして、ゆっくりと"), ("Volume", "330 ml")))
    thumbs = (f'<div class="lx-tile grain" style="padding:0">{C.pic("mother", 700, "50% 50%", C.BW)}</div>'
              f'<div class="lx-tile grain" style="padding:0">{C.pic("whisk", 700, "50% 50%", C.BW)}</div>'
              f'<div class="lx-tile" style="background:#EFEBE2"><div style="width:58%">{LN.camellia("100%", BLACK)}</div></div>')
    content = (f'<section class="lx-pd"><div class="lx-pd-media">{stone_tile(0, "46%")}<div class="lx-pd-thumbs">{thumbs}</div></div>'
               f'<div class="lx-pd-info"><p class="mono lx-crumb"><a href="lenora-home.html#shop">Shop</a> / No. 027</p>'
               f'<h1><span class="lx-en">CAMELLIA</span> <b>椿</b></h1><p class="jp" style="font-size:18px">［フレーバー］</p>'
               f'<p class="jp lx-pd-p">椿の咲くころに仕込んだ、027番。名古屋で、手で、14日。ラベルの版は一枚ずつ手で刷り、最後に印を押してお届けします。</p>'
               f'<dl class="lx-dl mono">{rows}</dl>'
               f'<div class="lx-buy"><p class="lx-price">¥［　］<small>（税込）</small></p><input type="number" value="1" min="1" aria-label="数量"><button type="button" class="lx-btn mono lx-solid">カートに入れる</button></div>'
               + C.commerce("border-top:1px solid #C9C5BD; padding:14px 0; font-size:13px; line-height:1.9") + f'<div>{C.accordions("#C9C5BD")}</div>'
               f'<p class="jp" style="font-size:11px; color:{MUTE}">※本品は清涼飲料水です。医薬品ではありません。</p></div></section>'
               f'<section class="lx-sec"><div class="lx-row mono"><span>ほかの仕込み · Also this week</span><a href="lenora-home.html#shop">Shop all →</a></div>'
               '<div class="lx-grid lx-grid-2">' + lx_card(1) + lx_card(2) + '</div></section>')
    return p_shell(content)

# ====================================================================== MA
M = D["ogg"]
MI, GO, ODO, NERI, ODT = "#3A3631", "#FAF7F1", "#C39143", "#EDE4CD", "#8A6A3A"
BENI, PAPER = "#B8352B", "#E9E6E0"

def note(text, w, rot=-3, size="[[40]]", pad="[[40]]", extra=""):
    return (f'<div style="width:{w}; padding:{pad}; background:{GO}; transform:rotate({rot}deg); box-shadow:0 1px 2px rgba(58,54,49,.14), 0 10px 22px rgba(58,54,49,.10); {extra}">'
            f'<p class="hand" style="font-size:{size}; line-height:1.85; color:{MI}">{text}</p></div>')

def tag(text, w, size):
    return (f'<div style="width:{w}; aspect-ratio:3/5.2; background:{NERI}; clip-path:polygon(18% 0,82% 0,100% 11%,100% 100%,0 100%,0 11%); position:relative; container-type:inline-size; box-shadow:0 0 0 1px rgba(0,0,0,.03)">'
            f'<span style="position:absolute; top:7%; left:50%; width:9%; aspect-ratio:1; transform:translateX(-50%); border-radius:50%; background:var(--plate)"></span>'
            f'<p class="hand vt" style="position:absolute; right:22%; top:22%; font-size:{size}; line-height:1.9; color:{MI}">{text}</p></div>')

def badge(w, ink=MI, centre=None):
    return K.kakuin(w, ("名古屋", "手仕込"), ink)

def notebook(width, style=""):
    """The fermentation slip: the batch's fourteen days as a timeline, marked in red pen."""
    days = [(1, "仕込み", ""), (4, "", "膜が張ってきた"), (7, "", "酸味が出てきた"), (10, "", ""), (14, "瓶詰め", "やさしい酸味。")]
    top, bot = 330, 1300
    y = lambda d: top + (d - 1) / 13 * (bot - top)
    marks = "".join(f'<div style="left:[[248]]; top:[[{y(d) - 14:.0f}]]; width:[[28]]; aspect-ratio:1; border-radius:50%; background:{MI}"></div>'
                    f'<p class="mono" style="left:[[90]]; top:[[{y(d) - 22:.0f}]]; width:[[130]]; text-align:right; font-size:[[30]]">DAY {d:02d}</p>'
                    + (f'<p class="mono" style="left:[[310]]; top:[[{y(d) - 22:.0f}]]; font-size:[[30]]; opacity:.7">{a}</p>' if a else "")
                    + (f'<p class="pen" style="left:[[{460 if a else 310}]]; top:[[{y(d) - 30:.0f}]]; font-size:[[44]]; transform:rotate(-2deg)">{b}</p>' if b else "")
                    for d, a, b in days)
    return ab(105, 148,
              f'<p class="mono" style="left:[[90]]; top:[[90]]; font-size:[[28]]; letter-spacing:.1em">NAʻAU · 発酵メモ</p>'
              f'<p style="right:[[90]]; top:[[70]]; font-family:var(--lat); font-size:[[110]]; line-height:1">027</p>'
              f'<p class="hand" style="left:[[90]]; top:[[160]]; font-size:[[44]]">［フレーバー］· 紅茶と［素材］</p>'
              f'<div style="left:[[260]]; top:[[{top}]]; height:[[{bot - top}]]; width:[[3]]; background:{MI}"></div>{marks}'
              f'<div style="left:[[460]]; top:[[{y(14) + 34:.0f}]]; width:[[300]]; height:[[5]]; background:{BENI}; border-radius:[[3]]; transform:rotate(-2deg)"></div>'
              f'<div style="right:[[90]]; bottom:[[90]]; width:[[200]]; transform:rotate(-6deg)">{badge("100%")}</div>'
              f'<div style="right:[[110]]; top:[[420]]; width:[[230]]">{K.jar("100%", MI)}</div>',
              width, f"background:{GO}; color:{MI}; {style}")

# ---------------------------------------------------------------- 間, the pause, made a little more exclusive
# What stays: gofun and ōdo, vertical Japanese, the hand and red pen, the seal, the prints.
# What is added: one deep board colour per flavour, a photograph framed like a window, photographs out of
# focus for mood, overlapping cards, and the mark set large enough to be cropped.
KAKI, KOKE, KUROCHA = "#8E4B32", "#69704F", "#2A211C"   # persimmon tannin, moss, dark tea
WORDS = ("聴く", "待つ", "味わう")
OFL = [("［フレーバー］", ODO, "amber", "50% 55%", MI, "3a3631"), ("［フレーバー］", KAKI, "hoshigaki", "50% 40%", GO, "faf7f1"),
       ("［限定］", KOKE, "moss", "50% 50%", GO, "faf7f1")]
ITAL = "font-family:var(--lat); font-style:italic"
CAPS = "font-family:Inter, sans-serif; text-transform:uppercase"

def win(key, l, t, r, b, pos="50% 50%", w=900, z=1):
    """A photograph framed like a window, with film grain."""
    return f'<div class="grain" style="left:{l}; top:{t}; right:{r}; bottom:{b}; z-index:{z}">{C.pic(key, w, pos)}</div>'

def mood(key, pos="50% 50%"):
    """A photograph taken out of focus, for mood: colour and light, nothing to read."""
    return (f'<div class="fill grain mood">{C.pic(key, 600, pos, "filter:blur(18px) saturate(1.15); transform:scale(1.2)")}</div>')

def box(i=0, w="100%"):
    """Front of the bottle box: a deep board per flavour, three words, a framed photograph, the mark large."""
    fl, bg, key, pos, fg, mk = OFL[i]
    return ab(3, 4, f'<div class="row" style="left:[[90]]; right:[[90]]; top:[[78]]; justify-content:space-between; font-family:var(--jp); font-size:[[30]]; letter-spacing:.3em">'
              + "".join(f'<span>{x}</span>' for x in WORDS) + '</div>'
              + win(key, "[[90]]", "[[170]]", "[[90]]", "[[520]]", pos)
              + f'<p style="left:[[90]]; right:[[90]]; top:[[470]]; z-index:2; text-align:center; font-family:var(--jp); font-size:[[34]]; letter-spacing:.3em; color:#FAF7F1; text-shadow:0 0 [[24]] rgba(0,0,0,.45)">{fl}</p>'
              f'<div style="left:[[90]]; right:[[90]]; top:[[880]]">{L(M, mk, "100%")}</div>'
              f'<div class="row" style="left:[[90]]; right:[[90]]; bottom:[[64]]; justify-content:space-between; align-items:baseline">'
              f'<span style="{CAPS}; font-size:[[22]]; letter-spacing:.3em">330 ml · Nagoya</span><span class="hand" style="font-size:[[36]]">10/22</span></div>',
              w, f"background:{bg}; color:{fg}", cls="flat")

def m_dir():
    hero_ab = ab(16, 9, f'<div style="left:[[46]]; top:[[60]]; width:[[340]]">{L(M, "3a3631", "100%")}</div>'
                 f'<p style="left:[[50]]; top:[[200]]; {ITAL}; font-size:[[20]]; line-height:1.5">a pause, bottled in Nagoya</p>'
                 f'<div class="row" style="left:[[50]]; bottom:[[56]]; gap:[[36]]; font-family:var(--jp); font-size:[[15]]; letter-spacing:.3em">' + "".join(f'<span>{x}</span>' for x in WORDS) + '</div>'
                 f'<div class="ab flat" style="left:[[560]]; top:[[50]]; width:[[300]]; height:[[400]]; background:{ODO}"></div>'
                 + win("shoji", "[[420]]", "[[110]]", "[[290]]", "[[60]]", "45% 50%", 1200, 2)
                 + f'<p class="vt" style="right:[[46]]; top:[[60]]; font-family:var(--jp); font-size:[[22]]; letter-spacing:.34em; line-height:2">からだの声に、耳を澄ます。</p>'
                 f'<div style="left:[[250]]; top:[[300]]; z-index:3">' + note("今日もゆっくり。", "[[205]]", rot=-3, size="[[17]]", pad="[[18]] [[20]]") + '</div>',
                 "100%", f"background:{GO}; color:{MI}", cls="flat")
    hero = (f'<header class="wrap og-hero"><p class="eyebrow">Concept B · Ogg</p>{hero_ab}'
            f'<div class="og-intro"><h1>{C.T("間", "The pause")}</h1><p>{C.T("軽やかで、手づくりのまま、少し特別に。縦組みの日本語と手書きはそのままに、フレーバーごとの深い色、窓のように切り取った写真、ピントを外した光を加えます。開ける前に、ひと呼吸。", "Airy and hand-made, made a little more exclusive. Vertical Japanese and handwriting stay; we add one deep colour per flavour, photographs framed like windows, and light taken out of focus. A breath before you open the bottle.")}</p></div></header>')

    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 5, f'<p class="vt jp" style="right:[[80]]; top:[[80]]; font-size:[[40]]; letter-spacing:.26em; line-height:2; white-space:nowrap">からだの声に、耳を澄ます。</p><div style="left:[[80]]; bottom:[[80]]">{L(M, "3a3631", "[[360]]")}</div>', "100%", f"background:{GO}; color:{MI}", cls="flat"),
           "Quiet", "A small mark low, vertical text high, air between. The default."),
        pf(box(0), "Window", "A photograph framed on a deep board, three words above, the mark large below."),
        pf(ab(4, 5, mood("glow") + f'<div style="left:0; right:0; top:46%; text-align:center; color:#FAF7F1"><p style="font-family:var(--jp); font-size:[[46]]; letter-spacing:.2em">開ける前に、</p>'
              f'<p style="{ITAL}; font-size:[[54]]; margin-top:[[6]]">take a breath.</p></div><div style="left:[[80]]; right:[[80]]; bottom:[[80]]">{L(M, "faf7f1", "[[240]]")}</div>', "100%", f"background:{KUROCHA}", cls="flat"),
           "Mood", "Light taken out of focus; one small line in Japanese, one in italic."),
    ]) + '</div>'
    idn += ('<div class="sub"><h3>Prints and seal</h3><p>Cut from lino and printed by hand: what is in the jar, and the days it takes. A square seal closes every bag.</p></div><div class="grid g-wide">'
            + pf(ab(2.4, 1, "".join(f'<div class="ab flat" style="left:[[{50 + i * 184}]]; top:[[60]]; width:[[164]]; aspect-ratio:1; background:{NERI}"><div style="left:[[150]]; top:[[150]]; right:[[150]]; bottom:[[150]]">{K.MOTIFS[k]("100%", MI)}</div></div>'
                                     f'<p class="mono" style="left:[[{50 + i * 184}]]; top:[[240]]; width:[[164]]; text-align:center; font-size:[[13]]; letter-spacing:.14em">{lab}</p>'
                                     for i, (k, lab) in enumerate((("jar", "JAR"), ("scoby", "SCOBY"), ("leaf", "TEA"), ("bubbles", "FIZZ"), ("bottle", "BOTTLE")))) +
                    f'<div style="left:[[60]]; right:[[60]]; top:[[300]]">{K.calendar("100%", MI, 14, 14)}</div>',
                    "100%", f"background:{ODO}; color:{MI}", cls="flat"), "The print set", "Five blocks for what is in the jar, each printed on its own square; a waxing moon for the fourteen days.")
            + pf(ab(1.2, 1, f'<div style="left:50%; top:50%; transform:translate(-50%,-50%); width:[[620]]">{badge("100%")}</div>', "100%", f"background:{NERI}; color:{MI}", cls="flat"),
                 "The seal", "名古屋 · 手仕込: brewed by hand in Nagoya, as a square seal.")
            + '</div>')
    pal = (chips([("Gofun", GO, "Ground", 3), ("Ink", MI, "Text · 11.2:1", 2), ("Ōdo", ODO, "Flavour board, blocks", 1.4), ("Kakishibu", KAKI, "Flavour board", 1.2),
                  ("Koke", KOKE, "Flavour board", 1.2), ("Kurocha", KUROCHA, "Night: mood posts, the gift box", 1), ("Neri", NERI, "Cards, tags", 1), ("Beni pen", BENI, "The red pen", .6)]),
           "Palette D, deepened: gofun and ink for every day; ōdo, kakishibu and koke give each flavour its own board, like persimmon tannin and moss; kurocha, dark tea, for the evening pieces. The red pen stays for the notes.")
    typ = spec([("Wordmark", L(M, "3a3631", "170px"), "Ogg, set large enough to crop on boxes and posters"),
                ("Japanese", '<p class="vt jp" style="font-size:20px; letter-spacing:.3em; line-height:2; height:150px">からだの声に、耳を澄ます。</p>', "Zen Old Mincho, set vertically"),
                ("Small lines", f'<p style="font-family:var(--jp); font-size:15px; letter-spacing:.3em">聴く　待つ　味わう</p><p style="{ITAL}; font-size:22px">take a breath.</p><p style="{CAPS}; font-size:11px; letter-spacing:.3em">330 ml · Nagoya</p>', "Spaced Mincho, EB Garamond italic, Inter capitals"),
                ("Hand", '<p class="hand" style="font-size:22px; line-height:1.6">今日もゆっくり。</p><p class="pen" style="font-size:24px; transform:rotate(-2deg)">10/22 やさしい酸味！</p>', "The hand and red pen (stand-ins: Klee One, Yomogi)")])

    band = ab(2.6, 1, f'<span class="vt jp" style="left:[[70]]; top:50%; transform:translateY(-50%); font-size:[[130]]; line-height:1">間</span>'
              f'<div class="col" style="left:[[230]]; right:[[200]]; top:50%; transform:translateY(-50%); align-items:center; gap:[[16]]">{L(M, "3a3631", "100%")}<span class="hand" style="font-size:[[48]]">［フレーバー］</span></div>'
              f'<span class="vt hand" style="right:[[70]]; top:50%; transform:translateY(-50%); font-size:[[40]]; white-space:nowrap">10/22</span>', "84%")
    back = ab(2.6, 1, f'<dl style="left:[[60]]; top:[[50]]; width:[[560]]; font-family:var(--sans); font-size:[[27]]; line-height:1.65; column-gap:[[30]]">{C.ichi_rows()}</dl>'
              f'<p style="right:[[60]]; top:[[50]]; width:[[290]]; font-family:var(--sans); font-size:[[27]]; line-height:1.65">{C.HANDLING}</p>'
              f'<p class="hand" style="right:[[60]]; bottom:[[50]]; width:[[290]]; border:1px dashed currentColor; padding:[[14]] [[20]]; font-size:[[36]]; line-height:1.4">Batch 027<br>10/22</p>', "84%")
    trio = "".join(f'<div style="width:24%; transform:rotate({r}deg) translateY({y}%); box-shadow:0 22px 34px -16px rgba(42,33,28,.55)">{box(i)}</div>' for i, (r, y) in enumerate(((-2, 4), (1.5, -3), (-1, 5))))
    gift = ab(4, 3, mood("haze") + f'<div class="ab flat" style="left:[[120]]; top:[[110]]; width:[[400]]; height:[[530]]; background:{KUROCHA}; color:#FAF7F1">'
                  f'<div style="left:[[50]]; right:[[50]]; top:[[60]]">{L(M, "faf7f1", "100%")}</div><p class="vt" style="right:[[50]]; bottom:[[50]]; font-family:var(--jp); font-size:[[30]]; letter-spacing:.3em">三本の、間。</p>'
                  f'<p style="left:[[50]]; bottom:[[50]]; {ITAL}; font-size:[[24]]">three pauses</p></div>'
                  f'<div style="left:[[460]]; top:[[230]]; width:[[230]]; transform:rotate(4deg); box-shadow:0 [[14]] [[30]] rgba(0,0,0,.35)">{box(1)}</div>'
                  f'<div style="right:[[90]]; bottom:[[80]]; width:[[140]]; transform:rotate(-10deg)">{badge("100%", "#FAF7F1")}</div>', "100%", f"background:{KUROCHA}", cls="flat")
    pack = (pf(f'<div style="display:flex; gap:3%; align-items:center; justify-content:center; width:100%">{trio}</div>', "The range", "One deep board per flavour, a photograph framed as a window, three words above and the mark large below; each box is dated by hand.", "21/10", pstyle=f"background:#E9E3D8") +
            '<div class="grid g3" style="margin-top:clamp(20px,3vw,36px)">' +
            pf(band + back, "Band label and back label", "On the bottle, inside the box: 間 in vertical Mincho, the mark, and the date written by hand. 一括表示 at 8 pt minimum.", "1/1", pstyle="flex-direction:column; gap:7%") +
            pf(tag("［お名前］さんへ<br>ゆっくり、どうぞ。", "30%", "[[120]]") + f'<div style="position:absolute; left:12%; bottom:12%">{K.moon("64px", 1, MI)}</div>', "String tag", "Tied at the neck, written by hand for each order.", "1/1") +
            pf(notebook(fitw(1, 105 / 148, .84)), "Fermentation slip", "In every order: the batch’s fourteen days, marked in red pen.", "1/1") + '</div>'
            + '<div class="grid g-wide" style="margin-top:clamp(20px,3vw,36px)">'
            + pf(gift, "Gift set", "Three bottles in a kurocha sleeve, on light taken out of focus; sealed with the seal in gofun.")
            + pf(f'<div style="position:absolute; inset:7% 5%; color:{MI}">{K.moon_paper("100%", MI)}</div>', "Wrapping paper", "Neri tissue printed with small moons in a half-drop repeat, waxing along each row as a batch does.", "1.2/1", pstyle=f"background:{NERI}")
            + '</div>')

    a5w = fitw(4 / 3, 148 / 210, .82)
    fl_f = ab(148, 210, win("pourcup", "[[70]]", "[[90]]", "[[330]]", "[[640]]", "50% 45%", 900, 2)
              + f'<div class="ab flat" style="left:[[400]]; top:[[520]]; width:[[530]]; height:[[640]]; z-index:1; background:{ODO}; color:{MI}">'
              f'<p class="vt jp" style="right:[[60]]; top:[[60]]; font-size:[[62]]; font-weight:600; letter-spacing:.14em; line-height:1.8">はじめての、<br>コンブチャ仕込み。</p>'
              f'<p class="hand" style="left:[[50]]; bottom:[[60]]; font-size:[[44]]">［月日］名古屋</p></div>'
              f'<div style="left:[[70]]; bottom:[[70]]; width:[[300]]; z-index:3">{L(M, "faf7f1", "100%")}</div>'
              f'<div style="left:[[60]]; top:[[830]]; z-index:3">' + note("少人数で、<br>のんびり仕込みましょう。", "[[400]]", rot=-4, size="[[26]]", pad="[[28]]") + '</div>',
              a5w, f"background:{KUROCHA}; color:#FAF7F1")
    fl_b = ab(148, 210, f'<p class="jp" style="left:[[90]]; top:[[110]]; font-size:[[54]]">ワークショップのご案内</p>'
              f'<dl style="left:[[90]]; right:[[90]]; top:[[260]]; font-family:var(--sans); font-size:[[36]]; line-height:1.55; column-gap:[[40]]; row-gap:[[30]]">'
              + "".join(f'<dt style="color:{ODT}">{a}</dt><dd>{b}</dd>' for a, b in [("日時", "［月日（曜）時間］"), ("場所", "名古屋市［　］"), ("対象", "どなたでも"), ("定員", "［　］名（先着順）"), ("内容", "仕込みの体験と試飲"), ("参加費", "¥［　］（税込）"), ("申込方法", "Instagram DM / LINE")]) + '</dl>'
              f'<div class="row" style="left:[[90]]; bottom:[[100]]; gap:[[30]]">' + "".join(f'<span style="width:[[150]]; aspect-ratio:1; border:1px solid currentColor; display:flex; align-items:center; justify-content:center; font-size:[[24]]; letter-spacing:.2em">{q}</span>' for q in ("LINE", "IG")) + '</div>'
              f'<p class="pen" style="right:[[90]]; bottom:[[110]]; font-size:[[54]]; transform:rotate(-4deg)">お待ちしています！</p>', a5w, f"background:{GO}; color:{MI}")
    cw = fitw(4 / 3, 91 / 55, .34)
    card_f = ab(91, 55, f'<div style="left:[[70]]; bottom:[[70]]">{L(M, "3a3631", "[[330]]")}</div><span class="vt jp" style="right:[[70]]; top:[[70]]; font-size:[[40]]; letter-spacing:.34em">ナアウ</span>', cw, f"background:{GO}; color:{MI}")
    card_b = ab(91, 55, f'<p class="hand" style="left:[[70]]; top:[[70]]; font-size:[[60]]">またね。</p><p style="left:[[70]]; bottom:[[70]]; font-family:var(--sans); font-size:[[32]]">名古屋市［　］ · @naau_kombucha</p>', cw, f"background:{KAKI}; color:{GO}")
    prt = ('<div class="grid g2">' + pf(fl_f + fl_b, "A5 workshop flyer", "A photograph and an ochre card overlapping on kurocha, the title set vertically, a handwritten note pinned; details in the standard order on the back.", "4/3") +
           pf(card_f + card_b, "Shop card, 91 × 55 mm", "Gofun front, kakishibu back with a handwritten line.", "4/3", pstyle="flex-direction:column; gap:7%") + '</div>')

    posts = [
        (ab(3, 4, f'<div class="row" style="left:[[80]]; right:[[80]]; top:[[70]]; justify-content:space-between; font-family:var(--jp); font-size:[[28]]; letter-spacing:.3em">' + "".join(f'<span>{x}</span>' for x in WORDS) + '</div>'
                  + win("hoshigaki", "[[80]]", "[[150]]", "[[80]]", "[[330]]", "50% 40%")
                  + f'<p style="left:0; right:0; top:[[560]]; z-index:2; text-align:center; font-family:var(--jp); font-size:[[40]]; letter-spacing:.3em; color:#FAF7F1; text-shadow:0 0 [[24]] rgba(0,0,0,.45)">［フレーバー］</p>'
                  f'<div class="row" style="left:[[80]]; right:[[80]]; bottom:[[90]]; justify-content:space-between; align-items:flex-end"><div style="width:[[300]]">{L(M, "faf7f1", "100%")}</div>'
                  f'<span class="hand" style="font-size:[[40]]">今週の仕込み</span></div>', "100%", f"background:{KAKI}; color:{GO}", cls="flat post"),
         "Batch post", "The flavour’s board and window, as on its box; a handwritten line beneath."),
        (ab(3, 4, mood("haze", "50% 40%") + f'<div style="left:0; right:0; top:44%; text-align:center; color:#FAF7F1"><p style="font-family:var(--jp); font-size:[[48]]; letter-spacing:.24em">開ける前に、</p>'
                  f'<p style="{ITAL}; font-size:[[58]]">take a breath.</p></div><div style="left:50%; bottom:[[90]]; transform:translateX(-50%); width:[[220]]">{L(M, "faf7f1", "100%")}</div>', "100%", f"background:{KUROCHA}", cls="flat post"),
         "Mood post", "Light out of focus; a small line in the middle, the mark small below."),
        (ab(3, 4, win("curtain", "[[80]]", "[[110]]", "[[400]]", "[[560]]", "50% 50%", 900, 1)
                  + f'<div class="ab flat" style="left:[[440]]; top:[[480]]; width:[[480]]; height:[[700]]; z-index:2; background:{ODO}; color:{MI}">'
                  f'<p class="vt" style="right:[[56]]; top:[[60]]; font-family:var(--jp); font-size:[[36]]; letter-spacing:.3em; line-height:2">からだの声に、<br>耳を澄ます。</p>'
                  f'<div style="left:[[46]]; right:[[46]]; bottom:[[-34]]">{L(M, "3a3631", "100%")}</div></div>',
                  "100%", f"background:{KUROCHA}; color:{GO}", cls="flat post"),
         "Overlap post", "A photograph and an ochre card overlapping on kurocha; the mark cropped by the card’s edge."),
    ]
    rules_ = "".join(f'<div style="right:[[{100 + k * 108}]]; top:[[110]]; bottom:[[330]]; width:1px; background:rgba(184,53,43,.35)"></div>' for k in range(9))
    letter = ("こんにちは、naʻau です。", "はじめての仕込みの会を", "ひらきます。", "［月］［日］（土）十三時から、", "名古屋［　］にて。", "定員［　］名、先着順です。", "おまちしています。")
    story = ab(9, 16, rules_ + "".join(f'<p class="pen vt" style="right:[[{150 + i * 108}]]; top:[[150]]; font-size:[[60]]; line-height:1; letter-spacing:.12em; white-space:nowrap">{t}</p>' for i, t in enumerate(letter))
               + f'<div style="left:[[90]]; right:[[90]]; top:[[110]]; bottom:[[330]]; border:1px solid rgba(184,53,43,.35)"></div>'
               f'<div style="left:[[110]]; bottom:[[90]]; width:[[230]]">{K.jar("100%", MI)}</div>'
               f'<div style="right:[[110]]; bottom:[[100]]; width:[[180]]; transform:rotate(-5deg)">{badge("100%")}</div>', "100%", f"background:{PAPER}", cls="flat story")
    nts = notes(["The wordmark is shown from your Ogg setting with the ʻokina turned the right way; retype it with ‘ (U+2018) in Ogg for the font’s own mark.",
                 "Borrowed as principles, not copied: one deep colour per product, a photograph framed like a window, light out of focus for mood, overlapping cards, and a mark large enough to crop. Ours: Japanese colours (ōdo, kakishibu, koke, kurocha), three Japanese words, vertical type and the handwriting.",
                 "Photographs are stand-ins from Unsplash; the shoot would be the kitchen in morning light, the jar, the pour, persimmons drying, moss in the garden.",
                 "Handwriting is set in Klee One as a stand-in until the real handwriting is scanned."])
    direction_page(M, hero, idn, pal, typ, pack, prt, social("ogg", posts, story), nts)

# ---------------------------------------------------------------- the Ogg website: a slow, poetic journal on gofun paper
# A headline with photographs set between the words, handwriting over a photograph, numbered batches,
# a typed page on a split photograph with the notebook laid on it, and a journal grid.
def pill(key, pos="50% 50%"):
    """A photograph set inline, between words, like a word itself."""
    return f'<span class="og-pill">{C.pic(key, 500, pos)}</span>'

def corners(a, b, c):
    return '<div class="og-corner tw">' + "".join(f'<span>{x}</span>' for x in (a, b, c)) + '</div>'

def m_shell(content):
    nav = ('<header class="og-head"><nav class="og-nav tw" aria-label="Shop"><div><a href="ogg-product.html">お店 · Shop</a><a href="ogg-home.html#notes">ノート · Notes</a></div>'
           f'<a href="ogg-home.html" aria-label="naʻau home">{L(M, "3a3631", "112px")}</a>'
           '<div><a href="ogg-home.html#journal">読みもの · Journal</a><a href="#">かご (0)</a></div></nav></header>')
    foot = (f'<footer class="og-foot"><div class="og-foot-in"><div>{L(M, "faf7f1", "140px")}<p class="hand" style="margin-top:14px">またね。</p></div>'
            f'<div class="jp og-foot-links">{C.legal_links()}</div></div>'
            '<div class="og-foot-base tw"><span>Kombucha</span><span>and</span><span>a pause</span></div></footer>')
    return f'<div class="shop og">{nav}<main>{content}</main>{foot}</div>'

def og_card(i, n):
    fl, bg, *_ = OFL[i]
    body = ("紅茶と［素材］を、ゆっくり。やさしい酸味。", "柿の干されるころの、深い色。", "苔の庭のような、静かな一本。")[i]
    return (f'<a class="og-card" href="ogg-product.html"><p class="og-num">{n:02d}</p><p class="tw og-k">Batch {27 + i:03d}</p>{m_tile(i, "4/5", "60%")}'
            f'<p class="jp og-card-t">{fl}</p><p class="jp og-card-b">{body}</p><span class="tw og-view">View →</span></a>')

def m_home():
    hero = ('<section class="og-poem">' + corners("Kombucha", "and", "a pause") +
            '<h1 class="og-big jp">'
            f'<span>からだの {pill("pourcup", "50% 45%")}</span>'
            f'<span>{pill("shoji", "45% 50%")} <i>声に、</i></span>'
            f'<span>耳を {pill("hoshigaki", "50% 40%")} 澄ます。</span></h1>'
            '<p class="og-poem-en">listen, then open the bottle.</p>'
            + corners("Brewed in", "名古屋", "by hand") + '</section>')
    feature = (f'<section class="og-feat grain">{C.pic("hoshigaki", 2000, "50% 45%")}'
               f'<p class="vt jp og-feat-v">今週の、ひと瓶。</p>'
               f'<p class="og-feat-big">A pause,<br><span>bottled.</span></p>'
               f'<p class="og-feat-s">柿の干されるころに仕込んだ、<br>028番。kakishibu の一本。</p>'
               f'<div class="og-feat-pg tw"><b>01</b><span>02</span><span>03</span></div>'
               f'<a class="og-feat-go tw" href="ogg-product.html">Shop · 見る</a></section>')
    notes_ = (f'<section class="og-story" id="notes"><div class="og-story-a"><div class="og-story-pic grain">{C.pic("curtain", 900, "50% 50%")}</div>'
              f'<p class="vt tw og-story-l">Notes</p><h2 class="jp">はじまりは、<br>ひとつの直感。</h2></div>'
              f'<div class="og-story-b"><p class="pen og-script">今日もゆっくり、<br>自分の声を<br>聴いてね。</p><div class="og-story-pic2 grain">{C.pic("linen", 1200, "50% 50%")}</div></div>'
              f'<div class="og-story-c"><div><p class="tw og-k">The naʻau way</p><p class="jp">直感kombucha、instinct kombucha、gut feeling kombucha。どれも違う。大好きなハワイの言葉で「直感」は naʻau。腸と、内なる声のこと。</p>'
              f'<p class="jp">名古屋の台所で、ひと瓶ずつ仕込んでいます。</p><a class="og-btn tw" href="#shop">今週の仕込み</a></div>'
              f'<div class="og-story-frame"><div class="grain">{C.pic("ceramics", 900, "50% 50%")}</div></div></div></section>')
    shop = ('<section class="og-shop" id="shop"><div class="og-shop-h"><p class="tw og-k">今週の仕込み · This week</p><p class="og-shop-i">Three batches, each dated by hand.</p></div>'
            '<div class="og-cards">' + "".join(og_card(i, i + 1) for i in range(3)) + '</div></section>')
    typed = ("NAʻAU MEANS THE GUT, AND THE VOICE WITHIN, IN HAWAIIAN.", "IT IS KOMBUCHA BREWED SLOWLY IN A KITCHEN IN NAGOYA,", "ONE JAR AT A TIME.",
             "LISTEN BEFORE YOU OPEN IT.", "HOW DID YOU SLEEP? HOW IS YOUR STOMACH? HOW DO YOU FEEL TODAY?")
    split = (f'<section class="og-split"><div class="og-split-top grain">{C.pic("wall", 1800, "50% 50%", "filter:sepia(.5) saturate(.7) brightness(1.08)")}<div class="og-split-mark">{L(M, "3a3631", "100%")}<p class="vt jp">間</p></div></div>'
             f'<div class="og-typed">' + "".join(f'<span>{t}</span>' for t in typed) + '</div>'
             f'<div class="og-split-low grain">{C.pic("bokeh", 1800, "50% 50%", "filter:brightness(.55)")}'
             f'<div class="og-book">{notebook("100%", "box-shadow:none")}</div>'
             f'<p class="og-typeline">今日も、ゆっくり。<br><span>what a slow day.</span></p></div></section>')
    J = [("glasses", "10.22", "光と、グラスと、朝の台所。"), ("amber", "10.15", "琥珀色になるまでの、十四日。"), ("moss", "10.08", "苔の庭で、深呼吸。"),
         ("slit", "10.01", "障子の隙間の、細い光。"), ("pourbowl", "09.24", "注ぐ音を、聴く。"), ("dusk", "09.17", "夕方の、柿色の壁。"), ("ceramics", "09.10", "器を選ぶ、という仕込み。")]
    tiles = "".join(f'<a class="og-j og-j{i}" href="#"><div class="og-j-pic grain">{C.pic(k, 900, "50% 50%")}</div><p class="tw og-k">{d}</p><p class="og-j-t jp">{t}</p></a>' for i, (k, d, t) in enumerate(J))
    journal = (f'<section class="og-journal" id="journal"><div class="og-jgrid">{tiles}</div>'
               '<p class="og-jintro"><i>読みもの</i> — a slow journal of the kitchen in Nagoya: the jar, the light, the days a batch takes, and what you notice while you wait.</p></section>')
    return m_shell(hero + feature + notes_ + shop + split + journal)

def m_product():
    detail = [("01", "Taste · 味わい", "［味わいの説明］。やさしい酸味と、紅茶の香り。"), ("02", "How to drink · 飲みかた", "よく冷やして、ゆっくりと。開ける前に、ひと呼吸。"), ("03", "Made · 仕込み", "名古屋の台所で、14日。日付は一本ずつ手書きで。")]
    content = (f'<section class="og-pd"><div class="og-pd-media">{m_tile(1, "4/5", "58%")}<p class="vt tw og-story-l">Batch 028</p>'
               f'<div class="og-pd-hand grain">{C.pic("linen", 1200, "50% 50%")}<p class="pen og-script og-script-s">このノートと<br>一緒に届けます。</p></div></div>'
               f'<div class="og-pd-info"><p class="tw og-k"><a href="ogg-home.html#shop">お店</a> / 028</p><h1 class="jp">［フレーバー］</h1><p class="og-poem-en" style="text-align:left; margin:0">kakishibu · a pause, bottled</p>'
               f'<p class="jp" style="line-height:2.1">紅茶と［素材］を、酵母と酢酸菌でゆっくり発酵させました。柿の干されるころの、深い色の一本です。</p>'
               f'<p style="font-size:24px">¥［　］<small style="font-size:13px">（税込）· 330 ml</small></p>'
               f'<label style="display:flex; gap:10px; align-items:center; min-height:44px"><input type="checkbox" style="width:20px; height:20px; accent-color:{MI}"><span class="jp">手書きのメッセージを添える</span></label>'
               f'<div style="display:flex; gap:10px"><input type="number" value="1" min="1" aria-label="数量" style="width:72px; min-height:48px; border:1px solid {MI}; background:transparent; padding:0 10px">'
               f'<button type="button" class="og-btn tw og-solid" style="flex:1">カートに入れる</button></div>'
               + C.commerce(f"border-top:1px solid #DDD3C3; padding:14px 0; font-size:13px; line-height:1.9")
               + '<div class="og-nums">' + "".join(f'<div><p class="og-num">{n}</p><p class="tw og-k">{h}</p><p class="jp">{b}</p></div>' for n, h, b in detail) + '</div>'
               + f'<div>{C.accordions("#DDD3C3")}</div><p class="jp" style="font-size:11px; color:#7A7268">※本品は清涼飲料水です。医薬品ではありません。</p></div></section>'
               f'<section class="og-shop"><div class="og-shop-h"><p class="tw og-k">ほかの仕込み · Also this week</p></div><div class="og-cards og-cards-2">{og_card(0, 1)}{og_card(2, 3)}</div></section>')
    return m_shell(content)

# ---------------------------------------------------------------- product tiles: the label itself, not a placeholder
def s_tile(fl="［フレーバー］", ratio="4/5", bg="#F1F1EF", w="56%"):
    st = ab(1, 1, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[46]]">{L(S, "1e1e1e", "62%")}<span style="position:static; font-family:var(--sans); font-size:[[40]]; letter-spacing:.24em">{fl}· 330 ml</span></div>', "100%", "border-radius:50%")
    return f'<div style="aspect-ratio:{ratio}; background:{bg}; display:flex; align-items:center; justify-content:center"><div style="width:{w}; filter:drop-shadow(0 10px 18px rgba(0,0,0,.12))">{st}</div></div>'

def m_tile(i=0, ratio="3/4", w="58%", rot=-2):
    """A product tile: the flavour's box, standing on warm paper."""
    return (f'<div style="aspect-ratio:{ratio}; background:#E9E3D8; display:flex; align-items:center; justify-content:center">'
            f'<div style="width:{w}; transform:rotate({rot}deg); box-shadow:0 22px 34px -16px rgba(42,33,28,.55)">{box(i)}</div></div>')

# ====================================================================== write
for d, build, home, product in ((S, s_dir, s_home, s_product), (P, p_dir, p_home, p_product), (M, m_dir, m_home, m_product)):
    build()
    C.page(f'{d["key"]}-home.html', f'naʻau — home ({d["name"]})', d["cls"], home())
    C.page(f'{d["key"]}-product.html', f'naʻau — product ({d["name"]})', d["cls"], product())
print("direction pages written")
