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

def draw_acorn_squash(d):
    # Dark green ribbed acorn shape with orange spot
    d.polygon([(25, 42), (14, 18), (36, 18)], fill=DKGREEN)
    d.ellipse([14, 15, 36, 30], fill=DKGREEN)
    # Orange spot
    d.ellipse([14, 18, 22, 28], fill=ORANGE)
    # Stem
    d.rectangle([23, 8, 27, 15], fill=DKBROWN)

def draw_spaghetti_squash(d):
    # Oblong yellow squash
    d.ellipse([15, 14, 35, 42], fill=YELLOW)
    d.ellipse([25, 14, 35, 42], fill=DKYELLOW)
    # Stem
    d.rectangle([23, 7, 27, 14], fill=BROWN)

def draw_chayote(d):
    # Pear shaped green wrinkled gourd
    d.ellipse([18, 14, 32, 28], fill=LTGREEN)
    d.ellipse([14, 24, 36, 42], fill=LTGREEN)
    # Wrinkle lines
    d.line([(25, 18), (25, 38)], fill=GREEN)
    d.line([(20, 28), (20, 38)], fill=GREEN)
    d.line([(30, 28), (30, 38)], fill=GREEN)

def draw_kohlrabi(d):
    # Light green round bulb with leafy stems coming out the top
    d.ellipse([15, 20, 35, 40], fill=LTGREEN)
    # Leaf stems
    d.line([(20, 20), (14, 8)], fill=GREEN, width=2)
    d.line([(25, 20), (25, 6)], fill=GREEN, width=2)
    d.line([(30, 20), (36, 8)], fill=GREEN, width=2)
    # Tiny leaves
    d.ellipse([11, 4, 17, 10], fill=LTGREEN)
    d.ellipse([22, 2, 28, 8], fill=LTGREEN)
    d.ellipse([33, 4, 39, 10], fill=LTGREEN)

def draw_radicchio(d):
    # Round purple ball with white leaf veins
    d.ellipse([14, 14, 36, 36], fill=DKPURPLE)
    # White veins
    d.arc([14, 14, 36, 36], 180, 270, fill=WHITE, width=2)
    d.arc([14, 14, 36, 36], 270, 360, fill=WHITE, width=2)
    d.line([(25, 20), (25, 36)], fill=WHITE, width=2)

def draw_endive(d):
    # Elongated pale yellow leaves, tightly packed
    d.polygon([(18, 42), (25, 10), (32, 42)], fill=WHITE)
    # Pale yellow leaf tips
    d.polygon([(21, 18), (25, 10), (29, 18)], fill=YELLOW)
    d.polygon([(18, 30), (22, 18), (25, 30)], fill=YELLOW)
    d.polygon([(32, 30), (28, 18), (25, 30)], fill=YELLOW)

def draw_watercress(d):
    # Bunch of small dark green round leaves
    d.ellipse([12, 12, 24, 24], fill=DKGREEN)
    d.ellipse([26, 12, 38, 24], fill=DKGREEN)
    d.ellipse([18, 6, 32, 20], fill=GREEN)
    d.ellipse([20, 20, 30, 30], fill=DKGREEN)
    # Thin green stems
    d.line([(25, 25), (25, 44)], fill=LTGREEN, width=2)

def draw_arugula(d):
    # Long jagged green leaf
    d.polygon([(25, 10), (18, 20), (22, 22), (16, 30), (23, 32), (25, 44)], fill=GREEN)
    d.polygon([(25, 10), (32, 20), (28, 22), (34, 30), (27, 32), (25, 44)], fill=DKGREEN)
    # Stem
    d.line([(25, 40), (25, 46)], fill=LTGREEN, width=2)

def draw_mustard_greens(d):
    # Large frilly light green leaf
    d.ellipse([14, 12, 36, 38], fill=LTGREEN)
    # Frilly edge lines
    d.arc([14, 12, 36, 38], 0, 360, fill=GREEN, width=2)
    # Veins
    d.line([(25, 14), (25, 38)], fill=WHITE, width=2)

