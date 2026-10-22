"""The three direction pages, each with its own home and product mockups.

Shiro (naʻau today): white, centred, photo-led, round sticker labels.
Ippon (Lenora): sumi, strict symmetry, double-rule frames, batch numerals, made out to one person.
Ma (Ogg): gofun and ōdo, asymmetry, vertical Japanese, kimy's handwritten notes.
"""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
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

def direction_page(d, hero, idn, pal, typ, pack, prt, soc, nts):
    k = d["key"]
    body = (C.nav(k) + hero +
            sec("01", "Identity", "The mark on its ground, the moods it can take, colour and type.", idn + f'<div class="sub"><h3>Colour</h3><p>{pal[1]}</p></div>' + pal[0] + typ) +
            sec("02", "Packaging", "330 ml amber glass, matte water-resistant labels, and the 一括表示 panel on the back.", pack) +
            sec("03", "Print", "An A5 workshop flyer and a 91 × 55 mm shop card.", prt) +
            sec("04", "Social", "Feed posts at 3:4 (1080 × 1440) with key content inside the 4:5 crop; stories at 9:16.", soc) +
            sec("05", "Website", "Working pages: tax-inclusive prices, refrigerated delivery cost and date beside the cart, legal pages in the footer.", C.previews(d)) +
            f'<section class="sec"><div class="wrap">{nts}</div></section>'
            '<footer class="site"><div class="wrap">naʻau kombucha · brand concepts by Ivycoast · text in ［brackets］ is for naʻau to fill in · photography is shown as direction, not final images.</div></footer>')
    C.page(f"{k}.html", f'{d["kanji"]} {d["name"]} — naʻau brand concepts', d["cls"], body, C.FIT)

# ====================================================================== SHIRO
S = D["current"]

def s_dir():
    hero = (f'<header class="wrap" style="padding-top:clamp(64px,9vw,120px); text-align:center; display:flex; flex-direction:column; align-items:center; gap:22px">'
            f'<p class="eyebrow">Direction 0 · naʻau today</p>{L(S, "1e1e1e", "min(62%,340px)")}'
            f'<h1 style="margin:22px 0 0; font-weight:400; font-size:clamp(30px,3.6vw,46px); line-height:1.15">白 Shiro — the brand as it is</h1>'
            f'<p style="max-width:560px; color:var(--muted)">kimy’s script, on white. Black ink, small centred type, nothing added. The colour comes from the amber glass and the light in the photographs.</p></header>'
            f'<div class="wrap" style="margin-top:clamp(40px,6vw,72px)">{still("current", "range", "21/9", "morning light, white table", zoom=1.55)}</div>')
    pr, pb = 4 / 3, 1
    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 3, f'<div class="fill" style="display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "40%")}</div>', "100%", cls="flat"), "Plain", "The lockup, centred and small, on white."),
        pf(ab(4, 3, ph("current", "pour", "0", "0", "100%", "4/3.4") + f'<div style="left:0; right:0; bottom:0; height:[[110]]; background:#fff; display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "16%", small=True)}</div>', "100%", cls="flat"), "Photo-led", "The photograph carries the colour; the mark sits beneath it."),
        pf(ab(4, 3, ph("current", "single", "0", "0", "100%", "4/3", zoom=1.4) + f'<div style="right:[[50]]; bottom:[[44]]">{L(S, "1e1e1e", "[[150]]", small=True)}</div>', "100%", cls="flat"), "Signature", "The script small in a corner, like a signature on a print."),
    ]) + '</div>'
    pal = (chips([("White", "#FFFFFF", "Ground", 3), ("Ink", "#1E1E1E", "Text · 16.9:1", 2), ("Grey", "#6B6B6B", "Small text · 5.3:1", 1), ("Mist", "#F1F1EF", "Photo backdrops", 2), ("Amber glass", "#8E4E1F", "From the bottle only", 1.2)]),
           "Plain white and ink, as naʻau looks today.")
    typ = spec([("Wordmark", L(S, "1e1e1e", "160px"), "kimy’s script, as it is"),
                ("Japanese", '<p style="font-family:var(--sans); font-weight:300; font-size:20px; line-height:1.9">飲むだけじゃない。<br>自分の身体に気づく、kombucha。</p>', "Zen Kaku Gothic New, Light"),
                ("Latin", '<p style="font-family:var(--sans); font-weight:300; font-size:20px; letter-spacing:.14em">NO. 027 · 330 ML</p>', "Same family, tracked, small")])
    sticker = ab(1, 1, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[46]]">{L(S, "1e1e1e", "62%")}<span style="position:static; font-family:var(--sans); font-size:[[40]]; letter-spacing:.24em">［フレーバー］· 330 ml</span></div>', fitw(1, 1, .7), "border-radius:50%")
    back = ab(3, 4, f'<div class="fill col" style="padding:[[80]] [[76]]; font-family:var(--sans); font-size:[[42]]; line-height:1.75; gap:[[40]]"><dl style="position:static; column-gap:[[40]]">{C.ichi_rows()}</dl>'
              f'<p style="position:static">{C.HANDLING}</p><div style="position:static; margin-top:auto; border:1px dashed currentColor; padding:[[24]] [[30]]; display:flex; justify-content:space-between"><span>Batch ＿＿</span><span>瓶詰め日 ＿＿</span></div></div>', fitw(1, .75, .8))
    box = ab(4, 3, f'<div class="fill" style="display:flex; align-items:center; justify-content:center">{L(S, "1e1e1e", "38%")}</div><span style="left:0; right:0; bottom:[[60]]; text-align:center; font-family:var(--sans); font-size:[[30]]; letter-spacing:.3em">要冷蔵 · クール便</span>', "74%")
    pack = (pf(still("current", "range", "21/9", zoom=1.45), "The range", "330 ml amber glass with a round white sticker, Ø 60 mm. The glass is the only colour.", plate=False) +
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
        (ab(3, 4, ph("current", "single", "[[70]]", "[[70]]", "[[860]]", "1/1.08", zoom=1.9) + '<p style="left:0; right:0; bottom:[[90]]; text-align:center; font-family:var(--sans); font-size:[[36]]; letter-spacing:.16em">No. 027 · ［フレーバー］</p>', "100%", cls="flat post"), "Batch post", "Photograph first, one line beneath."),
        (ab(3, 4, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[80]]"><p style="position:static; font-family:var(--sans); font-weight:300; font-size:[[50]]; line-height:2.1; text-align:center">飲むだけじゃない。<br>自分の身体に気づく、kombucha。</p>{L(S, "1e1e1e", "[[200]]", small=True)}</div>', "100%", cls="flat post", style="outline:1px solid var(--rule)"), "Words post", "Small centred type on white."),
        (ab(3, 4, ph("current", "pour", "0", "0", "100%", "3/4", zoom=1.7), "100%", cls="flat post"), "Pour post", "The pour, in the same white light."),
    ]
    story = ab(9, 16, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[90]]; text-align:center">{L(S, "1e1e1e", "[[300]]", small=True)}'
               f'<p style="position:static; font-family:var(--sans); font-size:[[64]]; line-height:1.9">今日のおなか、<br>どうですか？</p><div style="position:static; display:flex; gap:[[24]]">' +
               "".join(f'<span style="border:1px solid #1E1E1E; border-radius:999px; padding:[[18]] [[40]]; font-family:var(--sans); font-size:[[40]]">{w}</span>' for w in ("軽い", "重い", "ふつう")) + '</div></div>', "100%", cls="flat story", style="outline:1px solid var(--rule)")
    nts = notes(["The current logo uses a straight apostrophe (na'au). Hawaiian spelling uses the ʻokina (ʻ); worth correcting at the next reprint.",
                 "White and ink are kept deliberately plain. The research favours warm off-whites, so a warmer palette can be added later without changing the look."])
    direction_page(S, hero, idn, pal, typ, pack, prt, social("current", posts, story), nts)

