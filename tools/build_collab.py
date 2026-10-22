"""collab.html: naʻau × Ivycoast — KOM'BAR, the assets we plan, the shared language, and how it sits with each direction.

The page borrows the KOM'BAR package's own language: peach stock, black artwork, a bold vertical
product name, tracked capitals, and the two names stacked in black.
"""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
from common import D, L, ab, fitw, pf, ph, still, sec
C.SITE = sys.argv[1]

PEACH, INK, MUTE = "#F4D9C6", "#1E1E1E", "#6E655B"
ART = lambda w, style="": f'<img src="assets/collab/kombar-artwork.svg" alt="KOM’BAR artwork: a woman holding a SCOBY among plants, sun and bird" style="width:{w}; {style}">'
IVY = lambda col, w, style="": f'<img src="assets/collab/ivycoast-wordmark-{col}.png" alt="IVYCOAST" style="width:{w}; {style}">'
IVYICON = lambda w: f'<img src="assets/collab/ivycoast-icon-green.png" alt="" style="width:{w}">'
NAAU = lambda w, col="1e1e1e", style="": f'<img src="assets/logos/current-naau-{col}.png" alt="naʻau" style="width:{w}; {style}">'

def lockup(w_naau, w_ivy, gap="[[22]]", align="flex-end", col="1e1e1e", ivy="dark"):
    return f'<div class="col" style="align-items:{align}; gap:{gap}">{NAAU(w_naau, col)}{IVY(ivy, w_ivy)}</div>'

def soapbox(width, style=""):
    return ab(3, 2, f'<p style="left:[[70]]; bottom:[[70]]; writing-mode:vertical-rl; text-orientation:sideways; transform:rotate(180deg); font-family:Inter; font-weight:700; font-size:[[118]]; line-height:.9; letter-spacing:.01em; white-space:nowrap">KOM’BAR</p>'
              f'<div style="left:[[300]]; top:[[80]]; width:[[400]]">{ART("100%")}</div>'
              f'<p style="right:[[60]]; bottom:[[60]]; text-align:right; font-family:Inter; font-size:[[24]]; letter-spacing:.2em; line-height:1.8">ORGANIC KOMBUCHA<br>COLD PROCESSED BAR SOAP</p>',
              width, f"background:{PEACH}; color:{INK}; {style}")

# ------------------------------------------------------------------ hero, in the package's language
hero = (f'<header class="kb"><div class="wrap kb-grid">'
        f'<p class="kb-name">KOM’BAR</p>'
        f'<div class="kb-art">{ART("100%")}</div>'
        f'<div class="kb-side"><p class="kb-eyebrow">naʻau × Ivycoast · 2026</p>'
        f'<div class="kb-mid"><p class="kb-jp">発酵が生み出す美しさ。</p><p class="kb-en">A cold-process bar soap made with naʻau’s kombucha and the SCOBY that brews it.</p></div>'
        f'<div class="kb-foot"><p class="kb-caps">ORGANIC KOMBUCHA<br>COLD PROCESSED BAR SOAP</p>'
        f'<div class="kb-lock">{NAAU("118px")}{IVY("dark", "150px")}</div></div></div>'
        f'</div></header>')

intro = ('<section class="wrap kb-intro">'
         '<p class="kb-lead">Ivycoast brings Australian botanicals into Japanese homes for daily rituals. naʻau brews kombucha in Nagoya to help people listen to their bodies. Together we made a soap.</p>'
         '<div><p class="muted">This page is for both teams: what we plan to make, the words we will use, and how the collaboration sits with each naʻau direction.</p>'
         '<ol class="toc">' + "".join(f'<li><a href="#{a}"><span>{n}</span>{t}</a></li>' for n, a, t in [
             ("01", "brands", "Two brands, one ritual"), ("02", "product", "The product"), ("03", "assets", "Assets we plan to make"),
             ("04", "language", "Website language"), ("05", "ties", "How it ties to each direction"), ("06", "roles", "Who does what")]) + '</ol></div></section>')

