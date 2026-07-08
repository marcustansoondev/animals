import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    target = f"images/animals/{filename}" if not filename.startswith("images/animals/") else filename
    img.save(target)
    print(f"Generated {target}")

def draw_zebra(draw):
    # Legs (white with dark hooves)
    draw.line([(18, 35), (18, 45)], fill=(255, 255, 255, 255), width=2)
    draw.rectangle([17, 45, 19, 48], fill=(30, 30, 30, 255))
    draw.line([(32, 35), (32, 45)], fill=(255, 255, 255, 255), width=2)
    draw.rectangle([31, 45, 33, 48], fill=(30, 30, 30, 255))
    
    # Body (white)
    draw.ellipse([10, 22, 35, 38], fill=(255, 255, 255, 255))
    
    # Neck and Head
    draw.polygon([(30, 30), (35, 25), (42, 10), (38, 10)], fill=(255, 255, 255, 255))
    draw.ellipse([35, 8, 45, 15], fill=(255, 255, 255, 255))
    
    # Snout (dark)
    draw.ellipse([42, 10, 48, 15], fill=(50, 50, 50, 255))
    
    # Ears
    draw.polygon([(38, 10), (36, 4), (40, 8)], fill=(255, 255, 255, 255))
    
    # Mane (black/white)
    draw.line([(38, 10), (34, 15)], fill=(0, 0, 0, 255), width=2)
    draw.line([(35, 14), (32, 20)], fill=(0, 0, 0, 255), width=2)
    draw.line([(32, 19), (29, 25)], fill=(0, 0, 0, 255), width=2)
    
    # Tail
    draw.line([(12, 28), (8, 40)], fill=(255, 255, 255, 255), width=2)
    draw.ellipse([6, 38, 10, 42], fill=(0, 0, 0, 255))
    
    # Eye
    draw.rectangle([40, 10, 42, 12], fill=(0,0,0,255))
    
    # Stripes (black lines over body and neck)
    # Body stripes
    for x in range(15, 32, 4):
        draw.line([(x, 23), (x-2, 37)], fill=(0, 0, 0, 255), width=1)
    
    # Neck stripes
    draw.line([(36, 12), (32, 22)], fill=(0, 0, 0, 255), width=1)
    draw.line([(38, 14), (34, 25)], fill=(0, 0, 0, 255), width=1)
    draw.line([(40, 16), (36, 28)], fill=(0, 0, 0, 255), width=1)

create_sprite("zebra_50x50.png", draw_zebra)