def s_header():
    return (f'<header style="border-bottom:1px solid #E4E4E1"><div class="wrap" style="display:flex; flex-direction:column; align-items:center; gap:14px; padding-top:30px; padding-bottom:18px">'
            f'<a href="current-home.html" aria-label="naʻau home">{L(S, "1e1e1e", "140px")}</a>'
            f'<nav aria-label="Shop" style="display:flex; flex-wrap:wrap; justify-content:center; gap:30px; font-family:var(--sans); font-size:12px; letter-spacing:.2em">'
            f'<a href="current-product.html">SHOP</a><a href="current-home.html#about">ABOUT</a><a href="#">WORKSHOP</a><a href="#">CART (0)</a></nav></div></header>')
def s_footer():
    return (f'<footer style="border-top:1px solid #E4E4E1; padding:48px 0; text-align:center; font-family:var(--sans); font-size:12px"><div class="wrap" style="display:flex; flex-direction:column; align-items:center; gap:20px">'
            f'{L(S, "1e1e1e", "90px", small=True)}<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:10px 24px">{C.legal_links()}</div><span style="color:#6B6B6B">© 2026 naʻau kombucha · concept mockup</span></div></footer>')

def s_home():
    cards = "".join(f'<a href="current-product.html" style="text-align:center; display:flex; flex-direction:column; gap:12px">{still("current", "single", "4/5", label="current", zoom=2.2, flavours=(f,) * 3)}'
                    f'<span style="font-family:var(--sans); font-size:14px">{f}</span><span style="font-family:var(--sans); font-size:13px; color:#6B6B6B">¥［　］（税込）</span></a>'
                    for f in ("［フレーバー］", "［フレーバー］", "［限定］", "［3本セット］"))
    insta = "".join(still("current", k, "1/1", zoom=z) for k, z in (("pour", 2.2), ("range", 2.4), ("glass", 2.0), ("single", 2.6), ("jar", 2.0), ("pour", 3)))
    main = (f'<main>{still("current", "range", "16/7", zoom=1.4)}'
            f'<section style="text-align:center; padding:clamp(64px,9vw,120px) 0"><div class="wrap"><p class="jp" style="font-family:var(--sans); font-weight:300; font-size:clamp(20px,2.2vw,26px); line-height:2.1">飲むだけじゃない。<br>自分の身体に気づく、kombucha。</p>'
            f'<p style="margin:20px auto 0; max-width:520px; font-family:var(--sans); font-size:14px; line-height:2.1; color:#6B6B6B">naʻau（ナアウ）は、ハワイ語で「腸・心・内なる声」。名古屋の台所で、ひと瓶ずつ仕込んでいます。</p></div></section>'
            f'<section style="padding:0 0 clamp(64px,9vw,120px)"><div class="wrap"><p style="text-align:center; font-family:var(--sans); font-size:12px; letter-spacing:.26em; margin-bottom:32px">THIS WEEK</p>'
            f'<div class="grid g4">{cards}</div></div></section>'
            f'<section id="about" style="padding:clamp(64px,9vw,120px) 0; border-top:1px solid #E4E4E1"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr)); gap:clamp(32px,6vw,80px); align-items:center">'
            f'{still("current", "jar", "4/5", zoom=1.9)}<div style="display:flex; flex-direction:column; gap:20px; font-family:var(--sans)"><p style="font-size:12px; letter-spacing:.26em">ABOUT</p>'
            f'<p style="font-size:20px; font-weight:300">名前は、直感で決めました。</p>'
            f'<p style="font-size:14px; line-height:2.1; color:#4A4A4A">大好きなハワイの言葉で「直感」は naʻau。腸と感情、内なる声を感じるという意味もあると知って、これしかないと決めました。</p>'
            f'<p style="font-size:13px; color:#6B6B6B">kimy — 看護師として働きながら、コンブチャを仕込んでいます。</p></div></div></section>'
            f'<section style="padding:0 0 clamp(64px,9vw,120px)"><div class="wrap"><p style="text-align:center; font-family:var(--sans); font-size:12px; letter-spacing:.26em; margin-bottom:24px">@naau_kombucha</p>'
            f'<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:6px">{insta}</div></div></section>'
            f'<section style="text-align:center; padding:clamp(56px,7vw,96px) 0; border-top:1px solid #E4E4E1"><div class="wrap"><p style="margin-bottom:18px; font-family:var(--sans); font-size:14px">新しい仕込みと、ワークショップのお知らせ</p>'
            f'<form onsubmit="return false" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px"><label style="display:flex; flex-direction:column; gap:4px; text-align:left"><span style="font-family:var(--sans); font-size:11px; color:#6B6B6B">Email</span>'
            f'<input type="email" placeholder="you@example.com" style="min-height:46px; width:260px; border:1px solid #1E1E1E; padding:0 12px"></label>'
            f'<button class="btn" type="submit" style="align-self:flex-end; background:#1E1E1E; color:#fff; border-color:#1E1E1E">登録する</button><a class="btn" href="#" style="align-self:flex-end">LINE</a></form></div></section></main>')
    return f'<div class="shop" style="background:#fff; color:#1E1E1E">{s_header()}{main}{s_footer()}</div>'

def s_product():
    thumbs = "".join(still("current", k, "1/1", zoom=z) for k, z in (("single", 2.4), ("pour", 2.2), ("glass", 2.2), ("range", 2.0)))
    main = (f'<main><section style="padding:clamp(28px,5vw,64px) 0 clamp(64px,9vw,120px)"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr)); gap:clamp(28px,5vw,72px); align-items:start">'
            f'<div style="display:flex; flex-direction:column; gap:8px">{still("current", "single", "1/1", zoom=1.9)}<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:8px">{thumbs}</div></div>'
            f'<div style="display:flex; flex-direction:column; gap:18px; font-family:var(--sans)">'
            f'<p style="font-size:11px; letter-spacing:.22em; color:#6B6B6B">NO. 027 · 330 ML</p><h1 style="margin:0; font-weight:300; font-size:26px">［フレーバー］</h1>'
            f'<p style="font-size:19px">¥［　］<span style="font-size:12px">（税込）</span></p><p style="font-size:14px; line-height:2.1; color:#3A3A3A">紅茶と［素材］を、酵母と酢酸菌でゆっくり発酵させました。［味わいの説明］。</p>'
            f'<div style="display:flex; gap:8px"><label style="display:flex; flex-direction:column; gap:4px"><span style="font-size:11px; color:#6B6B6B">数量</span><input type="number" value="1" min="1" style="width:72px; min-height:48px; border:1px solid #1E1E1E; padding:0 10px"></label>'
            f'<button type="button" class="btn" style="align-self:flex-end; flex:1; background:#1E1E1E; color:#fff; border-color:#1E1E1E">カートに入れる</button></div>'
            + C.commerce("border:1px solid #E4E4E1; padding:14px 16px; font-family:var(--sans); font-size:13px; line-height:1.9") + f'<div>{C.accordions("#E4E4E1")}</div>'
            f'<p style="font-size:11px; color:#6B6B6B">※本品は清涼飲料水です。医薬品ではありません。</p></div></div></section></main>')
    return f'<div class="shop" style="background:#fff; color:#1E1E1E">{s_header()}{main}{s_footer()}</div>'

