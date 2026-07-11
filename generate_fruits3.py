import os
import random
import math
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/fruits"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    
    alpha = img.split()[3]
    mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
    img.paste((0, 0, 0, 0), mask=mask)
    
    # Quantize to 9 colors + transparency = 10 colors
    img = img.quantize(colors=9).convert("RGBA")
    
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a < 255:
                pixels[x, y] = (0, 0, 0, 0)
                
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    img.save(path)
    print(f"  Saved: {path}")

# Palette definitions
RED         = (210, 30, 30, 255)
DKRED       = (120, 15, 15, 255)
LIGHTRED    = (255, 100, 100, 255)
ORANGE      = (255, 120, 0, 255)
DKORANGE    = (170, 70, 0, 255)
LIGHTORANGE = (255, 175, 70, 255)
YELLOW      = (245, 215, 30, 255)
LIGHTYELLOW = (255, 245, 130, 255)
DKYELLOW    = (165, 140, 10, 255)
GREEN       = (40, 160, 40, 255)
DKGREEN     = (20, 85, 20, 255)
LIGHTGREEN  = (120, 220, 120, 255)
BROWN       = (110, 70, 25, 255)
DKBROWN     = (65, 40, 10, 255)
LIGHTBROWN  = (160, 115, 70, 255)
WHITE       = (255, 255, 255, 255)
BLACK       = (15, 15, 15, 255)
DARKBLUE    = (20, 30, 70, 255)
MIDBLUE     = (45, 75, 160, 255)
LIGHTBLUE   = (135, 190, 255, 255)
PURPLE      = (95, 35, 120, 255)
DKPURPLE    = (50, 15, 70, 255)
LIGHTPURPLE = (175, 100, 200, 255)
BEIGE       = (225, 195, 155, 255)
GREY        = (180, 180, 180, 255)
DKGREY      = (90, 90, 90, 255)
MAGENTA     = (200, 20, 120, 255)
CYAN        = (20, 200, 200, 255)

def draw_sphere(d, bbox, color_dark, color_mid, color_light, highlight_offset=0.3):
    x0, y0, x1, y1 = bbox
    w, h = x1 - x0, y1 - y0
    d.ellipse([x0, y0, x1, y1], fill=color_dark)
    d.ellipse([x0 + w*0.1, y0 + h*0.1, x1 - w*0.1, y1 - h*0.1], fill=color_mid)
    d.ellipse([x0 + w*highlight_offset, y0 + h*highlight_offset, x1 - w*(1-highlight_offset-0.2), y1 - h*(1-highlight_offset-0.2)], fill=color_light)
    d.ellipse([x0 + w*(highlight_offset+0.1), y0 + h*(highlight_offset+0.1), x0 + w*(highlight_offset+0.2), y0 + h*(highlight_offset+0.2)], fill=WHITE)

def draw_texture(d, bbox, color, density=20, size=1):
    x0, y0, x1, y1 = bbox
    random.seed(x0*y1) # deterministic
    for _ in range(density):
        px, py = random.randint(int(x0), int(x1)), random.randint(int(y0), int(y1))
        # check if in ellipse roughly
        cx, cy = (x0+x1)/2, (y0+y1)/2
        rx, ry = (x1-x0)/2, (y1-y0)/2
        if ((px-cx)**2)/(rx**2) + ((py-cy)**2)/(ry**2) <= 1:
            d.ellipse([px, py, px+size, py+size], fill=color)

def draw_leaf(d, x, y, angle_deg, length, width, color1, color2):
    rad = math.radians(angle_deg)
    dx = math.cos(rad) * length
    dy = math.sin(rad) * length
    dx_w = math.cos(rad + math.pi/2) * width
    dy_w = math.sin(rad + math.pi/2) * width
    pts = [(x, y), (x+dx/2+dx_w, y+dy/2+dy_w), (x+dx, y+dy), (x+dx/2-dx_w, y+dy/2-dy_w)]
    d.polygon(pts, fill=color1)
    d.line([(x, y), (x+dx, y+dy)], fill=color2, width=1)

# 1. Damson
def draw_damson(d):
    draw_leaf(d, 25, 8, -45, 15, 8, GREEN, DKGREEN)
    draw_sphere(d, [10, 8, 40, 46], DKPURPLE, DARKBLUE, MIDBLUE, 0.25)
    draw_texture(d, [12, 10, 38, 44], LIGHTBLUE, density=60, size=1)
    d.line([(25, 8), (27, 2)], fill=DKBROWN, width=2)
    d.arc([15, 10, 35, 40], start=180, end=270, fill=LIGHTBLUE, width=1)

# 2. Honeyberry
def draw_honeyberry(d):
    draw_leaf(d, 25, 10, 20, 18, 6, DKGREEN, GREEN)
    d.rounded_rectangle([14, 10, 36, 44], radius=8, fill=DKPURPLE)
    d.rounded_rectangle([16, 12, 34, 42], radius=6, fill=DARKBLUE)
    d.rounded_rectangle([20, 16, 30, 38], radius=4, fill=MIDBLUE)
    draw_texture(d, [14, 10, 36, 44], LIGHTBLUE, density=50)
    d.ellipse([22, 18, 26, 26], fill=LIGHTBLUE)
    d.polygon([(20, 44), (25, 40), (30, 44), (25, 42)], fill=DKBROWN)
    d.line([(25, 10), (25, 4)], fill=DKBROWN, width=2)

