"""
enhance_animals_v2.py
=====================
Comprehensive enhancement of ALL 135 50x50 animal sprites for a kids'
pixel-coloring game.

Goals:
  1. Replace ALL duplicate images with unique art for each animal
  2. Improve bland/placeholder images (<=3 colors) with realistic detail
  3. Quantize every image to <= 10 colors (no dithering, no noise)
  4. NO black outlines added around the sprites
  5. Clean, solid color regions ideal for children's coloring

Duplicate groups found in original data:
  - alligator = crocodile
  - beetle = ladybug
  - beluga = narwhal = whale
  - bison = yak
  - cheetah = jaguar = leopard = panther
  - chipmunk = squirrel
  - dugong = manatee = sea_lion = seal
  - goose = swan
  - hedgehog = porcupine
  - ostrich = pelican = puffin

Bland images (<=3 colors):
  ant, camel, crow, firefly, gecko, lemur, pangolin,
  salamander, seahorse, starfish, stingray, tapir
"""

import os
import glob
import math
from PIL import Image, ImageDraw
import numpy as np

OUTPUT_DIR = "images/animals"

# ---------------------------------------------------------------------------
# Palette (shared across all sprites)
# ---------------------------------------------------------------------------
T    = (0,   0,   0,   0)      # transparent
BK   = (25,  25,  25,  255)    # black
WH   = (245, 245, 245, 255)   # white
LGY  = (200, 200, 200, 255)   # light grey
MGY  = (160, 160, 160, 255)   # mid grey
DGY  = (100, 100, 100, 255)   # dark grey

BRN  = (160, 105, 55,  255)   # medium brown
DBRN = (110, 65,  25,  255)   # dark brown
LBRN = (210, 170, 120, 255)   # light brown / tan
ORNG = (235, 130, 40,  255)   # orange
YELL = (240, 210, 50,  255)   # yellow
RED  = (210, 60,  50,  255)   # red
PINK = (240, 175, 175, 255)   # pink
GRN  = (80,  160, 70,  255)   # green
DGRN = (50,  110, 45,  255)   # dark green
LGRN = (160, 210, 130, 255)   # light green
BLU  = (70,  120, 200, 255)   # blue
LBLU = (160, 210, 250, 255)   # light blue
PURP = (150, 90,  200, 255)   # purple
CRMS = (180, 50,  80,  255)   # crimson
GOLD = (210, 175, 55,  255)   # gold
SKIN = (230, 195, 155, 255)   # skin tone
DRED = (150, 40,  30,  255)   # dark red
LPNK = (255, 200, 200, 255)   # light pink
TEAL = (60,  170, 170, 255)   # teal
NAVY = (40,  60,  120, 255)   # navy


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
    mask = alpha > 128

    rgb = arr[:, :, :3].astype(float)
    new_alpha = alpha.copy()

    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((rgb, new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))

    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    fa = np.array(final)
    fa[:, :, 3] = new_alpha
    return Image.fromarray(fa, "RGBA")


# ===========================================================================
# DUPLICATE-FIX SPRITES: Unique art for each animal that was duplicated
# ===========================================================================

# --- alligator vs crocodile (were identical) ---
def draw_alligator(d):
    """Alligator: wider snout, darker green, low profile."""
    d.ellipse([10, 28, 44, 42], fill=DGRN)        # body
    d.ellipse([12, 30, 42, 40], fill=GRN)          # belly
    # wide flat head
    d.rounded_rectangle([4, 24, 24, 36], radius=3, fill=DGRN)
    d.ellipse([4, 28, 16, 36], fill=GRN)           # jaw
    # teeth along mouth
    for x in range(6, 20, 3):
        d.rectangle([x, 32, x+1, 34], fill=WH)
    # eyes on top of head
    d.ellipse([14, 24, 18, 28], fill=YELL)
    d.ellipse([20, 24, 24, 28], fill=YELL)
    d.ellipse([15, 25, 17, 27], fill=BK)
    d.ellipse([21, 25, 23, 27], fill=BK)
    # scaly ridges on back
    for x in range(24, 44, 4):
        d.polygon([(x, 28), (x+2, 24), (x+4, 28)], fill=DGRN)
    # tail
    d.polygon([(42, 32), (50, 30), (50, 36), (42, 36)], fill=DGRN)
    # legs
    for x in [16, 24, 32, 38]:
        d.rectangle([x, 40, x+3, 46], fill=DGRN)

def draw_crocodile(d):
    """Crocodile: narrower V-shaped snout, lighter, visible teeth."""
    d.ellipse([12, 28, 44, 42], fill=GRN)          # body
    d.ellipse([14, 30, 42, 40], fill=LGRN)         # belly
    # narrow V-snout
    d.polygon([(4, 30), (22, 28), (22, 36), (4, 34)], fill=GRN)
    d.polygon([(4, 32), (12, 31), (12, 33), (4, 33)], fill=LGRN)
    # teeth sticking out
    for x in range(6, 18, 3):
        d.rectangle([x, 30, x+1, 32], fill=WH)
        d.rectangle([x, 34, x+1, 36], fill=WH)
    # eyes raised
    d.ellipse([18, 24, 22, 28], fill=YELL)
    d.ellipse([19, 25, 21, 27], fill=BK)
    # armor plates on back
    for x in range(24, 42, 3):
        d.rectangle([x, 28, x+2, 30], fill=DGRN)
    # tail (long, tapered)
    d.polygon([(42, 32), (50, 34), (42, 38)], fill=GRN)
    # legs
    for x in [18, 26, 32, 38]:
        d.rectangle([x, 40, x+3, 46], fill=DGRN)

# --- beetle vs ladybug (were identical) ---
def draw_beetle(d):
    """Beetle: shiny dark green/brown, horn."""
    d.ellipse([14, 22, 38, 42], fill=DGRN)         # body (hard shell)
    d.ellipse([16, 24, 36, 40], fill=GRN)          # wing case
    # wing split line
    d.line([25, 22, 25, 42], fill=DGRN, width=1)
    # head
    d.ellipse([18, 14, 32, 26], fill=DBRN)
    # horn
    d.polygon([(24, 14), (26, 14), (25, 6)], fill=DBRN)
    # eyes
    d.ellipse([18, 16, 22, 20], fill=BK)
    d.ellipse([28, 16, 32, 20], fill=BK)
    # legs (3 per side)
    for y_off in [28, 32, 36]:
        d.line([14, y_off, 8, y_off+4], fill=DBRN, width=2)
        d.line([38, y_off, 44, y_off+4], fill=DBRN, width=2)
    # antennae
    d.line([22, 16, 14, 8], fill=DBRN, width=1)
    d.line([28, 16, 36, 8], fill=DBRN, width=1)

def draw_ladybug(d):
    """Ladybug: bright red with black spots, distinct from beetle."""
    d.ellipse([12, 18, 38, 42], fill=RED)           # shell
    # wing line
    d.line([25, 18, 25, 42], fill=BK, width=1)
    # black spots
    for x, y in [(16, 22), (30, 22), (18, 30), (28, 30), (22, 36)]:
        d.ellipse([x, y, x+4, y+4], fill=BK)
    # head (black)
    d.ellipse([18, 12, 32, 22], fill=BK)
    # eyes
    d.ellipse([19, 14, 23, 18], fill=WH)
    d.ellipse([27, 14, 31, 18], fill=WH)
    d.ellipse([20, 15, 22, 17], fill=BK)
    d.ellipse([28, 15, 30, 17], fill=BK)
    # legs
    for y_off in [26, 32, 38]:
        d.line([12, y_off, 6, y_off+3], fill=BK, width=2)
        d.line([38, y_off, 44, y_off+3], fill=BK, width=2)
    # antennae
    d.line([22, 14, 16, 6], fill=BK, width=1)
    d.line([28, 14, 34, 6], fill=BK, width=1)

# --- beluga vs narwhal vs whale (were identical) ---
def draw_beluga(d):
    """Beluga: all white, round head (melon), small body."""
    d.ellipse([8, 22, 42, 42], fill=WH)            # body
    d.ellipse([10, 26, 40, 40], fill=LGY)          # belly shading
    # round melon head
    d.ellipse([4, 16, 24, 32], fill=WH)
    # small mouth
    d.arc([6, 24, 16, 30], start=0, end=180, fill=MGY, width=1)
    # eye
    d.ellipse([8, 20, 12, 24], fill=BK)
    # flippers
    d.ellipse([18, 36, 28, 46], fill=LGY)
    # tail fluke
    d.polygon([(40, 28), (50, 22), (50, 26)], fill=LGY)
    d.polygon([(40, 34), (50, 36), (50, 40)], fill=LGY)

def draw_narwhal(d):
    """Narwhal: grey with long spiraling tusk, spotted."""
    d.ellipse([12, 24, 44, 40], fill=MGY)           # body
    d.ellipse([14, 26, 42, 38], fill=LGY)           # belly
    # spots
    for x, y in [(18, 26), (26, 25), (34, 26), (22, 32), (30, 32)]:
        d.ellipse([x, y, x+3, y+3], fill=DGY)
    # head
    d.ellipse([6, 22, 22, 34], fill=MGY)
    # tusk (long, spiraling)
    d.line([8, 26, 0, 14], fill=LBRN, width=3)
    d.line([0, 14, 0, 4], fill=LBRN, width=2)
    # eye
    d.ellipse([10, 24, 14, 28], fill=BK)
    # flipper
    d.ellipse([20, 34, 28, 44], fill=DGY)
    # tail fluke
    d.polygon([(42, 28), (50, 22), (50, 26)], fill=DGY)
    d.polygon([(42, 34), (50, 36), (50, 40)], fill=DGY)

def draw_whale(d):
    """Whale: large blue body, water spout, baleen lines."""
    d.ellipse([6, 22, 44, 44], fill=BLU)            # body
    d.ellipse([8, 28, 42, 42], fill=LBLU)           # belly
    # head
    d.ellipse([2, 24, 20, 38], fill=BLU)
    d.ellipse([4, 30, 14, 38], fill=LBLU)           # jaw
    # baleen lines
    for y in range(30, 36, 2):
        d.line([6, y, 12, y], fill=MGY, width=1)
    # eye
    d.ellipse([8, 26, 12, 30], fill=BK)
    # water spout
    d.line([14, 24, 14, 14], fill=LBLU, width=2)
    d.ellipse([10, 8, 18, 14], fill=LBLU)
    # flipper
    d.ellipse([20, 36, 30, 46], fill=BLU)
    # tail fluke
    d.polygon([(42, 30), (50, 22), (50, 28)], fill=BLU)
    d.polygon([(42, 36), (50, 38), (50, 44)], fill=BLU)

# --- bison vs yak (were identical) ---
def draw_bison(d):
    """Bison: massive hump, shaggy mane, horns curve outward."""
    d.ellipse([14, 28, 44, 46], fill=DBRN)          # body
    # big shoulder hump
    d.ellipse([10, 18, 30, 34], fill=DBRN)
    d.ellipse([12, 20, 28, 32], fill=BRN)           # mane fur
    # head (lower, massive)
    d.ellipse([4, 22, 22, 36], fill=DBRN)
    d.ellipse([4, 28, 14, 36], fill=BRN)            # muzzle
    # short curved horns
    d.arc([4, 16, 14, 26], start=180, end=300, fill=LBRN, width=3)
    d.arc([14, 16, 24, 26], start=240, end=360, fill=LBRN, width=3)
    # eye
    d.ellipse([8, 24, 11, 27], fill=BK)
    # beard
    d.ellipse([6, 34, 14, 40], fill=DBRN)
    # legs
    for x in [18, 24, 32, 38]:
        d.rectangle([x, 44, x+3, 50], fill=BRN)

