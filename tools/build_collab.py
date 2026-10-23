"""collab.html: naʻau × Ivycoast — KOM'BAR.

The full illustration appears once per piece at most (the box front, the hero). Everywhere else
the artwork is used as its ten separate elements. The front design belongs to the soap box alone.
"""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
import kombar as KB
KB_DEF0 = C.T("<b>KOM</b>bucha + <b>BAR</b> soap · コンブチャの石けん", "<b>KOM</b>bucha + <b>BAR</b> soap")
KB_DEF1 = C.T("KOM’BAR：<b>KOM</b>bucha（コンブチャ）＋ <b>BAR</b> soap（固形石けん）", "KOM’BAR: <b>KOM</b>bucha + <b>BAR</b> soap")
KB_DEF2 = C.T("<b>KOM</b>bucha ＋ <b>BAR</b> soap の略。常に大文字で表記し、見出しではロゴを使います。", "<b>KOM</b>bucha + <b>BAR</b> soap. Always in capitals; set as the drawn wordmark wherever it is the headline.")
import ink as K
from common import D, L, ab, pf, still, sec, ph
C.SITE = sys.argv[1]

PEACH, INK, PAPER, GREEN, AMBER, KRAFT, MUTE = "#F4D9C6", "#1E1E1E", "#F6F1E9", "#144948", "#9C5B22", "#CDB48E", "#6E655B"
# The collaboration palette: Ivycoast green as the anchor, two warm accents from kombucha, a coastal blue, on white.
# Peach belongs to the soap box alone.
WHITE, TURMERIC, PERSIMMON, TIDE = "#F8F6F1", "#E3A630", "#D4542E", "#A9C9D8"
el, wm, art = KB.el, KB.wordmark, KB.artwork
P = C.pic

# The voice. Name it by what is in it; one true number; the scent as a scene; time as the luxury; say the plain truth.
# Each line is written twice, once per language, rather than translated.
TAG = ("お茶だったものを、<br>手のひらに。", "Once, it was tea.")
DESCR = ("コンブチャと SCOBY の石けん", "Kombucha &amp; SCOBY cold-process bar")
NUM = ("14日、仕込む。<br>60日、待つ。", "Brewed fourteen days. Cured sixty.")
SCENT = ("雨のあとの森と、<br>むいたばかりのマンダリン。", "A forest after rain. A mandarin, just peeled.")
MOTHER = ("「母」から<br>生まれた石けん。", "A soap with a mother.")
ORIGIN = ("名古屋で仕込み、<br>海辺の工房で切る。", "Brewed in Nagoya. Cut by hand by the sea.")
HONEST = ("コンブチャを仕込むたびに、SCOBY はひと層ずつ育ちます。使いきれずにいたその層を、石けんにしました。",
          "Every brew grows the mother another layer. The layers we couldn’t use became soap.")
USE = ("手のなかで、ゆっくり泡立てて。", "Work it slowly between wet hands.")
br = lambda x: x.replace("<br>", "")
IVY = lambda col, w, style="": f'<img src="assets/collab/ivycoast-wordmark-{col}.png" alt="IVYCOAST" style="width:{w}; display:block; {style}">'
IVYICON = lambda w: f'<img src="assets/collab/ivycoast-icon-green.png" alt="" style="width:{w}">'
OGGCOL = {"1e1e1e": "3a3631", "ffffff": "faf7f1"}
NAAU = lambda w, col="1e1e1e", style="": f'<img src="assets/logos/ogg-{OGGCOL.get(col, col)}.png" alt="naʻau" style="width:{w}; display:block; {style}">'
NAAU_CUR = lambda w, col="1e1e1e", style="": f'<img src="assets/logos/current-naau-{col}.png" alt="naʻau" style="width:{w}; display:block; {style}">'
SANS = "font-family:Inter, sans-serif"
JPB = "font-family:var(--sans); font-weight:700"

# Measured from the artwork: naʻau (Ogg) x-height is 279 of 1230 px wide, baseline 9 px above the image bottom;
# IVYCOAST cap height is 186 of 1200 px wide, baseline 2 px above the bottom.
IVY_K = 1200 * 279 / (1230 * 186)          # IVYCOAST width per naʻau width, so caps match the x-height

def pair(w, col="1e1e1e", ivy="dark", style=""):
    """naʻau × IVYCOAST on one baseline."""
    return (f'<div class="pair-lock" style="--w:{w}; {style}">'
            f'<img src="assets/logos/ogg-{OGGCOL.get(col, col)}.png" alt="naʻau" style="width:var(--w); margin-bottom:calc(var(--w) * -0.0073)">'
            f'<svg viewBox="0 0 10 10" aria-label="×" style="width:calc(var(--w) * .07); margin-bottom:calc(var(--w) * .0784)"><path d="M1 1 L9 9 M9 1 L1 9" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/></svg>'
            f'<img src="assets/collab/ivycoast-wordmark-{ivy}.png" alt="IVYCOAST" style="width:calc(var(--w) * {IVY_K:.4f}); margin-bottom:calc(var(--w) * {-IVY_K * 2 / 1200:.4f})"></div>')

def lockup(w_naau, w_ivy=None, gap=None, align=None, col="1e1e1e", ivy="dark"):
    """Always the one-line, baseline-aligned lockup."""
    return pair(w_naau, col, ivy)

def caps(text, size, extra=""):
    return f'<p style="{SANS}; font-size:{size}; letter-spacing:.18em; line-height:1.7; text-transform:uppercase; {extra}">{text}</p>'

def rows(items, size, col="rgba(30,30,30,.35)", pad="[[10]]", extra=""):
    return (f'<dl class="spec-rows" style="position:static; {SANS}; font-size:{size}; letter-spacing:.04em; border-bottom:1px solid {col}; {extra}">'
            + "".join(f'<dt style="padding:{pad} [[24]] {pad} 0; border-color:{col}; opacity:.62">{a}</dt><dd style="margin:0; padding:{pad} 0; border-color:{col}">{b}</dd>' for a, b in items) + '</dl>')

# ====================================================================== box faces (90 × 44 × 30 mm, to confirm)
BW, BH, BD = 90, 44, 30
STORY = ['コンブチャは、細菌と酵母が共に働くことで生まれる、伝統的な発酵茶です。', 'その発酵を支えるのが、SCOBY（スコビー）。<br>Symbiotic Culture of Bacteria and Yeast<br>細菌と酵母の共生培養体を意味します。', '発酵が進むにつれて、SCOBYはバクテリアセルロースからなる繊細な膜を育んでいきます。大切に育てたSCOBYを細かな粉末にし、やさしいスクラブとして石鹸に取り入れました。', '発酵から生まれた素材を、手仕事によって新たなかたちへ。丁寧に仕込んだコンブチャの発酵液と、このSCOBYの粉末を組み合わせ、発酵の物語を手づくりの石鹸へとつなぎました。', '時間をかけて育まれるものの豊かさ、変化することの美しさ、そして人の手から生まれるものへの敬意を込めて。']
CLOSE = "育てる時間。手をかけること。自然から学ぶこと。"
INGREDIENTS = "オリーブ油、ヤシ油、米油、パーム油、カカオ脂、ヒマシ油、精製水、水酸化Na、コンブチャ、コンブチャSCOBY、シダーウッド精油、パチュリ精油、マンダリン精油、ホワイトセージ精油"
LABEL = [("品名", "化粧石けん"), ("内容量", "［　］g"), ("全成分", INGREDIENTS), ("使用方法", "よく泡立てて使用し、洗い流す"), ("製造販売元", "［　］"), ("原産国", "日本")]

