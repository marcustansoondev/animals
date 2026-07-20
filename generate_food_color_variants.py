import os
import colorsys
from PIL import Image

def quantize_10(img):
    bg = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    bg.paste(img, (0, 0), img)
    rgb = Image.new("RGB", (50, 50), (255, 255, 255))
    alpha = bg.split()[3]
    rgb.paste(bg, mask=alpha)
    q = rgb.quantize(colors=9, method=Image.MEDIANCUT, dither=Image.NONE)
    f = q.convert("RGBA")
    fp = f.load()
    for y in range(50):
        for x in range(50):
            orig_a = alpha.getpixel((x, y))
            r, g, b, _ = fp[x, y]
            fp[x, y] = (r, g, b, orig_a)
    return f

def generate_variant(base_name, new_name, hue_shift, target_hue=None, hue_tolerance=0.2):
    base_path = f"images/food_desserts/{base_name}_50x50.png"
    if not os.path.exists(base_path):
        print(f"Base {base_path} not found!")
        return False
        
    img = Image.open(base_path).convert("RGBA")
    new_img = img.copy()
    pixels = new_img.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a == 0: continue
            
            h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
            
            # Don't modify pure greyscale/blacks/whites much
            if s > 0.05 and v > 0.1:
                modify = True
                if target_hue is not None:
                    dist = min(abs(h - target_hue), 1.0 - abs(h - target_hue))
                    if dist > hue_tolerance:
                        modify = False
                
                if modify:
                    new_h = (h + hue_shift) % 1.0
                    new_s, new_v = s, v
                    
                    if "chocolate" in new_name or "cola" in new_name or "rootbeer" in new_name:
                        new_s = min(s, 0.4)
                        new_v = min(v, 0.4)
                    elif "vanilla" in new_name:
                        new_s = min(s, 0.15)
                        new_v = min(v + 0.3, 1.0)
                        
                    nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                    pixels[x, y] = (int(nr*255), int(ng*255), int(nb*255), a)
                    
    final_img = quantize_10(new_img)
    out_path = f"images/food_desserts/{new_name}_50x50.png"
    final_img.save(out_path)
    return out_path

VARIANTS = [
    ("macaron", "macaron_matcha", "Matcha Macaron", 0.4, 0.95),
    ("macaron", "macaron_lemon", "Lemon Macaron", 0.2, 0.95),
    ("macaron", "macaron_blueberry", "Blueberry Macaron", 0.65, 0.95),
    ("macaron", "macaron_grape", "Grape Macaron", 0.8, 0.95),
    ("macaron", "macaron_chocolate", "Chocolate Macaron", 0.1, 0.95),
    
    ("donut", "donut_chocolate", "Chocolate Glazed Donut", 0.1, 0.95),
    ("donut", "donut_matcha", "Matcha Glazed Donut", 0.4, 0.95),
    ("donut", "donut_blueberry", "Blueberry Glazed Donut", 0.65, 0.95),
    ("donut", "donut_lemon", "Lemon Glazed Donut", 0.2, 0.95),
    ("donut", "donut_vanilla", "Vanilla Glazed Donut", 0.15, 0.95),
    
    ("cupcake", "cupcake_mint", "Mint Chocolate Cupcake", 0.5, None),
    ("cupcake", "cupcake_blueberry", "Blueberry Cupcake", 0.7, None),
    ("cupcake", "cupcake_strawberry", "Strawberry Cupcake", 0.9, None),
    ("cupcake", "cupcake_lemon", "Lemon Cupcake", 0.2, None),
    ("cupcake", "cupcake_grape", "Grape Cupcake", 0.8, None),
    
    ("soda", "soda_cola", "Cola Can", 0.4, 0.6),
    ("soda", "soda_lemonlime", "Lemon-Lime Soda Can", -0.25, 0.6),
    ("soda", "soda_orange", "Orange Soda Can", 0.5, 0.6),
    ("soda", "soda_grape", "Grape Soda Can", 0.2, 0.6),
    ("soda", "soda_rootbeer", "Root Beer Can", 0.45, 0.6),
    
    ("softserve", "softserve_chocolate", "Chocolate Soft Serve", 0.1, 0.95),
    ("softserve", "softserve_matcha", "Matcha Soft Serve", 0.4, 0.95),
    ("softserve", "softserve_mango", "Mango Soft Serve", 0.2, 0.95),
    ("softserve", "softserve_blueberry", "Blueberry Soft Serve", 0.65, 0.95),
    ("softserve", "softserve_melon", "Melon Soft Serve", 0.35, 0.95),
    
    ("lollipop", "lollipop_blue", "Blue Raspberry Lollipop", 0.65, 0.95),
    ("lollipop", "lollipop_green", "Green Apple Lollipop", 0.35, 0.95),
    ("lollipop", "lollipop_yellow", "Lemon Lollipop", 0.2, 0.95),
    ("lollipop", "lollipop_purple", "Grape Lollipop", 0.8, 0.95),
    ("lollipop", "lollipop_orange", "Orange Lollipop", 0.1, 0.95),
    
    ("cake", "cake_chocolate", "Chocolate Cake Slice", 0.1, 0.95),
    ("cake", "cake_matcha", "Matcha Cake Slice", 0.4, 0.95),
    ("cake", "cake_blueberry", "Blueberry Cake Slice", 0.65, 0.95),
    ("cake", "cake_lemon", "Lemon Cake Slice", 0.2, 0.95),
    ("cake", "cake_grape", "Grape Cake Slice", 0.8, 0.95),
    
    ("icecream", "icecream_mint", "Mint Ice Cream", 0.45, 0.95),
    ("icecream", "icecream_chocolate", "Chocolate Ice Cream", 0.1, 0.95),
    ("icecream", "icecream_vanilla", "Vanilla Ice Cream", 0.15, 0.95),
    ("icecream", "icecream_mango", "Mango Ice Cream", 0.2, 0.95),
    ("icecream", "icecream_blueberry", "Blueberry Ice Cream", 0.65, 0.95),
    
    ("candycane", "candycane_green", "Green Candy Cane", 0.35, 0.95),
    ("candycane", "candycane_blue", "Blue Candy Cane", 0.65, 0.95),
    ("candycane", "candycane_purple", "Purple Candy Cane", 0.8, 0.95),
    ("candycane", "candycane_orange", "Orange Candy Cane", 0.1, 0.95),
    ("candycane", "candycane_yellow", "Yellow Candy Cane", 0.2, 0.95),
    
    ("pudding", "pudding_matcha", "Matcha Pudding", 0.2, 0.15),
    ("pudding", "pudding_chocolate", "Chocolate Pudding", 0.9, 0.15),
    ("pudding", "pudding_strawberry", "Strawberry Pudding", 0.8, 0.15),
    ("pudding", "pudding_blueberry", "Blueberry Pudding", 0.5, 0.15),
    ("pudding", "pudding_taro", "Taro Pudding", 0.65, 0.15)
]