# ====================================================================== IPPON
P = D["lenora"]
INK, KIN, SUMI, MUTE = "#2B2926", "#EFEBE2", "#1F1E1C", "#6E6860"

def frame(inner, pad="[[50]]", gap="[[24]]", rule=None, inner_pad="[[70]] [[60]]", just="space-between"):
    col = rule or "currentColor"
    return (f'<div class="fill" style="padding:{pad}"><div style="position:relative; height:100%; border:1px solid {col}; outline:1px solid {col}; outline-offset:[[-14]]; '
            f'display:flex; flex-direction:column; align-items:center; justify-content:{just}; text-align:center; padding:{inner_pad}; gap:{gap}">{inner}</div></div>')

def p_dir():
    hero = (f'<header class="wrap" style="padding-top:clamp(56px,8vw,110px); display:flex; flex-direction:column; align-items:center; text-align:center; gap:26px">'
            f'<p class="eyebrow">Direction 1 · Lenora</p>'
            + ab(16, 10, frame(f'<span class="eyebrow" style="font-size:[[22]]; color:#A39E95">No. 027</span>{L(P, "efebe2", "68%")}<span class="eyebrow" style="font-size:[[22]]; color:#A39E95">Bottled for one</span>', pad="[[40]]", inner_pad="[[70]] [[60]]"),
                 "min(100%,720px)", f"background:{SUMI}; color:{KIN}", cls="flat") +
            f'<h1 style="margin:14px 0 0; font-weight:400; font-size:clamp(30px,3.6vw,46px); line-height:1.15">一本 Ippon — bottled for one</h1>'
            f'<p style="max-width:600px; color:var(--muted)">A made-to-order atelier. Sumi grounds and strict symmetry inside a fine double rule. The batch number is the ornament, every label is made out to the person it’s for, and the water-drop ʻokina is the only flourish.</p></header>'
            f'<div class="wrap" style="margin-top:clamp(40px,6vw,72px)">{still("lenora", "single", "21/9", "one shaft of evening light", zoom=1.5)}</div>')
    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 3, frame(f'<span></span>{L(P, "2b2926", "62%")}<span class="eyebrow" style="font-size:[[24]]; color:{MUTE}">Listen to your naʻau</span>'), "100%", f"background:{KIN}; color:{INK}", cls="flat"), "Framed", "Centred, double rule, symmetry. The default."),
        pf(ab(4, 3, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[10]]"><span style="position:static; font-family:var(--lat); font-size:[[300]]; line-height:.9">027</span>{L(P, "efebe2", "26%")}</div>', "100%", f"background:{INK}; color:{KIN}", cls="flat"), "Numeral", "The batch number as the headline."),
        pf(ab(4, 3, f'<div style="left:[[60]]; right:[[60]]; bottom:[[60]]">{L(P, "efebe2", "100%")}</div><span class="eyebrow" style="left:[[60]]; top:[[56]]; font-size:[[22]]; color:#A39E95">Nagoya · kombucha</span>', "100%", f"background:{SUMI}; color:{KIN}", cls="flat"), "Confident", "The mark edge to edge, for posters and the shop sign."),
    ]) + '</div>'
    pal = (chips([("Sumi", "#2B2926", "Ground · 12.2:1 on kinari", 3), ("Kinari", "#EFEBE2", "Labels, type on sumi", 2), ("Keshizumi", "#524E4D", "Rules", 1), ("Usuzumi", "#A39E95", "Captions on sumi", 1), ("Amber glass", "#9C5B22", "The only warmth", 1.2)]),
           "Palette A, Sumi & Kinari: ink on washi; the amber bottle is the only warmth.")
    typ = spec([("Wordmark", L(P, "efebe2", "170px"), "Lenora, with a water-drop ʻokina"),
                ("Japanese", '<p style="font-family:\'Shippori Mincho B1\'; font-weight:700; font-size:22px; line-height:1.8">一滴から、からだの声を。</p>', "Shippori Mincho B1, Bold"),
                ("Numerals", '<p style="font-size:44px; line-height:1; font-variant-numeric:lining-nums">027 028 029</p>', "EB Garamond")])
    lw = fitw(1, .75, .8)
    front = ab(3, 4, frame(f'<span></span>{L(P, "2b2926", "78%")}<span style="font-family:var(--lat); font-style:italic; font-size:[[60]]">kombucha</span>'
                           f'<dl style="position:static; width:100%; text-align:left; column-gap:[[40]]; row-gap:[[8]]; font-size:[[44]]; align-items:baseline">'
                           f'<dt class="eyebrow" style="font-size:[[28]]; color:{MUTE}">For</dt><dd class="jp">［お名前］様</dd><dt class="eyebrow" style="font-size:[[28]]; color:{MUTE}">Bottled</dt><dd>2026 · 10 · 22</dd>'
                           f'<dt class="eyebrow" style="font-size:[[28]]; color:{MUTE}">Batch</dt><dd>No. 027 · day 14</dd></dl>', inner_pad="[[90]] [[70]] [[80]]"), lw, f"background:{KIN}; color:{INK}")
    back = ab(3, 4, frame(f'<dl style="position:static; text-align:left; font-family:var(--jp); font-size:[[40]]; line-height:1.75; column-gap:[[36]]; width:100%">{C.ichi_rows()}</dl>'
                          f'<p class="jp" style="position:static; font-size:[[38]]; line-height:1.7; text-align:left">{C.HANDLING}</p>'
                          f'<div style="position:static; width:100%; display:flex; justify-content:space-between; border-top:1px solid currentColor; padding-top:[[24]]; font-size:[[34]]"><span>No. ＿＿</span><span>瓶詰め ＿＿</span></div>', inner_pad="[[80]] [[64]]"), lw, f"background:{KIN}; color:{INK}")
    gift = ab(4, 3, f'<div class="fill" style="background:{INK}"></div><div class="ab flat" style="left:50%; top:50%; transform:translate(-50%,-50%); width:[[330]]; aspect-ratio:3/4; background:{KIN}; color:{INK}; box-shadow:0 10px 24px rgba(0,0,0,.4)">'
              + frame(f'<span class="eyebrow" style="font-size:[[60]]; color:{MUTE}">Made out to</span><span class="jp" style="font-size:[[120]]">［お名前］様</span>{L(P, "2b2926", "62%")}', pad="[[60]]", inner_pad="[[120]] [[60]]") + '</div>'
              f'<div style="left:0; right:0; top:50%; height:[[18]]; background:#524E4D; transform:translateY(-50%); z-index:-1"></div>', "78%")
    pack = (pf(still("lenora", "range", "21/9", zoom=1.45), "The range", "A tall framed label made out to its owner; a sumi collar carries the batch number.", plate=False) +
            '<div class="grid g3" style="margin-top:clamp(20px,3vw,36px)">' +
            pf(front, "Front label", "Name, bottling date and batch printed at the counter.", "1/1") +
            pf(back, "Back label", "一括表示 inside the same double rule, 8 pt minimum.", "1/1") +
            pf(gift, "Gift box", "Sumi board with a framed card made out to the recipient.", "1/1") + '</div>')
    a5w = fitw(4 / 3, 148 / 210, .82)
    fl_f = ab(148, 210, frame(f'<span class="eyebrow" style="font-size:[[30]]; color:#A39E95">An evening at the counter</span><div style="display:flex; flex-direction:column; align-items:center; gap:[[30]]">'
                              f'<span style="font-family:var(--lat); font-size:[[260]]; line-height:.9">027</span><p style="font-family:\'Shippori Mincho B1\'; font-weight:700; font-size:[[64]]; line-height:1.6">仕込みと、<br>試飲の会。</p></div>{L(P, "efebe2", "54%")}',
                              pad="[[56]]", inner_pad="[[120]] [[60]] [[110]]"), a5w, f"background:{INK}; color:{KIN}")
    fl_b = ab(148, 210, frame(f'<span class="eyebrow" style="font-size:[[30]]; color:{MUTE}">Details</span><dl style="position:static; width:100%; text-align:left; font-family:var(--jp); font-size:[[40]]; line-height:1.55; column-gap:[[40]]; row-gap:[[26]]">'
                              + "".join(f'<dt style="color:{MUTE}">{a}</dt><dd>{b}</dd>' for a, b in [("日時", "［月日（曜）時間］"), ("場所", "名古屋市［　］"), ("定員", "［　］名（先着順）"), ("内容", "仕込みの体験と試飲"), ("参加費", "¥［　］（税込）"), ("申込", "Instagram DM / LINE")]) +
                              f'</dl><div style="display:flex; gap:[[40]]">' + "".join(f'<span style="width:[[150]]; aspect-ratio:1; border:1px solid currentColor; display:flex; align-items:center; justify-content:center; font-size:[[24]]; letter-spacing:.2em">{q}</span>' for q in ("LINE", "IG")) + '</div>',
                              pad="[[56]]", inner_pad="[[120]] [[80]] [[100]]"), a5w, f"background:{KIN}; color:{INK}")
    cw = fitw(4 / 3, 91 / 55, .34)
    card_f = ab(91, 55, frame(f'{L(P, "efebe2", "50%")}', pad="[[40]]", just="center"), cw, f"background:{INK}; color:{KIN}")
    card_b = ab(91, 55, frame(f'<span class="eyebrow" style="font-size:[[30]]; color:{MUTE}">Bottled for</span><span class="jp" style="font-size:[[66]]">［お名前］様</span><span style="font-size:[[38]]">2026 · 10 · 22</span>', pad="[[40]]", inner_pad="[[50]]"), cw, f"background:{KIN}; color:{INK}")
    prt = ('<div class="grid g2">' + pf(fl_f + fl_b, "A5 invitation", "A tasting-and-brewing evening, framed like a card; details on kinari.", "4/3") +
           pf(card_f + card_b, "Shop card and gift card, 91 × 55 mm", "The back is made out by hand at the counter.", "4/3", pstyle="flex-direction:column; gap:7%") + '</div>')
    posts = [
        (ab(3, 4, f'<div class="fill col" style="align-items:center; justify-content:center; gap:[[20]]"><span style="position:static; font-family:var(--lat); font-size:[[380]]; line-height:.9">027</span>'
                  f'<span class="eyebrow" style="position:static; font-size:[[30]]; color:#A39E95; margin-bottom:[[50]]">Now pouring</span>{L(P, "efebe2", "[[300]]")}</div>', "100%", f"background:{INK}; color:{KIN}", cls="flat post"), "Batch post", "The number is the headline."),
        (ab(3, 4, f'<div class="ab flat" style="left:[[70]]; top:[[70]]; right:[[70]]; bottom:[[70]]; background:{KIN}; color:{INK}">' +
                  frame(f'<span></span><p style="font-family:\'Shippori Mincho B1\'; font-weight:700; font-size:[[78]]; line-height:1.8">一本の、<br>自分のための時間。</p>{L(P, "2b2926", "40%")}', pad="[[50]]", inner_pad="[[90]] [[60]] [[100]]") + '</div>', "100%", f"background:{INK}", cls="flat post"), "Words post", "A framed card on sumi."),
        (ab(3, 4, ph("lenora", "single", "0", "0", "100%", "3/4", zoom=1.75), "100%", cls="flat post"), "Product post", "The bottle and its card, in one shaft of light."),
    ]
    story = ab(9, 16, frame(f'<span class="eyebrow" style="font-size:[[36]]; color:#A39E95">Invitation</span><p style="font-family:\'Shippori Mincho B1\'; font-weight:700; font-size:[[78]]; line-height:1.8">今日のおなか、<br>どうですか？</p>'
                            f'<div style="width:80%; display:flex; flex-direction:column; gap:[[24]]">' + "".join(f'<span class="jp" style="border:1px solid #6E6860; padding:[[26]] 0; font-size:[[44]]">{w}</span>' for w in ("軽い", "重い", "ふつう")) + f'</div>{L(P, "efebe2", "46%")}',
                            pad="[[70]]", inner_pad="[[130]] [[70]] [[120]]"), "100%", f"background:{INK}; color:{KIN}", cls="flat story")
    nts = notes(["The wordmark is shown from your Lenora setting with a redrawn water-drop ʻokina. License Lenora with Superior Type’s Logo and Merchandise add-ons, then reset it as vector."])
    direction_page(P, hero, idn, pal, typ, pack, prt, social("lenora", posts, story), nts)

