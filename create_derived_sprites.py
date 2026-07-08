import os
from PIL import Image

transformations = [
    ("alligator", "lizard_50x50.png", (30, 80, 30), 0.8),
    ("alpaca", "sheep_50x50.png", (180, 140, 100), 0.6),
    ("ant", "spider_50x50.png", (50, 0, 0), 0.9),
    ("armadillo", "turtle_50x50.png", (130, 100, 80), 0.7),
    ("badger", "raccoon_50x50.png", (100, 100, 100), 0.6),
    ("bison", "cow_50x50.png", (80, 50, 30), 0.7),
    ("camel", "horse_50x50.png", (200, 170, 100), 0.6),
    ("chameleon", "lizard_50x50.png", (0, 255, 255), 0.5),
    ("chimpanzee", "monkey_50x50.png", (40, 30, 30), 0.8),
    ("crocodile", "lizard_50x50.png", (50, 100, 50), 0.7),
    ("emu", "chicken_50x50.png", (120, 110, 100), 0.8),
    ("falcon", "eagle_50x50.png", (100, 130, 180), 0.5),
    ("flamingo", "duck_50x50.png", (255, 100, 150), 0.8),
    ("gorilla", "monkey_50x50.png", (20, 20, 20), 0.9),
    ("hedgehog", "pig_50x50.png", (130, 100, 70), 0.7),
    ("iguana", "lizard_50x50.png", (100, 200, 50), 0.6),
    ("jaguar", "cheetah_50x50.png", (255, 180, 50), 0.5),
    ("lemur", "monkey_50x50.png", (150, 150, 150), 0.8),
    ("leopard", "cheetah_50x50.png", (255, 200, 100), 0.4),
    ("moose", "deer_50x50.png", (90, 60, 40), 0.7),
    ("ostrich", "chicken_50x50.png", (50, 50, 50), 0.8),
    ("panther", "tiger_50x50.png", (30, 30, 30), 0.9),
    ("pelican", "duck_50x50.png", (240, 240, 240), 0.8),
    ("sloth", "bear_50x50.png", (160, 140, 110), 0.6),
    ("walrus", "bear_50x50.png", (120, 90, 70), 0.7),
]

def tint_image(base_path, target_path, tint_color, intensity):
    # Try looking in images/animals/ first, then current directory
    if os.path.exists(f"images/animals/{base_path}"):
        src = f"images/animals/{base_path}"
    elif os.path.exists(base_path):
        src = base_path
    else:
        print(f"Could not find base image {base_path}")
        return

    img = Image.open(src).convert("RGBA")
    data = img.getdata()
    new_data = []
    tr, tg, tb = tint_color
    
    for r, g, b, a in data:
        if a > 0:
            # Keep very dark colors (outlines, eyes)
            if r < 40 and g < 40 and b < 40:
                new_data.append((r, g, b, a))
            # Keep very light colors (highlights, eye shines)
            elif r > 240 and g > 240 and b > 240:
                new_data.append((r, g, b, a))
            else:
                nr = int(r * (1 - intensity) + tr * intensity)
                ng = int(g * (1 - intensity) + tg * intensity)
                nb = int(b * (1 - intensity) + tb * intensity)
                new_data.append((nr, ng, nb, a))
        else:
            new_data.append((r, g, b, a))
            
    img.putdata(new_data)
    img.save(target_path)
    print(f"Generated {target_path} from {base_path}")

for animal_id, base_file, color, intensity in transformations:
    tint_image(base_file, f"images/animals/{animal_id}_50x50.png", color, intensity)
