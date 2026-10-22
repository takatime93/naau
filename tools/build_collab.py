"""collab.html: naʻau × Ivycoast — KOM'BAR.

The full illustration appears once per piece at most (the box front, the hero). Everywhere else
the artwork is used as its ten separate elements. The front design belongs to the soap box alone.
"""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
import kombar as KB
import ink as K
from common import D, L, ab, pf, still, sec
C.SITE = sys.argv[1]

PEACH, INK, PAPER, GREEN, AMBER, KRAFT, MUTE = "#F4D9C6", "#1E1E1E", "#F6F1E9", "#144948", "#9C5B22", "#CDB48E", "#6E655B"
el, wm, art = KB.el, KB.wordmark, KB.artwork
IVY = lambda col, w, style="": f'<img src="assets/collab/ivycoast-wordmark-{col}.png" alt="IVYCOAST" style="width:{w}; display:block; {style}">'
IVYICON = lambda w: f'<img src="assets/collab/ivycoast-icon-green.png" alt="" style="width:{w}">'
OGGCOL = {"1e1e1e": "3a3631", "ffffff": "faf7f1"}
NAAU = lambda w, col="1e1e1e", style="": f'<img src="assets/logos/ogg-{OGGCOL.get(col, col)}.png" alt="naʻau" style="width:{w}; display:block; {style}">'
NAAU_CUR = lambda w, col="1e1e1e", style="": f'<img src="assets/logos/current-naau-{col}.png" alt="naʻau" style="width:{w}; display:block; {style}">'
SANS = "font-family:Inter, sans-serif"
JPB = "font-family:var(--sans); font-weight:700"

def lockup(w_naau, w_ivy, gap="[[16]]", align="flex-start", col="1e1e1e", ivy="dark"):
    return f'<div class="col" style="position:static; align-items:{align}; gap:{gap}">{NAAU(w_naau, col)}{IVY(ivy, w_ivy)}</div>'

def caps(text, size, extra=""):
    return f'<p style="{SANS}; font-size:{size}; letter-spacing:.18em; line-height:1.7; text-transform:uppercase; {extra}">{text}</p>'

def rows(items, size, col="rgba(30,30,30,.35)", pad="[[10]]", extra=""):
    return (f'<dl class="spec-rows" style="position:static; {SANS}; font-size:{size}; letter-spacing:.04em; border-bottom:1px solid {col}; {extra}">'
            + "".join(f'<dt style="padding:{pad} [[24]] {pad} 0; border-color:{col}; opacity:.62">{a}</dt><dd style="margin:0; padding:{pad} 0; border-color:{col}">{b}</dd>' for a, b in items) + '</dl>')

# ====================================================================== box faces (90 × 44 × 30 mm, to confirm)
BW, BH, BD = 90, 44, 30
STORY = ['コンブチャは、細菌と酵母が共に働くことで生まれる、伝統的な発酵茶です。', 'その発酵を支えるのが、SCOBY（スコビー）。<br>Symbiotic Culture of Bacteria and Yeast<br>細菌と酵母の共生培養体を意味します。', '発酵が進むにつれて、SCOBYはバクテリアセルロースからなる繊細な膜を育んでいきます。大切に育てたSCOBYを細かな粉末にし、やさしいスクラブとして石鹸に取り入れました。', '発酵から生まれた素材を、手仕事によって新たなかたちへ。丁寧に仕込んだコンブチャの発酵液と、このSCOBYの粉末を組み合わせ、発酵の物語を手づくりの石鹸へとつなぎました。', '時間をかけて育まれるものの豊かさ、変化することの美しさ、そして人の手から生まれるものへの敬意を込めて。']
CLOSE = "育てる時間。手をかけること。自然から学ぶこと。"
LABEL = [("品名", "化粧石けん"), ("内容量", "［　］g"), ("全成分", "［確認中］"), ("使用方法", "よく泡立てて使用し、洗い流す"), ("製造販売元", "［　］"), ("原産国", "日本")]

