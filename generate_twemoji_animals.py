import os
import glob
import unicodedata
from PIL import Image

def get_hex_from_char(c):
    return hex(ord(c))[2:]

# Manual overrides for tricky animal names or missing emojis
OVERRIDES = {
    "bee": "HONEYBEE",
    "squirrel": "CHIPMUNK",
    "hippo": "HIPPOPOTAMUS",
    "rhino": "RHINOCEROS",
    "cheetah": "LEOPARD",
    "panther": "LEOPARD",
    "jaguar": "LEOPARD",
    "alpaca": "LLAMA",
    "yak": "WATER BUFFALO",
    "bison": "WATER BUFFALO",
    "sea_lion": "SEAL",
    "manatee": "SEAL",
    "dugong": "SEAL",
    "beluga": "WHALE",
    "orca": "SPOUTING WHALE",
    "narwhal": "WHALE",
    "stingray": "FISH",
    "jellyfish": "SQUID",
    "seahorse": "FISH",
    "starfish": "GLOWING STAR",
    "cuttlefish": "SQUID",
    "eel": "SNAKE",
    "gecko": "LIZARD",
    "komodo_dragon": "LIZARD",
    "salamander": "LIZARD",
    "toad": "FROG",
    "centipede": "BUG",
    "dragonfly": "BUTTERFLY",
    "grasshopper": "CRICKET",
    "mantis": "CRICKET",
    "firefly": "BUG",
    "echidna": "HEDGEHOG",
    "alligator": "CROCODILE",
    "mongoose": "BADGER",
    "meerkat": "BADGER",
    "wombat": "BEAR",
    "quokka": "BEAR",
    "tasmanian_devil": "WOLF",
    "anteater": "BADGER",
    "pangolin": "LIZARD",
    "tapir": "BOAR",
    "okapi": "HORSE",
    "hyena": "WOLF",
    "mole": "BADGER",
    "bandicoot": "RAT",
    "porcupine": "HEDGEHOG",
    "gopher": "HAMSTER",
    "groundhog": "BEAVER",
    "prairie_dog": "HAMSTER",
    "manta_ray": "FISH",
    "pelican": "BIRD",
    "puffin": "BIRD",
    "ostrich": "BIRD",
    "swan": "SWAN",
    "goose": "SWAN",
    "shrimp": "SHRIMP",
    "lobster": "LOBSTER",
    "crab": "CRAB",
    "spider": "SPIDER",
    "ladybug": "LADY BEETLE",
    "beetle": "LADY BEETLE"
}

def get_emoji_hex(animal_name):
    query = OVERRIDES.get(animal_name, animal_name.replace("_", " ")).upper()
    
    char = None
    for suffix in ["", " FACE", " HEAD"]:
        try:
            char = unicodedata.lookup(query + suffix)
            break
        except KeyError:
            continue
            
    if char:
        return get_hex_from_char(char)
    return "1f43e" # Paw prints as ultimate fallback

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
        
    # Quantize to 10 colors
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

def main():
    files = glob.glob("images/animals/*_50x50.png")
    
    for f in files:
        basename = os.path.basename(f)
        animal = basename.replace("_50x50.png", "")
        
        hexcode = get_emoji_hex(animal)
        emoji_path = f"twemoji-14.0.2/assets/72x72/{hexcode}.png"
        
        if not os.path.exists(emoji_path):
            print(f"Warning: Twemoji not found for {animal} (hex: {hexcode}). Using paw prints.")
            emoji_path = "twemoji-14.0.2/assets/72x72/1f43e.png"
            
        try:
            emoji_img = Image.open(emoji_path).convert("RGBA")
            new_art = add_outline_and_quantize(emoji_img)
            new_art.save(f)
            print(f"Generated completely new art for {animal}")
        except Exception as e:
            print(f"Error processing {animal}: {e}")

if __name__ == "__main__":
    main()
