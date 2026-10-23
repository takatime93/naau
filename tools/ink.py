"""Hand-made marks: block-print motifs, a fine-line tea branch, and stamps.

Block prints are plain shapes run through the `lino` filter (wobbled edges, ink speckle);
carved lines are cut out with a mask so the paper shows through on any ground.
"""
import math

DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
        '<filter id="lino" x="-8%" y="-8%" width="116%" height="116%" color-interpolation-filters="sRGB">'
        '<feTurbulence type="fractalNoise" baseFrequency=".03" numOctaves="3" seed="4" result="w"/>'
        '<feDisplacementMap in="SourceGraphic" in2="w" scale="5" xChannelSelector="R" yChannelSelector="G" result="ink"/>'
        '<feTurbulence type="fractalNoise" baseFrequency=".22" numOctaves="3" seed="9" result="g"/>'
        '<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -16 0 0 0 11.6" result="holes"/>'
        '<feComposite in="ink" in2="holes" operator="in"/></filter>'
        '<filter id="brush" x="-8%" y="-8%" width="116%" height="116%">'
        '<feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="2" seed="2" result="w"/>'
        '<feDisplacementMap in="SourceGraphic" in2="w" scale="1.6" xChannelSelector="R" yChannelSelector="G"/></filter>'
        '<filter id="seal" x="-8%" y="-8%" width="116%" height="116%">'
        '<feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="11" result="w"/>'
        '<feDisplacementMap in="SourceGraphic" in2="w" scale="2.2" xChannelSelector="R" yChannelSelector="G" result="ink"/>'
        '<feTurbulence type="fractalNoise" baseFrequency=".3" numOctaves="3" seed="5" result="g"/>'
        '<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -12 0 0 0 8.7" result="holes"/>'
        '<feComposite in="ink" in2="holes" operator="in"/></filter>'
        '</defs></svg>')

_n = [0]
def _id(p):
    _n[0] += 1
    return f"{p}{_n[0]}"

def _svg(vb, body, w, style="", label=""):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg viewBox="{vb}" style="width:{w}; display:block; overflow:visible; {style}" {aria}>{body}</svg>'

def _carved(shape, cuts, fill):
    """A filled shape with carved (transparent) cuts, then printed."""
    m = _id("m")
    return (f'<mask id="{m}" maskUnits="userSpaceOnUse" x="-50" y="-50" width="400" height="400"><rect x="-50" y="-50" width="400" height="400" fill="#fff"/>'
            f'<g fill="#000" stroke="#000" stroke-linecap="round" stroke-linejoin="round">{cuts}</g></mask>'
            f'<g filter="url(#lino)"><g mask="url(#{m})" fill="{fill}">{shape}</g></g>')

# ------------------------------------------------------------------ block-print motifs (viewBox 0 0 200 200)
def bottle(w, ink="currentColor"):
    shape = '<path d="M72 196 H128 Q136 196 136 188 V96 C136 78 118 70 114 56 V24 H86 V56 C82 70 64 78 64 96 V188 Q64 196 72 196Z"/><rect x="83" y="6" width="34" height="20" rx="2"/>'
    cuts = ('<path d="M74 102 C74 90 80 84 88 79" stroke-width="3.2" fill="none"/><path d="M75 110 V178" stroke-width="3.2" fill="none"/>'
            '<rect x="70" y="124" width="60" height="40" stroke="none"/><path d="M86 28 H114" stroke-width="2" fill="none"/>')
    label = f'<g filter="url(#lino)" fill="{ink}"><path d="M80 136 H120 M84 146 H116 M88 154 H112" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/></g>'
    return _svg("0 0 200 200", _carved(shape, cuts, ink) + label, w, label="block-print bottle")

