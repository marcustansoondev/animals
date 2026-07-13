import os
import random
from PIL import Image, ImageDraw
import numpy as np

# reuse enhance_weather_image function from the enhancement script
from enhance_weather import enhance_weather_image

OUTPUT_DIR = "images/weather"
os.makedirs(OUTPUT_DIR, exist_ok=True)

js_objects = []

for i in range(1, 101):
    # Transparent background
    img = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    bg_choice = random.choice(["clear", "cloudy", "night", "stormy", "sunset", "windy"])
    weather_type = "Variant"
    desc = f"A unique weather variant #{i}."
    
    # 1. Background / Primary Celestial object
    if bg_choice == "clear":
        cx, cy = random.randint(15, 35), random.randint(15, 30)
        r = random.randint(10, 14)
        sun_color = random.choice([(255, 220, 0), (255, 200, 50), (255, 180, 0)])
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=sun_color)
        # rays
        for ray in range(8):
            draw.line([cx, cy, cx+random.randint(-20, 20), cy+random.randint(-20, 20)], fill=sun_color, width=3)
        # redraw core
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=sun_color)
        weather_type = "Sunny"
    elif bg_choice == "night":
        cx, cy = random.randint(15, 35), random.randint(15, 30)
        r = random.randint(10, 14)
        moon_color = random.choice([(220, 220, 255), (255, 255, 200), (200, 200, 200)])
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=moon_color)
        # make it a crescent occasionally
        if random.random() > 0.5:
            draw.ellipse([cx-r+4, cy-r-4, cx+r+4, cy+r-4], fill=(0,0,0,0))
        weather_type = "Clear"
    elif bg_choice == "sunset":
        cx, cy = random.randint(15, 35), random.randint(35, 45)
        r = random.randint(12, 18)
        sun_color = random.choice([(255, 100, 50), (255, 150, 50), (255, 50, 50)])
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=sun_color)
        weather_type = "Sunny"
        
    # 2. Clouds
    if random.random() > 0.4 or bg_choice in ["cloudy", "stormy", "windy"]:
        num_clouds = random.randint(1, 3)
        for _ in range(num_clouds):
            cx, cy = random.randint(15, 35), random.randint(15, 35)
            if bg_choice == "stormy":
                c_color = random.choice([(100, 100, 100), (80, 80, 80), (120, 120, 120)])
            elif bg_choice == "sunset":
                c_color = random.choice([(255, 150, 150), (200, 100, 150)])
            else:
                c_color = random.choice([(255, 255, 255), (230, 230, 230), (200, 200, 200)])
                
            draw.ellipse([cx-12, cy-6, cx+12, cy+6], fill=c_color)
            draw.ellipse([cx-6, cy-12, cx+6, cy], fill=c_color)
            draw.ellipse([cx-16, cy-3, cx-4, cy+6], fill=c_color)
            draw.ellipse([cx+4, cy-3, cx+16, cy+6], fill=c_color)
        
        if bg_choice in ["cloudy", "windy"]:
            weather_type = "Cloudy"
    
    # 3. Precipitation / Effects
    if bg_choice == "stormy" or random.random() > 0.7:
        precip = random.choice(["rain", "snow", "lightning", "rainbow"])
        if precip == "rain":
            rain_color = random.choice([(100, 150, 255), (50, 100, 255), (150, 200, 255)])
            for _ in range(random.randint(6, 12)):
                rx, ry = random.randint(5, 45), random.randint(25, 45)
                draw.line([rx, ry, rx-3, ry+6], fill=rain_color, width=2)
            weather_type = "Rainy"
        elif precip == "snow":
            for _ in range(random.randint(5, 10)):
                sx, sy = random.randint(5, 45), random.randint(20, 45)
                # Draw small chunkier cross
                draw.line([sx-2, sy, sx+2, sy], fill=(255, 255, 255), width=2)
                draw.line([sx, sy-2, sx, sy+2], fill=(255, 255, 255), width=2)
            weather_type = "Snowy"
        elif precip == "lightning":
            lx = random.randint(15, 35)
            ly = random.randint(15, 25)
            l_color = random.choice([(255, 255, 0), (255, 255, 150), (200, 255, 0)])
            draw.polygon([lx, ly, lx-6, ly+12, lx+3, ly+12, lx-3, ly+28, lx+8, ly+10, lx-1, ly+10], fill=l_color)
            weather_type = "Stormy"
        elif precip == "rainbow" and bg_choice not in ["night", "stormy"]:
            for r, c in zip([25, 22, 19, 16], [(255,0,0), (255,165,0), (255,255,0), (0,255,0)]):
                draw.arc([-r+25, -r+25, r+25, r+25], start=180, end=0, fill=c, width=3)
            weather_type = "Sunny"
            
    # Save base image
    filepath = f"{OUTPUT_DIR}/variant_weather_{i}_50x50.png"
    img.save(filepath)
    
    # Re-use our kid-friendly 10-color enhancement script logic to perfectly process it!
    enhance_weather_image(filepath)
    
    # Generate the JS object line
    js_objects.append(f'    {{ id: "variant_weather_{i}", name: "Weather Variant {i}", filename: "{filepath}", category: "weather", type: "{weather_type}", material: "Various", rarity: "★☆☆☆☆", description: "{desc}" }},')

with open("variants_app.js", "w") as f:
    f.write("\n".join(js_objects))

print(f"Generated 100 weather variants successfully and saved JS data to variants_app.js")
