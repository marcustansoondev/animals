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

def draw_banana_pepper(d):
    d.arc([14, 14, 36, 36], 0, 180, fill=YELLOW, width=4)
    d.line([(34, 25), (38, 21)], fill=GREEN, width=2)

def draw_jalapeno_pepper(d):
    d.arc([14, 14, 36, 36], 0, 180, fill=GREEN, width=5)
    d.line([(34, 25), (37, 20)], fill=DKGREEN, width=2)

def draw_shishito_pepper(d):
    # Wrinkled green pepper
    d.polygon([(14, 25), (36, 18), (38, 22), (16, 29)], fill=GREEN)
    d.line([(20, 24), (32, 20)], fill=LTGREEN)
    d.line([(14, 25), (10, 28)], fill=DKGREEN, width=2)

def draw_birds_eye_chilli(d):
    # Small very thin red pepper
    d.line([(15, 35), (35, 15)], fill=RED, width=2)
    d.line([(35, 15), (38, 12)], fill=GREEN, width=1)

def draw_anaheim_pepper(d):
    # Long light green pepper
    d.polygon([(12, 38), (38, 12), (36, 8), (10, 34)], fill=LTGREEN)
    d.line([(38, 12), (42, 8)], fill=GREEN, width=2)

def draw_hungarian_wax_pepper(d):
    # Pale yellow pepper
    d.polygon([(12, 38), (38, 12), (36, 8), (10, 34)], fill=CREAM)
    d.line([(38, 12), (42, 8)], fill=GREEN, width=2)

def draw_cherry_pepper(d):
    # Small round red pepper
    d.ellipse([16, 18, 34, 36], fill=RED)
    d.ellipse([25, 18, 34, 36], fill=DKRED)
    d.rectangle([23, 10, 27, 18], fill=GREEN)

def draw_bell_pepper_yellow(d):
    d.rectangle([14, 16, 36, 40], fill=YELLOW)
    d.ellipse([12, 16, 24, 40], fill=YELLOW)
    d.ellipse([26, 16, 38, 40], fill=DKYELLOW)
    d.rectangle([23, 8, 27, 16], fill=GREEN)

def draw_bell_pepper_orange(d):
    d.rectangle([14, 16, 36, 40], fill=ORANGE)
    d.ellipse([12, 16, 24, 40], fill=ORANGE)
    d.ellipse([26, 16, 38, 40], fill=DKORANGE)
    d.rectangle([23, 8, 27, 16], fill=GREEN)

def draw_elephant_garlic(d):
    # Massive garlic bulb
    d.ellipse([10, 16, 40, 44], fill=CREAM)
    d.polygon([(25, 8), (16, 20), (34, 20)], fill=WHITE)
    d.line([(22, 44), (22, 47)], fill=LTBROWN)
    d.line([(28, 44), (28, 47)], fill=LTBROWN)

def draw_pearl_onion(d):
    # Tiny white onion
    d.ellipse([18, 20, 32, 34], fill=WHITE)
    d.polygon([(25, 14), (20, 22), (30, 22)], fill=CREAM)
    d.line([(25, 34), (25, 38)], fill=LTBROWN)

def draw_cipollini_onion(d):
    # Flat yellow onion
    d.ellipse([12, 22, 38, 38], fill=YELLOW)
    d.ellipse([25, 22, 38, 38], fill=DKYELLOW)
    d.line([(25, 38), (25, 42)], fill=LTBROWN)

def draw_vidalia_onion(d):
    # Sweet yellow onion, slightly flat
    d.ellipse([13, 20, 37, 39], fill=YELLOW)
    d.ellipse([25, 20, 37, 39], fill=DKYELLOW)
    d.line([(25, 39), (25, 43)], fill=CREAM)

def draw_chives(d):
    # Thin green straw shoots
    d.line([(18, 44), (18, 8)], fill=GREEN, width=1)
    d.line([(24, 44), (24, 6)], fill=LTGREEN, width=1)
    d.line([(30, 44), (30, 8)], fill=GREEN, width=1)

def draw_garlic_chives(d):
    # Flat green grass shoots
    d.line([(18, 44), (18, 8)], fill=GREEN, width=2)
    d.line([(25, 44), (25, 6)], fill=LTGREEN, width=2)
    d.line([(32, 44), (32, 8)], fill=GREEN, width=2)

def draw_lovage(d):
    # Celery-like leafy sprig
    d.line([(25, 44), (25, 20)], fill=GREEN, width=2)
    d.ellipse([15, 14, 25, 24], fill=LTGREEN)
    d.ellipse([25, 10, 35, 20], fill=GREEN)
    d.ellipse([21, 20, 29, 28], fill=DKGREEN)

