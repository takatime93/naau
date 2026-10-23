"""index.html: the overview — what we heard, research, colour, the three directions, decisions."""
import sys
sys.path.insert(0, sys.argv[2])
import common as C
from common import D, L, still, sec, chips
C.SITE = sys.argv[1]

PALETTES = [
 ("S", "白と墨", "White & Ink", "Current identity", "Plain white and ink, as naʻau looks today. The glass and the photographs bring the colour.",
  [("White", "#FFFFFF", "Ground", 3), ("Ink", "#1E1E1E", "Text · 16.9:1", 2), ("Grey", "#6B6B6B", "Small text · 5.3:1", 1), ("Mist", "#F1F1EF", "Photo backdrops", 2), ("Amber glass", "#8E4E1F", "From the bottle", 1.2)]),
 ("A", "墨と生成り", "Sumi & Kinari", "Concept A", "Near-monochrome. Ink on washi; the amber bottle is the only warmth.",
  [("Kinari", "#EFEBE2", "Ground", 3), ("Sumi", "#2B2926", "Text · 12.2:1", 2), ("Keshizumi", "#524E4D", "Rules · 6.9:1", 1), ("Rikyū-shiracha", "#B3ADA0", "Secondary", 1), ("Usuzumi", "#A3A3A2", "Tint", 1)]),
 ("D", "胡粉と黄土", "Gofun & Ōdo", "Concept B", "Lighter and airier. Morning light through shōji; ochre rhymes with the glass.",
  [("Gofun", "#FAF7F1", "Ground", 3), ("Ink", "#3A3631", "Text · 11.2:1", 2), ("Ōdo", "#C39143", "Fills only", 1.5), ("Ōdo text", "#8A6A3A", "Accent text · 4.7:1", 1), ("Neri", "#EDE4CD", "Tint", 1.5)]),
 ("B", "柿渋と土", "Kakishibu & Earth", "Alternative, warmer", "Persimmon-tanned paper and a clay storehouse. Swap in for any direction.",
  [("Raw linen", "#E9E0CF", "Ground", 3), ("Kenpō brown", "#3B2B22", "Text · 10.3:1", 2), ("Kakishibu", "#9F563A", "Accent · large text", 1.2), ("Namakabe", "#94846A", "Decoration", 1), ("Kurumi", "#A86F4C", "Support", 1)]),
 ("C", "弁柄", "Bengara", "Alternative", "A red-oxide seal on handmade paper. A deeper accent for any direction.",
  [("Paper", "#F2EDE3", "Ground", 3), ("Warm ink", "#2E2624", "Text · 12.7:1", 2), ("Bengara", "#8F2E14", "Accent · 7.0:1", 1.2), ("Kurotsurubami", "#544A47", "Secondary · 7.4:1", 1), ("Aku-iro", "#9E9478", "Support", 1)]),
]

RESEARCH = [
 ("Packaging", ["330 ml amber glass blocks UV and protects the live culture.",
                "Matte, water-resistant label stock; condensation ruins uncoated paper.",
                "The back label carries the 一括表示 at 8 pt minimum, plus 要冷蔵, ‘don’t shake’ and a batch box.",
                "Kombucha under 1% alcohol is 清涼飲料水; test each batch, as it can ferment past 1% in the bottle."],
  [("Mountain Culture", "https://www.bevnet.com/news/2019/mountain-culture-kombucha-launches-new-glass-bottle-design-from-ardagh-group"),
   ("Health-Ade", "https://thedieline.com/before-after-health-ade-kombucha/"), ("MHLW", "https://www.mhlw.go.jp/content/11130500/000398573.pdf")]),
 ("Print", ["A5 is the standard hand-out; shop cards are 91 × 55 mm, with 3 mm bleed.",
            "Workshop details in the expected order: 日時, 場所, 対象, 定員, 内容, 参加費（税込）, 申込方法.",
            "QR codes for LINE and Instagram on the back."],
  [("A5 sizes", "https://imitsu.jp/matome/printing/postcard-size-a5")]),
 ("Social", ["Instagram’s grid shows 3:4 since 2025: design at 1080 × 1440, key content inside the 4:5 crop.",
             "Stories and Reels at 9:16.",
             "Batch posts, process, the maker’s hands, workshop carousels with details on the last slide; LINE for restock alerts."],
  [("Post sizes", "https://www.inro.social/blog/instagram-post-size")]),
 ("Website and shop", ["Prices shown tax-inclusive (総額表示, since 2021).",
                       "クール便 cost, dispatch days and a delivery date next to the cart button: 64% of shoppers look for shipping cost on the product page.",
                       "Footer: 特定商取引法に基づく表記, 配送・返品, プライバシー. BASE supports クール便 and PayPay."],
  [("Baymard", "https://baymard.com/blog/show-shipping-costs-on-product-pages"), ("総額表示", "https://www.gov-online.go.jp/article/202104/entry-10238.html")]),
 ("Colour and trust", ["Undyed, low-saturation colours read as more natural and raise willingness to pay for healthy food.",
                       "Matte packs read as more natural than glossy ones.",
                       "Saturated blue reads ‘competent’ and corporate; warm off-white and warm ink read hand-made."],
  [("Marozzo et al. 2020", "https://openaccess.city.ac.uk/id/eprint/23205/"), ("Matte matters", "https://research.wu.ac.at/de/publications/matte-matters-when-matte-packaging-increases-perceptions-of-food--7/")]),
 ("Words", ["No health-effect claims on a normal food: avoid 便秘解消, 腸内環境改善, 免疫力UP.",
            "kimy’s nursing background belongs in her bio, never beside product benefits, and never as ‘監修’.",
            "Check with 名古屋市保健所 before any label says 非加熱 (unheated)."],
  [("Saitama guidance", "https://www.pref.saitama.lg.jp/documents/19134/620443.pdf")]),
]

