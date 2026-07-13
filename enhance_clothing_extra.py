import os
import glob
from PIL import Image
import numpy as np
import generate_clothing_extra

def enhance_image(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        return
    try:
        # Load image and ensure RGBA
        img = Image.open(filepath).convert("RGBA")
        data = np.array(img).astype(float)
        
        # Extract alpha channel
        alpha = data[:, :, 3].copy()
        
        # Mask of non-transparent pixels
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
            
        # --- Realistic 3D Detail & Shading (Cell-Shaded for Coloring Game) ---
        rgb_data = data[:, :, :3].copy()
        
        # 1. Directional Lighting (Top-Left Highlight, Bottom-Right Shadow)
        y, x = np.mgrid[0:h, 0:w]
        dist = np.sqrt((x - 10)**2 + (y - 10)**2)
        light_factor = 1.0 - (dist / 70.0)
        
        # Use discrete steps for lighting to avoid smooth gradients/noise
        light_factor = np.round(light_factor * 4) / 4.0
        light_multiplier = 0.7 + (light_factor * 0.6)
        
        # 2. Ambient Occlusion (Inner shadows)
        neighbors = np.zeros((h, w), dtype=float)
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0: continue
                shifted = np.roll(alpha_data, dy, axis=0)
                shifted = np.roll(shifted, dx, axis=1)
                if dy == 1: shifted[0, :] = False
                if dy == -1: shifted[-1, :] = False
                if dx == 1: shifted[:, 0] = False
                if dx == -1: shifted[:, -1] = False
                neighbors += shifted.astype(float)
                
        ao_factor = neighbors / 8.0
        # Discretize AO to keep shapes solid and clean
        ao_factor = np.round(ao_factor * 2) / 2.0
        ao_multiplier = 0.85 + (ao_factor * 0.3)
        
        # Apply multipliers to the interior active area
        active_area = alpha_data & (~outline)
        for c in range(3):
            channel = rgb_data[:, :, c]
            modified = channel * light_multiplier * ao_multiplier
            channel[active_area] = np.clip(modified[active_area], 0, 255)
            rgb_data[:, :, c] = channel
            
        # Set outline pixels to black
        rgb_data[outline, 0] = 0
        rgb_data[outline, 1] = 0
        rgb_data[outline, 2] = 0
        
        # Update alpha since we added an outline
        new_alpha = alpha.copy()
        new_alpha[outline] = 255
        new_alpha_uint8 = new_alpha.astype(np.uint8)
        
        # Recreate image
        enhanced_img = Image.fromarray(np.dstack((rgb_data, new_alpha_uint8)).astype(np.uint8), "RGBA")
        
        # Create a clean flat RGB image
        rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
        rgb_img.paste(enhanced_img, mask=Image.fromarray(new_alpha_uint8, "L"))
        
        # Quantize strictly to 9 colors (well below 10) for retro pixel-art consistency
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

def main():
    count = 0
    for name in generate_clothing_extra.DRAWINGS.keys():
        f = f"images/clothing/{name}_50x50.png"
        if os.path.exists(f):
            enhance_image(f)
            count += 1
    print(f"Added realistic 3D shading, texture, and pixel coloring art outline to {count} extra clothing images (colors <= 10).")

if __name__ == "__main__":
    main()