def draw_purslane(d):
    # Reddish stems, fat green paddle leaves
    d.line([(25, 44), (25, 20)], fill=RED, width=2)
    d.ellipse([14, 14, 22, 22], fill=GREEN)
    d.ellipse([28, 14, 36, 22], fill=LTGREEN)
    d.ellipse([20, 22, 30, 30], fill=GREEN)

def draw_tatsoi(d):
    # Rosette spoon-shaped dark green leaves
    d.ellipse([12, 22, 24, 34], fill=DKGREEN)
    d.ellipse([26, 22, 38, 34], fill=DKGREEN)
    d.ellipse([18, 14, 32, 26], fill=DKGREEN)
    d.line([(25, 30), (25, 44)], fill=WHITE, width=2)

def draw_mizuna(d):
    # Feathery green rosette leaf
    d.polygon([(25, 10), (18, 20), (22, 22), (15, 32), (25, 44)], fill=LTGREEN)
    d.polygon([(25, 10), (32, 20), (28, 22), (35, 32), (25, 44)], fill=GREEN)

def draw_komatsuna(d):
    # Spinach-like leaf, lighter stem
    d.ellipse([15, 12, 35, 36], fill=GREEN)
    d.line([(25, 30), (25, 45)], fill=LTGREEN, width=3)

def draw_shungiku(d):
    # Chrysanthemum greens: serrated leaf
    d.polygon([(25, 8), (16, 18), (22, 22), (14, 32), (25, 44)], fill=GREEN)
    d.polygon([(25, 8), (34, 18), (28, 22), (36, 32), (25, 44)], fill=DKGREEN)

def draw_pea_shoots(d):
    # Tender green stems with curly tendrils
    d.line([(25, 44), (25, 18)], fill=LTGREEN, width=2)
    d.ellipse([18, 14, 24, 20], fill=GREEN)
    d.ellipse([26, 12, 32, 18], fill=GREEN)
    # Curly tendril
    d.arc([20, 8, 30, 18], 0, 180, fill=LTGREEN, width=1)

def draw_sunflower_sprouts(d):
    # Pair of green cotyledon leaves on pale stem
    d.line([(25, 44), (25, 20)], fill=WHITE, width=2)
    d.ellipse([14, 14, 24, 22], fill=LTGREEN)
    d.ellipse([26, 14, 36, 22], fill=GREEN)

def draw_alfalfa_sprouts(d):
    # Nest of thin white tangled stems, tiny green tips
    d.line([(18, 44), (20, 18)], fill=WHITE, width=1)
    d.line([(25, 44), (24, 12)], fill=WHITE, width=1)
    d.line([(32, 44), (29, 16)], fill=WHITE, width=1)
    d.ellipse([18, 16, 22, 20], fill=LTGREEN)
    d.ellipse([22, 10, 26, 14], fill=LTGREEN)
    d.ellipse([27, 14, 31, 18], fill=LTGREEN)

def draw_mung_bean_sprouts(d):
    # Thick white stem with yellow bean cap
    d.line([(25, 44), (25, 18)], fill=WHITE, width=3)
    d.ellipse([21, 12, 29, 18], fill=YELLOW)

def draw_soy_bean_sprouts(d):
    # Thick white stem with large yellow split bean cap
    d.line([(25, 44), (25, 20)], fill=WHITE, width=4)
    d.ellipse([20, 12, 30, 20], fill=YELLOW)
    d.line([(25, 12), (25, 20)], fill=DKYELLOW)

def draw_black_eyed_peas(d):
    # Tan peas with black eye spot
    d.ellipse([14, 20, 24, 28], fill=CREAM)
    d.ellipse([18, 23, 20, 25], fill=BLACK)
    d.ellipse([26, 22, 36, 30], fill=CREAM)
    d.ellipse([30, 25, 32, 27], fill=BLACK)

def draw_yardlong_bean(d):
    # Extremely long coiled green bean pod
    d.arc([14, 14, 36, 36], 0, 360, fill=GREEN, width=3)
    d.line([(14, 25), (10, 42)], fill=GREEN, width=3)

def draw_winged_bean(d):
    # Green pod with 4 frilly wings
    d.polygon([(16, 14), (34, 14), (27, 42), (23, 42)], fill=GREEN)
    # Frilly wing edge
    d.line([(16, 14), (23, 42)], fill=LTGREEN, width=2)
    d.line([(34, 14), (27, 42)], fill=LTGREEN, width=2)

def draw_hyacinth_bean(d):
    # Purple broad pod with white seam line
    d.polygon([(12, 20), (38, 20), (30, 34), (16, 34)], fill=PURPLE)
    d.line([(12, 20), (38, 20)], fill=WHITE, width=2)

