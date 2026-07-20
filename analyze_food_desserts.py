"""Analyze all 50x50 food & dessert sprites: color count, noise level, and quality."""
import os
import numpy as np
from PIL import Image

IMG_DIR = "images/food_desserts"
files = sorted([f for f in os.listdir(IMG_DIR) if f.endswith("_50x50.png")])

print(f"Total food & dessert 50x50 sprites: {len(files)}")
print("=" * 80)

issues = []
good = []

for fname in files:
    path = os.path.join(IMG_DIR, fname)
    img = Image.open(path).convert("RGBA")
    arr = np.array(img)
    
    # Count unique opaque colors
    opaque_mask = arr[:, :, 3] > 0
    opaque_pixels = arr[opaque_mask]
    if len(opaque_pixels) == 0:
        issues.append((fname, 0, 0, 0, "EMPTY - no opaque pixels"))
        continue
    
    unique_colors = set()
    for pixel in opaque_pixels:
        unique_colors.add(tuple(pixel[:3]))
    color_count = len(unique_colors)
    
    # Count opaque pixel count (fill ratio)
    total_opaque = opaque_mask.sum()
    fill_ratio = total_opaque / (50 * 50) * 100
    
    # Measure noise: count how many pixels have a color that appears less than
    # 1% of total opaque pixels (isolated/noise colors)
    from collections import Counter
    color_freq = Counter()
    for pixel in opaque_pixels:
        color_freq[tuple(pixel[:3])] += 1
    
    noise_threshold = max(2, total_opaque * 0.005)  # 0.5% or at least 2 pixels
    noise_colors = sum(1 for c, cnt in color_freq.items() if cnt < noise_threshold)
    noise_pixels = sum(cnt for c, cnt in color_freq.items() if cnt < noise_threshold)
    noise_ratio = noise_pixels / total_opaque * 100 if total_opaque > 0 else 0
    
    # Determine issue
    issue_parts = []
    if color_count > 10:
        issue_parts.append(f"TOO MANY COLORS ({color_count})")
    if noise_ratio > 15:
        issue_parts.append(f"NOISY ({noise_ratio:.1f}% noise pixels)")
    if fill_ratio < 15:
        issue_parts.append(f"TOO SPARSE ({fill_ratio:.1f}% fill)")
    if total_opaque < 200:
        issue_parts.append(f"VERY SMALL ({total_opaque} opaque px)")
    
    name = fname.replace("_50x50.png", "")
    
    if issue_parts:
        issues.append((name, color_count, fill_ratio, noise_ratio, " | ".join(issue_parts)))
    else:
        good.append((name, color_count, fill_ratio, noise_ratio))

print(f"\n{'='*80}")
print(f"SPRITES WITH ISSUES ({len(issues)}):")
print(f"{'='*80}")
for name, cc, fr, nr, issue in sorted(issues, key=lambda x: x[1], reverse=True):
    print(f"  {name:30s} colors={cc:3d} fill={fr:5.1f}% noise={nr:5.1f}% -> {issue}")

print(f"\n{'='*80}")
print(f"GOOD SPRITES ({len(good)}):")
print(f"{'='*80}")
for name, cc, fr, nr in sorted(good, key=lambda x: x[1], reverse=True):
    print(f"  {name:30s} colors={cc:3d} fill={fr:5.1f}% noise={nr:5.1f}%")

print(f"\n{'='*80}")
print(f"SUMMARY: {len(good)} good, {len(issues)} with issues, {len(files)} total")
print(f"{'='*80}")
