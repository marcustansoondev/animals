import os
import hashlib
from PIL import Image, ImageDraw

new_animals = [
    {"id": "alligator", "name": "Alligator", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Swamps", "rarity": "★★★☆☆", "description": "Large reptilian predators known for their powerful jaws."},
    {"id": "alpaca", "name": "Alpaca", "category": "domestic", "isPredator": False, "diet": "Herbivore", "habitat": "Mountains", "rarity": "★★☆☆☆", "description": "Fluffy herd animals bred for their soft fleece."},
    {"id": "ant", "name": "Ant", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Everywhere", "rarity": "★☆☆☆☆", "description": "Tiny industrious insects that can lift many times their body weight."},
    {"id": "armadillo", "name": "Armadillo", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Deserts", "rarity": "★★☆☆☆", "description": "Armored mammals that can roll into a ball for defense."},
    {"id": "badger", "name": "Badger", "category": "wild", "isPredator": True, "diet": "Omnivore", "habitat": "Woodlands", "rarity": "★★★☆☆", "description": "Fierce, burrowing mammals with striking black and white striped faces."},
    {"id": "bison", "name": "Bison", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Plains", "rarity": "★★★☆☆", "description": "Massive herd animals that roam the open prairies."},
    {"id": "camel", "name": "Camel", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Deserts", "rarity": "★★★☆☆", "description": "Desert-dwelling animals adapted to survive without water for long periods."},
    {"id": "chameleon", "name": "Chameleon", "category": "wild", "isPredator": True, "diet": "Insectivore", "habitat": "Rainforests", "rarity": "★★★★☆", "description": "Reptiles famous for their ability to change skin color."},
    {"id": "chimpanzee", "name": "Chimpanzee", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Jungles", "rarity": "★★★★☆", "description": "Highly intelligent apes closely related to humans."},
    {"id": "crocodile", "name": "Crocodile", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Rivers", "rarity": "★★★★☆", "description": "Ancient, stealthy predators that lurk in shallow waters."},
    {"id": "emu", "name": "Emu", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Outback", "rarity": "★★★☆☆", "description": "Tall, flightless birds known for their incredible running speed."},
    {"id": "falcon", "name": "Falcon", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Mountains", "rarity": "★★★★☆", "description": "High-speed birds of prey that dive at breakneck speeds."},
    {"id": "flamingo", "name": "Flamingo", "category": "wild", "isPredator": False, "diet": "Omnivore", "habitat": "Lakes", "rarity": "★★★☆☆", "description": "Elegant wading birds with distinctive pink plumage."},
    {"id": "gorilla", "name": "Gorilla", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Jungles", "rarity": "★★★★★", "description": "Powerful but gentle giant apes that live in troops."},
    {"id": "hedgehog", "name": "Hedgehog", "category": "wild", "isPredator": True, "diet": "Insectivore", "habitat": "Gardens", "rarity": "★★☆☆☆", "description": "Small, spiky mammals that roll up into a prickly ball."},
    {"id": "iguana", "name": "Iguana", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Tropics", "rarity": "★★★☆☆", "description": "Large, sun-loving lizards with a row of spines down their back."},
    {"id": "jaguar", "name": "Jaguar", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Rainforests", "rarity": "★★★★★", "description": "Fearsome big cats with stunning rosette patterns."},
    {"id": "lemur", "name": "Lemur", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Madagascar", "rarity": "★★★★☆", "description": "Agile primates with long, often ringed tails."},
    {"id": "leopard", "name": "Leopard", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Savannas", "rarity": "★★★★☆", "description": "Stealthy big cats capable of dragging prey up into trees."},
    {"id": "moose", "name": "Moose", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Boreal Forests", "rarity": "★★★★☆", "description": "The largest living species in the deer family, sporting massive antlers."},
    {"id": "ostrich", "name": "Ostrich", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Savannas", "rarity": "★★★☆☆", "description": "The world's largest bird, capable of running very fast."},
    {"id": "panther", "name": "Panther", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Jungles", "rarity": "★★★★★", "description": "Melanistic big cats known for their sleek black coats."},
    {"id": "pelican", "name": "Pelican", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Coasts", "rarity": "★★★☆☆", "description": "Large water birds featuring a distinctive throat pouch."},
    {"id": "sloth", "name": "Sloth", "category": "wild", "isPredator": False, "diet": "Herbivore", "habitat": "Rainforests", "rarity": "★★★★☆", "description": "Extremely slow-moving mammals that spend their lives hanging in trees."},
    {"id": "walrus", "name": "Walrus", "category": "wild", "isPredator": True, "diet": "Carnivore", "habitat": "Arctic", "rarity": "★★★★☆", "description": "Large marine mammals recognized by their prominent tusks and whiskers."}
]

def generate_sprite(animal_id):
    hash_bytes = hashlib.md5(animal_id.encode('utf-8')).digest()
    r = 50 + (hash_bytes[0] % 200)
    g = 50 + (hash_bytes[1] % 200)
    b = 50 + (hash_bytes[2] % 200)
    base_color = (r, g, b, 255)
    
    r2 = 50 + (hash_bytes[3] % 200)
    g2 = 50 + (hash_bytes[4] % 200)
    b2 = 50 + (hash_bytes[5] % 200)
    accent_color = (r2, g2, b2, 255)
    
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    for y in range(10):
        for x in range(5):
            idx = y * 5 + x
            val = hash_bytes[6 + (idx % 10)]
            if val % 3 == 0:
                color = base_color
            elif val % 3 == 1:
                color = accent_color
            else:
                color = None
            
            if color:
                draw.rectangle([x*5, y*5, x*5+4, y*5+4], fill=color)
                rx = 9 - x
                draw.rectangle([rx*5, y*5, rx*5+4, y*5+4], fill=color)
                
    img.save(f"{animal_id}_50x50.png")
    print(f"Generated {animal_id}_50x50.png")

def main():
    for a in new_animals:
        a["filename"] = f"{a['id']}_50x50.png"
        generate_sprite(a['id'])

    with open("app.js", "r") as f:
        content = f.read()

    idx = content.rfind("];")
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
            
        # check if we need a leading comma
        last_obj_end = content.rfind("}", 0, idx)
        prefix = ""
        if last_obj_end != -1:
            # count if there's already a comma after the last object
            between = content[last_obj_end+1:idx].strip()
            if not between.startswith(","):
                prefix = ","
                
        insert_str = prefix + "\n" + ",\n".join(js_arr) + "\n"
        new_content = content[:idx] + insert_str + content[idx:]
        
        with open("app.js", "w") as f:
            f.write(new_content)
        print("app.js successfully updated with 25 new animals.")
    else:
        print("Error: Could not find closing brace of animals array in app.js")

if __name__ == "__main__":
    main()