def draw_bok_choy(d):
    # White base fading into green leaves
    d.polygon([(16, 42), (22, 26), (28, 26), (34, 42)], fill=WHITE)
    d.polygon([(18, 26), (12, 10), (25, 26)], fill=GREEN)
    d.polygon([(32, 26), (38, 10), (25, 26)], fill=DKGREEN)
    d.ellipse([20, 8, 30, 20], fill=GREEN)

def draw_napa_cabbage(d):
    # Elongated barrel-shaped light green cabbage
    d.ellipse([15, 14, 35, 42], fill=CREAM)
    # Wavy green outer leaves wrapping
    d.polygon([(15, 42), (12, 20), (22, 42)], fill=LTGREEN)
    d.polygon([(35, 42), (38, 20), (28, 42)], fill=LTGREEN)

def draw_savoy_cabbage(d):
    # Round heavily crinkled cabbage
    d.ellipse([13, 13, 37, 37], fill=DKGREEN)
    # Crinkled textures
    for i in range(16, 36, 4):
        d.line([(14, i), (36, i)], fill=GREEN)
        d.line([(i, 14), (i, 36)], fill=GREEN)

def draw_snow_peas(d):
    # Flat green pea pod
    d.polygon([(10, 25), (40, 15), (35, 30), (12, 35)], fill=LTGREEN)
    # Small bumps for seeds inside
    d.ellipse([18, 22, 22, 26], fill=GREEN)
    d.ellipse([25, 20, 29, 24], fill=GREEN)
    d.ellipse([32, 18, 36, 22], fill=GREEN)

def draw_sugar_snap_peas(d):
    # Plump green pea pod
    d.polygon([(10, 22), (40, 18), (35, 32), (12, 30)], fill=GREEN)
    # Plumper pea shape reflections
    d.ellipse([16, 20, 22, 26], fill=LTGREEN)
    d.ellipse([23, 20, 29, 26], fill=LTGREEN)
    d.ellipse([30, 20, 36, 26], fill=LTGREEN)

def draw_fava_beans(d):
    # Large green pod
    d.polygon([(10, 18), (40, 22), (32, 34), (12, 30)], fill=DKGREEN)
    # Green beans next to it or on it
    d.ellipse([16, 22, 24, 28], fill=LTGREEN)
    d.ellipse([26, 24, 34, 30], fill=LTGREEN)

def draw_lima_beans(d):
    # Broad flat seed (pale green/cream)
    d.ellipse([14, 18, 36, 32], fill=CREAM)
    # Inner curved line
    d.arc([16, 20, 34, 30], 0, 180, fill=LTGREEN, width=2)

def draw_edamame(d):
    # Hairy green soybean pod
    d.polygon([(10, 22), (40, 20), (32, 32), (12, 30)], fill=GREEN)
    # Little hair dashes
    d.line([(18, 22), (18, 20)], fill=LTGREEN)
    d.line([(25, 24), (25, 22)], fill=LTGREEN)
    d.line([(32, 23), (32, 21)], fill=LTGREEN)

def draw_chickpeas(d):
    # Small round bumpy tan peas
    d.ellipse([15, 22, 23, 30], fill=CREAM)
    d.ellipse([26, 20, 34, 28], fill=LTBROWN)
    d.ellipse([20, 28, 28, 36], fill=CREAM)

def draw_shallot(d):
    # Teardrop shaped copper/red bulb
    d.ellipse([16, 22, 34, 40], fill=BROWN)
    # Pointed tip
    d.polygon([(25, 12), (18, 24), (32, 24)], fill=LTBROWN)
    # Purple/red shade
    d.ellipse([25, 22, 34, 40], fill=DKRED)

def draw_ramp(d):
    # Wild leek: purple stem base, green leaves
    d.line([(25, 45), (25, 25)], fill=PURPLE, width=3)
    d.polygon([(25, 25), (15, 8), (25, 8)], fill=GREEN)
    d.polygon([(25, 25), (35, 8), (25, 8)], fill=DKGREEN)

def draw_jicama(d):
    # Turnip-shaped brown root with white flesh showing from cut
    d.ellipse([14, 18, 36, 40], fill=BROWN)
    # Wedge slice taken out showing white
    d.polygon([(25, 18), (14, 28), (25, 40)], fill=CREAM)

