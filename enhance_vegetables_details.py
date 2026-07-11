import os
import glob
from PIL import Image, ImageFilter
import numpy as np

def apply_realistic_lighting(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist")
        return
        
    try:
        # Load image and ensure RGBA
        img = Image.open(filepath).convert("RGBA")
        data = np.array(img).astype(float)
        
        # Extract alpha channel
        alpha = data[:, :, 3].copy()
        alpha_mask = alpha > 128
        
        if not np.any(alpha_mask):
            return
            
        h, w = alpha_mask.shape
        
        # Identify the black outline (thick border)
        is_black = (data[:, :, 0] < 20) & (data[:, :, 1] < 20) & (data[:, :, 2] < 20) & alpha_mask
        
        # We will apply lighting to non-black colored pixels
        colored_mask = alpha_mask & (~is_black)
        
        # Generate lighting maps
        # 1. Shadow map: Shift colored mask bottom-right
        shadow_mask = np.zeros((h, w), dtype=bool)
        shifted_up = np.roll(colored_mask, -2, axis=0)
        shifted_left = np.roll(colored_mask, -2, axis=1)
        # pixels that are colored, but if we shift them they hit black/transparent, 
        # meaning they are at the bottom-right edges
        shadow_mask = colored_mask & ~(shifted_up & shifted_left)
        
        # 2. Highlight map: Shift colored mask top-left
        highlight_mask = np.zeros((h, w), dtype=bool)
        shifted_down = np.roll(colored_mask, 2, axis=0)
        shifted_right = np.roll(colored_mask, 2, axis=1)
        highlight_mask = colored_mask & ~(shifted_down & shifted_right)
        
        # Apply lighting
        # Multiply shadows by 0.6
        data[shadow_mask, 0] = np.clip(data[shadow_mask, 0] * 0.6, 0, 255)
        data[shadow_mask, 1] = np.clip(data[shadow_mask, 1] * 0.6, 0, 255)
        data[shadow_mask, 2] = np.clip(data[shadow_mask, 2] * 0.6, 0, 255)
        
        # Add highlight by blending with white
        data[highlight_mask, 0] = np.clip(data[highlight_mask, 0] + (255 - data[highlight_mask, 0]) * 0.4, 0, 255)
        data[highlight_mask, 1] = np.clip(data[highlight_mask, 1] + (255 - data[highlight_mask, 1]) * 0.4, 0, 255)
        data[highlight_mask, 2] = np.clip(data[highlight_mask, 2] + (255 - data[highlight_mask, 2]) * 0.4, 0, 255)
        
        # Recreate image
        enhanced_img = Image.fromarray(data.astype(np.uint8), "RGBA")
        
        # Create a clean flat RGB image for quantization
        rgb_img = Image.new("RGB", enhanced_img.size, (255, 255, 255))
        rgb_img.paste(enhanced_img, mask=Image.fromarray(alpha.astype(np.uint8), "L"))
        
        # Quantize without dithering to keep colors solid and clean
        quantized = rgb_img.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
        
        # Convert back to RGBA and re-apply alpha
        final_img = quantized.convert("RGBA")
        final_data = np.array(final_img)
        
        # Restore transparency
        final_data[:, :, 3] = alpha.astype(np.uint8)
        
        # Save back
        Image.fromarray(final_data, "RGBA").save(filepath)
    except Exception as e:
        print(f"Error enhancing {filepath}: {e}")

if __name__ == "__main__":
    print("Applying realistic lighting details (highlights & shadows, <= 10 colors) to all vegetables...")
    
    files = glob.glob("images/vegetables/*_50x50.png")
    for filepath in files:
        apply_realistic_lighting(filepath)
        
    print(f"Successfully added realistic details to {len(files)} vegetables.")
