import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img.save(filename)
    print(f"Generated {filename}")

def draw_emu(draw):
    # Legs (grey-brown)
    draw.line([(20, 35), (20, 48)], fill=(139, 137, 137, 255), width=2)
    draw.line([(28, 35), (28, 48)], fill=(139, 137, 137, 255), width=2)
    # Body (shaggy grey-brown)
    draw.ellipse([10, 20, 35, 40], fill=(101, 80, 70, 255))
    draw.ellipse([8, 25, 30, 42], fill=(80, 60, 50, 255)) # some texture
    # Neck
    draw.line([(32, 25), (38, 10)], fill=(139, 137, 137, 255), width=3)
    # Head
    draw.ellipse([34, 5, 42, 15], fill=(101, 80, 70, 255))
    # Beak
    draw.polygon([(42, 8), (48, 11), (42, 12)], fill=(50, 50, 50, 255))
    # Eye
    draw.rectangle([38, 8, 40, 10], fill=(0,0,0,255))

def draw_pelican(draw):
    # Legs
    draw.line([(20, 42), (20, 48)], fill=(255, 140, 0, 255), width=2)
    draw.line([(28, 42), (28, 48)], fill=(255, 140, 0, 255), width=2)
    # Body
    draw.ellipse([10, 25, 35, 42], fill=(240, 240, 240, 255))
    # Neck
    draw.line([(32, 30), (32, 15)], fill=(240, 240, 240, 255), width=4)
    # Head
    draw.ellipse([25, 10, 35, 20], fill=(240, 240, 240, 255))
    # Bill (top)
    draw.polygon([(34, 12), (48, 14), (34, 15)], fill=(255, 200, 0, 255))
    # Pouch
    draw.polygon([(32, 15), (48, 14), (40, 25)], fill=(255, 165, 0, 255))
    # Eye
    draw.rectangle([31, 13, 33, 15], fill=(0,0,0,255))

def draw_panther(draw):
    # Body
    draw.ellipse([8, 25, 38, 40], fill=(30, 30, 30, 255))
    # Head
    draw.ellipse([32, 18, 45, 32], fill=(30, 30, 30, 255))
    # Snout
    draw.ellipse([40, 25, 48, 32], fill=(30, 30, 30, 255))
    # Ears
    draw.polygon([(34, 18), (36, 12), (39, 18)], fill=(30, 30, 30, 255))
    draw.polygon([(40, 18), (42, 14), (44, 18)], fill=(30, 30, 30, 255))
    # Tail
    draw.arc([5, 15, 20, 35], 90, 270, fill=(30, 30, 30, 255), width=3)
    # Eye (glowing yellow)
    draw.rectangle([38, 22, 40, 24], fill=(255,255,0,255))
    # Legs (4 of them for depth)
    draw.rectangle([12, 38, 15, 48], fill=(15, 15, 15, 255)) # back
    draw.rectangle([18, 38, 21, 48], fill=(30, 30, 30, 255)) # front
    draw.rectangle([30, 38, 33, 48], fill=(15, 15, 15, 255)) # back
    draw.rectangle([36, 38, 39, 48], fill=(30, 30, 30, 255)) # front

def draw_leopard(draw):
    # Body
    draw.ellipse([8, 25, 38, 40], fill=(230, 160, 40, 255))
    # Spots on body
    spots = [(12, 28), (16, 32), (20, 27), (24, 33), (28, 29), (32, 34), (18, 30), (26, 30)]
    for sx, sy in spots:
        draw.ellipse([sx, sy, sx+2, sy+2], fill=(20, 20, 20, 255))
    # Head
    draw.ellipse([32, 18, 45, 32], fill=(230, 160, 40, 255))
    # Spots on head
    draw.ellipse([34, 21, 36, 23], fill=(20, 20, 20, 255))
    draw.ellipse([38, 26, 40, 28], fill=(20, 20, 20, 255))
    # Snout
    draw.ellipse([40, 25, 48, 32], fill=(230, 160, 40, 255))
    # Ears
    draw.polygon([(34, 18), (36, 12), (39, 18)], fill=(230, 160, 40, 255))
    draw.polygon([(40, 18), (42, 14), (44, 18)], fill=(230, 160, 40, 255))
    # Tail (golden with spots/rings)
    draw.arc([5, 15, 20, 35], 90, 270, fill=(230, 160, 40, 255), width=3)
    draw.point((8, 20), fill=(20, 20, 20, 255))
    draw.point((6, 25), fill=(20, 20, 20, 255))
    draw.point((8, 30), fill=(20, 20, 20, 255))
    # Eye (glowing yellow)
    draw.rectangle([38, 22, 40, 24], fill=(255,255,0,255))
    # Legs (4 of them for depth)
    draw.rectangle([12, 38, 15, 48], fill=(180, 120, 25, 255)) # back
    draw.rectangle([18, 38, 21, 48], fill=(230, 160, 40, 255)) # front
    draw.rectangle([30, 38, 33, 48], fill=(180, 120, 25, 255)) # back
    draw.rectangle([36, 38, 39, 48], fill=(230, 160, 40, 255)) # front

