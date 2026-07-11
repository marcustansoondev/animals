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

def draw_carrot(d):
    # Cone body
    d.polygon([(25, 45), (15, 15), (35, 15)], fill=ORANGE)
    d.polygon([(25, 45), (25, 15), (35, 15)], fill=DKORANGE)
    # Green tuft
    d.line([(25, 15), (25, 5)], fill=GREEN, width=2)
    d.line([(25, 15), (18, 7)], fill=DKGREEN, width=2)
    d.line([(25, 15), (32, 7)], fill=LTGREEN, width=2)

def draw_broccoli(d):
    # Stalk
    d.rectangle([21, 28, 29, 44], fill=LTGREEN)
    d.rectangle([25, 28, 29, 44], fill=GREEN)
    # Florets
    d.ellipse([10, 10, 28, 28], fill=GREEN)
    d.ellipse([22, 10, 40, 28], fill=DKGREEN)
    d.ellipse([15, 5, 35, 22], fill=GREEN)

def draw_cauliflower(d):
    # Outer leaves
    d.ellipse([8, 12, 42, 42], fill=DKGREEN)
    # Inner florets (cream)
    d.ellipse([14, 14, 28, 28], fill=CREAM)
    d.ellipse([22, 14, 36, 28], fill=WHITE)
    d.ellipse([16, 22, 34, 36], fill=CREAM)
    d.ellipse([18, 10, 32, 22], fill=WHITE)

def draw_eggplant(d):
    # Purple pear body
    d.ellipse([15, 18, 35, 44], fill=PURPLE)
    d.ellipse([22, 18, 35, 44], fill=DKPURPLE)
    d.ellipse([18, 25, 32, 40], fill=PURPLE)
    # Green cap/stem
    d.polygon([(25, 10), (20, 18), (30, 18)], fill=DKGREEN)
    d.rectangle([24, 6, 26, 12], fill=GREEN)

def draw_tomato(d):
    # Round body
    d.ellipse([12, 14, 38, 40], fill=RED)
    d.ellipse([25, 14, 38, 40], fill=DKRED)
    # Stem star
    d.polygon([(25, 14), (21, 10), (29, 10)], fill=DKGREEN)
    d.polygon([(25, 14), (25, 8), (25, 14)], fill=GREEN)
    d.line([(25, 12), (25, 6)], fill=GREEN, width=2)

def draw_potato(d):
    # Oval lumpy body
    d.ellipse([12, 16, 38, 38], fill=LTBROWN)
    # Spots
    d.point([(18, 22), (22, 30), (32, 20), (28, 32), (16, 28), (34, 26)], fill=DKBROWN)

def draw_sweet_potato(d):
    # Elongated pointed body
    d.polygon([(10, 25), (20, 16), (38, 20), (42, 27), (35, 34), (20, 32)], fill=PINK)
    d.polygon([(20, 25), (20, 16), (38, 20), (42, 27), (35, 34)], fill=DKPURPLE)

def draw_bell_pepper_red(d):
    # Lobed body
    d.rectangle([14, 16, 36, 40], fill=RED)
    d.ellipse([12, 16, 24, 40], fill=RED)
    d.ellipse([26, 16, 38, 40], fill=DKRED)
    d.ellipse([19, 16, 31, 40], fill=RED)
    # Stem
    d.rectangle([23, 8, 27, 16], fill=GREEN)

def draw_bell_pepper_green(d):
    # Lobed body
    d.rectangle([14, 16, 36, 40], fill=GREEN)
    d.ellipse([12, 16, 24, 40], fill=GREEN)
    d.ellipse([26, 16, 38, 40], fill=DKGREEN)
    d.ellipse([19, 16, 31, 40], fill=LTGREEN)
    # Stem
    d.rectangle([23, 8, 27, 16], fill=LTGREEN)

def draw_cucumber(d):
    # Long curved cylinder
    d.polygon([(10, 36), (36, 10), (40, 14), (14, 40)], fill=DKGREEN)
    # Bumps / light stripes
    d.line([(15, 31), (31, 15)], fill=GREEN, width=2)
    d.line([(19, 35), (35, 19)], fill=GREEN, width=1)