def p_frame_html(inner, style=""):
    return (f'<div style="border:1px solid currentColor; outline:1px solid currentColor; outline-offset:-8px; padding:clamp(28px,4vw,56px); display:flex; flex-direction:column; align-items:center; text-align:center; gap:22px; {style}">{inner}</div>')

def p_shell(content):
    return (f'<div class="shop" style="background:{SUMI}; color:{KIN}; min-height:100vh">'
            f'<header style="border-bottom:1px solid #3A3835"><nav class="wrap" aria-label="Shop" style="display:grid; grid-template-columns:1fr auto 1fr; align-items:center; gap:14px; padding-top:24px; padding-bottom:24px; font-size:12px; letter-spacing:.22em; text-transform:uppercase">'
            f'<div style="display:flex; flex-wrap:wrap; gap:22px"><a href="lenora-product.html">Shop</a><a href="lenora-home.html#ritual">Ritual</a></div>'
            f'<a href="lenora-home.html" aria-label="naʻau home">{L(P, "efebe2", "118px")}</a>'
            f'<div style="display:flex; flex-wrap:wrap; gap:22px; justify-content:flex-end"><a href="#">Workshop</a><a href="#">Cart (0)</a></div></nav></header>'
            f'<main>{content}</main>'
            f'<footer style="border-top:1px solid #3A3835; padding:56px 0; text-align:center"><div class="wrap" style="display:flex; flex-direction:column; align-items:center; gap:20px">{L(P, "efebe2", "110px")}'
            f'<div class="jp" style="display:flex; flex-wrap:wrap; justify-content:center; gap:8px 24px; font-size:13px">{C.legal_links()}</div><span class="eyebrow" style="color:#A39E95">© 2026 naʻau kombucha · concept mockup</span></div></footer></div>')