# 3. Acai
def draw_acai(d):
    d.line([(25, 4), (25, 20)], fill=BROWN, width=2)
    d.line([(25, 15), (15, 25)], fill=BROWN, width=1)
    d.line([(25, 15), (35, 25)], fill=BROWN, width=1)
    d.line([(25, 20), (20, 35)], fill=BROWN, width=1)
    d.line([(25, 20), (30, 35)], fill=BROWN, width=1)
    coords = [(15,25), (35,25), (20,35), (30,35), (25,40), (12,30), (38,30)]
    for bx, by in coords:
        draw_sphere(d, [bx-6, by-6, bx+6, by+6], BLACK, DKPURPLE, MIDBLUE, 0.2)
        d.point((bx-2, by-2), fill=LIGHTPURPLE)

# 4. Goji Berry
def draw_goji_berry(d):
    draw_leaf(d, 20, 15, -120, 12, 4, GREEN, DKGREEN)
    for ox, oy, rot in [(18, 28, -15), (32, 22, 20), (26, 36, 5)]:
        d.ellipse([ox-7, oy-14, ox+7, oy+14], fill=DKRED)
        d.ellipse([ox-5, oy-12, ox+5, oy+12], fill=RED)
        d.ellipse([ox-2, oy-8, ox+2, oy+4], fill=LIGHTRED)
        d.line([(ox, oy-14), (ox+2, oy-20)], fill=DKGREEN, width=1)
        d.point((ox, oy-8), fill=WHITE)

# 5. Seabuckthorn
def draw_seabuckthorn(d):
    d.line([(5, 45), (45, 5)], fill=DKBROWN, width=4)
    d.line([(7, 43), (43, 7)], fill=BROWN, width=2)
    draw_leaf(d, 35, 15, -30, 15, 4, LIGHTGREEN, GREEN)
    draw_leaf(d, 15, 35, 150, 15, 4, LIGHTGREEN, GREEN)
    for bx, by in [(20, 30), (26, 24), (32, 18), (14, 36), (28, 30), (34, 24), (22, 38), (38, 28), (18, 24)]:
        draw_sphere(d, [bx-5, by-5, bx+5, by+5], DKORANGE, ORANGE, LIGHTORANGE, 0.3)
        draw_texture(d, [bx-5, by-5, bx+5, by+5], BROWN, density=3, size=1)
        d.point((bx, by-2), fill=WHITE)

# 6. Salmonberry
def draw_salmonberry(d):
    draw_leaf(d, 25, 16, 160, 14, 7, GREEN, DKGREEN)
    draw_leaf(d, 25, 16, 20, 14, 7, GREEN, DKGREEN)
    d.polygon([(25, 44), (10, 20), (40, 20)], fill=DKORANGE)
    druplets = [(25,40), (21,36), (29,36), (17,32), (25,32), (33,32), (13,28), (21,28), (29,28), (37,28), (17,24), (25,24), (33,24), (21,20), (29,20)]
    for dx, dy in druplets:
        draw_sphere(d, [dx-5, dy-5, dx+5, dy+5], DKORANGE, ORANGE, LIGHTORANGE, 0.2)
    d.polygon([(15, 20), (25, 12), (35, 20)], fill=DKGREEN)
    d.polygon([(20, 20), (25, 16), (30, 20)], fill=GREEN)
    d.line([(25, 12), (25, 4)], fill=BROWN, width=2)

# 7. Thimbleberry
def draw_thimbleberry(d):
    draw_leaf(d, 25, 12, 180, 16, 12, DKGREEN, GREEN)
    d.ellipse([8, 16, 42, 40], fill=DKRED)
    for y in range(20, 38, 4):
        for x in range(12, 38, 4):
            if ((x-25)**2)/220 + ((y-28)**2)/80 <= 1:
                draw_sphere(d, [x-3, y-3, x+3, y+3], DKRED, RED, LIGHTRED, 0.2)
    d.ellipse([18, 16, 32, 26], fill=DKRED)
    d.ellipse([20, 18, 30, 24], fill=DKBROWN)
    d.polygon([(18, 16), (25, 8), (32, 16)], fill=GREEN)
    d.line([(25, 8), (25, 2)], fill=DKGREEN, width=2)

# 8. Ackee
def draw_ackee(d):
    d.ellipse([8, 10, 42, 44], fill=DKRED)
    d.ellipse([10, 12, 40, 42], fill=RED)
    draw_texture(d, [10, 12, 40, 42], LIGHTRED, density=40)
    d.polygon([(25, 20), (16, 42), (34, 42)], fill=YELLOW)
    d.ellipse([14, 26, 26, 38], fill=BEIGE)
    d.ellipse([24, 26, 36, 38], fill=WHITE)
    draw_sphere(d, [18, 20, 26, 28], BLACK, DKGREY, GREY, 0.2)
    draw_sphere(d, [26, 21, 32, 27], BLACK, DKGREY, GREY, 0.2)
    d.line([(25, 10), (25, 4)], fill=DKGREEN, width=3)

# 9. Langsat
def draw_langsat(d):
    d.line([(25, 2), (25, 46)], fill=DKBROWN, width=3)
    coords = [(20,12), (30,16), (16,24), (32,28), (22,34), (34,40), (18,44)]
    for fx, fy in coords:
        draw_sphere(d, [fx-8, fy-8, fx+8, fy+8], DKBROWN, BEIGE, WHITE, 0.3)
        draw_texture(d, [fx-6, fy-6, fx+6, fy+6], DKBROWN, density=5)
        d.ellipse([fx-2, fy-8, fx+2, fy-6], fill=BROWN)

