import os
import numpy as np
from PIL import Image

import generate_electronics2
import generate_electronics3

def apply_clean_coloring_detail(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist")
        return
        
    try:
        # Load image and ensure RGBA
        img = Image.open(filepath).convert("RGBA")
        data = np.array(img).astype(float)
        
        # Extract alpha channel
        alpha = data[:, :, 3].copy()
        
        # Mask of non-transparent pixels (using 128 as threshold)
        alpha_data = alpha > 128
        
        if not np.any(alpha_data):
            return
            
        h, w = alpha_data.shape
        outline = np.zeros((h, w), dtype=bool)
        
        # Thicker outline for coloring art (cardinal directions)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            shifted = np.roll(alpha_data, dy, axis=0)
            shifted = np.roll(shifted, dx, axis=1)
            if dy == 1: shifted[0, :] = False
            if dy == -1: shifted[-1, :] = False
            if dx == 1: shifted[:, 0] = False
            if dx == -1: shifted[:, -1] = False
            
            outline = outline | ((~alpha_data) & shifted)
            
        # Set outline pixels to black
        data[outline, 0] = 0
        data[outline, 1] = 0
        data[outline, 2] = 0
        data[outline, 3] = 255
        
        # Update alpha since we added an outline
        new_alpha = alpha.copy()
        new_alpha[outline] = 255
        new_alpha_uint8 = new_alpha.astype(np.uint8)
        
        # Recreate image
        enhanced_img = Image.fromarray(data.astype(np.uint8), "RGBA")
        
        # Create a clean flat RGB image
        rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
        rgb_img.paste(enhanced_img, mask=Image.fromarray(new_alpha_uint8, "L"))
        
        # Quantize without dithering to keep colors solid and clean
        quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
        
        # Convert back to RGBA and re-apply alpha
        final_img = quantized.convert("RGBA")
        final_data = np.array(final_img)
        
        # Restore transparency
        final_data[:, :, 3] = new_alpha_uint8
        
        # Save back
        Image.fromarray(final_data, "RGBA").save(filepath)
    except Exception as e:
        print(f"Error enhancing {filepath}: {e}")

if __name__ == "__main__":
    print("Applying clean pixel coloring details (solid colors, black outlines) to batch 2 and batch 3 electronics...")
    
    # Get all names
    names = list(generate_electronics2.DRAWINGS.keys()) + list(generate_electronics3.DRAWINGS.keys())
    
    for name in names:
        filepath = f"images/electronics/{name}_50x50.png"
        apply_clean_coloring_detail(filepath)
        
    print(f"Successfully added clean pixel coloring details to {len(names)} electronics items.")