def p_home():
    cards = "".join(f'<a href="lenora-product.html" style="display:flex; flex-direction:column; gap:14px">{still("lenora", "single", "4/5", zoom=2.3, flavours=(f,) * 3)}'
                    f'<div style="display:flex; justify-content:space-between; align-items:baseline; border-top:1px solid #3A3835; padding-top:12px"><span style="font-size:30px; line-height:1">{n}</span><span class="jp">{f}</span></div>'
                    f'<span style="font-size:14px; color:#A39E95">¥［　］（税込）· fermented {dd} days</span></a>'
                    for f, n, dd in zip(FL, ("027", "028", "029"), ("14", "11", "18")))
    content = (f'<section style="padding:clamp(56px,9vw,120px) 0"><div class="wrap" style="display:flex; justify-content:center">'
               + p_frame_html(f'<span class="eyebrow" style="color:#A39E95">Kombucha · 名古屋</span>{L(P, "efebe2", "min(70%,520px)")}<p style="font-family:\'Shippori Mincho B1\'; font-size:clamp(20px,2.4vw,30px); font-weight:700">一滴から、からだの声を。</p>'
                              f'<p style="font-style:italic; color:#A39E95; margin-top:-10px">Every bottle made out to one person.</p><a class="btn" href="lenora-product.html">Choose your bottle</a>', "width:min(100%,900px)") + '</div></section>'
               f'<section style="padding:0 0 clamp(64px,9vw,120px)"><div class="wrap"><p class="eyebrow" style="text-align:center; color:#A39E95; margin-bottom:32px">This week’s batches</p><div class="grid g3">{cards}</div></div></section>'
               f'<section style="background:{KIN}; color:{INK}; padding:clamp(64px,9vw,120px) 0"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:clamp(32px,6vw,80px); align-items:center">'
               + p_frame_html(f'{L(P, "2b2926", "78%")}<span class="jp" style="font-size:22px">さくら 様</span><span style="font-size:13px">2026 · 10 · 22 · No. 027</span>', "aspect-ratio:3/4; justify-content:space-between; max-width:340px; justify-self:center; width:100%") +
               f'<div style="display:flex; flex-direction:column; gap:18px; max-width:480px"><p class="eyebrow" style="color:{MUTE}">Made out to you</p><p style="font-family:\'Shippori Mincho B1\'; font-size:clamp(24px,2.6vw,32px); font-weight:700; line-height:1.6">ラベルに、あなたの名前を。</p>'
               f'<p class="jp" style="line-height:2.1">店頭でもオンラインでも、瓶詰めの日にお名前を入れてお届けします。贈りものには、相手の名前を。</p>'
               f'<label style="display:flex; flex-direction:column; gap:6px"><span class="eyebrow" style="color:{MUTE}">Name on the label</span><input type="text" placeholder="例：さくら" style="min-height:50px; border:1px solid {INK}; background:transparent; padding:0 14px; color:inherit"></label></div></div></section>'
               f'<section id="ritual" style="padding:clamp(64px,9vw,120px) 0; text-align:center"><div class="wrap grid g3">' +
               "".join(f'<div style="display:flex; flex-direction:column; align-items:center; gap:10px; border-top:1px solid #3A3835; padding-top:28px"><span style="font-size:40px; line-height:1">{n}</span><span style="font-family:\'Shippori Mincho B1\'; font-size:22px; font-weight:700">{a}</span><span style="font-style:italic; color:#A39E95">{b}</span></div>'
                       for n, a, b in [("i", "味わう", "Taste this week’s batches."), ("ii", "選ぶ", "Choose by how you feel."), ("iii", "名を入れる", "Your name goes on the label.")]) + '</div></section>'
               f'<section style="padding:0 0 clamp(64px,9vw,120px)"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr)); gap:clamp(32px,6vw,80px); align-items:center">'
               f'{still("lenora", "jar", "4/5", zoom=1.9)}<div style="display:flex; flex-direction:column; gap:18px"><p class="eyebrow" style="color:#A39E95">About naʻau</p><p style="font-family:\'Shippori Mincho B1\'; font-size:clamp(24px,2.6vw,32px); font-weight:700; line-height:1.6">名前は、直感で決めました。</p>'
               f'<p class="jp" style="line-height:2.1; color:#D8D2C8">大好きなハワイの言葉で「直感」は naʻau。腸と感情、内なる声を感じるという意味もあると知って、これしかないと決めました。</p>'
               f'<p class="jp" style="font-size:13px; color:#A39E95">kimy — 看護師として働きながら、名古屋でコンブチャを仕込んでいます。</p></div></div></section>')
    return p_shell(content)

def p_product():
    content = (f'<section style="padding:clamp(28px,5vw,64px) 0 clamp(64px,9vw,120px)"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr)); gap:clamp(28px,5vw,64px); align-items:start">'
               f'<div style="display:flex; flex-direction:column; gap:8px">{still("lenora", "single", "1/1", zoom=1.9)}<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px">'
               + "".join(still("lenora", k, "1/1", zoom=z) for k, z in (("pour", 2.2), ("range", 2.0), ("jar", 2.0))) + '</div></div>'
               f'<div style="background:{KIN}; color:{INK}; padding:clamp(24px,3.5vw,44px); display:flex; flex-direction:column; gap:18px">'
               f'<div style="display:flex; justify-content:space-between; align-items:baseline"><span style="font-size:60px; line-height:1">027</span><span class="eyebrow" style="color:{MUTE}">330 ml</span></div>'
               f'<h1 style="margin:0; font-family:\'Shippori Mincho B1\'; font-size:clamp(26px,2.6vw,34px); font-weight:700">［フレーバー］</h1>'
               f'<dl style="display:grid; grid-template-columns:auto 1fr; gap:6px 20px; margin:0; font-size:15px; border-top:1px solid {INK}; border-bottom:1px solid {INK}; padding:12px 0"><dt class="eyebrow" style="color:{MUTE}">Tea</dt><dd class="jp" style="margin:0">［茶葉］</dd><dt class="eyebrow" style="color:{MUTE}">Fermented</dt><dd style="margin:0">14 days</dd><dt class="eyebrow" style="color:{MUTE}">Bottled</dt><dd style="margin:0">on the day you order</dd></dl>'
               f'<p style="font-size:26px">¥［　］<small style="font-size:14px">（税込）</small></p>'
               f'<label style="display:flex; flex-direction:column; gap:6px"><span class="eyebrow" style="color:{MUTE}">Name on the label (optional)</span><input type="text" placeholder="例：さくら" maxlength="12" style="min-height:50px; border:1px solid {INK}; background:transparent; padding:0 14px"></label>'
               f'<div style="display:flex; gap:10px"><label style="display:flex; flex-direction:column; gap:6px"><span class="eyebrow" style="color:{MUTE}">Qty</span><input type="number" value="1" min="1" style="width:80px; min-height:50px; border:1px solid {INK}; background:transparent; padding:0 10px"></label>'
               f'<button type="button" class="btn" style="align-self:flex-end; flex:1; background:{INK}; color:{KIN}; border-color:{INK}">カートに入れる</button></div>'
               + C.commerce(f"border:1px solid {INK}; padding:14px 16px; font-size:13px; line-height:1.9") + f'<div>{C.accordions("#C9C2B6")}</div>'
               f'<p class="jp" style="font-size:11px; color:{MUTE}">※本品は清涼飲料水です。医薬品ではありません。</p></div></div></section>')
    return p_shell(content)

