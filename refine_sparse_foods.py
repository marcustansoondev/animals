import sys
import generate_food_desserts as gen

# Pull in palette for easy use
BK = gen.BK; WH = gen.WH; WHITE = gen.WH
RED = gen.RED; DRED = gen.DRED
YEL = gen.YEL; DYEL = gen.DYEL
GRN = gen.GRN; DGRN = gen.DGRN
BRN = gen.BRN; BROWN = gen.BRN
DBRN = gen.DBRN; LBRN = gen.LBRN
CREAM = gen.CREAM; ORNG = gen.ORNG
PNK = gen.PNK; DPNK = gen.DPNK
BLU = gen.BLU; LBLU = gen.LBLU
PURP = gen.PURP; DGY = gen.DGY
SHD = gen.SHD

def draw_churro(d):
    # Two thick churros crossing with chocolate dip
    d.polygon([(10, 36), (36, 10), (42, 16), (16, 42)], fill=BRN)
    d.polygon([(12, 34), (34, 12), (40, 18), (18, 40)], fill=LBRN)
    d.polygon([(8, 26), (26, 8), (32, 14), (14, 32)], fill=BRN)
    d.polygon([(10, 24), (24, 10), (30, 16), (16, 30)], fill=LBRN)
    
    # Ridges
    for i in range(12, 34, 4):
        d.line([(i, 46-i), (i+6, 52-i)], fill=DBRN, width=1)
        
    # Chocolate dip at the bottom
    d.polygon([(10, 36), (22, 24), (32, 34), (20, 46)], fill=DBRN)
    d.polygon([(8, 26), (18, 16), (28, 26), (18, 36)], fill=DBRN)

def draw_yakitori(d):
    # Two thick skewers
    d.line([(10, 40), (25, 10)], fill=LBRN, width=3)
    d.line([(25, 45), (40, 15)], fill=LBRN, width=3)
    
    # Meat chunks
    for cx, cy in [(14, 32), (18, 24), (22, 16)]:
        d.ellipse([cx-6, cy-6, cx+6, cy+6], fill=DBRN)
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=BRN)
        d.line([(cx-2, cy-2), (cx+2, cy+2)], fill=DRED, width=2)
        
    for cx, cy in [(29, 37), (33, 29), (37, 21)]:
        d.ellipse([cx-6, cy-6, cx+6, cy+6], fill=DBRN)
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=BRN)
        d.line([(cx-2, cy-2), (cx+2, cy+2)], fill=DRED, width=2)

def draw_bruschetta(d):
    # Large bread slice
    d.polygon([(8, 25), (25, 10), (45, 25), (25, 45)], fill=BRN)
    d.polygon([(10, 25), (25, 12), (43, 25), (25, 43)], fill=LBRN)
    
    # Tomato cubes & basil
    for x, y in [(20, 20), (25, 18), (30, 22), (22, 28), (28, 26), (25, 32), (18, 25), (32, 28)]:
        d.polygon([(x, y-3), (x+3, y), (x, y+3), (x-3, y)], fill=RED)
        d.point((x, y), fill=DRED)
        
    for x, y in [(16, 22), (32, 20), (25, 38), (36, 25)]:
        d.polygon([(x, y-2), (x+4, y-2), (x+2, y+2)], fill=GRN)

def draw_candycane(d):
    # Thick candy cane
    d.arc([10, 10, 30, 30], start=180, end=0, fill=WH, width=8)
    d.line([(30, 20), (30, 45)], fill=WH, width=8)
    
    # Red stripes
    d.arc([10, 10, 30, 30], start=200, end=240, fill=RED, width=9)
    d.arc([10, 10, 30, 30], start=280, end=320, fill=RED, width=9)
    d.arc([10, 10, 30, 30], start=340, end=20, fill=RED, width=9)
    d.line([(26, 25), (34, 28)], fill=RED, width=4)
    d.line([(26, 35), (34, 38)], fill=RED, width=4)
    d.line([(26, 45), (34, 48)], fill=RED, width=4)

def draw_corncob(d):
    # Big corn cob
    d.polygon([(10, 40), (40, 10), (45, 15), (15, 45)], fill=YEL)
    
    # Husk
    d.polygon([(8, 42), (20, 30), (10, 48), (5, 45)], fill=GRN)
    d.polygon([(15, 48), (30, 35), (20, 52), (10, 50)], fill=DGRN)
    d.polygon([(5, 35), (25, 15), (15, 25), (8, 40)], fill=GRN)
    
    # Kernels grid
    for i in range(14, 38, 4):
        d.line([(i, 52-i), (i+6, 58-i)], fill=DYEL, width=1)
        d.line([(52-i, i), (58-i, i+6)], fill=DYEL, width=1)

def draw_empanada(d):
    # Thick empanada shape
    d.chord([8, 15, 42, 45], start=180, end=0, fill=LBRN)
    
    # Crimped edge
    for x in range(8, 42, 4):
        d.ellipse([x-2, 26, x+4, 32], fill=BRN)
        
    # Fried texture dots
    for x, y in [(15, 20), (25, 18), (35, 22), (20, 24), (30, 24)]:
        d.point((x, y), fill=DBRN)

