import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/kitchen"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def enforce_max_colors(img, max_colors=9):
    pixels = list(img.getdata())
    unique_colors = set(pixels)
    if len(unique_colors) <= max_colors:
        return img
    
    alpha = img.split()[3]
    rgb = img.convert("RGB")
    
    quantized_rgb = rgb.quantize(colors=max_colors - 1, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    quantized_rgb = quantized_rgb.convert("RGB")
    
    w, h = img.size
    new_data = []
    rgb_pixels = list(quantized_rgb.getdata())
    alpha_pixels = list(alpha.getdata())
    
    for i in range(len(rgb_pixels)):
        a = alpha_pixels[i]
        if a < 128:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(rgb_pixels[i] + (255,))
            
    out_img = Image.new("RGBA", (w, h))
    out_img.putdata(new_data)
    return out_img

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img = enforce_max_colors(img, max_colors=9)
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)

# Palette
RED       = (210, 45, 45, 255)
DKRED     = (130, 20, 20, 255)
BLUE      = (50, 110, 210, 255)
DKBLUE    = (20, 50, 140, 255)
YELLOW    = (240, 200, 30, 255)
DKYELLOW  = (180, 150, 20, 255)
GREEN     = (50, 160, 60, 255)
DKGREEN   = (20, 90, 20, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
ORANGE    = (235, 110, 25, 255)
BROWN     = (130, 85, 45, 255)
DKBROWN   = (80, 50, 25, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (180, 180, 190, 255)
TAN       = (210, 180, 140, 255)
GLASS     = (150, 200, 255, 180)
PINK      = (235, 130, 160, 255)

def draw_wheel(draw, x, y, r, tire=BLACK, rim=SILVER, center=DKGREY):
    draw.ellipse([x-r, y-r, x+r, y+r], fill=tire)
    if r > 2:
        draw.ellipse([x-r+1, y-r+1, x+r-1, y+r-1], fill=rim)
        draw.ellipse([x-r+2, y-r+2, x+r-2, y+r-2], fill=center)
        if r > 4:
            draw.ellipse([x-1, y-1, x+1, y+1], fill=BLACK)

# 1. rice_cooker
def draw_rice_cooker(draw):
    draw.rounded_rectangle([10, 16, 40, 42], radius=4, fill=WHITE)
    draw.rounded_rectangle([12, 18, 38, 42], radius=2, fill=SILVER)
    draw.rectangle([18, 28, 32, 36], fill=DKGREY)
    draw.ellipse([22, 32, 24, 34], fill=RED)
    draw.ellipse([28, 32, 30, 34], fill=GREEN)
    draw.rounded_rectangle([14, 12, 36, 16], radius=2, fill=DKGREY)

# 2. sous_vide
def draw_sous_vide(draw):
    draw.rectangle([16, 34, 34, 40], fill=GREY)
    draw.rectangle([20, 6, 30, 38], fill=BLACK)
    draw.rectangle([22, 8, 28, 16], fill=BLUE)
    draw.line([(24, 12), (26, 12)], fill=WHITE, width=1)
    draw.ellipse([25, 30, 25, 30], fill=BLUE)

# 3. dehydrator
def draw_dehydrator(draw):
    draw.rounded_rectangle([10, 12, 40, 44], radius=4, fill=GREY)
    for i in range(16, 40, 6):
        draw.line([(12, i), (38, i)], fill=DKGREY, width=2)
        draw.line([(14, i), (36, i)], fill=WHITE, width=1)
    draw.rectangle([18, 40, 32, 42], fill=BLACK)

# 4. vacuum_sealer
def draw_vacuum_sealer(draw):
    draw.rounded_rectangle([6, 22, 44, 34], radius=3, fill=WHITE)
    draw.rectangle([8, 24, 42, 32], fill=SILVER)
    draw.rectangle([14, 25, 20, 27], fill=BLUE)
    draw.rectangle([30, 25, 36, 27], fill=RED)
    draw.line([(6, 30), (44, 30)], fill=DKGREY, width=1)

# 5. panini_press
def draw_panini_press(draw):
    draw.rectangle([8, 26, 42, 38], fill=DKGREY)
    draw.rectangle([10, 12, 40, 24], fill=SILVER)
    draw.line([(10, 16), (40, 16)], fill=BLACK, width=2)
    draw.line([(8, 24), (42, 24)], fill=BLACK, width=2)
    for i in range(12, 38, 4):
        draw.line([(i, 26), (i, 38)], fill=BLACK, width=1)

# 6. water_pitcher
def draw_water_pitcher(draw):
    draw.rounded_rectangle([14, 16, 34, 44], radius=3, fill=GLASS)
    draw.rectangle([16, 22, 32, 42], fill=LIGHTBLUE)
    draw.arc([30, 20, 38, 36], 270, 90, fill=WHITE, width=3)

# 7. dough_cutter
def draw_dough_cutter(draw):
    draw.rectangle([12, 24, 38, 38], fill=SILVER)
    draw.rounded_rectangle([10, 14, 40, 24], radius=3, fill=BROWN)
    draw.line([(12, 38), (38, 38)], fill=WHITE, width=1)

# 8. pie_server
def draw_pie_server(draw):
    draw.polygon([(14, 32), (36, 32), (25, 12)], fill=SILVER)
    draw.line([(25, 32), (25, 44)], fill=BLACK, width=3)

# 9. cookie_jar
def draw_cookie_jar(draw):
    draw.rounded_rectangle([12, 18, 38, 44], radius=6, fill=WHITE)
    draw.ellipse([18, 12, 32, 18], fill=WHITE)
    draw.rectangle([18, 28, 32, 34], fill=BROWN)

# 10. bagel_cutter
def draw_bagel_cutter(draw):
    draw.rectangle([14, 18, 36, 44], fill=WHITE, outline=GREY)
    draw.polygon([(16, 24), (34, 24), (25, 12)], fill=SILVER)
    draw.ellipse([20, 28, 30, 38], fill=BROWN)

# 11. juicer_press
def draw_juicer_press(draw):
    draw.line([(14, 22), (36, 22)], fill=SILVER, width=4)
    draw.line([(12, 18), (34, 18)], fill=STEEL, width=2)
    draw.line([(14, 22), (8, 42)], fill=SILVER, width=3)
    draw.line([(12, 18), (6, 38)], fill=STEEL, width=3)

# 12. pot_holder
def draw_pot_holder(draw):
    draw.rounded_rectangle([10, 10, 40, 40], radius=3, fill=RED)
    draw.rounded_rectangle([12, 12, 38, 38], radius=2, fill=WHITE)
    for i in range(12, 38, 4):
        draw.line([(12, i), (i, 12)], fill=GREY, width=1)
        draw.line([(i, 38), (38, i)], fill=GREY, width=1)

# 13. cupcake_carrier
def draw_cupcake_carrier(draw):
    draw.rounded_rectangle([10, 24, 40, 42], radius=4, fill=WHITE)
    draw.rounded_rectangle([12, 16, 38, 34], radius=6, fill=GLASS)
    draw.ellipse([22, 12, 28, 16], fill=WHITE)

# 14. taco_holder
def draw_taco_holder(draw):
    for i in [10, 22, 34]:
        draw.polygon([(i, 38), (i+6, 20), (i+12, 38)], fill=YELLOW)
        draw.rectangle([i+2, 24, i+10, 32], fill=GREEN)
    draw.line([(6, 38), (44, 38)], fill=SILVER, width=2)

# 15. ice_pop_mold
def draw_ice_pop_mold(draw):
    draw.rectangle([8, 32, 42, 40], fill=WHITE)
    for x in [14, 25, 36]:
        draw.rounded_rectangle([x-4, 18, x+4, 32], radius=2, fill=PINK)
        draw.line([(x, 32), (x, 44)], fill=TAN, width=2)

# 16. lunch_box
def draw_lunch_box(draw):
    draw.rounded_rectangle([10, 16, 40, 42], radius=5, fill=RED)
    draw.rectangle([14, 12, 36, 16], fill=DKGREY)
    draw.line([(10, 28), (40, 28)], fill=SILVER, width=2)

# 17. apron_hook
def draw_apron_hook(draw):
    draw.rectangle([20, 12, 30, 24], fill=BROWN) # Wood plaque
    draw.line([(25, 20), (25, 36)], fill=STEEL, width=3) # Metal hook
    draw.line([(25, 36), (32, 32)], fill=STEEL, width=3)
    draw.ellipse([18, 30, 28, 44], fill=BLUE) # Hanging apron representation

# 18. sponge_holder
def draw_sponge_holder(draw):
    draw.rectangle([12, 26, 38, 40], fill=WHITE, outline=GREY)
    draw.rectangle([16, 18, 34, 30], fill=GREEN)
    draw.rectangle([16, 26, 34, 30], fill=YELLOW)

# 19. soap_dispenser
def draw_soap_dispenser(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=4, fill=GLASS)
    draw.rectangle([18, 20, 32, 42], fill=LIGHTBLUE)
    draw.rectangle([22, 12, 28, 18], fill=SILVER)
    draw.line([(22, 14), (16, 16)], fill=SILVER, width=2)

# 20. knife_sharpener
def draw_knife_sharpener(draw):
    draw.rounded_rectangle([8, 30, 42, 42], radius=2, fill=BLACK) # Base
    draw.rectangle([14, 20, 22, 30], fill=GREY) # Sharpening slot 1
    draw.rectangle([28, 20, 36, 30], fill=WHITE) # Sharpening slot 2
    draw.line([(18, 18), (32, 18)], fill=STEEL, width=2) # Handle

# 21. timer_hourglass
def draw_timer_hourglass(draw):
    draw.polygon([(14, 12), (36, 12), (25, 25), (25, 25)], fill=GLASS) # Glass top
    draw.polygon([(25, 25), (25, 25), (36, 38), (14, 38)], fill=GLASS) # Glass bottom
    draw.line([(12, 10), (38, 10)], fill=BROWN, width=3) # Wood top
    draw.line([(12, 40), (38, 40)], fill=BROWN, width=3) # Wood bottom
    draw.line([(14, 10), (14, 40)], fill=STEEL, width=2) # Supports
    draw.line([(36, 10), (36, 40)], fill=STEEL, width=2)
    # Sand
    draw.polygon([(18, 14), (32, 14), (25, 24)], fill=YELLOW)
    draw.polygon([(22, 38), (28, 38), (25, 30)], fill=YELLOW)

# 22. sink_strainer
def draw_sink_strainer(draw):
    draw.ellipse([10, 10, 40, 40], fill=SILVER)
    draw.ellipse([14, 14, 36, 36], fill=STEEL)
    draw.ellipse([18, 18, 32, 32], fill=DKGREY)
    for x in [21, 25, 29]:
        for y in [21, 25, 29]:
            draw.ellipse([x-1, y-1, x+1, y+1], fill=BLACK) # Drainage holes
    draw.ellipse([23, 23, 27, 27], fill=SILVER) # Center post knob

# 23. wine_cradle
def draw_wine_cradle(draw):
    draw.arc([10, 20, 40, 44], 0, 180, fill=BROWN, width=3) # Cradle body
    draw.line([(10, 24), (20, 12)], fill=BROWN, width=3)
    # Wine bottle placed diagonally
    draw.polygon([(12, 34), (36, 18), (38, 22), (14, 38)], fill=DKGREEN)
    draw.line([(36, 18), (44, 12)], fill=BROWN, width=2) # Cork neck

# 24. corn_holders
def draw_corn_holders(draw):
    for y in [18, 32]:
        draw.rounded_rectangle([10, y, 22, y+6], radius=2, fill=YELLOW) # Handle
        draw.line([(22, y+3), (38, y+3)], fill=STEEL, width=1) # Prongs
        draw.line([(22, y+1), (38, y+1)], fill=STEEL, width=1)
        draw.ellipse([34, y-2, 44, y+8], fill=DKYELLOW) # Corn cob slice representation

# 25. meat_hook
def draw_meat_hook(draw):
    draw.line([(25, 4), (25, 16)], fill=STEEL, width=3) # Top chain
    draw.arc([16, 16, 26, 32], 90, 270, fill=STEEL, width=3) # S-curve top
    draw.arc([24, 26, 34, 42], 270, 90, fill=STEEL, width=3) # S-curve bottom pointing up
    draw.polygon([(34, 26), (34, 30), (38, 28)], fill=SILVER) # Sharp point

# 26. pepper_corer
def draw_pepper_corer(draw):
    draw.rectangle([8, 22, 22, 28], fill=RED) # Handle
    draw.line([(22, 25), (38, 25)], fill=STEEL, width=3) # Metal shaft
    draw.ellipse([34, 20, 42, 30], fill=SILVER) # Serrated loop tip
    draw.ellipse([36, 22, 40, 28], fill=255)

# 27. herb_scissors
def draw_herb_scissors(draw):
    draw.ellipse([8, 14, 18, 24], fill=GREEN) # Handle 1
    draw.ellipse([8, 26, 18, 36], fill=GREEN) # Handle 2
    # Multiple blades
    for y in [18, 22, 26]:
        draw.line([(18, y), (42, y)], fill=SILVER, width=1)

# 28. trivet_stone
def draw_trivet_stone(draw):
    draw.rounded_rectangle([10, 10, 40, 40], radius=4, fill=WHITE) # Marble base
    # Grey marble veins
    draw.line([(12, 12), (24, 30)], fill=GREY, width=2)
    draw.line([(22, 20), (36, 14)], fill=GREY, width=1)
    draw.line([(18, 28), (38, 38)], fill=GREY, width=1)

# 29. whiskey_decanter
def draw_whiskey_decanter(draw):
    draw.rounded_rectangle([14, 18, 36, 44], radius=3, fill=GLASS)
    draw.rectangle([16, 20, 34, 42], fill=BROWN) # Whiskey
    draw.rectangle([20, 10, 30, 18], fill=GLASS) # Neck
    draw.ellipse([18, 6, 32, 12], fill=GLASS) # Round stopper

# 30. oil_mister
def draw_oil_mister(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=3, fill=SILVER) # Metal container
    draw.rectangle([18, 10, 32, 18], fill=BLACK) # Spray head
    draw.rectangle([20, 12, 26, 16], fill=WHITE) # Button
    # Spray mist lines
    draw.line([(16, 14), (6, 11)], fill=LIGHTBLUE, width=1)
    draw.line([(16, 14), (6, 17)], fill=LIGHTBLUE, width=1)

# 31. pot_lid_holder
def draw_pot_lid_holder(draw):
    draw.rectangle([8, 36, 42, 40], fill=DKGREY) # Base plate
    for x in [14, 25, 36]:
        draw.arc([x-4, 16, x+4, 36], 180, 360, fill=STEEL, width=2) # Wire loops
    # Pot lid resting inside
    draw.ellipse([20, 20, 36, 36], fill=GLASS)

# 32. banana_hanger
def draw_banana_hanger(draw):
    draw.line([(25, 42), (25, 12)], fill=STEEL, width=3) # Vertical stand
    draw.ellipse([16, 40, 34, 44], fill=STEEL) # Base
    draw.arc([16, 8, 25, 16], 90, 270, fill=STEEL, width=3) # Top hanger hook
    # Hanging bananas
    draw.arc([10, 14, 22, 32], 0, 120, fill=YELLOW, width=3)
    draw.arc([12, 16, 24, 34], 0, 120, fill=YELLOW, width=3)

# 33. egg_piercer
def draw_egg_piercer(draw):
    draw.ellipse([14, 14, 36, 36], fill=WHITE, outline=GREY) # Circular base
    draw.ellipse([20, 20, 30, 30], fill=RED) # Punch button
    draw.line([(25, 21), (25, 29)], fill=STEEL, width=2) # Metal needle pin

# 34. tapioca_scoop
def draw_tapioca_scoop(draw):
    draw.line([(26, 20), (46, 10)], fill=BROWN, width=3) # Handle
    draw.ellipse([10, 16, 28, 34], fill=SILVER) # Scoop rim
    draw.ellipse([12, 18, 26, 32], fill=255) # Transparent center mesh
    for x, y in [(16, 22), (22, 22), (16, 28), (22, 28)]:
        draw.ellipse([x-1, y-1, x+1, y+1], fill=BLACK) # Boba pearls caught in scoop

# 35. sauce_dispenser
def draw_sauce_dispenser(draw):
    draw.rounded_rectangle([16, 18, 34, 44], radius=4, fill=YELLOW) # Squeeze bottle (mustard/sauce)
    draw.polygon([(20, 18), (30, 18), (25, 8)], fill=YELLOW) # Pointed nozzle spout
    draw.line([(18, 22), (32, 22)], fill=DKYELLOW, width=2)

# 36. toothpick_dispenser
def draw_toothpick_dispenser(draw):
    draw.rounded_rectangle([14, 16, 36, 42], radius=4, fill=WHITE)
    draw.rectangle([20, 12, 30, 16], fill=GREEN) # Top push button
    draw.line([(25, 16), (25, 28)], fill=GREY, width=2)
    # Toothpick emerging
    draw.line([(25, 8), (25, 12)], fill=TAN, width=2)

# 37. tea_bag_squeezer
def draw_tea_bag_squeezer(draw):
    draw.line([(10, 25), (38, 20)], fill=SILVER, width=3) # Tong 1
    draw.line([(10, 25), (38, 30)], fill=SILVER, width=3) # Tong 2
    draw.rectangle([34, 16, 42, 22], fill=STEEL) # Perforated squeezing plates
    draw.rectangle([34, 28, 42, 34], fill=STEEL)

# 38. can_punch
def draw_can_punch(draw):
    draw.rectangle([8, 22, 26, 28], fill=RED) # Handle
    draw.line([(26, 25), (42, 25)], fill=STEEL, width=4) # Metal body
    draw.polygon([(38, 25), (44, 22), (40, 28)], fill=SILVER) # Punch tooth point

# 39. ice_bag
def draw_ice_bag(draw):
    draw.polygon([(14, 20), (36, 20), (32, 44), (18, 44)], fill=WHITE) # Canvas bag
    draw.ellipse([18, 16, 32, 24], fill=WHITE)
    draw.line([(16, 20), (34, 20)], fill=BROWN, width=2) # Drawstring tie
    draw.rectangle([22, 32, 28, 38], fill=DKBLUE) # Cold ice logo stamp

# 40. cocktail_pick
def draw_cocktail_pick(draw):
    draw.line([(12, 38), (38, 12)], fill=STEEL, width=2) # Metal spear shaft
    draw.ellipse([36, 10, 40, 14], fill=RED) # Decorative top bead
    draw.ellipse([18, 26, 26, 34], fill=GREEN) # Olive skewered

# 41. champagne_flute
def draw_champagne_flute(draw):
    draw.polygon([(18, 10), (32, 10), (28, 28), (22, 28)], fill=GLASS) # Tall bowl
    draw.rectangle([21, 14, 29, 26], fill=YELLOW) # Champagne
    draw.line([(25, 28), (25, 42)], fill=GLASS, width=2) # Stem
    draw.ellipse([18, 40, 32, 44], fill=GLASS) # Base

# 42. carafe
def draw_carafe(draw):
    draw.polygon([(18, 14), (32, 14), (36, 24), (14, 24)], fill=GLASS) # Neck
    draw.ellipse([12, 22, 38, 44], fill=GLASS) # Flared bottom body
    draw.ellipse([14, 24, 36, 42], fill=LIGHTBLUE) # Water inside

# 43. ramekin
def draw_ramekin(draw):
    draw.rounded_rectangle([10, 22, 40, 42], radius=2, fill=WHITE) # Ramekin bowl
    # Ribbed texture lines on ceramic sides
    for x in range(14, 38, 4):
        draw.line([(x, 26), (x, 40)], fill=GREY, width=1)
    draw.rectangle([12, 16, 38, 22], fill=YELLOW) # Souffle rising top

# 44. moka_pot
def draw_moka_pot(draw):
    draw.polygon([(16, 28), (34, 28), (32, 44), (18, 44)], fill=SILVER) # Bottom chamber
    draw.polygon([(18, 14), (32, 14), (34, 26), (16, 26)], fill=SILVER) # Top chamber
    draw.line([(14, 18), (18, 20)], fill=SILVER, width=3) # Spout
    draw.arc([28, 20, 38, 38], 270, 90, fill=BLACK, width=3) # Handle

# 45. siphon_coffee
def draw_siphon_coffee(draw):
    draw.ellipse([16, 8, 34, 22], fill=GLASS) # Top bulb
    draw.line([(25, 22), (25, 34)], fill=GLASS, width=3) # Connecting tube
    draw.ellipse([16, 28, 34, 42], fill=GLASS) # Bottom globe
    draw.ellipse([18, 30, 32, 40], fill=BROWN) # Boiling coffee
    draw.line([(12, 18), (12, 44)], fill=BLACK, width=2) # Metal stand frame

# 46. whipped_cream_dispenser
def draw_whipped_cream_dispenser(draw):
    draw.rounded_rectangle([16, 16, 34, 44], radius=3, fill=SILVER) # Aluminum bottle
    draw.rectangle([18, 8, 32, 16], fill=WHITE) # Plastic charger head
    draw.line([(20, 10), (14, 14)], fill=WHITE, width=3) # Whipped nozzle
    draw.line([(28, 10), (32, 14)], fill=WHITE, width=2) # Lever trigger

# 47. gravy_separator
def draw_gravy_separator(draw):
    draw.rounded_rectangle([16, 20, 36, 42], radius=4, fill=GLASS) # Pitcher
    draw.line([(16, 40), (10, 22)], fill=GLASS, width=3) # Low spout drawing from bottom
    draw.arc([32, 24, 40, 38], 270, 90, fill=WHITE, width=2) # Handle
    draw.rectangle([18, 22, 34, 40], fill=BROWN) # Gravy broth
    draw.rectangle([18, 22, 34, 26], fill=YELLOW) # Fat layer floating on top

# 48. roasting_rack
def draw_roasting_rack(draw):
    draw.rectangle([8, 28, 42, 40], fill=GREY, outline=DKGREY) # Roasting pan
    for x in range(12, 40, 4):
        draw.line([(x, 24), (x+2, 32)], fill=STEEL, width=1) # Slanted V-rack wires
        draw.line([(x, 32), (x-2, 24)], fill=STEEL, width=1)

# 49. splatter_screen
def draw_splatter_screen(draw):
    draw.ellipse([12, 12, 38, 38], fill=SILVER) # Outer metal ring
    draw.ellipse([14, 14, 36, 36], fill=255) # Transparent mesh
    for i in range(14, 36, 4):
        draw.line([(i, 14), (i, 36)], fill=GREY, width=1) # Mesh grid lines
        draw.line([(14, i), (36, i)], fill=GREY, width=1)
    draw.line([(25, 38), (25, 48)], fill=BLACK, width=3) # Handle

# 50. steamer_basket
def draw_steamer_basket(draw):
    draw.rectangle([10, 24, 40, 42], fill=TAN) # Bamboo steamer body
    # Woven basket texture lines
    for x in range(12, 40, 4):
        draw.line([(x, 24), (x, 42)], fill=DKBROWN, width=1)
    draw.line([(10, 33), (40, 33)], fill=DKBROWN, width=2) # Intersecting weave
    draw.rounded_rectangle([12, 16, 38, 24], radius=2, fill=TAN) # Lid

items = [
    ("rice_cooker", draw_rice_cooker),
    ("sous_vide", draw_sous_vide),
    ("dehydrator", draw_dehydrator),
    ("vacuum_sealer", draw_vacuum_sealer),
    ("panini_press", draw_panini_press),
    ("water_pitcher", draw_water_pitcher),
    ("dough_cutter", draw_dough_cutter),
    ("pie_server", draw_pie_server),
    ("cookie_jar", draw_cookie_jar),
    ("bagel_cutter", draw_bagel_cutter),
    ("juicer_press", draw_juicer_press),
    ("pot_holder", draw_pot_holder),
    ("cupcake_carrier", draw_cupcake_carrier),
    ("taco_holder", draw_taco_holder),
    ("ice_pop_mold", draw_ice_pop_mold),
    ("lunch_box", draw_lunch_box),
    ("apron_hook", draw_apron_hook),
    ("sponge_holder", draw_sponge_holder),
    ("soap_dispenser", draw_soap_dispenser),
    ("knife_sharpener", draw_knife_sharpener),
    ("timer_hourglass", draw_timer_hourglass),
    ("sink_strainer", draw_sink_strainer),
    ("wine_cradle", draw_wine_cradle),
    ("corn_holders", draw_corn_holders),
    ("meat_hook", draw_meat_hook),
    ("pepper_corer", draw_pepper_corer),
    ("herb_scissors", draw_herb_scissors),
    ("trivet_stone", draw_trivet_stone),
    ("whiskey_decanter", draw_whiskey_decanter),
    ("oil_mister", draw_oil_mister),
    ("pot_lid_holder", draw_pot_lid_holder),
    ("banana_hanger", draw_banana_hanger),
    ("egg_piercer", draw_egg_piercer),
    ("tapioca_scoop", draw_tapioca_scoop),
    ("sauce_dispenser", draw_sauce_dispenser),
    ("toothpick_dispenser", draw_toothpick_dispenser),
    ("tea_bag_squeezer", draw_tea_bag_squeezer),
    ("can_punch", draw_can_punch),
    ("ice_bag", draw_ice_bag),
    ("cocktail_pick", draw_cocktail_pick),
    ("champagne_flute", draw_champagne_flute),
    ("carafe", draw_carafe),
    ("ramekin", draw_ramekin),
    ("moka_pot", draw_moka_pot),
    ("siphon_coffee", draw_siphon_coffee),
    ("whipped_cream_dispenser", draw_whipped_cream_dispenser),
    ("gravy_separator", draw_gravy_separator),
    ("roasting_rack", draw_roasting_rack),
    ("splatter_screen", draw_splatter_screen),
    ("steamer_basket", draw_steamer_basket)
]

print(f"Generating {len(items)} unique detailed kitchen sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 unique kitchen sprites generated successfully!")
