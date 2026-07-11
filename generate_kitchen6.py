import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/kitchen"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def enforce_max_colors(img, max_colors=9):
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

def draw_shadow(draw, box):
    draw.ellipse([box[0], box[3]-2, box[2], box[3]+4], fill=(0,0,0,100))

# 1. rice_cooker
def draw_rice_cooker(draw):
    draw_shadow(draw, [8, 16, 42, 44])
    draw.rounded_rectangle([10, 16, 40, 42], radius=6, fill=SILVER) # Main body
    draw.rounded_rectangle([12, 16, 38, 42], radius=4, fill=WHITE) # Face highlight
    draw.rounded_rectangle([8, 12, 42, 18], radius=3, fill=STEEL) # Lid base
    draw.ellipse([20, 8, 30, 14], fill=DKGREY) # Lid handle
    draw.rectangle([18, 28, 32, 38], fill=DKGREY) # Control panel
    draw.ellipse([20, 32, 24, 36], fill=DKRED) # LED Off
    draw.ellipse([28, 32, 32, 36], fill=GREEN) # LED On
    draw.line([(10, 20), (40, 20)], fill=GREY, width=1) # Seam
    draw.line([(14, 16), (14, 40)], fill=WHITE, width=2) # Left glare
    draw.line([(38, 16), (38, 40)], fill=SILVER, width=2) # Right shadow

# 2. sous_vide
def draw_sous_vide(draw):
    draw_shadow(draw, [14, 6, 36, 44])
    draw.rectangle([20, 6, 30, 42], fill=BLACK) # Main shaft
    draw.rectangle([22, 6, 28, 42], fill=DKGREY) # Shaft highlight
    draw.rectangle([18, 6, 32, 16], fill=SILVER) # Control head
    draw.rectangle([20, 8, 30, 14], fill=BLUE) # LCD Display
    draw.text((22, 8), "60", fill=WHITE) # Temp text
    draw.line([(24, 20), (26, 20)], fill=STEEL, width=2) # Vent
    draw.line([(24, 24), (26, 24)], fill=STEEL, width=2)
    draw.line([(24, 28), (26, 28)], fill=STEEL, width=2)
    draw.ellipse([22, 34, 28, 40], fill=STEEL) # Water circulator inlet
    draw.line([(22, 34), (28, 40)], fill=BLACK, width=1) # Inlet grill
    draw.line([(28, 34), (22, 40)], fill=BLACK, width=1)

# 3. dehydrator
def draw_dehydrator(draw):
    draw_shadow(draw, [6, 12, 44, 46])
    draw.rounded_rectangle([10, 12, 40, 44], radius=4, fill=GREY)
    draw.rounded_rectangle([12, 12, 38, 44], radius=2, fill=SILVER)
    for i in range(16, 40, 6):
        draw.rectangle([10, i, 40, i+2], fill=DKGREY) # Trays
        draw.rectangle([12, i, 38, i+1], fill=BLACK) # Tray shadow
        # Food on trays
        draw.ellipse([16, i-2, 20, i+1], fill=ORANGE)
        draw.ellipse([24, i-2, 28, i+1], fill=RED)
        draw.ellipse([32, i-2, 36, i+1], fill=GREEN)
    draw.rectangle([18, 40, 32, 44], fill=BLACK) # Base control
    draw.ellipse([24, 41, 26, 43], fill=GREEN) # Power LED

# 4. vacuum_sealer
def draw_vacuum_sealer(draw):
    draw_shadow(draw, [4, 22, 46, 36])
    draw.rounded_rectangle([6, 22, 44, 34], radius=3, fill=STEEL)
    draw.rounded_rectangle([8, 20, 42, 32], radius=2, fill=WHITE)
    draw.line([(8, 30), (42, 30)], fill=DKGREY, width=2) # Sealing strip
    draw.line([(8, 31), (42, 31)], fill=BLACK, width=1) # Sealing line
    draw.rectangle([14, 23, 20, 27], fill=BLUE) # Seal button
    draw.rectangle([30, 23, 36, 27], fill=RED) # Cancel button
    draw.polygon([(22, 30), (28, 30), (32, 44), (18, 44)], fill=GLASS) # Vacuum bag attached
    draw.polygon([(20, 34), (30, 34), (28, 42), (22, 42)], fill=RED) # Meat in bag

# 5. panini_press
def draw_panini_press(draw):
    draw_shadow(draw, [6, 26, 44, 40])
    draw.rounded_rectangle([8, 28, 42, 38], radius=2, fill=DKGREY) # Lower base
    draw.rounded_rectangle([8, 20, 42, 28], radius=2, fill=STEEL) # Upper lid
    draw.rounded_rectangle([10, 18, 40, 26], radius=2, fill=SILVER) # Upper lid highlight
    draw.line([(8, 28), (42, 28)], fill=BLACK, width=2) # Hinge line
    draw.rectangle([18, 16, 32, 20], fill=BLACK) # Handle mount
    draw.line([(14, 16), (36, 16)], fill=DKGREY, width=3) # Handle
    draw.line([(14, 15), (36, 15)], fill=WHITE, width=1) # Handle highlight
    # Panini sticking out slightly
    draw.rectangle([12, 26, 38, 30], fill=BROWN)
    draw.rectangle([14, 27, 36, 29], fill=YELLOW) # Cheese melting

# 6. water_pitcher
def draw_water_pitcher(draw):
    draw_shadow(draw, [12, 16, 36, 46])
    draw.polygon([(16, 16), (32, 16), (34, 44), (14, 44)], fill=GLASS) # Glass body
    draw.polygon([(17, 24), (31, 24), (33, 42), (15, 42)], fill=LIGHTBLUE) # Water
    draw.ellipse([14, 41, 34, 45], fill=BLUE) # Water base depth
    draw.ellipse([16, 23, 32, 25], fill=WHITE) # Water surface reflection
    draw.line([(18, 16), (16, 40)], fill=WHITE, width=2) # Glass glare
    draw.arc([28, 18, 40, 38], 270, 90, fill=GLASS, width=4) # Handle
    draw.arc([28, 18, 40, 38], 270, 90, fill=WHITE, width=1) # Handle highlight
    draw.polygon([(16, 16), (20, 10), (24, 16)], fill=GLASS) # Spout