# ====================================================================== MA
M = D["ogg"]
MI, GO, ODO, NERI, ODT = "#3A3631", "#FAF7F1", "#C39143", "#EDE4CD", "#8A6A3A"

def note(text, w, rot=-3, size="[[40]]", pad="[[40]]", extra=""):
    return (f'<div style="width:{w}; padding:{pad}; background:{GO}; transform:rotate({rot}deg); box-shadow:0 1px 2px rgba(58,54,49,.14), 0 10px 22px rgba(58,54,49,.10); {extra}">'
            f'<p class="hand" style="font-size:{size}; line-height:1.85; color:{MI}">{text}</p></div>')

def tag(text, w, size):
    return (f'<div style="width:{w}; aspect-ratio:3/5.2; background:{NERI}; clip-path:polygon(18% 0,82% 0,100% 11%,100% 100%,0 100%,0 11%); position:relative; container-type:inline-size; box-shadow:0 0 0 1px rgba(0,0,0,.03)">'
            f'<span style="position:absolute; top:7%; left:50%; width:9%; aspect-ratio:1; transform:translateX(-50%); border-radius:50%; background:var(--plate)"></span>'
            f'<p class="hand vt" style="position:absolute; right:22%; top:22%; font-size:{size}; line-height:1.9; color:{MI}">{text}</p></div>')

