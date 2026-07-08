import os
from PIL import Image, ImageDraw

new_animals = [
    {"id": "platypus", "name": "Platypus", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Rivers", "rarity": "★★★★★", "description": "Semi-aquatic egg-laying mammal native to eastern Australia."},
    {"id": "meerkat", "name": "Meerkat", "category": "wild", "isPredator": False, "diet": "Insectivore", "habitat": "Deserts", "rarity": "★★★☆☆", "description": "Small mongooses known for their sentinel behavior of standing on hind legs."},
    {"id": "otter", "name": "Otter", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Rivers & Coasts", "rarity": "★★★★☆", "description": "Playful semi-aquatic mammals known for holding hands while sleeping."},
    {"id": "puffin", "name": "Puffin", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Cliffs & Ocean", "rarity": "★★★★☆", "description": "Colorfully beaked seabirds that nest in clifftop colonies."},
    {"id": "capybara", "name": "Capybara", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Swamps & Rivers", "rarity": "★★★★☆", "description": "The largest living rodents in the world, known for their gentle and social nature."},
    {"id": "seal", "name": "Seal", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Polar & Coasts", "rarity": "★★★☆☆", "description": "Sleek marine mammals that are clumsy on land but extremely agile in water."},
    {"id": "swan", "name": "Swan", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Lakes & Ponds", "rarity": "★★★☆☆", "description": "Large, elegant waterfowl famous for their graceful necks and lifelong mating bonds."},
    {"id": "goose", "name": "Goose", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "Farms & Ponds", "rarity": "★★☆☆☆", "description": "Highly territorial waterfowl known for their loud honks and guard-dog behavior."},
    {"id": "donkey", "name": "Donkey", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "Farms & Deserts", "rarity": "★★☆☆☆", "description": "Sturdy domesticated beasts of burden known for their intelligence and caution."},
    {"id": "goat", "name": "Goat", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "Mountains & Farms", "rarity": "★★☆☆☆", "description": "Sure-footed herbivores famous for their climbing agility and curious eating habits."},
    {"id": "yak", "name": "Yak", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "High Mountains", "rarity": "★★★★☆", "description": "Long-haired domesticated bovines native to the Himalayan region."},
    {"id": "hamster", "name": "Hamster", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "Grasslands & Homes", "rarity": "★☆☆☆☆", "description": "Small, burrowing rodents with expandable cheek pouches used to carry food."},
    {"id": "skunk", "name": "Skunk", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Forests", "rarity": "★★★☆☆", "description": "Mammals famous for their ability to spray a liquid with a strong, unpleasant odor."},
    {"id": "peacock", "name": "Peacock", "category": "domestic", "isPredator": False, "diet": "Omnivore", "habitat": "Gardens & Forests", "rarity": "★★★★☆", "description": "Male peafowls renowned for their iridescent blue and green tail plumage."},
    {"id": "crow", "name": "Crow", "category": "wild", "isPredator": True, "diet": "Omnivore", "habitat": "Everywhere", "rarity": "★★☆☆☆", "description": "Highly intelligent black birds capable of problem-solving and recognizing human faces."}
]

def draw_platypus(draw):
    # Flat beaver-like tail
    draw.ellipse([2, 26, 16, 36], fill=(50, 35, 20, 255))
    # Brown body
    draw.ellipse([10, 22, 38, 38], fill=(95, 65, 45, 255))
    # Head
    draw.ellipse([32, 18, 44, 30], fill=(95, 65, 45, 255))
    # Duck bill
    draw.polygon([(40, 24), (48, 25), (46, 31), (39, 29)], fill=(40, 40, 45, 255))
    # Feet
    draw.rectangle([16, 36, 22, 42], fill=(30, 30, 35, 255))
    draw.rectangle([30, 36, 36, 42], fill=(30, 30, 35, 255))
    # Eye
    draw.rectangle([37, 21, 39, 23], fill=(0,0,0,255))

def draw_meerkat(draw):
    # Stand-up body (slender)
    draw.ellipse([18, 16, 28, 42], fill=(210, 180, 140, 255))
    # Head
    draw.ellipse([17, 8, 27, 18], fill=(210, 180, 140, 255))
    # Muzzle
    draw.polygon([(24, 12), (30, 14), (24, 16)], fill=(185, 155, 115, 255))
    # Back stripes
    draw.line([(19, 24), (23, 24)], fill=(100, 80, 65, 255), width=1)
    draw.line([(19, 28), (23, 28)], fill=(100, 80, 65, 255), width=1)
    draw.line([(19, 32), (23, 32)], fill=(100, 80, 65, 255), width=1)
    # Dark eye patch & Eye
    draw.rectangle([22, 11, 25, 13], fill=(80, 60, 45, 255))
    draw.rectangle([23, 11, 24, 12], fill=(0, 0, 0, 255))
    # Legs & feet
    draw.rectangle([19, 40, 22, 48], fill=(185, 155, 115, 255))
    draw.rectangle([24, 40, 27, 48], fill=(185, 155, 115, 255))
    # Tail
    draw.line([(22, 38), (14, 48)], fill=(180, 150, 110, 255), width=2)

def draw_otter(draw):
    # Long sleek body
    draw.ellipse([8, 22, 38, 38], fill=(120, 80, 50, 255))
    # Neck and head
    draw.ellipse([30, 20, 42, 34], fill=(120, 80, 50, 255))
    draw.ellipse([36, 16, 46, 28], fill=(120, 80, 50, 255))
    # Light chin
    draw.ellipse([33, 25, 41, 31], fill=(220, 210, 190, 255))
    # Tail
    draw.polygon([(10, 30), (0, 35), (10, 34)], fill=(100, 65, 40, 255))
    # Legs
    draw.rectangle([14, 36, 18, 44], fill=(100, 65, 40, 255))
    draw.rectangle([28, 36, 32, 44], fill=(100, 65, 40, 255))
    # Eye
    draw.rectangle([41, 19, 43, 21], fill=(0,0,0,255))

def draw_puffin(draw):
    # Black body
    draw.ellipse([10, 20, 32, 42], fill=(30, 30, 35, 255))
    # White belly/chest
    draw.ellipse([16, 22, 30, 40], fill=(255, 255, 255, 255))
    # Head (black)
    draw.ellipse([18, 10, 30, 22], fill=(30, 30, 35, 255))
    # White face patch
    draw.ellipse([23, 12, 30, 20], fill=(255, 255, 255, 255))
    # Colorful beak
    draw.polygon([(29, 12), (39, 16), (29, 21)], fill=(255, 90, 0, 255))
    # Orange legs
    draw.line([(18, 40), (18, 48)], fill=(255, 120, 40, 255), width=2)
    draw.line([(24, 40), (24, 48)], fill=(255, 120, 40, 255), width=2)
    # Eye
    draw.rectangle([26, 14, 28, 16], fill=(0,0,0,255))

def draw_capybara(draw):
    # Stout body
    draw.ellipse([6, 18, 38, 44], fill=(125, 85, 55, 255))
    # Boxy Head
    draw.rectangle([30, 20, 44, 34], fill=(125, 85, 55, 255))
    draw.ellipse([38, 23, 46, 34], fill=(100, 65, 40, 255))
    # Ear
    draw.ellipse([31, 17, 35, 21], fill=(95, 60, 35, 255))
    # Legs
    draw.rectangle([12, 42, 17, 48], fill=(95, 60, 35, 255))
    draw.rectangle([27, 42, 32, 48], fill=(95, 60, 35, 255))
    # Eye
    draw.rectangle([38, 22, 40, 24], fill=(0,0,0,255))

def draw_seal(draw):
    # Sleek grey body
    draw.ellipse([8, 20, 38, 42], fill=(140, 150, 160, 255))
    # Rear flippers
    draw.polygon([(10, 31), (0, 26), (0, 36)], fill=(115, 125, 135, 255))
    # Head
    draw.ellipse([32, 16, 46, 30], fill=(140, 150, 160, 255))
    # Light snout
    draw.ellipse([40, 22, 47, 29], fill=(180, 190, 200, 255))
    # Front flipper
    draw.polygon([(22, 34), (20, 46), (28, 42)], fill=(115, 125, 135, 255))
    # Eye
    draw.rectangle([38, 20, 40, 22], fill=(0,0,0,255))

def draw_swan(draw):
    # Body floating
    draw.ellipse([10, 24, 36, 42], fill=(250, 250, 250, 255))
    # Long neck
    draw.line([(30, 28), (35, 12)], fill=(250, 250, 250, 255), width=4)
    draw.line([(35, 12), (31, 6)], fill=(250, 250, 250, 255), width=4)
    # Head
    draw.ellipse([27, 3, 34, 10], fill=(250, 250, 250, 255))
    # Beak
    draw.polygon([(28, 6), (20, 9), (28, 10)], fill=(255, 120, 0, 255))
    # Eye
    draw.rectangle([30, 5, 32, 7], fill=(0,0,0,255))

def draw_goose(draw):
    # Body
    draw.ellipse([10, 22, 34, 40], fill=(225, 225, 230, 255))
    # Neck
    draw.line([(28, 26), (32, 14)], fill=(225, 225, 230, 255), width=3)
    # Head
    draw.ellipse([29, 8, 35, 15], fill=(225, 225, 230, 255))
    # Bill
    draw.polygon([(34, 10), (41, 12), (34, 14)], fill=(255, 130, 20, 255))
    # Legs
    draw.line([(18, 38), (18, 48)], fill=(255, 120, 30, 255), width=2)
    draw.line([(25, 38), (25, 48)], fill=(255, 120, 30, 255), width=2)
    # Eye
    draw.rectangle([31, 10, 33, 12], fill=(0, 0, 0, 255))

def draw_donkey(draw):
    # Grey body
    draw.ellipse([8, 22, 36, 42], fill=(120, 120, 125, 255))
    # Neck
    draw.polygon([(25, 26), (33, 26), (37, 14), (31, 14)], fill=(120, 120, 125, 255))
    # Head
    draw.ellipse([31, 8, 43, 18], fill=(120, 120, 125, 255))
    # Muzzle
    draw.ellipse([39, 12, 44, 18], fill=(235, 235, 240, 255))
    # Ears
    draw.polygon([(32, 9), (30, 0), (35, 8)], fill=(100, 100, 105, 255))
    draw.polygon([(35, 9), (33, 1), (38, 8)], fill=(100, 100, 105, 255))
    # Legs
    draw.rectangle([13, 40, 17, 48], fill=(100, 100, 105, 255))
    draw.rectangle([27, 40, 31, 48], fill=(100, 100, 105, 255))
    # Eye
    draw.rectangle([35, 11, 37, 13], fill=(0,0,0,255))

def draw_goat(draw):
    # Body
    draw.ellipse([10, 22, 36, 40], fill=(245, 240, 230, 255))
    # Neck & Head
    draw.polygon([(27, 24), (33, 24), (37, 12), (31, 12)], fill=(245, 240, 230, 255))
    draw.ellipse([30, 8, 39, 16], fill=(245, 240, 230, 255))
    # Floppy ears
    draw.polygon([(30, 11), (27, 18), (32, 14)], fill=(235, 230, 220, 255))
    # Beard
    draw.polygon([(32, 15), (34, 21), (36, 15)], fill=(245, 240, 230, 255))
    # Curved horns
    draw.arc([26, 0, 36, 10], 0, 180, fill=(150, 140, 130, 255), width=2)
    # Legs with dark hooves
    draw.rectangle([14, 38, 17, 46], fill=(220, 215, 205, 255))
    draw.rectangle([14, 46, 17, 48], fill=(50, 50, 50, 255)) # Hoof
    draw.rectangle([28, 38, 31, 46], fill=(220, 215, 205, 255))
    draw.rectangle([28, 46, 31, 48], fill=(50, 50, 50, 255)) # Hoof
    # Eye outline with black pupil
    draw.ellipse([33, 9, 37, 13], fill=(255, 255, 255, 255))
    draw.rectangle([34, 10, 36, 12], fill=(0, 0, 0, 255))

def draw_yak(draw):
    # Large shaggy body
    draw.ellipse([5, 18, 40, 44], fill=(75, 50, 35, 255))
    draw.ellipse([12, 14, 28, 26], fill=(75, 50, 35, 255))
    # Head
    draw.ellipse([32, 18, 44, 30], fill=(75, 50, 35, 255))
    # Horns
    draw.line([(38, 20), (42, 12)], fill=(225, 225, 225, 255), width=2)
    draw.line([(42, 12), (38, 8)], fill=(225, 225, 225, 255), width=2)
    # Legs
    draw.rectangle([10, 40, 16, 48], fill=(55, 35, 25, 255))
    draw.rectangle([28, 40, 34, 48], fill=(55, 35, 25, 255))
    # Eye
    draw.rectangle([37, 22, 39, 24], fill=(0,0,0,255))

def draw_hamster(draw):
    # Chubby body
    draw.ellipse([10, 20, 38, 44], fill=(225, 160, 100, 255)) # Golden fur
    draw.ellipse([16, 24, 32, 44], fill=(255, 245, 235, 255)) # White belly
    # Head & Chubby cheeks
    draw.ellipse([26, 18, 40, 32], fill=(225, 160, 100, 255))
    draw.ellipse([32, 24, 39, 31], fill=(255, 200, 200, 255)) # Pink cheeks!
    # Pink ears
    draw.ellipse([27, 12, 33, 20], fill=(225, 160, 100, 255))
    draw.ellipse([29, 14, 32, 18], fill=(255, 190, 190, 255)) # Pink inner ear
    # Tiny legs
    draw.rectangle([14, 43, 18, 48], fill=(255, 200, 200, 255))
    draw.rectangle([30, 43, 34, 48], fill=(255, 200, 200, 255))
    # Cute black eye
    draw.ellipse([33, 20, 37, 24], fill=(0, 0, 0, 255))
    draw.point((34, 21), fill=(255, 255, 255, 255)) # Highlight

def draw_skunk(draw):
    # Body
    draw.ellipse([8, 22, 34, 42], fill=(35, 35, 35, 255))
    # Head
    draw.ellipse([28, 18, 38, 30], fill=(35, 35, 35, 255))
    # Bushy tail pointing up
    draw.polygon([(10, 28), (2, 9), (14, 18)], fill=(35, 35, 35, 255))
    # White stripes
    draw.line([(33, 20), (21, 24)], fill=(255, 255, 255, 255), width=2)
    draw.line([(21, 24), (9, 26)], fill=(255, 255, 255, 255), width=2)
    draw.line([(9, 26), (5, 11)], fill=(255, 255, 255, 255), width=2)
    # Legs
    draw.rectangle([13, 40, 16, 47], fill=(20, 20, 20, 255))
    draw.rectangle([25, 40, 28, 47], fill=(20, 20, 20, 255))
    # Eye
    draw.rectangle([33, 22, 35, 24], fill=(0,0,0,255))

def draw_peacock(draw):
    # Body
    draw.ellipse([10, 24, 28, 38], fill=(0, 120, 240, 255))
    # Fan tail (green)
    draw.ellipse([0, 12, 20, 38], fill=(35, 135, 35, 255))
    # Tail spots (yellow highlights)
    draw.ellipse([3, 15, 6, 18], fill=(255, 215, 0, 255))
    draw.ellipse([8, 18, 11, 21], fill=(255, 215, 0, 255))
    draw.ellipse([5, 26, 8, 29], fill=(255, 215, 0, 255))
    # Neck & Head
    draw.line([(23, 28), (27, 14)], fill=(0, 120, 240, 255), width=3)
    draw.ellipse([24, 8, 30, 15], fill=(0, 120, 240, 255))
    # Bill
    draw.polygon([(29, 10), (34, 11), (29, 13)], fill=(210, 210, 190, 255))
    # Eye
    draw.rectangle([26, 10, 28, 12], fill=(0,0,0,255))

def draw_crow(draw):
    # Black body
    draw.ellipse([12, 22, 34, 38], fill=(45, 45, 50, 255))
    draw.ellipse([16, 24, 28, 32], fill=(25, 25, 30, 255)) # Wing
    # Head & Bill
    draw.ellipse([28, 14, 38, 24], fill=(45, 45, 50, 255))
    draw.polygon([(36, 16), (46, 19), (36, 22)], fill=(20, 20, 25, 255))
    # Tail feathers
    draw.polygon([(14, 30), (6, 36), (12, 34)], fill=(25, 25, 30, 255))
    # Legs
    draw.line([(20, 36), (20, 46)], fill=(20, 20, 25, 255), width=2)
    draw.line([(26, 36), (26, 46)], fill=(20, 20, 25, 255), width=2)
    # Yellow eye patch with black pupil to pop against dark grey head
    draw.ellipse([31, 16, 35, 20], fill=(255, 220, 40, 255))
    draw.rectangle([32, 17, 34, 19], fill=(0, 0, 0, 255))

drawing_functions = {
    "platypus": draw_platypus,
    "meerkat": draw_meerkat,
    "otter": draw_otter,
    "puffin": draw_puffin,
    "capybara": draw_capybara,
    "seal": draw_seal,
    "swan": draw_swan,
    "goose": draw_goose,
    "donkey": draw_donkey,
    "goat": draw_goat,
    "yak": draw_yak,
    "hamster": draw_hamster,
    "skunk": draw_skunk,
    "peacock": draw_peacock,
    "crow": draw_crow
}

def generate_sprite(animal_id):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    if animal_id in drawing_functions:
        drawing_functions[animal_id](draw)
    else:
        # Fallback (never triggers for our 15, but good practice)
        draw.rectangle([10, 10, 40, 40], fill=(128, 128, 128, 255))
        
    out_dir = "images/animals"
    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, f"{animal_id}_50x50.png")
    img.save(filepath)
    print(f"Generated {filepath}")

def main():
    for a in new_animals:
        a["filename"] = f"{a['id']}_50x50.png"
        generate_sprite(a['id'])

    with open("app.js", "r") as f:
        content = f.read()

    app_state_idx = content.find("// Application State")
    idx = content.rfind("];", 0, app_state_idx)
    if idx != -1:
        js_arr = []
        for a in new_animals:
            js_str = f"""    {{
        id: "{a['id']}",
        name: "{a['name']}",
        filename: "{a['filename']}",
        category: "{a['category']}",
        isPredator: {'true' if a['isPredator'] else 'false'},
        diet: "{a['diet']}",
        habitat: "{a['habitat']}",
        rarity: "{a['rarity']}",
        description: "{a['description']}"
    }}"""
            js_arr.append(js_str)
            
        last_obj_end = content.rfind("}", 0, idx)
        prefix = ""
        if last_obj_end != -1:
            between = content[last_obj_end+1:idx].strip()
            if not between.startswith(","):
                prefix = ","
                
        insert_str = prefix + "\n" + ",\n".join(js_arr) + "\n"
        new_content = content[:idx] + insert_str + content[idx:]
        
        with open("app.js", "w") as f:
            f.write(new_content)
        print("app.js successfully updated with 15 new animals.")
    else:
        print("Error: Could not find closing brace of animals array in app.js")

if __name__ == "__main__":
    main()