def draw_zucchini(d):
    # Long cylinder
    d.polygon([(8, 38), (38, 8), (42, 12), (12, 42)], fill=GREEN)
    # Lighter green highlights
    d.line([(12, 34), (34, 12)], fill=LTGREEN, width=2)

def draw_pumpkin(d):
    # Large ribbed round body
    d.ellipse([10, 15, 40, 42], fill=ORANGE)
    d.ellipse([15, 15, 35, 42], fill=DKORANGE)
    d.ellipse([20, 15, 30, 42], fill=ORANGE)
    # Thick stem
    d.rectangle([22, 7, 28, 15], fill=DKBROWN)

def draw_butternut_squash(d):
    # Pear shape
    d.ellipse([18, 15, 32, 28], fill=CREAM)
    d.ellipse([14, 24, 36, 43], fill=CREAM)
    # Shading
    d.ellipse([24, 24, 36, 43], fill=LTBROWN)

def draw_garlic(d):
    # Bulb with pointed top
    d.ellipse([14, 20, 36, 42], fill=CREAM)
    d.polygon([(25, 12), (18, 22), (32, 22)], fill=WHITE)
    # Roots
    d.line([(22, 43), (22, 46)], fill=LTBROWN)
    d.line([(25, 43), (25, 47)], fill=LTBROWN)
    d.line([(28, 43), (28, 46)], fill=LTBROWN)

def draw_onion_red(d):
    # Red/purple bulb
    d.ellipse([14, 18, 36, 41], fill=PURPLE)
    d.ellipse([25, 18, 36, 41], fill=DKPURPLE)
    d.polygon([(25, 10), (16, 20), (34, 20)], fill=PURPLE)
    # Root tuft
    d.line([(23, 42), (27, 45)], fill=CREAM)

def draw_onion_yellow(d):
    # Golden yellow bulb
    d.ellipse([14, 18, 36, 41], fill=YELLOW)
    d.ellipse([25, 18, 36, 41], fill=DKYELLOW)
    d.polygon([(25, 10), (16, 20), (34, 20)], fill=YELLOW)
    d.line([(23, 42), (27, 45)], fill=CREAM)

def draw_radish(d):
    # Round red bulb, white root tip
    d.ellipse([16, 20, 34, 38], fill=RED)
    d.ellipse([24, 20, 34, 38], fill=DKRED)
    d.polygon([(25, 44), (22, 36), (28, 36)], fill=WHITE)
    # Green leaves
    d.line([(25, 20), (25, 8)], fill=GREEN, width=2)
    d.ellipse([21, 6, 29, 12], fill=LTGREEN)

def draw_turnip(d):
    # White bottom, purple top
    d.ellipse([15, 20, 35, 40], fill=WHITE)
    d.ellipse([15, 20, 35, 30], fill=PURPLE)
    # Root tail
    d.line([(25, 40), (25, 46)], fill=WHITE)
    # Leaf stem
    d.line([(25, 20), (25, 8)], fill=GREEN, width=2)

def draw_beetroot(d):
    # Red/purple round body
    d.ellipse([14, 18, 36, 40], fill=DKPURPLE)
    # Long thin taproot
    d.line([(25, 40), (25, 47)], fill=DKRED, width=2)
    # Leaf stems & dark red veins
    d.line([(25, 18), (20, 8)], fill=RED, width=2)
    d.line([(25, 18), (30, 8)], fill=DKRED, width=2)

def draw_celery(d):
    # Bundle of green stalks
    d.rectangle([18, 15, 22, 42], fill=LTGREEN)
    d.rectangle([24, 15, 28, 42], fill=GREEN)
    d.rectangle([30, 15, 34, 42], fill=DKGREEN)
    # Leafy tops
    d.ellipse([15, 8, 23, 16], fill=GREEN)
    d.ellipse([22, 8, 30, 16], fill=LTGREEN)
    d.ellipse([28, 8, 36, 16], fill=DKGREEN)

def draw_asparagus(d):
    # Spear bundle
    d.rectangle([16, 20, 20, 44], fill=DKGREEN)
    d.rectangle([23, 14, 27, 44], fill=GREEN)
    d.rectangle([30, 22, 34, 44], fill=DKGREEN)
    # Tips
    d.polygon([(18, 15), (16, 20), (20, 20)], fill=LTGREEN)
    d.polygon([(25, 8), (23, 14), (27, 14)], fill=LTGREEN)
    d.polygon([(32, 17), (30, 22), (34, 22)], fill=GREEN)