if __name__ == "__main__":
    os.makedirs("images/food_desserts", exist_ok=True)
    successes = []
    
    for base, new_name, desc, h_shift, t_hue in VARIANTS:
        out_path = generate_variant(base, new_name, h_shift, t_hue)
        if out_path:
            successes.append({
                "id": f"food_{new_name}",
                "name": desc,
                "filename": out_path,
                "category": "food_desserts",
                "type": "Drink" if "soda" in new_name else "Dessert",
                "material": "Variant",
                "rarity": "★★★☆☆",
                "description": f"A beautiful {desc.lower()} pixel art."
            })
            print(f"Generated {out_path}")
            
    # Inject into app.js
    app_js_path = "app.js"
    with open(app_js_path, "r") as f:
        content = f.read()
        
    if "food_macaron_matcha" in content:
        print("Entries already exist in app.js. Skipping injection.")
    else:
        target = '    { id: "food_pizzapie_whole", name: "Whole Pizza Pie", filename: "images/food_desserts/pizzapie_whole_50x50.png", category: "food_desserts", type: "Meal", material: "Cheese & Pepperoni", rarity: "★★★★★", description: "A full, unsliced round pizza pie fresh from the oven." }\n];'
        if target in content:
            js_entries = []
            for s in successes:
                entry = f'    {{ id: "{s["id"]}", name: "{s["name"]}", filename: "{s["filename"]}", category: "{s["category"]}", type: "{s["type"]}", material: "{s["material"]}", rarity: "{s["rarity"]}", description: "{s["description"]}" }}'
                js_entries.append(entry)
                
            insertion = '    { id: "food_pizzapie_whole", name: "Whole Pizza Pie", filename: "images/food_desserts/pizzapie_whole_50x50.png", category: "food_desserts", type: "Meal", material: "Cheese & Pepperoni", rarity: "★★★★★", description: "A full, unsliced round pizza pie fresh from the oven." },\n' + ",\n".join(js_entries) + "\n];"
            content = content.replace(target, insertion)
            with open(app_js_path, "w") as f:
                f.write(content)
            print(f"Injected {len(successes)} variant items into app.js!")
        else:
            print("Failed to find insertion point in app.js!")