def draw_rutabaga(d):
    # Large rough root, purple top, yellow bottom
    d.ellipse([14, 18, 36, 40], fill=YELLOW)
    d.ellipse([14, 18, 36, 28], fill=PURPLE)
    d.line([(25, 40), (25, 46)], fill=LTBROWN, width=2) # root tail

def draw_parsnip(d):
    # Long tapered cream/pale yellow root
    d.polygon([(18, 14), (32, 14), (25, 44)], fill=CREAM)
    # Ridges
    d.line([(20, 22), (26, 22)], fill=LTBROWN)
    d.line([(21, 30), (25, 30)], fill=LTBROWN)

def draw_sunchoke(d):
    # Knobby ginger-like brown root
    d.ellipse([18, 22, 30, 32], fill=BROWN)
    d.ellipse([24, 16, 36, 26], fill=LTBROWN)
    d.ellipse([14, 26, 24, 38], fill=BROWN)

def draw_celeriac(d):
    # Large bumpy brown root ball
    d.ellipse([14, 18, 36, 40], fill=BROWN)
    # Bumps and rootlet squiggles
    d.arc([14, 18, 36, 40], 0, 180, fill=DKBROWN, width=2)
    # Stem cutoffs on top
    d.rectangle([22, 12, 28, 18], fill=GREEN)

def draw_fiddlehead_fern(d):
    # Coiled green fern shoot
    d.arc([16, 16, 34, 34], 0, 360, fill=DKGREEN, width=4)
    d.arc([20, 20, 30, 30], 0, 270, fill=GREEN, width=4)
    # Stem tail
    d.line([(16, 30), (10, 42)], fill=DKGREEN, width=4)

def draw_seaweed(d):
    # Wavy green kelp strands
    d.arc([14, 10, 26, 42], 0, 180, fill=GREEN, width=3)
    d.arc([24, 10, 36, 42], 180, 360, fill=DKGREEN, width=3)

def draw_nori(d):
    # Dark green/black rectangular sheet
    d.rectangle([12, 12, 38, 38], fill=DKGRAY)
    # Grid/texture line
    d.line([(16, 12), (16, 38)], fill=DKGREEN)
    d.line([(32, 12), (32, 38)], fill=DKGREEN)

def draw_portobello_mushroom(d):
    # Large brown cap mushroom
    d.ellipse([12, 14, 38, 28], fill=DKBROWN)
    # Thick cream stem
    d.rectangle([20, 28, 30, 42], fill=CREAM)

def draw_oyster_mushroom(d):
    # Fan-shaped light gray cap
    d.ellipse([15, 14, 35, 30], fill=GRAY)
    # Gills under cap
    d.line([(25, 25), (20, 36)], fill=WHITE, width=2)
    d.line([(25, 25), (30, 36)], fill=WHITE, width=2)
    # Stem
    d.rectangle([21, 30, 29, 42], fill=CREAM)

def draw_chanterelle_mushroom(d):
    # Funnel-shaped yellow/orange mushroom
    d.polygon([(14, 14), (36, 14), (27, 36), (23, 36)], fill=YELLOW)
    # Shading
    d.polygon([(25, 14), (36, 14), (27, 36)], fill=ORANGE)
    d.rectangle([23, 36, 27, 42], fill=YELLOW)

def draw_morel_mushroom(d):
    # Honeycomb-textured cone cap
    d.polygon([(25, 10), (16, 30), (34, 30)], fill=BROWN)
    # Grid honeycomb lines
    for i in range(16, 30, 4):
        d.line([(25, i), (25, i+2)], fill=DKBROWN)
    # Stem
    d.rectangle([22, 30, 28, 42], fill=CREAM)

def draw_enoki_mushroom(d):
    # Bunch of long thin white mushrooms
    d.line([(20, 16), (20, 42)], fill=WHITE, width=2)
    d.line([(25, 14), (25, 42)], fill=WHITE, width=2)
    d.line([(30, 16), (30, 42)], fill=WHITE, width=2)
    # Caps
    d.ellipse([18, 12, 22, 16], fill=CREAM)
    d.ellipse([23, 10, 27, 14], fill=CREAM)
    d.ellipse([28, 12, 32, 16], fill=CREAM)

