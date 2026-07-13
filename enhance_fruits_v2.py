"""
enhance_fruits_v2.py
====================
Comprehensive enhancement of all 127 50x50 fruit sprites for a kids'
pixel-coloring game.

Goals:
  1. Replace/improve 27 bland/sparse images (<=4 colors or <500 opaque pixels)
  2. Quantize every image to <= 10 colors (no dithering, no noise, no outlines)
  3. Clean, solid color regions ideal for children's coloring

Fruits needing replacement/improvement:
  salak, tamarind, bergamot, bilberry, breadfruit, cherimoya, cherry,
  custard_apple, elderberry, grape, langsat, monstera_deliciosa, physalis,
  pineapple, rambutan, soursop, starfruit, barberry, black_currant,
  cloudberry, mulberry, red_currant, banana, blackberry, boysenberry,
  marionberry, raspberry
"""

import os
import glob
import math
from PIL import Image, ImageDraw
import numpy as np

OUTPUT_DIR = "images/fruits"

# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------
T     = (0,   0,   0,   0)
BK    = (15,  15,  15,  255)
WH    = (255, 255, 255, 255)
LGY   = (200, 200, 200, 255)
MGY   = (160, 160, 160, 255)
DGY   = (100, 100, 100, 255)

RED   = (210, 40,  40,  255)
DRED  = (140, 25,  25,  255)
LRED  = (240, 100, 100, 255)
ORNG  = (240, 140, 30,  255)
DORNG = (180, 90,  10,  255)
LORNG = (255, 185, 80,  255)
YELL  = (245, 215, 40,  255)
LYELL = (255, 245, 140, 255)
DYELL = (180, 155, 20,  255)
GRN   = (50,  160, 50,  255)
DGRN  = (30,  100, 30,  255)
LGRN  = (130, 210, 130, 255)
BRN   = (120, 75,  30,  255)
DBRN  = (70,  45,  15,  255)
LBRN  = (170, 125, 75,  255)
PURP  = (110, 40,  130, 255)
DPURP = (60,  20,  75,  255)
LPURP = (180, 110, 210, 255)
PINK  = (240, 140, 160, 255)
DPINK = (200, 80,  110, 255)
LPINK = (255, 200, 210, 255)
CRIM  = (180, 30,  60,  255)
BEIGE = (230, 200, 160, 255)
CREAM = (255, 240, 210, 255)
TEAL  = (40,  170, 170, 255)
NAVY  = (30,  40,  100, 255)


def save_sprite(name, draw_fn):
    """Draw a 50x50 sprite, quantize to <=10 colors (no outline), save."""
    img = Image.new("RGBA", (50, 50), T)
    d = ImageDraw.Draw(img)
    draw_fn(d)
    img = _quantize_no_outline(img)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)