def jar(w, ink="currentColor"):
    shape = ('<path d="M70 52 H130 V64 Q164 74 166 112 V176 Q166 196 146 196 H54 Q34 196 34 176 V112 Q36 74 70 64Z"/>'
             '<path d="M58 30 Q100 14 142 30 L140 50 Q100 42 60 50Z"/><path d="M62 44 Q52 58 58 70 M138 44 Q148 58 142 70" stroke="' + ink + '" stroke-width="7" fill="none" stroke-linecap="round"/>')
    cuts = ('<path d="M62 46 Q100 38 138 46" stroke-width="3" fill="none"/><path d="M40 112 H160" stroke-width="3"/><path d="M40 121 Q100 128 160 121" stroke-width="2.2" fill="none"/>'
            '<path d="M48 136 V180" stroke-width="3.6" stroke-linecap="round"/><path d="M72 76 Q56 84 50 98" stroke-width="3" fill="none"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="none"/>' for x, y, r in ((84, 160, 3.6), (108, 146, 2.4), (126, 174, 3), (98, 182, 2), (142, 140, 2.4), (70, 150, 1.8))))
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="block-print fermenting jar")

def leaf(w, ink="currentColor"):
    teeth = []
    for side in (1, -1):
        for i in range(9):
            t = .12 + i * .09
            x = 100 + side * 54 * math.sin(math.pi * t) * (1 - t * .25)
            y = 186 - t * 176
            teeth.append((t, x, y, side))
    left = sorted([p for p in teeth if p[3] == -1], key=lambda p: -p[0])
    right = sorted([p for p in teeth if p[3] == 1], key=lambda p: p[0])
    pts = [(100, 196)] + [(x, y) for _, x, y, _ in right] + [(100, 6)] + [(x, y) for _, x, y, _ in left]
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
    shape = f'<path d="{d}" stroke="{ink}" stroke-width="6" stroke-linejoin="round"/>'
    cuts = '<path d="M100 192 Q98 100 100 14" stroke-width="3.6" fill="none"/>' + "".join(
        f'<path d="M100 {176 - i * 20} Q{100 + s * 22} {166 - i * 20} {100 + s * 38} {150 - i * 20}" stroke-width="2.4" fill="none"/>' for i in range(7) for s in (1, -1))
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="block-print tea leaf")

def bubbles(w, ink="currentColor"):
    rings = ((70, 150, 26), (128, 112, 18), (96, 70, 12), (140, 44, 8), (62, 92, 7), (118, 164, 9))
    body = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{ink}" stroke-width="{max(3, r * .28):.1f}"/>' for x, y, r in rings)
    body += f'<circle cx="62" cy="142" r="5" fill="{ink}"/><circle cx="124" cy="106" r="3.4" fill="{ink}"/>'
    return _svg("0 0 200 200", f'<g filter="url(#lino)">{body}</g>', w, label="block-print bubbles")

def sun(w, ink="currentColor"):
    rays = "".join(f'<path d="M{100 + 52 * math.cos(a):.1f} {100 + 52 * math.sin(a):.1f} L{100 + 84 * math.cos(a + .05):.1f} {100 + 84 * math.sin(a + .05):.1f}" stroke="{ink}" stroke-width="{9 if i % 2 == 0 else 5}" stroke-linecap="round"/>'
                   for i, a in enumerate(math.radians(d) for d in range(0, 360, 30)))
    shape = f'<circle cx="100" cy="100" r="38"/>'
    cuts = '<circle cx="100" cy="100" r="24" stroke-width="3" fill="none"/><circle cx="100" cy="100" r="9" stroke-width="2.6" fill="none"/>'
    return _svg("0 0 200 200", _carved(shape, cuts, ink) + f'<g filter="url(#lino)">{rays}</g>', w, label="block-print sun")

MOTIFS = {"bottle": bottle, "jar": jar, "leaf": leaf, "bubbles": bubbles, "sun": sun}