# 7. dough_cutter
def draw_dough_cutter(draw):
    draw_shadow(draw, [10, 24, 40, 40])
    draw.rectangle([12, 22, 38, 38], fill=SILVER) # Metal blade
    draw.rectangle([14, 22, 36, 38], fill=WHITE) # Metal glare
    draw.line([(12, 38), (38, 38)], fill=STEEL, width=2) # Sharp edge
    draw.rounded_rectangle([10, 14, 40, 24], radius=3, fill=DKBROWN) # Handle shadow
    draw.rounded_rectangle([10, 12, 40, 22], radius=3, fill=BROWN) # Wood handle
    draw.line([(12, 14), (38, 14)], fill=TAN, width=1) # Handle highlight
    draw.ellipse([16, 16, 18, 18], fill=BLACK) # Rivet
    draw.ellipse([24, 16, 26, 18], fill=BLACK) # Rivet
    draw.ellipse([32, 16, 34, 18], fill=BLACK) # Rivet

# 8. pie_server
def draw_pie_server(draw):
    draw_shadow(draw, [12, 12, 38, 46])
    draw.polygon([(14, 34), (36, 34), (28, 12), (22, 12)], fill=SILVER) # Metal blade
    draw.polygon([(16, 32), (34, 32), (26, 14), (24, 14)], fill=WHITE) # Blade glare
    draw.line([(14, 34), (22, 12)], fill=STEEL, width=2) # Edge shadow
    draw.rectangle([23, 34, 27, 46], fill=BLACK) # Handle
    draw.rectangle([24, 34, 26, 44], fill=DKGREY) # Handle highlight
    # Serrated edge
    for y in range(16, 32, 3):
        draw.line([(31 + (y-16)//4, y), (33 + (y-16)//4, y)], fill=DKGREY, width=1)

# 9. cookie_jar
def draw_cookie_jar(draw):
    draw_shadow(draw, [10, 18, 40, 46])
    draw.rounded_rectangle([12, 20, 38, 44], radius=8, fill=CREAM if 'CREAM' in globals() else WHITE) # Jar body
    draw.rounded_rectangle([14, 20, 36, 44], radius=6, fill=WHITE) # Highlight
    draw.ellipse([12, 40, 38, 46], fill=STEEL) # Base shadow
    draw.ellipse([14, 16, 36, 24], fill=WHITE) # Lid base
    draw.ellipse([22, 10, 28, 16], fill=WHITE) # Lid knob
    draw.ellipse([24, 12, 26, 14], fill=SILVER) # Knob highlight
    draw.text((18, 28), "COOKIES", fill=BROWN, font=None) # Label (approx)
    draw.line([(16, 24), (16, 40)], fill=WHITE, width=2) # Side glare

# 10. bagel_cutter
def draw_bagel_cutter(draw):
    draw_shadow(draw, [12, 12, 38, 46])
    draw.rounded_rectangle([14, 22, 36, 44], radius=4, fill=WHITE) # Base stand
    draw.rounded_rectangle([16, 24, 34, 44], radius=2, fill=GREY) # Inner slot
    draw.line([(25, 24), (25, 44)], fill=BLACK, width=2) # Cutting slot
    draw.polygon([(16, 26), (34, 26), (28, 12), (22, 12)], fill=SILVER) # Guillotine blade
    draw.polygon([(18, 24), (32, 24), (27, 14), (23, 14)], fill=WHITE) # Blade glare
    draw.rectangle([18, 10, 32, 14], fill=BLACK) # Top handle
    draw.ellipse([20, 30, 30, 42], fill=BROWN) # Bagel inside
    draw.ellipse([23, 34, 27, 38], fill=GREY) # Bagel hole

# 11. juicer_press
def draw_juicer_press(draw):
    draw_shadow(draw, [6, 18, 44, 44])
    draw.ellipse([14, 22, 36, 34], fill=STEEL) # Lower cup exterior
    draw.ellipse([16, 24, 34, 32], fill=YELLOW) # Lemon half inside
    draw.ellipse([14, 18, 36, 30], fill=SILVER) # Upper press dome
    draw.line([(25, 18), (25, 14)], fill=SILVER, width=4) # Hinge connector
    draw.line([(12, 18), (34, 18)], fill=DKGREY, width=2) # Hinge pin
    draw.line([(14, 28), (6, 42)], fill=SILVER, width=4) # Bottom handle
    draw.line([(14, 20), (6, 36)], fill=STEEL, width=4) # Top handle
    draw.line([(15, 27), (7, 41)], fill=WHITE, width=1) # Handle glare

# 12. pot_holder
def draw_pot_holder(draw):
    draw_shadow(draw, [8, 8, 42, 42])
    draw.rounded_rectangle([10, 10, 40, 40], radius=4, fill=DKRED) # Fabric edge
    draw.rounded_rectangle([12, 12, 38, 38], radius=2, fill=RED) # Main fabric
    # Quilted pattern with highlight/shadow for 3D
    for i in range(16, 38, 6):
        draw.line([(12, i), (38, i)], fill=DKRED, width=1)
        draw.line([(12, i+1), (38, i+1)], fill=PINK, width=1)
        draw.line([(i, 12), (i, 38)], fill=DKRED, width=1)
        draw.line([(i+1, 12), (i+1, 38)], fill=PINK, width=1)
    draw.ellipse([8, 8, 14, 14], fill=SILVER) # Hanging loop
    draw.ellipse([10, 10, 12, 12], fill=WHITE) # Loop hole

# 13. cupcake_carrier
def draw_cupcake_carrier(draw):
    draw_shadow(draw, [8, 12, 42, 44])
    draw.rounded_rectangle([10, 34, 40, 42], radius=4, fill=LIGHTBLUE) # Base tray
    draw.line([(10, 36), (40, 36)], fill=WHITE, width=1) # Tray highlight
    # Cupcakes
    for x in [16, 25, 34]:
        draw.polygon([(x-4, 34), (x+4, 34), (x+3, 40), (x-3, 40)], fill=TAN) # Wrapper
        draw.ellipse([x-5, 28, x+5, 34], fill=PINK) # Frosting
        draw.ellipse([x-1, 26, x+1, 28], fill=RED) # Cherry
    draw.rounded_rectangle([12, 18, 38, 36], radius=8, fill=GLASS) # Clear dome
    draw.arc([12, 18, 38, 36], 0, 360, fill=WHITE, width=1) # Dome glare
    draw.rectangle([20, 14, 30, 18], fill=LIGHTBLUE) # Handle base
    draw.arc([22, 10, 28, 16], 180, 360, fill=LIGHTBLUE, width=3) # Handle loop

# 14. taco_holder
def draw_taco_holder(draw):
    draw_shadow(draw, [4, 20, 46, 40])
    draw.line([(6, 36), (44, 36)], fill=SILVER, width=3) # Bottom rack wire
    draw.line([(6, 34), (44, 34)], fill=WHITE, width=1) # Wire glare
    for i in [10, 22, 34]:
        # Rack waves
        draw.polygon([(i-2, 36), (i+6, 20), (i+14, 36)], fill=STEEL) 
        draw.polygon([(i, 36), (i+6, 22), (i+12, 36)], fill=SILVER) 
        # Tacos
        draw.polygon([(i+2, 34), (i+6, 22), (i+10, 34)], fill=YELLOW) # Shell
        draw.line([(i+6, 22), (i+6, 34)], fill=DKYELLOW, width=1) # Shell crease
        draw.rectangle([i+3, 22, i+9, 26], fill=GREEN) # Lettuce
        draw.rectangle([i+4, 26, i+8, 28], fill=RED) # Tomato
        draw.rectangle([i+4, 28, i+8, 32], fill=BROWN) # Meat

# 15. ice_pop_mold
def draw_ice_pop_mold(draw):
    draw_shadow(draw, [6, 18, 44, 46])
    draw.rounded_rectangle([8, 34, 42, 42], radius=2, fill=WHITE) # Base mold
    draw.line([(8, 36), (42, 36)], fill=GREY, width=1) # Base rim
    for x in [14, 25, 36]:
        # Popsicle
        draw.rounded_rectangle([x-4, 20, x+4, 34], radius=3, fill=PINK) 
        draw.rounded_rectangle([x-2, 20, x+2, 34], radius=1, fill=WHITE) # Ice glare
        # Wooden stick
        draw.line([(x, 34), (x, 44)], fill=DKBROWN, width=3)
        draw.line([(x, 34), (x, 44)], fill=TAN, width=1)

# 16. lunch_box
def draw_lunch_box(draw):
    draw_shadow(draw, [8, 12, 42, 44])
    draw.rounded_rectangle([10, 18, 40, 42], radius=5, fill=DKRED) # Box shadow
    draw.rounded_rectangle([10, 16, 40, 40], radius=5, fill=RED) # Box body
    draw.rounded_rectangle([12, 18, 38, 38], radius=3, fill=WHITE) # Box glare (subtle)
    draw.rounded_rectangle([12, 19, 38, 39], radius=3, fill=RED) # Restore center
    draw.line([(10, 26), (40, 26)], fill=DKRED, width=2) # Lid seam
    draw.rectangle([16, 24, 20, 28], fill=SILVER) # Left latch
    draw.rectangle([30, 24, 34, 28], fill=SILVER) # Right latch
    draw.arc([18, 10, 32, 20], 180, 360, fill=BLACK, width=3) # Handle
    draw.arc([18, 11, 32, 21], 180, 360, fill=STEEL, width=1) # Handle highlight

# 17. apron_hook
def draw_apron_hook(draw):
    draw_shadow(draw, [18, 12, 32, 46])
    draw.rounded_rectangle([20, 12, 30, 26], radius=2, fill=DKBROWN) # Wood plaque shadow
    draw.rounded_rectangle([20, 12, 28, 24], radius=2, fill=BROWN) # Wood plaque
    draw.ellipse([22, 14, 26, 18], fill=BLACK) # Nail hole
    # Metal hook
    draw.line([(24, 18), (24, 34)], fill=BLACK, width=4) 
    draw.line([(24, 18), (24, 34)], fill=SILVER, width=2) 
    draw.arc([20, 30, 28, 38], 0, 180, fill=BLACK, width=4)
    draw.arc([20, 30, 28, 38], 0, 180, fill=SILVER, width=2)
    # Apron hanging
    draw.polygon([(24, 38), (14, 46), (34, 46)], fill=BLUE)
    draw.line([(24, 38), (14, 46)], fill=DKBLUE, width=2) # Fold lines

# 18. sponge_holder
def draw_sponge_holder(draw):
    draw_shadow(draw, [10, 18, 40, 42])
    draw.rounded_rectangle([12, 26, 38, 40], radius=4, fill=GREY) # Ceramic holder shadow
    draw.rounded_rectangle([12, 26, 36, 38], radius=4, fill=WHITE) # Ceramic holder
    draw.line([(14, 28), (34, 28)], fill=SILVER, width=1) # Holder rim
    # Sponge
    draw.rounded_rectangle([16, 18, 32, 32], radius=2, fill=DKGREEN) # Scrubber
    draw.rounded_rectangle([16, 22, 32, 32], radius=2, fill=YELLOW) # Sponge foam
    # Pores
    for x, y in [(18, 24), (22, 26), (28, 24), (20, 28), (26, 28), (30, 26)]:
        draw.ellipse([x, y, x+2, y+2], fill=DKYELLOW)

# 19. soap_dispenser
def draw_soap_dispenser(draw):
    draw_shadow(draw, [14, 12, 36, 46])
    draw.rounded_rectangle([16, 20, 34, 44], radius=4, fill=GLASS) # Bottle
    draw.rounded_rectangle([18, 22, 32, 42], radius=2, fill=BLUE) # Soap liquid
    draw.line([(18, 22), (18, 42)], fill=LIGHTBLUE, width=2) # Liquid highlight
    # Pump mechanism
    draw.rectangle([22, 16, 28, 20], fill=STEEL) # Collar
    draw.rectangle([23, 10, 27, 16], fill=SILVER) # Stem
    draw.rounded_rectangle([20, 8, 30, 12], radius=2, fill=SILVER) # Pump head
    draw.line([(20, 10), (12, 14)], fill=SILVER, width=3) # Spout
    draw.ellipse([11, 14, 13, 16], fill=LIGHTBLUE) # Soap drip

# 20. knife_sharpener
def draw_knife_sharpener(draw):
    draw_shadow(draw, [6, 18, 44, 44])
    draw.rounded_rectangle([8, 30, 42, 42], radius=4, fill=BLACK) # Base
    draw.rounded_rectangle([10, 30, 40, 40], radius=4, fill=DKGREY) # Base top
    draw.rectangle([14, 20, 24, 30], fill=SILVER) # Slot 1 casing
    draw.rectangle([26, 20, 36, 30], fill=SILVER) # Slot 2 casing
    draw.polygon([(16, 20), (22, 20), (19, 26)], fill=DKGREY) # Slot 1 V
    draw.polygon([(28, 20), (34, 20), (31, 26)], fill=WHITE) # Slot 2 V (ceramic)
    draw.line([(8, 36), (42, 36)], fill=BLACK, width=2) # Base groove
    draw.arc([10, 18, 20, 30], 90, 270, fill=BLACK, width=3) # Handle grip left

# 21. timer_hourglass
def draw_timer_hourglass(draw):
    draw_shadow(draw, [10, 10, 40, 42])
    # Wood bases
    draw.rounded_rectangle([12, 8, 38, 12], radius=1, fill=DKBROWN)
    draw.rounded_rectangle([12, 8, 38, 10], radius=1, fill=BROWN)
    draw.rounded_rectangle([12, 40, 38, 44], radius=1, fill=DKBROWN)
    draw.rounded_rectangle([12, 40, 38, 42], radius=1, fill=BROWN)
    # Spindles
    draw.line([(14, 12), (14, 40)], fill=STEEL, width=2)
    draw.line([(36, 12), (36, 40)], fill=STEEL, width=2)
    draw.line([(25, 12), (25, 40)], fill=STEEL, width=1) # Back spindle
    # Glass bulbs
    draw.polygon([(16, 12), (34, 12), (26, 26), (24, 26)], fill=GLASS)
    draw.polygon([(24, 26), (26, 26), (34, 40), (16, 40)], fill=GLASS)
    # Sand
    draw.polygon([(18, 16), (32, 16), (25, 26)], fill=TAN)
    draw.polygon([(21, 40), (29, 40), (25, 32)], fill=TAN)
    draw.line([(25, 26), (25, 32)], fill=TAN, width=1) # Sand falling

# 22. sink_strainer
def draw_sink_strainer(draw):
    draw_shadow(draw, [8, 8, 42, 42])
    draw.ellipse([10, 10, 40, 40], fill=DKGREY) # Outer rim shadow
    draw.ellipse([10, 10, 38, 38], fill=SILVER) # Outer rim
    draw.ellipse([14, 14, 36, 36], fill=STEEL) # Inner bowl
    draw.ellipse([18, 18, 32, 32], fill=DKGREY) # Deep center
    # Concentric drainage holes
    for r in [12, 8, 4]:
        for i in range(0, 360, 45):
            import math
            x = 25 + int(r * math.cos(math.radians(i)))
            y = 25 + int(r * math.sin(math.radians(i)))
            draw.ellipse([x-1, y-1, x+1, y+1], fill=BLACK)
    draw.ellipse([23, 23, 27, 27], fill=WHITE) # Center pin knob
    draw.ellipse([24, 24, 26, 26], fill=SILVER)

# 23. wine_cradle
def draw_wine_cradle(draw):
    draw_shadow(draw, [8, 12, 42, 40])
    draw.arc([10, 20, 40, 44], 0, 180, fill=DKBROWN, width=4) # Cradle back
    # Wine bottle
    draw.polygon([(12, 32), (34, 16), (38, 20), (16, 36)], fill=BLACK) # Bottle shadow
    draw.polygon([(12, 30), (34, 14), (38, 18), (16, 34)], fill=DKGREEN) # Bottle body
    draw.polygon([(14, 30), (34, 15), (36, 18), (16, 33)], fill=GREEN) # Bottle glare
    draw.line([(36, 16), (44, 10)], fill=DKRED, width=4) # Foil neck
    draw.line([(36, 15), (44, 9)], fill=RED, width=2) # Foil glare
    draw.rectangle([20, 20, 26, 28], fill=CREAM if 'CREAM' in globals() else WHITE) # Label
    draw.arc([10, 20, 40, 44], 0, 180, fill=BROWN, width=2) # Cradle front
    draw.line([(10, 24), (16, 12)], fill=BROWN, width=3) # Front leg

# 24. corn_holders
def draw_corn_holders(draw):
    draw_shadow(draw, [8, 16, 42, 40])
    # Ear of corn section
    draw.ellipse([28, 14, 42, 36], fill=DKYELLOW)
    for y in range(16, 36, 4):
        for x in range(30, 40, 4):
            draw.ellipse([x, y, x+3, y+3], fill=YELLOW)
    # Holder 1 (Top)
    draw.line([(22, 20), (32, 20)], fill=STEEL, width=2) # Prongs
    draw.line([(22, 24), (32, 24)], fill=STEEL, width=2)
    draw.rounded_rectangle([10, 18, 22, 26], radius=2, fill=DKGREEN) # Corn-shaped handle
    draw.rounded_rectangle([10, 18, 20, 24], radius=2, fill=GREEN)
    # Holder 2 (Bottom)
    draw.line([(22, 30), (32, 30)], fill=STEEL, width=2)
    draw.line([(22, 34), (32, 34)], fill=STEEL, width=2)
    draw.rounded_rectangle([10, 28, 22, 36], radius=2, fill=DKGREEN)
    draw.rounded_rectangle([10, 28, 20, 34], radius=2, fill=GREEN)

# 25. meat_hook
def draw_meat_hook(draw):
    draw_shadow(draw, [14, 4, 36, 44])
    draw.line([(25, 4), (25, 16)], fill=DKGREY, width=4) # Chain shadow
    draw.line([(25, 4), (25, 16)], fill=SILVER, width=2) # Chain highlight
    # Top hook
    draw.arc([16, 16, 26, 32], 90, 270, fill=DKGREY, width=5)
    draw.arc([16, 16, 26, 32], 90, 270, fill=SILVER, width=2)
    # Bottom hook
    draw.arc([24, 26, 34, 42], 270, 90, fill=DKGREY, width=5)
    draw.arc([24, 26, 34, 42], 270, 90, fill=SILVER, width=2)
    draw.polygon([(34, 26), (32, 30), (36, 30)], fill=SILVER) # Sharp tip
    draw.polygon([(34, 26), (34, 30), (36, 30)], fill=WHITE) # Tip glare

# 26. pepper_corer
def draw_pepper_corer(draw):
    draw_shadow(draw, [6, 20, 44, 32])
    draw.rounded_rectangle([8, 22, 22, 30], radius=3, fill=DKRED) # Handle shadow
    draw.rounded_rectangle([8, 22, 20, 28], radius=3, fill=RED) # Handle
    draw.line([(10, 24), (18, 24)], fill=WHITE, width=1) # Handle glare
    draw.line([(22, 26), (38, 26)], fill=DKGREY, width=4) # Shaft shadow
    draw.line([(22, 25), (38, 25)], fill=STEEL, width=3) # Shaft
    draw.line([(22, 24), (38, 24)], fill=WHITE, width=1) # Shaft glare
    draw.ellipse([34, 20, 42, 32], fill=STEEL) # Coring loop
    draw.ellipse([36, 22, 40, 30], fill=255) # Transparent center
    # Serrations
    for y in range(20, 32, 2):
        draw.line([(42, y), (44, y+1)], fill=SILVER, width=1)

# 27. herb_scissors
def draw_herb_scissors(draw):
    draw_shadow(draw, [6, 14, 44, 38])
    # Blades (5 layers)
    for y in range(18, 27, 2):
        draw.line([(20, y), (42, y-6 + (y-18))], fill=DKGREY, width=2) # Lower blades
        draw.line([(20, y), (42, y-6 + (y-18))], fill=SILVER, width=1)
    for y in range(26, 35, 2):
        draw.line([(20, y), (42, y+6 - (34-y))], fill=DKGREY, width=2) # Upper blades
        draw.line([(20, y), (42, y+6 - (34-y))], fill=STEEL, width=1)
    # Handles
    draw.ellipse([8, 14, 20, 26], fill=DKGREEN)
    draw.ellipse([8, 14, 18, 24], fill=GREEN)
    draw.ellipse([12, 18, 16, 22], fill=255)
    draw.ellipse([8, 26, 20, 38], fill=DKGREEN)
    draw.ellipse([8, 26, 18, 36], fill=GREEN)
    draw.ellipse([12, 30, 16, 34], fill=255)
    draw.ellipse([22, 24, 26, 28], fill=SILVER) # Pivot screw

# 28. trivet_stone
def draw_trivet_stone(draw):
    draw_shadow(draw, [8, 10, 42, 44])
    draw.rounded_rectangle([10, 14, 40, 42], radius=4, fill=GREY) # Stone thickness shadow
    draw.rounded_rectangle([10, 10, 40, 40], radius=4, fill=WHITE) # Stone top
    # Marble veining
    draw.line([(12, 16), (20, 34)], fill=STEEL, width=2)
    draw.line([(18, 24), (36, 14)], fill=STEEL, width=1)
    draw.line([(24, 36), (38, 28)], fill=STEEL, width=1)
    draw.line([(30, 32), (36, 38)], fill=STEEL, width=2)
    draw.rounded_rectangle([11, 11, 39, 39], radius=3, fill=WHITE) # Polish glare (alpha blend sim)

# 29. whiskey_decanter
def draw_whiskey_decanter(draw):
    draw_shadow(draw, [12, 6, 38, 46])
    draw.rounded_rectangle([14, 20, 36, 44], radius=3, fill=GLASS) # Bottle
    draw.polygon([(16, 24), (34, 24), (34, 42), (16, 42)], fill=BROWN) # Whiskey
    draw.polygon([(17, 24), (33, 24), (33, 41), (17, 41)], fill=DKBROWN) # Whiskey depth
    draw.line([(16, 22), (16, 40)], fill=WHITE, width=2) # Glass edge glare
    draw.line([(34, 22), (34, 40)], fill=WHITE, width=1)
    # Faceted cuts in glass
    draw.line([(20, 26), (30, 40)], fill=DKBROWN, width=1)
    draw.line([(30, 26), (20, 40)], fill=DKBROWN, width=1)
    draw.rectangle([20, 12, 30, 20], fill=GLASS) # Neck
    draw.line([(22, 12), (22, 20)], fill=WHITE, width=1)
    draw.ellipse([18, 6, 32, 14], fill=GLASS) # Stopper
    draw.ellipse([20, 8, 26, 12], fill=WHITE) # Stopper glare

# 30. oil_mister
def draw_oil_mister(draw):
    draw_shadow(draw, [14, 10, 36, 46])
    draw.rounded_rectangle([16, 18, 34, 44], radius=3, fill=DKGREY) # Metal body shadow
    draw.rounded_rectangle([16, 18, 32, 44], radius=3, fill=SILVER) # Metal body
    draw.line([(20, 18), (20, 44)], fill=WHITE, width=2) # Cylindrical glare
    draw.rectangle([18, 10, 32, 18], fill=BLACK) # Spray cap
    draw.rectangle([18, 10, 30, 18], fill=DKGREY) # Cap highlight
    draw.rectangle([22, 8, 28, 12], fill=WHITE) # Pump button
    draw.line([(18, 14), (6, 10)], fill=LIGHTBLUE, width=1) # Mist spray
    draw.line([(18, 14), (4, 14)], fill=LIGHTBLUE, width=1)
    draw.line([(18, 14), (6, 18)], fill=LIGHTBLUE, width=1)

# 31. pot_lid_holder
def draw_pot_lid_holder(draw):
    draw_shadow(draw, [6, 16, 44, 42])
    draw.rectangle([8, 38, 42, 42], fill=BLACK) # Base
    draw.rectangle([8, 36, 40, 40], fill=DKGREY) # Base top
    # Lids slotted in
    draw.ellipse([12, 20, 28, 36], fill=GLASS)
    draw.arc([12, 20, 28, 36], 0, 360, fill=WHITE, width=1)
    draw.ellipse([24, 16, 42, 34], fill=STEEL)
    draw.arc([24, 16, 42, 34], 0, 360, fill=SILVER, width=2)
    # Wire dividers
    for x in [14, 25, 36]:
        draw.arc([x-4, 16, x+4, 38], 180, 360, fill=BLACK, width=3)
        draw.arc([x-4, 16, x+4, 38], 180, 360, fill=SILVER, width=1)

# 32. banana_hanger
def draw_banana_hanger(draw):
    draw_shadow(draw, [8, 8, 42, 46])
    draw.ellipse([16, 40, 34, 46], fill=DKGREY) # Base shadow
    draw.ellipse([16, 38, 34, 44], fill=SILVER) # Base top
    draw.line([(25, 40), (25, 12)], fill=DKGREY, width=4) # Post
    draw.line([(25, 40), (25, 12)], fill=SILVER, width=2) # Post glare
    draw.arc([18, 8, 26, 16], 90, 270, fill=DKGREY, width=4) # Hook
    draw.arc([18, 8, 26, 16], 90, 270, fill=SILVER, width=2)
    # Bananas hanging
    draw.polygon([(20, 16), (24, 16), (22, 20)], fill=BROWN) # Stem
    draw.arc([10, 16, 22, 36], 0, 130, fill=DKYELLOW, width=5) # Banana 1 shadow
    draw.arc([10, 16, 22, 36], 0, 130, fill=YELLOW, width=3) # Banana 1
    draw.arc([14, 18, 26, 38], 0, 130, fill=DKYELLOW, width=5) # Banana 2
    draw.arc([14, 18, 26, 38], 0, 130, fill=YELLOW, width=3)
    draw.arc([18, 20, 30, 40], 0, 130, fill=DKYELLOW, width=5) # Banana 3
    draw.arc([18, 20, 30, 40], 0, 130, fill=YELLOW, width=3)

# 33. egg_piercer
def draw_egg_piercer(draw):
    draw_shadow(draw, [12, 14, 38, 38])
    draw.ellipse([14, 16, 36, 38], fill=DKGREY) # Base shadow
    draw.ellipse([14, 14, 36, 36], fill=WHITE) # Base
    draw.ellipse([16, 16, 34, 34], fill=SILVER) # Inner rim
    draw.ellipse([20, 22, 30, 32], fill=DKRED) # Button shadow
    draw.ellipse([20, 20, 30, 30], fill=RED) # Button
    draw.ellipse([22, 22, 26, 26], fill=PINK) # Button glare
    draw.line([(25, 20), (25, 10)], fill=STEEL, width=2) # Needle
    draw.polygon([(24, 10), (26, 10), (25, 6)], fill=SILVER) # Needle tip

# 34. tapioca_scoop
def draw_tapioca_scoop(draw):
    draw_shadow(draw, [8, 10, 48, 36])
    draw.line([(26, 22), (46, 12)], fill=DKBROWN, width=5) # Handle shadow
    draw.line([(26, 20), (46, 10)], fill=BROWN, width=3) # Handle
    draw.line([(26, 19), (46, 9)], fill=TAN, width=1) # Handle glare
    draw.ellipse([10, 16, 28, 34], fill=DKGREY) # Ring shadow
    draw.ellipse([10, 14, 28, 32], fill=SILVER) # Ring
    draw.ellipse([12, 16, 26, 30], fill=255) # Transparent center
    # Wire mesh
    for i in range(14, 26, 3):
        draw.line([(i, 16), (i, 30)], fill=STEEL, width=1)
        draw.line([(12, i+2), (26, i+2)], fill=STEEL, width=1)
    # Boba
    for x, y in [(16, 20), (22, 20), (18, 24), (24, 26), (16, 26)]:
        draw.ellipse([x, y, x+3, y+3], fill=BLACK)
        draw.ellipse([x+1, y+1, x+2, y+2], fill=BROWN) # Boba glare

# 35. sauce_dispenser
def draw_sauce_dispenser(draw):
    draw_shadow(draw, [14, 8, 36, 46])
    draw.rounded_rectangle([16, 20, 34, 44], radius=4, fill=DKYELLOW) # Bottle shadow
    draw.rounded_rectangle([16, 18, 32, 44], radius=4, fill=YELLOW) # Bottle
    draw.line([(18, 20), (18, 42)], fill=WHITE, width=2) # Plastic glare
    draw.rectangle([18, 16, 32, 20], fill=RED) # Cap base
    draw.polygon([(20, 16), (30, 16), (26, 4), (24, 4)], fill=RED) # Nozzle
    draw.polygon([(20, 16), (25, 16), (25, 4), (24, 4)], fill=PINK) # Nozzle glare
    draw.ellipse([23, 2, 27, 6], fill=WHITE) # Squeeze drop
    draw.ellipse([24, 3, 26, 5], fill=YELLOW)

# 36. toothpick_dispenser
def draw_toothpick_dispenser(draw):
    draw_shadow(draw, [12, 8, 38, 44])
    draw.rounded_rectangle([14, 18, 36, 42], radius=4, fill=DKGREY) # Body shadow
    draw.rounded_rectangle([14, 16, 34, 42], radius=4, fill=WHITE) # Body
    draw.line([(16, 18), (16, 40)], fill=WHITE, width=2) # Glare
    draw.rectangle([20, 14, 30, 18], fill=DKGREEN) # Button shadow
    draw.rectangle([20, 12, 28, 16], fill=GREEN) # Button
    # Slot
    draw.line([(25, 18), (25, 28)], fill=BLACK, width=2)
    # Toothpick popping up
    draw.line([(25, 6), (25, 12)], fill=DKBROWN, width=2)
    draw.line([(25, 6), (25, 12)], fill=TAN, width=1)
    draw.ellipse([24, 4, 26, 6], fill=TAN) # Tip

# 37. tea_bag_squeezer
def draw_tea_bag_squeezer(draw):
    draw_shadow(draw, [8, 16, 44, 36])
    draw.line([(10, 26), (38, 21)], fill=DKGREY, width=4) # Tong 1 shadow
    draw.line([(10, 25), (38, 20)], fill=SILVER, width=3) # Tong 1
    draw.line([(10, 26), (38, 31)], fill=DKGREY, width=4) # Tong 2 shadow
    draw.line([(10, 25), (38, 30)], fill=SILVER, width=3) # Tong 2
    draw.arc([6, 20, 14, 30], 90, 270, fill=SILVER, width=3) # Spring hinge
    # Squeezing plates
    draw.polygon([(34, 16), (42, 16), (40, 22), (36, 22)], fill=STEEL)
    draw.polygon([(34, 34), (42, 34), (40, 28), (36, 28)], fill=STEEL)
    for x in [36, 38, 40]:
        draw.ellipse([x, 18, x+1, 19], fill=BLACK) # Perforations
        draw.ellipse([x, 31, x+1, 32], fill=BLACK)
    # Tea bag inside
    draw.rectangle([35, 23, 41, 27], fill=BROWN)
    draw.line([(38, 23), (38, 10)], fill=WHITE, width=1) # String
    draw.rectangle([36, 8, 40, 10], fill=WHITE) # Tag

# 38. can_punch
def draw_can_punch(draw):
    draw_shadow(draw, [6, 22, 46, 30])
    draw.rectangle([8, 24, 26, 30], fill=DKRED) # Handle shadow
    draw.rectangle([8, 22, 24, 28], fill=RED) # Handle
    draw.line([(10, 24), (22, 24)], fill=PINK, width=2) # Handle glare
    draw.line([(26, 26), (42, 26)], fill=DKGREY, width=5) # Metal body shadow
    draw.line([(26, 25), (42, 25)], fill=STEEL, width=4) # Metal body
    draw.line([(26, 24), (42, 24)], fill=SILVER, width=2) # Metal body glare
    draw.polygon([(38, 25), (44, 22), (40, 28)], fill=DKGREY) # Punch tooth shadow
    draw.polygon([(38, 24), (43, 21), (40, 27)], fill=SILVER) # Punch tooth
    draw.ellipse([34, 24, 36, 26], fill=BLACK) # Rivet

# 39. ice_bag
def draw_ice_bag(draw):
    draw_shadow(draw, [12, 16, 38, 46])
    draw.polygon([(14, 22), (36, 22), (32, 46), (18, 46)], fill=GREY) # Bag shadow
    draw.polygon([(14, 20), (36, 20), (32, 44), (18, 44)], fill=WHITE) # Canvas bag
    # Canvas wrinkles
    draw.line([(20, 24), (24, 40)], fill=GREY, width=1)
    draw.line([(30, 26), (26, 42)], fill=GREY, width=1)
    draw.ellipse([18, 16, 32, 24], fill=WHITE) # Gathered top
    draw.line([(16, 20), (34, 20)], fill=DKBROWN, width=3) # Drawstring
    draw.line([(16, 20), (34, 20)], fill=TAN, width=1)
    draw.polygon([(24, 30), (28, 30), (26, 36)], fill=DKBLUE) # Logo

# 40. cocktail_pick
def draw_cocktail_pick(draw):
    draw_shadow(draw, [10, 10, 42, 40])
    draw.line([(12, 40), (38, 14)], fill=DKGREY, width=3) # Shaft shadow
    draw.line([(12, 38), (38, 12)], fill=SILVER, width=2) # Metal shaft
    draw.ellipse([36, 12, 42, 18], fill=DKRED) # Bead shadow
    draw.ellipse([36, 10, 40, 14], fill=RED) # Decorative bead
    draw.ellipse([37, 11, 38, 12], fill=PINK) # Bead glare
    draw.ellipse([20, 28, 28, 36], fill=DKGREEN) # Olive shadow
    draw.ellipse([18, 26, 26, 34], fill=GREEN) # Olive
    draw.ellipse([24, 28, 26, 30], fill=RED) # Pimento
    draw.ellipse([19, 27, 21, 29], fill=WHITE) # Olive glare

# 41. champagne_flute
def draw_champagne_flute(draw):
    draw_shadow(draw, [16, 10, 34, 46])
    draw.polygon([(18, 10), (32, 10), (28, 28), (22, 28)], fill=GLASS) # Tall bowl
    draw.polygon([(19, 14), (31, 14), (27, 27), (23, 27)], fill=YELLOW) # Champagne
    draw.polygon([(20, 14), (24, 14), (24, 27), (23, 27)], fill=DKYELLOW) # Liquid depth
    # Bubbles
    for x, y in [(25, 24), (26, 20), (24, 16), (28, 18), (25, 26)]:
        draw.ellipse([x, y, x+1, y+1], fill=WHITE)
    draw.line([(25, 28), (25, 42)], fill=GLASS, width=3) # Stem
    draw.line([(24, 28), (24, 42)], fill=WHITE, width=1) # Stem glare
    draw.ellipse([18, 42, 32, 46], fill=GLASS) # Base
    draw.ellipse([18, 41, 30, 43], fill=WHITE) # Base glare

# 42. carafe
def draw_carafe(draw):
    draw_shadow(draw, [10, 14, 40, 46])
    draw.polygon([(18, 14), (32, 14), (36, 24), (14, 24)], fill=GLASS) # Neck
    draw.ellipse([12, 22, 38, 46], fill=DKGREY) # Body shadow (base)
    draw.ellipse([12, 22, 38, 44], fill=GLASS) # Flared body
    draw.ellipse([14, 24, 36, 42], fill=LIGHTBLUE) # Water
    draw.ellipse([14, 24, 24, 42], fill=BLUE) # Water depth
    draw.line([(18, 14), (14, 30)], fill=WHITE, width=2) # Left glare
    draw.line([(32, 14), (36, 30)], fill=WHITE, width=1) # Right glare
    draw.ellipse([16, 23, 34, 27], fill=WHITE) # Water surface reflection

# 43. ramekin
def draw_ramekin(draw):
    draw_shadow(draw, [8, 14, 42, 44])
    draw.rounded_rectangle([10, 24, 40, 44], radius=2, fill=GREY) # Ramekin shadow
    draw.rounded_rectangle([10, 22, 38, 42], radius=2, fill=WHITE) # Ramekin bowl
    # Ribbed texture
    for x in range(14, 38, 4):
        draw.line([(x, 24), (x, 42)], fill=DKGREY, width=1)
        draw.line([(x-1, 24), (x-1, 42)], fill=WHITE, width=1)
    # Souffle
    draw.ellipse([12, 14, 38, 24], fill=DKBROWN) # Crust edge shadow
    draw.ellipse([12, 12, 36, 22], fill=BROWN) # Crust
    draw.ellipse([16, 14, 32, 20], fill=YELLOW) # Center puff
    draw.ellipse([18, 15, 24, 18], fill=WHITE) # Puff highlight

# 44. moka_pot
def draw_moka_pot(draw):
    draw_shadow(draw, [12, 14, 40, 46])
    draw.polygon([(16, 30), (34, 30), (32, 46), (18, 46)], fill=DKGREY) # Bottom shadow
    draw.polygon([(16, 28), (34, 28), (32, 44), (18, 44)], fill=SILVER) # Bottom chamber
    draw.polygon([(18, 14), (32, 14), (34, 28), (16, 28)], fill=SILVER) # Top chamber
    draw.line([(25, 14), (25, 44)], fill=WHITE, width=3) # Center glare
    draw.polygon([(18, 14), (25, 14), (25, 44), (16, 28)], fill=STEEL) # Facet shading
    draw.polygon([(14, 18), (18, 20), (18, 22), (16, 24)], fill=SILVER) # Spout
    draw.arc([28, 20, 38, 38], 270, 90, fill=BLACK, width=4) # Handle shadow
    draw.arc([28, 19, 37, 37], 270, 90, fill=DKGREY, width=2) # Handle
    draw.rectangle([22, 10, 28, 14], fill=BLACK) # Top knob

# 45. siphon_coffee
def draw_siphon_coffee(draw):
    draw_shadow(draw, [10, 8, 40, 46])
    # Stand
    draw.line([(12, 22), (12, 46)], fill=BROWN, width=3)
    draw.line([(12, 22), (20, 22)], fill=BROWN, width=3)
    draw.ellipse([10, 42, 30, 46], fill=BROWN)
    draw.ellipse([22, 40, 28, 42], fill=YELLOW) # Burner flame
    # Bottom globe
    draw.ellipse([16, 28, 34, 42], fill=GLASS)
    draw.ellipse([18, 30, 32, 40], fill=BROWN) # Coffee
    # Connecting tube
    draw.line([(25, 22), (25, 34)], fill=GLASS, width=4)
    draw.line([(25, 22), (25, 34)], fill=BROWN, width=2) # Coffee rising
    # Top bulb
    draw.ellipse([16, 8, 34, 22], fill=GLASS)
    draw.ellipse([18, 12, 32, 20], fill=DKBROWN) # Grounds
    # Glares
    draw.arc([16, 8, 34, 22], 180, 270, fill=WHITE, width=2)
    draw.arc([16, 28, 34, 42], 180, 270, fill=WHITE, width=2)

# 46. whipped_cream_dispenser
def draw_whipped_cream_dispenser(draw):
    draw_shadow(draw, [12, 8, 38, 46])
    draw.rounded_rectangle([16, 18, 34, 46], radius=4, fill=DKGREY) # Bottle shadow
    draw.rounded_rectangle([16, 16, 32, 44], radius=4, fill=SILVER) # Aluminum bottle
    draw.line([(20, 16), (20, 44)], fill=WHITE, width=3) # Cylindrical glare
    draw.rectangle([18, 8, 32, 16], fill=WHITE) # Plastic charger head
    draw.rectangle([18, 8, 24, 16], fill=GREY) # Charger shading
    # Whipped nozzle
    draw.line([(20, 12), (12, 16)], fill=WHITE, width=4)
    draw.line([(20, 11), (12, 15)], fill=STEEL, width=1) # Nozzle ridges
    draw.line([(20, 13), (12, 17)], fill=STEEL, width=1)
    # Lever
    draw.line([(28, 10), (34, 14)], fill=RED, width=3)
    draw.line([(28, 9), (34, 13)], fill=PINK, width=1)

# 47. gravy_separator
def draw_gravy_separator(draw):
    draw_shadow(draw, [8, 20, 42, 44])
    draw.rounded_rectangle([16, 20, 36, 44], radius=4, fill=GLASS) # Pitcher
    draw.rectangle([18, 26, 34, 42], fill=BROWN) # Gravy broth
    draw.rectangle([18, 22, 34, 26], fill=YELLOW) # Fat layer floating
    # Low spout
    draw.line([(16, 42), (8, 24)], fill=GLASS, width=5)
    draw.line([(16, 42), (8, 24)], fill=BROWN, width=3) # Broth in spout
    # Handle
    draw.arc([32, 24, 42, 40], 270, 90, fill=GLASS, width=4)
    draw.arc([32, 24, 42, 40], 270, 90, fill=WHITE, width=1) # Glare
    # Measurement lines
    for y in range(24, 40, 4):
        draw.line([(32, y), (34, y)], fill=RED, width=1)

# 48. roasting_rack
def draw_roasting_rack(draw):
    draw_shadow(draw, [6, 24, 44, 42])
    draw.rectangle([8, 30, 42, 42], fill=DKGREY) # Roasting pan shadow
    draw.rectangle([8, 28, 40, 40], fill=SILVER) # Roasting pan
    draw.rectangle([10, 30, 38, 38], fill=DKGREY) # Pan depth
    # Handles
    draw.arc([4, 30, 12, 38], 90, 270, fill=STEEL, width=2)
    draw.arc([36, 30, 44, 38], 270, 90, fill=STEEL, width=2)
    # V-rack
    for x in range(12, 40, 4):
        draw.line([(x, 24), (x+2, 34)], fill=STEEL, width=2)
        draw.line([(x, 34), (x-2, 24)], fill=STEEL, width=2)
        draw.line([(x, 24), (x+2, 34)], fill=WHITE, width=1) # Wire glare

# 49. splatter_screen
def draw_splatter_screen(draw):
    draw_shadow(draw, [10, 10, 40, 48])
    draw.ellipse([12, 12, 38, 38], fill=DKGREY) # Outer metal ring shadow
    draw.ellipse([12, 10, 38, 36], fill=SILVER) # Outer metal ring
    draw.ellipse([14, 12, 36, 34], fill=255) # Transparent mesh
    # Mesh grid with 3D weave effect
    for i in range(14, 36, 3):
        draw.line([(i, 14), (i, 34)], fill=GREY, width=1)
        draw.line([(14, i), (36, i)], fill=STEEL, width=1)
    draw.line([(25, 36), (25, 48)], fill=BLACK, width=4) # Handle shadow
    draw.line([(24, 36), (24, 48)], fill=DKGREY, width=2) # Handle
    draw.ellipse([23, 46, 25, 48], fill=WHITE) # Hanging hole

# 50. steamer_basket
def draw_steamer_basket(draw):
    draw_shadow(draw, [8, 16, 42, 44])
    draw.rectangle([10, 26, 40, 44], fill=DKBROWN) # Lower tier shadow
    draw.rectangle([10, 24, 38, 42], fill=TAN) # Lower tier
    draw.rectangle([10, 16, 40, 24], fill=BROWN) # Lid shadow
    draw.rectangle([10, 14, 38, 22], fill=TAN) # Lid
    # Woven basket texture lines
    for x in range(12, 38, 4):
        draw.line([(x, 24), (x, 42)], fill=DKBROWN, width=1)
        draw.line([(x, 14), (x, 22)], fill=DKBROWN, width=1)
    # Horizontal bamboo binding bands
    for y in [18, 28, 38]:
        draw.line([(10, y), (38, y)], fill=BROWN, width=2)
        draw.line([(10, y-1), (38, y-1)], fill=YELLOW, width=1) # Band highlight
    draw.ellipse([20, 10, 28, 14], fill=BROWN) # Top handle knot
    draw.ellipse([22, 11, 26, 13], fill=255) # Knot hole

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

print(f"Generating {len(items)} ultra-realistic kitchen sprites in '{OUTPUT_DIR}'...")
for name, func in items:
    create_sprite(name, func)
print("\nAll 50 unique ultra-realistic kitchen sprites generated successfully!")