def face_front(w="100%"):
    """The front as designed by Ivycoast: wordmark, artwork, two lines of capitals."""
    return ab(BW, BH, f'<div style="left:[[66]]; top:[[46]]; width:[[64]]">{wm("100%", INK, "v")}</div>'
              f'<div style="left:[[152]]; top:[[42]]; width:[[392]]">{art("100%", INK)}</div>'
              + caps("Organic kombucha<br>cold processed bar soap", "[[16.5]]", "position:absolute; right:[[48]]; bottom:[[42]]; text-align:right; letter-spacing:.2em; line-height:1.9"),
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def bars(w, h):
    b = "".join(f'<i style="width:[[{t}]]; background:{INK}; height:100%"></i><i style="width:[[{g}]]"></i>' for t, g in
                [(2, 1), (1, 1), (1, 2), (3, 1), (1, 2), (2, 1), (1, 1), (2, 2), (1, 1), (3, 1), (1, 2), (1, 1), (2, 1), (1, 2), (3, 1), (1, 1), (2, 1), (1, 0)])
    return f'<div style="width:{w}; height:{h}; display:flex; background:{PAPER}; padding:[[6]] [[10]]">{b}</div>'

def face_back(w="100%"):
    """Back: the headline and the first lines of the story, the label in order, the three logos."""
    return ab(BW, BH, caps("Kombucha soap", "[[14]]", "position:absolute; left:[[48]]; top:[[40]]; letter-spacing:.24em")
              + f'<p style="left:[[48]]; top:[[70]]; {JPB}; font-size:[[34]]; line-height:1.3">発酵が生み出す美しさ。</p>'
              f'<p style="left:[[48]]; top:[[130]]; width:[[480]]; font-family:var(--sans); font-size:[[17]]; line-height:1.85">{STORY[0]}大切に育てたSCOBYを細かな粉末にし、やさしいスクラブとして石鹸に取り入れました。</p>'
              f'<p style="left:[[48]]; top:[[262]]; {JPB}; font-size:[[16]]; letter-spacing:.06em">{CLOSE}</p>'
              f'<div class="row" style="left:[[48]]; bottom:[[40]]; gap:[[18]]; align-items:center">{NAAU("[[120]]")}<span style="font-size:[[18]]">×</span>{IVY("dark", "[[130]]")}</div>'
              f'<div style="left:[[600]]; top:[[40]]; width:[[200]]">{wm("100%", INK)}</div>'
              f'<div style="left:[[600]]; right:[[48]]; top:[[100]]">' + rows(LABEL, "[[12.5]]", pad="[[5.5]]") + '</div>'
              f'<div style="right:[[48]]; bottom:[[58]]">{bars("[[170]]", "[[54]]")}</div>'
              f'<p style="right:[[48]]; bottom:[[38]]; width:[[170]]; {SANS}; font-size:[[11]]; letter-spacing:.3em; text-align:center">4 ［　　　　　　］</p>',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def insert_card(w="100%"):
    """The whole story on a card inside the lid, 85 × 120 mm, with the three logos."""
    paras = "".join(f'<p style="position:static; margin:0 0 [[24]]">{t}</p>' for t in STORY)
    return ab(85, 120, caps("Kombucha soap", "[[22]]", "position:absolute; left:[[80]]; top:[[80]]; letter-spacing:.24em")
              + f'<div style="right:[[80]]; top:[[72]]; width:[[300]]">{wm("100%", INK)}</div>'
              f'<p style="left:[[80]]; top:[[170]]; {JPB}; font-size:[[60]]; line-height:1.35">発酵が生み出す美しさ。</p>'
              f'<div style="left:[[80]]; right:[[80]]; top:[[300]]; font-family:var(--sans); font-size:[[25]]; line-height:1.9">{paras}</div>'
              f'<p style="left:[[80]]; top:[[1050]]; {JPB}; font-size:[[28]]; letter-spacing:.06em; line-height:1.7">育てる時間。<br>手をかけること。<br>自然から学ぶこと。</p>'
              f'<div style="right:[[-70]]; bottom:[[-60]]; width:[[380]]">{el("mother", "100%", INK)}</div>'
              f'<div class="row" style="left:[[80]]; bottom:[[70]]; gap:[[24]]; align-items:center">{NAAU("[[170]]")}<span style="font-size:[[26]]">×</span>{IVY("dark", "[[190]]")}</div>',
              w, f"background:{PAPER}; color:{INK}")

def face_end(name, num, jp, en, w="100%", bg=PEACH, ink=INK):
    """End panel, 30 × 60: one element and one line, in sequence."""
    return ab(BD, BH, f'<p style="left:[[90]]; top:[[80]]; {SANS}; font-size:[[70]]; letter-spacing:.1em">{num}</p>'
              f'<p style="right:[[90]]; top:[[70]]; {JPB}; font-size:[[110]]">{jp}</p>'
              f'<div style="left:[[110]]; right:[[110]]; top:50%; transform:translateY(-50%); display:flex; justify-content:center">{el(name, "100%", ink)}</div>'
              + caps(en, "[[50]]", "position:absolute; left:[[90]]; right:[[90]]; bottom:[[80]]; line-height:1.4"),
              w, f"background:{bg}; color:{ink}", cls="flat")

def face_top(w="100%"):
    return ab(3, 1, f'<div style="left:[[46]]; top:50%; transform:translateY(-50%); width:[[300]]">{wm("100%", INK)}</div>'
              f'<div style="right:[[60]]; top:[[34]]; bottom:[[34]]; display:flex; align-items:center; gap:[[26]]">{el("tea", "auto", INK, "height:[[260]]; width:auto")}'
              f'<div class="col" style="position:static; gap:[[6]]"><p style="{SANS}; font-size:[[30]]; letter-spacing:.1em">01 · 茶</p>' + caps("It begins with tea", "[[22]]") + '</div></div>',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def face_bottom(w="100%"):
    return ab(3, 1, f'<div style="left:[[60]]; top:50%; transform:translateY(-50%); display:flex; align-items:center; gap:[[24]]">{el("sun", "[[180]]", INK)}'
              f'<div class="col" style="position:static; gap:[[6]]"><p style="{SANS}; font-size:[[30]]; letter-spacing:.1em">03 · 日</p>' + caps("Cured ［　］ weeks", "[[22]]") + '</div></div>'
              f'<p style="right:[[60]]; top:50%; transform:translateY(-50%); {SANS}; font-size:[[22]]; letter-spacing:.2em; text-align:right; line-height:1.8">MADE IN JAPAN<br>LOT ［　　　］</p>',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def dieline():
    """Flat net: side | front | side | back | glue; lid above the front, base below the back."""
    U, H, D, W = 4, BH, BD, BW
    X = {"sl": 0, "fr": D, "sr": D + W, "bk": 2 * D + W, "gl": 2 * D + 2 * W}
    T = 12                               # tuck flap
    Y = {"tp": T, "bd": T + D, "bt": T + D + H}
    TOT_W, TOT_H = 2 * D + 2 * W + 10, T + 2 * D + H + T
    def at(x, y, w_mm, inner):
        return f'<div style="left:[[{x * U * 1000 / (TOT_W * U):.1f}]]; top:[[{y * 1000 / TOT_W:.1f}]]; width:[[{w_mm * 1000 / TOT_W:.1f}]]">{inner}</div>'
    faces = (at(X["sl"], Y["bd"], D, face_end("bird", "04", "鳥", "Ivycoast,<br>by hand", "100%")) +
             at(X["fr"], Y["bd"], W, face_front("100%")) +
             at(X["sr"], Y["bd"], D, face_end("mother", "02", "母", "The<br>mother", "100%")) +
             at(X["bk"], Y["bd"], W, face_back("100%")) +
             at(X["fr"], Y["tp"], W, face_top("100%")) +
             at(X["bk"], Y["bt"], W, face_bottom("100%")))
    fr, sr, bk, gl, bd, bt = X["fr"], X["sr"], X["bk"], X["gl"], Y["bd"], Y["bt"]
    cut, fold = INK, "#9C5B22"
    lines = (f'<svg viewBox="0 0 {TOT_W} {TOT_H}" style="left:0; top:0; width:100%; height:100%; overflow:visible" aria-hidden="true">'
             f'<g fill="{PEACH}" stroke="{cut}" stroke-width=".25">'
             f'<path d="M{fr} {T} Q{fr} 0 {fr + 12} 0 H{sr - 12} Q{sr} 0 {sr} {T} Z"/>'
             f'<path d="M{bk} {bt + D} V{bt + D + T} H{gl} V{bt + D} Z"/>'
             f'<path d="M0 {bd} L4 {bd - 12} H{D - 4} L{D} {bd} Z M{sr} {bd} L{sr + 4} {bd - 12} H{bk - 4} L{bk} {bd} Z"/>'
             f'<path d="M0 {bt} L4 {bt + 12} H{D - 4} L{D} {bt} Z M{sr} {bt} L{sr + 4} {bt + 12} H{bk - 4} L{bk} {bt} Z"/>'
             f'<path d="M{gl} {bd + 2} L{gl + 10} {bd + 6} V{bt - 6} L{gl} {bt - 2} Z"/></g>'
             f'<g fill="none" stroke="{fold}" stroke-width=".3" stroke-dasharray="1.4 1"><path d="M{fr} {bd} V{bt} M{sr} {bd} V{bt} M{bk} {bd} V{bt} M{gl} {bd + 2} V{bt - 2} M{fr} {bd} H{sr} M{bk} {bt} H{gl} M{fr} {T} H{sr} M{bk} {bt + D} H{gl}"/></g>'
             f'<g font-family="Inter, sans-serif" font-size="2.6" letter-spacing=".3" fill="{MUTE}">'
             f'<text x="{bk + 10}" y="8">— CUT</text><line x1="{bk}" y1="7" x2="{bk + 8}" y2="7" stroke="{cut}" stroke-width=".3"/>'
             f'<text x="{bk + 36}" y="8">— FOLD</text><line x1="{bk + 26}" y1="7" x2="{bk + 34}" y2="7" stroke="{fold}" stroke-width=".35" stroke-dasharray="1.4 1"/>'
             f'<text x="{bk + 10}" y="14">{W} × {H} × {D} MM · ［TO CONFIRM］</text></g></svg>')
    return ab(TOT_W, TOT_H, lines + faces, "100%", "background:transparent", cls="flat")

def box3d(width_cqw=46, rx=-18, ry=-34, tilt=0):
    """A CSS box from the same faces: front, right end, lid."""
    F = width_cqw; H = F * BH / BW; Dp = F * BD / BW
    face = lambda w, h, tf, inner: (f'<div style="position:absolute; left:{-w / 2:.2f}cqw; top:{-h / 2:.2f}cqw; width:{w:.2f}cqw; height:{h:.2f}cqw; transform:{tf}; backface-visibility:hidden">{inner}</div>')
    return (f'<div style="position:absolute; left:50%; top:52%; transform-style:preserve-3d; transform:rotateX({rx}deg) rotateY({ry}deg) rotateZ({tilt}deg)">'
            + face(F, H, f"translateZ({Dp / 2:.2f}cqw)", face_front("100%"))
            + face(Dp, H, f"rotateY(90deg) translateZ({F / 2:.2f}cqw)", f'<div style="filter:brightness(.9)">{face_end("mother", "02", "母", "The<br>mother", "100%")}</div>')
            + face(F, Dp, f"rotateX(90deg) translateZ({H / 2:.2f}cqw)", f'<div style="filter:brightness(1.04)">{face_top("100%")}</div>')
            + '</div>')

# ====================================================================== hero
hero = (f'<header class="kb2"><div class="wrap kb2-grid">'
        f'<div class="kb2-text"><p class="kb-eyebrow">naʻau × Ivycoast · 2026</p>'
        f'<div class="kb2-wm">{wm("100%", INK)}</div>'
        f'<p class="kb2-def"><b>KOM</b>bucha + <b>BAR</b> soap</p>'
        f'<p class="kb-jp">発酵が生み出す美しさ。</p><p class="kb-en">A cold-process bar soap made with naʻau’s kombucha and the SCOBY that brews it.</p>'
        f'<div class="kb2-lock">{NAAU("128px")}<span>×</span>{IVY("dark", "150px")}</div></div>'
        f'<div class="kb2-art">{el("mother", "100%", INK)}</div>'
        f'</div></header>')

TOC = [("01", "brands", "Two brands, one ritual"), ("02", "product", "The product"), ("03", "elements", "The artwork, taken apart"), ("04", "system", "Colour, type and space"),
       ("05", "packaging", "Packaging"), ("06", "print", "Print"), ("07", "social", "Social"), ("08", "web", "Website"), ("09", "language", "Website language"),
       ("10", "ties", "How it ties to each direction"), ("11", "borrowed", "What we borrowed"), ("12", "roles", "Who does what")]
intro = ('<section class="wrap kb-intro">'
         '<p class="kb-lead">Ivycoast brings Australian botanicals into Japanese homes for daily rituals. naʻau brews kombucha in Nagoya to help people listen to their bodies. Together we made a soap.</p>'
         '<div><p class="muted">For both teams: the product, how we use its artwork, and every piece we plan to make, from the box to the website.</p>'
         '<ol class="toc">' + "".join(f'<li><a href="#{a}"><span>{n}</span>{t}</a></li>' for n, a, t in TOC) + '</ol></div></section>')

# ====================================================================== 01 brands, 02 product (unchanged in substance)
brands = ('<div class="pair">'
          f'<div class="side"><div class="side-mark">{IVYICON("38px")}{IVY("green", "170px")}</div>'
          '<p class="side-lead">Australian botanicals, brought into Japanese homes for daily rituals.</p>'
          '<dl class="facts"><dt>Voice</dt><dd>Calm and considered; ordinary moments, elevated just enough.</dd><dt>Language</dt><dd>English-led, with Japanese.</dd><dt>Look</dt><dd>Cream and deep green, a flared serif, beach light.</dd></dl></div>'
          '<div class="join" aria-hidden="true">×</div>'
          f'<div class="side"><div class="side-mark">{NAAU("124px")}</div>'
          '<p class="side-lead">Small-batch kombucha, brewed in Nagoya by kimy.</p>'
          '<dl class="facts"><dt>Voice</dt><dd>Warm, personal and a little playful.</dd><dt>Language</dt><dd>Japanese-led, with English.</dd><dt>Look</dt><dd>Being decided: see <a href="index.html">the overview</a>.</dd></dl></div>'
          '</div>'
          '<div class="shared"><p class="eyebrow" style="color:#6E655B">Where they meet</p><div class="shared-grid">' +
          "".join(f'<div><span class="jp">{e}</span><h3>{t}</h3><p>{b}</p></div>' for e, t, b in [
              ("儀式", "Ritual", "Small acts of care, repeated every day."),
              ("時間", "Time", "Kombucha ferments for weeks; cold-process soap cures for weeks."),
              ("素材", "Materials", "Natural ingredients, chosen carefully."),
              ("手", "Hands", "Made by hand, in small batches.")]) + '</div></div>')

product = ('<div class="grid g2" style="align-items:start">'
           + pf(face_front("100%"), "Front, as designed", "Kept exactly: the vertical wordmark, the full artwork, two lines of capitals.", plate=False)
           + pf(face_back("100%"), "Back, new", "The headline and the first lines of the story; the label in order; naʻau (Concept B), Ivycoast and KOM’BAR.", plate=False)
           + '</div><div class="grid g-wide" style="margin-top:clamp(24px,3vw,40px); align-items:center">'
           + pf(f'<div style="width:46%">{insert_card("100%")}</div>', "Story card inside the lid, 85 × 120 mm", "The full text, legible at 6 pt and above; the mother cropped off the corner.", "1/1")
           + '<dl class="facts facts-lg"><dt>Name</dt><dd>KOM’BAR: <b>KOM</b>bucha + <b>BAR</b> soap</dd><dt>Product</dt><dd>Organic kombucha cold-processed bar soap</dd><dt>Made with</dt><dd>naʻau kombucha ferment, and SCOBY powder as a gentle scrub</dd>'
           '<dt>Made by</dt><dd>Ivycoast, by hand</dd><dt>Box</dt><dd>90 × 44 × 30 mm ［to confirm］</dd><dt>Weight</dt><dd>［　g］</dd><dt>全成分</dt><dd>［to confirm］</dd></dl></div>')

# ====================================================================== 03 elements
FIELDS = [(PEACH, INK), (GREEN, PEACH), (PAPER, INK), (INK, PEACH), (KRAFT, INK), (AMBER, PAPER),
          (PAPER, GREEN), (PEACH, GREEN), (GREEN, PAPER), (PAPER, AMBER)]
def tile(i, name):
    _, jp, en, meaning = KB.ELEMENTS[name]
    bg, fg = FIELDS[i]
    return (f'<figure class="kel"><div class="kel-card" style="background:{bg}; color:{fg}"><span class="kel-n">{i + 1:02d}</span><span class="kel-jp">{jp}</span>'
            f'<div class="kel-art">{el(name, "auto", fg, "height:100%; width:auto; max-width:100%")}</div></div>'
            f'<figcaption><b>{en}</b><span>{meaning}</span></figcaption></figure>')

elements = ('<p class="lead-p">The illustration stays whole on the front of the soap box, and only there. Everywhere else we use it the way a printer would use a set of blocks: one element at a time, large, in one ink on one colour. Ten elements come out of the artwork, each with something to say.</p>'
            '<div class="kel-grid">' + "".join(tile(i, n) for i, n in enumerate(KB.ORDER)) + '</div>'
            '<p class="muted" style="font-size:14px; margin-top:18px">Element files: <code>assets/collab/elements/01-mother.svg</code> to <code>10-ginger.svg</code>, cut from the original artwork without redrawing; the tea leaves and the sprig are set side by side as one element. Meanings are proposals for both teams to agree.</p>')

# ====================================================================== 04 colour, type, space
PAL = [("Peach", PEACH, "The KOM’BAR stock. Always present.", 3), ("Ink", INK, "Artwork and text.", 2), ("Paper", PAPER, "Insides, cards, web ground.", 2),
       ("Coast green", GREEN, "From Ivycoast.", 1.4), ("Amber", AMBER, "From naʻau’s glass.", 1), ("Kraft", KRAFT, "Shipping and gift.", 1)]
pairs = "".join(f'<div class="pair-sw" style="background:{bg}; color:{fg}">{el(e, "auto", fg, "height:62%; width:auto")}<span>{lab}</span></div>' for bg, fg, e, lab in [
    (PEACH, INK, "lemon", "Ink on peach · 13.4:1"), (GREEN, PEACH, "bird", "Peach on green · 8.6:1"), (PAPER, GREEN, "tea", "Green on paper · 10.1:1"),
    (INK, PEACH, "scoby", "Peach on ink · 13.4:1"), (KRAFT, INK, "ginger", "Ink on kraft · 9.5:1"), (AMBER, PAPER, "sun", "Paper on amber · 5.6:1")])
type_card = ab(16, 9, f'<div style="left:[[60]]; top:[[60]]; width:[[440]]">{wm("100%", INK)}</div>'
               f'<p style="left:[[60]]; top:[[160]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">WORDMARK · KOMBUCHA + BAR SOAP</p>'
               f'<p style="left:[[60]]; top:[[230]]; {JPB}; font-size:[[44]]; line-height:1.4">発酵が生み出す美しさ。</p>'
               f'<p style="left:[[60]]; top:[[320]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">JAPANESE · ZEN KAKU GOTHIC NEW, BOLD</p>'
               f'<p class="it" style="left:[[60]]; top:[[370]]; font-family:var(--lat); font-size:[[40]]">Time to grow. Care by hand.</p>'
               f'<p style="left:[[60]]; top:[[430]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">VOICE · EB GARAMOND ITALIC, ONE LINE ONLY</p>'
               + caps("Organic kombucha cold processed bar soap", "[[24]]", f"position:absolute; left:[[60]]; top:[[480]]")
               + f'<p style="left:[[60]]; top:[[520]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">CAPTIONS · INTER, TRACKED CAPITALS</p>'
               f'<div style="right:[[60]]; top:[[60]]; width:[[360]]">' + rows([("WITH", "kombucha + SCOBY"), ("MADE BY", "Ivycoast"), ("CURED", "［　］ weeks"), ("WEIGHT", "［　］ g")], "[[17]]", pad="[[8]]") + '</div>'
               f'<p style="right:[[60]]; top:[[250]]; width:[[360]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">DETAILS · INTER, RULED ROWS</p>'
               f'<div style="right:[[-30]]; bottom:[[-110]]; width:[[250]]">{el("tea", "100%", GREEN)}</div>',
               "100%", f"background:{PAPER}; color:{INK}", cls="flat")
system = ('<div class="sub" style="margin-top:0"><h3>Colour</h3><p>Peach is always there. One partner colour per piece, never more than two inks.</p></div>'
          + C.chips([(n, h, r, w) for n, h, r, w in PAL]) +
          f'<div class="pairs">{pairs}</div>'
          '<div class="sub"><h3>Type</h3><p>The KOM’BAR wordmark is the only display type. Everything else is quiet.</p></div>'
          + pf(type_card, "Type hierarchy", "Five voices, each with one job.", plate=False))

# ====================================================================== 05 packaging
def band(no, date, ink):
    """A narrow peach band for the bare bar, dated with a Japanese round date stamp."""
    bar = (f'<div style="left:[[110]]; right:[[110]]; top:[[150]]; bottom:[[150]]; background:#E7D7BF; border-radius:[[22]]; box-shadow:inset 0 [[-8]] [[16]] rgba(120,90,60,.18), 0 [[16]] [[30]] rgba(60,40,30,.18)"></div>')
    strip = (f'<div class="ab flat" style="left:[[110]]; right:[[110]]; top:[[380]]; height:[[150]]; background:{PEACH}; color:{INK}; box-shadow:0 [[4]] [[10]] rgba(0,0,0,.12); overflow:visible">'
             f'<div style="left:[[60]]; top:50%; transform:translateY(-50%); width:[[330]]">{wm("100%", INK)}</div>'
             f'<p style="left:[[60]]; bottom:[[-180]]; {SANS}; font-size:[[24]]; letter-spacing:.2em; color:{MUTE}">CURE {no}</p></div>'
             f'<div style="right:[[150]]; top:[[300]]; width:[[230]]; transform:rotate(-8deg)">{K.date_stamp("100%", "名古屋", date, "CURE " + no, ink)}</div>')
    return ab(1, 1, bar + strip, "100%", "background:transparent", cls="flat")

bands = ('<div class="grid g3">' + band("01", "26.11.03", GREEN) + band("02", "26.11.24", INK) + band("03", "26.12.15", AMBER) + '</div>')

def mailer():
    """Kraft lid: the route the kombucha takes, from Nagoya to the Ivycoast studio."""
    route = (f'<svg viewBox="0 0 1000 750" style="left:0; top:0; width:100%; height:100%" aria-hidden="true">'
             f'<path d="M150 560 C260 420 380 610 500 470 C610 340 720 520 850 250" fill="none" stroke="{GREEN}" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round"/>'
             f'<circle cx="150" cy="560" r="14" fill="{GREEN}"/><circle cx="850" cy="250" r="14" fill="none" stroke="{GREEN}" stroke-width="5"/></svg>')
    return ab(4, 3, f'<div class="fill" style="background:{KRAFT}"></div>' + route +
              f'<p style="left:[[80]]; top:[[620]]; {JPB}; font-size:[[30]]">名古屋</p>' + caps("naʻau kombucha", "[[18]]", "position:absolute; left:[[80]]; top:[[662]]") +
              f'<p style="right:[[80]]; top:[[160]]; {JPB}; font-size:[[30]]; text-align:right">［　］</p>' + caps("Ivycoast studio", "[[18]]", "position:absolute; right:[[80]]; top:[[205]]") +
              f'<div style="left:[[430]]; top:[[330]]; width:[[150]]; transform:rotate(-14deg)">{el("bird", "100%", GREEN)}</div>'
              f'<div class="ab flat" style="left:[[80]]; top:[[70]]; width:[[300]]; aspect-ratio:3/2; background:{PEACH}; color:{INK}; box-shadow:0 [[3]] [[8]] rgba(0,0,0,.12)">'
              f'<div style="left:[[70]]; top:[[80]]; width:[[600]]">{wm("100%", INK)}</div>'
              + caps("To ［　　　　］ 様", "[[50]]", "position:absolute; left:[[70]]; top:[[320]]; letter-spacing:.06em") + '</div>',
              "100%", "background:transparent", cls="flat")

def mailer_inside():
    return ab(4, 3, f'<div class="fill" style="background:{PEACH}"></div><div style="left:[[-60]]; bottom:[[-200]]; width:[[600]]">{el("sun", "100%", INK)}</div>'
              f'<p style="right:[[80]]; top:[[110]]; {JPB}; font-size:[[56]]; line-height:1.5; text-align:right; white-space:nowrap">ひらいてくれて、<br>ありがとう。</p>'
              f'<p class="it" style="right:[[80]]; top:[[320]]; font-family:var(--lat); font-size:[[30]]; text-align:right">Thank you for opening this.</p>'
              f'<div style="right:[[80]]; bottom:[[70]]">{lockup("[[120]]", "[[150]]", "[[10]]", "flex-end")}</div>',
              "100%", "background:transparent", cls="flat")

def tissue():
    """A regular half-drop repeat of one element, like a printed textile."""
    cells = ""
    for r in range(6):
        for c in range(7):
            x = c * 160 + (80 if r % 2 else 0) - 40
            cells += f'<div style="left:[[{x}]]; top:[[{r * 140 - 40}]]; width:[[96]]; transform:rotate({0 if r % 2 else 180}deg)">{el("tea", "100%", GREEN)}</div>'
    return ab(4, 3, cells, "100%", f"background:{PAPER}", cls="flat")

def kakegami():
    return ab(4, 3, f'<div class="fill" style="background:{KRAFT}"></div>'
              f'<div style="left:[[-90]]; top:[[-60]]; width:[[640]]; transform:rotate(12deg)">{el("bird", "100%", GREEN)}</div>'
              f'<div class="ab flat" style="right:[[160]]; top:0; bottom:0; width:[[190]]; background:{PEACH}; color:{INK}; box-shadow:[[-4]] 0 [[10]] rgba(0,0,0,.12)">'
              f'<p class="vt" style="left:50%; top:[[60]]; transform:translateX(-50%); {JPB}; font-size:[[120]]; letter-spacing:.1em">おくりもの</p>'
              f'<div style="left:[[300]]; right:[[300]]; bottom:[[90]]">{el("lemon", "100%", INK)}</div></div>'
              f'<div style="left:[[70]]; bottom:[[60]]">{lockup("[[120]]", "[[150]]", "[[10]]")}</div>'
              + caps("KOM’BAR + naʻau kombucha 330 ml", "[[18]]", "position:absolute; left:[[70]]; bottom:[[210]]"),
              "100%", "background:transparent", cls="flat")

packaging = ('<div class="sub" style="margin-top:0"><h3>The box, flat</h3><p>Every panel has a job. The ends tell the story in order: 01 tea, 02 the mother, 03 time, 04 Ivycoast.</p></div>'
             + pf(dieline(), "Dieline, 90 × 44 × 30 mm", "Front as designed; back, ends, lid and base new. Sizes to confirm with Ivycoast’s printer.", plate=False) +
             '<div class="grid g-wide" style="margin-top:clamp(24px,3vw,40px); align-items:stretch">'
             + pf(f'<div style="position:absolute; inset:0; container-type:inline-size; perspective:1600px">{box3d(48)}</div>', "The box, assembled", "Front, the mother on the end, tea on the lid.", "4/3", pstyle=f"background:linear-gradient(180deg,#EFE6DA 0 64%,#E3D6C6 64%)")
             + pf(face_back("100%"), "Back panel", "The story’s opening and closing lines; the label in order; the three logos.", plate=False, style="justify-content:center")
             + '</div>'
             '<div class="sub"><h3>Batch bands</h3><p>For the bare bar at markets and the naʻau counter: a narrow band, dated by hand with a round date stamp for each cure.</p></div>' + bands +
             '<div class="sub"><h3>Shipping and gifts</h3><p>Kraft outside, peach inside. The tissue repeats one element; the gift set gets a Japanese paper band.</p></div>'
             '<div class="grid g2">' + pf(mailer(), "Mailer, outside", "The route across the lid: from naʻau in Nagoya to the Ivycoast studio, with a peach address label.", plate=False) + pf(mailer_inside(), "Mailer, inside the lid", "The first thing you read when it opens.", plate=False)
             + pf(tissue(), "Tissue paper", "One element, the tea leaf, in a regular half-drop repeat; every other row turned.", plate=False) + pf(kakegami(), "Gift set, with a paper band", "KOM’BAR and a bottle of naʻau, wrapped with a peach 掛け紙 band.", plate=False) + '</div>')

# ====================================================================== 06 print
def story_card(no, name, jp, line_jp, line_en, bg, fg, cw=820):
    return ab(55, 91, f'<p style="left:[[80]]; top:[[80]]; {SANS}; font-size:[[60]]; letter-spacing:.1em">{no}</p><p style="right:[[80]]; top:[[60]]; {JPB}; font-size:[[150]]">{jp}</p>'
              f'<p style="left:[[80]]; top:[[300]]; right:[[80]]; {JPB}; font-size:[[78]]; line-height:1.5">{line_jp}</p>'
              f'<p class="it" style="left:[[80]]; top:[[560]]; right:[[80]]; font-family:var(--lat); font-size:[[54]]; line-height:1.35">{line_en}</p>'
              f'<div style="right:[[-120]]; bottom:[[-200]]; width:[[{cw}]]">{el(name, "100%", fg)}</div>',
              "23%", f"background:{bg}; color:{fg}")

cards = (story_card("01", "tea", "茶", "はじまりは、<br>お茶。", "It begins<br>with tea.", PAPER, GREEN, 1000) +
         story_card("02", "mother", "母", "SCOBYは、<br>コンブチャの母。", "The SCOBY is<br>the mother.", PEACH, INK) +
         story_card("03", "sun", "日", "石鹸になるまで、<br>数週間。", "Weeks of<br>curing.", AMBER, PAPER) +
         story_card("04", "bird", "鳥", "海辺の工房で、<br>手で切る。", "Cut by hand<br>by the coast.", GREEN, PEACH))

counter = ab(105, 148, f'<p style="left:[[80]]; top:[[90]]; {JPB}; font-size:[[78]]; line-height:1.45">コンブチャから、<br>石鹸ができました。</p>'
             f'<p class="it" style="left:[[80]]; top:[[330]]; font-family:var(--lat); font-size:[[40]]">Kombucha, made into soap.</p>'
             f'<div style="right:[[-160]]; bottom:[[-120]]; width:[[900]]">{el("mother", "100%", INK)}</div>'
             f'<div style="left:[[80]]; bottom:[[80]]; width:[[380]]">{wm("100%", INK)}</div>'
             + caps("¥［　］ · 税込", "[[26]]", "position:absolute; left:[[80]]; bottom:[[170]]"),
             "100%", f"background:{PEACH}; color:{INK}")

poster = ab(297, 420, f'<div style="left:[[70]]; right:[[70]]; top:[[80]]">{wm("100%", PEACH)}</div>'
            + caps("<b>KOM</b>bucha + <b>BAR</b> soap", "[[22]]", f"position:absolute; left:[[70]]; top:[[250]]; color:{PEACH}")
            + f'<p style="left:[[70]]; top:[[340]]; {JPB}; font-size:[[56]]; line-height:1.5; color:{PEACH}">発酵が生み出す美しさ。</p>'
            f'<div style="left:[[70]]; right:[[70]]; top:[[460]]; color:{PEACH}">' + rows([("発売", "［月日］"), ("取扱", "naʻau 名古屋 · Ivycoast online"), ("価格", "¥［　］（税込）")], "[[24]]", "rgba(244,217,198,.4)", "[[14]]") + '</div>'
            f'<div style="left:[[70]]; top:[[700]]; display:flex; gap:[[24]]; align-items:center; color:{PEACH}">{NAAU("[[170]]", "ffffff")}<span style="font-size:[[28]]">×</span>{IVY("white", "[[190]]")}</div>'
            f'<div style="left:[[100]]; right:[[100]]; top:[[960]]">{el("sun", "100%", PEACH)}</div>',
            "100%", f"background:{GREEN}; color:{PEACH}")

print_ = ('<div class="sub" style="margin-top:0"><h3>Story cards, 55 × 91 mm</h3><p>Four cards inside each box: how a cup of tea becomes a bar of soap.</p></div>'
          + pf(f'<div style="display:flex; gap:2.5%; justify-content:center; align-items:flex-start; width:100%">{cards}</div>', "Story cards, front", "One element each, cropped off the bottom; one line in Japanese, one in English.", "21/9")
          + '<div class="grid g2" style="margin-top:clamp(24px,3vw,40px)">'
          + pf(f'<div style="width:46%">{counter}</div>', "Counter card, A6", "At the naʻau counter and Ivycoast stockists.", "1/1")
          + pf(f'<div style="width:50%">{poster}</div>', "Launch poster, A3", "For the shop window: the wordmark across the top, what it stands for, and the sun rising from the bottom edge.", "1/1") + '</div>')

# ====================================================================== 07 social
def post(inner, bg, fg=INK):
    return ab(3, 4, inner, "100%", f"background:{bg}; color:{fg}", cls="flat post")

p_reveal = post(f'<div style="left:[[110]]; top:[[230]]; width:[[780]]; transform:rotate(-4deg); box-shadow:0 [[30]] [[50]] rgba(60,40,30,.28)">{face_front("100%")}</div>'
                f'<div style="left:[[70]]; right:[[70]]; bottom:[[90]]">{wm("100%", INK)}</div>' + caps("naʻau × Ivycoast · ［月日］", "[[24]]", "position:absolute; left:[[70]]; top:[[80]]"), PAPER)
p_sun = post(f'<div style="right:[[-250]]; top:[[-220]]; width:[[900]]">{el("sun", "100%", PEACH)}</div>'
             f'<p style="left:[[70]]; bottom:[[220]]; {JPB}; font-size:[[90]]; line-height:1.4; color:{PEACH}">四週間、<br>待ちました。</p>'
             f'<p class="it" style="left:[[70]]; bottom:[[150]]; font-family:var(--lat); font-size:[[40]]; color:{PEACH}">Cured for four weeks.</p>'
             f'<div style="left:[[70]]; bottom:[[70]]; width:[[260]]">{wm("100%", PEACH)}</div>', GREEN)
p_mother = post(f'<div style="left:[[-120]]; bottom:[[-140]]; width:[[820]]">{el("mother", "100%", INK)}</div>'
                f'<p style="right:[[70]]; top:[[90]]; {JPB}; font-size:[[78]]; line-height:1.45; text-align:right">SCOBYは、<br>コンブチャの<br>「母」。</p>'
                f'<p class="it" style="right:[[70]]; top:[[440]]; font-family:var(--lat); font-size:[[36]]; text-align:right">Brewers call it the mother.</p>', PEACH)

def panorama():
    S = 1000  # one slide = 1000 units of a 5000-wide strip
    steps = [("01", "茶", "Tea"), ("02", "菌", "SCOBY"), ("03", "母", "The mother"), ("04", "日", "Cure"), ("05", "鳥", "Ivycoast")]
    labels = "".join(f'<p style="left:[[{i * S + 70}]]; top:[[80]]; {SANS}; font-size:[[40]]; letter-spacing:.12em">{n}</p>'
                     f'<p style="left:[[{i * S + 70}]]; top:[[140]]; {JPB}; font-size:[[110]]">{jp}</p>'
                     + caps(en, "[[34]]", f"position:absolute; left:[[{i * S + 70}]]; top:[[290]]") for i, (n, jp, en) in enumerate(steps))
    art_ = (f'<svg viewBox="0 0 5000 1250" style="left:0; top:0; width:[[5000]]; height:[[1250]]" aria-hidden="true"><path d="M300 1080 C900 1180 1300 700 1900 900 C2500 1100 2900 800 3500 980 C4000 1120 4300 900 4900 980" fill="none" stroke="{GREEN}" stroke-width="10" stroke-dasharray="4 26" stroke-linecap="round"/></svg>'
            f'<div style="left:[[200]]; top:[[420]]; width:[[640]]">{el("tea", "100%", INK)}</div>'
            f'<div style="left:[[1250]]; top:[[420]]; width:[[520]]">{el("scoby", "100%", INK)}</div>'
            f'<div style="left:[[2250]]; top:[[300]]; width:[[640]]">{el("mother", "100%", INK)}</div>'
            f'<div style="left:[[3300]]; top:[[330]]; width:[[520]]">{el("sun", "100%", AMBER)}</div>'
            f'<div style="left:[[4250]]; top:[[420]]; width:[[640]]">{el("bird", "100%", INK)}</div>'
            f'<div style="left:[[4620]]; top:[[1080]]; width:[[310]]">{wm("100%", INK)}</div>')
    import re
    return re.sub(r"\[\[(-?\d+(?:\.\d+)?)\]\]", lambda m: f"[[{float(m.group(1)) / 5:g}]]", labels + art_)

def slide(i):
    return ab(4, 5, f'<div class="ab flat" style="left:[[{-i * 1000}]]; top:0; width:[[5000]]; aspect-ratio:4/1; background:transparent">{panorama()}</div>',
              "100%", f"background:{PEACH}; color:{INK}", cls="flat")

carousel = '<div class="caro">' + "".join(f'<div>{slide(i)}</div>' for i in range(5)) + '</div>'
story = ab(9, 16, f'<div style="left:[[70]]; right:[[70]]; top:[[90]]">{wm("100%", INK)}</div>'
           f'<p style="left:[[70]]; top:[[330]]; {JPB}; font-size:[[90]]">発売まで</p>'
           f'<p style="left:[[50]]; top:[[420]]; {SANS}; font-weight:700; font-size:[[620]]; line-height:1">3</p>'
           f'<p style="left:[[420]]; top:[[820]]; {JPB}; font-size:[[90]]">日</p>'
           f'<div style="right:[[-200]]; bottom:[[-140]]; width:[[900]]">{el("sun", "100%", AMBER)}</div>'
           + caps("naʻau × Ivycoast", "[[30]]", "position:absolute; left:[[70]]; bottom:[[90]]"),
           "100%", f"background:{PEACH}; color:{INK}", cls="flat story")

social = ('<div class="soc">' + pf(p_reveal, "Reveal", "Collab post from both accounts. The box is the only full artwork.", plate=False)
          + pf(p_sun, "Time", "One element, one line.", plate=False) + pf(p_mother, "The mother", "Explains the SCOBY without a single claim.", plate=False)
          + pf(story, "Story countdown", "9:16 · three days to launch.", plate=False) + '</div>'
          '<div class="sub"><h3>How it’s made, a five-slide carousel</h3><p>One continuous picture: swipe and a dotted line carries you from tea to the coast.</p></div>'
          + carousel)

# ====================================================================== 08 website
def pdp():
    return ab(16, 10, f'<div style="left:0; right:0; top:0; height:[[56]]; border-bottom:1px solid #E5DCCF; display:flex; align-items:center; justify-content:space-between; padding:0 [[40]]">'
              f'{IVY("green", "[[120]]")}<span style="{SANS}; font-size:[[11]]; letter-spacing:.2em; color:{GREEN}">SHOP · JOURNAL · CART (0)</span></div>'
              f'<div class="ab flat" style="left:[[40]]; top:[[80]]; width:[[440]]; aspect-ratio:1; background:{PEACH}">'
              f'<div style="left:50%; top:50%; width:[[700]]; transform:translate(-50%,-50%) rotate(-6deg); box-shadow:0 [[20]] [[40]] rgba(60,40,30,.25)">{face_front("100%")}</div></div>'
              f'<div style="left:[[40]]; top:[[530]]; width:[[440]]; display:grid; grid-template-columns:repeat(4,1fr); gap:[[8]]">'
              + "".join(f'<div style="aspect-ratio:1; background:{bg}; display:flex; align-items:center; justify-content:center; box-shadow:inset 0 0 0 1px #E5DCCF">{el(n, "auto", fg, "height:64%; width:auto")}</div>'
                        for n, bg, fg in (("tea", PAPER, GREEN), ("mother", PEACH, INK), ("sun", AMBER, PAPER), ("bird", GREEN, PEACH))) + '</div>'
              f'<div class="col" style="left:[[540]]; right:[[40]]; top:[[90]]; gap:[[16]]">{wm("[[260]]", INK)}'
              + caps("naʻau × Ivycoast · Organic kombucha bar soap", "[[11]]", "position:static")
              + f'<p style="position:static; {JPB}; font-size:[[24]]">発酵が生み出す美しさ。</p>'
              f'<p style="position:static; font-family:var(--sans); font-size:[[12]]; line-height:1.9; color:#3E3833">名古屋の naʻau が仕込んだコンブチャの発酵液と、SCOBY の粉末を練り込み、Ivycoast が手で切り分けて数週間寝かせた石鹸です。</p>'
              f'<p style="position:static; {SANS}; font-size:[[22]]">¥［　］<span style="font-size:[[11]]">（税込）</span></p>'
              + rows([("WITH", "naʻau kombucha + SCOBY"), ("MADE BY", "Ivycoast, by hand"), ("CURED", "［　］ weeks"), ("SHIPPING", "常温便 · ［　］日でお届け")], "[[11]]", pad="[[6]]") +
              f'<p style="position:static; background:{GREEN}; color:{PAPER}; text-align:center; padding:[[12]] 0; {SANS}; font-size:[[12]]; letter-spacing:.2em">カートに入れる</p></div>',
              "100%", f"background:{PAPER}; color:{INK}", cls="flat")

def banner(which):
    if which == "ivy":
        return ab(16, 6, f'<p style="left:[[60]]; top:[[70]]; {SANS}; font-size:[[14]]; letter-spacing:.2em; color:{GREEN}">NEW · COLLABORATION</p>'
                  f'<p style="left:[[60]]; top:[[120]]; font-family:var(--lat); font-size:[[48]]; line-height:1.2; color:{GREEN}">Soap, brewed<br>in Nagoya.</p>'
                  f'<p style="left:[[60]]; bottom:[[70]]; {SANS}; font-size:[[13]]; letter-spacing:.16em; color:{GREEN}; border-bottom:1px solid {GREEN}; padding-bottom:[[4]]">DISCOVER KOM’BAR</p>'
                  f'<div class="ab flat" style="right:0; top:0; bottom:0; width:[[560]]; background:{PEACH}"><div style="right:[[-30]]; bottom:[[-40]]; width:[[400]]">{el("bird", "100%", GREEN)}</div>'
                  f'<div style="left:[[60]]; top:[[60]]; width:[[300]]">{wm("100%", INK)}</div></div>',
                  "100%", f"background:{PAPER}", cls="flat")
    return ab(16, 6, f'<div class="ab flat" style="left:0; top:0; bottom:0; width:[[560]]; background:{PEACH}"><div style="left:[[-60]]; bottom:[[-120]]; width:[[520]]">{el("mother", "100%", INK)}</div></div>'
              f'<p style="left:[[620]]; top:[[70]]; font-family:var(--sans); font-size:[[13]]; letter-spacing:.2em">NEW · コラボレーション</p>'
              f'<p style="left:[[620]]; top:[[120]]; font-family:var(--sans); font-weight:300; font-size:[[40]]; line-height:1.5">コンブチャから、<br>石鹸ができました。</p>'
              f'<div style="left:[[620]]; bottom:[[70]]; width:[[260]]">{wm("100%", INK)}</div>',
              "100%", "background:#FFFFFF; color:#1E1E1E", cls="flat")

web = ('<div class="browser"><div class="browser-bar"><i></i><i></i><i></i><span>Ivycoast · KOM’BAR</span></div>' + pdp() + '</div>'
       '<p class="muted" style="font-size:14px; margin-top:12px">Product page, on Ivycoast and on the naʻau shop: the same photographs and copy; each shop keeps its own header and footer.</p>'
       '<div class="sub"><h3>Home page banners</h3><p>Each site introduces the soap in its own voice.</p></div>'
       '<div class="grid g2">' + pf(banner("ivy"), "On Ivycoast", "English first, Ivycoast green, the bird.", plate=False) + pf(banner("naau"), "On naʻau", "Japanese first, the mother.", plate=False) + '</div>')

# ====================================================================== 09 language
LINES = [("発酵が生み出す美しさ。", "The beauty that fermentation makes."),
         ("育てる時間。手をかけること。自然から学ぶこと。", "Time to grow. Care by hand. Learning from nature."),
         ("発酵から生まれた素材を、手仕事によって新たなかたちへ。", "What fermentation grew, given a new form by hand."),
         ("SCOBYは、コンブチャの「母」。", "Brewers call the SCOBY the mother."),
         ("丁寧に仕込んだコンブチャの発酵液と、SCOBYの粉末を。", "Carefully brewed kombucha, and the SCOBY that made it.")]
language = ('<div class="lang">'
            '<div><p class="lang-voice"><b>Japanese first, English as a quiet second line.</b> Sensory and process-led: what it is, how it’s made, how it feels to use. Calm like Ivycoast; warm and personal like naʻau. No exclamation marks, no superlatives.</p>'
            '<h3 class="lang-h">Key lines</h3><div class="lines">' + "".join(f'<div><p class="jp">{j}</p><p class="it">{e}</p></div>' for j, e in LINES) + '</div>'
            '<h3 class="lang-h">Names</h3><dl class="facts"><dt>naʻau × Ivycoast</dt><dd>With the ʻokina, and a multiplication sign ×, not the letter x.</dd>'
            '<dt>KOM’BAR</dt><dd><b>KOM</b>bucha + <b>BAR</b> soap. Always in capitals; set as the drawn wordmark wherever it is the headline.</dd><dt>SCOBY（スコビー）</dt><dd>Explained once as 細菌と酵母の共生培養体.</dd></dl></div>'
            '<div><h3 class="lang-h" style="margin-top:0">Words we can use, for soap</h3><p class="muted" style="font-size:15px; margin-bottom:10px">Soap is a cosmetic, so claims stay inside the approved cosmetic effects.</p>'
            '<ul class="words ok">' + "".join(f'<li class="jp">{w}</li>' for w in ("肌を清浄にする（洗浄により）", "肌を整える／肌のキメを整える", "皮膚をすこやかに保つ", "SCOBYの粉末をスクラブとして配合")) + '</ul>'
            '<h3 class="lang-h">Words we avoid</h3><ul class="words no">' + "".join(f'<li class="jp">{w}</li>' for w in ("美白、アンチエイジング、若返る", "「発酵の力で肌が生まれ変わる」など、効能をうたう表現", "腸活・腸内環境など、飲料の健康効果と石鹸を結びつける表現", "治る、改善、医師・看護師がすすめる")) + '</ul>'
            '<p class="muted" style="font-size:13px; margin-top:14px">Final copy to be checked against 薬機法 by the party holding the cosmetics licence.</p></div></div>')

# ====================================================================== 10 ties
def tie(bg, inner, label, note, link):
    return pf(ab(4, 5, inner, "100%", f"background:{bg}", cls="flat"), label, note + f' <a href="{link}">See the direction →</a>', plate=False)

ties = ('<div class="grid g3">'
        + tie("#FFFFFF", f'<div style="left:[[120]]; right:[[120]]; top:[[200]]; box-shadow:0 [[20]] [[40]] rgba(0,0,0,.12)">{face_front("100%")}</div>'
                         f'<div class="row" style="left:0; right:0; bottom:[[200]]; justify-content:center; gap:[[40]]">{NAAU_CUR("[[200]]")}<span style="font-size:[[40]]">×</span>{IVY("dark", "[[250]]")}</div>',
              "Current identity", "White and plain, so the peach box leads. The script and the Ivycoast serif contrast clearly.", "current.html")
        + tie("#2B2926", f'<div style="left:[[-100]]; bottom:[[-140]]; width:[[640]]">{el("tea", "100%", "#3A3835")}</div>'
                         f'<div style="left:[[150]]; right:[[150]]; top:[[200]]; box-shadow:0 [[20]] [[40]] rgba(0,0,0,.4)">{face_front("100%")}</div>'
                         f'<div class="row" style="left:0; right:0; bottom:[[200]]; justify-content:center; gap:[[40]]; color:#EFEBE2">{L(D["lenora"], "efebe2", "[[210]]")}<span style="font-size:[[40]]">×</span>{IVY("white", "[[250]]")}</div>',
              "Concept A · Lenora", "The most luxurious pairing; two high-contrast serifs side by side can blur, so keep naʻau on sumi and Ivycoast on its own paper.", "lenora.html")
        + tie("#FAF7F1", f'<div style="right:[[-80]]; top:[[-60]]; width:[[520]]">{el("sun", "100%", "#E6D9BF")}</div>'
                         f'<div style="left:[[120]]; right:[[120]]; top:[[200]]; box-shadow:0 [[20]] [[40]] rgba(58,54,49,.16)">{face_front("100%")}</div>'
                         f'<div class="row" style="left:0; right:0; bottom:[[200]]; justify-content:center; gap:[[40]]">{L(D["ogg"], "3a3631", "[[220]]")}<span style="font-size:[[40]]">×</span>{IVY("dark", "[[250]]")}</div>',
              "Concept B · Ogg", "The warmest fit: Ogg’s calligraphic serif and Ivycoast’s flared serif feel related but distinct.", "ogg.html")
        + '</div>')

# ====================================================================== 11 borrowed
BORROWED = [
    ("Wine and chocolate labels set like spec sheets", "Plain facts in ruled rows", "Our rows hold the Japanese cosmetic label in its legal order, on the back only; the front stays Ivycoast’s illustration."),
    ("Kombucha back labels that speak plainly", "A plain, personal voice", "Our back carries the founders’ own story of fermentation, in their words, with no jokes and no claims."),
    ("Food cartons with a picture on each end", "Every panel of the box has a job", "Our ends tell one story in order, 01 tea to 04 Ivycoast, with elements cut from our own artwork."),
    ("Cut-paper cards and flat-colour labels", "One shape on one colour", "Our shapes are cut from the KOM’BAR artwork, never drawn new; the colours come from the two brands."),
    ("Kraft shipping boxes with one big mark", "A plain material, one idea", "Our lid draws the route from naʻau in Nagoya to the Ivycoast studio, with a peach address label."),
    ("Collab boxes covered in loose illustration", "Pattern on paper", "Ours is a regular half-drop repeat of one element, like a textile, rather than a scatter."),
    ("Soap sold with a paper band", "A band for the bare bar", "Ours is dated by hand with the Japanese round date stamp (日付印) for each cure."),
    ("Japanese gift wrapping", "The 掛け紙 paper band", "A tradition, used as itself: the band carries the name and one element."),
]
borrowed = ('<p class="lead-p">We looked at a wide set of packaging and print. For each, we took a principle and built our own version from our own material: the KOM’BAR artwork and wordmark, the two logos, and the copy. Nothing here reuses another brand’s illustration, layout or composition.</p>'
            '<div class="brw"><div class="brw-h"><span>Looked at</span><span>Principle borrowed</span><span>How ours differs</span></div>'
            + "".join(f'<div class="brw-r"><span>{a}</span><span>{b}</span><span>{c}</span></div>' for a, b, c in BORROWED) + '</div>')

# ====================================================================== 12 roles
roles = ('<div class="roles">' + "".join(
    f'<div class="{cls}"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for cls, t, items in [
        ("", "Ivycoast", ["Soap formulation and production", "Cosmetics licences (化粧品製造業・製造販売業) or a licensed OEM", "Box dieline, 全成分 and barcode", "Product page on Ivycoast"]),
        ("", "naʻau", ["Kombucha ferment and SCOBY supply", "The naming story and kimy’s voice", "Product page on the naʻau shop", "Counter card and workshop tie-in"]),
        ("together", "Together", ["Agree the ten elements and their meanings", "A photography day in both studios", "Launch posts as Instagram collab posts", "One shared copy deck, checked against 薬機法", "Launch date: ［　］"])]) + '</div>')

body = (KB.DEFS + C.nav("collab") + hero + intro +
        sec("01", "Two brands, one ritual", "Where Ivycoast and naʻau meet: small daily acts of care, and the patience of things that take weeks to make.", brands, sid="brands") +
        sec("02", "The product: KOM’BAR", "Organic kombucha cold-processed bar soap, made with naʻau’s kombucha and SCOBY.", product, sid="product") +
        sec("03", "The artwork, taken apart", "Ten elements from one illustration, each with a meaning.", elements, sid="elements") +
        sec("04", "Colour, type and space", "Six colours from both brands and five type voices.", system, sid="system") +
        sec("05", "Packaging", "The box as a whole object, batch bands, shipping and gifts.", packaging, sid="packaging") +
        sec("06", "Print", "Story cards in the box, a counter card and a launch poster.", print_, sid="print") +
        sec("07", "Social", "Feed posts at 3:4, a story at 9:16, a five-slide carousel.", social, sid="social") +
        sec("08", "Website", "The product page both shops share, and a banner for each home page.", web, sid="web") +
        sec("09", "Website language", "How both sites talk about the collaboration, in Japanese and English.", language, sid="language") +
        sec("10", "How it ties to each naʻau direction", "The box uses the Concept B logo. Here is how the collaboration would sit beside each direction.", ties, sid="ties") +
        sec("11", "What we borrowed", "Inspired by, never copied: a principle from each reference, made into our own version.", borrowed, sid="borrowed") +
        sec("12", "Who does what", "Responsibilities and next steps.", roles, sid="roles") +
        '<footer class="site"><div class="wrap">naʻau × Ivycoast · concept for discussion. Text in ［brackets］ is to be confirmed. Artwork and KOM’BAR wordmark from the Ivycoast files; Ivycoast logos from the Ivycoast brand files.</div></footer>')
C.page("collab.html", "naʻau × Ivycoast — KOM’BAR", "d-collab", body)
print("collab written")
