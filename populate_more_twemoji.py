import urllib.request
from PIL import Image
import os
import re

def add_outline_and_quantize(emoji_img):
    emoji_img = emoji_img.resize((40, 40), Image.Resampling.NEAREST)
    canvas = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    canvas.paste(emoji_img, (5, 5))
    pixels = canvas.load()
    
    for y in range(50):
        for x in range(50):
            r, g, b, a = pixels[x, y]
            if a > 127:
                pixels[x, y] = (r, g, b, 255)
            else:
                pixels[x, y] = (0, 0, 0, 0)
    
    outline = []
    for y in range(50):
        for x in range(50):
            if pixels[x, y][3] > 0:
                continue
            is_edge = False
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 50 and 0 <= ny < 50:
                    if pixels[nx, ny][3] > 127:
                        is_edge = True
                        break
            if is_edge:
                outline.append((x, y))
                
    for ox, oy in outline:
        pixels[ox, oy] = (25, 25, 25, 255)
        
    rgb_img = Image.new("RGB", (50, 50), (255, 255, 255))
    alpha = canvas.split()[3]
    rgb_img.paste(canvas, mask=alpha)
    
    quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=Image.NONE)
    final_img = quantized.convert("RGBA")
    final_pixels = final_img.load()
    
    for y in range(50):
        for x in range(50):
            orig_a = alpha.getpixel((x, y))
            r, g, b, _ = final_pixels[x, y]
            final_pixels[x, y] = (r, g, b, orig_a)
            
    return final_img

FOODS = [
    ("hotdog", "1f32d", "Twemoji Hot Dog", "Fast Food", "Sausage & Bun"),
    ("burrito", "1f32f", "Twemoji Burrito", "Meal", "Tortilla & Fillings"),
    ("pizza", "1f355", "Twemoji Pizza", "Fast Food", "Cheese & Dough"),
    ("meatonbone", "1f356", "Twemoji Meat on Bone", "Meal", "Meat"),
    ("poultryleg", "1f357", "Twemoji Poultry Leg", "Meal", "Meat"),
    ("spaghetti", "1f35d", "Twemoji Spaghetti", "Meal", "Pasta"),
    ("bread", "1f35e", "Twemoji Bread", "Meal", "Dough"),
    ("fries", "1f35f", "Twemoji French Fries", "Fast Food", "Potato"),
    ("sweetpotato", "1f360", "Twemoji Sweet Potato", "Vegetable", "Potato"),
    ("dango", "1f361", "Twemoji Dango", "Dessert", "Rice"),
    ("sushi", "1f363", "Twemoji Sushi", "Meal", "Fish & Rice"),
    ("friedshrimp", "1f364", "Twemoji Fried Shrimp", "Meal", "Shrimp"),
    ("fishcake", "1f365", "Twemoji Fish Cake", "Meal", "Fish"),
    ("icecream_soft", "1f366", "Twemoji Soft Ice Cream", "Dessert", "Cream"),
    ("shavedice", "1f367", "Twemoji Shaved Ice", "Dessert", "Ice & Syrup"),
    ("icecream", "1f368", "Twemoji Ice Cream", "Dessert", "Cream"),
    ("cookie", "1f36a", "Twemoji Cookie", "Dessert", "Dough"),
    ("chocolate", "1f36b", "Twemoji Chocolate", "Dessert", "Cocoa"),
    ("candy", "1f36c", "Twemoji Candy", "Dessert", "Sugar"),
    ("lollipop", "1f36d", "Twemoji Lollipop", "Dessert", "Sugar"),
    ("custard", "1f36e", "Twemoji Custard", "Dessert", "Egg & Milk"),
    ("honeypot", "1f36f", "Twemoji Honey Pot", "Dessert", "Honey"),
    ("shortcake", "1f370", "Twemoji Shortcake", "Dessert", "Cake"),
    ("croissant", "1f950", "Twemoji Croissant", "Breakfast", "Pastry"),
    ("avocado", "1f951", "Twemoji Avocado", "Fruit", "Avocado"),
    ("cucumber", "1f952", "Twemoji Cucumber", "Vegetable", "Cucumber"),
    ("bacon", "1f953", "Twemoji Bacon", "Breakfast", "Pork"),
    ("potato", "1f954", "Twemoji Potato", "Vegetable", "Potato"),
    ("carrot", "1f955", "Twemoji Carrot", "Vegetable", "Carrot"),
    ("baguette", "1f956", "Twemoji Baguette", "Meal", "Bread"),
    ("salad", "1f957", "Twemoji Green Salad", "Meal", "Greens"),
    ("egg", "1f95a", "Twemoji Egg", "Breakfast", "Egg"),
    ("milk", "1f95b", "Twemoji Milk", "Drink", "Dairy"),
    ("peanuts", "1f95c", "Twemoji Peanuts", "Snack", "Nuts"),
    ("kiwi", "1f95d", "Twemoji Kiwi", "Fruit", "Kiwi"),
    ("pancakes", "1f95e", "Twemoji Pancakes", "Breakfast", "Flour"),
    ("dumpling", "1f95f", "Twemoji Dumpling", "Meal", "Dough & Meat"),
    ("fortunecookie", "1f960", "Twemoji Fortune Cookie", "Dessert", "Dough"),
    ("takeoutbox", "1f961", "Twemoji Takeout Box", "Meal", "Various"),
    ("pie", "1f967", "Twemoji Pie", "Dessert", "Dough & Fruit"),
    ("pretzel", "1f968", "Twemoji Pretzel", "Snack", "Dough"),
    ("sandwich", "1f96a", "Twemoji Sandwich", "Meal", "Bread"),
    ("waffle", "1f9c7", "Twemoji Waffle", "Breakfast", "Batter"),
    ("butter", "1f9c8", "Twemoji Butter", "Ingredient", "Dairy"),
    ("garlic", "1f9c4", "Twemoji Garlic", "Vegetable", "Garlic"),
    ("onion", "1f9c5", "Twemoji Onion", "Vegetable", "Onion"),
    ("falafel", "1f9c6", "Twemoji Falafel", "Meal", "Chickpeas"),
    ("oyster", "1f9aa", "Twemoji Oyster", "Meal", "Seafood"),
    ("beverage", "1f9c3", "Twemoji Beverage Box", "Drink", "Juice")
]

