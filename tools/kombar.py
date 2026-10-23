"""The KOM'BAR artwork, taken apart into its elements, plus the KOM'BAR wordmark (KOMbucha + BAR soap).

Source: assets/collab/source/kombar-artwork-layers.svg (59 shapes) and kombar-wordmark.svg.
Each element becomes an inline <symbol>; use el("sun", "120px", "#144948") anywhere on the page.
Running this file also writes one SVG per element to assets/collab/elements/ for the design team.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "assets", "collab", "source")
_art = open(os.path.join(SRC, "kombar-artwork-layers.svg")).read()
PATHS = re.findall(r'<path class="cls-1" d="([^"]+)"/>', _art)
BBOX = json.load(open(os.path.join(HERE, "kombar-bbox.json")))
_wm = open(os.path.join(SRC, "kombar-wordmark.svg")).read()
WM_SHAPES = re.findall(r'<(?:path|polygon) class="cls-1" (d|points)="([^"]+)"/>', _wm)

# name: (shape indices, Japanese, English, what it stands for)
ELEMENTS = {
    "mother":  ([0, 8, 9, 13] + list(range(48, 59)), "母", "The mother", "The woman holding the SCOBY, which brewers call the mother. The heart of the artwork."),
    "sun":     ([10, 20, 21, 23, 24, 25, 26, 27, 28, 30, 37], "日", "Sun", "Time. Kombucha ferments for weeks; the soap cures for two months."),
    "bird":    ([2], "鳥", "Bird", "The coast, and Ivycoast’s own bird."),
    "tea":     ([44, 7, 15, 17, 18], "茶", "Tea leaves", "Where kombucha begins: the tea plant, from the branch at the top to the sprig and leaves at its foot."),
    "gut":     ([4, 6], "腸", "The gut", "Healthy intestines: naʻau is Hawaiian for the gut, so this is the name, drawn. A shape only; on soap it is never captioned with gut-health words."),
    "seaweed": ([1], "藻", "Seaweed", "The sea, and the Australian coast."),
    "scoby":   ([3], "菌", "SCOBY", "The culture of bacteria and yeast that brews the kombucha, and is milled into the soap."),
    "botanical": ([5, 14, 19, 22, 40, 41, 42, 43], "花", "Flowering branch", "Berries and flower on one branch: the botanicals Ivycoast works with."),
    "lemon":   ([45, 47, 29, 31, 39], "柑", "Lemon", "A kombucha flavour."),
    "ginger":  ([46], "生姜", "Ginger", "A kombucha flavour."),
}
ORDER = list(ELEMENTS)
# parts drawn apart in the artwork that belong to one element: (element, shape indices, dx, dy)
MOVES = {"tea": ([7, 15, 17, 18], 300, -520)}

def _shift(name, i):
    m = MOVES.get(name)
    return (m[1], m[2]) if m and i in m[0] else (0, 0)

def _box(idx, name=None):
    sh = {i: _shift(name, i) for i in idx}
    xs = [BBOX[i][0] + sh[i][0] for i in idx]; ys = [BBOX[i][1] + sh[i][1] for i in idx]
    x2 = [BBOX[i][0] + BBOX[i][2] + sh[i][0] for i in idx]; y2 = [BBOX[i][1] + BBOX[i][3] + sh[i][1] for i in idx]
    x, y, X, Y = min(xs), min(ys), max(x2), max(y2)
    return x - 2, y - 2, X - x + 4, Y - y + 4

def _symbol(name):
    idx = ELEMENTS[name][0]
    x, y, w, h = _box(idx, name)
    return f'<symbol id="k-{name}" viewBox="{x} {y} {w} {h}">' + "".join(_path(name, i) for i in idx) + '</symbol>'

def _path(name, i):
    dx, dy = _shift(name, i)
    return f'<path d="{PATHS[i]}"' + (f' transform="translate({dx} {dy})"' if dx or dy else "") + '/>'

def ratio(name):
    _, _, w, h = _box(ELEMENTS[name][0], name)
    return w / h

_wm_body = "".join(f'<path d="{v}"/>' if k == "d" else f'<polygon points="{v}"/>' for k, v in WM_SHAPES)
DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
        + "".join(_symbol(n) for n in ORDER)
        + '<symbol id="k-artwork" viewBox="0 0 1254 1254">' + "".join(f'<path d="{d}"/>' for d in PATHS) + '</symbol>'
        + f'<symbol id="k-wm-v" viewBox="0 0 72.71 463.81">{_wm_body}</symbol>'
        + f'<symbol id="k-wm-h" viewBox="0 0 463.81 72.71"><g transform="translate(0 72.71) rotate(-90)">{_wm_body}</g></symbol>'
        + '</defs></svg>')

def el(name, w, color="currentColor", style="", label=""):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg style="width:{w}; aspect-ratio:{ratio(name):.4f}; display:block; fill:{color}; overflow:visible; {style}" {aria}><use href="#k-{name}"/></svg>'

def artwork(w, color="currentColor", style=""):
    return f'<svg viewBox="0 0 1254 1254" style="width:{w}; display:block; fill:{color}; {style}" role="img" aria-label="KOM’BAR artwork"><use href="#k-artwork"/></svg>'

def wordmark(w, color="currentColor", orient="h", style=""):
    vb = "0 0 463.81 72.71" if orient == "h" else "0 0 72.71 463.81"
    return f'<svg viewBox="{vb}" style="width:{w}; display:block; fill:{color}; {style}" role="img" aria-label="KOM’BAR"><use href="#k-wm-{orient}"/></svg>'

if __name__ == "__main__":
    out = os.path.join(HERE, "..", "assets", "collab", "elements")
    os.makedirs(out, exist_ok=True)
    for i, n in enumerate(ORDER, 1):
        idx = ELEMENTS[n][0]; x, y, w, h = _box(idx, n)
        open(os.path.join(out, f"{i:02d}-{n}.svg"), "w").write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}"><g fill="#1e1e1e">' + "".join(_path(n, j) for j in idx) + '</g></svg>\n')
    print("elements written:", len(ORDER))