def draw_brussels_sprout(d):
    # Small leafy ball
    d.ellipse([16, 16, 34, 34], fill=GREEN)
    # Wavy leaves
    d.ellipse([20, 16, 30, 34], fill=LTGREEN)
    d.arc([16, 16, 34, 34], 0, 180, fill=DKGREEN, width=2)

def draw_cabbage_green(d):
    # Round leafy head
    d.ellipse([12, 12, 38, 38], fill=GREEN)
    # Curved outer leaf layers
    d.ellipse([16, 12, 34, 38], fill=LTGREEN)
    d.ellipse([20, 16, 30, 34], fill=GREEN)

def draw_cabbage_red(d):
    # Round purple/red head
    d.ellipse([12, 12, 38, 38], fill=DKPURPLE)
    d.ellipse([16, 12, 34, 38], fill=PURPLE)
    d.ellipse([20, 16, 30, 34], fill=DKPURPLE)

def draw_spinach_leaf(d):
    # Oval green leaf
    d.ellipse([14, 12, 36, 38], fill=GREEN)
    # Stem & veins
    d.line([(25, 38), (25, 45)], fill=LTGREEN, width=2)
    d.line([(25, 14), (25, 38)], fill=LTGREEN, width=1)
    d.line([(25, 20), (18, 16)], fill=LTGREEN, width=1)
    d.line([(25, 26), (32, 22)], fill=LTGREEN, width=1)

def draw_lettuce_romaine(d):
    # Elongated leaves
    d.polygon([(16, 40), (22, 10), (28, 10), (34, 40)], fill=GREEN)
    d.polygon([(20, 40), (25, 14), (30, 40)], fill=LTGREEN)
    d.line([(25, 25), (25, 43)], fill=WHITE, width=3)

def draw_kale_leaf(d):
    # Wavy curly leaf
    d.ellipse([15, 12, 35, 38], fill=DKGREEN)
    d.ellipse([20, 15, 30, 35], fill=GREEN)
    # Frilly edges
    d.ellipse([12, 16, 18, 22], fill=DKGREEN)
    d.ellipse([32, 16, 38, 22], fill=DKGREEN)
    d.ellipse([13, 26, 17, 30], fill=DKGREEN)
    d.ellipse([33, 26, 37, 30], fill=DKGREEN)

def draw_corn_on_the_cob(d):
    # Yellow cob
    d.ellipse([18, 12, 32, 38], fill=YELLOW)
    # Grid details (kernels)
    for y in range(16, 36, 4):
        d.line([(20, y), (30, y)], fill=DKYELLOW)
    # Green husks peeled back
    d.polygon([(12, 40), (18, 22), (20, 40)], fill=DKGREEN)
    d.polygon([(38, 40), (32, 22), (30, 40)], fill=DKGREEN)

def draw_pea_pod(d):
    # Curved green pod
    d.polygon([(10, 20), (40, 20), (30, 32), (15, 30)], fill=GREEN)
    # Three round green peas inside
    d.ellipse([15, 20, 21, 26], fill=LTGREEN)
    d.ellipse([22, 20, 28, 26], fill=LTGREEN)
    d.ellipse([29, 20, 35, 26], fill=LTGREEN)

def draw_green_bean(d):
    # Long thin green pod
    d.line([(10, 40), (40, 10)], fill=GREEN, width=4)
    d.line([(40, 10), (43, 7)], fill=DKGREEN, width=2) # stem

def draw_okra(d):
    # Ridged pointed green pod
    d.polygon([(15, 15), (35, 15), (25, 45)], fill=GREEN)
    # Ridges
    d.line([(25, 15), (25, 45)], fill=LTGREEN, width=1)
    d.line([(20, 15), (23, 35)], fill=DKGREEN, width=1)
    d.line([(30, 15), (27, 35)], fill=LTGREEN, width=1)