def m_dir():
    hero = (f'<header class="wrap" style="padding-top:clamp(48px,7vw,96px); display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr)); gap:clamp(32px,6vw,80px); align-items:center">'
            f'<div style="display:flex; flex-direction:column; gap:22px"><p class="eyebrow">Direction 2 · Ogg</p>{L(M, "3a3631", "min(100%,440px)")}'
            f'<h1 style="margin:6px 0 0; font-weight:400; font-size:clamp(30px,3.6vw,46px); line-height:1.15">間 Ma — the pause</h1>'
            f'<p style="max-width:520px; color:var(--muted)">Airy and hand-made. Asymmetric layouts with room to breathe, vertical Japanese, an ochre block, and kimy’s handwriting on cards that overlap the page. A small card asks how you feel before you open the bottle.</p></div>'
            f'<div style="position:relative; padding:0 0 40px 52px">{still("ogg", "single", "4/5", zoom=1.9)}'
            f'<p class="vt jp" style="position:absolute; left:0; top:0; font-size:clamp(17px,1.6vw,21px); letter-spacing:.34em; line-height:2">からだの声に、耳を澄ます。</p>'
            f'<div style="position:absolute; left:20px; bottom:0">' + note("今日もゆっくり、<br>自分の声を聴いてね。<br>— kimy", "min(56vw,210px)", size="16px", pad="18px 20px") + '</div></div></header>')
    idn = '<div class="grid g3">' + "".join([
        pf(ab(4, 3, f'<p class="vt jp" style="right:[[70]]; top:[[60]]; font-size:[[44]]; letter-spacing:.34em; line-height:2">からだの声に、耳を澄ます。</p><div style="left:[[70]]; bottom:[[70]]">{L(M, "3a3631", "[[330]]")}</div>', "100%", f"background:{GO}; color:{MI}", cls="flat"), "Quiet", "A small mark low, vertical text high, air between. The default."),
        pf(ab(4, 3, f'<div style="left:[[90]]; top:[[90]]">' + note("今日もゆっくり、<br>自分の声を聴いてね。<br>— kimy", "[[640]]", size="[[48]]", pad="[[56]]") + f'</div><div style="right:[[70]]; bottom:[[70]]">{L(M, "3a3631", "[[280]]")}</div>', "100%", f"background:{NERI}; color:{MI}", cls="flat"), "Note", "kimy’s handwriting on a card that overlaps the page."),
        pf(ab(4, 3, f'<p class="jp" style="left:[[70]]; top:[[70]]; font-size:[[64]]; font-weight:600; line-height:1.6">今日のおなか、<br>どうですか？</p><div style="left:[[-40]]; bottom:[[-120]]; width:[[1080]]">{L(M, "3a3631", "100%")}</div>', "100%", f"background:{ODO}; color:{MI}", cls="flat"), "Ochre", "The mark large and cropped, for social and the shop sign."),
    ]) + '</div>'
    pal = (chips([("Gofun", "#FAF7F1", "Ground", 3), ("Ink", "#3A3631", "Text · 11.2:1", 2), ("Ōdo", "#C39143", "Blocks and fills", 1.5), ("Ōdo text", "#8A6A3A", "Accent text · 4.7:1", 1), ("Neri", "#EDE4CD", "Cards, tags", 1.5)]),
           "Palette D, Gofun & Ōdo: morning light through shōji; ochre rhymes with the glass.")
    typ = spec([("Wordmark", L(M, "3a3631", "170px"), "Ogg, with the ʻokina turned the right way"),
                ("Japanese", '<p class="vt jp" style="font-size:20px; letter-spacing:.3em; line-height:2; height:150px">からだの声に、耳を澄ます。</p>', "Zen Old Mincho, set vertically"),
                ("Hand", '<p class="hand" style="font-size:24px; line-height:1.7">今日もゆっくり。<br>— kimy</p>', "kimy’s hand (stand-in: Klee One)")])
    band = ab(2.6, 1, f'<span class="vt jp" style="left:[[70]]; top:50%; transform:translateY(-50%); font-size:[[130]]; line-height:1">間</span>'
              f'<div class="col" style="left:[[230]]; right:[[200]]; top:50%; transform:translateY(-50%); align-items:center; gap:[[16]]">{L(M, "3a3631", "100%")}<span class="hand" style="font-size:[[48]]">［フレーバー］</span></div>'
              f'<span class="vt hand" style="right:[[70]]; top:50%; transform:translateY(-50%); font-size:[[40]]; white-space:nowrap">10/22 kimy</span>', "84%")
    back = ab(2.6, 1, f'<dl style="left:[[60]]; top:[[50]]; width:[[560]]; font-family:var(--sans); font-size:[[27]]; line-height:1.65; column-gap:[[30]]">{C.ichi_rows()}</dl>'
              f'<p style="right:[[60]]; top:[[50]]; width:[[290]]; font-family:var(--sans); font-size:[[27]]; line-height:1.65">{C.HANDLING}</p>'
              f'<p class="hand" style="right:[[60]]; bottom:[[50]]; width:[[290]]; border:1px dashed currentColor; padding:[[14]] [[20]]; font-size:[[36]]; line-height:1.4">Batch 027<br>10/22</p>', "84%")
    wrapc = (f'<div style="width:40%; aspect-ratio:1; background:{NERI}; position:relative; box-shadow:0 10px 24px -8px rgba(58,54,49,.25); container-type:inline-size">'
             f'<span style="position:absolute; left:0; right:0; top:52%; height:14%; background:{ODO}"></span><div style="position:absolute; left:50%; top:24%; transform:translateX(-50%); width:56%">{L(M, "3a3631", "100%")}</div></div>')
    pack = (pf(still("ogg", "range", "21/9", zoom=1.45), "The range", "A band wraps the bottle: 間 in vertical Mincho, the mark, and the date written by kimy.", plate=False) +
            '<div class="grid g3" style="margin-top:clamp(20px,3vw,36px)">' +
            pf(band + back, "Band label and back label", "Matte, water-resistant. 一括表示 at 8 pt minimum; batch written by hand.", "1/1", pstyle="flex-direction:column; gap:7%") +
            pf(tag("［お名前］さんへ<br>ゆっくり、どうぞ。", "30%", "[[120]]"), "String tag", "Tied at the neck, written by kimy for each order.", "1/1") +
            pf(wrapc + tag("［お名前］さんへ", "17%", "[[130]]"), "Gift wrap", "Neri paper, one ochre band, the tag tied on.", "1/1", pstyle="align-items:flex-end; padding-bottom:16%") + '</div>')
    a5w = fitw(4 / 3, 148 / 210, .82)
    fl_f = ab(148, 210, ph("ogg", "single", "[[300]]", "[[250]]", "[[700]]", "1/1.25", zoom=2.4) +
              f'<div style="left:[[70]]; top:[[80]]">{L(M, "3a3631", "[[330]]")}</div>'
              f'<p class="vt jp" style="left:[[80]]; top:[[280]]; font-size:[[58]]; font-weight:600; letter-spacing:.14em; line-height:1.8">はじめての、<br>コンブチャ仕込み。</p>'
              f'<div style="left:0; bottom:0; width:[[620]]; height:[[330]]; background:{ODO}"></div>'
              f'<div style="left:[[90]]; bottom:[[200]]">' + note("少人数で、のんびり<br>仕込みましょう。<br>— kimy", "[[470]]", size="[[40]]", pad="[[40]]") + '</div>'
              f'<p class="hand" style="right:[[80]]; bottom:[[90]]; font-size:[[46]]">［月日］名古屋</p>', a5w, f"background:{GO}; color:{MI}")
    fl_b = ab(148, 210, f'<p class="jp" style="left:[[90]]; top:[[110]]; font-size:[[54]]">ワークショップのご案内</p>'
              f'<dl style="left:[[90]]; right:[[90]]; top:[[260]]; font-family:var(--sans); font-size:[[36]]; line-height:1.55; column-gap:[[40]]; row-gap:[[30]]">'
              + "".join(f'<dt style="color:{ODT}">{a}</dt><dd>{b}</dd>' for a, b in [("日時", "［月日（曜）時間］"), ("場所", "名古屋市［　］"), ("対象", "どなたでも"), ("定員", "［　］名（先着順）"), ("内容", "仕込みの体験と試飲"), ("参加費", "¥［　］（税込）"), ("申込方法", "Instagram DM / LINE")]) + '</dl>'
              f'<div class="row" style="left:[[90]]; bottom:[[100]]; gap:[[30]]">' + "".join(f'<span style="width:[[150]]; aspect-ratio:1; border:1px solid currentColor; display:flex; align-items:center; justify-content:center; font-size:[[24]]; letter-spacing:.2em">{q}</span>' for q in ("LINE", "IG")) + '</div>'
              f'<p class="hand" style="right:[[90]]; bottom:[[110]]; font-size:[[48]]; transform:rotate(-4deg)">お待ちしています。</p>', a5w, f"background:{GO}; color:{MI}")
    cw = fitw(4 / 3, 91 / 55, .34)
    card_f = ab(91, 55, f'<div style="left:[[70]]; bottom:[[70]]">{L(M, "3a3631", "[[330]]")}</div><span class="vt jp" style="right:[[70]]; top:[[70]]; font-size:[[40]]; letter-spacing:.34em">ナアウ</span>', cw, f"background:{GO}; color:{MI}")
    card_b = ab(91, 55, f'<p class="hand" style="left:[[70]]; top:[[70]]; font-size:[[60]]">またね。kimy</p><p style="left:[[70]]; bottom:[[70]]; font-family:var(--sans); font-size:[[32]]">名古屋市［　］ · @naau_kombucha</p>', cw, f"background:{ODO}; color:{MI}")
    prt = ('<div class="grid g2">' + pf(fl_f + fl_b, "A5 workshop flyer", "Vertical title, an ochre block and kimy’s note on the front; details in the standard order on the back.", "4/3") +
           pf(card_f + card_b, "Shop card, 91 × 55 mm", "Gofun front, ochre back with a handwritten line.", "4/3", pstyle="flex-direction:column; gap:7%") + '</div>')
    posts = [
        (ab(3, 4, ph("ogg", "range", "[[230]]", "[[90]]", "[[770]]", "1/1.32", zoom=2.3) + f'<p class="vt jp" style="left:[[80]]; top:[[110]]; font-size:[[50]]; letter-spacing:.34em">今週の仕込み</p>'
                  f'<p class="hand" style="left:[[80]]; bottom:[[90]]; font-size:[[48]]">No. 027 ［フレーバー］</p>', "100%", f"background:{GO}; color:{MI}", cls="flat post"), "Batch post", "Offset photograph, vertical caption."),
        (ab(3, 4, f'<div style="left:[[100]]; top:[[160]]">' + note("kombuchaが全てでは<br>ないけれど、<br>きっかけにはなるはず。<br>— kimy", "[[800]]", size="[[52]]", pad="[[70]]") + f'</div><div style="right:[[80]]; bottom:[[80]]">{L(M, "3a3631", "[[300]]")}</div>', "100%", f"background:{NERI}; color:{MI}", cls="flat post"), "Note post", "kimy’s words, by hand."),
        (ab(3, 4, f'<p class="vt jp" style="right:[[90]]; top:[[90]]; font-size:[[78]]; font-weight:600; letter-spacing:.24em">ワークショップ</p><p class="hand" style="left:[[80]]; top:[[100]]; font-size:[[52]]">［月日］名古屋</p>'
                  f'<div style="left:[[80]]; bottom:[[80]]">{L(M, "3a3631", "[[380]]")}</div>', "100%", f"background:{ODO}; color:{MI}", cls="flat post"), "Workshop post", "Ochre block, vertical title."),
    ]
    story = ab(9, 16, f'<div style="left:[[90]]; top:[[110]]">{L(M, "3a3631", "[[380]]")}</div>'
               f'<div style="left:[[90]]; right:[[90]]; top:[[560]]; padding:[[70]]; background:{GO}; transform:rotate(-2deg); box-shadow:0 10px 22px rgba(58,54,49,.12)"><p class="eyebrow" style="font-size:[[30]]; margin-bottom:[[30]]">Listening card</p>' +
               "".join(f'<p class="jp" style="padding:[[26]] 0; border-bottom:1px dashed #CDBFA6; font-size:[[48]]">{q}</p>' for q in ("よく眠れた？", "おなかの調子は？", "今日の気分は？")) +
               f'</div><p class="hand" style="left:[[90]]; bottom:[[120]]; font-size:[[52]]">ひとことで、返信してね。</p>', "100%", f"background:{NERI}; color:{MI}", cls="flat story")
    nts = notes(["The wordmark is shown from your Ogg setting with the ʻokina turned the right way; retype it with ‘ (U+2018) in Ogg for the font’s own mark.",
                 "Handwriting is set in Klee One as a stand-in until kimy’s hand is scanned."])
    direction_page(M, hero, idn, pal, typ, pack, prt, social("ogg", posts, story), nts)