# 10. Santol
def draw_santol(d):
    draw_leaf(d, 28, 8, -20, 16, 8, DKGREEN, GREEN)
    draw_sphere(d, [6, 10, 44, 46], DKBROWN, YELLOW, LIGHTYELLOW, 0.4)
    draw_texture(d, [8, 12, 42, 44], DKYELLOW, density=120)
    draw_texture(d, [8, 12, 42, 44], ORANGE, density=60)
    d.ellipse([20, 10, 30, 14], fill=DKBROWN)
    d.line([(25, 12), (28, 4)], fill=BROWN, width=3)

# 11. Jabuticaba
def draw_jabuticaba(d):
    d.rectangle([0, 0, 50, 50], fill=DKBROWN)
    for i in range(5):
        d.line([(10+i*8, 0), (8+i*8, 50)], fill=BROWN, width=2)
        d.line([(12+i*8, 0), (14+i*8, 50)], fill=BLACK, width=1)
    draw_sphere(d, [10, 10, 40, 40], BLACK, DKPURPLE, LIGHTPURPLE, 0.3)
    draw_sphere(d, [4, 30, 18, 44], BLACK, DKPURPLE, LIGHTPURPLE, 0.3)
    draw_sphere(d, [34, 14, 46, 26], BLACK, DKPURPLE, LIGHTPURPLE, 0.3)
    d.point((22, 18), fill=WHITE)

# 12. Naranjilla
def draw_naranjilla(d):
    draw_sphere(d, [4, 10, 36, 42], DKORANGE, ORANGE, LIGHTORANGE, 0.3)
    draw_texture(d, [4, 10, 36, 42], LIGHTYELLOW, density=150)
    d.ellipse([20, 20, 48, 48], fill=DKGREEN)
    d.ellipse([22, 22, 46, 46], fill=GREEN)
    d.polygon([(34, 22), (22, 34), (34, 46), (46, 34)], fill=LIGHTGREEN)
    d.ellipse([30, 30, 38, 38], fill=GREEN)
    for sx, sy in [(28, 28), (40, 28), (28, 40), (40, 40)]:
        d.ellipse([sx-2, sy-2, sx+2, sy+2], fill=WHITE)

# 13. Cocona
def draw_cocona(d):
    draw_leaf(d, 25, 8, 160, 15, 6, DKGREEN, GREEN)
    draw_sphere(d, [10, 8, 40, 46], DKRED, ORANGE, YELLOW, 0.4)
    draw_texture(d, [12, 10, 38, 44], LIGHTYELLOW, density=40)
    d.polygon([(18, 8), (25, 14), (32, 8), (25, 4)], fill=DKGREEN)
    d.line([(25, 8), (25, 2)], fill=BROWN, width=2)
    d.arc([14, 12, 36, 42], start=180, end=270, fill=LIGHTYELLOW, width=2)

# 14. Pepino
def draw_pepino(d):
    draw_leaf(d, 25, 8, 10, 14, 6, GREEN, LIGHTGREEN)
    draw_sphere(d, [10, 6, 40, 48], DKYELLOW, BEIGE, WHITE, 0.3)
    for i in range(14, 38, 6):
        d.arc([10, 6, 40, 48], start=90+i*2, end=270-i*2, fill=PURPLE, width=2)
        d.arc([10, 6, 40, 48], start=270+i*2, end=90-i*2, fill=DKPURPLE, width=2)
    d.line([(25, 6), (25, 2)], fill=DKGREEN, width=2)

# 15. Tamarillo
def draw_tamarillo(d):
    draw_leaf(d, 25, 10, -10, 16, 8, DKGREEN, GREEN)
    draw_sphere(d, [12, 12, 38, 46], DKRED, RED, LIGHTRED, 0.25)
    draw_texture(d, [14, 14, 36, 44], ORANGE, density=60)
    d.polygon([(20, 12), (25, 16), (30, 12)], fill=DKGREEN)
    d.line([(25, 14), (25, 4)], fill=BROWN, width=2)
    d.ellipse([22, 18, 25, 24], fill=WHITE)

# 16. Canistel
def draw_canistel(d):
    draw_leaf(d, 25, 8, -30, 15, 6, DKGREEN, GREEN)
    d.polygon([(25, 48), (8, 20), (42, 20)], fill=DKORANGE)
    draw_sphere(d, [8, 12, 42, 34], DKORANGE, ORANGE, YELLOW, 0.35)
    d.polygon([(25, 44), (14, 22), (36, 22)], fill=ORANGE)
    d.polygon([(25, 40), (20, 24), (30, 24)], fill=YELLOW)
    d.line([(25, 12), (25, 4)], fill=DKBROWN, width=3)
    d.ellipse([18, 16, 24, 20], fill=WHITE)

# 17. Sapodilla
def draw_sapodilla(d):
    draw_sphere(d, [4, 10, 36, 42], DKBROWN, BROWN, LIGHTBROWN, 0.3)
    draw_texture(d, [4, 10, 36, 42], DKBROWN, density=100)
    d.ellipse([18, 18, 48, 46], fill=DKBROWN)
    d.ellipse([20, 20, 46, 44], fill=BEIGE)
    d.ellipse([28, 26, 38, 38], fill=BEIGE) # inner
    d.ellipse([26, 28, 34, 36], fill=BLACK)
    d.ellipse([27, 29, 30, 32], fill=WHITE)
    draw_texture(d, [20, 20, 46, 44], LIGHTBROWN, density=30)