COVERS = [
 ("current", "#FFFFFF", "#1E1E1E", L(D["current"], "1e1e1e", "46%"), "Current identity", "kimy’s script, as it is", "kimy’s script as it is: white, ink, centred, photo-led, round sticker labels."),
 ("lenora", "#2B2926", "#EFEBE2", L(D["lenora"], "efebe2", "56%"), "Concept A · Lenora", "Bottled for one", "A made-to-order atelier: sumi, wide margins, batch numerals, labels made out to one person."),
 ("ogg", "#FAF7F1", "#3A3631", L(D["ogg"], "3a3631", "56%"), "Concept B · Ogg", "The pause", "Airy and hand-made: vertical Japanese, kimy’s handwritten notes, band labels and string tags."),
]

hero = ('<header class="wrap ov-hero">'
        '<p class="eyebrow">Brand concepts for naʻau kombucha · Nagoya · 2026</p>'
        '<h1>Three ways naʻau could look</h1>'
        '<p class="ov-sub">One keeps the brand naʻau has today; two are new. Each is shown on packaging, print, social and a working shop.</p>'
        '</header>')

heard = ('<div class="grid g3">' + "".join(
    f'<div class="heard"><span class="heard-n">{n}</span><h3>{t}</h3><p>{b}</p></div>' for n, t, b in [
        ("i", "The name", "naʻau is Hawaiian for the gut, the heart and the inner voice. kimy chose it in a second, after 直感kombucha, instinct kombucha and gut feeling kombucha all felt wrong."),
        ("ii", "The maker", "kimy is a nurse and gut-health advisor who brews kombucha in Nagoya and teaches it in workshops. Her voice is warm, direct and a little playful."),
        ("iii", "The feeling", "Grounded, trustworthy and hand-made; quiet rather than corporate. Kombucha is not everything, but it can be where you begin to listen to your body.")]) + '</div>')

def src(srcs):
    return " · ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in srcs)

research = '<div class="rows">' + "".join(
    f'<div class="rrow"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>'
    f'<p class="src">{src(srcs)}</p></div>' for t, items, srcs in RESEARCH) + '</div>'

palettes = '<div class="rows">' + "".join(
    f'<div class="prow"><div class="prow-h"><p class="eyebrow">{letter} · {used}</p><h3><span class="jp">{jp}</span> {en}</h3><p class="muted">{mood}</p></div>{chips(cs)}</div>'
    for letter, jp, en, used, mood, cs in PALETTES) + '</div>'

dirs = ('<div class="ov-dirs">' + "".join(
    f'<a href="{k}.html" class="dcard"><div class="dcard-img" style="background:{bg}; color:{fg}">{L(D[k], fg.lstrip("#").lower(), "48%")}</div>'
    f'<h3>{lab}</h3><p class="muted">{s}</p></a>'
    for k, bg, fg, logo, lab, e, s in COVERS) + '</div>'
    '<a href="collab.html" class="ov-collab"><span>Collaboration</span><b>naʻau × Ivycoast — KOM’BAR</b><span class="link">View →</span></a>')

decisions = '<ol class="decide">' + "".join(f'<li><span>{i:02d}</span><p>{t}</p></li>' for i, t in enumerate([
    "Choose a direction, and a palette for it.",
    "If Concept A or B: license the font for logo use (Lenora needs the Logo and Merchandise add-ons; Ogg’s desktop licence covers logos) and confirm trademark registration in Japan in writing with the foundry.",
    "Confirm with 名古屋市保健所 how the kombucha may be described (heated or not) and the 一括表示 wording.",
    "Send scans of kimy’s handwriting and plan a photography day: hands, tea, the pour, the brewing table.",
    "Choose the shop platform (BASE handles クール便 and PayPay) and set up LINE."], 1)) + '</ol>'

appendix = ('<details class="appx"><summary>What we heard</summary>' + heard + '</details>'
            '<details class="appx"><summary>What the research says</summary>' + research + '</details>'
            '<details class="appx"><summary>Colour options: five palettes</summary>' + palettes + '</details>')

body = (C.nav("index") + hero +
        f'<section class="wrap ov-sec">{dirs}</section>' +
        sec("01", "Decisions for naʻau", "", decisions) +
        sec("02", "Background", "The brief, the research and the palettes behind the directions.", appendix) +
        '<footer class="site"><div class="wrap">Concepts by Ivycoast for naʻau kombucha. Text in ［brackets］ is for naʻau to fill in. Lenora and Ogg wordmarks are shown from unlicensed settings for discussion only.</div></footer>')
C.page("index.html", "naʻau kombucha — brand concepts", "", body, extra_head='<meta name="description" content="Brand concepts for naʻau kombucha, Nagoya.">')
print("index written")