def draw_truffle(d):
    # Bumpy round black/dark brown ball
    d.ellipse([14, 16, 36, 38], fill=DKGRAY)
    # Spikes/bumps
    for p in [(16, 22), (24, 18), (32, 22), (22, 28), (30, 30), (20, 34)]:
        d.point(p, fill=BLACK)

def draw_sweet_corn(d):
    # Pile of yellow kernels
    d.ellipse([15, 20, 25, 30], fill=YELLOW)
    d.ellipse([23, 18, 33, 28], fill=DKYELLOW)
    d.ellipse([20, 26, 30, 36], fill=YELLOW)

def draw_baby_corn(d):
    # Tiny light yellow corn cob
    d.polygon([(25, 10), (20, 42), (30, 42)], fill=CREAM)
    # Small kernel rows
    for y in range(16, 40, 4):
        d.line([(22, y), (28, y)], fill=YELLOW)

def draw_hearts_of_palm(d):
    # Cylinder stick white/cream
    d.rectangle([18, 14, 32, 42], fill=CREAM)
    # Rings
    d.arc([18, 14, 32, 24], 0, 360, fill=WHITE, width=1)
    d.arc([18, 30, 32, 40], 0, 360, fill=WHITE, width=1)

def draw_cactus_pad(d):
    # Green flat oval pad with spines
    d.ellipse([15, 14, 35, 42], fill=GREEN)
    # Spines
    for p in [(18, 20), (32, 20), (25, 28), (20, 34), (30, 34)]:
        d.line([(p[0]-2, p[1]-2), (p[0]+2, p[1]+2)], fill=YELLOW)

def draw_tomatillo(d):
    # Green fruit wrapped in paper husk
    d.ellipse([16, 18, 34, 38], fill=LTGREEN)
    # Straw/husk lines wrapping
    d.arc([14, 14, 36, 38], 0, 180, fill=CREAM, width=2)
    d.arc([14, 14, 36, 38], 180, 360, fill=CREAM, width=2)

def draw_habanero_pepper(d):
    # Orange blocky hot pepper
    d.rectangle([16, 18, 34, 38], fill=ORANGE)
    d.ellipse([16, 18, 24, 38], fill=ORANGE)
    d.ellipse([26, 18, 34, 38], fill=DKORANGE)
    # Stem
    d.rectangle([23, 9, 27, 18], fill=GREEN)

def draw_poblano_pepper(d):
    # Dark green blocky pepper
    d.rectangle([15, 18, 35, 38], fill=DKGREEN)
    # Stem
    d.rectangle([23, 9, 27, 18], fill=GREEN)

def draw_serrano_pepper(d):
    # Thin green chilli pepper
    d.arc([14, 14, 36, 36], 0, 180, fill=GREEN, width=4)
    # Stem
    d.line([(34, 25), (38, 21)], fill=LTGREEN, width=2)

def draw_ghost_pepper(d):
    # Wrinkled red pepper tapering to point
    d.polygon([(18, 18), (32, 18), (25, 42)], fill=RED)
    # Wrinkle shades
    d.line([(25, 18), (25, 38)], fill=DKRED, width=2)

def draw_delicata_squash(d):
    # Oblong cream squash with green stripes
    d.ellipse([16, 14, 34, 42], fill=CREAM)
    # Green stripes
    d.line([(20, 14), (20, 42)], fill=GREEN, width=2)
    d.line([(30, 14), (30, 42)], fill=GREEN, width=2)

def draw_kabocha_squash(d):
    # Round dark green squash
    d.ellipse([14, 15, 36, 39], fill=DKGREEN)
    # Faint orange/green stripe flecks
    d.line([(25, 15), (25, 39)], fill=GREEN, width=1)
    # Stem
    d.rectangle([23, 8, 27, 15], fill=BROWN)

