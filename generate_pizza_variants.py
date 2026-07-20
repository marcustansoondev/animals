import os
from PIL import Image, ImageDraw

# Strict 10-Color Palette
BK = (20, 20, 20, 255); WH = (250, 250, 250, 255)
RED = (220, 50, 50, 255); DRED = (150, 20, 20, 255)
YEL = (250, 200, 50, 255); DYEL = (200, 150, 20, 255)
GRN = (50, 200, 50, 255); DGRN = (30, 150, 30, 255)
BRN = (180, 100, 50, 255); DBRN = (120, 60, 30, 255)
PURP = (140, 80, 195, 255)
DGY = (100, 100, 100, 255)
ORG = (250, 140, 30, 255); DORG = (180, 90, 20, 255)
OLV = (40, 40, 40, 255); LGY = (180, 180, 180, 255)
SHD = (0, 0, 0, 80)

def get_canvas():
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    return img, ImageDraw.Draw(img)

def quantize_10(img):
    bg = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    bg.paste(img, (0, 0), img)
    rgb = Image.new("RGB", (50, 50), (255, 255, 255))
    alpha = bg.split()[3]
    rgb.paste(bg, mask=alpha)
    q = rgb.quantize(colors=9, method=Image.MEDIANCUT, dither=Image.NONE)
    f = q.convert("RGBA")
    fp = f.load()
    for y in range(50):
        for x in range(50):
            orig_a = alpha.getpixel((x, y))
            r, g, b, _ = fp[x, y]
            fp[x, y] = (r, g, b, orig_a)
    return f

def base_slice(d, cheese_color=YEL):
    # Crust base (thick bottom crust)
    d.polygon([(9, 11), (41, 11), (25, 46)], outline=DBRN, fill=BRN)
    # Inner crust shadow for depth
    d.polygon([(11, 13), (39, 13), (25, 43)], fill=DORG)
    # Cheese layer
    d.polygon([(12, 14), (38, 14), (25, 41)], fill=cheese_color)
    
    # Cheese highlights and textures (small dots/blobs)
    if cheese_color == YEL:
        d.polygon([(15, 17), (20, 17), (17, 21)], fill=WH)
        d.polygon([(30, 20), (35, 20), (32, 24)], fill=WH)
        d.ellipse([22, 28, 25, 31], fill=WH)
        d.ellipse([20, 16, 22, 18], fill=ORG)
        d.ellipse([31, 28, 33, 30], fill=ORG)
        d.ellipse([26, 36, 27, 37], fill=ORG)
    elif cheese_color == WH:
        d.polygon([(15, 17), (20, 17), (17, 21)], fill=LGY)
        d.ellipse([22, 28, 25, 31], fill=LGY)
        d.ellipse([30, 20, 32, 22], fill=LGY)
    
    # Top crust (3D bulky look)
    d.rectangle([6, 6, 44, 11], fill=BRN, outline=DBRN, width=1)
    d.rectangle([8, 8, 42, 9], fill=ORG) # highlight on crust
    d.rectangle([10, 11, 40, 12], fill=DBRN) # shadow under crust
    
    # Cheese melting off the crust
    d.polygon([(14, 11), (19, 11), (16, 16)], fill=cheese_color)
    d.polygon([(31, 11), (36, 11), (33, 17)], fill=cheese_color)
    if cheese_color == YEL:
        d.polygon([(15, 12), (17, 12), (16, 15)], fill=WH)
        d.polygon([(32, 12), (34, 12), (33, 16)], fill=WH)

def draw_margherita():
    i, d = get_canvas()
    base_slice(d)
    d.ellipse([15, 15, 23, 23], fill=WH, outline=LGY)
    d.ellipse([27, 19, 35, 27], fill=WH, outline=LGY)
    d.ellipse([19, 27, 27, 35], fill=WH, outline=LGY)
    # Basil leaves
    d.polygon([(14, 20), (16, 17), (19, 23)], fill=DGRN)
    d.polygon([(15, 21), (16, 18), (18, 22)], fill=GRN)
    d.polygon([(30, 26), (34, 23), (33, 29)], fill=DGRN)
    d.polygon([(31, 26), (33, 24), (32, 28)], fill=GRN)
    d.polygon([(24, 33), (22, 35), (27, 37)], fill=DGRN)
    d.polygon([(24, 34), (23, 35), (26, 36)], fill=GRN)
    return quantize_10(i)

