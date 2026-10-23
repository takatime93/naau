"""Concept A (Lenora), 手当て: a set of bold linocut prints.

Each print is one filled block with lines carved out of it (the paper shows through), run through
ink.py's `lino` filter for a wobbled, speckled edge. Shapes are blocky and naive on purpose, like a
first cut in linoleum. viewBox 0 0 200 200 throughout.
"""
from ink import _svg, _carved

def _caps(pts, w):
    """Rounded strokes as filled capsules (a carved block has no outlines)."""
    return "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke-width="{w}" stroke-linecap="round" fill="none"/>' for x1, y1, x2, y2 in pts)

def _hatch(x0, x1, y0, y1, step, w=2.4, slope=0):
    return "".join(f'<path d="M{x0} {y} L{x1} {y + slope}" stroke-width="{w}" fill="none"/>' for y in range(y0, y1, step))

def hand(w, ink="currentColor"):
    """The emblem: an open hand, palm up, holding one drop. 手当て, care by hand."""
    fingers = [(72, 112, 66, 46), (92, 104, 90, 30), (112, 104, 114, 34), (130, 114, 138, 56)]
    shape = (f'<g stroke="{ink}">' + _caps(fingers, 20) + _caps([(66, 138, 34, 104)], 22) + '</g>'
             '<path d="M58 112 Q100 100 142 116 L140 150 Q136 174 122 182 L124 196 L78 190 L80 182 Q62 172 60 150Z"/>')
    cuts = ('<path d="M100 122 C100 122 86 140 86 149 A14 14 0 0 0 114 149 C114 140 100 122 100 122Z" stroke="none"/>'
            + _caps([(64, 62, 70, 61), (88, 52, 94, 51), (110, 56, 116, 56), (132, 74, 138, 73), (42, 112, 48, 110)], 2.6)
            + '<path d="M70 126 Q76 160 94 172" stroke-width="2.6" fill="none"/><path d="M132 130 Q128 152 116 166" stroke-width="2.2" fill="none"/>')
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: an open hand holding a drop")

def bowl(w, ink="currentColor"):
    """A tea bowl with three lines of steam."""
    shape = ('<path d="M34 100 H166 Q164 156 122 168 H78 Q36 156 34 100Z"/><rect x="80" y="166" width="40" height="14" rx="3"/>'
             f'<g stroke="{ink}" stroke-width="9" stroke-linecap="round" fill="none">'
             '<path d="M78 84 C66 70 90 62 78 46 C70 36 80 26 86 22"/><path d="M104 86 C94 70 118 62 106 44 C100 34 108 24 112 20"/><path d="M128 84 C120 72 140 64 132 50"/></g>')
    cuts = ('<path d="M40 110 H160" stroke-width="3"/>'
            + "".join(f'<path d="M{x} 112 Q{x + 3} 128 {x - 2} {136 + (x % 3) * 6}" stroke-width="3.4" fill="none" stroke-linecap="round"/>' for x in (56, 74, 96, 118, 140))
            + '<path d="M46 132 Q100 150 154 132" stroke-width="2.2" fill="none"/>')
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: a steaming tea bowl")

def camellia(w, ink="currentColor"):
    """The tea flower, five round petals and two leaves."""
    import math
    petals = "".join(f'<circle cx="{100 + 34 * math.cos(math.radians(a)):.1f}" cy="{86 + 34 * math.sin(math.radians(a)):.1f}" r="30"/>' for a in range(-90, 270, 72))
    shape = (petals + '<circle cx="100" cy="86" r="30"/>'
             '<path d="M100 150 Q66 132 34 156 Q62 186 100 150Z"/><path d="M106 148 Q136 128 170 150 Q142 182 106 148Z"/>')
    cuts = ('<circle cx="100" cy="86" r="16" stroke="none"/>'
            + "".join(f'<path d="M100 86 L{100 + 30 * math.cos(math.radians(a)):.1f} {86 + 30 * math.sin(math.radians(a)):.1f}" stroke-width="2.6" fill="none"/>' for a in range(-54, 306, 72))
            + '<path d="M96 151 Q70 150 46 158" stroke-width="2.6" fill="none"/><path d="M110 149 Q136 146 158 152" stroke-width="2.6" fill="none"/>')
    stamens = "".join(f'<circle cx="{100 + 9 * math.cos(math.radians(a)):.1f}" cy="{86 + 9 * math.sin(math.radians(a)):.1f}" r="3.4" fill="{ink}"/>' for a in range(0, 360, 45))
    return _svg("0 0 200 200", _carved(shape, cuts, ink) + f'<g filter="url(#lino)">{stamens}</g>', w, label="linocut: a camellia, the tea flower")

