with open("variants_app.js", "r") as f:
    variants = f.read()
    
with open("app.js", "r") as f:
    content = f.read()
    
target = '    { id: "morning_dew", name: "Morning Dew", filename: "images/weather/morning_dew_50x50.png", category: "weather", type: "Clear", material: "Water Droplets", rarity: "★★☆☆☆", description: "Tiny, pristine drops of morning dew sparkling on a green leaf." }'
replacement = target + ",\n" + variants

if target in content:
    content = content.replace(target, replacement)
    with open("app.js", "w") as f:
        f.write(content)
    print("Successfully injected variants into app.js")
else:
    print("Could not find target string in app.js")