def draw_ostrich(draw):
    # Legs
    draw.line([(22, 32), (22, 48)], fill=(255, 182, 193, 255), width=2)
    draw.line([(30, 32), (30, 48)], fill=(255, 182, 193, 255), width=2)
    # Body
    draw.ellipse([10, 18, 38, 35], fill=(20, 20, 20, 255))
    # White tail feathers
    draw.ellipse([5, 20, 15, 30], fill=(240, 240, 240, 255))
    # Neck
    draw.line([(35, 25), (42, 8)], fill=(255, 182, 193, 255), width=3)
    # Head
    draw.ellipse([38, 2, 46, 10], fill=(255, 182, 193, 255))
    # Beak
    draw.polygon([(46, 5), (50, 7), (46, 9)], fill=(200, 150, 100, 255))
    # Eye
    draw.rectangle([42, 4, 44, 6], fill=(0,0,0,255))

def draw_lemur(draw):
    # Body (seated)
    draw.ellipse([15, 25, 35, 45], fill=(150, 150, 150, 255))
    # Belly (lighter)
    draw.ellipse([25, 30, 35, 45], fill=(200, 200, 200, 255))
    # Head
    draw.ellipse([28, 15, 40, 28], fill=(150, 150, 150, 255))
    # Mask
    draw.ellipse([32, 18, 40, 25], fill=(50, 50, 50, 255))
    # Ears
    draw.polygon([(30, 15), (32, 10), (35, 15)], fill=(150, 150, 150, 255))
    # Eye (big yellow)
    draw.ellipse([34, 19, 38, 23], fill=(255, 255, 0, 255))
    draw.point((36, 21), fill=(0,0,0,255))
    # Tail (thick arc with stripes)
    for i in range(10):
        color = (20, 20, 20, 255) if i % 2 == 0 else (200, 200, 200, 255)
        # We simulate an upright curved tail with overlapping circles
        y = 40 - (i * 3)
        x = 10 + (abs(5 - i) * 1)
        draw.ellipse([x, y, x+8, y+8], fill=color)

def draw_gorilla(draw):
    # Body (hunched, large)
    draw.ellipse([10, 20, 38, 45], fill=(20, 20, 20, 255))
    # Back/Silverback
    draw.ellipse([12, 22, 28, 38], fill=(100, 100, 100, 255))
    # Head (tall brow)
    draw.ellipse([25, 10, 40, 25], fill=(20, 20, 20, 255))
    # Face
    draw.ellipse([32, 15, 40, 25], fill=(40, 40, 40, 255))
    # Arms (walking on knuckles)
    draw.rectangle([30, 25, 36, 48], fill=(20, 20, 20, 255))
    # Legs (short)
    draw.rectangle([15, 35, 22, 48], fill=(20, 20, 20, 255))
    # Eye
    draw.rectangle([35, 17, 37, 19], fill=(0,0,0,255))

def draw_chameleon(draw):
    # Branch
    draw.rectangle([0, 45, 50, 50], fill=(101, 67, 33, 255))
    # Body
    draw.ellipse([15, 25, 35, 40], fill=(0, 200, 150, 255))
    # Head
    draw.ellipse([32, 20, 45, 32], fill=(0, 200, 150, 255))
    # Casque (head bump)
    draw.polygon([(32, 22), (38, 12), (45, 22)], fill=(0, 200, 150, 255))
    # Eye (large)
    draw.ellipse([36, 22, 42, 28], fill=(200, 255, 200, 255))
    draw.point((39, 25), fill=(0,0,0,255))
    # Tail (spiral)
    draw.arc([5, 25, 20, 40], 0, 270, fill=(0, 200, 150, 255), width=3)
    # Legs
    draw.rectangle([20, 38, 23, 45], fill=(0, 150, 100, 255))
    draw.rectangle([30, 38, 33, 45], fill=(0, 150, 100, 255))

def draw_alligator(draw):
    # Similar to crocodile but darker and wider snout
    # Body
    draw.ellipse([5, 35, 35, 45], fill=(30, 70, 30, 255))
    # Snout (wider/blockier)
    draw.rectangle([30, 38, 48, 45], fill=(30, 70, 30, 255))
    # Head bump
    draw.ellipse([28, 33, 38, 45], fill=(30, 70, 30, 255))
    # Tail
    draw.polygon([(10, 40), (0, 48), (5, 45)], fill=(30, 70, 30, 255))
    # Scales
    for x in range(10, 30, 4):
        draw.polygon([(x, 35), (x+2, 33), (x+4, 35)], fill=(10, 40, 10, 255))
    # Eye
    draw.rectangle([32, 35, 34, 37], fill=(0,0,0,255))
    # Legs
    draw.rectangle([10, 43, 13, 48], fill=(10, 40, 10, 255))
    draw.rectangle([25, 43, 28, 48], fill=(10, 40, 10, 255))

animals_to_fix = [
    ("emu_50x50.png", draw_emu),
    ("pelican_50x50.png", draw_pelican),
    ("panther_50x50.png", draw_panther),
    ("leopard_50x50.png", draw_leopard),
    ("ostrich_50x50.png", draw_ostrich),
    ("lemur_50x50.png", draw_lemur),
    ("gorilla_50x50.png", draw_gorilla),
    ("chameleon_50x50.png", draw_chameleon),
    ("alligator_50x50.png", draw_alligator)
]

for filename, func in animals_to_fix:
    create_sprite(filename, func)
