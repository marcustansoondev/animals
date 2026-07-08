import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    target = f"images/animals/{filename}" if not filename.startswith("images/animals/") else filename
    img.save(target)
    print(f"Generated {target}")

def draw_alpaca(draw):
    # Legs
    draw.line([(18, 35), (18, 48)], fill=(150, 100, 50, 255), width=2)
    draw.line([(32, 35), (32, 48)], fill=(150, 100, 50, 255), width=2)
    # Fluffy Body
    draw.ellipse([10, 20, 38, 38], fill=(220, 180, 140, 255))
    draw.ellipse([8, 18, 25, 35], fill=(230, 190, 150, 255))
    # Fluffy Neck
    draw.ellipse([30, 10, 42, 30], fill=(220, 180, 140, 255))
    # Head
    draw.ellipse([34, 5, 46, 16], fill=(220, 180, 140, 255))
    # Snout
    draw.ellipse([42, 10, 48, 15], fill=(180, 130, 80, 255))
    # Ears
    draw.polygon([(36, 5), (38, 0), (40, 5)], fill=(180, 130, 80, 255))
    # Eye
    draw.rectangle([40, 8, 42, 10], fill=(0,0,0,255))

def draw_kangaroo(draw):
    # Big back legs
    draw.polygon([(15, 30), (10, 45), (20, 48), (25, 35)], fill=(180, 110, 50, 255))
    # Long thick tail
    draw.polygon([(15, 35), (2, 45), (10, 48), (18, 40)], fill=(180, 110, 50, 255))
    # Body (hunched)
    draw.ellipse([12, 18, 32, 40], fill=(210, 140, 80, 255))
    # Chest (lighter)
    draw.ellipse([22, 22, 32, 38], fill=(245, 200, 165, 255))
    # Neck and Head
    draw.polygon([(28, 25), (35, 12), (40, 15), (32, 28)], fill=(210, 140, 80, 255))
    draw.ellipse([32, 8, 42, 16], fill=(210, 140, 80, 255))
    # Snout
    draw.ellipse([38, 10, 46, 15], fill=(180, 110, 50, 255))
    # Small front arms
    draw.line([(28, 28), (35, 35)], fill=(180, 110, 50, 255), width=2)
    # Ears
    draw.polygon([(34, 8), (32, 0), (38, 6)], fill=(180, 110, 50, 255))
    # Eye
    draw.rectangle([38, 10, 40, 12], fill=(0,0,0,255))

def draw_hippo(draw):
    # Body - massive and low to ground
    draw.ellipse([2, 20, 42, 45], fill=(130, 140, 150, 255))
    # Head - huge and blocky
    draw.ellipse([30, 15, 48, 40], fill=(130, 140, 150, 255))
    # Snout - massive, rounded
    draw.ellipse([38, 25, 50, 42], fill=(120, 130, 140, 255))
    # Nostril
    draw.ellipse([44, 28, 47, 32], fill=(200, 150, 160, 255))
    # Ears
    draw.ellipse([32, 12, 36, 18], fill=(130, 140, 150, 255))
    # Eye
    draw.rectangle([38, 20, 40, 22], fill=(0,0,0,255))
    # Legs (thick and stubby)
    draw.rectangle([10, 40, 16, 48], fill=(100, 110, 120, 255))
    draw.rectangle([26, 40, 32, 48], fill=(100, 110, 120, 255))

def draw_parrot(draw):
    # colorful body (red)
    draw.ellipse([14, 20, 32, 40], fill=(235, 45, 45, 255))
    # wing (blue and green)
    draw.ellipse([14, 24, 28, 38], fill=(30, 90, 200, 255))
    draw.ellipse([16, 28, 24, 36], fill=(50, 180, 50, 255))
    # long tail (red and blue)
    draw.polygon([(16, 36), (10, 48), (20, 48), (20, 36)], fill=(235, 45, 45, 255))
    draw.polygon([(18, 38), (14, 48), (17, 48), (20, 38)], fill=(30, 90, 200, 255))
    # neck & head (red)
    draw.ellipse([22, 10, 34, 22], fill=(235, 45, 45, 255))
    # white face patch
    draw.ellipse([28, 12, 33, 18], fill=(255, 255, 255, 255))
    # black eye
    draw.rectangle([30, 14, 32, 16], fill=(0, 0, 0, 255))
    # hooked yellow beak
    draw.polygon([(32, 13), (40, 15), (32, 21)], fill=(245, 220, 30, 255))
    # grey legs
    draw.line([(22, 38), (20, 45)], fill=(120, 120, 120, 255), width=2)
    draw.line([(26, 38), (28, 45)], fill=(120, 120, 120, 255), width=2)

def draw_eagle(draw):
    # dark brown body
    draw.ellipse([10, 20, 34, 38], fill=(90, 60, 40, 255))
    # wing
    draw.ellipse([12, 23, 28, 36], fill=(65, 40, 25, 255))
    # tail feathers (white/dark tip)
    draw.polygon([(12, 32), (4, 42), (12, 42)], fill=(255, 255, 255, 255))
    draw.polygon([(4, 40), (2, 44), (6, 44)], fill=(40, 30, 20, 255))
    # neck and head (white)
    draw.polygon([(26, 24), (32, 24), (32, 12), (24, 12)], fill=(255, 255, 255, 255))
    draw.ellipse([24, 8, 34, 18], fill=(255, 255, 255, 255))
    # hooked yellow beak
    draw.polygon([(32, 11), (42, 13), (32, 19)], fill=(245, 190, 20, 255))
    # yellow eye
    draw.rectangle([29, 11, 31, 13], fill=(245, 190, 20, 255))
    draw.point((30, 12), fill=(0, 0, 0, 255)) # Pupil
    # yellow legs & talons
    draw.line([(20, 36), (18, 45)], fill=(245, 190, 20, 255), width=2)
    draw.line([(26, 36), (28, 45)], fill=(245, 190, 20, 255), width=2)

animals_to_fix = [
    ("alpaca_50x50.png", draw_alpaca),
    ("kangaroo_50x50.png", draw_kangaroo),
    ("hippo_50x50.png", draw_hippo),
    ("parrot_50x50.png", draw_parrot),
    ("eagle_50x50.png", draw_eagle)
]

for filename, func in animals_to_fix:
    create_sprite(filename, func)