def draw_mushroom():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32)]:
        d.ellipse([cx-4, cy-4, cx+4, cy], fill=DBRN) # shadow
        d.ellipse([cx-3, cy-3, cx+3, cy], fill=DGY) # cap
        d.ellipse([cx-2, cy-2, cx+1, cy-1], fill=WH) # highlight
        d.rectangle([cx-1, cy, cx+1, cy+3], fill=DGY) # stem
    return quantize_10(i)

def draw_veggie():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(18, 18), (25, 28), (30, 34)]:
        d.ellipse([cx-3, cy-3, cx+3, cy+3], outline=OLV, width=2)
        d.point((cx-1, cy-1), fill=WH)
    for px, py in [(32, 18), (20, 34), (25, 20)]:
        d.line([(px-3, py-3), (px+3, py+3)], fill=DGRN, width=3)
        d.line([(px-2, py-2), (px+2, py+2)], fill=GRN, width=1)
    d.arc([14, 24, 22, 32], 0, 180, fill=PURP, width=2)
    d.arc([15, 25, 21, 31], 0, 180, fill=WH, width=1)
    return quantize_10(i)

def draw_bbqchicken():
    i, d = get_canvas()
    base_slice(d, cheese_color=ORG)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32)]:
        d.rectangle([cx-4, cy-3, cx+4, cy+3], fill=BK) # shadow
        d.rectangle([cx-3, cy-2, cx+3, cy+2], fill=DBRN) # chicken
        d.rectangle([cx-2, cy-1, cx, cy], fill=BRN) # highlight
    for cx, cy in [(25, 20), (22, 28), (28, 30)]:
        d.arc([cx-4, cy-4, cx+4, cy+4], 0, 180, fill=PURP, width=2)
    return quantize_10(i)

def draw_supreme():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(16, 17), (26, 32)]:
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=DBRN)
        d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=DRED)
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=RED)
        d.point((cx-1, cy-1), fill=WH)
    d.ellipse([29, 15, 35, 19], fill=DGY)
    d.rectangle([31, 19, 33, 21], fill=DGY)
    d.ellipse([21, 23, 27, 29], outline=OLV, width=2)
    d.line([(17, 31), (23, 35)], fill=GRN, width=2)
    return quantize_10(i)

def draw_white():
    i, d = get_canvas()
    base_slice(d, cheese_color=WH)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32)]:
        d.polygon([(cx-3, cy), (cx, cy-3), (cx+3, cy), (cx, cy+3)], fill=DGRN)
        d.polygon([(cx-1, cy), (cx, cy-1), (cx+1, cy), (cx, cy+1)], fill=GRN)
    return quantize_10(i)

def draw_olive():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32), (25, 20), (22, 24), (28, 24)]:
        d.ellipse([cx-3, cy-3, cx+3, cy+3], outline=OLV, width=2)
        d.point((cx-1, cy-1), fill=WH)
    return quantize_10(i)

def draw_sausage():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32), (25, 20)]:
        d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=BK)
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=DBRN)
        d.point((cx-1, cy-1), fill=BRN)
    return quantize_10(i)

def draw_jalapeno():
    i, d = get_canvas()
    base_slice(d)
    for cx, cy in [(18, 18), (32, 18), (25, 28), (20, 34), (30, 32)]:
        d.ellipse([cx-4, cy-4, cx+4, cy+4], outline=DGRN, width=3)
        d.ellipse([cx-3, cy-3, cx+3, cy+3], outline=GRN, width=1)
        d.point((cx, cy), fill=DGRN)
    return quantize_10(i)

