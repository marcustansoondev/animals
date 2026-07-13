import os
import glob
from PIL import Image
import numpy as np

def enhance_weather_image(filepath):
    try:
        # Load image and ensure RGBA
        img = Image.open(filepath).convert("RGBA")
        data = np.array(img).astype(float)
        
        # Extract alpha channel
        alpha = data[:, :, 3].copy()
        alpha_data = alpha > 128
        
        if not np.any(alpha_data):
            return
            
        h, w = alpha_data.shape
        
        # 1. NOISE REDUCTION / THICKENING
        # To make it easier for kids to color, we dilate the alpha to make thin lines (like rain) thicker
        # and eliminate tiny 1px gaps.
        dilated_alpha = alpha_data.copy()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            shifted = np.roll(alpha_data, dy, axis=0)
            shifted = np.roll(shifted, dx, axis=1)
            if dy == 1: shifted[0, :] = False
            if dy == -1: shifted[-1, :] = False
            if dx == 1: shifted[:, 0] = False
            if dx == -1: shifted[:, -1] = False
            dilated_alpha = dilated_alpha | shifted
            
        # 2. CREATE THICK BLACK OUTLINE
        # Now find the outline of the DILATED alpha
        outline = np.zeros((h, w), dtype=bool)
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            shifted = np.roll(dilated_alpha, dy, axis=0)
            shifted = np.roll(shifted, dx, axis=1)
            if dy == 1: shifted[0, :] = False
            if dy == -1: shifted[-1, :] = False
            if dx == 1: shifted[:, 0] = False
            if dx == -1: shifted[:, -1] = False
            # Outline is where it is outside the dilated alpha, but neighbors the dilated alpha
            outline = outline | ((~dilated_alpha) & shifted)
            
        # 3. APPLY OUTLINE & SOLIDIFY ALPHA
        final_alpha = alpha_data | outline
        
        # Set outline pixels to black
        data[outline, 0] = 0
        data[outline, 1] = 0
        data[outline, 2] = 0
        data[outline, 3] = 255
        
        # Update alpha
        new_alpha = np.zeros((h, w), dtype=np.uint8)
        new_alpha[final_alpha] = 255
        
        # Recreate image
        enhanced_img = Image.fromarray(data.astype(np.uint8), "RGBA")
        
        # Create a clean flat RGB image for quantization
        rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
        rgb_img.paste(enhanced_img, mask=Image.fromarray(new_alpha, "L"))
        
        # Quantize without dithering to keep colors solid and clean (max 9 colors + transparent = 10)
        quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
        
        # Convert back to RGBA and re-apply alpha
        final_img = quantized.convert("RGBA")
        final_data = np.array(final_img)
        
        # Restore transparency
        final_data[:, :, 3] = new_alpha
        
        # Save back over the original image
        Image.fromarray(final_data, "RGBA").save(filepath)
    except Exception as e:
        print(f"Error enhancing {filepath}: {e}")

def main():
    files = glob.glob("images/weather/*_50x50.png")
    for f in files:
        enhance_weather_image(f)
    print(f"Enhanced {len(files)} weather images for pixel coloring art (thick outlines, flat colors).")

if __name__ == "__main__":
    main()