# 18. Mamey Sapote
def draw_mamey_sapote(d):
    d.polygon([(25, 4), (6, 25), (25, 46), (44, 25)], fill=DKBROWN)
    draw_texture(d, [6, 4, 44, 46], BLACK, density=80)
    d.polygon([(25, 8), (10, 25), (25, 42), (40, 25)], fill=ORANGE)
    d.polygon([(25, 12), (16, 25), (25, 38), (34, 25)], fill=LIGHTORANGE)
    d.ellipse([20, 18, 30, 32], fill=BLACK)
    d.ellipse([22, 20, 28, 30], fill=DKBROWN)
    d.ellipse([23, 21, 26, 24], fill=WHITE)

# 19. Black Sapote
def draw_black_sapote(d):
    draw_sphere(d, [4, 10, 38, 44], DKGREEN, GREEN, LIGHTGREEN, 0.3)
    d.ellipse([18, 18, 46, 46], fill=DKGREEN)
    d.ellipse([20, 20, 44, 44], fill=DKBROWN)
    draw_texture(d, [20, 20, 44, 44], BLACK, density=100, size=2)
    d.ellipse([14, 8, 28, 14], fill=DKGREEN)
    d.polygon([(14, 11), (21, 4), (28, 11)], fill=GREEN)
    d.ellipse([28, 28, 36, 36], fill=BLACK)

# 20. White Sapote
def draw_white_sapote(d):
    draw_leaf(d, 25, 10, -45, 18, 8, DKGREEN, GREEN)
    draw_sphere(d, [10, 10, 40, 44], DKGREEN, GREEN, LIGHTGREEN, 0.3)
    draw_texture(d, [12, 12, 38, 42], WHITE, density=40)
    d.ellipse([16, 14, 24, 22], fill=WHITE)
    d.line([(25, 10), (25, 4)], fill=BROWN, width=2)
    d.arc([14, 14, 36, 40], start=180, end=270, fill=WHITE, width=2)

# 21. Cherimoya
def draw_cherimoya(d):
    draw_leaf(d, 25, 8, 10, 16, 8, DKGREEN, GREEN)
    d.polygon([(25, 46), (8, 20), (42, 20)], fill=DKGREEN)
    d.ellipse([8, 10, 42, 30], fill=DKGREEN)
    d.polygon([(25, 42), (12, 22), (38, 22)], fill=GREEN)
    d.ellipse([12, 12, 38, 28], fill=GREEN)
    for y in range(16, 40, 6):
        for x in range(12, 38, 6):
            if ((x-25)**2)/150 + ((y-25)**2)/100 <= 1:
                d.arc([x-4, y-4, x+4, y+4], start=0, end=180, fill=LIGHTGREEN, width=2)
                d.arc([x-4, y-4, x+4, y+4], start=180, end=360, fill=DKGREEN, width=1)
    d.line([(25, 12), (25, 4)], fill=DKBROWN, width=3)

# 22. Monstera Deliciosa
def draw_monstera_deliciosa(d):
    d.polygon([(25, 48), (16, 12), (34, 12)], fill=DKGREEN)
    d.rounded_rectangle([16, 10, 34, 44], radius=4, fill=GREEN)
    d.polygon([(25, 44), (20, 14), (30, 14)], fill=LIGHTGREEN)
    for y in range(14, 42, 5):
        for x in [18, 23, 28]:
            d.polygon([(x, y), (x+4, y), (x+2, y+3)], fill=DKGREEN)
            d.point((x+2, y+1), fill=LIGHTGREEN)
    d.line([(25, 10), (25, 2)], fill=BROWN, width=4)

# 23. Prickly Pear
def draw_prickly_pear(d):
    draw_sphere(d, [12, 10, 38, 46], DKPURPLE, PURPLE, LIGHTPURPLE, 0.3)
    for sx, sy in [(18, 16), (32, 18), (25, 24), (16, 30), (34, 30), (20, 38), (30, 38)]:
        d.ellipse([sx-2, sy-2, sx+2, sy+2], fill=YELLOW)
        d.point((sx, sy), fill=DKBROWN)
        for dx, dy in [(-2,-2), (2,-2), (-2,2), (2,2)]:
            d.line([(sx, sy), (sx+dx, sy+dy)], fill=LIGHTYELLOW, width=1)
    d.ellipse([20, 10, 30, 14], fill=DKGREEN)

# 24. Pitanga
def draw_pitanga(d):
    draw_leaf(d, 25, 12, -45, 14, 6, DKGREEN, GREEN)
    d.ellipse([8, 14, 42, 44], fill=DKRED)
    for rx, rw in [(10, 12), (18, 14), (26, 12), (34, 8)]:
        d.ellipse([rx, 14, rx+rw, 44], fill=RED)
        d.ellipse([rx+2, 16, rx+rw-2, 42], fill=LIGHTRED)
        d.line([(rx+rw/2, 18), (rx+rw/2, 38)], fill=WHITE, width=1)
    d.line([(25, 14), (25, 4)], fill=DKGREEN, width=2)