def draw_artichoke(d):
    # Green layered bud
    d.ellipse([15, 18, 35, 38], fill=GREEN)
    # Leaves/scales layers
    d.polygon([(25, 14), (20, 22), (30, 22)], fill=DKGREEN)
    d.polygon([(20, 22), (15, 30), (25, 30)], fill=GREEN)
    d.polygon([(30, 22), (25, 30), (35, 30)], fill=DKGREEN)
    # Stem
    d.rectangle([23, 38, 27, 45], fill=GREEN)

def draw_leek(d):
    # White bottom, green top
    d.rectangle([21, 28, 29, 44], fill=WHITE)
    d.rectangle([21, 12, 29, 28], fill=LTGREEN)
    # Leafy fans
    d.polygon([(21, 12), (14, 4), (25, 12)], fill=GREEN)
    d.polygon([(29, 12), (36, 4), (25, 12)], fill=DKGREEN)

def draw_scallion(d):
    # Thin green onion
    d.line([(25, 45), (25, 25)], fill=WHITE, width=3)
    d.line([(25, 25), (20, 8)], fill=LTGREEN, width=2)
    d.line([(25, 25), (30, 8)], fill=GREEN, width=2)

def draw_ginger_root(d):
    # Knobby tan root
    d.ellipse([16, 20, 28, 32], fill=LTBROWN)
    d.ellipse([22, 16, 34, 28], fill=LTBROWN)
    d.ellipse([26, 24, 38, 36], fill=BROWN)

def draw_mushroom_button(d):
    # Cream cap
    d.ellipse([14, 14, 36, 30], fill=CREAM)
    # Stem
    d.rectangle([22, 30, 28, 42], fill=WHITE)

def draw_shiitake_mushroom(d):
    # Brown cap
    d.ellipse([12, 14, 38, 28], fill=BROWN)
    d.ellipse([20, 14, 38, 28], fill=DKBROWN)
    # Stem
    d.rectangle([22, 28, 28, 42], fill=CREAM)

def draw_chilli_red(d):
    # Curved red pepper
    d.arc([14, 14, 36, 36], 0, 180, fill=RED, width=4)
    # Stem
    d.line([(34, 25), (38, 21)], fill=GREEN, width=2)

def draw_chilli_green(d):
    # Curved green jalapeno
    d.arc([14, 14, 36, 36], 0, 180, fill=GREEN, width=4)
    d.line([(34, 25), (38, 21)], fill=LTGREEN, width=2)

def draw_bitter_melon(d):
    # Wrinkled bumpy green cucumber
    d.polygon([(10, 36), (36, 10), (40, 14), (14, 40)], fill=GREEN)
    # Dots representing bumps
    for p in [(15, 33), (20, 28), (25, 23), (30, 18), (35, 13)]:
        d.ellipse([p[0]-1, p[1]-1, p[0]+1, p[1]+1], fill=LTGREEN)

def draw_daikon_radish(d):
    # Long thick white root
    d.polygon([(20, 12), (30, 12), (25, 45)], fill=WHITE)
    # Soft gray shading
    d.polygon([(25, 12), (30, 12), (25, 45)], fill=GRAY)

def draw_fennel_bulb(d):
    # White thick bulb
    d.ellipse([16, 24, 34, 42], fill=CREAM)
    # Feathery green tops
    d.line([(22, 24), (18, 10)], fill=GREEN, width=2)
    d.line([(28, 24), (32, 10)], fill=DKGREEN, width=2)
    # Fronds
    d.line([(18, 10), (14, 6)], fill=LTGREEN, width=1)
    d.line([(32, 10), (36, 6)], fill=LTGREEN, width=1)

def draw_taro_root(d):
    # Hairy brown root
    d.ellipse([15, 18, 35, 38], fill=BROWN)
    # Concentric rings
    d.arc([15, 18, 35, 38], 0, 360, fill=DKBROWN, width=1)
    d.ellipse([20, 22, 30, 32], fill=LTBROWN)

def draw_yam(d):
    # Rough brown root
    d.polygon([(12, 28), (20, 16), (38, 20), (35, 34), (20, 32)], fill=DKBROWN)

def draw_cassava(d):
    # Tapered woody root
    d.polygon([(10, 25), (40, 15), (38, 30)], fill=BROWN)

def draw_horseradish(d):
    # Long rough cream root
    d.polygon([(18, 15), (28, 15), (23, 44)], fill=CREAM)
    # Root wrinkles
    d.line([(20, 25), (26, 25)], fill=LTBROWN)
    d.line([(21, 35), (25, 35)], fill=LTBROWN)