def draw_yak(d):
    """Yak: long shaggy hair, long horns curve up, Tibetan look."""
    d.ellipse([12, 26, 44, 46], fill=BK)            # dark body
    # very long shaggy skirt of hair
    d.ellipse([10, 34, 46, 50], fill=DBRN)
    d.ellipse([12, 36, 44, 50], fill=BRN)
    # head
    d.ellipse([4, 18, 22, 32], fill=BK)
    d.ellipse([4, 24, 14, 32], fill=DGY)            # muzzle
    # long curved horns (upward)
    d.arc([2, 8, 14, 22], start=180, end=340, fill=LGY, width=3)
    d.arc([14, 8, 26, 22], start=200, end=360, fill=LGY, width=3)
    # eye
    d.ellipse([8, 22, 11, 25], fill=BK)
    d.ellipse([9, 23, 10, 24], fill=WH)
    # legs (hidden in fur, just hooves visible)
    for x in [18, 24, 32, 38]:
        d.rectangle([x, 46, x+3, 50], fill=DGY)

# --- cheetah vs jaguar vs leopard vs panther (were identical) ---
def draw_cheetah(d):
    """Cheetah: slim, tan, small solid spots, tear marks on face."""
    d.ellipse([12, 26, 42, 42], fill=LBRN)          # slim body
    d.ellipse([14, 28, 40, 40], fill=(240, 210, 170, 255))  # belly
    # small solid spots
    for x, y in [(16, 28), (22, 27), (28, 28), (34, 27), (18, 34), (26, 34), (32, 34)]:
        d.ellipse([x, y, x+2, y+2], fill=BK)
    # head (small, round)
    d.ellipse([6, 16, 22, 28], fill=LBRN)
    # tear marks (black lines from eye to mouth)
    d.line([8, 22, 6, 28], fill=BK, width=1)
    d.line([16, 22, 18, 28], fill=BK, width=1)
    # eye
    d.ellipse([10, 18, 14, 22], fill=YELL)
    d.ellipse([11, 19, 13, 21], fill=BK)
    # ears
    d.ellipse([8, 14, 12, 18], fill=BRN)
    d.ellipse([16, 13, 20, 17], fill=BRN)
    # long tail
    d.line([42, 34, 50, 28], fill=LBRN, width=3)
    # long slim legs
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 40, x+2, 48], fill=LBRN)

def draw_jaguar(d):
    """Jaguar: stocky, golden-orange, large rosette spots with centers."""
    d.ellipse([10, 24, 42, 44], fill=ORNG)          # stocky body
    d.ellipse([12, 28, 40, 42], fill=LBRN)          # belly
    # rosettes (circles with lighter centers)
    for x, y in [(16, 26), (26, 26), (34, 26), (20, 34), (30, 34)]:
        d.ellipse([x, y, x+5, y+5], fill=DBRN)
        d.ellipse([x+1, y+1, x+4, y+4], fill=ORNG)
    # broad head
    d.ellipse([4, 16, 24, 30], fill=ORNG)
    d.ellipse([4, 22, 14, 30], fill=LBRN)           # muzzle
    # eye
    d.ellipse([8, 18, 12, 22], fill=YELL)
    d.ellipse([9, 19, 11, 21], fill=BK)
    # ears
    d.ellipse([8, 14, 12, 18], fill=ORNG)
    d.ellipse([18, 13, 22, 17], fill=ORNG)
    # legs (thick)
    for x in [14, 22, 30, 36]:
        d.rectangle([x, 42, x+3, 50], fill=BRN)
    # tail
    d.line([42, 34, 50, 32], fill=ORNG, width=3)

def draw_leopard(d):
    """Leopard: golden, open rosettes, long tail, tree-dweller look."""
    d.ellipse([10, 26, 42, 42], fill=YELL)          # body
    d.ellipse([12, 28, 40, 40], fill=(250, 230, 180, 255))  # belly
    # open rosettes (rings only)
    for x, y in [(16, 27), (24, 26), (32, 27), (18, 34), (28, 34)]:
        d.ellipse([x, y, x+5, y+5], outline=DBRN, width=1)
    # head
    d.ellipse([4, 16, 22, 28], fill=YELL)
    d.ellipse([4, 22, 12, 28], fill=LBRN)           # muzzle
    # whisker dots
    d.ellipse([4, 24, 6, 26], fill=BK)
    d.ellipse([10, 24, 12, 26], fill=BK)
    # eye
    d.ellipse([8, 18, 12, 22], fill=GRN)
    d.ellipse([9, 19, 11, 21], fill=BK)
    # ears
    d.ellipse([8, 14, 12, 18], fill=BRN)
    d.ellipse([18, 13, 22, 17], fill=BRN)
    # long curving tail
    d.arc([36, 24, 50, 42], start=270, end=90, fill=YELL, width=4)
    # legs
    for x in [14, 22, 30, 36]:
        d.rectangle([x, 40, x+3, 48], fill=BRN)

def draw_panther(d):
    """Panther: all-black with subtle dark grey markings, green eyes."""
    d.ellipse([10, 26, 42, 42], fill=BK)            # body
    d.ellipse([12, 28, 40, 40], fill=DGY)           # subtle belly
    # subtle rosettes in dark grey
    for x, y in [(16, 28), (24, 27), (32, 28), (20, 34), (30, 34)]:
        d.ellipse([x, y, x+4, y+4], fill=DGY)
    # head
    d.ellipse([4, 16, 22, 28], fill=BK)
    d.ellipse([4, 22, 12, 28], fill=DGY)            # muzzle
    # glowing green eyes
    d.ellipse([8, 18, 12, 22], fill=GRN)
    d.ellipse([9, 19, 11, 21], fill=YELL)
    # ears
    d.ellipse([8, 14, 12, 18], fill=DGY)
    d.ellipse([18, 13, 22, 17], fill=DGY)
    # tail
    d.arc([36, 24, 50, 42], start=270, end=90, fill=BK, width=4)
    # legs
    for x in [14, 22, 30, 36]:
        d.rectangle([x, 40, x+3, 48], fill=DGY)

# --- chipmunk vs squirrel (were identical) ---
def draw_chipmunk(d):
    """Chipmunk: small, stripes on back, cheek pouches, short tail."""
    d.ellipse([14, 26, 38, 42], fill=BRN)           # body
    d.ellipse([16, 28, 36, 40], fill=LBRN)          # belly
    # back stripes (chipmunk signature)
    d.line([18, 26, 18, 40], fill=DBRN, width=1)
    d.line([22, 26, 22, 40], fill=WH, width=1)
    d.line([26, 26, 26, 40], fill=DBRN, width=1)
    d.line([30, 26, 30, 40], fill=WH, width=1)
    d.line([34, 26, 34, 40], fill=DBRN, width=1)
    # head
    d.ellipse([8, 16, 24, 28], fill=BRN)
    # puffy cheeks
    d.ellipse([6, 20, 14, 28], fill=LBRN)
    d.ellipse([18, 20, 26, 28], fill=LBRN)
    # eye
    d.ellipse([10, 18, 14, 22], fill=BK)
    # nose
    d.ellipse([8, 24, 11, 26], fill=PINK)
    # ears (small round)
    d.ellipse([14, 14, 18, 18], fill=BRN)
    d.ellipse([20, 13, 24, 17], fill=BRN)
    # short fluffy tail (up)
    d.ellipse([34, 18, 44, 32], fill=BRN)
    # legs
    for x in [16, 22, 28, 34]:
        d.rectangle([x, 40, x+3, 46], fill=DBRN)

def draw_squirrel(d):
    """Squirrel: bushy curled tail, acorn-reddish, sitting up."""
    d.ellipse([16, 28, 34, 44], fill=ORNG)          # body
    d.ellipse([18, 30, 32, 42], fill=LBRN)          # belly
    # big bushy tail curling over back
    d.ellipse([30, 10, 48, 28], fill=ORNG)
    d.ellipse([32, 12, 46, 26], fill=LBRN)
    d.arc([28, 20, 44, 36], start=270, end=90, fill=ORNG, width=5)
    # head
    d.ellipse([8, 18, 24, 30], fill=ORNG)
    d.ellipse([8, 24, 16, 30], fill=LBRN)           # muzzle
    # eye (big, cute)
    d.ellipse([10, 20, 15, 25], fill=BK)
    d.ellipse([11, 21, 13, 23], fill=WH)
    # nose
    d.ellipse([8, 25, 11, 28], fill=BK)
    # ears (tufted)
    d.ellipse([14, 14, 18, 20], fill=ORNG)
    d.ellipse([20, 13, 24, 19], fill=ORNG)
    d.line([16, 14, 16, 10], fill=ORNG, width=1)
    d.line([22, 13, 22, 9], fill=ORNG, width=1)
    # arms holding something
    d.rectangle([14, 32, 18, 38], fill=BRN)
    # legs
    d.rectangle([18, 42, 22, 48], fill=BRN)
    d.rectangle([28, 42, 32, 48], fill=BRN)

# --- dugong vs manatee vs sea_lion vs seal (were identical) ---
def draw_dugong(d):
    """Dugong: grey-brown, whale-like tail fluke, rounded snout pointing down."""
    d.ellipse([8, 22, 42, 42], fill=MGY)            # body
    d.ellipse([10, 26, 40, 40], fill=LGY)           # belly
    # head with downturned snout
    d.ellipse([2, 20, 20, 34], fill=MGY)
    d.ellipse([2, 26, 12, 34], fill=LGY)            # muzzle (points down)
    # bristles on snout
    d.line([4, 30, 2, 32], fill=DGY, width=1)
    d.line([6, 30, 4, 32], fill=DGY, width=1)
    d.line([8, 30, 6, 32], fill=DGY, width=1)
    # eye
    d.ellipse([8, 22, 12, 26], fill=BK)
    # flippers
    d.ellipse([16, 34, 24, 44], fill=DGY)
    # whale-like tail fluke (horizontal)
    d.polygon([(40, 30), (50, 24), (50, 28)], fill=DGY)
    d.polygon([(40, 34), (50, 36), (50, 42)], fill=DGY)

def draw_manatee(d):
    """Manatee: round, paddle-shaped tail, grey, gentle face."""
    d.ellipse([6, 20, 42, 44], fill=DGY)            # big round body
    d.ellipse([8, 24, 40, 42], fill=MGY)            # belly
    # round head
    d.ellipse([2, 22, 18, 36], fill=DGY)
    d.ellipse([2, 28, 12, 36], fill=MGY)            # muzzle
    # bristly upper lip
    d.ellipse([4, 28, 10, 32], fill=LGY)
    # eye
    d.ellipse([6, 24, 10, 28], fill=BK)
    # round paddle flippers
    d.ellipse([14, 34, 22, 46], fill=DGY)
    # paddle-shaped tail (round, NOT fluked)
    d.ellipse([38, 28, 50, 40], fill=DGY)
    # wrinkle details
    d.arc([20, 26, 36, 36], start=0, end=180, fill=LGY, width=1)

def draw_sea_lion(d):
    """Sea lion: sleek, brown, ear flaps, flippers can walk."""
    d.ellipse([12, 26, 42, 44], fill=BRN)           # body
    d.ellipse([14, 30, 40, 42], fill=LBRN)          # belly
    # head (sleek, pointed)
    d.ellipse([4, 18, 22, 32], fill=BRN)
    d.ellipse([4, 24, 12, 32], fill=LBRN)           # muzzle
    # visible ear flaps (distinguishes from seal)
    d.ellipse([16, 16, 22, 22], fill=BRN)
    d.ellipse([17, 17, 21, 21], fill=DBRN)
    # eye
    d.ellipse([8, 20, 12, 24], fill=BK)
    # whiskers
    d.line([4, 26, 0, 24], fill=LGY, width=1)
    d.line([4, 28, 0, 28], fill=LGY, width=1)
    d.line([4, 30, 0, 32], fill=LGY, width=1)
    # front flippers (large, can support weight)
    d.polygon([(16, 34), (8, 44), (20, 44)], fill=DBRN)
    # rear flippers
    d.polygon([(36, 38), (40, 46), (48, 42)], fill=DBRN)
    # nose
    d.ellipse([4, 24, 8, 28], fill=BK)