def draw_gyoza(d):
    # Three gyoza
    for y_offset in [10, 22, 34]:
        # Body
        d.chord([10, y_offset, 40, y_offset+20], start=180, end=0, fill=CREAM)
        # Crispy bottom
        d.line([(12, y_offset+10), (38, y_offset+10)], fill=BRN, width=3)
        # Crimps
        for x in range(12, 38, 4):
            d.line([(x, y_offset), (x+2, y_offset+6)], fill=LBRN, width=2)

def draw_nachos(d):
    # Big pile of chips
    d.polygon([(8, 30), (25, 10), (42, 30), (25, 45)], fill=YEL)
    d.polygon([(5, 20), (20, 5), (35, 25), (15, 35)], fill=LBRN)
    d.polygon([(15, 40), (35, 20), (48, 35), (25, 48)], fill=YEL)
    
    # Cheese melt
    d.polygon([(12, 25), (25, 15), (38, 25), (25, 35)], fill=ORNG)
    d.polygon([(20, 35), (30, 25), (42, 35), (30, 45)], fill=ORNG)
    
    # Jalapenos & salsa
    for x, y in [(25, 20), (18, 28), (35, 30), (28, 40)]:
        d.ellipse([x, y, x+4, y+4], fill=GRN)
        d.point((x+2, y+2), fill=WH)
    for x, y in [(30, 18), (22, 32), (40, 25)]:
        d.ellipse([x, y, x+3, y+3], fill=RED)

def draw_onigiri(d):
    # Big rice triangle
    d.polygon([(25, 8), (42, 38), (8, 38)], fill=WH)
    d.polygon([(25, 12), (38, 35), (12, 35)], fill=CREAM) # shading
    
    # Seaweed wrap
    d.polygon([(20, 28), (30, 28), (32, 42), (18, 42)], fill=BK)
    d.polygon([(22, 30), (28, 30), (29, 40), (21, 40)], fill=DGRN)
    
    # Plum filling poking out top
    d.ellipse([23, 15, 27, 20], fill=RED)

def draw_pecanpie(d):
    # Whole pie
    d.ellipse([6, 10, 44, 40], fill=DBRN)
    d.ellipse([8, 12, 42, 38], fill=LBRN) # crust
    d.ellipse([10, 14, 40, 36], fill=BRN) # filling
    
    # Pecans everywhere
    pecans = [(25, 18), (18, 24), (32, 24), (25, 30), (20, 32), (30, 32), (15, 20), (35, 20), (25, 24)]
    for px, py in pecans:
        d.ellipse([px-4, py-3, px+4, py+3], fill=DBRN)
        d.line([(px-3, py), (px+3, py)], fill=LBRN, width=2)

def draw_profiteroles(d):
    # Stack of pastry puffs
    puffs = [(15, 28), (35, 28), (25, 35), (25, 15), (18, 20), (32, 20)]
    for px, py in puffs:
        d.ellipse([px-8, py-8, px+8, py+8], fill=LBRN)
        d.ellipse([px-6, py-6, px+6, py+6], fill=CREAM)
        
    # Chocolate drizzle
    d.line([(25, 8), (15, 28), (25, 45)], fill=DBRN, width=3)
    d.line([(25, 8), (35, 28), (25, 45)], fill=DBRN, width=3)
    d.line([(18, 20), (32, 20)], fill=DBRN, width=3)

def draw_samosa(d):
    # Two large samosas
    d.polygon([(25, 8), (42, 35), (8, 35)], fill=BRN)
    d.polygon([(25, 12), (38, 32), (12, 32)], fill=LBRN)
    
    d.polygon([(35, 15), (48, 40), (20, 45)], fill=BRN)
    d.polygon([(35, 20), (45, 38), (23, 42)], fill=LBRN)
    
    # Flaky crust texture
    for x, y in [(25, 20), (20, 30), (30, 30), (35, 30), (40, 35)]:
        d.point((x, y), fill=DBRN)
        d.point((x+1, y), fill=YEL)

def draw_satay(d):
    # Three skewers
    for offset in [-8, 0, 8]:
        d.line([(10+offset, 40-offset), (30+offset, 10-offset)], fill=LBRN, width=2)
        # Meat
        for i in range(3):
            cx = 15 + offset + i * 5
            cy = 30 - offset - i * 5
            d.polygon([(cx-4, cy-4), (cx+4, cy-4), (cx+4, cy+4), (cx-4, cy+4)], fill=BRN)
            d.polygon([(cx-2, cy-2), (cx+2, cy-2), (cx+2, cy+2), (cx-2, cy+2)], fill=YEL)
        
        # Peanut sauce
        d.line([(15+offset, 30-offset), (25+offset, 20-offset)], fill=ORNG, width=3)