def m_shell(content):
    return (f'<div class="shop" style="background:{GO}; color:{MI}"><header><nav class="wrap" aria-label="Shop" style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:14px; padding-top:26px; padding-bottom:26px">'
            f'<a href="ogg-home.html" aria-label="naʻau home">{L(M, "3a3631", "120px")}</a><div class="jp" style="display:flex; flex-wrap:wrap; gap:26px; font-size:14px">'
            f'<a href="ogg-product.html">お店</a><a href="ogg-home.html#listen">聴く</a><a href="#">ワークショップ</a><a href="#">かご (0)</a></div></nav></header>'
            f'<main>{content}</main><footer style="background:{NERI}; padding:56px 0 40px"><div class="wrap" style="display:flex; flex-wrap:wrap; gap:32px; justify-content:space-between; align-items:flex-end">'
            f'<div style="display:flex; flex-direction:column; gap:12px">{L(M, "3a3631", "110px")}<span class="hand" style="font-size:15px">またね。kimy</span></div>'
            f'<div class="jp" style="display:grid; grid-template-columns:repeat(2,minmax(140px,1fr)); gap:8px 32px; font-size:13px">{C.legal_links()}</div></div>'
            f'<div class="wrap"><p class="eyebrow" style="margin-top:32px">© 2026 naʻau kombucha · concept mockup</p></div></footer></div>')

def m_home():
    cards = "".join(f'<a href="ogg-product.html" style="display:flex; flex-direction:column; gap:12px; margin-top:{off}px">{still("ogg", "single", "3/4", zoom=2.3, flavours=(f,) * 3)}'
                    f'<span class="hand" style="font-size:18px">{f}</span><span style="font-size:14px">¥［　］（税込）</span></a>'
                    for f, off in zip(FL, (0, 72, 28)))
    content = (f'<section style="padding:clamp(16px,3vw,40px) 0 clamp(64px,9vw,120px)"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:clamp(28px,5vw,64px); align-items:end">'
               f'<div style="display:flex; gap:clamp(18px,3vw,44px); align-items:flex-start"><p class="vt jp" style="font-size:clamp(24px,2.8vw,34px); letter-spacing:.26em; line-height:1.9">からだの声に、耳を澄ます。</p>'
               f'<div style="display:flex; flex-direction:column; gap:22px; padding-top:44%"><p class="jp" style="line-height:2.1">飲むだけじゃない。自分の身体に気づく、kombucha。名古屋の台所から、ひと瓶ずつ。</p><a class="btn" href="ogg-product.html" style="align-self:flex-start">お店をのぞく</a></div></div>'
               f'<div style="position:relative; padding:0 0 48px 48px">{still("ogg", "pour", "4/5", zoom=1.9)}'
               f'<div style="position:absolute; left:0; bottom:0">' + note("今週は［素材］の仕込み。<br>やさしい酸味です。<br>— kimy", "230px", size="16px", pad="18px 20px") + '</div></div></div></section>'
               f'<section style="padding:0 0 clamp(64px,9vw,120px)"><div class="wrap"><div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:28px"><p class="jp" style="font-size:22px">今週の仕込み</p><a class="hand" href="ogg-product.html" style="font-size:16px">ぜんぶ見る →</a></div>'
               f'<div class="grid g3" style="align-items:start">{cards}</div></div></section>'
               f'<section id="listen" style="background:{ODO}; padding:clamp(64px,9vw,120px) 0"><div class="wrap" style="display:flex; flex-wrap:wrap; gap:clamp(32px,6vw,80px); align-items:center">'
               f'<p class="vt jp" style="font-size:clamp(24px,2.8vw,32px); font-weight:600; letter-spacing:.26em">開ける前に、ひと呼吸。</p>'
               f'<div style="flex:0 1 380px; padding:30px; background:{GO}; transform:rotate(-2deg); box-shadow:0 10px 22px rgba(58,54,49,.14)"><p class="eyebrow" style="margin-bottom:12px">Listening card · 毎回の注文に</p>' +
               "".join(f'<p class="jp" style="padding:12px 0; border-bottom:1px dashed #CDBFA6; font-size:16px">{q}</p>' for q in ("よく眠れた？", "おなかの調子は？", "今日の気分は？")) +
               '</div></div></section>'
               f'<section style="padding:clamp(64px,9vw,120px) 0"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr)); gap:clamp(32px,6vw,80px); align-items:center">'
               f'<div style="margin-top:40px">{still("ogg", "jar", "4/5", zoom=1.9)}</div>'
               f'<div style="display:flex; flex-direction:column; gap:18px"><p class="jp" style="font-size:clamp(24px,2.6vw,32px); line-height:1.6">名前は、直感で決めました。</p>'
               f'<p class="jp" style="line-height:2.1">直感kombucha、instinct kombucha、gut feeling kombucha。どれも違う。大好きなハワイの言葉で「直感」は naʻau。</p>'
               f'<p class="hand" style="font-size:18px">これしかない！と、秒で決定。— kimy</p><p class="jp" style="font-size:13px; color:#7A7268">看護師として働きながら、名古屋でコンブチャを仕込んでいます。</p></div></div></section>')
    return m_shell(content)

def m_product():
    content = (f'<section style="padding:clamp(16px,3vw,40px) 0 clamp(64px,9vw,120px)"><div class="wrap" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr)); gap:clamp(32px,5vw,72px); align-items:start">'
               f'<div style="position:relative; padding-bottom:40px">{still("ogg", "single", "4/5", zoom=1.9)}<div style="position:absolute; right:-6px; bottom:0; width:96px">{tag("［お名前］さんへ<br>ゆっくり、どうぞ。", "100%", "12px")}</div></div>'
               f'<div style="display:flex; gap:22px"><p class="vt jp" style="font-size:28px; letter-spacing:.2em">［フレーバー］</p><div style="flex:1; display:flex; flex-direction:column; gap:18px">'
               f'<span class="hand" style="font-size:17px">No. 027 · 14日発酵 · 330 ml</span><p style="font-size:26px">¥［　］<small style="font-size:14px">（税込）</small></p>'
               f'<p class="jp" style="line-height:2.1">紅茶と［素材］を、酵母と酢酸菌でゆっくり発酵させました。［味わいの説明］。</p>'
               f'<label style="display:flex; gap:10px; align-items:center; min-height:44px"><input type="checkbox" style="width:20px; height:20px; accent-color:{MI}"><span class="jp">kimy の手書きメッセージを添える</span></label>'
               f'<div style="display:flex; gap:10px"><label style="display:flex; flex-direction:column; gap:6px"><span class="eyebrow">数量</span><input type="number" value="1" min="1" style="width:80px; min-height:50px; border:1px solid {MI}; background:transparent; padding:0 10px"></label>'
               f'<button type="button" class="btn" style="align-self:flex-end; flex:1; background:{MI}; color:{GO}; border-color:{MI}">カートに入れる</button></div>'
               + C.commerce(f"background:{NERI}; padding:14px 16px; font-size:13px; line-height:1.9") + f'<div>{C.accordions("#DDD3C3")}</div>'
               f'<p class="jp" style="font-size:11px; color:#7A7268">※本品は清涼飲料水です。医薬品ではありません。</p></div></div></div></section>')
    return m_shell(content)

# ====================================================================== write
for d, build, home, product in ((S, s_dir, s_home, s_product), (P, p_dir, p_home, p_product), (M, m_dir, m_home, m_product)):
    build()
    C.page(f'{d["key"]}-home.html', f'naʻau — home ({d["name"]})', d["cls"], home())
    C.page(f'{d["key"]}-product.html', f'naʻau — product ({d["name"]})', d["cls"], product())
print("direction pages written")
