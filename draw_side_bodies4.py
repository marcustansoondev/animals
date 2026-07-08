import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    target = f"images/animals/{filename}" if not filename.startswith("images/animals/") else filename
    img.save(target)
    print(f"Generated {target}")

def draw_giraffe(draw):
    # Legs
    draw.line([(18, 35), (18, 48)], fill=(244, 208, 63, 255), width=2)
    draw.line([(32, 35), (32, 48)], fill=(244, 208, 63, 255), width=2)
    # Body
    draw.ellipse([12, 20, 38, 35], fill=(244, 208, 63, 255))
    # Spots
    draw.ellipse([15, 22, 20, 27], fill=(160, 65, 0, 255))
    draw.ellipse([25, 25, 30, 30], fill=(160, 65, 0, 255))
    draw.ellipse([30, 22, 35, 27], fill=(160, 65, 0, 255))
    # Neck
    draw.polygon([(30, 25), (35, 25), (42, 8), (38, 8)], fill=(244, 208, 63, 255))
    draw.ellipse([35, 12, 38, 17], fill=(160, 65, 0, 255))
    # Head
    draw.ellipse([35, 3, 45, 12], fill=(244, 208, 63, 255))
    # Snout
    draw.ellipse([42, 6, 48, 12], fill=(235, 190, 120, 255))
    # Ossicones
    draw.line([(38, 4), (36, 1)], fill=(160, 65, 0, 255), width=2)
    draw.line([(42, 4), (40, 1)], fill=(160, 65, 0, 255), width=2)
    # Eye
    draw.rectangle([40, 6, 42, 8], fill=(0,0,0,255))
    # Tail
    draw.line([(12, 25), (8, 35)], fill=(244, 208, 63, 255), width=2)
    draw.ellipse([6, 35, 10, 39], fill=(160, 65, 0, 255))

def draw_hippo(draw):
    # Body
    draw.ellipse([5, 20, 40, 45], fill=(110, 120, 130, 255))
    # Head
    draw.ellipse([30, 18, 48, 38], fill=(110, 120, 130, 255))
    # Snout
    draw.ellipse([38, 25, 50, 38], fill=(110, 120, 130, 255))
    # Ears
    draw.ellipse([32, 15, 36, 20], fill=(110, 120, 130, 255))
    # Eye
    draw.rectangle([38, 22, 40, 24], fill=(0,0,0,255))
    # Nostril
    draw.ellipse([45, 28, 47, 30], fill=(255, 190, 205, 255))
    # Legs
    draw.rectangle([10, 40, 15, 48], fill=(90, 100, 110, 255))
    draw.rectangle([25, 40, 30, 48], fill=(90, 100, 110, 255))

def draw_rhino(draw):
    # Body
    draw.ellipse([5, 20, 38, 42], fill=(120, 125, 130, 255))
    # Head
    draw.ellipse([30, 18, 46, 35], fill=(120, 125, 130, 255))
    # Snout
    draw.ellipse([38, 22, 48, 35], fill=(120, 125, 130, 255))
    # Big Horn
    draw.polygon([(46, 25), (42, 25), (46, 12)], fill=(240, 240, 240, 255))
    # Small Horn
    draw.polygon([(42, 22), (39, 22), (42, 16)], fill=(240, 240, 240, 255))
    # Ears
    draw.polygon([(32, 20), (30, 12), (36, 18)], fill=(120, 125, 130, 255))
    # Eye
    draw.rectangle([38, 20, 40, 22], fill=(0,0,0,255))
    # Tail
    draw.line([(8, 25), (4, 35)], fill=(120, 125, 130, 255), width=2)
    # Legs
    draw.rectangle([10, 38, 15, 48], fill=(100, 105, 110, 255))
    draw.rectangle([25, 38, 30, 48], fill=(100, 105, 110, 255))

animals_to_fix = [
    ("giraffe_50x50.png", draw_giraffe),
    ("hippo_50x50.png", draw_hippo),
    ("rhino_50x50.png", draw_rhino)
]

for filename, func in animals_to_fix:
    create_sprite(filename, func)