if __name__ == "__main__":
    os.makedirs("images/food_desserts", exist_ok=True)
    successes = []
    
    for shortname, hexcode, name, type_cat, material in FOODS:
        url = f"https://raw.githubusercontent.com/jdecked/twemoji/master/assets/72x72/{hexcode}.png"
        out_path = f"images/food_desserts/twemoji_{shortname}_50x50.png"
        if os.path.exists(out_path):
            print(f"Skipping {shortname}, already exists at {out_path}")
            successes.append({
                "id": f"food_twemoji_{shortname}",
                "name": name,
                "filename": out_path,
                "category": "food_desserts",
                "type": type_cat,
                "material": material,
                "rarity": "★★★☆☆",
                "description": f"A beautiful {name.lower()} icon converted from Twemoji."
            })
            continue

        temp_path = f"temp_{shortname}.png"
        try:
            urllib.request.urlretrieve(url, temp_path)
            img = Image.open(temp_path).convert("RGBA")
            new_art = add_outline_and_quantize(img)
            
            new_art.save(out_path)
            print(f"Saved {out_path}")
            
            successes.append({
                "id": f"food_twemoji_{shortname}",
                "name": name,
                "filename": out_path,
                "category": "food_desserts",
                "type": type_cat,
                "material": material,
                "rarity": "★★★☆☆",
                "description": f"A beautiful {name.lower()} icon converted from Twemoji."
            })
            os.remove(temp_path)
        except Exception as e:
            print(f"Skipped {shortname}: {e}")
            
    # Inject into app.js
    app_js_path = "app.js"
    with open(app_js_path, "r") as f:
        content = f.read()
        
    # Prevent duplicate injections if running in a new session with an already updated app.js
    if "food_twemoji_hamburger" in content or "food_twemoji_hotdog" in content:
        print("Entries already exist in app.js. Skipping injection to avoid duplicates.")
    else:
        # We want to insert just before '];' at the end of the foodDesserts array
        target = '    { id: "food_twemoji_donut", name: "Twemoji Donut", filename: "images/food_desserts/twemoji_donut_50x50.png", category: "food_desserts", type: "Dessert", material: "Twemoji", rarity: "★★★☆☆", description: "A sweet glazed donut icon converted from Twemoji." }\\n];'
        if target in content:
            js_entries = []
            for s in successes:
                entry = f'    {{ id: "{s["id"]}", name: "{s["name"]}", filename: "{s["filename"]}", category: "{s["category"]}", type: "{s["type"]}", material: "{s["material"]}", rarity: "{s["rarity"]}", description: "{s["description"]}" }}'
                js_entries.append(entry)
                
            insertion = '    { id: "food_twemoji_donut", name: "Twemoji Donut", filename: "images/food_desserts/twemoji_donut_50x50.png", category: "food_desserts", type: "Dessert", material: "Twemoji", rarity: "★★★☆☆", description: "A sweet glazed donut icon converted from Twemoji." },\\n' + ",\\n".join(js_entries) + "\\n];"
            content = content.replace(target, insertion)
            
            with open(app_js_path, "w") as f:
                f.write(content)
            print(f"Injected {len(successes)} items into app.js!")
        else:
            print("Failed to find insertion point in app.js")

