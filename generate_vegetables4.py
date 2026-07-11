import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/vegetables"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color Constants
ORANGE     = (240, 110, 30, 255)
DKORANGE   = (180, 70, 10, 255)
GREEN      = (60, 160, 60, 255)
DKGREEN    = (30, 90, 30, 255)
LTGREEN    = (130, 210, 100, 255)
WHITE      = (240, 240, 240, 255)
GRAY       = (160, 160, 160, 255)
DKGRAY     = (80, 80, 80, 255)
PURPLE     = (130, 50, 150, 255)
DKPURPLE   = (70, 20, 90, 255)
RED        = (220, 50, 50, 255)
DKRED      = (140, 20, 20, 255)
BROWN      = (140, 100, 60, 255)
DKBROWN    = (90, 60, 30, 255)
LTBROWN    = (200, 170, 130, 255)
YELLOW     = (240, 200, 50, 255)
DKYELLOW   = (170, 130, 20, 255)
CREAM      = (245, 235, 205, 255)
PINK       = (230, 120, 160, 255)
BLACK      = (0, 0, 0, 255)

def draw_radish_daikon_green(d):
    d.polygon([(20, 12), (30, 12), (25, 45)], fill=WHITE)
    d.polygon([(20, 12), (30, 12), (25, 20)], fill=LTGREEN)

def draw_watermelon_radish(d):
    # Slice showing pink inside, green outside
    d.ellipse([12, 12, 38, 38], fill=DKGREEN)
    d.ellipse([14, 14, 36, 36], fill=WHITE)
    d.ellipse([16, 16, 34, 34], fill=PINK)

def draw_black_spanish_radish(d):
    # Round black root, white root tail
    d.ellipse([15, 18, 35, 38], fill=DKGRAY)
    d.line([(25, 38), (25, 45)], fill=WHITE, width=2)
    d.line([(25, 18), (25, 8)], fill=GREEN, width=2)

def draw_french_breakfast_radish(d):
    # Elongated red radish with white bottom
    d.polygon([(20, 18), (30, 18), (27, 40), (23, 40)], fill=RED)
    d.rectangle([23, 36, 27, 40], fill=WHITE)
    d.line([(25, 18), (25, 8)], fill=GREEN, width=2)

def draw_moringa_pod(d):
    # Long ribbed drumstick pod
    d.line([(10, 42), (42, 10)], fill=DKGREEN, width=3)
    d.line([(14, 38), (38, 14)], fill=GREEN, width=1)

def draw_lotus_stem(d):
    # Cylinder stick with small holes
    d.rectangle([18, 14, 32, 42], fill=CREAM)
    # Shading and details
    d.rectangle([25, 14, 32, 42], fill=LTBROWN)

def draw_arrowroot(d):
    # Tapered white scale bulb
    d.polygon([(20, 15), (30, 15), (25, 44)], fill=WHITE)
    # Ring layers
    d.arc([20, 15, 30, 25], 0, 360, fill=GRAY)
    d.arc([21, 28, 29, 38], 0, 360, fill=GRAY)

def draw_burdock_root(d):
    # Long thin brown stick root
    d.line([(10, 42), (42, 10)], fill=BROWN, width=3)
    # Wrinkle notches
    d.point([(20, 32), (30, 22), (25, 27)], fill=DKBROWN)

def draw_salsify(d):
    # Long thin white/tan root
    d.line([(10, 42), (42, 10)], fill=CREAM, width=3)
    d.point([(20, 32), (30, 22), (25, 27)], fill=LTBROWN)

def draw_hamburg_parsley(d):
    # Parsnip-like root with parsley leaf top
    d.polygon([(18, 20), (32, 20), (25, 44)], fill=WHITE)
    # Leaf top
    d.line([(25, 20), (25, 8)], fill=GREEN, width=2)
    d.ellipse([21, 6, 29, 12], fill=LTGREEN)

def draw_maca_root(d):
    # Heart shaped yellow/brown root
    d.polygon([(25, 42), (14, 18), (36, 18)], fill=YELLOW)
    d.ellipse([14, 15, 36, 28], fill=DKYELLOW)
    d.line([(25, 42), (25, 46)], fill=BROWN, width=2)

