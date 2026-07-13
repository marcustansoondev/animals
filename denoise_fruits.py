"""
denoise_fruits.py
=================
Removes noisy "sprinkle" pixels from all 50x50 fruit sprites.
Each isolated pixel (one that differs from ALL its 4-connected neighbors)
is replaced with its most common neighbor color. Runs 3 passes for
thorough cleaning, then re-quantizes all images to <= 9 opaque colors
(no dithering, no outlines).

This ensures all fruit images have clean solid color regions suitable
for a kids' pixel coloring game.
"""

import os
import glob
from collections import Counter
from PIL import Image
import numpy as np

OUTPUT_DIR = "images/fruits"


def denoise_image(filepath):
    """Replace isolated pixels with their most common neighbor color."""
    img = Image.open(filepath).convert("RGBA")
    arr = np.array(img).copy()
    alpha = arr[:, :, 3]
    h, w = alpha.shape

    changed = 0
    passes = 3
    for _ in range(passes):
        new_arr = arr.copy()
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if alpha[y, x] <= 128:
                    continue
                px = tuple(arr[y, x, :3])
                neighbors = []
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1),
                               (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and alpha[ny, nx] > 128:
                        neighbors.append(tuple(arr[ny, nx, :3]))
                if not neighbors:
                    continue
                n4 = []
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and alpha[ny, nx] > 128:
                        n4.append(tuple(arr[ny, nx, :3]))
                if n4 and all(n != px for n in n4):
                    most_common = Counter(neighbors).most_common(1)[0][0]
                    new_arr[y, x, :3] = most_common
                    changed += 1
        arr = new_arr

    final = Image.fromarray(arr, "RGBA")
    final.save(filepath)
    return changed


def quantize_no_outline(filepath):
    """Quantize to <=9 opaque colors, no dither, no outline."""
    img = Image.open(filepath).convert("RGBA")
    arr = np.array(img)
    alpha = arr[:, :, 3]
    new_alpha = alpha.copy()
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    composed = Image.fromarray(
        np.dstack((arr[:, :, :3], new_alpha)).astype(np.uint8), "RGBA"
    )
    flat.paste(composed, mask=Image.fromarray(new_alpha, "L"))
    q = flat.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
    final = q.convert("RGBA")
    fa = np.array(final)
    fa[:, :, 3] = new_alpha
    Image.fromarray(fa, "RGBA").save(filepath)


def main():
    files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*_50x50.png")))
    print(f"De-noising {len(files)} fruit images...")
    total_changed = 0
    for f in files:
        name = os.path.basename(f).replace("_50x50.png", "")
        c = denoise_image(f)
        if c > 0:
            print(f"  ✓ {name}: {c} noisy pixels cleaned")
            total_changed += c

    print(f"\nTotal pixels cleaned: {total_changed}")

    print("\nRe-quantizing all images...")
    for f in files:
        quantize_no_outline(f)

    # Verify
    print("\nVerification:")
    all_ok = True
    for f in files:
        name = os.path.basename(f).replace("_50x50.png", "")
        img = Image.open(f).convert("RGBA")
        arr = np.array(img)
        mask = arr[:, :, 3] > 128
        if mask.any():
            colors = set(map(tuple, arr[mask][:, :3]))
            nc = len(colors)
        else:
            nc = 0
        if nc > 10:
            print(f"  ⚠️ {name}: {nc} colors")
            all_ok = False

    if all_ok:
        print("  ✓ All images ≤ 10 colors")
    print("Done!")


if __name__ == "__main__":
    main()