def draw_seal(d):
    """Seal: round, grey, no ear flaps, spotted, belly-slider."""
    d.ellipse([8, 24, 44, 42], fill=MGY)            # round body
    d.ellipse([10, 28, 42, 40], fill=LGY)           # belly
    # spots
    for x, y in [(14, 26), (22, 25), (30, 26), (18, 32), (28, 32), (36, 28)]:
        d.ellipse([x, y, x+3, y+3], fill=DGY)
    # round head (no ear flaps)
    d.ellipse([2, 18, 20, 32], fill=MGY)
    # big dark eyes
    d.ellipse([6, 20, 12, 26], fill=BK)
    d.ellipse([7, 21, 9, 23], fill=WH)
    # nose
    d.ellipse([4, 26, 10, 30], fill=BK)
    # whiskers
    d.line([4, 28, 0, 26], fill=WH, width=1)
    d.line([4, 30, 0, 30], fill=WH, width=1)
    # small flippers (can't walk on them)
    d.ellipse([14, 36, 22, 44], fill=DGY)
    # rear flippers (point backward)
    d.polygon([(40, 30), (50, 28), (50, 36)], fill=DGY)

# --- goose vs swan (were identical) ---
def draw_goose(d):
    """Goose: white/grey, orange beak, shorter neck than swan, stocky."""
    d.ellipse([16, 26, 40, 44], fill=WH)            # body
    d.ellipse([18, 28, 38, 42], fill=LGY)           # wing shading
    # shorter neck
    d.rectangle([14, 16, 22, 30], fill=WH)
    # head
    d.ellipse([10, 10, 24, 22], fill=WH)
    # orange beak
    d.polygon([(10, 14), (4, 16), (10, 18)], fill=ORNG)
    # eye
    d.ellipse([12, 12, 16, 16], fill=BK)
    # grey wing feathers
    d.ellipse([22, 26, 40, 38], fill=MGY)
    # orange feet
    d.polygon([(22, 42), (16, 48), (26, 48)], fill=ORNG)
    d.polygon([(32, 42), (28, 48), (38, 48)], fill=ORNG)
    # tail
    d.polygon([(38, 32), (46, 30), (38, 36)], fill=LGY)

def draw_swan(d):
    """Swan: elegant white, long curved neck, orange/black beak."""
    d.ellipse([18, 28, 42, 44], fill=WH)            # body
    d.ellipse([20, 30, 40, 42], fill=LGY)           # wing
    # long S-curved neck
    d.arc([4, 6, 24, 30], start=180, end=360, fill=WH, width=6)
    # head at end of curve
    d.ellipse([4, 6, 16, 16], fill=WH)
    # beak (orange with black tip)
    d.polygon([(4, 10), (0, 10), (0, 12), (4, 12)], fill=ORNG)
    d.rectangle([0, 10, 2, 12], fill=BK)
    # eye
    d.ellipse([6, 8, 10, 12], fill=BK)
    # elegant wing detail
    d.ellipse([24, 28, 42, 38], fill=LGY)
    d.polygon([(40, 30), (48, 28), (40, 34)], fill=LGY)  # tail feathers
    # legs (tucked under or in water)
    d.rectangle([24, 42, 28, 48], fill=BK)
    d.rectangle([32, 42, 36, 48], fill=BK)

# --- hedgehog vs porcupine (were identical) ---
def draw_hedgehog(d):
    """Hedgehog: small, brown/tan face, short spines on back only."""
    d.ellipse([12, 24, 40, 44], fill=DBRN)          # body with spines
    # short spines (triangles on top half)
    for x in range(14, 40, 3):
        d.polygon([(x, 24), (x+1, 18), (x+2, 24)], fill=BRN)
    # light belly/face
    d.ellipse([14, 32, 38, 44], fill=LBRN)
    # cute face
    d.ellipse([8, 22, 22, 34], fill=LBRN)
    # button nose
    d.ellipse([8, 28, 12, 32], fill=BK)
    # eye (big, cute)
    d.ellipse([10, 24, 15, 29], fill=BK)
    d.ellipse([11, 25, 13, 27], fill=WH)
    # ear
    d.ellipse([16, 20, 22, 26], fill=BRN)
    # tiny legs
    for x in [16, 22, 28, 34]:
        d.rectangle([x, 42, x+3, 48], fill=DBRN)

def draw_porcupine(d):
    """Porcupine: bigger, LONG quills all over, darker, visible quill detail."""
    d.ellipse([12, 26, 40, 44], fill=DBRN)          # body
    d.ellipse([14, 30, 38, 42], fill=BRN)           # belly
    # long quills (much longer than hedgehog spines)
    for x in range(14, 40, 2):
        d.line([x, 26, x-2, 10], fill=LGY, width=1)
        d.line([x, 26, x+1, 12], fill=WH, width=1)
    # darker face (not as cute as hedgehog)
    d.ellipse([6, 22, 20, 34], fill=DBRN)
    d.ellipse([6, 26, 14, 34], fill=BRN)            # muzzle
    # eye (smaller)
    d.ellipse([8, 24, 12, 28], fill=BK)
    # nose
    d.ellipse([6, 28, 10, 32], fill=BK)
    # ears
    d.ellipse([14, 20, 18, 24], fill=DBRN)
    # legs (larger)
    for x in [14, 22, 28, 34]:
        d.rectangle([x, 42, x+4, 50], fill=BK)

# --- ostrich vs pelican vs puffin (were identical) ---
def draw_ostrich(d):
    """Ostrich: very long legs, tiny wings, long neck, big body."""
    # big round body
    d.ellipse([20, 16, 42, 32], fill=BK)           # black body feathers
    # small wings
    d.ellipse([24, 18, 42, 28], fill=DGY)
    # white tail feathers
    d.polygon([(40, 22), (48, 18), (48, 28)], fill=WH)
    # long neck
    d.rectangle([14, 4, 22, 20], fill=MGY)
    # small head
    d.ellipse([10, 2, 22, 12], fill=MGY)
    # beak (flat)
    d.polygon([(10, 6), (4, 6), (4, 8), (10, 8)], fill=PINK)
    # eye (large)
    d.ellipse([11, 3, 15, 7], fill=BK)
    d.ellipse([12, 4, 14, 6], fill=WH)
    # very long legs
    d.rectangle([24, 30, 28, 44], fill=PINK)
    d.rectangle([32, 30, 36, 44], fill=PINK)
    # two-toed feet
    d.line([24, 44, 20, 48], fill=PINK, width=2)
    d.line([28, 44, 30, 48], fill=PINK, width=2)
    d.line([32, 44, 30, 48], fill=PINK, width=2)
    d.line([36, 44, 38, 48], fill=PINK, width=2)

def draw_pelican(d):
    """Pelican: huge beak pouch, white body, grey wings."""
    d.ellipse([18, 22, 42, 40], fill=WH)            # body
    d.ellipse([22, 24, 42, 36], fill=LGY)           # wing
    # long neck
    d.rectangle([14, 12, 22, 26], fill=WH)
    # head
    d.ellipse([10, 6, 24, 18], fill=WH)
    # huge beak with pouch
    d.polygon([(10, 12), (0, 10), (0, 14)], fill=YELL)
    d.polygon([(10, 12), (0, 14), (4, 22), (10, 18)], fill=ORNG)  # pouch
    # eye
    d.ellipse([12, 8, 16, 12], fill=BK)
    # tail feathers
    d.polygon([(40, 28), (48, 26), (40, 34)], fill=LGY)
    # legs
    d.rectangle([24, 38, 28, 46], fill=YELL)
    d.rectangle([32, 38, 36, 46], fill=YELL)
    # webbed feet
    d.polygon([(22, 46), (30, 46), (26, 50)], fill=ORNG)
    d.polygon([(30, 46), (38, 46), (34, 50)], fill=ORNG)

def draw_puffin(d):
    """Puffin: black/white body, colorful orange/red beak, small stocky."""
    d.ellipse([16, 22, 36, 44], fill=BK)            # black body
    d.ellipse([18, 28, 34, 42], fill=WH)            # white breast
    # head
    d.ellipse([12, 14, 28, 26], fill=BK)
    d.ellipse([12, 18, 22, 26], fill=WH)            # white face
    # colorful beak (orange with red/grey stripes)
    d.polygon([(12, 18), (4, 18), (4, 22), (12, 22)], fill=ORNG)
    d.line([4, 20, 12, 20], fill=RED, width=1)
    # eye
    d.ellipse([14, 15, 18, 19], fill=BK)
    d.ellipse([13, 14, 19, 18], fill=WH)
    d.ellipse([15, 16, 17, 18], fill=BK)
    # small wings
    d.ellipse([10, 24, 20, 36], fill=BK)
    d.ellipse([32, 24, 42, 36], fill=BK)
    # orange feet
    d.rectangle([20, 42, 24, 48], fill=ORNG)
    d.rectangle([28, 42, 32, 48], fill=ORNG)

# ===========================================================================
# BLAND IMAGE FIXES (<=3 colors, need more realistic detail)
# ===========================================================================

def draw_ant(d):
    """Ant: 3-segment body, 6 legs, antennae, reddish-brown."""
    d.ellipse([22, 34, 32, 44], fill=DBRN)          # abdomen (large)
    d.ellipse([22, 26, 30, 36], fill=BRN)           # thorax
    d.ellipse([20, 18, 30, 28], fill=BRN)           # head
    # mandibles
    d.line([20, 24, 16, 28], fill=DBRN, width=2)
    d.line([30, 24, 34, 28], fill=DBRN, width=2)
    # eyes
    d.ellipse([21, 20, 24, 23], fill=WH)
    d.ellipse([26, 20, 29, 23], fill=WH)
    d.ellipse([22, 21, 23, 22], fill=BK)
    d.ellipse([27, 21, 28, 22], fill=BK)
    # antennae
    d.line([23, 18, 16, 10], fill=DBRN, width=1)
    d.line([16, 10, 12, 8], fill=DBRN, width=1)
    d.line([27, 18, 34, 10], fill=DBRN, width=1)
    d.line([34, 10, 38, 8], fill=DBRN, width=1)
    # 6 legs
    d.line([22, 30, 12, 26], fill=BRN, width=2)
    d.line([22, 32, 12, 32], fill=BRN, width=2)
    d.line([22, 34, 12, 38], fill=BRN, width=2)
    d.line([30, 30, 40, 26], fill=BRN, width=2)
    d.line([30, 32, 40, 32], fill=BRN, width=2)
    d.line([30, 34, 40, 38], fill=BRN, width=2)

def draw_camel(d):
    """Camel: tan, two humps, long legs, droopy face."""
    d.ellipse([12, 28, 42, 44], fill=LBRN)          # body
    # two humps
    d.ellipse([14, 18, 26, 32], fill=BRN)
    d.ellipse([26, 16, 38, 30], fill=BRN)
    # neck
    d.rectangle([10, 18, 18, 32], fill=LBRN)
    # head
    d.ellipse([4, 14, 18, 26], fill=LBRN)
    # droopy lips/muzzle
    d.ellipse([2, 20, 10, 26], fill=BRN)
    # eye
    d.ellipse([6, 16, 10, 20], fill=BK)
    d.ellipse([7, 17, 9, 19], fill=WH)
    # nostrils
    d.ellipse([4, 22, 6, 24], fill=DGY)
    # ears
    d.ellipse([12, 12, 16, 16], fill=LBRN)
    # long legs
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 42, x+3, 50], fill=BRN)

def draw_crow(d):
    """Crow: glossy black, purple sheen, prominent beak."""
    d.ellipse([18, 20, 38, 36], fill=BK)            # body
    # purple-blue sheen on wings
    d.ellipse([20, 22, 36, 34], fill=(50, 40, 70, 255))
    d.ellipse([22, 24, 34, 32], fill=DGY)
    # head
    d.ellipse([10, 14, 24, 26], fill=BK)
    # strong beak
    d.polygon([(10, 18), (2, 18), (2, 20), (10, 22)], fill=DGY)
    # eye
    d.ellipse([12, 16, 16, 20], fill=WH)
    d.ellipse([13, 17, 15, 19], fill=BK)
    # tail feathers
    d.polygon([(36, 26), (48, 24), (48, 32), (36, 32)], fill=BK)
    # legs
    d.line([24, 36, 22, 44], fill=DGY, width=2)
    d.line([30, 36, 30, 44], fill=DGY, width=2)
    d.line([22, 44, 18, 46], fill=DGY, width=1)
    d.line([22, 44, 24, 46], fill=DGY, width=1)
    d.line([30, 44, 28, 46], fill=DGY, width=1)
    d.line([30, 44, 32, 46], fill=DGY, width=1)