# ------------------------------------------------------------------ 01 brands
brands = ('<div class="pair">'
          f'<div class="side"><div class="side-mark">{IVYICON("38px")}{IVY("green", "170px")}</div>'
          '<p class="side-lead">Australian botanicals, brought into Japanese homes for daily rituals.</p>'
          '<dl class="facts"><dt>Voice</dt><dd>Calm and considered; ordinary moments, elevated just enough.</dd><dt>Language</dt><dd>English-led, with Japanese.</dd><dt>Look</dt><dd>Cream and deep green, a flared serif, beach light.</dd></dl></div>'
          '<div class="join" aria-hidden="true">×</div>'
          f'<div class="side"><div class="side-mark">{NAAU("124px")}</div>'
          '<p class="side-lead">Small-batch kombucha, brewed in Nagoya by kimy.</p>'
          '<dl class="facts"><dt>Voice</dt><dd>Warm, personal and a little playful.</dd><dt>Language</dt><dd>Japanese-led, with English.</dd><dt>Look</dt><dd>Being decided: three directions, see <a href="index.html">the overview</a>.</dd></dl></div>'
          '</div>'
          '<div class="shared"><p class="eyebrow" style="color:#6E655B">Where they meet</p><div class="shared-grid">' +
          "".join(f'<div><span class="jp">{k}</span><h3>{t}</h3><p>{b}</p></div>' for k, t, b in [
              ("儀式", "Ritual", "Small acts of care, repeated every day."),
              ("時間", "Time", "Kombucha ferments for weeks; cold-process soap cures for weeks."),
              ("素材", "Materials", "Natural ingredients, chosen carefully."),
              ("手", "Hands", "Made by hand, in small batches.")]) + '</div></div>')

# ------------------------------------------------------------------ 02 product
product = ('<div class="grid g-wide" style="align-items:start">'
           + pf(f'<div style="padding:clamp(18px,3vw,40px)">{"<img src=\"assets/collab/kombar-package-front.jpg\" alt=\"KOM’BAR package, front and inside panels\" style=\"width:100%\">"}</div>', "Package, outside and inside", "The current design: peach stock, the illustration, the story inside the lid.", pstyle="background:#5A5550") +
           '<div style="display:flex; flex-direction:column; gap:clamp(20px,3vw,32px)">'
           + pf(f'<div style="padding:clamp(14px,2vw,24px)"><img src="assets/collab/kombar-package-back.jpg" alt="KOM’BAR package, back panel with both names" style="width:100%"></div>', "Back panel", "Both names, stacked.", pstyle="background:#5A5550") +
           '<dl class="facts facts-lg"><dt>Product</dt><dd>Organic kombucha cold-processed bar soap</dd><dt>Made with</dt><dd>naʻau kombucha ferment, and SCOBY powder as a gentle scrub</dd>'
           '<dt>Made by</dt><dd>Ivycoast, by hand</dd><dt>Weight</dt><dd>［　g］</dd><dt>全成分</dt><dd>［to confirm］</dd></dl></div></div>')

# ------------------------------------------------------------------ 03 assets
def slide(n, jp, en, inner, bg):
    return ab(4, 5, inner + f'<p style="left:[[60]]; top:[[56]]; font-family:Inter; font-size:[[40]]; letter-spacing:.14em">{n}</p>'
              f'<div class="col" style="left:[[60]]; bottom:[[56]]; gap:[[8]]"><p class="jp" style="font-family:var(--sans); font-weight:700; font-size:[[78]]">{jp}</p><p style="font-family:Inter; font-size:[[34]]">{en}</p></div>',
              "29%", f"background:{bg}; color:{INK}")

carousel = (slide("01", "発酵", "Kombucha, brewed by naʻau", ph("collab", "jar", "0", "[[-40]]", "100%", "4/4.4", label="current", zoom=2.6), "#F2E7DB") +
            slide("02", "SCOBY", "Dried and milled to a scrub", f'<div style="left:[[200]]; top:[[170]]; width:[[600]]; aspect-ratio:1; border-radius:50%; background:radial-gradient(circle at 40% 35%, #F1E4C8, #D9C29A 60%, #C4A574); box-shadow:inset 0 0 0 [[14]] rgba(255,255,255,.25)"></div>', "#F2E7DB") +
            slide("03", "石鹸", "Cured for weeks by Ivycoast", f'<div style="left:[[150]]; top:[[190]]; width:[[700]]">{ART("100%")}</div>', PEACH))

product_card = ab(4, 3, f'<div style="left:[[50]]; top:[[60]]; width:[[440]]; aspect-ratio:1; background:{PEACH}; display:flex; align-items:center; justify-content:center">{ART("72%")}</div>'
                  f'<div class="col" style="left:[[540]]; right:[[50]]; top:[[70]]; gap:[[24]]; font-family:var(--sans)">'
                  f'<p style="font-family:Inter; font-weight:700; font-size:[[52]]">KOM’BAR</p><p style="font-size:[[30]]; color:{MUTE}">naʻau × Ivycoast</p>'
                  f'<p style="font-size:[[38]]">¥［　］<span style="font-size:[[24]]">（税込）</span></p>'
                  f'<p style="font-size:[[24]]; line-height:1.8">丁寧に仕込んだコンブチャの発酵液と、SCOBYの粉末を。</p>'
                  f'<p style="background:{INK}; color:#fff; text-align:center; padding:[[18]] 0; font-size:[[26]]; margin-top:[[10]]">カートに入れる</p></div>'
                  f'<p style="left:[[50]]; bottom:[[50]]; font-family:var(--sans); font-size:[[22]]; color:{MUTE}">ivycoast ・ naʻau　同じ写真と文章で</p>', "86%", "background:#fff")