def draw_springroll(d):
    # Two big spring rolls
    d.polygon([(10, 30), (30, 10), (40, 20), (20, 40)], fill=BRN)
    d.polygon([(12, 28), (28, 12), (36, 20), (20, 36)], fill=LBRN)
    
    d.polygon([(15, 40), (35, 20), (45, 30), (25, 50)], fill=BRN)
    d.polygon([(17, 38), (33, 22), (41, 30), (25, 46)], fill=LBRN)
    
    # Herbs showing
    d.polygon([(30, 10), (35, 5), (40, 10)], fill=GRN)
    d.polygon([(35, 20), (40, 15), (45, 20)], fill=ORNG)
    
    # Sweet chili sauce bowl
    d.ellipse([5, 5, 20, 20], fill=WH)
    d.ellipse([7, 7, 18, 18], fill=RED)
    d.point((12, 12), fill=YEL)

def draw_elote(d):
    # Big corn cob with cheese and chili
    d.polygon([(10, 40), (40, 10), (46, 16), (16, 46)], fill=YEL)
    d.polygon([(12, 38), (38, 12), (42, 16), (16, 42)], fill=WH) # mayo/cheese
    
    # Stick
    d.line([(5, 45), (15, 35)], fill=LBRN, width=4)
    
    # Chili powder and cheese crumbs
    for i in range(15, 40, 3):
        d.point((i, 48-i), fill=RED)
        d.point((i+2, 50-i), fill=RED)
        d.point((i-1, 46-i), fill=CREAM)
        d.point((i+3, 52-i), fill=YEL)

def draw_garlicbread(d):
    # Thick baguette slices
    d.polygon([(5, 25), (25, 5), (45, 25), (25, 45)], fill=BRN)
    d.polygon([(8, 25), (25, 8), (42, 25), (25, 42)], fill=CREAM)
    
    # Butter & Garlic
    d.polygon([(15, 25), (25, 15), (35, 25), (25, 35)], fill=YEL)
    
    # Parsley sprinkles
    for x, y in [(25, 25), (20, 20), (30, 30), (20, 30), (30, 20), (15, 25), (35, 25)]:
        d.ellipse([x, y, x+2, y+2], fill=GRN)

def draw_garlicknots(d):
    # Pile of knots
    knots = [(15, 15), (35, 15), (25, 25), (15, 35), (35, 35)]
    for cx, cy in knots:
        d.ellipse([cx-8, cy-8, cx+8, cy+8], fill=BRN)
        d.ellipse([cx-6, cy-6, cx+6, cy+6], fill=LBRN)
        # Knot folds
        d.arc([cx-6, cy-6, cx+6, cy+6], start=0, end=180, fill=DBRN, width=2)
        d.arc([cx-4, cy-4, cx+4, cy+4], start=180, end=360, fill=DBRN, width=2)
        # Parsley
        d.point((cx-2, cy-2), fill=GRN)
        d.point((cx+2, cy+2), fill=GRN)

def draw_scone(d):
    # Large triangular scone
    d.polygon([(10, 40), (40, 40), (25, 10)], fill=BRN)
    d.polygon([(12, 38), (38, 38), (25, 13)], fill=LBRN)
    
    # Jam and cream on top
    d.ellipse([20, 20, 30, 30], fill=RED)
    d.ellipse([22, 22, 28, 28], fill=WH)
    
    # Currants inside
    for x, y in [(18, 35), (32, 35), (25, 30), (15, 30), (35, 30)]:
        d.ellipse([x, y, x+2, y+2], fill=DBRN)

def draw_crabrangoon(d):
    # Three star-shaped rangoons
    rangoons = [(25, 15), (15, 35), (35, 35)]
    for cx, cy in rangoons:
        d.polygon([(cx, cy-10), (cx+4, cy-4), (cx+10, cy), (cx+4, cy+4), 
                   (cx, cy+10), (cx-4, cy+4), (cx-10, cy), (cx-4, cy-4)], fill=BRN)
        d.polygon([(cx, cy-7), (cx+3, cy-3), (cx+7, cy), (cx+3, cy+3), 
                   (cx, cy+7), (cx-3, cy+3), (cx-7, cy), (cx-3, cy-3)], fill=LBRN)
        # Cream cheese center
        d.ellipse([cx-2, cy-2, cx+2, cy+2], fill=WH)

# Map functions
funcs = {
    "churro": draw_churro,
    "yakitori": draw_yakitori,
    "bruschetta": draw_bruschetta,
    "candycane": draw_candycane,
    "corncob": draw_corncob,
    "empanada": draw_empanada,
    "gyoza": draw_gyoza,
    "nachos": draw_nachos,
    "onigiri": draw_onigiri,
    "pecanpie": draw_pecanpie,
    "profiteroles": draw_profiteroles,
    "samosa": draw_samosa,
    "satay": draw_satay,
    "springroll": draw_springroll,
    "elote": draw_elote,
    "garlicbread": draw_garlicbread,
    "garlicknots": draw_garlicknots,
    "scone": draw_scone,
    "crabrangoon": draw_crabrangoon
}

for name, fn in funcs.items():
    gen.save_sprite(name, fn)

print("Successfully replaced all 19 sparse food/dessert sprites.")