def draw_firefly(d):
    """Firefly: dark brown body, glowing yellow-green abdomen, wings."""
    d.ellipse([18, 22, 32, 36], fill=DBRN)          # body
    # glowing abdomen
    d.ellipse([20, 32, 30, 42], fill=YELL)
    d.ellipse([22, 34, 28, 40], fill=(200, 255, 100, 255))  # bright glow center
    # head
    d.ellipse([20, 14, 30, 24], fill=DBRN)
    d.ellipse([22, 16, 24, 18], fill=BK)            # eye L
    d.ellipse([26, 16, 28, 18], fill=BK)            # eye R
    # antennae
    d.line([23, 14, 18, 8], fill=DBRN, width=1)
    d.line([27, 14, 32, 8], fill=DBRN, width=1)
    # wings (translucent look)
    d.ellipse([6, 20, 20, 34], fill=LBLU)
    d.ellipse([30, 20, 44, 34], fill=LBLU)
    # legs
    d.line([20, 30, 14, 36], fill=DBRN, width=1)
    d.line([30, 30, 36, 36], fill=DBRN, width=1)
    d.line([20, 34, 14, 40], fill=DBRN, width=1)
    d.line([30, 34, 36, 40], fill=DBRN, width=1)

def draw_gecko(d):
    """Gecko: bright green, toe pads, big eyes, top-down view."""
    d.ellipse([18, 24, 34, 40], fill=LGRN)          # body
    d.ellipse([20, 26, 32, 38], fill=GRN)           # darker pattern
    # tail
    d.polygon([(24, 40), (28, 40), (26, 50)], fill=LGRN)
    # head (wide, flat)
    d.ellipse([14, 14, 38, 28], fill=LGRN)
    # very large eyes (gecko signature)
    d.ellipse([14, 14, 22, 22], fill=YELL)
    d.ellipse([16, 16, 20, 20], fill=BK)
    d.ellipse([30, 14, 38, 22], fill=YELL)
    d.ellipse([32, 16, 36, 20], fill=BK)
    # mouth line
    d.arc([18, 22, 34, 28], start=0, end=180, fill=DGRN, width=1)
    # 4 legs with toe pads
    d.line([20, 28, 8, 22], fill=GRN, width=3)
    d.line([32, 28, 44, 22], fill=GRN, width=3)
    d.line([20, 36, 8, 42], fill=GRN, width=3)
    d.line([32, 36, 44, 42], fill=GRN, width=3)
    # toe pads (round circles at end of feet)
    for tx, ty in [(6, 20), (46, 20), (6, 42), (46, 42)]:
        d.ellipse([tx-2, ty-2, tx+2, ty+2], fill=LGRN)

def draw_lemur(d):
    """Lemur: grey body, black/white ringed tail, big eyes."""
    d.ellipse([12, 26, 36, 44], fill=MGY)           # body
    d.ellipse([14, 30, 34, 42], fill=LGY)           # belly
    # ringed tail (black and white stripes, curving up)
    d.arc([32, 10, 50, 30], start=250, end=90, fill=WH, width=5)
    for i, y_pos in enumerate(range(12, 28, 3)):
        c = BK if i % 2 == 0 else WH
        d.rectangle([40, y_pos, 46, y_pos+2], fill=c)
    # head
    d.ellipse([10, 14, 30, 30], fill=MGY)
    # huge round eyes (lemur signature)
    d.ellipse([11, 17, 19, 25], fill=YELL)
    d.ellipse([13, 19, 17, 23], fill=BK)
    d.ellipse([21, 17, 29, 25], fill=YELL)
    d.ellipse([23, 19, 27, 23], fill=BK)
    # nose
    d.ellipse([17, 25, 23, 28], fill=BK)
    # ears
    d.ellipse([8, 12, 14, 18], fill=MGY)
    d.ellipse([26, 12, 32, 18], fill=MGY)
    # legs
    for x in [16, 22, 28, 32]:
        d.rectangle([x, 42, x+3, 48], fill=DGY)

def draw_pangolin(d):
    """Pangolin: armored scales, curled posture, long snout."""
    d.ellipse([12, 22, 42, 44], fill=BRN)           # body
    # overlapping scales
    for row, y in enumerate(range(24, 44, 4)):
        for col in range(5):
            x = 14 + col * 6 + (row % 2) * 3
            if x < 42:
                d.polygon([(x, y), (x+3, y-2), (x+6, y), (x+3, y+3)], fill=DBRN)
    # lighter belly
    d.ellipse([16, 34, 38, 44], fill=LBRN)
    # pointed head and snout
    d.ellipse([4, 24, 18, 34], fill=BRN)
    d.polygon([(4, 28), (0, 28), (0, 30), (4, 30)], fill=LBRN)  # snout
    # eye
    d.ellipse([6, 26, 10, 30], fill=BK)
    # curling tail
    d.arc([34, 14, 50, 30], start=200, end=360, fill=DBRN, width=5)
    # small legs
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 42, x+3, 48], fill=DGY)

def draw_salamander(d):
    """Salamander: bright orange/yellow with black spots, long tail."""
    d.ellipse([16, 24, 38, 38], fill=ORNG)          # body
    d.ellipse([18, 26, 36, 36], fill=YELL)          # belly
    # distinctive black spots
    for x, y in [(20, 26), (28, 25), (24, 30), (32, 30), (22, 34)]:
        d.ellipse([x, y, x+3, y+3], fill=BK)
    # long tail
    d.polygon([(36, 28), (48, 26), (50, 30), (36, 34)], fill=ORNG)
    d.ellipse([44, 28, 48, 32], fill=YELL)          # tail spot
    # head
    d.ellipse([8, 18, 24, 32], fill=ORNG)
    d.ellipse([8, 24, 16, 30], fill=YELL)           # jaw
    # big round eyes
    d.ellipse([10, 20, 15, 25], fill=BK)
    d.ellipse([11, 21, 14, 24], fill=YELL)
    d.ellipse([12, 22, 13, 23], fill=BK)
    # legs (splayed)
    d.line([20, 36, 14, 44], fill=ORNG, width=3)
    d.line([28, 37, 26, 45], fill=ORNG, width=3)
    d.line([32, 36, 38, 44], fill=ORNG, width=3)

def draw_seahorse(d):
    """Seahorse: curled tail, spiny, horse-like head, orange/yellow."""
    # horse-shaped head
    d.ellipse([16, 6, 32, 20], fill=ORNG)
    # long tubular snout
    d.polygon([(16, 12), (8, 12), (8, 14), (16, 16)], fill=YELL)
    # eye
    d.ellipse([20, 8, 24, 12], fill=BK)
    # crown/coronet
    d.polygon([(24, 6), (26, 2), (28, 6)], fill=ORNG)
    d.polygon([(28, 6), (30, 2), (32, 6)], fill=YELL)
    # body (segmented, curving)
    d.arc([14, 16, 34, 40], start=270, end=90, fill=ORNG, width=7)
    # belly ridges
    for y in range(20, 38, 3):
        d.line([20, y, 26, y], fill=YELL, width=1)
    # curling tail
    d.arc([18, 34, 38, 48], start=90, end=270, fill=ORNG, width=5)
    d.arc([24, 42, 36, 50], start=90, end=270, fill=YELL, width=3)
    # dorsal fin
    d.polygon([(32, 18), (38, 14), (34, 24)], fill=YELL)

def draw_starfish(d):
    """Starfish: 5-pointed star, orange/red with texture dots."""
    cx, cy = 25, 26
    pts = []
    for i in range(5):
        a = math.radians(i * 72 - 90)
        pts.append((int(cx + 18 * math.cos(a)), int(cy + 18 * math.sin(a))))
        a2 = math.radians(i * 72 + 36 - 90)
        pts.append((int(cx + 8 * math.cos(a2)), int(cy + 8 * math.sin(a2))))
    d.polygon(pts, fill=ORNG)
    # lighter center disk
    d.ellipse([20, 22, 30, 32], fill=YELL)
    # texture bumps on each arm
    for i in range(5):
        a = math.radians(i * 72 - 90)
        tx = int(cx + 12 * math.cos(a))
        ty = int(cy + 12 * math.sin(a))
        d.ellipse([tx-1, ty-1, tx+1, ty+1], fill=RED)
        tx2 = int(cx + 8 * math.cos(a))
        ty2 = int(cy + 8 * math.sin(a))
        d.ellipse([tx2-1, ty2-1, tx2+1, ty2+1], fill=DRED)
    # tiny sucker dots along arms
    for i in range(5):
        a = math.radians(i * 72 - 90)
        for dist in [6, 14]:
            sx = int(cx + dist * math.cos(a))
            sy = int(cy + dist * math.sin(a))
            d.point((sx, sy), fill=LBRN)

def draw_stingray(d):
    """Stingray: flat diamond shape, long whip tail, spots."""
    # flat diamond body
    d.polygon([(25, 12), (8, 28), (25, 40), (42, 28)], fill=DGY)
    d.polygon([(25, 16), (12, 28), (25, 36), (38, 28)], fill=MGY)  # inner
    # spots pattern
    for x, y in [(20, 22), (30, 22), (25, 28), (18, 30), (32, 30)]:
        d.ellipse([x, y, x+3, y+3], fill=LGY)
    # eyes
    d.ellipse([20, 20, 24, 24], fill=BK)
    d.ellipse([28, 20, 32, 24], fill=BK)
    # long whip tail
    d.line([25, 40, 25, 50], fill=DGY, width=2)
    d.line([25, 50, 23, 48], fill=DGY, width=1)
    # barb
    d.polygon([(24, 44), (26, 44), (25, 48)], fill=BK)
    # mouth (underside)
    d.arc([20, 30, 30, 36], start=0, end=180, fill=WH, width=1)

def draw_tapir(d):
    """Tapir: dark body, white mid-section pattern, flexible snout."""
    d.ellipse([12, 26, 44, 46], fill=BK)            # body
    # white saddle/blanket marking
    d.ellipse([18, 28, 38, 42], fill=WH)
    # head
    d.ellipse([4, 18, 22, 32], fill=DGY)
    # flexible prehensile snout
    d.polygon([(4, 24), (0, 22), (0, 28), (4, 28)], fill=DGY)
    d.ellipse([0, 24, 4, 28], fill=BRN)
    # eye
    d.ellipse([8, 20, 12, 24], fill=BK)
    d.ellipse([9, 21, 11, 23], fill=WH)
    # ears (rounded)
    d.ellipse([14, 14, 20, 20], fill=DGY)
    d.ellipse([15, 15, 19, 19], fill=MGY)
    # legs
    for x in [16, 24, 32, 38]:
        d.rectangle([x, 44, x+3, 50], fill=BK)

# ===========================================================================
# ADDITIONAL IMPROVEMENTS for images that look odd or need detail
# These animals had existing art but were part of the "improve" list
# ===========================================================================

def draw_stingray_v2(d): draw_stingray(d)
def draw_jellyfish(d):
    """Jellyfish: translucent bell, flowing tentacles, purple."""
    # bell (dome shape)
    d.ellipse([10, 8, 40, 28], fill=(190, 140, 220, 255))
    d.ellipse([12, 10, 38, 26], fill=(220, 180, 245, 255))  # highlight
    d.ellipse([16, 12, 34, 22], fill=(240, 210, 255, 255))  # inner glow
    # oral arms (thick central tentacles)
    d.line([20, 28, 18, 42], fill=(180, 120, 200, 255), width=3)
    d.line([30, 28, 32, 42], fill=(180, 120, 200, 255), width=3)
    # flowing thin tentacles
    for x in [12, 16, 24, 28, 34, 38]:
        d.arc([x-2, 28, x+4, 48], start=0, end=180, fill=(160, 100, 190, 255), width=1)
    # eyes (simple dots)
    d.ellipse([18, 16, 22, 20], fill=(100, 50, 120, 255))
    d.ellipse([28, 16, 32, 20], fill=(100, 50, 120, 255))

