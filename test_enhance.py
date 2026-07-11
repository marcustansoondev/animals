from PIL import Image, ImageDraw
import random
import os

def apply_realistic_detail(filepath):
    img = Image.open(filepath).convert("RGBA")
    r, g, b, a = img.split()
    
    # Create a noise texture for metallic/matte surface detail
    noise_img = Image.new("RGBA", (50, 50), (0,0,0,0))
    noise_data = []
    
    # Simple scanline / noise combo
    for y in range(50):
        for x in range(50):
            # scanline effect on every other row, slightly darkens
            # noise random bright/dark
            val = random.randint(-15, 15)
            if y % 2 == 0:
                val -= 10
            # just some alpha noise
            noise_data.append((0, 0, 0, max(0, min(255, abs(val) * 2))))
            
    noise_img.putdata(noise_data)
    
    # Apply noise only where original image is opaque (or somewhat opaque)
    mask = a.point(lambda p: p if p > 0 else 0)
    
    combined = Image.alpha_composite(img, noise_img)
    
    # Add a border / edge highlight for realism
    draw = ImageDraw.Draw(combined)
    draw.rectangle([1, 1, 48, 48], outline=(255, 255, 255, 30))
    
    # Quantize back to 9 colors
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    flat.paste(combined, mask=mask)
    q = flat.quantize(colors=9, method=Image.MEDIANCUT)
    final = q.convert("RGBA")
    
    # Restore transparency
    data = final.getdata()
    alpha_data = mask.getdata()
    new_data = []
    for i in range(len(data)):
        if alpha_data[i] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((data[i][0], data[i][1], data[i][2], alpha_data[i]))
    final.putdata(new_data)
    
    final.save("test_enhanced.png")
    
    # Check color count
    colors = final.getcolors(maxcolors=256)
    print(f"Colors after enhancement: {len(colors)}")

apply_realistic_detail("images/electronics/smart_door_sensor.png")