# 25. Rose Apple
def draw_rose_apple(d):
    draw_leaf(d, 25, 10, 20, 18, 7, DKGREEN, GREEN)
    d.polygon([(25, 10), (8, 40), (42, 40)], fill=DKRED)
    d.ellipse([8, 30, 42, 46], fill=DKRED)
    d.polygon([(25, 14), (12, 38), (38, 38)], fill=RED)
    d.ellipse([12, 32, 38, 44], fill=RED)
    draw_texture(d, [10, 14, 40, 44], LIGHTRED, density=60)
    d.ellipse([16, 24, 22, 34], fill=WHITE)
    d.ellipse([20, 40, 30, 44], fill=DKGREEN)
    d.line([(25, 10), (25, 4)], fill=DKBROWN, width=2)

# 26. Jambolan
def draw_jambolan(d):
    draw_leaf(d, 25, 8, -25, 16, 6, GREEN, LIGHTGREEN)
    draw_sphere(d, [12, 8, 38, 46], BLACK, DKPURPLE, LIGHTPURPLE, 0.25)
    d.ellipse([16, 14, 22, 30], fill=WHITE)
    d.arc([14, 10, 36, 44], start=180, end=270, fill=LIGHTPURPLE, width=2)
    d.line([(25, 8), (25, 2)], fill=BROWN, width=2)
    draw_texture(d, [14, 10, 36, 44], DARKBLUE, density=40)

# 27. Bignay
def draw_bignay(d):
    d.line([(25, 2), (25, 40)], fill=DKGREEN, width=2)
    berries = [
        (22, 10, GREEN, LIGHTGREEN), (28, 14, RED, LIGHTRED), (18, 18, DKRED, RED),
        (32, 20, BLACK, DKPURPLE), (22, 26, BLACK, DKPURPLE), (28, 30, RED, LIGHTRED),
        (16, 32, GREEN, LIGHTGREEN), (30, 36, DKRED, RED), (22, 40, BLACK, DKPURPLE),
        (26, 44, RED, LIGHTRED)
    ]
    for bx, by, c1, c2 in berries:
        draw_sphere(d, [bx-5, by-5, bx+5, by+5], BLACK, c1, c2, 0.2)
        d.point((bx-1, by-1), fill=WHITE)
        d.line([(25, by-4), (bx, by)], fill=DKGREEN, width=1)

# 28. Ambarella
def draw_ambarella(d):
    draw_leaf(d, 25, 8, 150, 16, 8, DKGREEN, GREEN)
    draw_sphere(d, [10, 8, 40, 46], DKGREEN, YELLOW, LIGHTYELLOW, 0.3)
    draw_texture(d, [12, 10, 38, 44], ORANGE, density=50)
    draw_texture(d, [12, 10, 38, 44], DKGREEN, density=30)
    d.line([(25, 10), (28, 2)], fill=DKBROWN, width=3)
    d.ellipse([18, 14, 26, 20], fill=WHITE)

# 29. Calamondin
def draw_calamondin(d):
    draw_leaf(d, 25, 14, -30, 14, 6, DKGREEN, GREEN)
    draw_sphere(d, [10, 12, 40, 42], DKGREEN, ORANGE, LIGHTORANGE, 0.35)
    draw_texture(d, [12, 14, 38, 40], DKORANGE, density=80)
    draw_texture(d, [12, 14, 38, 40], YELLOW, density=40)
    d.ellipse([16, 18, 22, 24], fill=WHITE)
    d.line([(25, 12), (25, 6)], fill=DKBROWN, width=2)

# 30. Sudachi
def draw_sudachi(d):
    draw_leaf(d, 25, 10, 30, 15, 7, GREEN, LIGHTGREEN)
    draw_sphere(d, [10, 10, 40, 40], BLACK, DKGREEN, GREEN, 0.3)
    draw_texture(d, [12, 12, 38, 38], LIGHTGREEN, density=100)
    draw_texture(d, [12, 12, 38, 38], DKGREEN, density=60, size=2)
    d.ellipse([18, 16, 24, 20], fill=WHITE)
    d.line([(25, 10), (25, 4)], fill=BROWN, width=2)

# 31. Kabosu
def draw_kabosu(d):
    draw_leaf(d, 25, 10, 160, 18, 8, DKGREEN, GREEN)
    draw_sphere(d, [8, 8, 42, 42], DKGREEN, GREEN, YELLOW, 0.4)
    draw_texture(d, [10, 10, 40, 40], DKYELLOW, density=120)
    d.ellipse([14, 14, 22, 20], fill=WHITE)
    d.ellipse([20, 8, 30, 12], fill=DKBROWN)
    d.line([(25, 10), (25, 2)], fill=BROWN, width=3)

# 32. Finger Lime
def draw_finger_lime(d):
    d.polygon([(10, 12), (38, 18), (40, 24), (12, 18)], fill=DKBROWN)
    d.polygon([(12, 14), (36, 19), (38, 23), (14, 18)], fill=BROWN)
    d.polygon([(8, 28), (42, 34), (44, 40), (10, 34)], fill=DKBROWN)
    d.polygon([(10, 30), (40, 35), (42, 39), (12, 34)], fill=BROWN)
    for y in range(16, 36, 4):
        for x in range(12, 42, 4):
            if 18 <= y <= 32:
                d.ellipse([x-3, y-3, x+3, y+3], fill=LIGHTGREEN)
                d.ellipse([x-2, y-2, x+2, y+2], fill=GREEN)
                d.point((x, y), fill=WHITE)