def draw_cuttlefish(d):
    """Cuttlefish: W-shaped pupil, fins along body, many tentacles."""
    d.ellipse([12, 18, 40, 38], fill=(100, 150, 190, 255))
    d.ellipse([14, 20, 38, 36], fill=(140, 180, 210, 255))  # lighter
    # color-changing stripes
    for y in [22, 26, 30, 34]:
        d.line([14, y, 38, y], fill=(80, 120, 170, 255), width=1)
    # undulating fins along sides
    d.ellipse([8, 20, 16, 36], fill=(120, 160, 200, 255))
    d.ellipse([36, 20, 44, 36], fill=(120, 160, 200, 255))
    # W-shaped pupils in large eyes
    d.ellipse([16, 20, 24, 28], fill=WH)
    d.ellipse([18, 22, 22, 26], fill=BK)
    d.ellipse([28, 20, 36, 28], fill=WH)
    d.ellipse([30, 22, 34, 26], fill=BK)
    # tentacles (8 short + 2 long)
    for x in [14, 18, 22, 26, 30, 34]:
        d.line([x, 38, x - 1, 46], fill=(80, 120, 170, 255), width=2)
    # two long feeding tentacles
    d.line([20, 38, 16, 50], fill=(100, 140, 180, 255), width=2)
    d.line([32, 38, 36, 50], fill=(100, 140, 180, 255), width=2)

def draw_eel(d):
    """Eel: long snaking body, green, open mouth."""
    # wavy snake-like body
    d.arc([8, 8, 28, 28], start=90, end=270, fill=GRN, width=7)
    d.arc([18, 18, 38, 38], start=270, end=90, fill=GRN, width=7)
    d.arc([8, 28, 28, 48], start=90, end=270, fill=GRN, width=7)
    # lighter belly on curves
    d.arc([10, 10, 26, 26], start=90, end=270, fill=LGRN, width=3)
    d.arc([20, 20, 36, 36], start=270, end=90, fill=LGRN, width=3)
    # head
    d.ellipse([6, 6, 22, 18], fill=GRN)
    d.ellipse([8, 8, 20, 16], fill=LGRN)
    # eye
    d.ellipse([8, 8, 12, 12], fill=YELL)
    d.ellipse([9, 9, 11, 11], fill=BK)
    # open mouth with teeth
    d.polygon([(6, 14), (0, 16), (6, 18)], fill=DGRN)
    d.rectangle([2, 14, 4, 16], fill=WH)
    d.rectangle([2, 16, 4, 18], fill=WH)

def draw_komodo_dragon(d):
    """Komodo dragon: large, muscular, forked tongue, grey-green."""
    d.ellipse([12, 24, 44, 42], fill=DGY)           # body
    d.ellipse([14, 28, 42, 40], fill=MGY)           # lighter belly
    # muscular texture bumps
    for x, y in [(18, 26), (26, 25), (34, 26)]:
        d.ellipse([x, y, x+4, y+4], fill=(90, 90, 80, 255))
    # heavy tail
    d.polygon([(42, 30), (50, 32), (50, 38), (42, 38)], fill=DGY)
    # broad head
    d.ellipse([2, 22, 20, 36], fill=DGY)
    d.ellipse([2, 26, 12, 34], fill=MGY)            # jaw
    # yellow eye
    d.ellipse([4, 24, 9, 29], fill=YELL)
    d.ellipse([5, 25, 8, 28], fill=BK)
    # forked tongue (red, sticking far out)
    d.line([2, 30, 0, 28], fill=RED, width=1)
    d.line([2, 30, 0, 32], fill=RED, width=1)
    # powerful legs
    d.line([18, 40, 14, 48], fill=DGY, width=3)
    d.line([28, 41, 26, 49], fill=DGY, width=3)
    d.line([34, 40, 38, 48], fill=DGY, width=3)
    # claws
    d.line([14, 48, 12, 50], fill=BK, width=1)
    d.line([26, 49, 24, 50], fill=BK, width=1)

def draw_toad(d):
    """Toad: warty, wide flat body, big bulging eyes, olive green."""
    d.ellipse([10, 24, 42, 44], fill=(90, 130, 70, 255))  # body
    d.ellipse([12, 28, 40, 42], fill=(130, 170, 100, 255))  # belly
    # wart bumps
    for x, y in [(16, 26), (24, 25), (32, 26), (20, 30), (30, 30), (18, 36), (28, 36)]:
        d.ellipse([x, y, x+3, y+3], fill=(70, 110, 55, 255))
    # broad head
    d.ellipse([10, 14, 42, 30], fill=(90, 130, 70, 255))
    # very big eyes on top (toad signature)
    d.ellipse([11, 11, 21, 21], fill=YELL)
    d.ellipse([14, 14, 18, 18], fill=BK)
    d.ellipse([31, 11, 41, 21], fill=YELL)
    d.ellipse([34, 14, 38, 18], fill=BK)
    # wide mouth
    d.arc([14, 24, 38, 34], start=0, end=180, fill=DGRN, width=2)
    # hind legs (large, webbed)
    d.polygon([(10, 38), (2, 46), (14, 48)], fill=(80, 120, 60, 255))
    d.polygon([(42, 38), (50, 46), (38, 48)], fill=(80, 120, 60, 255))

def draw_dragonfly(d):
    """Dragonfly: long segmented abdomen, 4 wings, big compound eyes."""
    # long segmented abdomen
    d.line([25, 18, 25, 44], fill=BLU, width=4)
    # segment lines
    for y in range(22, 44, 3):
        d.line([23, y, 27, y], fill=NAVY, width=1)
    # thorax
    d.ellipse([21, 14, 29, 22], fill=TEAL)
    # 4 large wings
    d.ellipse([4, 10, 23, 22], fill=LBLU)
    d.ellipse([4, 20, 23, 32], fill=LBLU)
    d.ellipse([27, 10, 46, 22], fill=LBLU)
    d.ellipse([27, 20, 46, 32], fill=LBLU)
    # wing veins
    d.line([8, 16, 20, 16], fill=MGY, width=1)
    d.line([8, 26, 20, 26], fill=MGY, width=1)
    d.line([30, 16, 42, 16], fill=MGY, width=1)
    d.line([30, 26, 42, 26], fill=MGY, width=1)
    # head + huge compound eyes
    d.ellipse([20, 6, 30, 16], fill=TEAL)
    d.ellipse([17, 6, 25, 14], fill=BLU)            # eye L
    d.ellipse([25, 6, 33, 14], fill=BLU)            # eye R
    # tail tip
    d.polygon([(23, 44), (27, 44), (25, 48)], fill=NAVY)

def draw_grasshopper(d):
    """Grasshopper: large hind legs, green body, prominent eyes."""
    d.ellipse([16, 26, 40, 42], fill=GRN)           # body
    d.ellipse([18, 28, 38, 40], fill=LGRN)          # belly
    # head
    d.ellipse([6, 20, 22, 32], fill=GRN)
    # large compound eye
    d.ellipse([8, 20, 14, 26], fill=DGRN)
    d.ellipse([9, 21, 13, 25], fill=BK)
    # antennae
    d.line([14, 20, 6, 10], fill=DGRN, width=1)
    d.line([18, 20, 14, 10], fill=DGRN, width=1)
    # large powerful hind legs (Z-shaped)
    d.polygon([(24, 34), (14, 24), (10, 34)], fill=DGRN)
    d.line([10, 34, 8, 44], fill=DGRN, width=2)
    d.polygon([(36, 34), (46, 24), (48, 34)], fill=DGRN)
    d.line([48, 34, 46, 44], fill=DGRN, width=2)
    # front/middle legs
    d.line([18, 34, 12, 40], fill=DGRN, width=2)
    d.line([24, 34, 20, 40], fill=DGRN, width=2)
    d.line([30, 34, 34, 40], fill=DGRN, width=2)
    # wings
    d.ellipse([22, 22, 40, 34], fill=(180, 220, 160, 200))

def draw_mantis(d):
    """Praying mantis: triangular head, raptorial forelegs, slender."""
    d.rectangle([22, 24, 28, 42], fill=GRN)         # slender abdomen
    d.ellipse([20, 18, 30, 26], fill=LGRN)          # thorax
    # raptorial forelegs (praying position)
    d.polygon([(20, 20), (10, 10), (12, 22)], fill=GRN)
    d.polygon([(30, 20), (40, 10), (38, 22)], fill=GRN)
    # spines on forelegs
    d.line([10, 10, 6, 14], fill=DGRN, width=2)
    d.line([40, 10, 44, 14], fill=DGRN, width=2)
    # triangular head (can rotate)
    d.polygon([(19, 8), (31, 8), (25, 18)], fill=GRN)
    # large compound eyes on corners
    d.ellipse([17, 6, 23, 12], fill=YELL)
    d.ellipse([18, 7, 22, 11], fill=BK)
    d.ellipse([27, 6, 33, 12], fill=YELL)
    d.ellipse([28, 7, 32, 11], fill=BK)
    # antennae
    d.line([21, 8, 16, 2], fill=DGRN, width=1)
    d.line([29, 8, 34, 2], fill=DGRN, width=1)
    # hind wings (folded)
    d.ellipse([18, 26, 32, 40], fill=(160, 220, 140, 180))
    # walking legs
    d.line([22, 30, 14, 36], fill=DGRN, width=1)
    d.line([28, 30, 36, 36], fill=DGRN, width=1)

def draw_echidna(d):
    """Echidna: spines on back, long beak-like snout, small eyes."""
    d.ellipse([10, 22, 42, 44], fill=DBRN)          # body
    d.ellipse([12, 28, 40, 42], fill=BRN)           # belly
    # spines (top half only)
    for x in range(14, 42, 2):
        d.line([x, 24, x-1, 16], fill=YELL, width=1)
        d.line([x+1, 24, x, 14], fill=LGY, width=1)
    # small round head
    d.ellipse([4, 26, 18, 36], fill=BRN)
    # very long beak-like snout
    d.line([4, 32, 0, 32], fill=BRN, width=3)
    d.ellipse([0, 30, 4, 34], fill=DBRN)
    # tiny eye
    d.ellipse([8, 28, 11, 31], fill=BK)
    # short strong digging legs
    for x in [14, 22, 28, 34]:
        d.rectangle([x, 42, x+3, 48], fill=DBRN)
    # claws
    d.line([14, 48, 12, 50], fill=BK, width=1)
    d.line([22, 48, 20, 50], fill=BK, width=1)

def draw_mole(d):
    """Mole: dark velvety body, huge digging hands, tiny eyes."""
    d.ellipse([12, 24, 40, 44], fill=DGY)           # body
    d.ellipse([14, 28, 38, 42], fill=MGY)           # belly
    # very large pink digging hands (mole signature)
    d.ellipse([6, 30, 16, 42], fill=PINK)
    d.ellipse([34, 30, 44, 42], fill=PINK)
    # finger/claw details
    for dx in [8, 10, 12, 14]:
        d.line([dx, 30, dx-2, 26], fill=LBRN, width=1)
    for dx in [36, 38, 40, 42]:
        d.line([dx, 30, dx+2, 26], fill=LBRN, width=1)
    # head
    d.ellipse([16, 18, 34, 32], fill=DGY)
    # pink star-shaped nose
    d.ellipse([20, 26, 30, 32], fill=PINK)
    d.ellipse([22, 24, 28, 28], fill=LPNK)
    # very tiny eyes (nearly invisible)
    d.ellipse([18, 22, 20, 24], fill=BK)
    d.ellipse([30, 22, 32, 24], fill=BK)

def draw_mongoose(d):
    """Mongoose: sleek brown, long body, alert stance."""
    d.ellipse([10, 26, 42, 42], fill=BRN)           # body
    d.ellipse([12, 28, 40, 40], fill=LBRN)          # belly
    # head (alert, pointed)
    d.ellipse([4, 18, 24, 30], fill=BRN)
    d.ellipse([4, 22, 14, 30], fill=LBRN)           # muzzle
    # bright alert eyes
    d.ellipse([8, 20, 12, 24], fill=YELL)
    d.ellipse([9, 21, 11, 23], fill=BK)
    # pink nose
    d.ellipse([6, 26, 10, 29], fill=PINK)
    # ears (round)
    d.ellipse([16, 16, 20, 20], fill=BRN)
    d.ellipse([20, 15, 24, 19], fill=BRN)
    # slender long tail
    d.line([42, 34, 50, 30], fill=BRN, width=3)
    d.line([50, 30, 50, 26], fill=DBRN, width=2)   # dark tail tip
    # legs
    for x in [14, 22, 30, 36]:
        d.rectangle([x, 40, x+3, 46], fill=DBRN)