# ------------------------------------------------------------------ fine-line tea branch (Concept A)
def tea_branch(w, ink="currentColor", sw=1.1):
    def leafpath(x, y, ang, L, W):
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a); nx, ny = -uy, ux
        tip = (x + ux * L, y + uy * L)
        c1 = (x + ux * L * .3 + nx * W, y + uy * L * .3 + ny * W); c2 = (x + ux * L * .8 + nx * W * .7, y + uy * L * .8 + ny * W * .7)
        c3 = (x + ux * L * .8 - nx * W * .7, y + uy * L * .8 - ny * W * .7); c4 = (x + ux * L * .3 - nx * W, y + uy * L * .3 - ny * W)
        out = (f'M{x:.1f} {y:.1f} C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {tip[0]:.1f} {tip[1]:.1f} '
               f'C{c3[0]:.1f} {c3[1]:.1f} {c4[0]:.1f} {c4[1]:.1f} {x:.1f} {y:.1f}')
        mid = f'M{x:.1f} {y:.1f} Q{x + ux * L * .5 + nx * W * .12:.1f} {y + uy * L * .5 + ny * W * .12:.1f} {tip[0]:.1f} {tip[1]:.1f}'
        veins = ""
        for t in (.25, .42, .58, .74):
            px, py = x + ux * L * t, y + uy * L * t
            for s in (1, -1):
                e = W * (1 - abs(t - .45) * 1.1) * .62
                veins += f' M{px:.1f} {py:.1f} Q{px + ux * L * .06 + s * nx * e * .6:.1f} {py + uy * L * .06 + s * ny * e * .6:.1f} {px + ux * L * .12 + s * nx * e:.1f} {py + uy * L * .12 + s * ny * e:.1f}'
        return f'<path d="{out}"/><path d="{mid}"/><path d="{veins}" stroke-width="{sw * .6}"/>'
    stem = '<path d="M100 222 C98 196 104 170 100 140 C96 110 106 84 100 52"/><path d="M100 150 C112 140 124 134 136 120"/><path d="M101 96 C90 88 80 80 72 66"/>'
    leaves = (leafpath(100, 200, 200, 58, 15) + leafpath(100, 172, -20, 62, 16) + leafpath(136, 120, -40, 46, 12) + leafpath(100, 128, 196, 50, 13)
              + leafpath(72, 66, 240, 38, 10) + leafpath(100, 52, -95, 34, 9))
    fx, fy = 134, 82
    def petal(a, r, wdt):
        a1, a2 = math.radians(a - wdt), math.radians(a + wdt)
        return (f'<path d="M{fx:.1f} {fy:.1f} C{fx + r * 1.25 * math.cos(a1):.1f} {fy + r * 1.25 * math.sin(a1):.1f} '
                f'{fx + r * 1.25 * math.cos(a2):.1f} {fy + r * 1.25 * math.sin(a2):.1f} {fx:.1f} {fy:.1f}"/>')
    petals = "".join(petal(a, 20, 40) for a in range(-90, 270, 72)) + "".join(petal(a, 12, 34) for a in range(-54, 306, 72))
    stamens = "".join(f'<path d="M{fx:.1f} {fy:.1f} L{fx + 7 * math.cos(math.radians(a)):.1f} {fy + 7 * math.sin(math.radians(a)):.1f}" stroke-width="{sw * .5}"/><circle cx="{fx + 7.8 * math.cos(math.radians(a)):.1f}" cy="{fy + 7.8 * math.sin(math.radians(a)):.1f}" r="1" fill="{ink}" stroke="none"/>'
                      for a in range(0, 360, 30))
    flower_stem = f'<path d="M108 118 C116 106 124 96 {fx} {fy + 4}"/>'
    bud = '<path d="M101 96 C92 82 92 74 98 70 C104 74 106 84 101 96Z"/><path d="M98 70 C96 64 97 60 99 58"/>'
    body = f'<g fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{stem}{leaves}{flower_stem}{petals}{stamens}{bud}</g>'
    return _svg("40 36 140 192", body, w, label="fine-line tea branch with a camellia flower")