def draw_butter_bean(d):
    # Large flat white bean
    d.ellipse([14, 18, 36, 32], fill=WHITE)
    d.arc([16, 20, 34, 30], 0, 180, fill=GRAY, width=1)

def draw_runner_bean(d):
    # Long rough flat green bean pod
    d.line([(10, 40), (40, 10)], fill=DKGREEN, width=5)
    # Texturing
    d.line([(15, 35), (35, 15)], fill=GREEN, width=1)

def draw_romanesco_broccoli(d):
    # Lime green spiral cone shape
    d.polygon([(25, 10), (12, 38), (38, 38)], fill=LTGREEN)
    # Spiraling fractal cones
    for y in range(16, 38, 6):
        d.ellipse([21, y, 29, y+4], fill=GREEN)
    d.rectangle([21, 38, 29, 44], fill=GREEN)

def draw_broccolini(d):
    # Long thin green stalks with small heads
    d.line([(20, 44), (20, 22)], fill=LTGREEN, width=2)
    d.line([(30, 44), (28, 20)], fill=LTGREEN, width=2)
    d.ellipse([16, 14, 24, 22], fill=GREEN)
    d.ellipse([24, 12, 32, 20], fill=DKGREEN)

def draw_rapini(d):
    # Green stalk, leaves, and tiny yellow flower buds
    d.line([(25, 44), (25, 20)], fill=GREEN, width=2)
    d.ellipse([16, 16, 24, 24], fill=LTGREEN)
    # Yellow buds
    d.point([(20, 18), (22, 20), (28, 16)], fill=YELLOW)

def draw_gai_lan(d):
    # Thick green stems, large dark leaves
    d.line([(25, 44), (25, 22)], fill=GREEN, width=3)
    d.ellipse([14, 12, 28, 26], fill=DKGREEN)
    d.ellipse([26, 14, 38, 28], fill=DKGREEN)

def draw_brussels_sprouts_purple(d):
    d.ellipse([16, 16, 34, 34], fill=PURPLE)
    d.ellipse([20, 16, 30, 34], fill=PINK)
    d.arc([16, 16, 34, 34], 0, 180, fill=DKPURPLE, width=2)

def draw_cauliflower_purple(d):
    d.ellipse([8, 12, 42, 42], fill=DKGREEN)
    d.ellipse([14, 14, 28, 28], fill=PURPLE)
    d.ellipse([22, 14, 36, 28], fill=DKPURPLE)
    d.ellipse([16, 22, 34, 36], fill=PURPLE)

def draw_cauliflower_orange(d):
    d.ellipse([8, 12, 42, 42], fill=DKGREEN)
    d.ellipse([14, 14, 28, 28], fill=ORANGE)
    d.ellipse([22, 14, 36, 28], fill=DKORANGE)
    d.ellipse([16, 22, 34, 36], fill=ORANGE)

def draw_cauliflower_green(d):
    d.ellipse([8, 12, 42, 42], fill=DKGREEN)
    d.ellipse([14, 14, 28, 28], fill=LTGREEN)
    d.ellipse([22, 14, 36, 28], fill=GREEN)
    d.ellipse([16, 22, 34, 36], fill=LTGREEN)

def draw_red_russian_kale(d):
    # Oak-like purple/green leaf
    d.polygon([(25, 10), (18, 22), (23, 24), (16, 34), (25, 44)], fill=GREEN)
    # Purple veins
    d.line([(25, 10), (25, 44)], fill=PURPLE, width=2)
    d.line([(25, 24), (19, 20)], fill=PURPLE, width=1)

def draw_lacinato_kale(d):
    # Long, bumpy dark blue-green leaf
    d.polygon([(20, 42), (22, 8), (28, 8), (30, 42)], fill=DKGREEN)
    # Bumpy texture lines
    for i in range(12, 38, 4):
        d.line([(22, i), (28, i)], fill=GREEN)

def draw_curly_endive(d):
    # Super frizzy green and white leaf head
    d.ellipse([14, 14, 36, 36], fill=WHITE)
    # Frizzy green edges
    d.arc([14, 14, 36, 36], 0, 360, fill=GREEN, width=3)
    d.arc([18, 18, 32, 32], 0, 360, fill=LTGREEN, width=2)

def draw_belgian_endive(d):
    # Pale yellow small bullet shape
    d.polygon([(20, 42), (25, 14), (30, 42)], fill=CREAM)
    d.polygon([(22, 28), (25, 14), (28, 28)], fill=YELLOW)