# 33. Citron
def draw_citron(d):
    draw_leaf(d, 25, 10, -10, 18, 8, DKGREEN, GREEN)
    draw_sphere(d, [6, 10, 44, 44], DKYELLOW, YELLOW, LIGHTYELLOW, 0.3)
    for bx, by in [(16, 18), (30, 20), (20, 30), (34, 32), (12, 26), (26, 38), (38, 26)]:
        draw_sphere(d, [bx-6, by-6, bx+6, by+6], DKYELLOW, YELLOW, LIGHTYELLOW, 0.3)
        d.arc([bx-6, by-6, bx+6, by+6], start=0, end=180, fill=DKORANGE, width=1)
    draw_texture(d, [8, 12, 42, 42], DKYELLOW, density=80)
    d.line([(25, 10), (25, 2)], fill=BROWN, width=3)

# 34. Ponderosa Lemon
def draw_ponderosa_lemon(d):
    draw_leaf(d, 25, 12, 25, 20, 10, DKGREEN, GREEN)
    draw_sphere(d, [6, 10, 44, 46], DKORANGE, YELLOW, LIGHTYELLOW, 0.35)
    draw_texture(d, [8, 12, 42, 44], DKYELLOW, density=150)
    d.ellipse([14, 16, 24, 24], fill=WHITE)
    d.polygon([(20, 10), (25, 46), (30, 10)], fill=YELLOW)
    d.line([(25, 10), (25, 2)], fill=DKGREEN, width=4)

# 35. Bergamot
def draw_bergamot(d):
    draw_leaf(d, 25, 8, -45, 16, 8, DKGREEN, GREEN)
    d.polygon([(25, 10), (8, 30), (42, 30)], fill=DKGREEN)
    d.ellipse([8, 20, 42, 44], fill=DKGREEN)
    d.polygon([(25, 12), (10, 30), (40, 30)], fill=GREEN)
    d.ellipse([10, 22, 40, 42], fill=GREEN)
    draw_texture(d, [10, 14, 40, 42], LIGHTGREEN, density=100)
    for bx, by in [(25, 18), (16, 28), (34, 28), (25, 36), (18, 36), (32, 36)]:
        d.ellipse([bx-3, by-3, bx+3, by+3], fill=LIGHTGREEN)
        d.arc([bx-4, by-4, bx+4, by+4], start=0, end=180, fill=DKGREEN, width=1)
    d.line([(25, 10), (25, 2)], fill=BROWN, width=3)

# 36. Jujube
def draw_jujube(d):
    draw_leaf(d, 25, 8, 10, 14, 5, GREEN, LIGHTGREEN)
    draw_sphere(d, [12, 8, 38, 46], BLACK, DKBROWN, BROWN, 0.3)
    for y in range(12, 42, 4):
        d.line([(16, y), (34, y+random.randint(-2, 2))], fill=DKBROWN, width=1)
        d.line([(18, y+1), (32, y+1+random.randint(-2, 2))], fill=BLACK, width=1)
    d.ellipse([18, 14, 22, 28], fill=LIGHTBROWN)
    d.line([(25, 8), (25, 2)], fill=BROWN, width=2)

# 37. Hawthorn
def draw_hawthorn(d):
    draw_leaf(d, 25, 14, -20, 12, 6, DKGREEN, GREEN)
    draw_sphere(d, [10, 12, 40, 40], DKRED, RED, LIGHTRED, 0.3)
    draw_texture(d, [12, 14, 38, 38], DKBROWN, density=30)
    d.polygon([(20, 38), (25, 46), (30, 38)], fill=DKBROWN)
    d.polygon([(16, 36), (25, 44), (22, 36)], fill=BLACK)
    d.polygon([(34, 36), (25, 44), (28, 36)], fill=BLACK)
    d.ellipse([16, 18, 22, 24], fill=WHITE)
    d.line([(25, 12), (25, 4)], fill=DKBROWN, width=2)

# 38. Crabapple
def draw_crabapple(d):
    d.line([(25, 2), (18, 26)], fill=DKBROWN, width=2)
    d.line([(25, 2), (32, 20)], fill=DKBROWN, width=2)
    for ax, ay in [(18, 30), (32, 24)]:
        draw_leaf(d, ax, ay-8, 180, 10, 4, DKGREEN, GREEN)
        draw_sphere(d, [ax-9, ay-9, ax+9, ay+9], DKRED, RED, YELLOW, 0.3)
        draw_texture(d, [ax-7, ay-7, ax+7, ay+7], DKBROWN, density=20)
        d.ellipse([ax-3, ay-5, ax+1, ay-1], fill=WHITE)
        d.polygon([(ax-2, ay+8), (ax, ay+12), (ax+2, ay+8)], fill=BLACK)

# 39. Salal Berry
def draw_salal_berry(d):
    draw_leaf(d, 25, 10, 150, 16, 8, GREEN, LIGHTGREEN)
    d.polygon([(25, 42), (10, 16), (40, 16)], fill=BLACK)
    d.ellipse([8, 12, 42, 30], fill=BLACK)
    d.polygon([(25, 40), (12, 18), (38, 18)], fill=DARKBLUE)
    d.ellipse([10, 14, 40, 28], fill=DARKBLUE)
    draw_sphere(d, [15, 16, 35, 26], DARKBLUE, MIDBLUE, LIGHTBLUE, 0.2)
    d.polygon([(15, 12), (25, 4), (35, 12)], fill=DKGREEN)
    d.polygon([(10, 16), (25, 8), (20, 16)], fill=GREEN)
    d.polygon([(40, 16), (25, 8), (30, 16)], fill=GREEN)
    d.line([(25, 8), (25, 2)], fill=DKBROWN, width=2)