# ------------------------------------------------------------------ stamps
def hanko(w, text="一本", ink="#9B3A25"):
    chars = "".join(f'<text x="50" y="{58 + i * 50}" font-family="\'Shippori Mincho B1\'" font-weight="700" font-size="44" text-anchor="middle" fill="#fff">{c}</text>' for i, c in enumerate(text))
    m = _id("hm")
    body = (f'<mask id="{m}" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="140"><rect width="100" height="140" fill="#fff"/>'
            f'<g fill="#000">{chars.replace("fill=\"#fff\"", "fill=\"#000\"")}</g><rect x="11" y="11" width="78" height="118" rx="34" fill="none" stroke="#000" stroke-width="2.2"/></mask>'
            f'<g filter="url(#seal)"><rect x="4" y="4" width="92" height="132" rx="42" fill="{ink}" mask="url(#{m})"/></g>')
    return _svg("0 0 100 140", body, w, label=f"seal: {text}")


def kakuin(w, cols=("名古屋", "手仕込"), ink="currentColor"):
    """A square seal: kanji in columns read right to left, cut in relief inside a worn border."""
    n = max(len(c) for c in cols)
    cell = 100 / n
    text = ""
    for ci, col in enumerate(cols):
        x = 100 - (ci + .5) * (100 / len(cols)) + 10
        for ri, ch in enumerate(col):
            text += f'<text x="{x:.1f}" y="{10 + (ri + .82) * cell:.1f}" font-family="\'Shippori Mincho B1\'" font-weight="700" font-size="{cell * .86:.1f}" text-anchor="middle" fill="{ink}">{ch}</text>'
    body = (f'<g filter="url(#seal)"><rect x="3" y="3" width="114" height="114" rx="9" fill="none" stroke="{ink}" stroke-width="6"/>'
            f'<path d="M60 8 V112" stroke="{ink}" stroke-width="1.6"/>{text}</g>')
    return _svg("0 0 120 120", body, w, label="seal: " + " ".join(cols))

# ------------------------------------------------------------------ Concept A: the drop, taken from the wordmark's ʻokina
DROP = "M10 1 C10 1 2 13 2 19.5 A8 8 0 0 0 18 19.5 C18 13 10 1 10 1Z"

def drop(w, ink="currentColor", fill=False, sw=.6):
    body = f'<path d="{DROP}" fill="{ink if fill else "none"}" stroke="{ink}" stroke-width="{sw}"/>'
    return _svg("0 0 20 29", body, w)

def drops(w, days=14, filled=14, ink="currentColor", label=True):
    """The fermentation count: one drop per day, filled up to the day it was bottled."""
    gap = 26
    body = "".join(f'<path transform="translate({i * gap} 0)" d="{DROP}" fill="{ink if i < filled else "none"}" stroke="{ink}" stroke-width=".9"/>' for i in range(days))
    if label:
        body += (f'<text x="0" y="46" font-family="\'IBM Plex Mono\', monospace" font-size="9" letter-spacing="2" fill="{ink}" opacity=".7">DAY 01</text>'
                 f'<text x="{(days - 1) * gap + 20}" y="46" text-anchor="end" font-family="\'IBM Plex Mono\', monospace" font-size="9" letter-spacing="2" fill="{ink}" opacity=".7">{days:02d} · BOTTLED</text>')
    return _svg(f"-1 0 {(days - 1) * gap + 22} {50 if label else 30}", body, w, label=f"{filled} of {days} days")

