import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/clothing"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color constants
RED       = (210, 45, 45, 255)
DKRED     = (130, 20, 20, 255)
BLUE      = (50, 110, 210, 255)
DKBLUE    = (20, 50, 140, 255)
YELLOW    = (240, 200, 30, 255)
GREEN     = (50, 160, 60, 255)
DKGREEN   = (20, 90, 20, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
ORANGE    = (235, 110, 25, 255)
BROWN     = (130, 85, 45, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (180, 180, 190, 255)
GOLD      = (212, 175, 55, 255)
PINK      = (240, 130, 180, 255)
DKPINK    = (180, 80, 120, 255)
BEIGE     = (225, 200, 170, 255)
DKBROWN   = (80, 50, 25, 255)
KHAKI     = (195, 176, 145, 255)
TEAL      = (30, 140, 150, 255)
DKCYAN    = (0, 130, 130, 255)

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    # --- Add realistic 3D detail (pixel drop shadow and glossy reflection) ---
    r, g, b, a = base_img.split()
    shadow_mask = a.point(lambda p: 255 if p > 128 else 0)
    
    combined = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    # 1. Drop Shadow (offset by 2,2)
    shadow_color = Image.new("RGBA", (50, 50), (30, 30, 35, 255))
    combined.paste(shadow_color, (2, 2), mask=shadow_mask)
    
    # 2. Base Image
    combined = Image.alpha_composite(combined, base_img)
    
    # 3. Glossy Reflection Glare
    gloss = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.polygon([(0, 0), (35, 0), (0, 35)], fill=(255, 255, 255, 45))
    gloss_draw.polygon([(50, 25), (50, 50), (25, 50)], fill=(0, 0, 0, 45))
    gloss_masked = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_masked.paste(gloss, (0, 0), mask=shadow_mask)
    combined = Image.alpha_composite(combined, gloss_masked)
    
    # --- Quantize to strictly <= 9 colors ---
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    comb_a = combined.split()[3].point(lambda p: 255 if p > 128 else 0)
    flat.paste(combined, mask=comb_a)
    
    q = flat.quantize(colors=8, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    
    # Force all transparent pixels to a single identical RGBA value
    data = final.getdata()
    alpha_data = comb_a.getdata()
    new_data = []
    for i in range(len(data)):
        if alpha_data[i] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((data[i][0], data[i][1], data[i][2], 255))
    final.putdata(new_data)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    final.save(path)
    print(f"  Saved: {path}")

# --- 1. Fez Hat ---
def draw_fez_hat(draw):
    draw.polygon([(18, 16), (32, 16), (35, 34), (15, 34)], fill=RED)
    draw.line([25, 16, 32, 22], fill=GOLD, width=1)
    draw.ellipse([31, 21, 33, 23], fill=GOLD)

# --- 2. Silk Turban ---
def draw_turban(draw):
    draw.ellipse([14, 15, 36, 35], fill=WHITE)
    draw.ellipse([15, 19, 35, 33], fill=BEIGE)
    draw.ellipse([16, 23, 34, 31], fill=WHITE)
    draw.ellipse([22, 23, 28, 29], fill=GOLD)
    draw.ellipse([23, 24, 27, 28], fill=BLUE)

# --- 3. Gold Royal Crown ---
def draw_crown_regal(draw):
    draw.ellipse([15, 22, 35, 29], fill=PURPLE)
    draw.rectangle([13, 28, 37, 34], fill=GOLD)
    draw.polygon([(13, 28), (17, 18), (21, 28)], fill=GOLD)
    draw.polygon([(21, 28), (25, 14), (29, 28)], fill=GOLD)
    draw.polygon([(29, 28), (33, 18), (37, 28)], fill=GOLD)
    draw.ellipse([17, 30, 19, 32], fill=RED)
    draw.ellipse([24, 30, 26, 32], fill=BLUE)
    draw.ellipse([31, 30, 33, 32], fill=RED)

# --- 4. Silver Crystal Tiara ---
def draw_tiara_crystal(draw):
    draw.arc([11, 26, 39, 34], start=180, end=360, fill=SILVER, width=2)
    draw.polygon([(23, 28), (25, 16), (27, 28)], fill=SILVER)
    draw.polygon([(18, 28), (20, 20), (22, 28)], fill=SILVER)
    draw.polygon([(28, 28), (30, 20), (32, 28)], fill=SILVER)
    draw.ellipse([24, 15, 26, 17], fill=LIGHTBLUE)
    draw.ellipse([19, 19, 21, 21], fill=LIGHTBLUE)
    draw.ellipse([29, 19, 31, 21], fill=LIGHTBLUE)

# --- 5. Tricorn Pirate Hat ---
def draw_pirate_hat(draw):
    draw.polygon([(11, 22), (25, 14), (39, 22), (37, 32), (13, 32)], fill=BLACK)
    draw.polygon([(11, 22), (25, 20), (39, 22), (34, 28), (16, 28)], fill=GOLD)
    draw.ellipse([23, 24, 27, 27], fill=WHITE)

# --- 6. Pointy Witch Hat ---
def draw_witch_hat(draw):
    draw.ellipse([8, 30, 42, 38], fill=BLACK)
    draw.polygon([(16, 30), (34, 30), (25, 10)], fill=BLACK)
    draw.rectangle([17, 28, 33, 31], fill=PURPLE)
    draw.rectangle([23, 27, 27, 32], fill=GOLD)

# --- 7. Starry Wizard Hat ---
def draw_wizard_hat(draw):
    draw.ellipse([8, 30, 42, 38], fill=DKBLUE)
    draw.polygon([(16, 30), (34, 30), (28, 12), (21, 8)], fill=DKBLUE)
    draw.ellipse([22, 16, 24, 18], fill=GOLD)
    draw.ellipse([28, 22, 30, 24], fill=GOLD)

# --- 8. Festive Santa Hat ---
def draw_santa_hat(draw):
    draw.polygon([(15, 28), (35, 28), (28, 14)], fill=RED)
    draw.polygon([(28, 14), (38, 22), (32, 22)], fill=RED)
    draw.rounded_rectangle([13, 28, 37, 34], radius=2, fill=WHITE)
    draw.ellipse([36, 20, 42, 26], fill=WHITE)

# --- 9. Wool Baker Boy Cap ---
def draw_baker_boy_cap(draw):
    draw.ellipse([12, 14, 38, 32], fill=DKGREY)
    draw.polygon([(14, 30), (36, 30), (33, 34), (17, 34)], fill=BLACK)
    draw.ellipse([23, 13, 27, 16], fill=GREY)

# --- 10. Retro 1920s Cloche Hat ---
def draw_cloche_hat(draw):
    draw.ellipse([14, 16, 36, 34], fill=PURPLE)
    draw.ellipse([12, 28, 38, 36], fill=PURPLE)
    draw.rectangle([14, 27, 36, 29], fill=PINK)

# --- 11. Sherlock Deerstalker Hat ---
def draw_deerstalker_hat(draw):
    draw.ellipse([14, 16, 36, 32], fill=BROWN)
    draw.polygon([(10, 30), (14, 30), (14, 34)], fill=BROWN)
    draw.polygon([(36, 30), (40, 30), (36, 34)], fill=BROWN)
    draw.polygon([(20, 16), (30, 16), (25, 12)], fill=DKBROWN)

# --- 12. Scottish Glengarry Bonnet ---
def draw_glengarry_bonnet(draw):
    draw.polygon([(14, 20), (36, 18), (38, 30), (12, 30)], fill=DKBLUE)
    draw.ellipse([23, 16, 27, 20], fill=RED)
    draw.line([14, 30, 10, 38], fill=BLACK, width=2)
    draw.line([14, 30, 15, 39], fill=BLACK, width=2)

# --- 13. Jazz Porkpie Hat ---
def draw_porkpie_hat(draw):
    draw.rounded_rectangle([15, 18, 35, 29], radius=1, fill=DKGREY)
    draw.rectangle([15, 26, 35, 29], fill=TEAL)
    draw.ellipse([12, 28, 38, 32], fill=DKGREY)

# --- 14. Summer Straw Fedora ---
def draw_fedora_straw(draw):
    draw.ellipse([14, 18, 36, 32], fill=BEIGE)
    draw.rectangle([14, 25, 36, 28], fill=BLACK)
    draw.ellipse([9, 26, 41, 34], fill=BEIGE)

# --- 15. Yellow Construction Hard Hat ---
def draw_hard_hat(draw):
    draw.ellipse([13, 16, 37, 33], fill=YELLOW)
    draw.rectangle([23, 16, 27, 28], fill=ORANGE)
    draw.ellipse([10, 29, 40, 34], fill=YELLOW)

# --- 16. Industrial Welding Mask ---
def draw_welding_mask(draw):
    draw.rounded_rectangle([14, 14, 36, 38], radius=4, fill=DKGREY)
    draw.rectangle([19, 20, 31, 25], fill=GREEN)
    draw.line([20, 21, 23, 21], fill=WHITE)

# --- 17. Tactical Gas Mask ---
def draw_gas_mask(draw):
    draw.rounded_rectangle([15, 14, 35, 38], radius=6, fill=BLACK)
    draw.ellipse([17, 18, 23, 24], fill=LIGHTBLUE)
    draw.ellipse([27, 18, 33, 24], fill=LIGHTBLUE)
    draw.ellipse([22, 26, 28, 32], fill=GREY)
    draw.ellipse([11, 28, 16, 33], fill=DKGREY)
    draw.ellipse([34, 28, 39, 33], fill=DKGREY)

# --- 18. Astronaut Space Helmet ---
def draw_space_helmet(draw):
    draw.ellipse([11, 11, 39, 39], fill=WHITE)
    draw.ellipse([15, 15, 35, 33], fill=GOLD)
    draw.line([18, 18, 25, 25], fill=WHITE, width=2)

# --- 19. Deep Sea Scuba Mask ---
def draw_scuba_mask(draw):
    draw.rounded_rectangle([12, 16, 38, 30], radius=3, fill=TEAL)
    draw.rectangle([15, 19, 35, 27], fill=LIGHTBLUE)
    draw.line([38, 22, 42, 22], fill=BLACK, width=2)
    draw.line([42, 22, 42, 10], fill=BLACK, width=2)
    draw.line([38, 22, 35, 24], fill=BLACK, width=2)

# --- 20. Red Firefighter Helmet ---
def draw_fireman_helmet(draw):
    draw.ellipse([13, 14, 37, 32], fill=RED)
    draw.polygon([(9, 30), (41, 30), (37, 36), (13, 36)], fill=RED)
    draw.polygon([(22, 18), (28, 18), (25, 24)], fill=GOLD)

# --- 21. Officer Police Cap ---
def draw_police_cap(draw):
    draw.ellipse([13, 15, 37, 31], fill=DKBLUE)
    draw.polygon([(14, 28), (36, 28), (33, 33), (17, 33)], fill=BLACK)
    draw.polygon([(23, 20), (27, 20), (25, 24)], fill=GOLD)
    draw.line([15, 27, 35, 27], fill=GOLD, width=1)

# --- 22. White Sailor Dixie Cup Hat ---
def draw_sailor_hat(draw):
    draw.polygon([(15, 18), (35, 18), (38, 30), (12, 30)], fill=WHITE)
    draw.rectangle([11, 27, 39, 31], fill=WHITE)
    draw.line([12, 29, 38, 29], fill=GREY)

# --- 23. Green Commando Beret ---
def draw_military_beret(draw):
    draw.ellipse([13, 15, 37, 29], fill=DKGREEN)
    draw.polygon([(28, 21), (38, 21), (34, 29)], fill=DKGREEN)
    draw.ellipse([18, 21, 21, 24], fill=RED)

# --- 24. Jet Fighter Pilot Helmet ---
def draw_pilot_helmet(draw):
    draw.ellipse([12, 12, 38, 36], fill=DKGREEN)
    draw.rounded_rectangle([15, 16, 35, 26], radius=2, fill=BLACK)
    draw.ellipse([10, 22, 14, 30], fill=BLACK)
    draw.ellipse([36, 22, 40, 30], fill=BLACK)

# --- 25. Tri-corner Jester Hat ---
def draw_jester_hat(draw):
    draw.polygon([(13, 26), (25, 26), (10, 10)], fill=PURPLE)
    draw.polygon([(25, 26), (37, 26), (40, 10)], fill=GREEN)
    draw.polygon([(19, 26), (31, 26), (25, 12)], fill=YELLOW)
    draw.ellipse([9, 9, 12, 12], fill=GOLD)
    draw.ellipse([38, 9, 41, 11], fill=GOLD)
    draw.ellipse([24, 11, 27, 14], fill=GOLD)
    draw.rectangle([13, 26, 37, 30], fill=RED)

# --- 26. Greek Laurel Wreath Crown ---
def draw_crown_laurel(draw):
    draw.arc([14, 18, 36, 32], start=0, end=360, fill=DKGREEN, width=2)
    draw.ellipse([12, 22, 15, 24], fill=GREEN)
    draw.ellipse([35, 22, 38, 24], fill=GREEN)
    draw.ellipse([15, 16, 18, 18], fill=GREEN)
    draw.ellipse([32, 16, 35, 18], fill=GREEN)
    draw.ellipse([23, 14, 27, 16], fill=GREEN)

# --- 27. Ancient Egyptian Nemes Headdress ---
def draw_pharaoh_nemes(draw):
    draw.polygon([(14, 12), (36, 12), (40, 36), (10, 36)], fill=DKBLUE)
    draw.line([18, 12, 18, 36], fill=GOLD, width=1)
    draw.line([22, 12, 22, 36], fill=GOLD, width=1)
    draw.line([28, 12, 28, 36], fill=GOLD, width=1)
    draw.line([32, 12, 32, 36], fill=GOLD, width=1)
    draw.line([25, 18, 25, 14], fill=GOLD, width=2)

# --- 28. Horned Viking Helmet ---
def draw_vikings_helmet(draw):
    draw.ellipse([14, 16, 36, 32], fill=STEEL)
    draw.line([25, 26, 25, 34], fill=STEEL, width=2)
    draw.polygon([(14, 20), (6, 12), (10, 24)], fill=WHITE)
    draw.polygon([(36, 20), (44, 12), (40, 24)], fill=WHITE)

# --- 29. Roman Centurion Galea Helmet ---
def draw_roman_galea(draw):
    draw.ellipse([14, 18, 36, 32], fill=STEEL)
    draw.polygon([(16, 18), (34, 18), (25, 8)], fill=RED)
    draw.rectangle([21, 8, 29, 18], fill=RED)
    draw.polygon([(14, 28), (16, 36), (18, 28)], fill=STEEL)
    draw.polygon([(36, 28), (34, 36), (32, 28)], fill=STEEL)

# --- 30. Samurai Kabuto Helmet ---
def draw_kabuto_helmet(draw):
    draw.ellipse([14, 15, 36, 31], fill=BLACK)
    draw.polygon([(25, 20), (14, 10), (22, 20)], fill=GOLD)
    draw.polygon([(25, 20), (36, 10), (28, 20)], fill=GOLD)
    draw.polygon([(11, 28), (39, 28), (36, 36), (14, 36)], fill=RED)

# --- 31. Steel Medieval Knight Helmet ---
def draw_knights_helm(draw):
    draw.rounded_rectangle([14, 14, 36, 38], radius=4, fill=STEEL)
    draw.line([18, 22, 32, 22], fill=BLACK, width=2)
    draw.line([22, 28, 22, 32], fill=BLACK)
    draw.line([25, 28, 25, 32], fill=BLACK)
    draw.line([28, 28, 28, 32], fill=BLACK)
    draw.ellipse([22, 8, 28, 14], fill=RED)

# --- 32. Black Ninja Mask ---
def draw_ninja_hood(draw):
    draw.rounded_rectangle([14, 12, 36, 42], radius=6, fill=BLACK)
    draw.rectangle([18, 20, 32, 26], fill=BEIGE)
    draw.ellipse([20, 22, 22, 24], fill=BLACK)
    draw.ellipse([28, 22, 30, 24], fill=BLACK)

# --- 33. Cold Weather Balaclava ---
def draw_balaclava(draw):
    draw.rounded_rectangle([14, 12, 36, 42], radius=6, fill=DKGREY)
    draw.ellipse([20, 18, 30, 24], fill=0)
    draw.ellipse([23, 28, 27, 31], fill=0)

# --- 34. Tartan Plaid Earmuffs ---
def draw_earmuffs_plaid(draw):
    draw.ellipse([10, 22, 16, 30], fill=RED)
    draw.ellipse([34, 22, 40, 30], fill=RED)
    draw.line([13, 22, 13, 30], fill=BLACK)
    draw.line([37, 22, 37, 30], fill=BLACK)
    draw.arc([13, 14, 37, 26], start=180, end=360, fill=GREY, width=2)

# --- 35. Cute Cat Sleeping Mask ---
def draw_sleeping_mask_cute(draw):
    draw.rounded_rectangle([12, 18, 38, 28], radius=4, fill=PINK)
    draw.polygon([(14, 18), (18, 18), (15, 14)], fill=PINK)
    draw.polygon([(32, 18), (36, 18), (35, 14)], fill=PINK)
    draw.arc([16, 21, 22, 25], start=0, end=180, fill=BLACK)
    draw.arc([28, 21, 34, 25], start=0, end=180, fill=BLACK)

# --- 36. Neon Tennis Headband ---
def draw_headband_sport(draw):
    draw.rectangle([13, 20, 37, 26], fill=GREEN)
    draw.line([13, 23, 37, 23], fill=RED, width=1)

# --- 37. Colorful Flower Crown Wreath ---
def draw_flower_crown(draw):
    draw.ellipse([14, 18, 36, 32], outline=DKGREEN, width=2)
    draw.ellipse([13, 20, 17, 24], fill=RED)
    draw.ellipse([33, 20, 37, 24], fill=YELLOW)
    draw.ellipse([23, 15, 27, 19], fill=PINK)

# --- 38. Bridal Lace Veil ---
def draw_veil_lace(draw):
    draw.rectangle([18, 14, 32, 17], fill=WHITE)
    draw.polygon([(18, 17), (32, 17), (38, 44), (12, 44)], fill=(245, 245, 245, 120))

# --- 39. Monocle with Gold Chain ---
def draw_monocle_chain(draw):
    draw.ellipse([16, 18, 26, 28], outline=GOLD, width=2)
    draw.line([18, 20, 24, 26], fill=LIGHTBLUE)
    draw.line([25, 26, 28, 34], fill=GOLD)
    draw.line([28, 34, 34, 38], fill=GOLD)

# --- 40. Victorian Lace Cravat ---
def draw_cravat_lace(draw):
    draw.rectangle([18, 15, 32, 18], fill=WHITE)
    draw.polygon([(18, 18), (32, 18), (28, 32), (22, 32)], fill=WHITE)
    draw.polygon([(20, 24), (30, 24), (27, 38), (23, 38)], fill=SILVER)

# --- 41. Chunky Knit Infinity Scarf ---
def draw_scarf_infinity(draw):
    draw.ellipse([13, 16, 37, 34], fill=TEAL)
    draw.ellipse([18, 20, 32, 30], fill=(255, 255, 255, 0))
    draw.ellipse([14, 22, 36, 34], fill=DKBLUE)
    draw.ellipse([19, 25, 31, 31], fill=(255, 255, 255, 0))

# --- 42. Bohemian Fringed Shawl ---
def draw_shawl_fringe(draw):
    draw.polygon([(10, 16), (40, 16), (25, 38)], fill=ORANGE)
    draw.polygon([(13, 20), (37, 20), (25, 32)], fill=RED)
    for x in range(12, 39, 3):
        draw.line([x, 16 + abs(25-x), x, 22 + abs(25-x)], fill=GOLD)

# --- 43. Deep Red Velvet Cape ---
def draw_cape_velvet(draw):
    draw.polygon([(18, 14), (32, 14), (42, 44), (8, 44)], fill=DKRED)
    draw.rectangle([22, 14, 28, 17], fill=GOLD)

# --- 44. Viking Fur Collar Cloak ---
def draw_cloak_fur(draw):
    draw.polygon([(16, 20), (34, 20), (40, 45), (10, 45)], fill=DKGREY)
    draw.ellipse([15, 12, 35, 22], fill=BEIGE)

# --- 45. Mexican Serape Poncho ---
def draw_poncho_serape(draw):
    draw.polygon([(12, 16), (38, 16), (42, 40), (8, 40)], fill=ORANGE)
    draw.rectangle([10, 24, 40, 27], fill=YELLOW)
    draw.rectangle([9, 29, 41, 32], fill=RED)
    draw.rectangle([8, 34, 42, 36], fill=GREEN)

# --- 46. Spanish Bolero Shrug Jacket ---
def draw_bolero_jacket(draw):
    draw.rectangle([14, 15, 36, 28], fill=BLACK)
    draw.polygon([(25, 15), (20, 28), (30, 28)], fill=(255, 255, 255, 0))
    draw.rectangle([9, 17, 14, 36], fill=BLACK)
    draw.rectangle([36, 17, 41, 36], fill=BLACK)

# --- 47. Drape Front Buttonless Cardigan ---
def draw_cardigan_buttonless(draw):
    draw.rectangle([13, 14, 37, 42], fill=GREY)
    draw.polygon([(25, 14), (20, 42), (30, 42)], fill=BEIGE)
    draw.rectangle([8, 16, 13, 38], fill=GREY)
    draw.rectangle([37, 16, 42, 38], fill=GREY)

# --- 48. Victorian Brocade Waistcoat ---
def draw_waistcoat_brocade(draw):
    draw.rectangle([15, 15, 35, 38], fill=PURPLE)
    draw.polygon([(21, 15), (29, 15), (25, 23)], fill=WHITE)
    for x, y in [(18, 18), (32, 18), (18, 26), (32, 26), (18, 34), (32, 34)]:
        draw.ellipse([x, y, x+2, y+2], fill=GOLD)

# --- 49. Leather Crafting Utility Apron ---
def draw_apron_craft(draw):
    draw.polygon([(18, 15), (32, 15), (35, 42), (15, 42)], fill=BROWN)
    draw.line([18, 15, 14, 8], fill=DKBROWN, width=2)
    draw.line([32, 15, 36, 8], fill=DKBROWN, width=2)
    draw.rectangle([20, 28, 30, 36], fill=DKBROWN)

# --- 50. Medical Scrub Cap ---
def draw_scrubs_hat(draw):
    draw.ellipse([14, 16, 36, 32], fill=TEAL)
    draw.line([25, 30, 20, 36], fill=TEAL, width=2)
    draw.line([25, 30, 30, 36], fill=TEAL, width=2)

DRAWINGS = {
    "fez_hat": draw_fez_hat,
    "turban": draw_turban,
    "crown_regal": draw_crown_regal,
    "tiara_crystal": draw_tiara_crystal,
    "pirate_hat": draw_pirate_hat,
    "witch_hat": draw_witch_hat,
    "wizard_hat": draw_wizard_hat,
    "santa_hat": draw_santa_hat,
    "baker_boy_cap": draw_baker_boy_cap,
    "cloche_hat": draw_cloche_hat,
    "deerstalker_hat": draw_deerstalker_hat,
    "glengarry_bonnet": draw_glengarry_bonnet,
    "porkpie_hat": draw_porkpie_hat,
    "fedora_straw": draw_fedora_straw,
    "hard_hat": draw_hard_hat,
    "welding_mask": draw_welding_mask,
    "gas_mask": draw_gas_mask,
    "space_helmet": draw_space_helmet,
    "scuba_mask": draw_scuba_mask,
    "fireman_helmet": draw_fireman_helmet,
    "police_cap": draw_police_cap,
    "sailor_hat": draw_sailor_hat,
    "military_beret": draw_military_beret,
    "pilot_helmet": draw_pilot_helmet,
    "jester_hat": draw_jester_hat,
    "crown_laurel": draw_crown_laurel,
    "pharaoh_nemes": draw_pharaoh_nemes,
    "vikings_helmet": draw_vikings_helmet,
    "roman_galea": draw_roman_galea,
    "kabuto_helmet": draw_kabuto_helmet,
    "knights_helm": draw_knights_helm,
    "ninja_hood": draw_ninja_hood,
    "balaclava": draw_balaclava,
    "earmuffs_plaid": draw_earmuffs_plaid,
    "sleeping_mask_cute": draw_sleeping_mask_cute,
    "headband_sport": draw_headband_sport,
    "flower_crown": draw_flower_crown,
    "veil_lace": draw_veil_lace,
    "monocle_chain": draw_monocle_chain,
    "cravat_lace": draw_cravat_lace,
    "scarf_infinity": draw_scarf_infinity,
    "shawl_fringe": draw_shawl_fringe,
    "cape_velvet": draw_cape_velvet,
    "cloak_fur": draw_cloak_fur,
    "poncho_serape": draw_poncho_serape,
    "bolero_jacket": draw_bolero_jacket,
    "cardigan_buttonless": draw_cardigan_buttonless,
    "waistcoat_brocade": draw_waistcoat_brocade,
    "apron_craft": draw_apron_craft,
    "scrubs_hat": draw_scrubs_hat
}

if __name__ == "__main__":
    print(f"Generating 50 new detailed clothing/hat sprites inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done!")