# 40. Serviceberry
def draw_serviceberry(d):
    draw_leaf(d, 25, 12, -30, 14, 6, DKGREEN, GREEN)
    draw_sphere(d, [8, 10, 42, 42], BLACK, DKPURPLE, MIDBLUE, 0.3)
    draw_texture(d, [10, 12, 40, 40], LIGHTBLUE, density=60)
    d.polygon([(18, 40), (25, 48), (32, 40)], fill=BLACK)
    d.polygon([(14, 38), (25, 46), (22, 38)], fill=DKPURPLE)
    d.polygon([(36, 38), (25, 46), (28, 38)], fill=DKPURPLE)
    d.ellipse([16, 16, 22, 22], fill=WHITE)
    d.line([(25, 10), (25, 4)], fill=BROWN, width=2)

# 41. Chokeberry
def draw_chokeberry(d):
    draw_leaf(d, 25, 12, 20, 15, 7, DKGREEN, GREEN)
    draw_sphere(d, [8, 10, 42, 42], BLACK, DKGREY, GREY, 0.3)
    draw_texture(d, [10, 12, 40, 40], WHITE, density=20)
    d.ellipse([16, 16, 24, 24], fill=WHITE)
    d.ellipse([20, 40, 30, 44], fill=DKRED)
    d.line([(25, 12), (25, 4)], fill=DKRED, width=3)

# 42. Dewberry
def draw_dewberry(d):
    draw_leaf(d, 25, 14, 160, 16, 10, DKGREEN, GREEN)
    d.ellipse([6, 14, 44, 42], fill=BLACK)
    druplets = [(25,38), (18,34), (32,34), (12,28), (25,28), (38,28), (18,22), (32,22), (25,18)]
    for dx, dy in druplets:
        draw_sphere(d, [dx-6, dy-6, dx+6, dy+6], BLACK, DARKBLUE, MIDBLUE, 0.2)
        d.point((dx-2, dy-2), fill=LIGHTBLUE)
    d.polygon([(15, 18), (25, 10), (35, 18)], fill=DKGREEN)
    d.line([(25, 10), (25, 4)], fill=BROWN, width=2)

# 43. Tayberry
def draw_tayberry(d):
    draw_leaf(d, 25, 10, -10, 15, 8, GREEN, LIGHTGREEN)
    d.rounded_rectangle([12, 10, 38, 46], radius=6, fill=BLACK)
    for y in range(14, 44, 6):
        for x in [16, 22, 28, 34]:
            if ((x-25)**2)/120 + ((y-28)**2)/200 <= 1:
                draw_sphere(d, [x-4, y-4, x+4, y+4], BLACK, DKPURPLE, RED, 0.2)
                d.point((x-1, y-1), fill=LIGHTRED)
    d.polygon([(18, 12), (25, 6), (32, 12)], fill=DKGREEN)
    d.line([(25, 6), (25, 2)], fill=GREEN, width=2)

# 44. Loganberry
def draw_loganberry(d):
    draw_leaf(d, 25, 10, 10, 15, 8, DKGREEN, GREEN)
    d.rounded_rectangle([14, 10, 36, 46], radius=8, fill=DKRED)
    for y in range(14, 44, 6):
        for x in [18, 24, 30]:
            if ((x-25)**2)/100 + ((y-28)**2)/220 <= 1:
                draw_sphere(d, [x-4, y-4, x+4, y+4], DKRED, RED, LIGHTRED, 0.2)
                d.point((x-1, y-1), fill=WHITE)
    d.polygon([(18, 12), (25, 6), (32, 12)], fill=GREEN)
    d.line([(25, 6), (25, 2)], fill=BROWN, width=2)

# 45. White Mulberry
def draw_mulberry_white(d):
    draw_leaf(d, 25, 10, 170, 15, 8, GREEN, LIGHTGREEN)
    d.rounded_rectangle([14, 10, 36, 46], radius=6, fill=DKBROWN)
    for y in range(14, 44, 5):
        for x in [18, 23, 28, 33]:
            if ((x-25)**2)/100 + ((y-28)**2)/220 <= 1:
                draw_sphere(d, [x-3, y-3, x+3, y+3], DKBROWN, BEIGE, WHITE, 0.2)
                d.point((x, y), fill=LIGHTYELLOW)
    d.polygon([(20, 12), (25, 6), (30, 12)], fill=DKGREEN)
    d.line([(25, 6), (25, 2)], fill=GREEN, width=2)

# 46. Ice Cream Bean
def draw_ice_cream_bean(d):
    draw_leaf(d, 12, 38, -45, 18, 6, DKGREEN, GREEN)
    d.polygon([(6, 46), (40, 12), (46, 18), (12, 50)], fill=DKGREEN)
    d.polygon([(8, 44), (38, 14), (42, 18), (12, 46)], fill=GREEN)
    d.line([(6, 46), (40, 12)], fill=DKBROWN, width=2)
    for i in range(15, 40, 6):
        d.line([(i, 56-i), (i+6, 56-i-6)], fill=DKGREEN, width=2)
    d.ellipse([18, 22, 34, 34], fill=DKBROWN)
    d.ellipse([20, 24, 32, 32], fill=WHITE)
    draw_texture(d, [20, 24, 32, 32], BEIGE, density=30)
    d.ellipse([24, 26, 28, 30], fill=BLACK)

