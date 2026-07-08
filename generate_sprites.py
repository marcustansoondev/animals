import os
from PIL import Image, ImageDraw

def generate_all_sprites():
    def get_canvas():
        return Image.new("RGBA", (50, 50), (255, 255, 255, 0))

    def save_sprite(name, img):
        img.save(f"images/animals/{name}_50x50.png")
        print(f"Generated images/animals/{name}_50x50.png")

    # 1. DEER
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head & ears
    draw.ellipse([14, 18, 36, 40], fill=(150, 95, 55))
    draw.polygon([14, 20, 6, 12, 12, 22], fill=(150, 95, 55))
    draw.polygon([36, 20, 44, 12, 38, 22], fill=(150, 95, 55))
    # Antlers
    draw.line([18, 18, 12, 6], fill=(210, 195, 175), width=2)
    draw.line([12, 6, 6, 8], fill=(210, 195, 175), width=2)
    draw.line([12, 6, 12, 2], fill=(210, 195, 175), width=2)
    draw.line([32, 18, 38, 6], fill=(210, 195, 175), width=2)
    draw.line([38, 6, 44, 8], fill=(210, 195, 175), width=2)
    draw.line([38, 6, 38, 2], fill=(210, 195, 175), width=2)
    # White spots
    draw.rectangle([20, 20, 21, 21], fill=(255, 255, 255))
    draw.rectangle([29, 20, 30, 21], fill=(255, 255, 255))
    draw.rectangle([25, 23, 26, 24], fill=(255, 255, 255))
    # Muzzle & eyes
    draw.ellipse([19, 29, 31, 39], fill=(235, 210, 185))
    draw.ellipse([23, 29, 27, 32], fill=(25, 25, 25))
    draw.rectangle([18, 24, 20, 26], fill=(25, 25, 25))
    draw.rectangle([30, 24, 32, 26], fill=(25, 25, 25))
    save_sprite("deer", img)

    # 2. WOLF
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head & pointy ears
    draw.polygon([12, 18, 6, 4, 18, 18], fill=(110, 115, 125))
    draw.polygon([38, 18, 44, 4, 32, 18], fill=(110, 115, 125))
    draw.polygon([9, 14, 7, 6, 15, 16], fill=(245, 180, 190))
    draw.polygon([41, 14, 43, 6, 35, 16], fill=(245, 180, 190))
    draw.ellipse([12, 16, 38, 42], fill=(110, 115, 125))
    # White cheeks
    draw.ellipse([12, 26, 24, 38], fill=(240, 240, 245))
    draw.ellipse([26, 26, 38, 38], fill=(240, 240, 245))
    # Muzzle
    draw.ellipse([20, 28, 30, 38], fill=(200, 200, 205))
    draw.ellipse([23, 28, 27, 31], fill=(20, 20, 20))
    # Yellow eyes
    draw.rectangle([17, 21, 20, 24], fill=(255, 215, 0))
    draw.rectangle([18, 22, 19, 23], fill=(0, 0, 0))
    draw.rectangle([30, 21, 33, 24], fill=(255, 215, 0))
    draw.rectangle([31, 22, 32, 23], fill=(0, 0, 0))
    save_sprite("wolf", img)

    # 3. SHEEP
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Woolly background
    draw.ellipse([10, 14, 40, 38], fill=(245, 245, 245))
    draw.ellipse([8, 18, 20, 30], fill=(245, 245, 245))
    draw.ellipse([30, 18, 42, 30], fill=(245, 245, 245))
    # Face
    draw.ellipse([15, 18, 35, 38], fill=(245, 205, 185))
    draw.ellipse([12, 24, 18, 28], fill=(245, 205, 185))
    draw.ellipse([32, 24, 38, 28], fill=(245, 205, 185))
    # Eyes
    draw.rectangle([18, 23, 20, 25], fill=(30, 30, 30))
    draw.rectangle([30, 23, 32, 25], fill=(30, 30, 30))
    # Nose
    draw.line([25, 28, 25, 31], fill=(200, 140, 130), width=2)
    draw.line([23, 28, 27, 28], fill=(200, 140, 130), width=2)
    save_sprite("sheep", img)

    # 4. COW
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Horns
    draw.polygon([14, 14, 10, 6, 17, 12], fill=(235, 235, 215))
    draw.polygon([36, 14, 40, 6, 33, 12], fill=(235, 235, 215))
    # Ears
    draw.ellipse([8, 18, 16, 24], fill=(245, 245, 245))
    draw.ellipse([34, 18, 42, 24], fill=(245, 245, 245))
    # Head & Black spots
    draw.ellipse([12, 14, 38, 40], fill=(245, 245, 245))
    draw.ellipse([14, 16, 24, 26], fill=(35, 35, 40))
    draw.ellipse([28, 24, 36, 32], fill=(35, 35, 40))
    # Pink muzzle
    draw.ellipse([16, 28, 34, 39], fill=(255, 185, 195))
    draw.ellipse([20, 31, 22, 33], fill=(40, 40, 40))
    draw.ellipse([28, 31, 30, 33], fill=(40, 40, 40))
    # Eyes
    draw.rectangle([17, 21, 19, 23], fill=(10, 10, 10))
    draw.rectangle([31, 21, 33, 23], fill=(10, 10, 10))
    save_sprite("cow", img)

    # 5. HORSE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.polygon([14, 14, 11, 4, 18, 10], fill=(130, 70, 25))
    draw.polygon([36, 14, 39, 4, 32, 10], fill=(130, 70, 25))
    # Head
    draw.ellipse([14, 10, 36, 42], fill=(135, 75, 30))
    # Mane & Stripe
    draw.rectangle([23, 10, 27, 24], fill=(40, 40, 45))
    draw.rectangle([23, 20, 27, 34], fill=(245, 245, 245))
    # Snout
    draw.ellipse([17, 32, 33, 42], fill=(80, 45, 15))
    draw.ellipse([20, 36, 22, 38], fill=(20, 20, 20))
    draw.ellipse([28, 36, 30, 38], fill=(20, 20, 20))
    # Eyes
    draw.rectangle([17, 21, 19, 23], fill=(245, 245, 245))
    draw.rectangle([18, 21, 19, 22], fill=(10, 10, 10))
    draw.rectangle([31, 21, 33, 23], fill=(245, 245, 245))
    draw.rectangle([31, 21, 32, 22], fill=(10, 10, 10))
    save_sprite("horse", img)

    # 6. CHICKEN
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Comb
    draw.ellipse([21, 8, 25, 14], fill=(230, 35, 35))
    draw.ellipse([25, 6, 29, 13], fill=(230, 35, 35))
    # Head
    draw.ellipse([14, 12, 36, 36], fill=(250, 250, 250))
    # Beak
    draw.polygon([21, 22, 29, 22, 25, 28], fill=(255, 185, 25))
    # Wattle
    draw.ellipse([22, 28, 28, 34], fill=(230, 35, 35))
    # Eyes
    draw.rectangle([18, 18, 20, 21], fill=(20, 20, 20))
    draw.rectangle([30, 18, 32, 21], fill=(20, 20, 20))
    save_sprite("chicken", img)

    # 7. DUCK
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head
    draw.ellipse([14, 12, 36, 36], fill=(255, 225, 60))
    # Flat Bill
    draw.ellipse([18, 22, 32, 30], fill=(255, 125, 5))
    # Eyes
    draw.rectangle([18, 18, 20, 21], fill=(15, 15, 15))
    draw.rectangle([19, 18, 19, 19], fill=(255, 255, 255))
    draw.rectangle([30, 18, 32, 21], fill=(15, 15, 15))
    draw.rectangle([31, 18, 31, 19], fill=(255, 255, 255))
    save_sprite("duck", img)

    # 8. TURTLE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Shell Collar
    draw.ellipse([10, 28, 40, 42], fill=(30, 105, 30))
    # Head
    draw.ellipse([15, 14, 35, 34], fill=(135, 225, 135))
    # Eyes
    draw.rectangle([18, 20, 20, 23], fill=(20, 20, 20))
    draw.rectangle([30, 20, 32, 23], fill=(20, 20, 20))
    # Cheeks
    draw.ellipse([16, 24, 18, 26], fill=(245, 175, 185))
    draw.ellipse([32, 24, 34, 26], fill=(245, 175, 185))
    save_sprite("turtle", img)

    # 9. SNAKE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head
    draw.ellipse([13, 16, 37, 36], fill=(45, 200, 115))
    # Tongue
    draw.line([25, 32, 25, 38], fill=(235, 75, 60), width=2)
    draw.line([25, 38, 22, 42], fill=(235, 75, 60), width=2)
    draw.line([25, 38, 28, 42], fill=(235, 75, 60), width=2)
    # Slit eyes
    draw.rectangle([17, 21, 20, 24], fill=(255, 225, 25))
    draw.line([18, 21, 18, 24], fill=(0, 0, 0), width=1)
    draw.rectangle([30, 21, 33, 24], fill=(255, 225, 25))
    draw.line([31, 21, 31, 24], fill=(0, 0, 0), width=1)
    save_sprite("snake", img)

    # 10. LIZARD
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head
    draw.ellipse([14, 15, 36, 35], fill=(35, 175, 95))
    # Scales markings
    draw.ellipse([18, 17, 21, 20], fill=(245, 155, 20))
    draw.ellipse([29, 17, 32, 20], fill=(245, 155, 20))
    # Big round eyes
    draw.ellipse([16, 20, 20, 24], fill=(255, 245, 225))
    draw.ellipse([18, 21, 20, 23], fill=(0, 0, 0))
    draw.ellipse([30, 20, 34, 24], fill=(255, 245, 225))
    draw.ellipse([30, 21, 32, 23], fill=(0, 0, 0))
    save_sprite("lizard", img)

    # 11. SHARK
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Snout triangle pointing up (front view)
    draw.polygon([25, 10, 12, 38, 38, 38], fill=(95, 115, 135))
    # White mouth underbelly
    draw.polygon([25, 28, 16, 38, 34, 38], fill=(245, 245, 250))
    # Gills
    draw.line([14, 30, 16, 30], fill=(50, 50, 50), width=1)
    draw.line([13, 33, 15, 33], fill=(50, 50, 50), width=1)
    draw.line([36, 30, 34, 30], fill=(50, 50, 50), width=1)
    draw.line([37, 33, 35, 33], fill=(50, 50, 50), width=1)
    # Eyes
    draw.rectangle([19, 24, 21, 26], fill=(10, 10, 15))
    draw.rectangle([29, 24, 31, 26], fill=(10, 10, 15))
    save_sprite("shark", img)

    # 12. WHALE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Water Spout
    draw.line([25, 12, 25, 6], fill=(175, 215, 240), width=2)
    draw.line([25, 6, 21, 3], fill=(175, 215, 240), width=1)
    draw.line([25, 6, 29, 3], fill=(175, 215, 240), width=1)
    # Large head dome
    draw.ellipse([10, 14, 40, 42], fill=(45, 125, 185))
    # Eyes
    draw.rectangle([12, 28, 14, 30], fill=(255, 255, 255))
    draw.rectangle([36, 28, 38, 30], fill=(255, 255, 255))
    save_sprite("whale", img)

    # 13. DOLPHIN
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head and Beak
    draw.ellipse([13, 14, 37, 38], fill=(125, 180, 215))
    # Beak snout
    draw.ellipse([20, 28, 30, 40], fill=(110, 160, 195))
    # Eyes
    draw.rectangle([18, 22, 20, 24], fill=(20, 20, 25))
    draw.rectangle([19, 22, 19, 23], fill=(255, 255, 255))
    draw.rectangle([30, 22, 32, 24], fill=(20, 20, 25))
    draw.rectangle([30, 22, 30, 23], fill=(255, 255, 255))
    save_sprite("dolphin", img)

    # 14. OCTOPUS
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Bulbous head
    draw.ellipse([14, 12, 36, 34], fill=(155, 90, 180))
    # Tentacles sticking out
    for i in range(5):
        draw.ellipse([11 + i*6, 30, 17 + i*6, 38], fill=(130, 70, 155))
    # Big eyes
    draw.ellipse([16, 20, 22, 26], fill=(255, 255, 255))
    draw.ellipse([18, 22, 21, 25], fill=(10, 10, 10))
    draw.ellipse([28, 20, 34, 26], fill=(255, 255, 255))
    draw.ellipse([29, 22, 32, 25], fill=(10, 10, 10))
    save_sprite("octopus", img)

    # 15. CRAB
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Eye stalks
    draw.line([18, 18, 18, 12], fill=(230, 75, 60), width=2)
    draw.ellipse([16, 10, 20, 14], fill=(0, 0, 0))
    draw.line([32, 18, 32, 12], fill=(230, 75, 60), width=2)
    draw.ellipse([30, 10, 34, 14], fill=(0, 0, 0))
    # Shell body
    draw.ellipse([12, 16, 38, 36], fill=(230, 75, 60))
    # Pincers
    draw.arc([6, 12, 16, 22], start=0, end=360, fill=(230, 75, 60), width=3)
    draw.arc([34, 12, 44, 22], start=0, end=360, fill=(230, 75, 60), width=3)
    save_sprite("crab", img)

    # 16. SPIDER
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Legs (side arcs)
    for y in [22, 26, 30]:
        draw.line([14, y, 6, y - 4], fill=(70, 70, 70), width=2)
        draw.line([36, y, 44, y - 4], fill=(70, 70, 70), width=2)
    # Body
    draw.ellipse([14, 16, 36, 38], fill=(30, 30, 30))
    # Multiple red eyes
    for x in [18, 22, 28, 32]:
        draw.rectangle([x, 20, x+1, 21], fill=(230, 35, 35))
    for x in [20, 26, 30]:
        draw.rectangle([x, 23, x+1, 24], fill=(230, 35, 35))
    save_sprite("spider", img)

    # 17. BEE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Wings
    draw.ellipse([6, 14, 18, 22], fill=(175, 215, 240, 180))
    draw.ellipse([32, 14, 44, 22], fill=(175, 215, 240, 180))
    # Antennae
    draw.line([20, 15, 16, 8], fill=(40, 60, 80), width=2)
    draw.line([30, 15, 34, 8], fill=(40, 60, 80), width=2)
    # Head & stripes
    draw.ellipse([14, 14, 36, 36], fill=(240, 195, 15))
    draw.ellipse([18, 14, 32, 36], fill=(45, 60, 80))
    draw.ellipse([22, 14, 28, 36], fill=(240, 195, 15))
    # Eyes
    draw.rectangle([18, 21, 20, 24], fill=(10, 10, 10))
    draw.rectangle([30, 21, 32, 24], fill=(10, 10, 10))
    save_sprite("bee", img)

    # 18. BUTTERFLY
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Wings left and right
    draw.ellipse([6, 10, 24, 26], fill=(235, 110, 100))
    draw.ellipse([8, 22, 22, 38], fill=(90, 175, 225))
    draw.ellipse([26, 10, 44, 26], fill=(235, 110, 100))
    draw.ellipse([28, 22, 42, 38], fill=(90, 175, 225))
    # Body
    draw.ellipse([22, 12, 28, 38], fill=(45, 65, 85))
    # Antennae
    draw.line([23, 12, 19, 4], fill=(45, 65, 85), width=2)
    draw.line([27, 12, 31, 4], fill=(45, 65, 85), width=2)
    save_sprite("butterfly", img)

    # 19. BAT
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Large pointed ears
    draw.polygon([14, 18, 6, 4, 20, 18], fill=(50, 50, 55))
    draw.polygon([36, 18, 44, 4, 30, 18], fill=(50, 50, 55))
    draw.polygon([11, 14, 8, 7, 16, 15], fill=(245, 185, 180))
    draw.polygon([39, 14, 42, 7, 34, 15], fill=(245, 185, 180))
    # Head
    draw.ellipse([14, 16, 36, 38], fill=(50, 50, 55))
    # Red eyes
    draw.rectangle([18, 22, 20, 24], fill=(230, 30, 30))
    draw.rectangle([30, 22, 32, 24], fill=(230, 30, 30))
    # Small fangs
    draw.polygon([22, 28, 24, 28, 23, 31], fill=(255, 255, 255))
    draw.polygon([26, 28, 28, 28, 27, 31], fill=(255, 255, 255))
    save_sprite("bat", img)

    # 20. SQUIRREL
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.polygon([15, 16, 12, 8, 19, 13], fill=(210, 85, 0))
    draw.polygon([35, 16, 38, 8, 31, 13], fill=(210, 85, 0))
    # Head
    draw.ellipse([13, 14, 37, 38], fill=(211, 84, 0))
    # White cheeks
    draw.ellipse([14, 25, 24, 35], fill=(245, 245, 245))
    draw.ellipse([26, 25, 36, 35], fill=(245, 245, 245))
    # Eyes
    draw.rectangle([17, 21, 19, 23], fill=(20, 20, 20))
    draw.rectangle([31, 21, 33, 23], fill=(20, 20, 20))
    # Nose
    draw.ellipse([23, 26, 27, 29], fill=(110, 45, 0))
    save_sprite("squirrel", img)

    # 21. RACCOON
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.polygon([13, 16, 8, 6, 20, 16], fill=(128, 140, 150))
    draw.polygon([37, 16, 42, 6, 30, 16], fill=(128, 140, 150))
    # Head
    draw.ellipse([13, 14, 37, 38], fill=(128, 140, 150))
    # Black mask
    draw.ellipse([14, 21, 24, 29], fill=(45, 60, 80))
    draw.ellipse([26, 21, 36, 29], fill=(45, 60, 80))
    draw.rectangle([20, 23, 30, 27], fill=(45, 60, 80))
    # White eyes & snout
    draw.rectangle([18, 23, 20, 25], fill=(255, 255, 255))
    draw.rectangle([30, 23, 32, 25], fill=(255, 255, 255))
    draw.ellipse([20, 28, 30, 36], fill=(240, 240, 245))
    draw.ellipse([23, 28, 27, 31], fill=(20, 20, 20))
    save_sprite("raccoon", img)

    # 22. BEAVER
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.ellipse([14, 12, 19, 17], fill=(120, 65, 20))
    draw.ellipse([31, 12, 36, 17], fill=(120, 65, 20))
    # Head
    draw.ellipse([14, 14, 36, 38], fill=(120, 65, 20))
    # Orange teeth
    draw.rectangle([22, 28, 25, 33], fill=(245, 145, 25))
    draw.rectangle([25, 28, 28, 33], fill=(245, 145, 25))
    draw.line([25, 28, 25, 33], fill=(50, 30, 10), width=1)
    # Nose & eyes
    draw.ellipse([21, 24, 29, 29], fill=(60, 35, 10))
    draw.rectangle([18, 20, 20, 22], fill=(10, 10, 10))
    draw.rectangle([30, 20, 32, 22], fill=(10, 10, 10))
    save_sprite("beaver", img)

    # 23. KANGAROO
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Long ears
    draw.polygon([14, 18, 10, 2, 20, 12], fill=(210, 140, 80))
    draw.polygon([36, 18, 40, 2, 30, 12], fill=(210, 140, 80))
    draw.polygon([13, 14, 11, 4, 17, 10], fill=(245, 200, 165))
    draw.polygon([37, 14, 39, 4, 33, 10], fill=(245, 200, 165))
    # Head
    draw.ellipse([14, 14, 36, 38], fill=(210, 140, 80))
    # Snout
    draw.ellipse([19, 26, 31, 38], fill=(175, 110, 60))
    draw.ellipse([23, 26, 27, 29], fill=(20, 20, 20))
    # Eyes
    draw.rectangle([18, 21, 20, 23], fill=(10, 10, 10))
    draw.rectangle([30, 21, 32, 23], fill=(10, 10, 10))
    save_sprite("kangaroo", img)

    # 24. ZEBRA
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.polygon([14, 16, 11, 6, 18, 12], fill=(250, 250, 250))
    draw.polygon([36, 16, 39, 6, 32, 12], fill=(250, 250, 250))
    # Head
    draw.ellipse([13, 14, 37, 38], fill=(250, 250, 250))
    # Black stripes
    draw.polygon([13, 20, 22, 20, 18, 23], fill=(30, 30, 35))
    draw.polygon([37, 20, 28, 20, 32, 23], fill=(30, 30, 35))
    draw.polygon([13, 27, 20, 27, 17, 30], fill=(30, 30, 35))
    draw.polygon([37, 27, 30, 27, 33, 30], fill=(30, 30, 35))
    # Muzzle
    draw.ellipse([18, 28, 32, 38], fill=(40, 40, 45))
    # Blue eyes
    draw.rectangle([18, 20, 20, 22], fill=(50, 100, 255))
    draw.rectangle([30, 20, 32, 22], fill=(50, 100, 255))
    save_sprite("zebra", img)

    # 25. GIRAFFE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ossicones (horns)
    draw.line([20, 14, 18, 6], fill=(110, 45, 0), width=2)
    draw.ellipse([16, 4, 20, 8], fill=(110, 45, 0))
    draw.line([30, 14, 32, 6], fill=(110, 45, 0), width=2)
    draw.ellipse([30, 4, 34, 8], fill=(110, 45, 0))
    # Ears
    draw.polygon([14, 18, 6, 12, 17, 22], fill=(244, 208, 63))
    draw.polygon([36, 18, 44, 12, 33, 22], fill=(244, 208, 63))
    # Head
    draw.ellipse([14, 12, 36, 38], fill=(244, 208, 63))
    # Brown spots
    draw.ellipse([17, 16, 21, 20], fill=(160, 65, 0))
    draw.ellipse([28, 22, 33, 27], fill=(160, 65, 0))
    # Muzzle
    draw.ellipse([18, 28, 32, 37], fill=(235, 190, 120))
    draw.ellipse([23, 28, 27, 30], fill=(40, 40, 45))
    # Eyes
    draw.rectangle([18, 21, 20, 23], fill=(10, 10, 10))
    draw.rectangle([30, 21, 32, 23], fill=(10, 10, 10))
    save_sprite("giraffe", img)

    # 26. HIPPO
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Small ears
    draw.ellipse([14, 12, 19, 17], fill=(110, 120, 130))
    draw.ellipse([31, 12, 36, 17], fill=(110, 120, 130))
    # Large squared head
    draw.rectangle([13, 15, 37, 39], fill=(110, 120, 130))
    # Rounded corners
    draw.ellipse([13, 15, 23, 25], fill=(110, 120, 130))
    draw.ellipse([27, 15, 37, 25], fill=(110, 120, 130))
    draw.ellipse([13, 29, 23, 39], fill=(110, 120, 130))
    draw.ellipse([27, 29, 37, 39], fill=(110, 120, 130))
    # Pink nostrils
    draw.ellipse([18, 28, 23, 33], fill=(255, 190, 205))
    draw.ellipse([27, 28, 32, 33], fill=(255, 190, 205))
    # Eyes
    draw.rectangle([18, 20, 20, 22], fill=(20, 20, 20))
    draw.rectangle([30, 20, 32, 22], fill=(20, 20, 20))
    save_sprite("hippo", img)

    # 27. RHINO
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.polygon([14, 15, 10, 8, 18, 12], fill=(120, 125, 130))
    draw.polygon([36, 15, 40, 8, 32, 12], fill=(120, 125, 130))
    # Head
    draw.ellipse([13, 14, 37, 38], fill=(120, 125, 130))
    # Horn
    draw.polygon([25, 16, 21, 28, 29, 28], fill=(240, 240, 240))
    # Small secondary horn
    draw.polygon([25, 26, 23, 31, 27, 31], fill=(240, 240, 240))
    # Eyes
    draw.rectangle([17, 21, 19, 23], fill=(10, 10, 10))
    draw.rectangle([31, 21, 33, 23], fill=(10, 10, 10))
    save_sprite("rhino", img)

    # 28. CHEETAH
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Ears
    draw.ellipse([14, 12, 20, 18], fill=(243, 156, 18))
    draw.ellipse([30, 12, 36, 18], fill=(243, 156, 18))
    # Head
    draw.ellipse([13, 14, 37, 38], fill=(243, 156, 18))
    # Spots
    draw.rectangle([18, 17, 19, 18], fill=(30, 30, 30))
    draw.rectangle([30, 17, 31, 18], fill=(30, 30, 30))
    draw.rectangle([24, 22, 25, 23], fill=(30, 30, 30))
    draw.rectangle([16, 28, 17, 29], fill=(30, 30, 30))
    draw.rectangle([32, 28, 33, 29], fill=(30, 30, 30))
    # Tear lines
    draw.line([20, 22, 20, 30], fill=(20, 20, 20), width=1)
    draw.line([30, 22, 30, 30], fill=(20, 20, 20), width=1)
    # Snout
    draw.ellipse([20, 28, 30, 35], fill=(245, 245, 245))
    draw.ellipse([23, 28, 27, 30], fill=(20, 20, 20))
    # Eyes
    draw.rectangle([18, 21, 20, 23], fill=(10, 10, 10))
    draw.rectangle([30, 21, 32, 23], fill=(10, 10, 10))
    save_sprite("cheetah", img)

    # 29. EAGLE
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # White head base
    draw.ellipse([13, 14, 37, 36], fill=(250, 250, 250))
    # Curved Yellow beak
    draw.polygon([25, 22, 35, 22, 30, 34, 25, 28], fill=(244, 208, 63))
    # Angry eyes
    draw.rectangle([18, 18, 21, 21], fill=(244, 208, 63))
    draw.rectangle([19, 19, 20, 20], fill=(10, 10, 10))
    draw.line([16, 17, 22, 19], fill=(150, 100, 50), width=1) # brow
    draw.rectangle([29, 18, 32, 21], fill=(244, 208, 63))
    draw.rectangle([30, 19, 31, 20], fill=(10, 10, 10))
    draw.line([34, 17, 28, 19], fill=(150, 100, 50), width=1) # brow
    save_sprite("eagle", img)

    # 30. PARROT
    img = get_canvas()
    draw = ImageDraw.Draw(img)
    # Head red base
    draw.ellipse([13, 14, 37, 36], fill=(231, 76, 60))
    # Curved white beak
    draw.polygon([25, 21, 33, 21, 29, 33, 25, 27], fill=(245, 245, 245))
    # Blue cheek feathers
    draw.ellipse([13, 26, 18, 32], fill=(52, 152, 219))
    draw.ellipse([32, 26, 37, 32], fill=(52, 152, 219))
    # Eyes
    draw.ellipse([17, 17, 21, 21], fill=(245, 245, 245))
    draw.ellipse([18, 18, 20, 20], fill=(10, 10, 10))
    draw.ellipse([29, 17, 33, 21], fill=(245, 245, 245))
    draw.ellipse([30, 18, 32, 20], fill=(10, 10, 10))
    save_sprite("parrot", img)

if __name__ == "__main__":
    generate_all_sprites()