def _quantize_no_outline(img: Image.Image) -> Image.Image:
    """Quantize to 9 opaque colors (no dither, NO outline). Preserves alpha."""
    arr = np.array(img.convert("RGBA"))
    alpha = arr[:, :, 3]
    new_alpha = alpha.copy()

    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((arr[:, :, :3], new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    fa = np.array(final)
    fa[:, :, 3] = new_alpha
    return Image.fromarray(fa, "RGBA")


# ===========================================================================
# Hand-crafted fruit sprites
# ===========================================================================

def draw_salak(d):
    """Salak (snake fruit): brown scaly oval, pointed top, white flesh peek."""
    # body (egg-shaped)
    d.ellipse([12, 10, 38, 44], fill=BRN)
    d.ellipse([14, 12, 36, 42], fill=LBRN)
    # scaly texture (diagonal lines)
    for y in range(14, 42, 3):
        d.line([14, y, 36, y], fill=BRN, width=1)
    for x in range(16, 36, 4):
        d.line([x, 12, x+6, 42], fill=BRN, width=1)
    # pointed tip at top
    d.polygon([(22, 10), (28, 10), (25, 4)], fill=DBRN)
    # slight opening showing white/cream flesh
    d.polygon([(20, 38), (30, 38), (25, 44)], fill=CREAM)
    d.polygon([(22, 40), (28, 40), (25, 43)], fill=BEIGE)

def draw_tamarind(d):
    """Tamarind: brown curved pod with bumps, green stem."""
    # curved pod shape
    d.rounded_rectangle([8, 18, 44, 34], radius=8, fill=LBRN)
    d.rounded_rectangle([10, 20, 42, 32], radius=6, fill=BRN)
    # bumps (seeds visible through shell)
    for x in [14, 22, 30, 38]:
        d.ellipse([x-3, 22, x+3, 30], fill=LBRN)
    # cracked open area showing dark flesh
    d.ellipse([16, 24, 24, 28], fill=DBRN)
    # stem
    d.line([8, 26, 2, 22], fill=DGRN, width=2)
    d.line([44, 26, 48, 22], fill=DGRN, width=2)

def draw_bergamot(d):
    """Bergamot: green-yellow bumpy citrus, small leaf."""
    d.ellipse([10, 12, 40, 44], fill=DYELL)
    d.ellipse([12, 14, 38, 42], fill=YELL)
    # bumpy citrus texture
    for x, y in [(16, 18), (28, 16), (34, 24), (16, 32), (30, 34), (22, 26)]:
        d.ellipse([x, y, x+4, y+4], fill=LYELL)
    # slight green tinge at top
    d.ellipse([18, 12, 32, 22], fill=LGRN)
    # navel/blossom end
    d.ellipse([22, 38, 28, 42], fill=DYELL)
    # stem + leaf
    d.line([25, 12, 25, 6], fill=DGRN, width=2)
    d.polygon([(25, 6), (32, 4), (28, 8)], fill=GRN)

def draw_bilberry(d):
    """Bilberry: dark blue-purple berry, tiny crown, small cluster."""
    # main berry
    d.ellipse([14, 14, 36, 38], fill=DPURP)
    d.ellipse([16, 16, 34, 36], fill=PURP)
    # highlight
    d.ellipse([18, 18, 24, 24], fill=LPURP)
    # crown (calyx)
    d.polygon([(20, 14), (22, 10), (24, 14)], fill=DGRN)
    d.polygon([(26, 14), (28, 10), (30, 14)], fill=DGRN)
    # second smaller berry behind
    d.ellipse([30, 28, 44, 42], fill=DPURP)
    d.ellipse([32, 30, 42, 40], fill=PURP)
    d.ellipse([34, 32, 38, 36], fill=LPURP)
    # stem
    d.line([25, 10, 25, 4], fill=DGRN, width=1)

def draw_breadfruit(d):
    """Breadfruit: large green bumpy round fruit, thick stem."""
    d.ellipse([8, 10, 42, 46], fill=GRN)
    d.ellipse([10, 12, 40, 44], fill=LGRN)
    # hexagonal scale texture
    for y in range(14, 42, 5):
        for x in range(12, 38, 5):
            d.polygon([(x+2, y), (x+4, y+2), (x+4, y+4), (x+2, y+5), (x, y+4), (x, y+2)], fill=GRN)
    # yellowish patches (ripening)
    d.ellipse([18, 20, 26, 28], fill=YELL)
    d.ellipse([28, 30, 36, 38], fill=YELL)
    # thick stem
    d.line([25, 10, 25, 2], fill=DGRN, width=3)

def draw_cherimoya(d):
    """Cherimoya: heart-shaped green with scale pattern, stem."""
    # heart shape (rounded bottom, indented top)
    d.ellipse([10, 14, 40, 46], fill=LGRN)
    d.ellipse([8, 16, 26, 42], fill=GRN)
    d.ellipse([24, 16, 42, 42], fill=GRN)
    # scale/thumb-print pattern
    for y in range(18, 40, 5):
        for x in range(12, 38, 6):
            d.arc([x, y, x+5, y+5], start=0, end=180, fill=DGRN, width=1)
    # lighter belly
    d.ellipse([16, 28, 34, 42], fill=LGRN)
    # stem at top
    d.line([25, 14, 25, 6], fill=BRN, width=2)
    d.polygon([(25, 6), (30, 4), (28, 8)], fill=GRN)

def draw_cherry(d):
    """Cherry: pair of red cherries with joined stems, shiny."""
    # two cherries
    d.ellipse([8, 22, 24, 40], fill=RED)
    d.ellipse([10, 24, 22, 38], fill=LRED)
    d.ellipse([12, 26, 16, 30], fill=WH)  # shine
    d.ellipse([26, 22, 42, 40], fill=RED)
    d.ellipse([28, 24, 40, 38], fill=LRED)
    d.ellipse([30, 26, 34, 30], fill=WH)  # shine
    # joined stems
    d.arc([10, 4, 30, 26], start=200, end=340, fill=DGRN, width=2)
    d.arc([20, 4, 40, 26], start=200, end=340, fill=DGRN, width=2)
    # leaf at junction
    d.polygon([(22, 6), (28, 2), (30, 8)], fill=GRN)

def draw_custard_apple(d):
    """Custard apple: green bumpy round fruit, visible segments."""
    d.ellipse([8, 10, 42, 46], fill=GRN)
    d.ellipse([10, 12, 40, 44], fill=LGRN)
    # bumpy segments
    for y in range(14, 42, 6):
        for x in range(12, 38, 6):
            d.ellipse([x, y, x+5, y+5], fill=GRN)
    # lighter areas between segments
    for y in range(17, 40, 6):
        for x in range(14, 36, 6):
            d.ellipse([x, y, x+2, y+2], fill=LYELL)
    # stem
    d.line([25, 10, 25, 4], fill=BRN, width=2)

def draw_elderberry(d):
    """Elderberry: cluster of tiny dark berries on stem."""
    # stem structure
    d.line([25, 46, 25, 20], fill=DGRN, width=2)
    d.line([25, 24, 16, 18], fill=DGRN, width=1)
    d.line([25, 24, 34, 18], fill=DGRN, width=1)
    d.line([25, 28, 18, 24], fill=DGRN, width=1)
    d.line([25, 28, 32, 24], fill=DGRN, width=1)
    # many tiny berries in cluster
    for x, y in [(14, 14), (18, 12), (22, 10), (26, 10), (30, 12), (34, 14),
                 (16, 18), (20, 16), (24, 16), (28, 16), (32, 18),
                 (18, 22), (22, 20), (26, 20), (30, 22),
                 (20, 26), (24, 24), (28, 26)]:
        d.ellipse([x-2, y-2, x+2, y+2], fill=DPURP)
        d.ellipse([x-1, y-1, x+1, y+1], fill=PURP)

def draw_grape(d):
    """Grape: cluster of purple grapes in pyramid, stem + leaf."""
    # grape cluster (pyramid arrangement)
    positions = [
        (18, 18), (26, 18), (34, 18),
        (22, 24), (30, 24),
        (18, 30), (26, 30), (34, 30),
        (22, 36), (30, 36),
        (26, 42),
    ]
    for x, y in positions:
        d.ellipse([x-4, y-4, x+4, y+4], fill=PURP)
        d.ellipse([x-3, y-3, x+1, y+1], fill=LPURP)  # highlight
    # stem
    d.line([26, 18, 26, 8], fill=BRN, width=2)
    # leaf
    d.polygon([(26, 8), (34, 4), (38, 10), (30, 12)], fill=GRN)
    d.line([28, 8, 36, 6], fill=DGRN, width=1)

def draw_langsat(d):
    """Langsat: cluster of pale yellow round fruits, thin skin."""
    # cluster of 3-4 round fruits
    d.ellipse([8, 18, 26, 38], fill=YELL)
    d.ellipse([10, 20, 24, 36], fill=LYELL)
    d.ellipse([22, 14, 40, 34], fill=YELL)
    d.ellipse([24, 16, 38, 32], fill=LYELL)
    d.ellipse([16, 28, 34, 46], fill=YELL)
    d.ellipse([18, 30, 32, 44], fill=LYELL)
    # slight brown spots
    d.ellipse([14, 24, 16, 26], fill=LBRN)
    d.ellipse([28, 22, 30, 24], fill=LBRN)
    d.ellipse([24, 36, 26, 38], fill=LBRN)
    # stem at top
    d.line([30, 14, 30, 6], fill=DGRN, width=2)
    d.polygon([(30, 6), (36, 4), (34, 8)], fill=GRN)

def draw_monstera_deliciosa(d):
    """Monstera deliciosa: green hexagonal-scaled elongated fruit."""
    # elongated cone shape
    d.rounded_rectangle([14, 6, 36, 44], radius=6, fill=GRN)
    d.rounded_rectangle([16, 8, 34, 42], radius=4, fill=LGRN)
    # hexagonal scale pattern
    for y in range(10, 40, 4):
        for x in range(16, 34, 4):
            d.rectangle([x, y, x+3, y+3], fill=GRN)
    # cream colored ripe sections peeling
    d.rectangle([18, 30, 22, 34], fill=CREAM)
    d.rectangle([26, 32, 30, 36], fill=CREAM)
    d.rectangle([20, 36, 24, 40], fill=CREAM)
    # stem at top
    d.line([25, 6, 25, 2], fill=DGRN, width=2)

def draw_physalis(d):
    """Physalis (cape gooseberry): orange berry in papery husk."""
    # papery husk (lantern shape)
    d.polygon([(25, 4), (40, 18), (38, 40), (25, 46), (12, 40), (10, 18)], fill=LYELL)
    d.polygon([(25, 6), (38, 18), (36, 38), (25, 44), (14, 38), (12, 18)], fill=YELL)
    # veins on husk
    d.line([25, 4, 25, 46], fill=DYELL, width=1)
    d.line([10, 18, 40, 18], fill=DYELL, width=1)
    d.line([12, 40, 38, 40], fill=DYELL, width=1)
    # orange berry visible inside (peeking through)
    d.ellipse([18, 20, 32, 34], fill=ORNG)
    d.ellipse([20, 22, 28, 30], fill=LORNG)
    d.ellipse([22, 24, 25, 27], fill=WH)  # shine

def draw_pineapple(d):
    """Pineapple: golden body with diamond pattern, green crown."""
    # body
    d.rounded_rectangle([12, 18, 38, 46], radius=4, fill=ORNG)
    d.rounded_rectangle([14, 20, 36, 44], radius=3, fill=YELL)
    # diamond/cross-hatch pattern
    for y in range(20, 44, 4):
        for x in range(14, 36, 4):
            d.line([x, y, x+4, y+4], fill=DORNG, width=1)
            d.line([x+4, y, x, y+4], fill=DORNG, width=1)
    # small brown eyes at intersections
    for y in range(22, 42, 4):
        for x in range(16, 34, 4):
            d.ellipse([x, y, x+1, y+1], fill=BRN)
    # green crown (spiky leaves)
    d.polygon([(20, 20), (18, 10), (22, 18)], fill=GRN)
    d.polygon([(24, 18), (22, 6), (26, 16)], fill=DGRN)
    d.polygon([(26, 16), (28, 4), (30, 18)], fill=GRN)
    d.polygon([(28, 18), (32, 10), (32, 20)], fill=DGRN)
    d.polygon([(22, 20), (16, 14), (20, 20)], fill=LGRN)

def draw_rambutan(d):
    """Rambutan: red hairy round fruit, green/yellow spines."""
    # core red fruit
    d.ellipse([14, 16, 36, 40], fill=RED)
    d.ellipse([16, 18, 34, 38], fill=LRED)
    # hairy spines all around
    for angle in range(0, 360, 20):
        rad = math.radians(angle)
        cx, cy = 25, 28
        x1 = int(cx + 12 * math.cos(rad))
        y1 = int(cy + 12 * math.sin(rad))
        x2 = int(cx + 18 * math.cos(rad))
        y2 = int(cy + 18 * math.sin(rad))
        c = LGRN if angle % 40 == 0 else YELL
        d.line([x1, y1, x2, y2], fill=c, width=2)
    # highlight
    d.ellipse([18, 20, 24, 26], fill=WH)

def draw_soursop(d):
    """Soursop: green heart-shape with soft spines, white inside."""
    d.ellipse([8, 10, 42, 46], fill=GRN)
    d.ellipse([10, 12, 40, 44], fill=LGRN)
    # soft spines/bumps
    for y in range(14, 42, 5):
        for x in range(12, 38, 5):
            d.polygon([(x+2, y), (x+4, y+3), (x, y+3)], fill=GRN)
    # white flesh visible through slight crack
    d.ellipse([20, 28, 30, 38], fill=WH)
    d.ellipse([22, 30, 28, 36], fill=CREAM)
    # dark seeds visible
    d.ellipse([24, 32, 26, 34], fill=BK)
    # stem
    d.line([25, 10, 25, 4], fill=DGRN, width=2)

def draw_starfruit(d):
    """Starfruit: 5-pointed star cross-section, yellow-green."""
    cx, cy = 25, 25
    pts = []
    for i in range(5):
        a = math.radians(i * 72 - 90)
        pts.append((int(cx + 18 * math.cos(a)), int(cy + 18 * math.sin(a))))
        a2 = math.radians(i * 72 + 36 - 90)
        pts.append((int(cx + 9 * math.cos(a2)), int(cy + 9 * math.sin(a2))))
    d.polygon(pts, fill=YELL)
    # inner star with lighter color
    pts2 = []
    for i in range(5):
        a = math.radians(i * 72 - 90)
        pts2.append((int(cx + 14 * math.cos(a)), int(cy + 14 * math.sin(a))))
        a2 = math.radians(i * 72 + 36 - 90)
        pts2.append((int(cx + 7 * math.cos(a2)), int(cy + 7 * math.sin(a2))))
    d.polygon(pts2, fill=LYELL)
    # center
    d.ellipse([21, 21, 29, 29], fill=LGRN)
    # ridge lines from center to tips
    for i in range(5):
        a = math.radians(i * 72 - 90)
        x2 = int(cx + 16 * math.cos(a))
        y2 = int(cy + 16 * math.sin(a))
        d.line([cx, cy, x2, y2], fill=DYELL, width=1)
    # small seeds near center
    for i in range(5):
        a = math.radians(i * 72 - 90)
        sx = int(cx + 5 * math.cos(a))
        sy = int(cy + 5 * math.sin(a))
        d.ellipse([sx-1, sy-1, sx+1, sy+1], fill=DBRN)

def draw_barberry(d):
    """Barberry: elongated red berry cluster on thorny branch."""
    # branch
    d.line([4, 30, 46, 20], fill=BRN, width=2)
    # thorns
    d.line([12, 28, 10, 22], fill=BRN, width=1)
    d.line([24, 24, 22, 18], fill=BRN, width=1)
    d.line([36, 22, 34, 16], fill=BRN, width=1)
    # elongated red berries hanging
    for x, y in [(10, 30), (16, 28), (22, 26), (28, 24), (34, 22), (40, 20),
                 (13, 34), (19, 32), (25, 30), (31, 28), (37, 26)]:
        d.ellipse([x-2, y, x+2, y+6], fill=RED)
        d.ellipse([x-1, y+1, x+1, y+3], fill=LRED)

def draw_black_currant(d):
    """Black currant: cluster of shiny dark berries, stem with leaf."""
    # stem
    d.line([25, 44, 25, 16], fill=DGRN, width=2)
    d.line([25, 20, 18, 16], fill=DGRN, width=1)
    d.line([25, 24, 32, 20], fill=DGRN, width=1)
    # berry cluster
    for x, y in [(18, 12), (24, 10), (30, 12), (16, 18), (22, 16),
                 (28, 16), (34, 18), (20, 22), (26, 22), (32, 24),
                 (22, 28), (28, 28)]:
        d.ellipse([x-3, y-3, x+3, y+3], fill=DPURP)
        d.ellipse([x-2, y-2, x, y], fill=PURP)  # highlight
    # crown on each berry
    for x, y in [(18, 12), (24, 10), (30, 12), (22, 16), (28, 16)]:
        d.line([x-1, y-3, x+1, y-3], fill=DGRN, width=1)
    # leaf
    d.polygon([(25, 40), (32, 36), (38, 40), (32, 44)], fill=GRN)

def draw_cloudberry(d):
    """Cloudberry: amber/golden bumpy berry, red-tipped sepals."""
    # sepals underneath
    d.polygon([(10, 28), (8, 36), (16, 32)], fill=GRN)
    d.polygon([(40, 28), (42, 36), (34, 32)], fill=GRN)
    d.polygon([(20, 38), (18, 46), (26, 42)], fill=GRN)
    d.polygon([(30, 38), (32, 46), (24, 42)], fill=GRN)
    # drupelets (bumpy berry segments)
    for x, y in [(18, 16), (26, 14), (34, 16),
                 (14, 22), (22, 20), (30, 20), (38, 22),
                 (18, 28), (26, 26), (34, 28),
                 (22, 34), (30, 34)]:
        d.ellipse([x-4, y-4, x+4, y+4], fill=ORNG)
        d.ellipse([x-3, y-3, x-1, y-1], fill=LORNG)  # highlight
    # stem
    d.line([26, 14, 26, 6], fill=DGRN, width=2)

def draw_mulberry(d):
    """Mulberry: elongated dark berry cluster, stem."""
    # elongated shape made of drupelets
    for y_off in range(12, 40, 4):
        w = 6 if (y_off < 16 or y_off > 36) else 10
        cx = 25
        for x_off in range(cx - w, cx + w, 4):
            d.ellipse([x_off, y_off, x_off+4, y_off+4], fill=DPURP)
            d.ellipse([x_off+1, y_off+1, x_off+2, y_off+2], fill=PURP)
    # stem
    d.line([25, 12, 25, 4], fill=DGRN, width=2)
    # tiny leaf
    d.polygon([(25, 4), (30, 2), (28, 6)], fill=GRN)

def draw_red_currant(d):
    """Red currant: translucent red berries on stem, in a chain."""
    # long drooping stem
    d.line([25, 4, 25, 14], fill=DGRN, width=2)
    d.line([25, 14, 22, 20], fill=DGRN, width=1)
    d.line([22, 20, 24, 28], fill=DGRN, width=1)
    d.line([24, 28, 22, 36], fill=DGRN, width=1)
    # berries hanging along stem (translucent red)
    for x, y in [(20, 14), (28, 16), (18, 20), (26, 22),
                 (20, 26), (28, 28), (22, 32), (26, 36),
                 (22, 40)]:
        d.ellipse([x-3, y-3, x+3, y+3], fill=RED)
        d.ellipse([x-2, y-2, x, y], fill=LRED)  # highlight/shine
        d.ellipse([x-1, y-1, x, y], fill=WH)
    # leaf at top
    d.polygon([(25, 4), (34, 2), (32, 8)], fill=GRN)

def draw_banana(d):
    """Banana: curved yellow crescent, brown tips, green-to-yellow."""
    # curved banana shape
    d.arc([2, 8, 48, 48], start=200, end=340, fill=YELL, width=10)
    # fill the banana body
    d.polygon([(10, 14), (14, 10), (42, 22), (44, 28), (38, 34), (8, 22)], fill=YELL)
    d.polygon([(12, 16), (16, 12), (40, 24), (42, 28), (36, 32), (10, 20)], fill=LYELL)
    # brown tip at bottom
    d.ellipse([6, 18, 12, 24], fill=BRN)
    # stem at top
    d.rectangle([40, 20, 46, 26], fill=LGRN)
    d.rectangle([42, 22, 46, 24], fill=GRN)
    # ridge lines
    d.line([14, 12, 40, 24], fill=DYELL, width=1)

def draw_blackberry(d):
    """Blackberry: dark purple/black bumpy berry with green calyx."""
    # calyx (sepals)
    d.polygon([(10, 16), (6, 24), (14, 20)], fill=GRN)
    d.polygon([(40, 16), (44, 24), (36, 20)], fill=GRN)
    d.polygon([(14, 38), (10, 44), (18, 42)], fill=GRN)
    d.polygon([(36, 38), (40, 44), (32, 42)], fill=GRN)
    # drupelets
    for x, y in [(20, 14), (28, 14),
                 (16, 20), (24, 18), (32, 20),
                 (14, 26), (22, 24), (30, 24), (38, 26),
                 (16, 32), (24, 30), (32, 32),
                 (20, 38), (28, 38)]:
        d.ellipse([x-3, y-3, x+3, y+3], fill=BK)
        d.ellipse([x-3, y-3, x+3, y+3], fill=DPURP)
        d.ellipse([x-2, y-2, x, y], fill=PURP)  # highlight
    # stem
    d.line([24, 14, 24, 6], fill=DGRN, width=2)

def draw_boysenberry(d):
    """Boysenberry: dark reddish-purple berry, larger than blackberry."""
    # calyx
    d.polygon([(12, 14), (8, 20), (16, 18)], fill=DGRN)
    d.polygon([(38, 14), (42, 20), (34, 18)], fill=DGRN)
    # drupelets (reddish-purple, larger)
    for x, y in [(20, 12), (30, 12),
                 (15, 18), (25, 16), (35, 18),
                 (14, 26), (24, 24), (34, 26),
                 (16, 34), (26, 32), (36, 34),
                 (20, 40), (30, 40)]:
        d.ellipse([x-4, y-4, x+4, y+4], fill=CRIM)
        d.ellipse([x-3, y-3, x-1, y-1], fill=DPINK)
    # stem
    d.line([25, 12, 25, 4], fill=DGRN, width=2)

def draw_marionberry(d):
    """Marionberry: elongated dark berry, slightly conical."""
    # calyx at top
    d.polygon([(16, 12), (12, 18), (20, 16)], fill=GRN)
    d.polygon([(34, 12), (38, 18), (30, 16)], fill=GRN)
    # elongated cone of drupelets
    for x, y in [(22, 10), (28, 10),
                 (18, 16), (24, 14), (30, 14), (36, 16),
                 (16, 22), (22, 20), (28, 20), (34, 22),
                 (18, 28), (24, 26), (30, 26), (36, 28),
                 (20, 34), (26, 32), (32, 34),
                 (24, 40), (28, 40)]:
        d.ellipse([x-3, y-3, x+3, y+3], fill=DPURP)
        d.ellipse([x-2, y-2, x, y], fill=PURP)
    # stem
    d.line([25, 10, 25, 4], fill=DGRN, width=2)

def draw_raspberry(d):
    """Raspberry: pink-red bumpy berry, hollow center visible."""
    # calyx
    d.polygon([(12, 14), (8, 20), (16, 18)], fill=GRN)
    d.polygon([(38, 14), (42, 20), (34, 18)], fill=GRN)
    # drupelets (pink-red, round)
    for x, y in [(20, 12), (28, 12),
                 (14, 18), (22, 16), (30, 16), (38, 18),
                 (14, 24), (22, 22), (30, 22), (38, 24),
                 (16, 30), (24, 28), (32, 30),
                 (20, 36), (28, 36),
                 (24, 42)]:
        d.ellipse([x-3, y-3, x+3, y+3], fill=PINK)
        d.ellipse([x-3, y-3, x+3, y+3], fill=RED)
        d.ellipse([x-2, y-2, x, y], fill=LRED)
    # hollow center hint
    d.ellipse([22, 22, 28, 28], fill=DPINK)
    # stem
    d.line([24, 12, 24, 4], fill=DGRN, width=2)


# ===========================================================================
# Master replacement dict
# ===========================================================================

REPLACEMENTS = {
    # Bland (<=3 colors)
    "salak":              draw_salak,
    "tamarind":           draw_tamarind,
    # Bland (4 colors)
    "bergamot":           draw_bergamot,
    "bilberry":           draw_bilberry,
    "breadfruit":         draw_breadfruit,
    "cherimoya":          draw_cherimoya,
    "cherry":             draw_cherry,
    "custard_apple":      draw_custard_apple,
    "elderberry":         draw_elderberry,
    "grape":              draw_grape,
    "langsat":            draw_langsat,
    "monstera_deliciosa": draw_monstera_deliciosa,
    "physalis":           draw_physalis,
    "pineapple":          draw_pineapple,
    "rambutan":           draw_rambutan,
    "soursop":            draw_soursop,
    "starfruit":          draw_starfruit,
    # Sparse (<500 opaque px)
    "barberry":           draw_barberry,
    "black_currant":      draw_black_currant,
    "cloudberry":         draw_cloudberry,
    "mulberry":           draw_mulberry,
    "red_currant":        draw_red_currant,
    "banana":             draw_banana,
    "blackberry":         draw_blackberry,
    "boysenberry":        draw_boysenberry,
    "marionberry":        draw_marionberry,
    "raspberry":          draw_raspberry,
}


def apply_quantize_no_outline(filepath):
    """Quantize existing image to <=9 colors, no dither, NO outline."""
    try:
        img = Image.open(filepath).convert("RGBA")
        img = _quantize_no_outline(img)
        img.save(filepath)
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Draw all replacement/improved sprites
    print(f"Step 1/2 — Drawing {len(REPLACEMENTS)} replacement/improved fruit sprites…")
    for name, fn in REPLACEMENTS.items():
        save_sprite(name, fn)
        print(f"  ✓  {name}")

    # 2. Quantize ALL 50x50 images (no outline) for consistency
    all_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png")))
    print(f"\nStep 2/2 — Quantizing {len(all_files)} 50×50 images (no outline)…")
    for f in all_files:
        apply_quantize_no_outline(f)

    # 3. Verify
    print("\nColor count verification:")
    all_ok = True
    for f in sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png"))):
        name = os.path.basename(f).replace("_50x50.png", "")
        img = Image.open(f).convert("RGBA")
        arr = np.array(img)
        mask = arr[:, :, 3] > 128
        if mask.any():
            colors = set(map(tuple, arr[mask][:, :3]))
            nc = len(colors)
        else:
            nc = 0
        flag = "✓" if nc <= 10 else "⚠️"
        if nc > 10:
            all_ok = False
        print(f"  {flag} {name:25s}: {nc:2d} colors")

    # 4. Check for duplicates
    import hashlib
    hashes = {}
    for f in sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png"))):
        name = os.path.basename(f).replace("_50x50.png", "")
        img = Image.open(f).convert("RGBA")
        h = hashlib.md5(np.array(img).tobytes()).hexdigest()
        if h not in hashes:
            hashes[h] = []
        hashes[h].append(name)

    print("\nDuplicate check:")
    any_dupes = False
    for h, names in hashes.items():
        if len(names) > 1:
            print(f"  ⚠️ STILL DUPLICATED: {names}")
            any_dupes = True
    if not any_dupes:
        print("  ✓ No duplicates found!")

    status = "✓ ALL OK" if all_ok else "⚠️ Some images exceed 10 colors"
    print(f"\nDone — {status}")


if __name__ == "__main__":
    main()