# ------------------------------------------------------------------ Concept B: what is in the jar, and the days it takes
def scoby(w, ink="currentColor"):
    shape = '<path d="M100 18 C150 16 186 52 184 100 C186 150 148 184 100 182 C50 186 14 148 16 100 C14 52 52 18 100 18Z"/>'
    rings = "".join(f'<path d="M100 {100 - r} C{100 + r * 1.1} {100 - r * .96} {100 + r * 1.02} {100 + r * 1.06} 100 {100 + r} C{100 - r * 1.08} {100 + r} {100 - r * .98} {100 - r * 1.04} 100 {100 - r}Z" stroke-width="{2.4 + (i % 2)}" fill="none"/>'
                    for i, r in enumerate((66, 50, 36, 22)))
    cuts = rings + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="none"/>' for x, y, r in ((72, 70, 3), (132, 84, 2.4), (120, 140, 3.2), (78, 128, 2), (100, 100, 5)))
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="block-print SCOBY, seen from above")

def moon(w, f, ink="currentColor"):
    """A waxing moon, f = 0 (new) to 1 (full), printed as a block."""
    rx = abs(1 - 2 * f) * 70
    lit = f'<path d="M100 30 A70 70 0 0 1 100 170 A{rx:.1f} 70 0 0 {0 if f < .5 else 1} 100 30Z"/>' if f > 0 else ""
    body = f'<g filter="url(#lino)"><circle cx="100" cy="100" r="70" fill="none" stroke="{ink}" stroke-width="5"/><g fill="{ink}">{lit}</g></g>'
    return _svg("0 0 200 200", body, w)

def calendar(w, ink="currentColor", days=14, cols=7, numbers=True):
    """Fourteen days as a waxing moon, new to full: the half-month a batch takes."""
    cells = ""
    for d in range(days):
        x, y = (d % cols) * 120, (d // cols) * 150
        cells += f'<g transform="translate({x + 10} {y + 10}) scale(.5)">{moon("200px", ((d % 14) + 1) / 14, ink).replace("<svg ", "<svg width=\"200\" height=\"200\" ")}</g>'
        if numbers:
            cells += f'<text x="{x + 60}" y="{y + 132}" text-anchor="middle" font-family="\'IBM Plex Mono\', monospace" font-size="13" letter-spacing="2" fill="{ink}">{d + 1:02d}</text>'
    return _svg(f"0 0 {cols * 120} {(days + cols - 1) // cols * 150 - (0 if numbers else 30)}", cells, w, label="fourteen days as moon phases")

# ------------------------------------------------------------------ the Japanese round date stamp (日付印)
def date_stamp(w, top="名古屋", date="26.10.22", bottom="CURE 01", ink="currentColor"):
    body = (f'<g filter="url(#seal)"><circle cx="60" cy="60" r="55" fill="none" stroke="{ink}" stroke-width="3"/>'
            f'<path d="M8 46 H112 M8 74 H112" stroke="{ink}" stroke-width="2"/>'
            f'<text x="60" y="36" text-anchor="middle" font-family="\'Shippori Mincho B1\'" font-weight="700" font-size="17" fill="{ink}">{top}</text>'
            f'<text x="60" y="67" text-anchor="middle" font-family="\'IBM Plex Mono\', monospace" font-weight="500" font-size="17" letter-spacing="1" fill="{ink}">{date}</text>'
            f'<text x="60" y="95" text-anchor="middle" font-family="Inter, sans-serif" font-weight="700" font-size="11" letter-spacing="2" fill="{ink}">{bottom}</text></g>')
    return _svg("0 0 120 120", body, w, label=f"date stamp {date}")

MOTIFS.update({"scoby": scoby})

def moon_paper(w, ink="currentColor", cols=12, rows=5):
    """Tissue paper: small waxing moons in a half-drop repeat, the phase advancing along each row."""
    cells = ""
    for r in range(rows):
        for c in range(cols):
            x = c * 100 + (50 if r % 2 else 0)
            f = ((c + r * 3) % 14 + 1) / 14
            cells += f'<g transform="translate({x} {r * 90}) scale(.28)">{moon("200px", f, ink).replace("<svg ", '<svg width="200" height="200" ')}</g>'
    return _svg(f"-20 -20 {cols * 100 + 40} {rows * 90 + 30}", cells, w, label="tissue printed with small moons")