def mortar(w, ink="currentColor"):
    """A suribachi and pestle: the grinding bowl of the Japanese kitchen and the herbalist."""
    shape = (f'<path d="M98 112 L150 24" stroke="{ink}" stroke-width="16" stroke-linecap="round"/>'
             '<path d="M26 104 H174 Q172 160 128 176 H72 Q28 160 26 104Z"/><rect x="74" y="174" width="52" height="12" rx="3"/>')
    cuts = ('<path d="M32 112 H168" stroke-width="3"/>'
            + "".join(f'<path d="M{x} 118 L{x + 14} 160" stroke-width="2.6" fill="none"/>' for x in range(44, 150, 12))
            + '<path d="M138 40 L146 28" stroke-width="2.4"/>')
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: a grinding bowl and pestle")

def moon(w, ink="currentColor"):
    """A crescent with carved hatching: the days a batch takes."""
    shape = '<circle cx="100" cy="100" r="76"/>'
    cuts = '<circle cx="132" cy="84" r="66" stroke="none"/>' + _hatch(20, 120, 40, 180, 9, 2.4, 10)
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: a crescent moon")

def leaf(w, ink="currentColor"):
    """Three tea leaves on one stem, veins carved."""
    def lf(x, y, ang, ln, wd):
        return (f'<path transform="translate({x} {y}) rotate({ang})" d="M0 0 C{wd} {-ln * .3} {wd * .8} {-ln * .75} 0 {-ln} C{-wd * .8} {-ln * .75} {-wd} {-ln * .3} 0 0Z"/>',
                f'<g transform="translate({x} {y}) rotate({ang})"><path d="M0 -4 L0 {-ln + 10}" stroke-width="3" fill="none"/>'
                + "".join(f'<path d="M0 {-ln * t:.0f} L{s_ * wd * .55:.0f} {-ln * t - 12:.0f}" stroke-width="2.2" fill="none"/>' for t in (.25, .45, .65) for s_ in (1, -1)) + '</g>')
    parts = [lf(100, 150, -4, 120, 30), lf(98, 156, -52, 92, 25), lf(102, 160, 48, 86, 24)]
    shape = f'<path d="M100 150 L94 194" stroke="{ink}" stroke-width="8" stroke-linecap="round"/>' + "".join(p[0] for p in parts)
    cuts = "".join(p[1] for p in parts)
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: three tea leaves")

def drop(w, ink="currentColor"):
    """The ʻokina of the Lenora wordmark as a solid printed drop."""
    shape = '<path d="M100 14 C100 14 40 104 40 140 A60 60 0 0 0 160 140 C160 104 100 14 100 14Z"/>'
    cuts = '<path d="M70 132 Q70 108 86 92" stroke-width="5" fill="none" stroke-linecap="round"/>'
    return _svg("0 0 200 200", _carved(shape, cuts, ink), w, label="linocut: a drop")

PRINTS = {"hand": hand, "bowl": bowl, "camellia": camellia, "mortar": mortar, "moon": moon, "leaf": leaf, "drop": drop}

def grain(id_, ink, opacity=.18):
    """Woodblock grain (板目) as a tiled background image: the browser draws it once and reuses it."""
    from urllib.parse import quote
    h = ink.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='900' height='900'><filter id='w' x='0' y='0' width='100%' height='100%'>"
           f"<feTurbulence type='fractalNoise' baseFrequency='.0016 .045' numOctaves='4' seed='7' stitchTiles='stitch'/>"
           f"<feColorMatrix values='0 0 0 0 {r:.3f}  0 0 0 0 {g:.3f}  0 0 0 0 {b:.3f}  -3 0 0 0 1.75'/></filter>"
           f"<rect width='100%' height='100%' filter='url(#w)'/></svg>")
    return (f'<div class="fill" style="background-image:url(data:image/svg+xml,{quote(svg, safe="")}); background-size:900px 900px; '
            f'opacity:{opacity}; pointer-events:none" aria-hidden="true"></div>')