launch = ab(3, 4, f'<div style="left:[[140]]; top:[[120]]; width:[[720]]">{ART("100%")}</div>'
            f'<div class="row" style="left:[[80]]; right:[[80]]; bottom:[[80]]; justify-content:space-between; align-items:flex-end">'
            f'<p style="font-family:Inter; font-weight:700; font-size:[[64]]">KOM’BAR</p>{lockup("[[190]]", "[[240]]", gap="[[14]]")}</div>', fitw(1, .75, .84), f"background:{PEACH}; color:{INK}")

counter = ab(105, 148, f'<p style="left:[[80]]; top:[[90]]; font-family:var(--sans); font-weight:700; font-size:[[66]]; line-height:1.6">発酵が<br>生み出す美しさ。</p>'
             f'<div style="left:[[180]]; top:[[440]]; width:[[640]]">{ART("100%")}</div>'
             f'<p style="left:[[80]]; bottom:[[90]]; font-family:Inter; font-size:[[30]]; letter-spacing:.16em; line-height:1.8">KOM’BAR<br>ORGANIC KOMBUCHA SOAP</p>'
             f'<div style="right:[[80]]; bottom:[[90]]">{lockup("[[180]]", "[[230]]", gap="[[12]]")}</div>', fitw(1, 105 / 148, .8), f"background:{PEACH}; color:{INK}")

assets = ('<div class="grid g3">'
          + pf(soapbox("84%"), "Soap box", "Ivycoast · exists. Finalise the copy, 全成分 and barcode.", "1/1")
          + pf(product_card, "Product page", "Both shops · the same photographs and copy on Ivycoast and naʻau.", "1/1", pstyle="background:#E9E2D8")
          + pf(launch, "Launch post, 3:4", "Posted by both accounts as one Instagram collab post.", "1/1")
          + pf(carousel, "How it’s made, carousel", "Kombucha → SCOBY → soap, with photographs from both studios.", "1/1", pstyle="gap:3%")
          + pf(counter, "Counter card, A6", "At the naʻau counter and Ivycoast stockists.", "1/1")
          + pf(still("collab", "gift", "1/1", label="current", zoom=2.0), "Proposal · gift set", "A bottle of naʻau with KOM’BAR, for the holidays.", plate=False)
          + '</div>')

# ------------------------------------------------------------------ 04 language
LINES = [("発酵が生み出す美しさ。", "The beauty that fermentation makes."),
         ("育てる時間。手をかけること。自然から学ぶこと。", "Time to grow. Care by hand. Learning from nature."),
         ("丁寧に仕込んだコンブチャの発酵液と、SCOBYの粉末を。", "Carefully brewed kombucha, and the SCOBY that made it.")]
language = ('<div class="lang">'
            '<div><p class="lang-voice"><b>Japanese first, English as a quiet second line.</b> Sensory and process-led: what it is, how it’s made, how it feels to use. Calm like Ivycoast; warm and personal like naʻau. No exclamation marks, no superlatives.</p>'
            '<h3 class="lang-h">Key lines</h3><div class="lines">' + "".join(f'<div><p class="jp">{j}</p><p class="it">{e}</p></div>' for j, e in LINES) + '</div>'
            '<h3 class="lang-h">Names</h3><dl class="facts"><dt>naʻau × Ivycoast</dt><dd>With the ʻokina, and a multiplication sign ×, not the letter x.</dd>'
            '<dt>KOM’BAR</dt><dd>The product name, always in capitals.</dd><dt>SCOBY（スコビー）</dt><dd>Explained once as 細菌と酵母の共生培養体.</dd></dl></div>'
            '<div><h3 class="lang-h" style="margin-top:0">Words we can use, for soap</h3><p class="muted" style="font-size:15px; margin-bottom:10px">Soap is a cosmetic, so claims stay inside the approved cosmetic effects.</p>'
            '<ul class="words ok">' + "".join(f'<li class="jp">{w}</li>' for w in ("肌を清浄にする（洗浄により）", "肌を整える／肌のキメを整える", "皮膚をすこやかに保つ", "SCOBYの粉末をスクラブとして配合")) + '</ul>'
            '<h3 class="lang-h">Words we avoid</h3><ul class="words no">' + "".join(f'<li class="jp">{w}</li>' for w in ("美白、アンチエイジング、若返る", "「発酵の力で肌が生まれ変わる」など、効能をうたう表現", "腸活・腸内環境など、飲料の健康効果と石鹸を結びつける表現", "治る、改善、医師・看護師がすすめる")) + '</ul>'
            '<p class="muted" style="font-size:13px; margin-top:14px">Final copy to be checked against 薬機法 by the party holding the cosmetics licence.</p></div></div>')