def draw_lotus_root(d):
    # Slice of lotus root showing holes
    d.ellipse([12, 12, 38, 38], fill=CREAM)
    # Holes (transparency or dark brown center)
    for p in [(25, 18), (18, 25), (32, 25), (25, 32), (21, 21), (29, 21), (21, 29), (29, 29)]:
        d.ellipse([p[0]-2, p[1]-2, p[0]+2, p[1]+2], fill=DKBROWN)

def draw_bamboo_shoot(d):
    # Layered cone sheaths
    d.polygon([(25, 10), (15, 42), (35, 42)], fill=YELLOW)
    d.polygon([(25, 20), (18, 42), (32, 42)], fill=DKYELLOW)
    d.polygon([(25, 30), (22, 42), (28, 42)], fill=BROWN)

def draw_water_chestnut(d):
    # Dark brown flat-bottom bulb
    d.ellipse([14, 18, 36, 38], fill=DKBROWN)
    # Flat bottom
    d.rectangle([14, 34, 36, 38], fill=DKBROWN)
    # Light top sprout
    d.polygon([(25, 12), (22, 18), (28, 18)], fill=CREAM)

def draw_swiss_chard(d):
    # Green leaf
    d.ellipse([14, 12, 36, 38], fill=GREEN)
    # Bright red stem and veins
    d.line([(25, 38), (25, 46)], fill=RED, width=3)
    d.line([(25, 14), (25, 38)], fill=RED, width=2)
    d.line([(25, 20), (18, 15)], fill=RED, width=1)
    d.line([(25, 26), (32, 21)], fill=RED, width=1)

DRAWINGS = {
    "carrot": draw_carrot,
    "broccoli": draw_broccoli,
    "cauliflower": draw_cauliflower,
    "eggplant": draw_eggplant,
    "tomato": draw_tomato,
    "potato": draw_potato,
    "sweet_potato": draw_sweet_potato,
    "bell_pepper_red": draw_bell_pepper_red,
    "bell_pepper_green": draw_bell_pepper_green,
    "cucumber": draw_cucumber,
    "zucchini": draw_zucchini,
    "pumpkin": draw_pumpkin,
    "butternut_squash": draw_butternut_squash,
    "garlic": draw_garlic,
    "onion_red": draw_onion_red,
    "onion_yellow": draw_onion_yellow,
    "radish": draw_radish,
    "turnip": draw_turnip,
    "beetroot": draw_beetroot,
    "celery": draw_celery,
    "asparagus": draw_asparagus,
    "brussels_sprout": draw_brussels_sprout,
    "cabbage_green": draw_cabbage_green,
    "cabbage_red": draw_cabbage_red,
    "spinach_leaf": draw_spinach_leaf,
    "lettuce_romaine": draw_lettuce_romaine,
    "kale_leaf": draw_kale_leaf,
    "corn_on_the_cob": draw_corn_on_the_cob,
    "pea_pod": draw_pea_pod,
    "green_bean": draw_green_bean,
    "okra": draw_okra,
    "artichoke": draw_artichoke,
    "leek": draw_leek,
    "scallion": draw_scallion,
    "ginger_root": draw_ginger_root,
    "mushroom_button": draw_mushroom_button,
    "shiitake_mushroom": draw_shiitake_mushroom,
    "chilli_red": draw_chilli_red,
    "chilli_green": draw_chilli_green,
    "bitter_melon": draw_bitter_melon,
    "daikon_radish": draw_daikon_radish,
    "fennel_bulb": draw_fennel_bulb,
    "taro_root": draw_taro_root,
    "yam": draw_yam,
    "cassava": draw_cassava,
    "horseradish": draw_horseradish,
    "lotus_root": draw_lotus_root,
    "bamboo_shoot": draw_bamboo_shoot,
    "water_chestnut": draw_water_chestnut,
    "swiss_chard": draw_swiss_chard
}

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    # Save the base sprite
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    base_img.save(path)
    print(f"  Saved raw: {path}")

if __name__ == "__main__":
    print(f"Generating 50 raw vegetable sprites inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating raw vegetable sprites!")