def draw_kohlrabi_purple(d):
    d.ellipse([15, 20, 35, 40], fill=PURPLE)
    d.line([(25, 20), (25, 6)], fill=DKPURPLE, width=2)
    d.ellipse([22, 2, 28, 8], fill=LTGREEN)

def draw_sweet_potato_purple(d):
    d.polygon([(10, 25), (20, 16), (38, 20), (42, 27), (35, 34), (20, 32)], fill=PURPLE)
    d.polygon([(20, 25), (20, 16), (38, 20), (42, 27), (35, 34)], fill=DKPURPLE)

def draw_yam_purple(d):
    # Outer brown skin, purple inside cut showing
    d.ellipse([14, 18, 36, 38], fill=DKBROWN)
    d.ellipse([18, 20, 32, 34], fill=PURPLE)

def draw_potato_fingerling(d):
    # Tiny kidney shaped potato
    d.polygon([(16, 20), (28, 14), (34, 25), (22, 36), (14, 30)], fill=LTBROWN)

def draw_potato_red(d):
    # Red skinned round potato
    d.ellipse([14, 16, 36, 38], fill=PINK)
    d.point([(20, 22), (30, 24), (24, 32)], fill=RED)

def draw_potato_blue(d):
    # Deep blue/purple potato
    d.ellipse([14, 16, 36, 38], fill=DKPURPLE)

def draw_cassava_yellow(d):
    # Brown skin, yellow flesh cut showing
    d.polygon([(10, 25), (40, 15), (38, 30)], fill=BROWN)
    d.ellipse([22, 18, 32, 28], fill=YELLOW)

def draw_arrowhead_root(d):
    # Round bulb with arrow tip sprout
    d.ellipse([16, 22, 34, 40], fill=CREAM)
    d.polygon([(25, 8), (21, 22), (29, 22)], fill=LTGREEN)

def draw_nagaimo(d):
    # Long hairy cylinder
    d.rectangle([18, 14, 32, 42], fill=LTBROWN)
    d.point([(21, 20), (29, 30), (23, 38)], fill=DKBROWN)

def draw_pattypan_yellow(d):
    # Scalloped disc squash
    d.ellipse([12, 18, 38, 34], fill=YELLOW)
    # Scallop ridges
    for x in range(16, 36, 4):
        d.line([(x, 18), (x, 34)], fill=DKYELLOW)

def draw_pattypan_green(d):
    d.ellipse([12, 18, 38, 34], fill=LTGREEN)
    for x in range(16, 36, 4):
        d.line([(x, 18), (x, 34)], fill=GREEN)

def draw_crookneck_squash(d):
    # Yellow squash with curved neck
    d.ellipse([14, 25, 36, 43], fill=YELLOW)
    d.arc([18, 10, 36, 30], 180, 360, fill=YELLOW, width=5)
    d.rectangle([23, 8, 27, 13], fill=BROWN)

def draw_banana_squash(d):
    # Long thick pink/yellow squash
    d.polygon([(10, 28), (40, 16), (36, 34), (12, 36)], fill=CREAM)

def draw_hubbard_squash(d):
    # Huge bumpy blue-gray squash
    d.ellipse([12, 14, 38, 42], fill=GRAY)
    d.point([(18, 20), (32, 24), (22, 32)], fill=DKGRAY)

def draw_turban_squash(d):
    # Turban-like squash with green/orange cap
    d.ellipse([14, 22, 36, 42], fill=ORANGE)
    d.ellipse([18, 14, 32, 26], fill=DKGREEN)

def draw_chayote_yellow(d):
    d.ellipse([18, 14, 32, 28], fill=YELLOW)
    d.ellipse([14, 24, 36, 42], fill=YELLOW)
    d.line([(25, 18), (25, 38)], fill=DKYELLOW)

def draw_bitter_melon_white(d):
    d.polygon([(10, 36), (36, 10), (40, 14), (14, 40)], fill=WHITE)
    for p in [(15, 33), (20, 28), (25, 23), (30, 18), (35, 13)]:
         d.ellipse([p[0]-1, p[1]-1, p[0]+1, p[1]+1], fill=GRAY)