def draw_meerkat(d):
    """Meerkat: upright sentry stance, tan, dark eye patches."""
    d.ellipse([18, 28, 34, 46], fill=LBRN)          # body
    d.ellipse([20, 32, 32, 44], fill=(240, 220, 180, 255))  # cream belly
    # neck
    d.rectangle([20, 22, 30, 30], fill=LBRN)
    # head
    d.ellipse([16, 14, 36, 28], fill=LBRN)
    # dark eye patches (meerkat signature)
    d.ellipse([17, 18, 23, 24], fill=DBRN)
    d.ellipse([29, 18, 35, 24], fill=DBRN)
    d.ellipse([18, 19, 22, 23], fill=WH)
    d.ellipse([30, 19, 34, 23], fill=WH)
    d.ellipse([19, 20, 21, 22], fill=BK)
    d.ellipse([31, 20, 33, 22], fill=BK)
    # ears (small, round)
    d.ellipse([14, 12, 18, 17], fill=BRN)
    d.ellipse([34, 12, 38, 17], fill=BRN)
    # nose
    d.ellipse([23, 24, 29, 28], fill=BK)
    # arms
    d.rectangle([12, 30, 20, 36], fill=LBRN)
    d.rectangle([32, 30, 40, 36], fill=LBRN)
    # legs
    d.rectangle([20, 44, 24, 50], fill=BRN)
    d.rectangle([28, 44, 32, 50], fill=BRN)

def draw_anteater(d):
    """Anteater: very long snout, bushy tail, grey body."""
    d.ellipse([14, 24, 42, 42], fill=MGY)           # body
    d.ellipse([16, 28, 40, 40], fill=LGY)           # belly
    # very long tube-like snout
    d.polygon([(12, 28), (0, 24), (0, 30)], fill=MGY)
    d.line([0, 26, 0, 28], fill=BK, width=1)        # mouth opening
    # head
    d.ellipse([8, 20, 24, 32], fill=MGY)
    d.ellipse([10, 22, 14, 26], fill=BK)            # eye
    # small ear
    d.ellipse([18, 18, 22, 22], fill=DGY)
    # bushy tail
    d.ellipse([38, 20, 50, 38], fill=DGY)
    d.ellipse([40, 22, 50, 36], fill=MGY)
    # legs with claws
    for x in [18, 24, 30, 36]:
        d.rectangle([x, 40, x+3, 47], fill=DGY)
    d.line([18, 47, 16, 50], fill=BK, width=1)
    d.line([24, 47, 22, 50], fill=BK, width=1)

def draw_pangolin_v2(d): draw_pangolin(d)

def draw_okapi(d):
    """Okapi: reddish body, zebra-striped legs, giraffe-like head."""
    d.ellipse([14, 28, 42, 46], fill=(160, 80, 40, 255))
    # zebra stripes on rump and legs
    for y in [36, 40, 44]:
        d.line([30, y, 42, y], fill=WH, width=2)
    d.line([30, 38, 42, 38], fill=BK, width=1)
    d.line([30, 42, 42, 42], fill=BK, width=1)
    # neck
    d.rectangle([12, 16, 22, 32], fill=(160, 80, 40, 255))
    # giraffe-like head
    d.ellipse([6, 10, 24, 24], fill=(160, 80, 40, 255))
    # ossicones (short horns with fur)
    d.line([14, 10, 12, 4], fill=BRN, width=2)
    d.line([20, 10, 22, 4], fill=BRN, width=2)
    d.ellipse([11, 2, 14, 6], fill=BRN)
    d.ellipse([21, 2, 24, 6], fill=BRN)
    # big dark eye
    d.ellipse([8, 14, 13, 19], fill=BK)
    d.ellipse([9, 15, 11, 17], fill=WH)
    # pale muzzle
    d.ellipse([6, 18, 14, 24], fill=LBRN)
    # striped legs
    for x in [16, 22, 30, 36]:
        d.rectangle([x, 44, x+3, 50], fill=WH)
        d.line([x, 46, x+3, 46], fill=BK, width=1)
        d.line([x, 48, x+3, 48], fill=BK, width=1)

def draw_hyena(d):
    """Hyena: spotted, sloping back, large head, rounded ears."""
    d.ellipse([12, 26, 42, 44], fill=BRN)           # body
    d.ellipse([14, 28, 40, 42], fill=LBRN)          # belly
    # spots
    for x, y in [(16, 28), (24, 27), (32, 28), (20, 34), (30, 34)]:
        d.ellipse([x, y, x+3, y+3], fill=DBRN)
    # sloping back (front higher than rear)
    d.polygon([(12, 26), (28, 26), (42, 32), (42, 36)], fill=BRN)
    # dark mane along spine
    d.line([14, 26, 28, 26], fill=DBRN, width=2)
    # big powerful head
    d.ellipse([4, 18, 26, 32], fill=BRN)
    d.ellipse([4, 24, 16, 32], fill=LBRN)           # muzzle
    # round ears
    d.ellipse([14, 14, 20, 20], fill=BRN)
    d.ellipse([15, 15, 19, 19], fill=DBRN)
    d.ellipse([20, 13, 26, 19], fill=BRN)
    d.ellipse([21, 14, 25, 18], fill=DBRN)
    # eye
    d.ellipse([8, 20, 12, 24], fill=BK)
    # nose
    d.ellipse([6, 28, 10, 32], fill=BK)
    # legs (front longer)
    d.rectangle([16, 42, 19, 50], fill=BRN)
    d.rectangle([22, 42, 25, 50], fill=BRN)
    d.rectangle([30, 40, 33, 50], fill=BRN)
    d.rectangle([36, 40, 39, 50], fill=BRN)

def draw_bandicoot(d):
    """Bandicoot: pointed snout, large hind feet, brown."""
    d.ellipse([14, 24, 40, 44], fill=BRN)           # body
    d.ellipse([16, 28, 38, 42], fill=LBRN)          # belly
    # long pointed head/snout
    d.polygon([(14, 30), (2, 24), (4, 36)], fill=BRN)
    d.ellipse([2, 22, 18, 34], fill=BRN)
    # pink nose
    d.ellipse([2, 27, 6, 31], fill=PINK)
    # eye
    d.ellipse([8, 24, 12, 28], fill=BK)
    d.ellipse([9, 25, 11, 27], fill=WH)
    # big pointed ears
    d.polygon([(14, 24), (12, 14), (18, 24)], fill=BRN)
    d.polygon([(13, 22), (13, 16), (16, 22)], fill=PINK)
    d.polygon([(20, 24), (20, 14), (26, 24)], fill=BRN)
    d.polygon([(21, 22), (21, 16), (24, 22)], fill=PINK)
    # large hind feet
    d.rectangle([28, 40, 34, 50], fill=DBRN)
    d.rectangle([34, 40, 40, 50], fill=DBRN)
    # small front paws
    d.rectangle([16, 40, 20, 46], fill=BRN)
    # tail
    d.line([40, 36, 48, 32], fill=DBRN, width=3)

def draw_gopher(d):
    """Gopher: chubby cheek pouches, big front teeth, burrower."""
    d.ellipse([12, 24, 40, 46], fill=BRN)           # body
    d.ellipse([14, 28, 38, 44], fill=LBRN)          # belly
    # head
    d.ellipse([10, 16, 32, 30], fill=BRN)
    # big cheek pouches
    d.ellipse([6, 20, 16, 28], fill=LBRN)
    d.ellipse([26, 20, 36, 28], fill=LBRN)
    # eyes
    d.ellipse([12, 18, 16, 22], fill=BK)
    d.ellipse([22, 18, 26, 22], fill=BK)
    # pink nose
    d.ellipse([17, 22, 21, 25], fill=PINK)
    # prominent front teeth
    d.rectangle([17, 26, 19, 30], fill=WH)
    d.rectangle([20, 26, 22, 30], fill=WH)
    # small rounded ears
    d.ellipse([20, 14, 24, 18], fill=BRN)
    d.ellipse([26, 13, 30, 17], fill=BRN)
    # short digging claws
    d.rectangle([14, 42, 18, 48], fill=DBRN)
    d.rectangle([26, 42, 30, 48], fill=DBRN)
    d.line([14, 48, 12, 50], fill=BK, width=1)

def draw_groundhog(d):
    """Groundhog: chunky, upright lookout pose, brown."""
    d.ellipse([14, 26, 38, 48], fill=DBRN)          # body
    d.ellipse([16, 30, 36, 46], fill=BRN)           # belly
    # upright neck
    d.rectangle([18, 18, 32, 30], fill=DBRN)
    # head
    d.ellipse([12, 12, 36, 26], fill=DBRN)
    d.ellipse([14, 18, 26, 26], fill=BRN)           # muzzle
    # eye
    d.ellipse([14, 16, 18, 20], fill=BK)
    d.ellipse([15, 17, 17, 19], fill=WH)
    # nose
    d.ellipse([14, 22, 18, 25], fill=BK)
    # small ears
    d.ellipse([10, 10, 16, 16], fill=DBRN)
    d.ellipse([28, 10, 34, 16], fill=DBRN)
    # front paws (held up in lookout)
    d.rectangle([12, 30, 18, 38], fill=BRN)
    d.rectangle([32, 30, 38, 38], fill=BRN)
    # legs
    d.rectangle([18, 44, 24, 50], fill=DBRN)
    d.rectangle([28, 44, 34, 50], fill=DBRN)

def draw_prairie_dog(d):
    """Prairie dog: light tan, upright sentry, smaller than groundhog."""
    d.ellipse([16, 28, 36, 48], fill=LBRN)          # body
    d.ellipse([18, 32, 34, 46], fill=(240, 220, 180, 255))  # pale belly
    # neck
    d.rectangle([20, 22, 30, 30], fill=LBRN)
    # head (round)
    d.ellipse([14, 12, 36, 26], fill=LBRN)
    d.ellipse([16, 18, 26, 26], fill=(240, 220, 180, 255))  # muzzle
    # eye
    d.ellipse([16, 16, 20, 20], fill=BK)
    d.ellipse([28, 16, 32, 20], fill=BK)
    # nose
    d.ellipse([20, 22, 24, 25], fill=PINK)
    # small ears
    d.ellipse([12, 12, 16, 16], fill=BRN)
    d.ellipse([34, 12, 38, 16], fill=BRN)
    # arms (held together)
    d.rectangle([14, 32, 18, 40], fill=BRN)
    d.rectangle([34, 32, 38, 40], fill=BRN)
    # hind legs
    d.rectangle([20, 46, 24, 50], fill=BRN)
    d.rectangle([28, 46, 32, 50], fill=BRN)
    # short tail
    d.line([34, 40, 40, 38], fill=BRN, width=2)

def draw_wombat(d):
    """Wombat: chunky bear-like body, wide flat nose, dark."""
    d.ellipse([10, 26, 42, 48], fill=DGY)           # body
    d.ellipse([12, 30, 40, 46], fill=MGY)           # belly
    # broad head
    d.ellipse([8, 16, 34, 30], fill=DGY)
    d.ellipse([10, 22, 22, 30], fill=MGY)           # face
    # small rounded ears
    d.ellipse([10, 12, 16, 18], fill=DGY)
    d.ellipse([11, 13, 15, 17], fill=PINK)
    d.ellipse([26, 12, 32, 18], fill=DGY)
    d.ellipse([27, 13, 31, 17], fill=PINK)
    # eyes
    d.ellipse([12, 20, 16, 24], fill=BK)
    d.ellipse([13, 21, 15, 23], fill=WH)
    d.ellipse([22, 20, 26, 24], fill=BK)
    # broad flat nose (wombat signature)
    d.ellipse([14, 24, 22, 28], fill=BRN)
    d.ellipse([15, 25, 21, 27], fill=BK)
    # short powerful legs
    for x in [12, 20, 28, 36]:
        d.rectangle([x, 46, x+4, 50], fill=DBRN)