# 47. Marula
def draw_marula(d):
    draw_leaf(d, 25, 10, -25, 16, 7, DKGREEN, GREEN)
    draw_sphere(d, [10, 8, 40, 46], DKBROWN, DKYELLOW, YELLOW, 0.3)
    draw_texture(d, [12, 10, 38, 44], LIGHTYELLOW, density=80)
    draw_texture(d, [12, 10, 38, 44], DKBROWN, density=40)
    d.ellipse([16, 16, 22, 22], fill=WHITE)
    d.line([(25, 10), (25, 4)], fill=BROWN, width=3)

# 48. Baobab Fruit
def draw_baobab_fruit(d):
    draw_leaf(d, 25, 8, 10, 18, 8, DKGREEN, GREEN)
    draw_sphere(d, [6, 10, 44, 44], BLACK, DKGREEN, DKBROWN, 0.4)
    draw_texture(d, [8, 12, 42, 42], GREEN, density=200)
    for i in range(15, 35, 5):
        d.arc([8, 12, 42, 42], start=i*10, end=i*10+45, fill=DKBROWN, width=2)
    d.line([(25, 10), (25, 2)], fill=DKBROWN, width=4)

# 49. Cupuacu
def draw_cupuacu(d):
    draw_leaf(d, 25, 10, 150, 20, 10, DKGREEN, GREEN)
    draw_sphere(d, [6, 14, 44, 40], BLACK, DKBROWN, BROWN, 0.35)
    draw_texture(d, [8, 16, 42, 38], LIGHTBROWN, density=300)
    for i in range(18, 36, 4):
        d.line([(10, i), (40, i)], fill=DKBROWN, width=1)
    d.ellipse([16, 20, 24, 26], fill=LIGHTBROWN)
    d.line([(25, 14), (25, 4)], fill=DKBROWN, width=4)

# 50. Bacuri
def draw_bacuri(d):
    draw_leaf(d, 25, 8, -10, 18, 8, DKGREEN, GREEN)
    draw_sphere(d, [8, 8, 42, 46], DKBROWN, DKYELLOW, YELLOW, 0.3)
    draw_texture(d, [10, 10, 40, 44], DKBROWN, density=80)
    d.ellipse([20, 20, 44, 44], fill=BROWN)
    d.ellipse([22, 22, 42, 42], fill=BEIGE)
    draw_texture(d, [22, 22, 42, 42], WHITE, density=60)
    d.ellipse([28, 28, 36, 36], fill=DKBROWN)
    d.line([(25, 8), (25, 2)], fill=BROWN, width=3)

fruits = [
    ("damson", draw_damson),
    ("honeyberry", draw_honeyberry),
    ("acai", draw_acai),
    ("goji_berry", draw_goji_berry),
    ("seabuckthorn", draw_seabuckthorn),
    ("salmonberry", draw_salmonberry),
    ("thimbleberry", draw_thimbleberry),
    ("ackee", draw_ackee),
    ("langsat", draw_langsat),
    ("santol", draw_santol),
    ("jabuticaba", draw_jabuticaba),
    ("naranjilla", draw_naranjilla),
    ("cocona", draw_cocona),
    ("pepino", draw_pepino),
    ("tamarillo", draw_tamarillo),
    ("canistel", draw_canistel),
    ("sapodilla", draw_sapodilla),
    ("mamey_sapote", draw_mamey_sapote),
    ("black_sapote", draw_black_sapote),
    ("white_sapote", draw_white_sapote),
    ("cherimoya", draw_cherimoya),
    ("monstera_deliciosa", draw_monstera_deliciosa),
    ("prickly_pear", draw_prickly_pear),
    ("pitanga", draw_pitanga),
    ("rose_apple", draw_rose_apple),
    ("jambolan", draw_jambolan),
    ("bignay", draw_bignay),
    ("ambarella", draw_ambarella),
    ("calamondin", draw_calamondin),
    ("sudachi", draw_sudachi),
    ("kabosu", draw_kabosu),
    ("finger_lime", draw_finger_lime),
    ("citron", draw_citron),
    ("ponderosa_lemon", draw_ponderosa_lemon),
    ("bergamot", draw_bergamot),
    ("jujube", draw_jujube),
    ("hawthorn", draw_hawthorn),
    ("crabapple", draw_crabapple),
    ("salal_berry", draw_salal_berry),
    ("serviceberry", draw_serviceberry),
    ("chokeberry", draw_chokeberry),
    ("dewberry", draw_dewberry),
    ("tayberry", draw_tayberry),
    ("loganberry", draw_loganberry),
    ("mulberry_white", draw_mulberry_white),
    ("ice_cream_bean", draw_ice_cream_bean),
    ("marula", draw_marula),
    ("baobab_fruit", draw_baobab_fruit),
    ("cupuacu", draw_cupuacu),
    ("bacuri", draw_bacuri)
]

def main():
    print(f"Generating {len(fruits)} hyper-detailed fruit sprites in '{OUTPUT_DIR}'...")
    for name, func in fruits:
        create_sprite(name, func)
    print("\\nAll 50 new fruit sprites generated successfully!")

if __name__ == "__main__":
    main()