def draw_snake_gourd(d):
    # Coiled green gourd with white stripes
    d.arc([14, 14, 36, 36], 0, 360, fill=GREEN, width=4)
    # Stripes
    d.arc([14, 14, 36, 36], 90, 270, fill=WHITE, width=1)

def draw_luffa(d):
    # Long ribbed green gourd
    d.polygon([(10, 36), (36, 10), (40, 14), (14, 40)], fill=DKGREEN)
    d.line([(15, 31), (31, 15)], fill=GREEN, width=1)

def draw_sponge_gourd(d):
    # Smooth light green gourd
    d.polygon([(10, 36), (36, 10), (40, 14), (14, 40)], fill=LTGREEN)

def draw_bottle_gourd(d):
    # Double bulb green gourd
    d.ellipse([18, 14, 32, 26], fill=GREEN)
    d.ellipse([14, 24, 36, 43], fill=GREEN)

def draw_wax_gourd(d):
    # Huge green gourd with white waxy powder
    d.ellipse([12, 14, 38, 42], fill=GREEN)
    d.ellipse([18, 18, 32, 38], fill=CREAM)

def draw_ivy_gourd(d):
    # Small smooth oval green gourd
    d.ellipse([16, 20, 34, 34], fill=GREEN)
    d.line([(20, 27), (30, 27)], fill=LTGREEN, width=1)

def draw_point_gourd(d):
    # Pointed green gourd with white stripes
    d.polygon([(14, 25), (25, 12), (36, 25), (25, 38)], fill=GREEN)
    d.line([(25, 12), (25, 38)], fill=WHITE, width=1)

def draw_spine_gourd(d):
    # Small spiky green gourd
    d.ellipse([15, 18, 35, 36], fill=GREEN)
    # Spikes
    for p in [(18, 22), (32, 22), (25, 28), (20, 32), (30, 32)]:
        d.point(p, fill=LTGREEN)

def draw_wood_ear_mushroom(d):
    # Dark brown/black ear-shaped folds
    d.ellipse([15, 15, 35, 35], fill=DKGRAY)
    d.arc([15, 15, 35, 35], 0, 180, fill=BLACK, width=2)

def draw_king_oyster_mushroom(d):
    # Huge thick white stem, tiny brown cap
    d.rectangle([18, 22, 32, 42], fill=WHITE)
    d.ellipse([15, 14, 35, 22], fill=BROWN)

def draw_maitake_mushroom(d):
    # Frilly dark brown clustered layers
    d.ellipse([14, 14, 36, 36], fill=BROWN)
    d.ellipse([18, 18, 32, 32], fill=DKBROWN)

def draw_lions_mane_mushroom(d):
    # White shaggy ball
    d.ellipse([14, 14, 36, 36], fill=WHITE)
    # Shags
    for y in range(16, 36, 4):
        d.line([(18, y), (32, y)], fill=CREAM)

def draw_beech_mushroom(d):
    # Small cluster of brown caps
    d.line([(20, 22), (20, 42)], fill=WHITE, width=2)
    d.line([(30, 22), (30, 42)], fill=WHITE, width=2)
    d.ellipse([16, 16, 24, 22], fill=BROWN)
    d.ellipse([26, 16, 34, 22], fill=BROWN)

def draw_porcini_mushroom(d):
    # Fat stalk, broad brown cap
    d.ellipse([16, 22, 34, 42], fill=CREAM)
    d.ellipse([12, 12, 38, 22], fill=BROWN)

def draw_cremini_mushroom(d):
    # Small brown cap
    d.ellipse([14, 14, 36, 28], fill=LTBROWN)
    d.rectangle([22, 28, 28, 42], fill=CREAM)

def draw_straw_mushroom(d):
    # Cone cap with dark brown veil sheath
    d.polygon([(25, 12), (18, 32), (32, 32)], fill=CREAM)
    d.polygon([(25, 26), (18, 32), (32, 32)], fill=DKGRAY)

def draw_lobster_mushroom(d):
    # Bright orange rough funnel mushroom
    d.polygon([(14, 14), (36, 14), (27, 38), (23, 38)], fill=ORANGE)
    d.polygon([(18, 14), (32, 14), (25, 30)], fill=RED)

