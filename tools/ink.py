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
        '<filter id="crayon" x="-5%" y="-10%" width="110%" height="120%">'
        '<feTurbulence type="fractalNoise" baseFrequency=".09" numOctaves="2" seed="3" result="w"/>'
        '<feDisplacementMap in="SourceGraphic" in2="w" scale="3" xChannelSelector="R" yChannelSelector="G" result="ink"/>'
        '<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="8" result="g"/>'
        '<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -9 0 0 0 6.1" result="holes"/>'
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

def yunomi(w, ink="currentColor"):
    shape = '<path d="M34 64 H166 Q166 132 146 160 Q140 168 128 168 H72 Q60 168 54 160 Q34 132 34 64Z"/><rect x="76" y="168" width="48" height="10" rx="2"/>'
    cuts = "".join(f'<path d="M{40 + i * 2} {84 + i * 14} Q100 {90 + i * 14} {160 - i * 2} {84 + i * 14}" stroke-width="3" fill="none"/>' for i in range(5))
    steam = f'<g filter="url(#brush)" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"><path d="M100 50 C92 40 108 32 100 20 C94 12 104 6 100 2"/></g>'
    return _svg("0 0 200 200", _carved(shape, cuts, ink) + steam, w, label="block-print tea cup")

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

MOTIFS = {"bottle": bottle, "jar": jar, "yunomi": yunomi, "leaf": leaf, "bubbles": bubbles, "sun": sun}

# ------------------------------------------------------------------ brush pictograms (how to enjoy)
def picto(kind, w, ink="currentColor"):
    paths = {
        "chill": '<path d="M70 40 V150 Q70 168 100 168 Q130 168 130 150 V40"/><path d="M60 40 H140"/><path d="M84 70 L96 82 L84 94 M116 70 L104 82 L116 94"/>',
        "still": '<path d="M70 168 H130 V96 Q130 80 114 72 V36 H86 V72 Q70 80 70 96 Z"/><path d="M40 120 Q50 110 40 100 M160 120 Q150 110 160 100"/>',
        "pour": '<path d="M60 100 H140 L132 170 H68 Z"/><path d="M100 30 Q104 60 100 90"/><path d="M72 128 H128"/>',
        "listen": '<circle cx="100" cy="100" r="58"/><path d="M76 108 Q100 126 124 108"/><circle cx="80" cy="88" r="2"/><circle cx="120" cy="88" r="2"/>',
    }[kind]
    return _svg("0 0 200 200", f'<g filter="url(#brush)" fill="none" stroke="{ink}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">{paths}</g>', w)

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
def ring_badge(w, top, centre_svg="", ink="currentColor", font="'IBM Plex Mono', monospace", size=13, rings=True):
    p = _id("rp")
    body = (f'<defs><path id="{p}" d="M100 100 m-74 0 a74 74 0 1 1 148 0 a74 74 0 1 1 -148 0"/></defs>'
            f'<g filter="url(#seal)">' + (f'<circle cx="100" cy="100" r="92" fill="none" stroke="{ink}" stroke-width="2.4"/><circle cx="100" cy="100" r="56" fill="none" stroke="{ink}" stroke-width="1.4"/>' if rings else '') +
            f'<text font-family="{font}" font-size="{size}" letter-spacing="{size * .32:.1f}" fill="{ink}"><textPath href="#{p}" startOffset="0" textLength="458" lengthAdjust="spacing">{top}</textPath></text></g>'
            f'<g transform="translate(60 60) scale(.4)">{centre_svg}</g>')
    return _svg("0 0 200 200", body, w)

def hanko(w, text="一本", ink="#9B3A25"):
    chars = "".join(f'<text x="50" y="{58 + i * 50}" font-family="\'Shippori Mincho B1\'" font-weight="700" font-size="44" text-anchor="middle" fill="#fff">{c}</text>' for i, c in enumerate(text))
    m = _id("hm")
    body = (f'<mask id="{m}" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="140"><rect width="100" height="140" fill="#fff"/>'
            f'<g fill="#000">{chars.replace("fill=\"#fff\"", "fill=\"#000\"")}</g><rect x="11" y="11" width="78" height="118" rx="34" fill="none" stroke="#000" stroke-width="2.2"/></mask>'
            f'<g filter="url(#seal)"><rect x="4" y="4" width="92" height="132" rx="42" fill="{ink}" mask="url(#{m})"/></g>')
    return _svg("0 0 100 140", body, w, label=f"seal: {text}")