def draw_quokka(d):
    """Quokka: small happy marsupial, round face, big smile."""
    d.ellipse([14, 28, 38, 46], fill=BRN)           # body
    d.ellipse([16, 32, 36, 44], fill=LBRN)          # belly
    # head (round, happy)
    d.ellipse([12, 14, 36, 30], fill=BRN)
    d.ellipse([14, 20, 24, 28], fill=LBRN)          # muzzle
    # big round ears
    d.ellipse([8, 10, 16, 20], fill=BRN)
    d.ellipse([9, 11, 15, 18], fill=PINK)
    d.ellipse([32, 10, 40, 20], fill=BRN)
    d.ellipse([33, 11, 39, 18], fill=PINK)
    # big happy eyes
    d.ellipse([14, 16, 20, 22], fill=BK)
    d.ellipse([15, 17, 17, 19], fill=WH)            # glint
    d.ellipse([28, 16, 34, 22], fill=BK)
    d.ellipse([29, 17, 31, 19], fill=WH)
    # big smile (quokka is the "happiest animal")
    d.arc([16, 22, 32, 30], start=10, end=170, fill=BK, width=2)
    # nose
    d.ellipse([18, 22, 22, 25], fill=BK)
    # short legs
    d.rectangle([18, 44, 22, 50], fill=DBRN)
    d.rectangle([30, 44, 34, 50], fill=DBRN)
    # tail
    d.line([38, 38, 46, 36], fill=BRN, width=3)

def draw_tasmanian_devil(d):
    """Tasmanian devil: black, white chest patch, big jaws, red ears."""
    d.ellipse([12, 26, 40, 46], fill=BK)            # body
    d.ellipse([14, 30, 38, 44], fill=DGY)           # belly
    # white chest patches
    d.ellipse([18, 32, 30, 42], fill=WH)
    # big head with powerful jaws
    d.ellipse([8, 14, 36, 30], fill=BK)
    d.ellipse([8, 22, 24, 32], fill=DGY)            # muzzle
    # red-tipped ears
    d.ellipse([8, 10, 16, 18], fill=RED)
    d.ellipse([28, 10, 36, 18], fill=RED)
    # eyes
    d.ellipse([12, 16, 16, 20], fill=BK)
    d.ellipse([13, 17, 15, 19], fill=RED)
    d.ellipse([24, 16, 28, 20], fill=BK)
    d.ellipse([25, 17, 27, 19], fill=RED)
    # open mouth showing teeth
    d.arc([12, 24, 28, 32], start=0, end=180, fill=RED, width=2)
    d.rectangle([14, 26, 16, 29], fill=WH)
    d.rectangle([22, 26, 24, 29], fill=WH)
    # short legs
    for x in [14, 22, 28, 34]:
        d.rectangle([x, 44, x+3, 50], fill=BK)

# Additional previously-improved animals that also need the same treatment
def draw_armadillo(d):
    """Armadillo: banded armor shell, small head, long tail."""
    d.ellipse([14, 24, 38, 40], fill=DGY)           # armor body
    d.ellipse([16, 26, 36, 38], fill=MGY)           # lighter bands
    # armor bands
    d.line([20, 24, 20, 40], fill=DGY, width=1)
    d.line([25, 24, 25, 40], fill=DGY, width=1)
    d.line([30, 24, 30, 40], fill=DGY, width=1)
    # small pointed head
    d.ellipse([8, 24, 20, 32], fill=LBRN)
    d.ellipse([4, 26, 12, 32], fill=LBRN)           # snout
    # eye
    d.ellipse([10, 25, 13, 28], fill=BK)
    # ears
    d.ellipse([16, 22, 20, 26], fill=LBRN)
    # legs (short)
    for x in [16, 22, 28, 34]:
        d.rectangle([x, 38, x+3, 44], fill=LBRN)
    # long armored tail
    d.line([38, 32, 48, 36], fill=MGY, width=3)

def draw_capybara(d):
    """Capybara: large blocky rodent, brown, blunt snout."""
    d.rounded_rectangle([12, 26, 42, 44], radius=5, fill=BRN)
    d.rounded_rectangle([14, 30, 40, 42], radius=4, fill=LBRN)  # belly
    # big blocky head
    d.rounded_rectangle([6, 18, 26, 32], radius=4, fill=BRN)
    # blunt snout
    d.rounded_rectangle([4, 22, 14, 30], radius=3, fill=LBRN)
    # nostrils
    d.ellipse([6, 24, 8, 26], fill=BK)
    d.ellipse([10, 24, 12, 26], fill=BK)
    # eye
    d.ellipse([14, 20, 18, 24], fill=BK)
    d.ellipse([15, 21, 17, 23], fill=WH)
    # small ears
    d.ellipse([20, 16, 24, 20], fill=BRN)
    # legs (short, stocky)
    for x in [14, 22, 30, 36]:
        d.rectangle([x, 42, x+3, 48], fill=DBRN)

def draw_chameleon(d):
    """Chameleon: curled tail, casque head, color-changing body."""
    d.ellipse([16, 24, 40, 38], fill=GRN)           # body
    d.ellipse([18, 26, 38, 36], fill=LGRN)          # belly stripe
    # curled tail
    d.arc([36, 32, 50, 46], start=220, end=400, fill=GRN, width=4)
    d.arc([40, 38, 50, 48], start=180, end=320, fill=DGRN, width=3)
    # casque-shaped head
    d.polygon([(16, 28), (6, 20), (10, 34)], fill=GRN)
    d.ellipse([2, 18, 18, 30], fill=GRN)
    d.polygon([(10, 18), (8, 12), (14, 18)], fill=DGRN)  # casque crest
    # huge independently-rotating eye
    d.ellipse([4, 18, 12, 26], fill=YELL)
    d.ellipse([6, 20, 10, 24], fill=BK)
    # legs (grasping, 2-toed)
    d.line([22, 38, 18, 46], fill=DGRN, width=3)
    d.line([30, 38, 28, 46], fill=DGRN, width=3)
    d.line([34, 38, 38, 46], fill=DGRN, width=3)

def draw_chimpanzee(d):
    """Chimpanzee: dark brown, expressive face, big ears."""
    d.ellipse([14, 28, 38, 46], fill=DBRN)          # body
    # face (skin-colored center)
    d.ellipse([12, 14, 38, 34], fill=BRN)
    d.ellipse([16, 20, 34, 32], fill=SKIN)          # face
    # big ears
    d.ellipse([8, 18, 16, 26], fill=BRN)
    d.ellipse([9, 19, 15, 25], fill=PINK)
    d.ellipse([34, 18, 42, 26], fill=BRN)
    d.ellipse([35, 19, 41, 25], fill=PINK)
    # eyes
    d.ellipse([18, 22, 23, 27], fill=WH)
    d.ellipse([19, 23, 22, 26], fill=BK)
    d.ellipse([27, 22, 32, 27], fill=WH)
    d.ellipse([28, 23, 31, 26], fill=BK)
    # nose
    d.ellipse([22, 26, 28, 30], fill=SKIN)
    d.ellipse([23, 27, 25, 29], fill=BK)
    d.ellipse([26, 27, 28, 29], fill=BK)
    # mouth
    d.arc([20, 28, 30, 34], start=0, end=180, fill=BK, width=1)
    # arms
    d.rectangle([8, 32, 16, 44], fill=DBRN)
    d.rectangle([34, 32, 42, 44], fill=DBRN)

def draw_donkey(d):
    """Donkey: grey, very long ears, lighter muzzle."""
    d.ellipse([14, 28, 44, 44], fill=MGY)           # body
    # neck
    d.rectangle([12, 18, 22, 32], fill=MGY)
    # head
    d.ellipse([6, 14, 24, 28], fill=MGY)
    # very long ears (donkey signature)
    d.rectangle([8, 4, 12, 18], fill=MGY)
    d.rectangle([9, 5, 11, 16], fill=PINK)
    d.rectangle([16, 2, 20, 16], fill=MGY)
    d.rectangle([17, 3, 19, 14], fill=PINK)
    # lighter muzzle
    d.ellipse([6, 20, 16, 28], fill=LGY)
    # eye
    d.ellipse([10, 16, 14, 20], fill=BK)
    d.ellipse([11, 17, 13, 19], fill=WH)
    # nostril
    d.ellipse([8, 24, 10, 26], fill=DGY)
    # legs
    for x in [18, 24, 32, 38]:
        d.rectangle([x, 42, x+3, 50], fill=DGY)
    # tail with tuft
    d.line([44, 34, 48, 38], fill=DBRN, width=2)
    d.line([48, 38, 48, 44], fill=DBRN, width=3)

def draw_emu(d):
    """Emu: brown feathery body, long neck, tiny wings."""
    d.ellipse([18, 26, 42, 46], fill=DBRN)          # fluffy body
    d.ellipse([20, 28, 40, 44], fill=BRN)           # feather texture
    # long neck
    d.rectangle([14, 10, 22, 30], fill=BRN)
    # small head
    d.ellipse([10, 4, 24, 16], fill=BRN)
    # flat beak
    d.polygon([(10, 8), (4, 10), (10, 12)], fill=DGY)
    # eye (orange-ringed)
    d.ellipse([12, 6, 16, 10], fill=ORNG)
    d.ellipse([13, 7, 15, 9], fill=BK)
    # blue neck skin patch
    d.rectangle([14, 14, 22, 20], fill=LBLU)
    # tiny vestigial wings
    d.ellipse([14, 28, 22, 34], fill=DBRN)
    # very long legs
    d.rectangle([24, 44, 28, 50], fill=DGY)
    d.rectangle([32, 44, 36, 50], fill=DGY)

def draw_falcon(d):
    """Falcon: brown/white, hooked beak, sharp talons."""
    d.ellipse([16, 22, 38, 42], fill=BRN)           # body
    d.ellipse([18, 26, 36, 40], fill=LBRN)          # chest
    # head
    d.ellipse([12, 12, 32, 26], fill=DBRN)
    # helmet-like dark head marking
    d.ellipse([12, 12, 32, 20], fill=BK)
    # eye
    d.ellipse([16, 14, 20, 18], fill=YELL)
    d.ellipse([17, 15, 19, 17], fill=BK)
    # hooked beak
    d.polygon([(12, 18), (6, 16), (8, 20)], fill=YELL)
    # moustache stripe
    d.rectangle([12, 20, 16, 24], fill=BK)
    # wings
    d.polygon([(16, 28), (6, 40), (26, 36)], fill=DBRN)
    d.polygon([(38, 28), (46, 40), (28, 36)], fill=DBRN)
    # tail
    d.polygon([(18, 40), (32, 40), (25, 48)], fill=BRN)
    # talons
    d.line([22, 42, 18, 48], fill=YELL, width=2)
    d.line([28, 42, 28, 48], fill=YELL, width=2)

def draw_ferret(d):
    """Ferret: long slim body, masked face, light body."""
    d.ellipse([10, 26, 44, 38], fill=LBRN)          # long body
    d.ellipse([12, 28, 42, 36], fill=WH)            # lighter belly
    # head
    d.ellipse([4, 18, 22, 30], fill=LBRN)
    # dark mask across eyes (ferret signature)
    d.ellipse([6, 20, 14, 26], fill=DBRN)
    d.ellipse([14, 20, 22, 26], fill=DBRN)
    # eyes in mask
    d.ellipse([8, 21, 11, 24], fill=BK)
    d.ellipse([16, 21, 19, 24], fill=BK)
    # pink nose
    d.ellipse([8, 25, 12, 28], fill=PINK)
    # ears (small round)
    d.ellipse([14, 16, 18, 20], fill=LBRN)
    d.ellipse([18, 15, 22, 19], fill=LBRN)
    # short legs
    for x in [14, 22, 32, 38]:
        d.rectangle([x, 36, x+3, 42], fill=BRN)
    # long tail
    d.line([44, 32, 50, 28], fill=BRN, width=3)