def face_front(w="100%"):
    """The front, from Ivycoast's own file (assets/collab/source/kombar-front.svg), centred with an even margin."""
    cw = 887                                   # artwork width in board units; height follows its 729.28 : 333.84 ratio
    ch = cw * 333.84 / 729.28
    bh = 1000 * BH / BW
    return ab(BW, BH, f'<img src="assets/collab/source/kombar-front.svg" alt="KOM’BAR: the wordmark, the artwork and ORGANIC KOMBUCHA COLD PROCESSED BAR SOAP" '
              f'style="left:[[{(1000 - cw) / 2:.1f}]]; top:[[{(bh - ch) / 2:.1f}]]; width:[[{cw}]]">',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def bars(w, h):
    b = "".join(f'<i style="width:[[{t}]]; background:{INK}; height:100%"></i><i style="width:[[{g}]]"></i>' for t, g in
                [(2, 1), (1, 1), (1, 2), (3, 1), (1, 2), (2, 1), (1, 1), (2, 2), (1, 1), (3, 1), (1, 2), (1, 1), (2, 1), (1, 2), (3, 1), (1, 1), (2, 1), (1, 0)])
    return f'<div style="width:{w}; height:{h}; display:flex; background:{PAPER}; padding:[[6]] [[10]]">{b}</div>'

def face_back(w="100%"):
    """Back: headline and two sentences on the left, the label on the right, logos and barcode along the foot."""
    return ab(BW, BH, caps("Kombucha soap", "[[13]]", "position:absolute; left:[[56]]; top:[[52]]; letter-spacing:.26em")
              + f'<p style="left:[[56]]; top:[[84]]; {JPB}; font-size:[[36]]; line-height:1.3">発酵が生み出す美しさ。</p>'
              f'<p style="left:[[56]]; top:[[150]]; width:[[440]]; font-family:var(--sans); font-size:[[16]]; line-height:1.9">{STORY[0]}大切に育てたSCOBYを細かな粉末にし、やさしいスクラブとして石鹸に取り入れました。</p>'
              f'<div style="left:[[56]]; bottom:[[48]]">{pair("[[118]]")}</div>'
              f'<div style="left:[[580]]; right:[[56]]; top:[[46]]">' + rows(LABEL, "[[11.5]]", pad="[[5]]") + '</div>'
              f'<div style="right:[[56]]; bottom:[[62]]">{bars("[[150]]", "[[46]]")}</div>'
              f'<p style="right:[[56]]; bottom:[[44]]; width:[[150]]; {SANS}; font-size:[[10]]; letter-spacing:.3em; text-align:center">4 ［　　　　　　］</p>',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def insert_card(w="100%"):
    """The whole story on a card inside the lid, 85 × 120 mm, with the three logos."""
    paras = "".join(f'<p style="position:static; margin:0 0 [[24]]">{t}</p>' for t in STORY)
    return ab(85, 120, caps("Kombucha soap", "[[22]]", "position:absolute; left:[[80]]; top:[[80]]; letter-spacing:.24em")
              + f'<div style="right:[[80]]; top:[[72]]; width:[[300]]">{wm("100%", INK)}</div>'
              f'<p style="left:[[80]]; top:[[170]]; {JPB}; font-size:[[60]]; line-height:1.35">発酵が生み出す美しさ。</p>'
              f'<div style="left:[[80]]; right:[[80]]; top:[[290]]; font-family:var(--sans); font-size:[[27]]; line-height:1.85">{paras}</div>'
              f'<p style="left:[[80]]; top:[[1050]]; {JPB}; font-size:[[28]]; letter-spacing:.06em; line-height:1.7">育てる時間。<br>手をかけること。<br>自然から学ぶこと。</p>'
              f'<div style="right:[[-70]]; bottom:[[-60]]; width:[[380]]">{el("mother", "100%", INK)}</div>'
              f'<div style="left:[[80]]; bottom:[[70]]">{pair("[[170]]")}</div>',
              w, f"background:{PAPER}; color:{INK}")

def face_end(name, *_, w="100%", bg=PEACH, ink=INK):
    """End panel: one element, small, centred."""
    return ab(BD, BH, f'<div style="left:[[260]]; right:[[260]]; top:50%; transform:translateY(-50%)">{el(name, "100%", ink)}</div>',
              w, f"background:{bg}; color:{ink}", cls="flat")

def face_top(w="100%"):
    """Lid: the wordmark, centred."""
    return ab(BW, BD, f'<div style="left:50%; top:50%; transform:translate(-50%,-50%); width:[[300]]">{wm("100%", INK)}</div>',
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def face_bottom(w="100%"):
    return ab(BW, BD, caps("Made in Japan · Lot ［　　　］", "[[15]]", "position:absolute; left:0; right:0; top:50%; transform:translateY(-50%); text-align:center; letter-spacing:.3em"),
              w, f"background:{PEACH}; color:{INK}", cls="flat")

def dieline():
    """A technical drawing: cut, fold and panel names only."""
    W, H, D, T = BW, BH, BD, 12
    X = [0, D, D + W, 2 * D + W, 2 * D + 2 * W]
    top, bot = T + D, T + D + H
    TW, TH = 2 * D + 2 * W + 10, T + 2 * D + H + T
    cut, fold, lab = INK, PERSIMMON, MUTE
    t = lambda x, y, txt, sz=3.2, anchor="middle": f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="IBM Plex Mono, monospace" font-size="{sz}" letter-spacing=".4" fill="{lab}">{txt}</text>'
    body = (f'<g fill="none" stroke="{cut}" stroke-width=".3" stroke-linejoin="round">'
            f'<path d="M0 {top} H{X[1]} V{T} Q{X[1]} 0 {X[1] + 12} 0 H{X[2] - 12} Q{X[2]} 0 {X[2]} {T} V{top} H{X[4]} L{X[4] + 10} {top + 4} V{bot - 4} L{X[4]} {bot} '
            f'H{X[4]} V{bot + D + T} H{X[3]} V{bot} H0 Z"/>'
            f'<path d="M0 {top} L4 {top - 12} H{D - 4} L{D} {top} M{X[2]} {top} L{X[2] + 4} {top - 12} H{X[3] - 4} L{X[3]} {top}'
            f' M0 {bot} L4 {bot + 12} H{D - 4} L{D} {bot} M{X[2]} {bot} L{X[2] + 4} {bot + 12} H{X[3] - 4} L{X[3]} {bot}"/></g>'
            f'<g fill="none" stroke="{fold}" stroke-width=".35" stroke-dasharray="1.6 1.1">'
            f'<path d="M{X[1]} {top} V{bot} M{X[2]} {top} V{bot} M{X[3]} {top} V{bot} M{X[4]} {top} V{bot} M{X[1]} {top} H{X[2]} M{X[1]} {T} H{X[2]} M{X[3]} {bot} H{X[4]} M{X[3]} {bot + D} H{X[4]}"/></g>'
            + t(X[1] + W / 2, top + H / 2, "FRONT", 4) + t(X[1] + W / 2, top + H / 2 + 6, f"{W} × {H}", 3)
            + t(X[3] + W / 2, top + H / 2, "BACK", 4) + t(D / 2, top + H / 2, "END", 3.4) + t(X[2] + D / 2, top + H / 2, "END", 3.4)
            + t(X[1] + W / 2, T + D / 2 + 1, "LID", 3.4) + t(X[3] + W / 2, bot + D / 2 + 1, "BASE", 3.4) + t(X[1] + W / 2, T - 4, "TUCK", 2.6)
            + t(X[4] + 5, top + H / 2, "GLUE", 2.4)
            + f'<g transform="translate({X[3] + 4} 6)"><line x1="0" y1="-1" x2="8" y2="-1" stroke="{cut}" stroke-width=".3"/>{t(10, 0, "CUT", 2.6, "start")}'
            f'<line x1="22" y1="-1" x2="30" y2="-1" stroke="{fold}" stroke-width=".35" stroke-dasharray="1.6 1.1"/>{t(32, 0, "FOLD", 2.6, "start")}'
            f'{t(0, 6, f"{W} × {H} × {D} MM · TO CONFIRM", 2.6, "start")}</g>')
    return f'<svg viewBox="-2 -2 {TW + 4} {TH + 4}" style="width:100%; display:block" role="img" aria-label="Dieline: cut and fold lines">{body}</svg>'

# ====================================================================== hero
hero = (f'<header class="kb2"><div class="wrap kb2-grid">'
        f'<div class="kb2-text"><p class="kb-eyebrow">naʻau × Ivycoast · 2026</p>'
        f'<div class="kb2-wm">{wm("100%", INK)}</div>'
        f'<p class="kb2-def">{KB_DEF0}</p>'
        f'<p class="kb-jp">発酵が生み出す美しさ。</p><p class="kb-en">A cold-process bar soap made with naʻau’s kombucha and the SCOBY that brews it.</p>'
        f'<div class="kb2-lock">{pair("128px")}</div></div>'
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
brands = (f'<div class="meet">{pair("min(30vw,200px)")}'
          '<div class="meet-cols"><p><span>Ivycoast</span>Australian botanicals, brought into Japanese homes for daily rituals.</p>'
          '<p><span>naʻau</span>Small-batch kombucha, brewed in Nagoya.</p></div>'
          '<p class="meet-line">Where they meet: 儀式 ritual, 時間 time, 素材 materials, 手 hands.</p></div>')

product = ('<div class="grid g2" style="align-items:start">'
           + pf(face_front("100%"), "Front, as designed", "Kept exactly: the vertical wordmark, the full artwork, two lines of capitals.", plate=False)
           + pf(face_back("100%"), "Back, new", "The headline and the first lines of the story; the label in order; naʻau (Concept B), Ivycoast and KOM’BAR.", plate=False)
           + '</div><div class="grid g-wide" style="margin-top:clamp(24px,3vw,40px); align-items:center">'
           + pf(f'<div style="width:46%">{insert_card("100%")}</div>', "Story card inside the lid, 85 × 120 mm", "The full text, legible at 6 pt and above; the mother cropped off the corner.", "1/1")
           + '<dl class="facts facts-lg"><dt>Name</dt><dd>{KB_DEF1}</dd><dt>Product</dt><dd>Organic kombucha cold-processed bar soap</dd><dt>Made with</dt><dd>naʻau kombucha ferment, and SCOBY powder as a gentle scrub</dd>'
           '<dt>Made by</dt><dd>Ivycoast, by hand</dd><dt>Box</dt><dd>90 × 44 × 30 mm ［to confirm］</dd><dt>Weight</dt><dd>［　g］</dd><dt>全成分</dt><dd>［to confirm］</dd></dl></div>')

# ====================================================================== 03 elements
FIELDS = [(PEACH, INK), (GREEN, PEACH), (PAPER, INK), (INK, PEACH), (KRAFT, INK), (AMBER, PAPER),
          (PAPER, GREEN), (PEACH, GREEN), (GREEN, PAPER), (PAPER, AMBER)]
def tile(i, name):
    _, jp, en, meaning = KB.ELEMENTS[name]
    bg, fg = (TURMERIC, INK) if name == "sun" else [(GREEN, WHITE), (WHITE, GREEN)][i % 2]
    return (f'<figure class="kel"><div class="kel-card" style="background:{bg}; color:{fg}"><span class="kel-n">{i + 1:02d}</span><span class="kel-jp">{jp}</span>'
            f'<div class="kel-art">{el(name, "auto", fg, "height:100%; width:auto; max-width:100%")}</div></div>'
            f'<figcaption><b>{en}</b><span>{meaning}</span></figcaption></figure>')

elements = ('<p class="lead-p">The illustration stays whole on the front of the soap box, and only there. Everywhere else we use it the way a printer would use a set of blocks: one element at a time, large, in one ink on one colour. Ten elements come out of the artwork, each with something to say.</p>'
            '<div class="kel-grid">' + "".join(tile(i, n) for i, n in enumerate(KB.ORDER)) + '</div>'
            '<p class="muted" style="font-size:14px; margin-top:18px">Element files: <code>assets/collab/elements/01-mother.svg</code> to <code>10-ginger.svg</code>, cut from the original artwork without redrawing; the tea leaves and the sprig are set side by side as one element. Meanings are proposals for both teams to agree.</p>')

# ====================================================================== 04 colour, type, space
PAL = [("White", WHITE, "Ground, cards, the web.", 3), ("Coast green", GREEN, "Ivycoast. Carries the page.", 3), ("Turmeric", TURMERIC, "The one accent.", 1),
       ("Ink", INK, "Artwork and text.", 1), ("Persimmon", PERSIMMON, "The sun only.", .5), ("Tide", TIDE, "Ivycoast web only.", .5), ("Peach", PEACH, "The soap box only.", .6)]
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
               f'<div style="right:[[60]]; top:[[60]]; width:[[360]]">' + rows([("WITH", "kombucha + SCOBY"), ("MADE BY", "Ivycoast"), ("CURED", "2 months"), ("WEIGHT", "［　］ g")], "[[17]]", pad="[[8]]") + '</div>'
               f'<p style="right:[[60]]; top:[[250]]; width:[[360]]; {SANS}; font-size:[[16]]; letter-spacing:.2em; color:{MUTE}">DETAILS · INTER, RULED ROWS</p>'
               f'<div style="right:[[-30]]; bottom:[[-110]]; width:[[250]]">{el("tea", "100%", GREEN)}</div>',
               "100%", f"background:{PAPER}; color:{INK}", cls="flat")
system = ('<div class="sub" style="margin-top:0"><h3>Colour</h3><p>Peach is always there. One partner colour per piece, never more than two inks.</p></div>'
          + C.chips([(n, h, r, w) for n, h, r, w in PAL]) +
          f'<div class="pairs">{pairs}</div>'
          '<div class="sub"><h3>Type</h3><p>The KOM’BAR wordmark is the only display type. Everything else is quiet.</p></div>'
          + pf(type_card, "Type hierarchy", "Five voices, each with one job.", plate=False))

# ====================================================================== 05 packaging
def band(no, date, ink=None):
    """The bare bar with a green paper band, dated with a round date stamp for each cure."""
    bar = (f'<div style="left:[[110]]; right:[[110]]; top:[[150]]; bottom:[[150]]; background:#EFE9DE; border-radius:[[22]]; box-shadow:inset 0 [[-8]] [[16]] rgba(120,100,70,.14), 0 [[16]] [[30]] rgba(0,0,0,.18)"></div>')
    strip = (f'<div class="ab flat" style="left:[[110]]; right:[[110]]; top:[[400]]; height:[[170]]; background:{GREEN}; color:{WHITE}; box-shadow:0 [[4]] [[10]] rgba(0,0,0,.14)">'
             f'<div style="left:[[60]]; top:50%; transform:translateY(-50%); width:[[300]]">{wm("100%", WHITE)}</div>'
             f'<div style="right:[[50]]; top:50%; transform:translateY(-50%) rotate(-8deg); width:[[200]]">{K.date_stamp("100%", "名古屋", date, "CURE " + no, WHITE)}</div></div>')
    return ab(1, 1, bar + strip, "100%", "background:transparent", cls="flat clear")

bands = ('<div class="grid g3">' + band("01", "26.11.03", GREEN) + band("02", "26.11.24", INK) + band("03", "26.12.15", AMBER) + '</div>')

def mailer():
    """Kraft lid: the route the kombucha takes, from Nagoya to the Ivycoast studio."""
    route = (f'<svg viewBox="0 0 1000 750" style="left:0; top:0; width:100%; height:100%" aria-hidden="true">'
             f'<path d="M150 560 C260 420 380 610 500 470 C610 340 720 520 850 250" fill="none" stroke="{GREEN}" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round"/>'
             f'<circle cx="150" cy="560" r="14" fill="{GREEN}"/><circle cx="850" cy="250" r="14" fill="none" stroke="{GREEN}" stroke-width="5"/></svg>')
    return ab(4, 3, f'<div class="fill" style="background:{WHITE}"></div>' + route +
              f'<p style="left:[[80]]; top:[[620]]; {JPB}; font-size:[[30]]">名古屋</p>' + caps("naʻau kombucha", "[[18]]", "position:absolute; left:[[80]]; top:[[662]]") +
              f'<p style="right:[[80]]; top:[[160]]; {JPB}; font-size:[[30]]; text-align:right">［　］</p>' + caps("Ivycoast studio", "[[18]]", "position:absolute; right:[[80]]; top:[[205]]") +
              f'<div style="left:[[430]]; top:[[330]]; width:[[150]]; transform:rotate(-14deg)">{el("bird", "100%", GREEN)}</div>'
              f'<div class="ab flat" style="left:[[80]]; top:[[70]]; width:[[300]]; aspect-ratio:3/2; background:{TURMERIC}; color:{INK}; box-shadow:0 [[3]] [[8]] rgba(0,0,0,.12)">'
              f'<div style="left:[[70]]; top:[[80]]; width:[[600]]">{wm("100%", INK)}</div>'
              + caps("To ［　　　　］ 様", "[[50]]", "position:absolute; left:[[70]]; top:[[320]]; letter-spacing:.06em") + '</div>',
              "100%", "background:transparent", cls="flat")

def mailer_inside():
    """Inside the lid: the brand's own closing line, as the first thing read on opening."""
    return ab(4, 3, f'<div class="fill" style="background:{TURMERIC}"></div><div style="left:[[-60]]; bottom:[[-200]]; width:[[600]]">{el("sun", "100%", INK)}</div>'
              f'<p class="vt" style="right:[[110]]; top:[[80]]; {JPB}; font-size:[[60]]; line-height:2; letter-spacing:.14em">{TAG[0]}</p>'
              f'<div style="right:[[80]]; bottom:[[70]]">{lockup("[[120]]")}</div>',
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
    return ab(4, 3, f'<div class="fill" style="background:{GREEN}; color:{WHITE}"></div>'
              f'<div style="left:[[-90]]; top:[[-60]]; width:[[640]]; transform:rotate(12deg)">{el("bird", "100%", TURMERIC)}</div>'
              f'<div class="ab flat" style="right:[[160]]; top:0; bottom:0; width:[[190]]; background:{WHITE}; color:{INK}; box-shadow:[[-4]] 0 [[10]] rgba(0,0,0,.12)">'
              f'<p class="vt" style="left:50%; top:[[60]]; transform:translateX(-50%); {JPB}; font-size:[[120]]; letter-spacing:.1em">おくりもの</p>'
              f'<div style="left:[[300]]; right:[[300]]; bottom:[[90]]">{el("lemon", "100%", INK)}</div></div>'
              f'<div style="left:[[70]]; bottom:[[60]]">{pair("[[120]]", "ffffff", "white")}</div>'
              + caps("KOM’BAR + naʻau kombucha 330 ml", "[[18]]", "color:#F8F6F1; position:absolute; left:[[70]]; bottom:[[210]]"),
              "100%", "background:transparent", cls="flat")

# ====================================================================== 06 print
def story_card(no, name, word, line_jp, line_en, bg, fg, ew=640, w="23%"):
    return ab(55, 91, caps(f"{no} — {word}", "[[34]]", "position:absolute; left:[[90]]; top:[[96]]; letter-spacing:.22em")
              + f'<div style="right:[[90]]; top:[[90]]; width:[[200]]">{wm("100%", fg)}</div>'
              f'<div style="left:50%; top:[[700]]; transform:translate(-50%,-50%); width:[[{ew}]]">{el(name, "100%", fg)}</div>'
              f'<div style="left:[[90]]; right:[[90]]; top:[[1230]]; height:1px; background:currentColor; opacity:.35"></div>'
              f'<p style="left:[[90]]; right:[[90]]; top:[[1290]]; font-family:var(--sans); font-weight:500; font-size:[[58]]; line-height:1.6">{line_jp}</p>'
              f'<p class="it" style="left:[[90]]; right:[[90]]; top:[[1405]]; font-family:var(--lat); font-size:[[46]]">{line_en}</p>',
              w, f"background:{bg}; color:{fg}")

CARD_ARGS = [("01", "tea", "Tea", "名古屋で、お茶を仕込む。", "Tea, set to brew in Nagoya.", WHITE, GREEN, 640),
             ("02", "mother", "The mother", "14日で、母が育つ。", "In fourteen days, a mother grows.", WHITE, INK, 600),
             ("03", "bird", "Cut", "海辺の工房で、手で切る。", "Cut by hand, by the sea.", WHITE, GREEN, 700),
             ("04", "sun", "Cure", "そして60日、待つ。", "Then sixty days of waiting.", WHITE, PERSIMMON, 640)]
card1 = lambda i: story_card(*CARD_ARGS[i], w="100%")

cards = "".join(story_card(*c) for c in CARD_ARGS)

counter = ab(105, 148, f'<p style="left:[[80]]; top:[[90]]; {JPB}; font-size:[[78]]; line-height:1.45">{TAG[0]}</p>'
             f'<p class="it" style="left:[[80]]; top:[[330]]; font-family:var(--lat); font-size:[[40]]">{TAG[1]}</p>'
             + caps(DESCR[1], "[[22]]", "position:absolute; left:[[80]]; top:[[420]]") +
             f'<div style="right:[[-160]]; bottom:[[-120]]; width:[[900]]">{el("mother", "100%", INK)}</div>'
             f'<div style="left:[[80]]; bottom:[[80]]; width:[[380]]">{wm("100%", INK)}</div>'
             + caps("¥［　］ · 税込", "[[26]]", "position:absolute; left:[[80]]; bottom:[[170]]"),
             "100%", f"background:{TURMERIC}; color:{INK}")

poster = ab(297, 420, f'<div style="left:0; right:0; top:0; height:[[780]]">{P("mother", 1200, "50% 40%")}</div>'
            f'<div style="right:[[30]]; top:[[500]]; width:[[380]]; z-index:2">{el("mother", "100%", WHITE)}</div>'
            f'<div style="left:[[70]]; top:[[860]]; width:[[440]]">{wm("100%", WHITE)}</div>'
            + caps("<b>KOM</b>bucha + <b>BAR</b> soap", "[[20]]", f"position:absolute; left:[[70]]; top:[[1000]]; color:{WHITE}")
            + f'<p style="left:[[70]]; top:[[1060]]; {JPB}; font-size:[[48]]; line-height:1.5; color:{WHITE}">{TAG[0]}</p>'
            f'<div style="left:[[70]]; bottom:[[70]]; color:{WHITE}">{pair("[[150]]", "ffffff", "white")}</div>'
            f'<div style="left:[[520]]; right:[[70]]; bottom:[[64]]; color:{WHITE}">' + rows([("発売", "［月日］"), ("取扱", "naʻau · Ivycoast"), ("価格", "¥［　］")], "[[19]]", "rgba(248,246,241,.35)", "[[10]]") + '</div>',
            "100%", f"background:{GREEN}; color:{WHITE}")

print_ = ('<div class="sub" style="margin-top:0"><h3>Story cards, 55 × 91 mm</h3><p>Four cards inside each box: how a cup of tea becomes a bar of soap.</p></div>'
          + pf(f'<div style="display:flex; gap:2.5%; justify-content:center; align-items:flex-start; width:100%">{cards}</div>', "Story cards, front", "One element each, whole; one line in Japanese, one in English. Paper and peach alternate.", "21/9")
          + '<div class="grid g2" style="margin-top:clamp(24px,3vw,40px)">'
          + pf(f'<div style="width:46%">{counter}</div>', "Counter card, A6", "At the naʻau counter and Ivycoast stockists.", "1/1")
          + pf(f'<div style="width:50%">{poster}</div>', "Launch poster, A3", "For the shop window: the wordmark across the top, what it stands for, and the sun rising from the bottom edge.", "1/1") + '</div>')

# ====================================================================== 07 social
def post(inner, bg, fg=INK):
    return ab(3, 4, inner, "100%", f"background:{bg}; color:{fg}", cls="flat post")

p_reveal = post(f'<div style="left:[[110]]; top:[[230]]; width:[[780]]; transform:rotate(-4deg); box-shadow:0 [[30]] [[50]] rgba(60,40,30,.28)">{face_front("100%")}</div>'
                f'<div style="left:[[70]]; right:[[70]]; bottom:[[90]]">{wm("100%", INK)}</div>' + caps("naʻau × Ivycoast · ［月日］", "[[24]]", "position:absolute; left:[[70]]; top:[[80]]"), PAPER)
p_sun = post(f'<div style="right:[[-250]]; top:[[-220]]; width:[[900]]">{el("sun", "100%", TURMERIC)}</div>'
             f'<p style="left:[[70]]; bottom:[[220]]; {JPB}; font-size:[[84]]; line-height:1.4; color:{WHITE}">{NUM[0]}</p>'
             f'<p class="it" style="left:[[70]]; bottom:[[150]]; font-family:var(--lat); font-size:[[36]]; color:{WHITE}">{NUM[1]}</p>'
             f'<div style="left:[[70]]; bottom:[[70]]; width:[[260]]">{wm("100%", WHITE)}</div>', GREEN)
p_mother = post(f'<div style="left:[[-120]]; bottom:[[-140]]; width:[[820]]">{el("mother", "100%", INK)}</div>'
                f'<p style="right:[[70]]; top:[[90]]; {JPB}; font-size:[[78]]; line-height:1.45; text-align:right">{MOTHER[0]}</p>'
                f'<p class="it" style="right:[[70]]; top:[[340]]; font-family:var(--lat); font-size:[[36]]; text-align:right">{MOTHER[1]}</p>', WHITE)

STEPS = [("01", "茶", "Tea", "teabowl", "50% 50%", "tea", TURMERIC, "名古屋で、お茶を仕込む。", "Tea, set to brew in Nagoya."),
         ("02", "母", "The mother", "mother", "50% 45%", "mother", GREEN, "14日で、母が育つ。", "In fourteen days, a mother grows."),
         ("03", "切", "Cut", "hands", "50% 70%", "bird", GREEN, "海辺の工房で、手で切る。", "Cut by hand, by the sea."),
         ("04", "待", "Cure", "batter", "50% 50%", "sun", PERSIMMON, "そして60日、待つ。", "Then sixty days of waiting."),
         ("05", "香", "Scent", "forest", "50% 60%", "botanical", TURMERIC, br(SCENT[0]), SCENT[1])]

def slide(i):
    n, k, en, photo_, pos, name, col, jp, en_line = STEPS[i]
    return ab(4, 5, f'<div style="left:0; right:0; top:0; height:[[830]]">{P(photo_, 900, pos)}</div>'
              f'<div style="right:[[50]]; top:[[640]]; width:[[300]]; z-index:2">{el(name, "100%", col)}</div>'
              + caps(f"{n} — {en}", "[[24]]", "position:absolute; left:[[70]]; top:[[880]]; letter-spacing:.2em")
              + f'<p style="left:[[70]]; top:[[935]]; {JPB}; font-size:[[120]]; line-height:1">{k}</p>'
              f'<div class="col" style="left:[[250]]; right:[[400]]; top:[[945]]; gap:[[14]]"><p style="{JPB}; font-size:[[36]]; line-height:1.55">{jp}</p>'
              f'<p class="it" style="font-family:var(--lat); font-size:[[28]]; line-height:1.3; opacity:.75">{en_line}</p></div>',
              "100%", f"background:{WHITE}; color:{INK}", cls="flat")

carousel = '<div class="caro">' + "".join(f'<div>{slide(i)}</div>' for i in range(5)) + '</div>'
story = ab(9, 16, f'<div style="left:[[70]]; right:[[70]]; top:[[90]]">{wm("100%", INK)}</div>'
           f'<p style="left:[[70]]; top:[[330]]; {JPB}; font-size:[[90]]">発売まで</p>'
           f'<p style="left:[[50]]; top:[[420]]; {SANS}; font-weight:700; font-size:[[620]]; line-height:1">3</p>'
           f'<p style="left:[[420]]; top:[[820]]; {JPB}; font-size:[[90]]">日</p>'
           f'<div style="right:[[-200]]; bottom:[[-140]]; width:[[900]]">{el("sun", "100%", PERSIMMON)}</div>'
           + caps("naʻau × Ivycoast", "[[30]]", "position:absolute; left:[[70]]; bottom:[[90]]"),
           "100%", f"background:{WHITE}; color:{INK}", cls="flat story")

social = ('<div class="soc">' + pf(p_reveal, "Reveal", "Collab post from both accounts. The box is the only full artwork.", plate=False)
          + pf(p_sun, "Time", "One element, one line.", plate=False) + pf(p_mother, "The mother", "Explains the SCOBY without a single claim.", plate=False)
          + pf(story, "Story countdown", "9:16 · three days to launch.", plate=False) + '</div>'
          '<div class="sub"><h3>How it’s made, a five-slide carousel</h3><p>One continuous picture: swipe and a dotted line carries you from tea to the coast.</p></div>'
          + carousel)

# ====================================================================== 08 website
def pdp():
    return ab(16, 10, f'<div style="left:0; right:0; top:0; height:[[56]]; border-bottom:1px solid #E5DCCF; display:flex; align-items:center; justify-content:space-between; padding:0 [[40]]">'
              f'{IVY("green", "[[120]]")}<span style="{SANS}; font-size:[[11]]; letter-spacing:.2em; color:{GREEN}">SHOP · JOURNAL · CART (0)</span></div>'
              f'<div class="ab flat" style="left:[[40]]; top:[[80]]; width:[[440]]; aspect-ratio:1; background:{GREEN}">'
              f'<div class="fill">{P("hands", 900, "50% 62%")}</div>'
              f'<div style="right:[[24]]; bottom:[[24]]; width:[[130]]">{el("mother", "100%", WHITE)}</div></div>'
              f'<div style="left:[[40]]; top:[[530]]; width:[[440]]; display:grid; grid-template-columns:repeat(4,1fr); gap:[[8]]">'
              f'<div style="aspect-ratio:1; background:{GREEN}; position:relative; overflow:hidden"><div style="position:absolute; left:8%; right:8%; top:50%; transform:translateY(-50%) rotate(-4deg)">{face_front("100%")}</div></div>'
              + "".join(f'<div style="aspect-ratio:1; position:relative; overflow:hidden">{P(k, 300, pos_)}</div>' for k, pos_ in (("mother", "50% 45%"), ("teabowl", "50% 50%"), ("forest", "50% 50%"))) + '</div>'
              f'<div class="col" style="left:[[540]]; right:[[40]]; top:[[90]]; gap:[[16]]">{wm("[[260]]", INK)}'
              + caps("naʻau × Ivycoast · Organic kombucha bar soap", "[[11]]", "position:static")
              + f'<p style="position:static; {JPB}; font-size:[[24]]; line-height:1.5">{br(TAG[0])}</p>'
              f'<p style="position:static; font-family:var(--sans); font-size:[[12]]; line-height:1.9; color:#3E3833">{HONEST[0]}名古屋の naʻau が仕込んだコンブチャと SCOBY を、Ivycoast が海辺の工房で練り込み、手で切り分け、60日かけて熟成させました。香りは、雨のあとの森とむいたばかりのマンダリン。</p>'
              f'<p style="position:static; {SANS}; font-size:[[22]]">¥［　］<span style="font-size:[[11]]">（税込）</span></p>'
              + rows([("コンブチャ", "naʻau · 愛知県名古屋市"), ("SCOBY", "naʻau の仕込みから"), ("製法", "コールドプロセス · 60日熟成"), ("香り", "シダーウッド、パチュリ、マンダリン、ホワイトセージ")], "[[11]]", pad="[[6]]") +
              f'<p style="position:static; background:{GREEN}; color:{PAPER}; text-align:center; padding:[[12]] 0; {SANS}; font-size:[[12]]; letter-spacing:.2em">カートに入れる</p></div>',
              "100%", f"background:{PAPER}; color:{INK}", cls="flat")

def banner(which):
    if which == "ivy":
        return ab(16, 6, f'<p style="left:[[60]]; top:[[56]]; {SANS}; font-size:[[14]]; letter-spacing:.2em; color:{GREEN}">NEW · COLLABORATION</p>'
                  f'<p style="left:[[60]]; top:[[96]]; font-family:var(--lat); font-size:[[52]]; line-height:1.15; color:{GREEN}">Once,<br>it was tea.</p>'
                  f'<p style="left:[[60]]; top:[[232]]; font-family:var(--lat); font-size:[[17]]; line-height:1.5; color:{GREEN}; width:[[340]]">Kombucha and its mother, cut by hand by the sea.</p>'
                  f'<p style="left:[[60]]; bottom:[[48]]; {SANS}; font-size:[[13]]; letter-spacing:.16em; color:{GREEN}; border-bottom:1px solid {GREEN}; padding-bottom:[[4]]">DISCOVER KOM’BAR</p>'
                  f'<div class="ab flat" style="right:0; top:0; bottom:0; width:[[560]]"><div class="fill">{P("jar", 1000, "30% 50%")}</div>'
                  f'<div style="left:[[-70]]; bottom:[[-30]]; width:[[260]]">{el("bird", "100%", WHITE)}</div></div>',
                  "100%", f"background:{PAPER}", cls="flat")
    return ab(16, 6, f'<div class="ab flat" style="left:0; top:0; bottom:0; width:[[560]]"><div class="fill">{P("mother", 1000, "50% 45%")}</div><div style="right:[[-80]]; bottom:[[-40]]; width:[[300]]">{el("mother", "100%", WHITE)}</div></div>'
              f'<p style="left:[[620]]; top:[[52]]; font-family:var(--sans); font-size:[[13]]; letter-spacing:.2em">NEW · コラボレーション</p>'
              f'<p style="left:[[620]]; top:[[92]]; font-family:var(--sans); font-weight:500; font-size:[[34]]; line-height:1.5">{TAG[0]}</p>'
              f'<p style="left:[[620]]; top:[[205]]; font-family:var(--sans); font-size:[[13]]; line-height:1.8; width:[[330]]">{DESCR[0]}。名古屋で仕込み、海辺の工房で切って、60日。</p>'
              f'<div style="left:[[620]]; bottom:[[44]]; width:[[190]]">{wm("100%", INK)}</div>',
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
            f'<dt>KOM’BAR</dt><dd>{KB_DEF2}</dd><dt>SCOBY（スコビー）</dt><dd>Explained once as 細菌と酵母の共生培養体.</dd></dl></div>'
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
              "Concept A · Lenora", "Black and white with one red, so the peach box stands out most here. Keep naʻau’s mark on black and Ivycoast on its own paper.", "lenora.html")
        + tie("#FAF7F1", ''
                         f'<div style="left:[[120]]; right:[[120]]; top:[[200]]; box-shadow:0 [[20]] [[40]] rgba(58,54,49,.16)">{face_front("100%")}</div>'
                         f'<div class="row" style="left:0; right:0; bottom:[[200]]; justify-content:center; gap:[[40]]">{L(D["ogg"], "3a3631", "[[220]]")}<span style="font-size:[[40]]">×</span>{IVY("dark", "[[250]]")}</div>',
              "Concept B · Ogg", "The warmest fit: Ogg’s calligraphic serif and Ivycoast’s flared serif feel related but distinct.", "ogg.html")
        + '</div>')

# ====================================================================== 11 borrowed
BORROWED = [
    ("Wine and chocolate labels set like spec sheets", "Plain facts in ruled rows", "Our rows hold the Japanese cosmetic label in its legal order, on the back only; the front stays Ivycoast’s illustration."),
    ("Kombucha back labels that speak plainly", "A plain, personal voice", "Our back carries the brand’s own story of fermentation, in their words, with no jokes and no claims."),
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
        ("", "naʻau", ["Kombucha ferment and SCOBY supply", "The naming story and the brand voice", "Product page on the naʻau shop", "Counter card and workshop tie-in"]),
        ("together", "Together", ["Agree the ten elements and their meanings", "A photography day in both studios", "Launch posts as Instagram collab posts", "One shared copy deck, checked against 薬機法", "Launch date: ［　］"])]) + '</div>')

# ====================================================================== scenes: printed pieces as objects on a surface
def obj(x, y, w, inner, rot=0, z=1, shadow="paper"):
    """Place a printed piece in a scene: x, y, w in % of the scene; it keeps its own proportions."""
    sh = {"paper": "0 1px 1px rgba(0,0,0,.08), 0 14px 22px -10px rgba(0,0,0,.30), 0 40px 70px -30px rgba(0,0,0,.28)",
          "deep": "0 2px 2px rgba(0,0,0,.18), 0 24px 40px -14px rgba(0,0,0,.45), 0 60px 90px -40px rgba(0,0,0,.4)", "none": "none"}[shadow]
    return f'<div class="obj" style="left:{x}%; top:{y}%; width:{w}%; transform:rotate({rot}deg); z-index:{z}"><div style="box-shadow:{sh}">{inner}</div></div>'

def scene(bg, ratio, objs, cls=""):
    return f'<div class="scene {cls}" style="background:{bg}; aspect-ratio:{ratio}">{objs}</div>'

def chapter(n, title, desc, content, bg="var(--page)", fg="var(--ink)", sid="", cls=""):
    idattr = f' id="{sid}"' if sid else ""
    return (f'<section class="chap {cls}"{idattr} style="background:{bg}; color:{fg}"><div class="wrap">'
            f'<header class="chap-h"><p class="chap-l"><span>{n}</span>{title}</p>' + (f'<p class="chap-d">{desc}</p>' if desc else '') + f'</header>{content}</div></section>')

def cap(title, spec=""):
    return f'<p class="scap"><b>{C.t(title)}</b>{(" — " + C.t(spec)) if spec else ""}</p>'

# ---------------- cover
cover = (f'<header class="cover2" style="background:{GREEN}; color:{WHITE}"><div class="wrap cover2-in">'
         f'<div class="cover2-top"><span>naʻau × Ivycoast</span><span>A proposal for both teams · 2026</span></div>'
         f'<div class="cover2-box">{face_front("100%")}</div>'
         f'<div class="cover2-foot"><p class="cover2-jp">{C.T(br(TAG[0]), TAG[1])}</p><p class="kb2-def">{KB_DEF0}</p>'
         f'<div class="cover2-lock">{pair("150px", "ffffff", "white")}</div></div>'
         f'</div></header>')

# ---------------- 01 the idea
idea = ('<div class="idea2">'
        f'<div class="idea2-pic">{P("mother", 1600, "50% 45%")}<div class="idea2-el">{el("mother", "100%", GREEN)}</div></div>'
        f'<div class="idea2-txt"><p class="idea2-tag">{C.T(TAG[0], TAG[1])}</p>'
        f'<p class="idea2-sub">{C.T(DESCR[0], "Kombucha &amp; SCOBY bar soap")}</p>'
        f'<p class="idea2-p">{C.T(HONEST[0], HONEST[1])}</p>'
        '<dl class="idea2-num">' + "".join(f'<div><dt>{n}</dt><dd>{C.T(j, e)}</dd></div>' for n, j, e in (("14", "naʻau で仕込む日数", "days brewing at naʻau"), ("60", "熟成させる日数", "days curing"), ("4", "香りに使う精油の数", "essential oils, nothing else"))) + '</dl>'
        '</div></div>'
        '<div class="idea"><div class="idea-makers">'
        f'<div>{NAAU("96px")}<p>Small-batch kombucha, brewed in Nagoya.</p></div>'
        f'<div>{IVY("dark", f"calc(96px * {IVY_K:.4f})")}<p>Australian botanicals, brought into Japanese homes for daily rituals.</p></div>'
        '</div></div>')

# ---------------- 02 the product: the box, every side
def lay(x, y, w, inner, label):
    return obj(x, y, w, inner + f'<p class="lay-l">{label}</p>', 0, 1)

# ---------------- how it's made: Ivycoast's cold-process copy, adapted for KOM'BAR (no CBD superfat)
PROCESS_JP = [
    "コールドプロセスという方法で。熱を加えず、近道もしない。植物油は反応そのものが生む穏やかな熱だけで変化し、そのままの力を保ちます。",
    "そして、時間に委ねます。二ヶ月間の熟成を経て、やさしく、しっとりとした使い心地の石鹸が完成します。",
    "配合はシンプルに。植物由来のオイル、水酸化ナトリウム、精製水、そして naʻau のコンブチャと SCOBY。合成香料も、添加物も、防腐剤も、着色料も使いません。香りは四つの精油だけ。",
]
PROCESS = ('<div class="proc"><p class="proc-lead">ゆっくりと。<span>それが、私たちの石鹸のつくり方です。</span></p>'
           '<div class="proc-body">' + "".join(f'<p>{t}</p>' for t in PROCESS_JP) +
           '<p class="it">Slowly. Cold process: no added heat, no shortcuts, two months of curing. Plant oils, sodium hydroxide and water, '
           'with naʻau’s kombucha and SCOBY. Nothing synthetic; the scent is four essential oils.</p></div></div>')
INGR_BLOCK = (f'<div class="ingr"><p class="ingr-h">Ingredients / 全成分</p><p class="jp">{INGREDIENTS}</p></div>')

# all panels at one scale: 90 mm = 43% of the scene width
MM = 43 / 90
# front and back large, one end beside them at true scale; the lid and base live on the dieline
MM = 56 / 90
product_scene = scene("#ECE7DE", "16/11",
    lay(5, 6, 56, face_front("100%"), "Front") + lay(66, 6, 30 * MM, face_end("mother"), "End") +
    lay(5, 53, 56, face_back("100%"), "Back"))
card_scene = scene(GREEN, "4/5", obj(12, 7, 76, insert_card("100%"), 0, 1, "deep"))
product2 = (product_scene + cap("The box", "the front as Ivycoast designed it; a new back; one element on each end. Lid and base on the dieline below") +
            '<div class="two-uneven rev" style="margin-top:clamp(28px,4vw,56px)"><div>' + card_scene + cap("Story card inside the lid, 85 × 120 mm", "the full text") + '</div>'
            f'<dl class="facts facts-lg" style="align-self:center"><dt>Name</dt><dd>{KB_DEF1}</dd><dt>Product</dt><dd>Organic kombucha cold-processed bar soap</dd>'
            '<dt>Made with</dt><dd>naʻau kombucha, and SCOBY powder as a gentle scrub</dd><dt>Made by</dt><dd>Ivycoast, by hand</dd>'
            '<dt>Method</dt><dd>Cold process, cured for two months</dd><dt>Scent</dt><dd>Cedarwood, patchouli, mandarin and white sage essential oils</dd>'
            '<dt>Box</dt><dd>90 × 44 × 30 mm ［to confirm］</dd><dt>Weight</dt><dd>［　g］</dd></dl></div>'
            + PROCESS + INGR_BLOCK +
            '<div style="margin-top:clamp(40px,5vw,72px); background:#F6F1E9; padding:clamp(20px,4vw,56px)">' + dieline() + '</div>' + cap("Dieline", "to confirm with Ivycoast’s printer"))

# ---------------- 03 the artwork system
system_c = ('<div class="kel-grid kel-5">' + "".join(tile(i, n) for i, n in enumerate(KB.ORDER)) + '</div>'
            '<div class="sysrow"><div><p class="eyebrow">Colour</p>' + C.chips([(n, h, r, w) for n, h, r, w in PAL]) + '</div></div>')

# ---------------- 04 the world
opening = scene(GREEN, "16/9",
    obj(3, -6, 46, mailer_inside(), -3, 1) +
    obj(44, 6, 50, tissue(), 2, 2, "paper") +
    obj(50, 22, 14, card1(0), -12, 4) + obj(60, 20, 14, card1(1), -3, 5) + obj(70, 23, 14, card1(2), 6, 6) + obj(80, 30, 14, card1(3), 14, 7) +
    obj(16, 58, 34, face_front("100%"), -6, 8, "deep"))
market = scene("#ECE7DE", "4/3",
    obj(6, 4, 52, band("01", "26.11.03", GREEN), -6, 1, "none") + obj(40, 30, 52, band("02", "26.11.24", INK), 4, 2, "none") + obj(4, 46, 52, band("03", "26.12.15", AMBER), -2, 3, "none"))
counter_s = scene(WHITE, "3/4", obj(22, 14, 56, counter, -2, 1, "deep"))
poster_s = scene("#ECE7DE", "3/4", obj(20, 9, 60, poster, 0, 1, "deep"))
gift_s = scene("#ECE7DE", "16/9", obj(8, 10, 54, kakegami(), -3, 1, "deep") + obj(58, 30, 36, mailer(), 5, 2))

# ---------------- posts: a photograph, one drawn element crossing its edge, one line
def photo_box(key, l, t, r, b_, pos="50% 50%", w=900):
    return f'<div style="left:{l}; top:{t}; right:{r}; bottom:{b_}">{P(key, w, pos)}</div>'

post_a = post(photo_box("jar", 0, 0, 0, "[[400]]", "35% 50%")
              + f'<div style="left:[[590]]; top:[[600]]; width:[[440]]; z-index:2">{el("mother", "100%", WHITE)}</div>'
              + f'<p style="left:[[70]]; top:[[1000]]; {JPB}; font-size:[[58]]; line-height:1.45; color:{WHITE}">{TAG[0]}</p>'
              + f'<p class="it" style="left:[[70]]; bottom:[[70]]; font-family:var(--lat); font-size:[[32]]; color:{WHITE}">{TAG[1]}</p>'
              + f'<div style="right:[[70]]; bottom:[[78]]; width:[[200]]">{wm("100%", WHITE)}</div>', GREEN)
post_b = post(photo_box("mother", "[[400]]", 0, 0, 0, "45% 50%")
              + f'<p class="vt" style="left:[[110]]; top:[[110]]; {JPB}; font-size:[[66]]; line-height:1.7; letter-spacing:.1em">{MOTHER[0]}</p>'
              + f'<div style="left:[[210]]; top:[[760]]; width:[[400]]; z-index:2">{el("mother", "100%", GREEN)}</div>'
              + f'<p class="it" style="left:[[70]]; bottom:[[70]]; font-family:var(--lat); font-size:[[30]]">{MOTHER[1]}</p>', WHITE)
post_c = post(photo_box("mandarin", 0, 0, 0, 0, "50% 55%")
              + f'<p style="left:[[70]]; top:[[100]]; {JPB}; font-size:[[50]]; line-height:1.6; color:{WHITE}">{SCENT[0]}</p>'
              + f'<p class="it" style="left:[[70]]; top:[[290]]; font-family:var(--lat); font-size:[[30]]; color:{WHITE}; opacity:.8">{SCENT[1]}</p>'
              + f'<div style="right:[[70]]; bottom:[[170]]; width:[[230]]">{el("lemon", "100%", TURMERIC)}</div>'
              + caps("Cedarwood · Patchouli · Mandarin · White sage", "[[19]]", f"position:absolute; left:[[70]]; bottom:[[80]]; color:{WHITE}; opacity:.75"), "#0B0B0A")
post_t = post(photo_box("batter", 0, 0, 0, "[[620]]", "50% 50%")
              + f'<div style="left:[[560]]; top:[[520]]; width:[[360]]; z-index:2">{el("sun", "100%", PERSIMMON)}</div>'
              + "".join(f'<p style="left:[[{x}]]; top:[[790]]; font-family:var(--lat); font-size:[[230]]; line-height:1">{n}</p>'
                        f'<p style="left:[[{x + 6}]]; top:[[1050]]; {JPB}; font-size:[[38]]">{jp}</p>' for x, n, jp in ((70, "14", "日、仕込む。"), (520, "60", "日、待つ。")))
              + f'<p class="it" style="left:[[76]]; bottom:[[70]]; font-family:var(--lat); font-size:[[28]]; opacity:.7">{NUM[1]}</p>', WHITE)
story_o = ab(9, 16, photo_box("hands", 0, 0, 0, 0, "50% 60%", 1000)
             + f'<div style="left:[[70]]; right:[[70]]; top:[[110]]">{wm("100%", GREEN)}</div>'
             + f'<p style="left:[[70]]; top:[[360]]; {JPB}; font-size:[[64]]; line-height:1.5; color:{GREEN}">{TAG[0]}</p>'
             + f'<div style="right:[[70]]; bottom:[[110]]; width:[[230]]">{el("bird", "100%", GREEN)}</div>'
             + caps("naʻau × Ivycoast · ［月日］", "[[28]]", f"position:absolute; left:[[70]]; bottom:[[120]]; color:{GREEN}"),
             "100%", f"background:{WHITE}", cls="flat story")
posts_row = ('<div class="soc">' + pf(post_a, "Tagline post", "the kombucha jar; the mother drawn over the real one, crossing into green", plate=False)
             + pf(post_b, "A soap with a mother", "the SCOBY photographed; the drawn mother laid across its edge", plate=False)
             + pf(post_c, "The scent", "a scene, not a list; the drawn citrus beside the real one", plate=False)
             + pf(story_o, "Story", "hands, the tagline and the bird", plate=False) + '</div>')

feed = [post_a, p_reveal, post_t, post_b, ab(3, 4, f'<div style="left:[[200]]; right:[[200]]; top:50%; transform:translateY(-50%)">{el("tea", "100%", GREEN)}</div>', "100%", f"background:{WHITE}", cls="flat"), post_c]
phone_feed = (f'<div class="phone big"><div class="phone-screen"><div class="ig-head">{wm("38%", INK)}<span>naʻau × Ivycoast</span></div>'
              f'<div class="ig-grid">' + "".join(f'<div>{p}</div>' for p in feed) + '</div></div></div>')
feed_s = f'<div class="scene" style="background:{GREEN}; aspect-ratio:4/3; display:flex; align-items:center; justify-content:center">{phone_feed}</div>'
world = ('<h3 class="wsub">Opening the box</h3>' + opening + cap("Opening the box", "inside the lid, the brand’s closing line set vertically; tea-leaf tissue, four story cards, the bar")
         + '<h3 class="wsub">At the counter and at markets</h3><div class="two-uneven"><div>' + market + cap("Batch bands", "the bare bar, dated with a round date stamp for each cure") + '</div><div>' + counter_s + cap("Counter card, A6") + '</div></div>'
         + '<h3 class="wsub">Posts</h3>' + posts_row
         + '<h3 class="wsub">Launch</h3><div class="two-uneven rev"><div>' + poster_s + cap("Poster, A3", "for both shop windows") + '</div><div>' + feed_s + cap("The feed", "collab posts from both accounts") + '</div></div>'
         + '<h3 class="wsub">How it’s made</h3>' + carousel + cap("Carousel, five slides", "five photographs, tea to scent; on each, one element crosses the photograph’s edge")
         + '<h3 class="wsub">Online</h3>' + web
         + '<h3 class="wsub">As a gift</h3>' + gift_s + cap("Gift set and mailer", "a white 掛け紙 band on green; the route from Nagoya to the Ivycoast studio on the mailer"))

# ---------------- 05 voice
PRINCIPLES = [
    ("素材と、場所と、人で名づける。", "Name it by what, where and who.", "SHIRO · Flamingo Estate", f"{DESCR[0]}／naʻau（名古屋）のコンブチャ"),
    ("本当の数字を、ひとつ。", "One true number.", "Le Labo", "14日、仕込む。60日、待つ。"),
    ("香りは、情景で。", "Scent as a scene, not a list.", "Le Labo · Aesop", br(SCENT[0])),
    ("時間こそ、贅沢。", "Time is the luxury.", "Aesop · SHIRO", "仕込む、育てる、切る、待つ。"),
    ("飾らず、正直に。", "Say the plain truth.", "SHIRO", HONEST[0]),
    ("表は静かに、裏は詳しく。", "A quiet front, a full back.", "Aesop", "表：名前と一行だけ。裏：物語、使い方、全成分。"),
]
VOICE_LINES = [("Tagline", TAG), ("Descriptor", DESCR), ("The mother", MOTHER), ("The numbers", NUM), ("Scent", SCENT), ("Origin", ORIGIN), ("Use", USE)]
voice = (f'<div class="voice-lead"><p class="jp">{TAG[0]}</p><p class="it">{TAG[1]}</p></div>'
         '<div class="vprin">' + "".join(f'<div><p class="vprin-n">{i:02d}</p><p class="vprin-h">{C.T(j, e)}</p><p class="vprin-x">{x}</p><p class="vprin-r">{C.T("参考：", "From ")}{r}</p></div>'
                                         for i, (j, e, r, x) in enumerate(PRINCIPLES, 1)) + '</div>'
         '<h3 class="lang-h">' + C.T("言葉の一覧", "The lines") + '</h3><div class="vlines">'
         + "".join(f'<div><p class="vlines-k">{C.t(k)}</p><p class="jp">{br(j)}</p><p class="it">{e}</p></div>' for k, (j, e) in VOICE_LINES) + '</div>'
         '<p class="muted" style="font-size:14px; margin-top:12px">' + C.T("14日と60日は、naʻau と Ivycoast に確認のうえ使用します。数字は本当のものだけを使います。", "Fourteen and sixty days to be confirmed with naʻau and Ivycoast; we only print numbers that are true.") + '</p>'
         '<div class="lang"><div><p class="lang-voice"><b>Japanese first, English as its own line.</b> Each line is written twice, not translated: Japanese in calm です/ます or short verb-less phrases; English drier and shorter. No exclamation marks, no superlatives, no claims.</p>'
         '<h3 class="lang-h">Names</h3><dl class="facts"><dt>naʻau × Ivycoast</dt><dd>With the ʻokina, and a multiplication sign ×, not the letter x.</dd>'
         f'<dt>KOM’BAR</dt><dd>{KB_DEF2}</dd><dt>SCOBY（スコビー）</dt><dd>Explained once as 細菌と酵母の共生培養体; called 「母」 the mother, in brackets, as brewers do.</dd></dl></div>'
         '<div><h3 class="lang-h" style="margin-top:0">Words we can use, for soap</h3>'
         '<ul class="words ok">' + "".join(f'<li class="jp">{w}</li>' for w in ("肌を清浄にする（洗浄により）", "肌を整える／肌のキメを整える", "皮膚をすこやかに保つ", "SCOBYの粉末をスクラブとして配合", "香り：シダーウッド、マンダリンなど精油の名前")) + '</ul>'
         '<h3 class="lang-h">Words we avoid</h3><ul class="words no">' + "".join(f'<li class="jp">{w}</li>' for w in ("美白、アンチエイジング、若返る", "「発酵の力で肌が生まれ変わる」など、効能をうたう表現", "腸活・腸内環境など、飲料の健康効果と石鹸を結びつける表現", "「生きた菌が肌に働く」など、菌の作用をうたう表現", "リラックス効果など、精油の効能", "治る、改善、医師・看護師がすすめる")) + '</ul>'
         '<p class="muted" style="font-size:13px; margin-top:14px">Final copy to be checked against 薬機法 by the party holding the cosmetics licence.</p></div></div>')

# ---------------- 06 next steps
decide = ('<ol class="decide">' + "".join(f'<li><span>{i:02d}</span><p>{t}</p></li>' for i, t in enumerate([
    "Agree the ten elements and what each one means.",
    "Confirm the box size, the back panel copy and 全成分 with Ivycoast’s printer and the cosmetics licence holder.",
    "Book a photography day in both studios: the brewing jar, the pour, cutting and curing the bars.",
    "Set the launch date, then schedule the collab posts and the countdown.",
    "Choose naʻau’s direction; the collaboration uses Concept B for now."], 1)) + '</ol>')
nexts = (decide + '<div class="sub"><h3>Who does what</h3><p></p></div>' + roles +
         '<div class="sub"><h3>With each naʻau direction</h3><p>The box stays the same; the naʻau logo changes.</p></div>' + ties +
         '<details class="borrowed"><summary>What we borrowed from the references, line by line</summary>' + borrowed + '</details>')

body = (KB.DEFS + C.nav("collab") + cover +
        chapter("01", "The idea", "", idea, sid="idea") +
        chapter("02", "The product", "The box, every side.", product2, sid="product") +
        chapter("03", "The artwork", "Ten elements from one illustration, used one at a time.", system_c, bg=INK, fg=PAPER, sid="artwork", cls="dark") +
        chapter("04", "The world", "Every piece, as it will be used.", world, sid="world") +
        chapter("05", "The voice", "", voice, sid="voice") +
        chapter("06", "Next steps", "", nexts, sid="next") +
        '<footer class="site"><div class="wrap">naʻau × Ivycoast · a proposal for discussion. Text in ［brackets］ is to be confirmed. Artwork, KOM’BAR wordmark and Ivycoast logos from the Ivycoast files.</div></footer>')
C.page("collab.html", "naʻau × Ivycoast — KOM’BAR", "d-collab", body)
print("collab written")