def frame_stamp(w, title, side, centre_svg, ink="currentColor"):
    body = (f'<g filter="url(#seal)" fill="none" stroke="{ink}" stroke-width="3"><rect x="6" y="6" width="228" height="180"/></g>'
            f'<g filter="url(#brush)"><text x="20" y="40" font-family="\'IBM Plex Mono\', monospace" font-weight="500" font-size="22" letter-spacing="3" fill="{ink}">{title}</text>'
            f'<text x="212" y="58" font-family="\'IBM Plex Mono\', monospace" font-weight="500" font-size="18" letter-spacing="4" fill="{ink}" style="writing-mode:vertical-rl">{side}</text></g>'
            f'<g transform="translate(46 54) scale(.66)">{centre_svg}</g>')
    return _svg("0 0 240 192", body, w)

def pattern(motifs, ink, w="100%", h="100%", gap=150, seed=1):
    """A stamped all-over pattern for tissue or wrapping paper."""
    import random
    r = random.Random(seed)
    cells = ""
    for row in range(8):
        for col in range(8):
            fn = motifs[(row * 2 + col * 3 + seed) % len(motifs)]
            x = col * gap + (gap / 2 if row % 2 else 0) + r.uniform(-12, 12)
            y = row * gap * .82 + r.uniform(-10, 10)
            rot = r.uniform(-24, 24)
            cells += f'<g transform="translate({x:.0f} {y:.0f}) rotate({rot:.0f} 50 50) scale(.36)">{fn("200px", ink).replace("<svg ", "<svg width=\"200\" height=\"200\" ")}</g>'
    return f'<svg viewBox="0 0 {gap * 6} {gap * 5}" preserveAspectRatio="xMidYMid slice" style="width:{w}; height:{h}; display:block" aria-hidden="true">{cells}</svg>'

def pen_ellipse(w, ink="#B8352B"):
    """A quick loop drawn round something with a felt pen."""
    return _svg("0 0 300 100", f'<g filter="url(#brush)"><path d="M262 30 C230 6 70 4 26 30 C-4 50 22 86 120 90 C210 94 296 78 288 46 C282 24 214 14 168 16" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/></g>', w)

def perforated(w, ratio_h, inner, paper="#F2EFE8", tooth=14):
    """A postage stamp: perforated paper edge around an image."""
    W, H = 1000, 1000 * ratio_h
    r = tooth * .42
    nx, ny = int(W // tooth), int(H // tooth)
    sx, sy = W / nx, H / ny
    holes = "".join(f'<circle cx="{(i + .5) * sx:.1f}" cy="0" r="{r}"/><circle cx="{(i + .5) * sx:.1f}" cy="{H}" r="{r}"/>' for i in range(nx))
    holes += "".join(f'<circle cx="0" cy="{(j + .5) * sy:.1f}" r="{r}"/><circle cx="{W}" cy="{(j + .5) * sy:.1f}" r="{r}"/>' for j in range(ny))
    m = _id("pm")
    paper_svg = (f'<svg viewBox="0 0 {W} {H:.0f}" preserveAspectRatio="none" style="position:absolute; inset:0; width:100%; height:100%" aria-hidden="true">'
                 f'<mask id="{m}"><rect width="{W}" height="{H:.0f}" fill="#fff"/><g fill="#000">{holes}</g></mask>'
                 f'<rect width="{W}" height="{H:.0f}" fill="{paper}" mask="url(#{m})"/></svg>')
    return (f'<div style="position:relative; width:{w}; aspect-ratio:1/{ratio_h}; filter:drop-shadow(0 2px 3px rgba(0,0,0,.12))">{paper_svg}'
            f'<div style="position:absolute; inset:7%; overflow:hidden">{inner}</div></div>')