def draw_iguana(d):
    """Iguana: green with dorsal spines, dewlap, long tail."""
    d.ellipse([16, 26, 42, 40], fill=GRN)           # body
    # dorsal spines
    for x in range(18, 40, 3):
        d.polygon([(x, 26), (x+1, 20), (x+2, 26)], fill=DGRN)
    # long tail
    d.polygon([(40, 30), (50, 34), (50, 38), (40, 38)], fill=GRN)
    # head
    d.ellipse([4, 22, 20, 34], fill=GRN)
    # dewlap (hanging throat skin - iguana signature)
    d.polygon([(8, 30), (6, 38), (14, 34)], fill=ORNG)
    # eye with round pupil
    d.ellipse([6, 24, 11, 29], fill=YELL)
    d.ellipse([7, 25, 10, 28], fill=BK)
    # tympanum (ear disc)
    d.ellipse([14, 26, 18, 30], fill=DGRN)
    # legs
    d.line([22, 38, 18, 46], fill=DGRN, width=3)
    d.line([30, 39, 28, 47], fill=DGRN, width=3)
    d.line([34, 38, 38, 46], fill=DGRN, width=3)

def draw_moose(d):
    """Moose: massive palmate antlers, droopy snout, dark brown."""
    d.ellipse([14, 28, 42, 46], fill=DBRN)          # body
    # neck
    d.rectangle([12, 18, 22, 32], fill=DBRN)
    # head
    d.ellipse([6, 16, 24, 30], fill=BRN)
    # large pendulous snout/muzzle
    d.ellipse([4, 22, 16, 32], fill=LBRN)
    d.ellipse([6, 26, 10, 30], fill=BK)             # nostril
    # eye
    d.ellipse([10, 18, 14, 22], fill=BK)
    d.ellipse([11, 19, 13, 21], fill=WH)
    # palmate antlers (broad, flat)
    d.polygon([(12, 16), (4, 4), (10, 16)], fill=LBRN)
    d.polygon([(6, 6), (2, 10), (4, 4)], fill=LBRN)
    d.polygon([(20, 16), (28, 4), (22, 16)], fill=LBRN)
    d.polygon([(26, 6), (30, 10), (28, 4)], fill=LBRN)
    # dewlap (bell)
    d.polygon([(10, 30), (8, 36), (14, 34)], fill=DBRN)
    # legs
    for x in [16, 24, 32, 38]:
        d.rectangle([x, 44, x+3, 50], fill=BRN)

def draw_opossum(d):
    """Opossum: grey, white face, pink nose, prehensile tail."""
    d.ellipse([14, 26, 40, 44], fill=MGY)           # body
    d.ellipse([16, 30, 38, 42], fill=LGY)           # belly
    # pointed white face
    d.ellipse([8, 18, 30, 32], fill=WH)
    d.ellipse([6, 22, 18, 30], fill=WH)             # long snout
    # pink nose
    d.ellipse([6, 24, 10, 28], fill=PINK)
    # dark eye patches
    d.ellipse([12, 20, 18, 26], fill=DGY)
    d.ellipse([22, 20, 28, 26], fill=DGY)
    d.ellipse([13, 21, 17, 25], fill=BK)
    d.ellipse([23, 21, 27, 25], fill=BK)
    # pink ears
    d.ellipse([8, 14, 14, 20], fill=PINK)
    d.ellipse([24, 14, 30, 20], fill=PINK)
    # prehensile tail (curling)
    d.arc([36, 24, 50, 40], start=40, end=300, fill=PINK, width=3)
    # legs
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 42, x+3, 48], fill=MGY)

def draw_platypus(d):
    """Platypus: duck bill, beaver tail, brown body."""
    d.ellipse([12, 26, 42, 40], fill=BRN)           # body
    d.ellipse([14, 28, 40, 38], fill=LBRN)          # belly
    # flat paddle tail
    d.ellipse([38, 32, 50, 42], fill=DBRN)
    # head
    d.ellipse([4, 22, 22, 34], fill=BRN)
    # duck bill (platypus signature)
    d.ellipse([0, 24, 12, 32], fill=DGY)
    d.ellipse([2, 26, 10, 30], fill=MGY)
    # eye
    d.ellipse([10, 24, 14, 28], fill=BK)
    d.ellipse([11, 25, 13, 27], fill=WH)
    # legs (webbed feet)
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 38, x+3, 44], fill=DBRN)
    d.ellipse([14, 42, 20, 46], fill=DGY)
    d.ellipse([28, 42, 34, 46], fill=DGY)

def draw_red_panda(d):
    """Red panda: rusty red, white face markings, ringed tail."""
    d.ellipse([14, 28, 40, 44], fill=RED)           # body
    d.ellipse([16, 30, 38, 42], fill=ORNG)          # belly
    # head
    d.ellipse([10, 14, 34, 30], fill=RED)
    # white face markings
    d.ellipse([12, 20, 20, 28], fill=WH)
    d.ellipse([24, 20, 32, 28], fill=WH)
    # white ear tips
    d.ellipse([10, 10, 16, 16], fill=WH)
    d.ellipse([28, 10, 34, 16], fill=WH)
    d.ellipse([11, 11, 15, 15], fill=RED)
    d.ellipse([29, 11, 33, 15], fill=RED)
    # eyes
    d.ellipse([14, 21, 18, 25], fill=BK)
    d.ellipse([26, 21, 30, 25], fill=BK)
    # nose
    d.ellipse([19, 24, 25, 28], fill=BK)
    # ringed tail
    for i, c in enumerate([RED, ORNG, RED, ORNG]):
        y = 30 + i * 4
        d.rectangle([38, y, 48, y+3], fill=c)
    # legs
    for x in [16, 24, 30, 36]:
        d.rectangle([x, 42, x+3, 48], fill=DBRN)

def draw_walrus(d):
    """Walrus: large grey, prominent tusks, whisker pad."""
    d.ellipse([8, 24, 44, 48], fill=MGY)            # large body
    d.ellipse([10, 28, 42, 46], fill=LGY)           # belly
    # head
    d.ellipse([8, 14, 34, 30], fill=MGY)
    # whisker pad (puffy)
    d.ellipse([8, 24, 28, 34], fill=LGY)
    d.ellipse([10, 26, 16, 30], fill=LBRN)          # whisker dots
    d.ellipse([18, 26, 24, 30], fill=LBRN)
    # tusks (long, white)
    d.polygon([(14, 32), (12, 46), (16, 46)], fill=WH)
    d.polygon([(22, 32), (20, 46), (24, 46)], fill=WH)
    # eye
    d.ellipse([22, 18, 26, 22], fill=BK)
    # flippers
    d.ellipse([4, 38, 14, 48], fill=DGY)
    d.ellipse([38, 38, 48, 48], fill=DGY)

def draw_weasel(d):
    """Weasel: very long thin body, white chin, brown."""
    d.ellipse([6, 26, 46, 38], fill=BRN)            # very long body
    d.ellipse([8, 28, 44, 36], fill=LBRN)           # belly
    # head
    d.ellipse([2, 20, 18, 30], fill=BRN)
    # white chin/throat
    d.ellipse([4, 26, 14, 30], fill=WH)
    # eye
    d.ellipse([6, 22, 10, 26], fill=BK)
    d.ellipse([7, 23, 9, 25], fill=WH)
    # nose
    d.ellipse([2, 24, 6, 28], fill=PINK)
    # ears (tiny)
    d.ellipse([12, 18, 16, 22], fill=BRN)
    d.ellipse([14, 17, 18, 21], fill=BRN)
    # short legs
    for x in [10, 18, 32, 40]:
        d.rectangle([x, 36, x+3, 42], fill=DBRN)
    # long tail
    d.line([46, 32, 50, 28], fill=DBRN, width=3)

def draw_spider(d):
    """Spider: round body, 8 legs, pattern on abdomen."""
    d.ellipse([19, 28, 33, 42], fill=DGY)           # abdomen
    # pattern on abdomen
    d.ellipse([22, 30, 30, 40], fill=MGY)
    d.ellipse([24, 32, 28, 38], fill=BK)
    # cephalothorax
    d.ellipse([21, 20, 31, 30], fill=BK)
    # 4 eyes (front row)
    for ex in [22, 25, 28, 31]:
        d.ellipse([ex, 21, ex+2, 23], fill=RED)
    # 8 legs (4 per side, angled)
    legs_l = [(21, 24, 8, 16), (21, 26, 6, 22), (21, 28, 6, 30), (21, 30, 8, 38)]
    legs_r = [(31, 24, 44, 16), (31, 26, 46, 22), (31, 28, 46, 30), (31, 30, 44, 38)]
    for x1, y1, x2, y2 in legs_l:
        d.line([x1, y1, x2, y2], fill=BK, width=2)
    for x1, y1, x2, y2 in legs_r:
        d.line([x1, y1, x2, y2], fill=BK, width=2)

# ===========================================================================
# Master replacement dict
# ===========================================================================

REPLACEMENTS = {
    # Duplicate fixes (each gets unique art)
    "alligator":        draw_alligator,
    "crocodile":        draw_crocodile,
    "beetle":           draw_beetle,
    "ladybug":          draw_ladybug,
    "beluga":           draw_beluga,
    "narwhal":          draw_narwhal,
    "whale":            draw_whale,
    "bison":            draw_bison,
    "yak":              draw_yak,
    "cheetah":          draw_cheetah,
    "jaguar":           draw_jaguar,
    "leopard":          draw_leopard,
    "panther":          draw_panther,
    "chipmunk":         draw_chipmunk,
    "squirrel":         draw_squirrel,
    "dugong":           draw_dugong,
    "manatee":          draw_manatee,
    "sea_lion":         draw_sea_lion,
    "seal":             draw_seal,
    "goose":            draw_goose,
    "swan":             draw_swan,
    "hedgehog":         draw_hedgehog,
    "porcupine":        draw_porcupine,
    "ostrich":          draw_ostrich,
    "pelican":          draw_pelican,
    "puffin":           draw_puffin,
    # Bland/placeholder fixes (<=3 colors)
    "ant":              draw_ant,
    "camel":            draw_camel,
    "crow":             draw_crow,
    "firefly":          draw_firefly,
    "gecko":            draw_gecko,
    "lemur":            draw_lemur,
    "pangolin":         draw_pangolin,
    "salamander":       draw_salamander,
    "seahorse":         draw_seahorse,
    "starfish":         draw_starfish,
    "stingray":         draw_stingray,
    "tapir":            draw_tapir,
    # Additional improvement targets
    "jellyfish":        draw_jellyfish,
    "cuttlefish":       draw_cuttlefish,
    "eel":              draw_eel,
    "komodo_dragon":    draw_komodo_dragon,
    "toad":             draw_toad,
    "dragonfly":        draw_dragonfly,
    "grasshopper":      draw_grasshopper,
    "mantis":           draw_mantis,
    "echidna":          draw_echidna,
    "mole":             draw_mole,
    "mongoose":         draw_mongoose,
    "meerkat":          draw_meerkat,
    "anteater":         draw_anteater,
    "okapi":            draw_okapi,
    "hyena":            draw_hyena,
    "bandicoot":        draw_bandicoot,
    "gopher":           draw_gopher,
    "groundhog":        draw_groundhog,
    "prairie_dog":      draw_prairie_dog,
    "wombat":           draw_wombat,
    "quokka":           draw_quokka,
    "tasmanian_devil":  draw_tasmanian_devil,
    "armadillo":        draw_armadillo,
    "capybara":         draw_capybara,
    "chameleon":        draw_chameleon,
    "chimpanzee":       draw_chimpanzee,
    "donkey":           draw_donkey,
    "emu":              draw_emu,
    "falcon":           draw_falcon,
    "ferret":           draw_ferret,
    "iguana":           draw_iguana,
    "moose":            draw_moose,
    "opossum":          draw_opossum,
    "platypus":         draw_platypus,
    "red_panda":        draw_red_panda,
    "walrus":           draw_walrus,
    "weasel":           draw_weasel,
    "spider":           draw_spider,
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
    print(f"Step 1/2 — Drawing {len(REPLACEMENTS)} replacement/improved sprites…")
    for name, fn in REPLACEMENTS.items():
        save_sprite(name, fn)
        print(f"  ✓  {name}")

    # 2. Quantize ALL 50x50 images (no outline) for consistency
    all_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png")))
    print(f"\nStep 2/2 — Quantizing {len(all_files)} 50×50 images (no outline)…")
    for f in all_files:
        apply_quantize_no_outline(f)

    # 3. Verify: report color counts and check for duplicates
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

    # 4. Check for remaining duplicates
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
