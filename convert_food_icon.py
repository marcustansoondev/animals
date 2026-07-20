import urllib.request
from PIL import Image
import os

def add_outline_and_quantize(emoji_img):
    # Resize emoji to fit nicely
    emoji_img = emoji_img.resize((40, 40), Image.Resampling.NEAREST)
    
    # Create 50x50 canvas
    canvas = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    canvas.paste(emoji_img, (5, 5))
    
    pixels = canvas.load()
    
    # Clean up noisy anti-aliased alpha to make edges perfectly solid
    for y in range(50):
        for x in range(50):
            r, g, b, a = pixels[x, y]
            if a > 127:
                pixels[x, y] = (r, g, b, 255)
            else:
                pixels[x, y] = (0, 0, 0, 0)
    
    # Create crisp pixel-art outline using 4-neighbor connectivity
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
        pixels[ox, oy] = (25, 25, 25, 255) # Clean dark outline
        
    # Quantize to 10 colors (using 9 colors + transparent)
    rgb_img = Image.new("RGB", (50, 50), (255, 255, 255))
    alpha = canvas.split()[3]
    rgb_img.paste(canvas, mask=alpha)
    
    quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=Image.NONE)
    
    final_img = quantized.convert("RGBA")
    final_pixels = final_img.load()
    
    # Restore exact alpha transparency (including new outline)
    for y in range(50):
        for x in range(50):
            orig_a = alpha.getpixel((x, y))
            r, g, b, _ = final_pixels[x, y]
            final_pixels[x, y] = (r, g, b, orig_a)
            
    return final_img

def process_icon(name, hexcode):
    url = f"https://raw.githubusercontent.com/jdecked/twemoji/master/assets/72x72/{hexcode}.png"
    print(f"Downloading {name} from {url}...")
    
    try:
        temp_path = f"temp_{name}.png"
        urllib.request.urlretrieve(url, temp_path)
        
        img = Image.open(temp_path).convert("RGBA")
        new_art = add_outline_and_quantize(img)
        
        out_path = f"images/food_desserts/{name}_50x50.png"
        new_art.save(out_path)
        print(f"Successfully saved to {out_path}")
        
        # Cleanup temp file
        os.remove(temp_path)
    except Exception as e:
        print(f"Failed to process {name}: {e}")

if __name__ == "__main__":
    # Ensure directory exists
    os.makedirs("images/food_desserts", exist_ok=True)
    
    icons = [
        ("twemoji_hamburger", "1f354"),
        ("twemoji_bentobox", "1f371"),
        ("twemoji_taco", "1f32e"),
        ("twemoji_donut", "1f369")
    ]
    
    for name, hexcode in icons:
        process_icon(name, hexcode)