# ------------------------------------------------------------------ 05 ties
def tie(bg, inner, label, note, link):
    return pf(ab(4, 5, inner, "100%", f"background:{bg}", cls="flat"), label, note + f' <a href="{link}">See the direction →</a>', plate=False)

sb = lambda: soapbox("100%")
ties = ('<div class="grid g3">'
        + tie("#FFFFFF", f'<div style="left:[[150]]; right:[[150]]; top:[[260]]">{sb()}</div><div class="row" style="left:0; right:0; bottom:[[220]]; justify-content:center; gap:[[40]]">{NAAU("[[200]]")}<span style="font-size:[[40]]">×</span>{IVY("dark", "[[250]]")}</div>',
              "白 Shiro", "White and plain, so the peach package leads. The script and the Ivycoast serif contrast clearly; neither overpowers.", "current.html")
        + tie("#2B2926", f'<div class="fill" style="padding:[[60]]"><div style="height:100%; border:1px solid #EFEBE2; outline:1px solid #EFEBE2; outline-offset:[[-14]]"></div></div>'
                         f'<div style="left:[[190]]; right:[[190]]; top:[[250]]">{sb()}</div><div class="row" style="left:0; right:0; bottom:[[220]]; justify-content:center; gap:[[40]]; color:#EFEBE2">{L(D["lenora"], "efebe2", "[[210]]")}<span style="font-size:[[40]]">×</span>{IVY("white", "[[250]]")}</div>',
              "一本 Ippon", "The most luxurious pairing, but two high-contrast serifs side by side can blur. Keep naʻau on sumi and Ivycoast on its own paper.", "lenora.html")
        + tie("#FAF7F1", f'<div style="right:[[90]]; top:[[110]]; width:[[520]]">{sb()}</div>'
                         f'<div style="left:[[90]]; top:[[560]]; width:[[560]]; padding:[[50]]; background:#FFFFFF; transform:rotate(-3deg); box-shadow:0 8px 20px rgba(58,54,49,.12)"><p class="hand" style="font-size:[[46]]; line-height:1.8; color:#3A3631">kombuchaから、<br>石鹸ができました。<br>— kimy</p></div>'
                         f'<div class="row" style="left:[[90]]; bottom:[[100]]; gap:[[40]]">{L(D["ogg"], "3a3631", "[[220]]")}<span style="font-size:[[40]]">×</span>{IVY("dark", "[[250]]")}</div>',
              "間 Ma", "The warmest fit: Ogg’s calligraphic serif and Ivycoast’s flared serif feel related but distinct, and kimy’s notes add the maker’s voice.", "ogg.html")
        + '</div>')

# ------------------------------------------------------------------ 06 roles
roles = ('<div class="roles">' + "".join(
    f'<div class="{cls}"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for cls, t, items in [
        ("", "Ivycoast", ["Soap formulation and production", "Cosmetics licences (化粧品製造業・製造販売業) or a licensed OEM", "Package, 全成分 and barcode", "Product page on Ivycoast"]),
        ("", "naʻau", ["Kombucha ferment and SCOBY supply", "The naming story and kimy’s voice", "Product page on the naʻau shop", "Counter card and workshop tie-in"]),
        ("together", "Together", ["A photography day in both studios: the process", "Launch posts as Instagram collab posts", "One shared copy deck, checked against 薬機法", "Launch date: ［　］"])]) + '</div>')

body = (C.nav("collab") + hero + intro +
        sec("01", "Two brands, one ritual", "Where Ivycoast and naʻau meet: small daily acts of care, and the patience of things that take weeks to make.", brands, sid="brands") +
        sec("02", "The product: KOM’BAR", "Organic kombucha cold-processed bar soap, made with naʻau’s kombucha and SCOBY.", product, sid="product") +
        sec("03", "Assets we plan to make", "What each side makes, and where it appears. Proposals are marked.", assets, sid="assets") +
        sec("04", "Website language", "How both sites talk about the collaboration, in Japanese and English.", language, sid="language") +
        sec("05", "How it ties to each naʻau direction", "Whichever direction naʻau chooses, the collaboration keeps its own peach. Here is how it sits beside each one.", ties, sid="ties") +
        sec("06", "Who does what", "Responsibilities and next steps.", roles, sid="roles") +
        '<footer class="site"><div class="wrap">naʻau × Ivycoast · concept for discussion. Text in ［brackets］ is to be confirmed. Ivycoast logos from the Ivycoast brand files; photography is shown as direction.</div></footer>')
C.page("collab.html", "naʻau × Ivycoast — KOM’BAR", "d-collab", body)
print("collab written")
