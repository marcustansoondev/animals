import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    target = f"images/animals/{filename}" if not filename.startswith("images/animals/") else filename
    img.save(target)
    print(f"Generated {target}")

def draw_cat(draw):
    # Body (white)
    draw.ellipse([10, 25, 35, 40], fill=(240, 240, 240, 255))
    # Head
    draw.ellipse([25, 15, 40, 30], fill=(240, 240, 240, 255))
    # Ears (white with pink inner)
    draw.polygon([(26, 18), (30, 8), (32, 18)], fill=(240, 240, 240, 255))
    draw.polygon([(28, 17), (30, 11), (31, 17)], fill=(255, 182, 193, 255))
    
    draw.polygon([(33, 18), (36, 10), (39, 18)], fill=(240, 240, 240, 255))
    draw.polygon([(34, 17), (36, 13), (37, 17)], fill=(255, 182, 193, 255))
    
    # Tail (curved up)
    draw.arc([5, 15, 18, 35], 90, 270, fill=(240, 240, 240, 255), width=4)
    # Legs
    draw.rectangle([14, 38, 17, 48], fill=(220, 220, 220, 255)) # back left
    draw.rectangle([18, 38, 21, 48], fill=(240, 240, 240, 255)) # back right
    draw.rectangle([28, 38, 31, 48], fill=(220, 220, 220, 255)) # front left
    draw.rectangle([32, 38, 35, 48], fill=(240, 240, 240, 255)) # front right
    # Eye
    draw.rectangle([33, 20, 35, 22], fill=(0,0,0,255))
    # Nose
    draw.point((40, 25), fill=(255, 105, 180, 255))
    # Whiskers
    draw.line([(40, 26), (46, 24)], fill=(150, 150, 150, 255))
    draw.line([(40, 26), (46, 28)], fill=(150, 150, 150, 255))

def draw_fox(draw):
    # Colors
    orange = (230, 100, 20, 255)
    white = (245, 245, 245, 255)
    black = (30, 30, 30, 255)
    
    # Body
    draw.ellipse([10, 25, 35, 40], fill=orange)
    # Belly/chest fluff
    draw.ellipse([20, 30, 32, 40], fill=white)
    # Head
    draw.ellipse([25, 15, 40, 30], fill=orange)
    # Snout
    draw.polygon([(35, 20), (48, 28), (35, 28)], fill=orange)
    draw.polygon([(38, 25), (48, 28), (38, 30)], fill=white)
    # Nose
    draw.point((48, 28), fill=black)
    # Ears
    draw.polygon([(26, 18), (30, 8), (32, 18)], fill=orange)
    draw.polygon([(29, 8), (31, 8), (30, 12)], fill=black) # black tip
    draw.polygon([(34, 18), (37, 10), (40, 18)], fill=orange)
    draw.polygon([(36, 10), (38, 10), (37, 14)], fill=black) # black tip
    
    # Bushy Tail
    draw.ellipse([2, 20, 16, 42], fill=orange)
    # White tail tip
    draw.polygon([(2, 35), (8, 42), (12, 35)], fill=white)
    
    # Legs (black boots)
    # Back legs
    draw.rectangle([14, 38, 17, 43], fill=orange)
    draw.rectangle([14, 43, 17, 48], fill=black)
    draw.rectangle([18, 38, 21, 43], fill=orange)
    draw.rectangle([18, 43, 21, 48], fill=black)
    # Front legs
    draw.rectangle([28, 38, 31, 43], fill=orange)
    draw.rectangle([28, 43, 31, 48], fill=black)
    draw.rectangle([32, 38, 35, 43], fill=orange)
    draw.rectangle([32, 43, 35, 48], fill=black)
    
    # Eye
    draw.rectangle([34, 20, 36, 22], fill=black)


animals_to_fix = [
    ("cat_50x50.png", draw_cat),
    ("fox_50x50.png", draw_fox)
]

for filename, func in animals_to_fix:
    create_sprite(filename, func)
