import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    target = f"images/animals/{filename}" if not filename.startswith("images/animals/") else filename
    img.save(target)
    print(f"Generated {target}")

def draw_walrus(draw):
    # Brown body
    draw.ellipse([5, 20, 40, 45], fill=(139, 69, 19, 255))
    # Head
    draw.ellipse([30, 15, 48, 35], fill=(139, 69, 19, 255))
    # Snout
    draw.ellipse([40, 25, 50, 35], fill=(160, 82, 45, 255))
    # Tusks
    draw.polygon([(42, 32), (44, 32), (43, 45)], fill=(255, 255, 255, 255))
    draw.polygon([(46, 32), (48, 32), (47, 42)], fill=(255, 255, 255, 255))
    # Eye
    draw.rectangle([38, 22, 40, 24], fill=(0,0,0,255))
    # Flippers
    draw.ellipse([15, 40, 30, 48], fill=(101, 67, 33, 255))

def draw_sloth(draw):
    # Branch
    draw.rectangle([0, 10, 50, 15], fill=(101, 67, 33, 255))
    # Body hanging
    draw.ellipse([15, 15, 35, 38], fill=(160, 140, 110, 255))
    # Head
    draw.ellipse([30, 15, 45, 30], fill=(180, 160, 130, 255))
    # Face mask
    draw.ellipse([35, 18, 43, 26], fill=(220, 200, 180, 255))
    # Eye
    draw.rectangle([38, 20, 40, 22], fill=(0,0,0,255))
    # Arms holding branch
    draw.line([(32, 20), (35, 12)], fill=(160, 140, 110, 255), width=4)
    draw.line([(20, 30), (25, 12)], fill=(160, 140, 110, 255), width=4)

def draw_iguana(draw):
    # Body
    draw.ellipse([10, 30, 35, 42], fill=(34, 139, 34, 255))
    # Head
    draw.ellipse([30, 22, 45, 35], fill=(34, 139, 34, 255))
    # Tail
    draw.polygon([(15, 36), (0, 45), (10, 42)], fill=(34, 139, 34, 255))
    # Spines
    for x in range(15, 35, 5):
        draw.polygon([(x, 30), (x+2, 22), (x+4, 30)], fill=(0, 100, 0, 255))
    # Eye
    draw.rectangle([38, 26, 40, 28], fill=(0,0,0,255))
    # Legs
    draw.rectangle([15, 40, 18, 48], fill=(0, 100, 0, 255))
    draw.rectangle([25, 40, 28, 48], fill=(0, 100, 0, 255))

def draw_flamingo(draw):
    # Legs
    draw.line([(22, 35), (22, 48)], fill=(255, 105, 180, 255), width=2)
    draw.line([(28, 35), (28, 48)], fill=(255, 105, 180, 255), width=2)
    # Body
    draw.ellipse([10, 20, 35, 35], fill=(255, 182, 193, 255))
    # Neck
    draw.line([(30, 25), (40, 10)], fill=(255, 182, 193, 255), width=3)
    # Head
    draw.ellipse([38, 5, 45, 12], fill=(255, 182, 193, 255))
    # Beak
    draw.polygon([(45, 8), (50, 12), (44, 12)], fill=(0, 0, 0, 255))
    # Eye
    draw.rectangle([41, 7, 43, 9], fill=(0,0,0,255))

def draw_crocodile(draw):
    # Body
    draw.ellipse([5, 35, 35, 45], fill=(85, 107, 47, 255))
    # Snout
    draw.rectangle([30, 38, 48, 44], fill=(85, 107, 47, 255))
    # Head bump
    draw.ellipse([28, 33, 38, 44], fill=(85, 107, 47, 255))
    # Tail
    draw.polygon([(10, 40), (0, 48), (5, 45)], fill=(85, 107, 47, 255))
    # Scales
    for x in range(10, 30, 4):
        draw.polygon([(x, 35), (x+2, 32), (x+4, 35)], fill=(0, 50, 0, 255))
    # Eye
    draw.rectangle([32, 35, 34, 37], fill=(0,0,0,255))
    # Legs
    draw.rectangle([10, 43, 13, 48], fill=(0, 50, 0, 255))
    draw.rectangle([25, 43, 28, 48], fill=(0, 50, 0, 255))

def draw_armadillo(draw):
    # Shell (chord)
    draw.chord([5, 25, 40, 45], 180, 360, fill=(139, 115, 85, 255))
    # Shell bands
    for x in range(10, 35, 5):
        draw.line([(x, 25), (x, 45)], fill=(101, 67, 33, 255), width=1)
    # Head
    draw.ellipse([35, 35, 48, 45], fill=(205, 170, 125, 255))
    # Ears
    draw.polygon([(38, 35), (40, 28), (42, 35)], fill=(205, 170, 125, 255))
    # Eye
    draw.rectangle([42, 38, 44, 40], fill=(0,0,0,255))
    # Tail
    draw.polygon([(5, 40), (0, 45), (5, 45)], fill=(205, 170, 125, 255))
    # Legs
    draw.rectangle([15, 45, 18, 48], fill=(139, 115, 85, 255))
    draw.rectangle([25, 45, 28, 48], fill=(139, 115, 85, 255))

def draw_ant(draw):
    # Abdomen
    draw.ellipse([5, 28, 20, 40], fill=(50, 0, 0, 255))
    # Thorax
    draw.ellipse([18, 30, 30, 38], fill=(50, 0, 0, 255))
    # Head
    draw.ellipse([28, 26, 40, 38], fill=(50, 0, 0, 255))
    # Antennae
    draw.line([(35, 28), (42, 20)], fill=(0, 0, 0, 255), width=2)
    # Legs
    draw.line([(22, 36), (18, 46)], fill=(0, 0, 0, 255), width=2)
    draw.line([(25, 36), (25, 46)], fill=(0, 0, 0, 255), width=2)
    draw.line([(28, 36), (32, 46)], fill=(0, 0, 0, 255), width=2)

def draw_panther(draw):
    # Body
    draw.ellipse([8, 25, 38, 40], fill=(20, 20, 20, 255))
    # Head
    draw.ellipse([32, 18, 45, 32], fill=(20, 20, 20, 255))
    # Snout
    draw.ellipse([40, 25, 48, 32], fill=(20, 20, 20, 255))
    # Ears
    draw.polygon([(34, 18), (36, 12), (39, 18)], fill=(20, 20, 20, 255))
    # Tail
    draw.line([(12, 32), (5, 20)], fill=(20, 20, 20, 255), width=3)
    # Eye (glowing yellow)
    draw.rectangle([38, 22, 40, 24], fill=(255,255,0,255))
    # Legs
    draw.rectangle([15, 38, 18, 48], fill=(20, 20, 20, 255))
    draw.rectangle([30, 38, 33, 48], fill=(20, 20, 20, 255))

animals_to_fix = [
    ("walrus_50x50.png", draw_walrus),
    ("sloth_50x50.png", draw_sloth),
    ("iguana_50x50.png", draw_iguana),
    ("flamingo_50x50.png", draw_flamingo),
    ("crocodile_50x50.png", draw_crocodile),
    ("armadillo_50x50.png", draw_armadillo),
    ("ant_50x50.png", draw_ant),
    ("panther_50x50.png", draw_panther)
]

for filename, func in animals_to_fix:
    create_sprite(filename, func)