def draw_pizzapie():
    i, d = get_canvas()
    # Shadow under pizza
    d.ellipse([3, 5, 47, 48], fill=DBRN)
    
    # Crust
    d.ellipse([2, 2, 48, 48], fill=BRN, outline=DBRN, width=2)
    # Crust inner shadow
    d.ellipse([4, 4, 46, 46], fill=DORG)
    # Crust highlight
    d.arc([5, 5, 45, 45], 180, 360, fill=ORG, width=2)
    
    # Cheese base
    d.ellipse([8, 8, 42, 42], fill=YEL)
    # Cheese textures
    d.ellipse([15, 15, 25, 25], fill=WH)
    d.ellipse([30, 25, 38, 33], fill=WH)
    d.ellipse([20, 30, 24, 34], fill=WH)
    d.ellipse([25, 15, 27, 17], fill=ORG)
    d.ellipse([15, 25, 17, 27], fill=ORG)
    
    # Pepperonis with shading
    for cx, cy in [(15, 15), (35, 15), (25, 25), (15, 35), (35, 35), (25, 12), (25, 38), (12, 25), (38, 25)]:
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=DBRN) # Drop shadow
        d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=DRED)
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=RED)
        d.point((cx-1, cy-1), fill=WH) # Highlight
        d.point((cx+1, cy+1), fill=DRED) # Shadow
        
    # Cut lines (deep cuts)
    d.line([(25, 8), (25, 42)], fill=DORG, width=2)
    d.line([(8, 25), (42, 25)], fill=DORG, width=2)
    d.line([(13, 13), (37, 37)], fill=DORG, width=2)
    d.line([(13, 37), (37, 13)], fill=DORG, width=2)
    
    # Cheese strings over cuts
    d.line([(24, 15), (26, 17)], fill=YEL, width=1)
    d.line([(15, 24), (17, 26)], fill=YEL, width=1)
    d.line([(34, 34), (36, 36)], fill=YEL, width=1)
    
    return quantize_10(i)

VARIANTS = [
    ("margheritapizza", draw_margherita, "Margherita Pizza Slice", "Fast Food", "Tomato & Basil", "★★★☆☆", "A classic slice with fresh mozzarella patches and basil leaves."),
    ("mushroompizza", draw_mushroom, "Mushroom Pizza Slice", "Fast Food", "Mushrooms", "★★☆☆☆", "A savory slice of pizza topped with sliced grey mushrooms."),
    ("veggiepizza", draw_veggie, "Veggie Pizza Slice", "Fast Food", "Vegetables", "★★★☆☆", "A colorful pizza slice loaded with olives, peppers, and onions."),
    ("bbqchickenpizza", draw_bbqchicken, "BBQ Chicken Pizza Slice", "Fast Food", "Chicken & BBQ", "★★★★☆", "A tangy slice with BBQ sauce, chicken chunks, and red onions."),
    ("supremepizza", draw_supreme, "Supreme Pizza Slice", "Fast Food", "Mixed Toppings", "★★★★☆", "The ultimate slice loaded with pepperoni, veggies, and olives."),
    ("whitepizza", draw_white, "White Pizza Slice", "Fast Food", "Ricotta & Spinach", "★★★☆☆", "A rich slice with white cheeses and fresh spinach leaves."),
    ("olivepizza", draw_olive, "Olive Pizza Slice", "Fast Food", "Black Olives", "★★☆☆☆", "A tasty pizza slice covered generously in black olive rings."),
    ("sausagepizza", draw_sausage, "Sausage Pizza Slice", "Fast Food", "Italian Sausage", "★★★☆☆", "A meaty slice topped with savory Italian sausage crumbles."),
    ("jalapenopizza", draw_jalapeno, "Jalapeno Pizza Slice", "Fast Food", "Jalapeno", "★★★☆☆", "A spicy pizza slice topped with green jalapeno rings."),
    ("pizzapie_whole", draw_pizzapie, "Whole Pizza Pie", "Meal", "Cheese & Pepperoni", "★★★★★", "A full, unsliced round pizza pie fresh from the oven.")
]

if __name__ == "__main__":
    os.makedirs("images/food_desserts", exist_ok=True)
    for cid, func, name, type_cat, material, rarity, desc in VARIANTS:
        img = func()
        out_path = f"images/food_desserts/{cid}_50x50.png"
        img.save(out_path)
        print(f"Generated highly detailed {out_path}")