def draw_collard_greens(d):
    # Large broad dark green leaf
    d.ellipse([14, 12, 36, 38], fill=DKGREEN)
    # Stem & veins
    d.line([(25, 38), (25, 45)], fill=LTGREEN, width=2)
    d.line([(25, 14), (25, 38)], fill=LTGREEN, width=1)

def draw_dandelion_greens(d):
    # Jagged green tooth leaf
    d.polygon([(25, 10), (19, 22), (23, 24), (17, 34), (25, 44)], fill=GREEN)
    d.polygon([(25, 10), (31, 22), (27, 24), (33, 34), (25, 44)], fill=DKGREEN)

def draw_sorrel_leaf(d):
    # Shield shaped green leaf
    d.polygon([(25, 10), (14, 36), (20, 38), (25, 30), (30, 38), (36, 36)], fill=GREEN)
    d.line([(25, 30), (25, 45)], fill=LTGREEN, width=2)

def draw_galangal(d):
    # Knobby root like ginger but pinkish/white rings
    d.ellipse([16, 20, 28, 32], fill=CREAM)
    d.ellipse([22, 16, 34, 28], fill=CREAM)
    d.ellipse([26, 24, 38, 36], fill=PINK)

def draw_turmeric_root(d):
    # Knobby orange/brown root
    d.ellipse([16, 20, 28, 32], fill=ORANGE)
    d.ellipse([22, 16, 34, 28], fill=BROWN)
    d.ellipse([26, 24, 38, 36], fill=ORANGE)

DRAWINGS = {
    "acorn_squash": draw_acorn_squash,
    "spaghetti_squash": draw_spaghetti_squash,
    "chayote": draw_chayote,
    "kohlrabi": draw_kohlrabi,
    "radicchio": draw_radicchio,
    "endive": draw_endive,
    "watercress": draw_watercress,
    "arugula": draw_arugula,
    "mustard_greens": draw_mustard_greens,
    "bok_choy": draw_bok_choy,
    "napa_cabbage": draw_napa_cabbage,
    "savoy_cabbage": draw_savoy_cabbage,
    "snow_peas": draw_snow_peas,
    "sugar_snap_peas": draw_sugar_snap_peas,
    "fava_beans": draw_fava_beans,
    "lima_beans": draw_lima_beans,
    "edamame": draw_edamame,
    "chickpeas": draw_chickpeas,
    "shallot": draw_shallot,
    "ramp": draw_ramp,
    "jicama": draw_jicama,
    "rutabaga": draw_rutabaga,
    "parsnip": draw_parsnip,
    "sunchoke": draw_sunchoke,
    "celeriac": draw_celeriac,
    "fiddlehead_fern": draw_fiddlehead_fern,
    "seaweed": draw_seaweed,
    "nori": draw_nori,
    "portobello_mushroom": draw_portobello_mushroom,
    "oyster_mushroom": draw_oyster_mushroom,
    "chanterelle_mushroom": draw_chanterelle_mushroom,
    "morel_mushroom": draw_morel_mushroom,
    "enoki_mushroom": draw_enoki_mushroom,
    "truffle": draw_truffle,
    "sweet_corn": draw_sweet_corn,
    "baby_corn": draw_baby_corn,
    "hearts_of_palm": draw_hearts_of_palm,
    "cactus_pad": draw_cactus_pad,
    "tomatillo": draw_tomatillo,
    "habanero_pepper": draw_habanero_pepper,
    "poblano_pepper": draw_poblano_pepper,
    "serrano_pepper": draw_serrano_pepper,
    "ghost_pepper": draw_ghost_pepper,
    "delicata_squash": draw_delicata_squash,
    "kabocha_squash": draw_kabocha_squash,
    "collard_greens": draw_collard_greens,
    "dandelion_greens": draw_dandelion_greens,
    "sorrel_leaf": draw_sorrel_leaf,
    "galangal": draw_galangal,
    "turmeric_root": draw_turmeric_root
}

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    base_img.save(path)
    print(f"  Saved raw: {path}")

if __name__ == "__main__":
    print(f"Generating 50 raw vegetable sprites (batch 2) inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating raw vegetable sprites (batch 2)!")