def draw_sea_beans(d):
    # Segmented green marine spears
    d.line([(25, 44), (25, 14)], fill=GREEN, width=3)
    d.line([(25, 26), (18, 18)], fill=LTGREEN, width=2)
    d.line([(25, 32), (32, 24)], fill=LTGREEN, width=2)

def draw_saltbush(d):
    # Silvery green bunch of leaves
    d.ellipse([15, 15, 25, 25], fill=GRAY)
    d.ellipse([25, 15, 35, 25], fill=LTGREEN)
    d.ellipse([20, 25, 30, 35], fill=GRAY)

def draw_glasswort(d):
    # Fleshy green jointed stems
    d.line([(25, 44), (25, 12)], fill=GREEN, width=4)
    # Joints
    for y in range(16, 40, 6):
        d.line([(23, y), (27, y)], fill=LTGREEN, width=2)

def draw_kaniwa_greens(d):
    # Red-green leafy stalks
    d.line([(25, 44), (25, 12)], fill=RED, width=3)
    d.ellipse([16, 16, 24, 24], fill=GREEN)
    d.ellipse([26, 16, 34, 24], fill=GREEN)

def draw_amaranth_greens(d):
    # Oval green leaves with magenta centers
    d.ellipse([14, 12, 36, 38], fill=GREEN)
    d.ellipse([20, 18, 30, 32], fill=PINK)
    d.line([(25, 38), (25, 45)], fill=PINK, width=2)

DRAWINGS = {
    "radish_daikon_green": draw_radish_daikon_green,
    "watermelon_radish": draw_watermelon_radish,
    "black_spanish_radish": draw_black_spanish_radish,
    "french_breakfast_radish": draw_french_breakfast_radish,
    "moringa_pod": draw_moringa_pod,
    "lotus_stem": draw_lotus_stem,
    "arrowroot": draw_arrowroot,
    "burdock_root": draw_burdock_root,
    "salsify": draw_salsify,
    "hamburg_parsley": draw_hamburg_parsley,
    "maca_root": draw_maca_root,
    "kohlrabi_purple": draw_kohlrabi_purple,
    "sweet_potato_purple": draw_sweet_potato_purple,
    "yam_purple": draw_yam_purple,
    "potato_fingerling": draw_potato_fingerling,
    "potato_red": draw_potato_red,
    "potato_blue": draw_potato_blue,
    "cassava_yellow": draw_cassava_yellow,
    "arrowhead_root": draw_arrowhead_root,
    "nagaimo": draw_nagaimo,
    "pattypan_yellow": draw_pattypan_yellow,
    "pattypan_green": draw_pattypan_green,
    "crookneck_squash": draw_crookneck_squash,
    "banana_squash": draw_banana_squash,
    "hubbard_squash": draw_hubbard_squash,
    "turban_squash": draw_turban_squash,
    "chayote_yellow": draw_chayote_yellow,
    "bitter_melon_white": draw_bitter_melon_white,
    "snake_gourd": draw_snake_gourd,
    "luffa": draw_luffa,
    "sponge_gourd": draw_sponge_gourd,
    "bottle_gourd": draw_bottle_gourd,
    "wax_gourd": draw_wax_gourd,
    "ivy_gourd": draw_ivy_gourd,
    "point_gourd": draw_point_gourd,
    "spine_gourd": draw_spine_gourd,
    "wood_ear_mushroom": draw_wood_ear_mushroom,
    "king_oyster_mushroom": draw_king_oyster_mushroom,
    "maitake_mushroom": draw_maitake_mushroom,
    "lions_mane_mushroom": draw_lions_mane_mushroom,
    "beech_mushroom": draw_beech_mushroom,
    "porcini_mushroom": draw_porcini_mushroom,
    "cremini_mushroom": draw_cremini_mushroom,
    "straw_mushroom": draw_straw_mushroom,
    "lobster_mushroom": draw_lobster_mushroom,
    "sea_beans": draw_sea_beans,
    "saltbush": draw_saltbush,
    "glasswort": draw_glasswort,
    "kaniwa_greens": draw_kaniwa_greens,
    "amaranth_greens": draw_amaranth_greens
}

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    base_img.save(path)
    print(f"  Saved raw: {path}")

if __name__ == "__main__":
    print(f"Generating 50 raw vegetable sprites (batch 4) inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating raw vegetable sprites (batch 4)!")