def draw_escarole(d):
    # Wavy broad leaves, green outer, pale inner
    d.ellipse([14, 14, 36, 36], fill=LTGREEN)
    d.ellipse([18, 18, 32, 32], fill=CREAM)
    # Wavy edges
    d.arc([14, 14, 36, 36], 0, 360, fill=GREEN, width=2)

def draw_butterhead_lettuce(d):
    # Soft loose green round head
    d.ellipse([14, 14, 36, 36], fill=GREEN)
    d.ellipse([18, 18, 32, 32], fill=LTGREEN)

def draw_iceberg_lettuce(d):
    # Dense tight pale green ball
    d.ellipse([13, 13, 37, 37], fill=LTGREEN)
    d.ellipse([18, 18, 32, 32], fill=WHITE)

def draw_red_leaf_lettuce(d):
    # Wavy leaves, red/purple tips, green base
    d.ellipse([14, 14, 36, 36], fill=GREEN)
    d.arc([14, 14, 36, 36], 0, 360, fill=RED, width=3)

def draw_oak_leaf_lettuce(d):
    # Lobed oak-like green leaves
    d.polygon([(25, 10), (18, 20), (22, 22), (16, 30), (25, 42)], fill=GREEN)
    d.polygon([(25, 10), (32, 20), (28, 22), (34, 30), (25, 42)], fill=LTGREEN)

def draw_celtuce(d):
    # Thick stem with leafy head
    d.rectangle([21, 24, 29, 44], fill=LTGREEN)
    d.polygon([(21, 24), (15, 8), (25, 24)], fill=GREEN)
    d.polygon([(29, 24), (35, 8), (25, 24)], fill=DKGREEN)

DRAWINGS = {
    "banana_pepper": draw_banana_pepper,
    "jalapeno_pepper": draw_jalapeno_pepper,
    "shishito_pepper": draw_shishito_pepper,
    "birds_eye_chilli": draw_birds_eye_chilli,
    "anaheim_pepper": draw_anaheim_pepper,
    "hungarian_wax_pepper": draw_hungarian_wax_pepper,
    "cherry_pepper": draw_cherry_pepper,
    "bell_pepper_yellow": draw_bell_pepper_yellow,
    "bell_pepper_orange": draw_bell_pepper_orange,
    "elephant_garlic": draw_elephant_garlic,
    "pearl_onion": draw_pearl_onion,
    "cipollini_onion": draw_cipollini_onion,
    "vidalia_onion": draw_vidalia_onion,
    "chives": draw_chives,
    "garlic_chives": draw_garlic_chives,
    "lovage": draw_lovage,
    "purslane": draw_purslane,
    "tatsoi": draw_tatsoi,
    "mizuna": draw_mizuna,
    "komatsuna": draw_komatsuna,
    "shungiku": draw_shungiku,
    "pea_shoots": draw_pea_shoots,
    "sunflower_sprouts": draw_sunflower_sprouts,
    "alfalfa_sprouts": draw_alfalfa_sprouts,
    "mung_bean_sprouts": draw_mung_bean_sprouts,
    "soy_bean_sprouts": draw_soy_bean_sprouts,
    "black_eyed_peas": draw_black_eyed_peas,
    "yardlong_bean": draw_yardlong_bean,
    "winged_bean": draw_winged_bean,
    "hyacinth_bean": draw_hyacinth_bean,
    "butter_bean": draw_butter_bean,
    "runner_bean": draw_runner_bean,
    "romanesco_broccoli": draw_romanesco_broccoli,
    "broccolini": draw_broccolini,
    "rapini": draw_rapini,
    "gai_lan": draw_gai_lan,
    "brussels_sprouts_purple": draw_brussels_sprouts_purple,
    "cauliflower_purple": draw_cauliflower_purple,
    "cauliflower_orange": draw_cauliflower_orange,
    "cauliflower_green": draw_cauliflower_green,
    "red_russian_kale": draw_red_russian_kale,
    "lacinato_kale": draw_lacinato_kale,
    "curly_endive": draw_curly_endive,
    "belgian_endive": draw_belgian_endive,
    "escarole": draw_escarole,
    "butterhead_lettuce": draw_butterhead_lettuce,
    "iceberg_lettuce": draw_iceberg_lettuce,
    "red_leaf_lettuce": draw_red_leaf_lettuce,
    "oak_leaf_lettuce": draw_oak_leaf_lettuce,
    "celtuce": draw_celtuce
}

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    base_img.save(path)
    print(f"  Saved raw: {path}")

if __name__ == "__main__":
    print(f"Generating 50 raw vegetable sprites (batch 3) inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating raw vegetable sprites (batch 3)!")
