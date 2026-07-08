import os
from PIL import Image, ImageDraw

def create_sprite(filename, draw_func):
    img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw_func(draw)
    img.save(filename)

# 1. APPLE
def draw_apple(draw):
    draw.ellipse([12, 16, 38, 42], fill=(220, 40, 40, 255))
    draw.ellipse([18, 16, 32, 42], fill=(240, 50, 50, 255))
    draw.line([(25, 16), (25, 8)], fill=(101, 67, 33, 255), width=2)
    draw.polygon([(25, 10), (33, 6), (29, 12)], fill=(40, 160, 40, 255))

# 2. APRICOT
def draw_apricot(draw):
    draw.ellipse([12, 16, 38, 42], fill=(255, 160, 60, 255))
    draw.arc([12, 16, 38, 42], 90, 270, fill=(230, 120, 30, 255), width=1)
    draw.line([(25, 16), (25, 10)], fill=(101, 67, 33, 255), width=2)
    draw.polygon([(25, 11), (30, 8), (28, 13)], fill=(40, 160, 40, 255))

# 3. AVOCADO
def draw_avocado(draw):
    draw.ellipse([12, 14, 38, 42], fill=(30, 80, 30, 255))
    draw.ellipse([14, 16, 36, 40], fill=(180, 210, 80, 255))
    draw.ellipse([17, 19, 33, 37], fill=(220, 240, 120, 255))
    draw.ellipse([20, 25, 30, 35], fill=(120, 70, 30, 255))

# 4. BANANA
def draw_banana(draw):
    draw.arc([10, 10, 45, 45], 20, 160, fill=(240, 220, 30, 255), width=6)
    draw.polygon([(41, 23), (45, 20), (41, 17)], fill=(80, 70, 20, 255))
    draw.polygon([(11, 23), (8, 26), (12, 28)], fill=(60, 50, 10, 255))

# 5. BLACKBERRY
def draw_blackberry(draw):
    for offset in [(0,0), (-4, 4), (4, 4), (-6, 10), (0, 10), (6, 10), (-4, 16), (4, 16), (0, 20)]:
        draw.ellipse([22+offset[0], 16+offset[1], 28+offset[0], 22+offset[1]], fill=(30, 15, 45, 255))
        draw.ellipse([23+offset[0], 17+offset[1], 26+offset[0], 20+offset[1]], fill=(50, 25, 75, 255))
    draw.polygon([(21, 16), (25, 11), (29, 16)], fill=(50, 150, 50, 255))

# 6. BLUEBERRY
def draw_blueberry(draw):
    draw.ellipse([12, 18, 36, 42], fill=(40, 60, 150, 255))
    draw.ellipse([15, 21, 33, 39], fill=(60, 90, 200, 255))
    draw.polygon([(21, 18), (25, 14), (29, 18)], fill=(20, 30, 80, 255))
    draw.polygon([(25, 18), (25, 22), (29, 18)], fill=(20, 30, 80, 255))
    draw.ellipse([26, 12, 44, 30], fill=(30, 45, 120, 255))

# 7. CANTALOUPE
def draw_cantaloupe(draw):
    draw.ellipse([6, 12, 36, 42], fill=(160, 140, 100, 255))
    draw.arc([6, 12, 36, 42], 0, 360, fill=(220, 210, 180, 255), width=1)
    draw.line([(21, 12), (21, 42)], fill=(220, 210, 180, 255), width=1)
    draw.line([(6, 27), (36, 27)], fill=(220, 210, 180, 255), width=1)
    draw.polygon([(28, 22), (44, 18), (44, 42), (28, 38)], fill=(120, 100, 70, 255))
    draw.polygon([(30, 23), (42, 20), (42, 40), (30, 37)], fill=(255, 140, 50, 255))

# 8. CHERRY
def draw_cherry(draw):
    draw.line([(25, 8), (17, 26)], fill=(100, 150, 60, 255), width=2)
    draw.line([(25, 8), (33, 26)], fill=(100, 150, 60, 255), width=2)
    draw.ellipse([10, 22, 26, 38], fill=(180, 10, 30, 255))
    draw.ellipse([12, 24, 20, 32], fill=(220, 40, 60, 255))
    draw.ellipse([24, 22, 40, 38], fill=(180, 10, 30, 255))
    draw.ellipse([26, 24, 34, 32], fill=(220, 40, 60, 255))

# 9. COCONUT
def draw_coconut(draw):
    draw.ellipse([6, 16, 32, 42], fill=(100, 65, 30, 255))
    draw.ellipse([15, 23, 18, 26], fill=(50, 30, 10, 255))
    draw.ellipse([21, 23, 24, 26], fill=(50, 30, 10, 255))
    draw.ellipse([18, 28, 21, 31], fill=(50, 30, 10, 255))
    draw.ellipse([24, 20, 46, 42], fill=(100, 65, 30, 255))
    draw.ellipse([26, 22, 44, 40], fill=(255, 255, 255, 255))
    draw.ellipse([30, 26, 40, 36], fill=(255, 255, 255, 0))

# 10. CRANBERRY
def draw_cranberry(draw):
    draw.ellipse([10, 24, 26, 40], fill=(160, 10, 40, 255))
    draw.ellipse([22, 20, 38, 36], fill=(140, 5, 30, 255))
    draw.ellipse([18, 28, 34, 44], fill=(190, 20, 50, 255))
    draw.polygon([(16, 20), (12, 14), (20, 18)], fill=(50, 140, 50, 255))

# 11. DATE
def draw_date(draw):
    draw.ellipse([12, 20, 26, 38], fill=(90, 50, 30, 255))
    draw.ellipse([22, 16, 36, 34], fill=(70, 35, 15, 255))
    draw.ellipse([20, 26, 34, 44], fill=(85, 45, 20, 255))

# 12. DRAGONFRUIT
def draw_dragonfruit(draw):
    draw.ellipse([10, 14, 38, 42], fill=(235, 45, 115, 255))
    draw.polygon([(10, 24), (6, 21), (12, 20)], fill=(75, 195, 75, 255))
    draw.polygon([(38, 24), (42, 21), (36, 20)], fill=(75, 195, 75, 255))
    draw.polygon([(24, 14), (24, 6), (28, 14)], fill=(75, 195, 75, 255))
    draw.ellipse([22, 24, 44, 46], fill=(235, 45, 115, 255))
    draw.ellipse([24, 26, 42, 44], fill=(255, 255, 255, 255))
    draw.point((30, 32), fill=(0,0,0,255))
    draw.point((36, 30), fill=(0,0,0,255))
    draw.point((32, 38), fill=(0,0,0,255))
    draw.point((38, 36), fill=(0,0,0,255))

# 13. DURIAN
def draw_durian(draw):
    draw.ellipse([10, 14, 40, 42], fill=(130, 140, 50, 255))
    for x in range(12, 40, 6):
        draw.polygon([(x, 14), (x+3, 6), (x+6, 14)], fill=(100, 110, 30, 255))
        draw.polygon([(x, 42), (x+3, 48), (x+6, 42)], fill=(100, 110, 30, 255))
    draw.line([(25, 14), (25, 6)], fill=(90, 60, 20, 255), width=3)

# 14. FIG
def draw_fig(draw):
    draw.polygon([(25, 10), (12, 32), (38, 32)], fill=(100, 50, 100, 255))
    draw.ellipse([12, 22, 38, 42], fill=(100, 50, 100, 255))
    draw.ellipse([24, 24, 46, 44], fill=(100, 50, 100, 255))
    draw.ellipse([26, 26, 44, 42], fill=(230, 80, 100, 255))
    draw.ellipse([31, 31, 39, 37], fill=(250, 150, 160, 255))

# 15. GRAPE
def draw_grape(draw):
    offsets = [(21, 14), (29, 14), (17, 20), (25, 20), (33, 20), (21, 26), (29, 26), (17, 32), (25, 32), (21, 38)]
    for gx, gy in offsets:
        draw.ellipse([gx, gy, gx+8, gy+8], fill=(110, 50, 140, 255))
        draw.ellipse([gx+1, gy+1, gx+5, gy+5], fill=(140, 75, 180, 255))
    draw.line([(25, 6), (25, 14)], fill=(100, 140, 50, 255), width=2)

# 16. GRAPEFRUIT
def draw_grapefruit(draw):
    draw.ellipse([6, 12, 36, 42], fill=(245, 180, 60, 255))
    draw.ellipse([22, 22, 46, 46], fill=(245, 180, 60, 255))
    draw.ellipse([24, 24, 44, 44], fill=(255, 255, 255, 255))
    draw.ellipse([26, 26, 42, 42], fill=(235, 90, 100, 255))
    draw.line([(34, 26), (34, 42)], fill=(255, 255, 255, 255), width=1)
    draw.line([(26, 34), (42, 34)], fill=(255, 255, 255, 255), width=1)

# 17. GUAVA
def draw_guava(draw):
    draw.ellipse([8, 14, 34, 40], fill=(120, 180, 80, 255))
    draw.ellipse([22, 22, 44, 44], fill=(120, 180, 80, 255))
    draw.ellipse([24, 24, 42, 42], fill=(240, 120, 130, 255))
    draw.ellipse([30, 30, 36, 36], fill=(250, 200, 150, 255))

# 18. HONEYDEW
def draw_honeydew(draw):
    draw.ellipse([6, 12, 36, 42], fill=(210, 235, 175, 255))
    draw.polygon([(28, 22), (44, 18), (44, 42), (28, 38)], fill=(180, 215, 145, 255))
    draw.polygon([(30, 23), (42, 20), (42, 40), (30, 37)], fill=(160, 210, 120, 255))

# 19. JACKFRUIT
def draw_jackfruit(draw):
    draw.ellipse([10, 12, 40, 44], fill=(100, 120, 40, 255))
    for y in range(16, 42, 6):
        draw.line([(15, y), (35, y)], fill=(80, 100, 30, 255), width=1)

# 20. KIWI
def draw_kiwi(draw):
    draw.ellipse([6, 16, 32, 40], fill=(120, 90, 60, 255))
    draw.ellipse([22, 20, 46, 44], fill=(120, 90, 60, 255))
    draw.ellipse([24, 22, 44, 42], fill=(80, 180, 60, 255))
    draw.ellipse([30, 28, 38, 36], fill=(240, 250, 200, 255))
    draw.point((28, 30), fill=(0,0,0,255))
    draw.point((30, 27), fill=(0,0,0,255))
    draw.point((35, 26), fill=(0,0,0,255))
    draw.point((39, 29), fill=(0,0,0,255))
    draw.point((40, 33), fill=(0,0,0,255))
    draw.point((37, 39), fill=(0,0,0,255))
    draw.point((31, 39), fill=(0,0,0,255))

# 21. KUMQUAT
def draw_kumquat(draw):
    draw.ellipse([10, 24, 26, 38], fill=(255, 140, 20, 255))
    draw.ellipse([24, 18, 40, 32], fill=(255, 130, 10, 255))
    draw.polygon([(20, 22), (18, 14), (24, 18)], fill=(60, 150, 60, 255))

# 22. LEMON
def draw_lemon(draw):
    draw.polygon([(10, 25), (20, 15), (35, 15), (45, 25), (35, 35), (20, 35)], fill=(245, 220, 40, 255))
    draw.ellipse([14, 16, 40, 34], fill=(245, 220, 40, 255))
    draw.ellipse([20, 18, 34, 26], fill=(255, 245, 130, 255))

# 23. LIME
def draw_lime(draw):
    draw.polygon([(10, 25), (20, 15), (35, 15), (45, 25), (35, 35), (20, 35)], fill=(30, 150, 40, 255))
    draw.ellipse([14, 16, 40, 34], fill=(30, 150, 40, 255))
    draw.ellipse([20, 18, 34, 26], fill=(90, 210, 80, 255))

# 24. LYCHEE
def draw_lychee(draw):
    draw.ellipse([6, 20, 28, 42], fill=(200, 40, 60, 255))
    draw.ellipse([22, 16, 44, 38], fill=(200, 40, 60, 255))
    draw.ellipse([24, 18, 42, 36], fill=(240, 240, 245, 255))
    draw.ellipse([30, 24, 36, 30], fill=(110, 70, 40, 255))

# 25. MANGO
def draw_mango(draw):
    draw.ellipse([12, 16, 38, 42], fill=(235, 180, 45, 255))
    draw.ellipse([12, 16, 28, 36], fill=(225, 75, 45, 255))
    draw.ellipse([28, 28, 38, 42], fill=(120, 190, 50, 255))
    draw.line([(25, 16), (25, 8)], fill=(101, 67, 33, 255), width=2)

# 26. MULBERRY
def draw_mulberry(draw):
    for offset in [(0,0), (-3, 3), (3, 3), (-4, 8), (0, 8), (4, 8), (-4, 13), (0, 13), (4, 13), (-3, 18), (3, 18), (0, 23)]:
        draw.ellipse([22+offset[0], 14+offset[1], 28+offset[0], 20+offset[1]], fill=(25, 10, 40, 255))
    draw.polygon([(21, 14), (25, 9), (29, 14)], fill=(60, 140, 60, 255))

# 27. NECTARINE
def draw_nectarine(draw):
    draw.ellipse([12, 16, 38, 42], fill=(245, 180, 40, 255))
    draw.ellipse([12, 16, 30, 36], fill=(220, 40, 40, 255))
    draw.ellipse([30, 20, 34, 24], fill=(255, 255, 255, 200))

# 28. ORANGE
def draw_orange(draw):
    draw.ellipse([12, 16, 38, 42], fill=(245, 130, 30, 255))
    draw.ellipse([16, 19, 34, 38], fill=(255, 155, 50, 255))
    draw.line([(25, 16), (25, 10)], fill=(90, 60, 30, 255), width=2)
    draw.polygon([(25, 11), (32, 7), (29, 13)], fill=(50, 160, 50, 255))

# 29. PAPAYA
def draw_papaya(draw):
    draw.polygon([(25, 12), (12, 30), (16, 42), (34, 42), (38, 30)], fill=(235, 165, 45, 255))
    draw.ellipse([12, 22, 38, 43], fill=(235, 165, 45, 255))
    draw.ellipse([22, 22, 44, 44], fill=(235, 165, 45, 255))
    draw.ellipse([24, 24, 42, 42], fill=(245, 110, 40, 255))
    draw.ellipse([28, 28, 38, 38], fill=(30, 30, 30, 255))
    draw.ellipse([30, 30, 36, 36], fill=(0, 0, 0, 255))

# 30. PASSIONFRUIT
def draw_passionfruit(draw):
    draw.ellipse([6, 18, 32, 42], fill=(80, 40, 80, 255))
    draw.ellipse([22, 20, 46, 44], fill=(80, 40, 80, 255))
    draw.ellipse([24, 22, 44, 42], fill=(245, 210, 50, 255))
    draw.point((30, 30), fill=(40, 50, 10, 255))
    draw.point((35, 28), fill=(40, 50, 10, 255))
    draw.point((34, 34), fill=(40, 50, 10, 255))
    draw.point((38, 35), fill=(40, 50, 10, 255))

# 31. PEACH
def draw_peach(draw):
    draw.ellipse([12, 16, 38, 42], fill=(255, 140, 105, 255))
    draw.ellipse([12, 16, 28, 34], fill=(240, 80, 90, 255))
    draw.arc([12, 16, 38, 42], 90, 270, fill=(210, 100, 80, 255), width=1)
    draw.line([(25, 16), (25, 10)], fill=(101, 67, 33, 255), width=2)
    draw.polygon([(25, 11), (31, 7), (29, 13)], fill=(80, 170, 70, 255))

# 32. PEAR
def draw_pear(draw):
    draw.polygon([(25, 14), (14, 32), (18, 43), (32, 43), (36, 32)], fill=(155, 195, 60, 255))
    draw.ellipse([14, 24, 36, 43], fill=(155, 195, 60, 255))
    draw.line([(25, 14), (25, 8)], fill=(101, 67, 33, 255), width=2)

# 33. PERSIMMON
def draw_persimmon(draw):
    draw.ellipse([12, 18, 38, 42], fill=(255, 110, 20, 255))
    draw.polygon([(20, 18), (25, 13), (30, 18)], fill=(70, 110, 40, 255))
    draw.polygon([(25, 18), (25, 14), (29, 18)], fill=(70, 110, 40, 255))

# 34. PINEAPPLE
def draw_pineapple(draw):
    draw.ellipse([14, 20, 36, 45], fill=(230, 175, 45, 255))
    for i in range(22, 45, 6):
        draw.line([(14, i), (36, i-4)], fill=(190, 130, 20, 255), width=1)
    draw.polygon([(20, 21), (15, 6), (25, 18)], fill=(40, 140, 50, 255))
    draw.polygon([(25, 21), (25, 4), (29, 19)], fill=(40, 140, 50, 255))
    draw.polygon([(30, 21), (35, 6), (27, 18)], fill=(40, 140, 50, 255))

# 35. PLUM
def draw_plum(draw):
    draw.ellipse([12, 16, 38, 42], fill=(90, 40, 110, 255))
    draw.ellipse([15, 18, 35, 40], fill=(110, 50, 130, 255))
    draw.arc([12, 16, 38, 42], 90, 270, fill=(70, 20, 90, 255), width=1)

# 36. POMEGRANATE
def draw_pomegranate(draw):
    draw.ellipse([12, 16, 38, 42], fill=(195, 30, 45, 255))
    draw.polygon([(22, 16), (20, 10), (25, 15)], fill=(195, 30, 45, 255))
    draw.polygon([(28, 16), (30, 10), (25, 15)], fill=(195, 30, 45, 255))
    draw.ellipse([24, 24, 46, 46], fill=(195, 30, 45, 255))
    draw.ellipse([26, 26, 44, 44], fill=(250, 220, 180, 255))
    draw.ellipse([29, 29, 34, 34], fill=(220, 10, 35, 255))
    draw.ellipse([35, 30, 40, 35], fill=(220, 10, 35, 255))
    draw.ellipse([32, 36, 37, 41], fill=(220, 10, 35, 255))

# 37. POMELO
def draw_pomelo(draw):
    draw.ellipse([6, 12, 38, 44], fill=(210, 225, 80, 255))
    draw.ellipse([14, 18, 30, 34], fill=(230, 245, 120, 255))

# 38. QUINCE
def draw_quince(draw):
    draw.polygon([(25, 15), (13, 30), (16, 42), (34, 42), (37, 30)], fill=(235, 215, 55, 255))
    draw.ellipse([13, 23, 37, 43], fill=(235, 215, 55, 255))
    draw.line([(25, 15), (25, 8)], fill=(101, 67, 33, 255), width=2)

# 39. RASPBERRY
def draw_raspberry(draw):
    for offset in [(0,0), (-3, 3), (3, 3), (-5, 7), (0, 7), (5, 7), (-4, 12), (4, 12), (-2, 17), (2, 17), (0, 21)]:
        draw.ellipse([22+offset[0], 16+offset[1], 28+offset[0], 22+offset[1]], fill=(225, 45, 85, 255))
        draw.ellipse([23+offset[0], 17+offset[1], 26+offset[0], 20+offset[1]], fill=(245, 75, 115, 255))
    draw.polygon([(20, 16), (25, 11), (30, 16)], fill=(50, 160, 50, 255))

# 40. STARFRUIT
def draw_starfruit(draw):
    draw.polygon([(25, 8), (29, 18), (39, 18), (31, 26), (34, 36), (25, 30), (16, 36), (19, 26), (11, 18), (21, 18)], fill=(240, 220, 30, 255))
    draw.line([(25, 8), (25, 30)], fill=(200, 180, 10, 255), width=1)
    draw.line([(11, 18), (39, 18)], fill=(200, 180, 10, 255), width=1)

# 41. STRAWBERRY
def draw_strawberry(draw):
    draw.polygon([(25, 44), (12, 22), (20, 16), (30, 16), (38, 22)], fill=(220, 30, 30, 255))
    draw.ellipse([12, 16, 38, 34], fill=(220, 30, 30, 255))
    draw.polygon([(18, 16), (25, 20), (32, 16)], fill=(50, 150, 50, 255))
    draw.polygon([(14, 16), (25, 10), (36, 16)], fill=(50, 150, 50, 255))
    seeds = [(18, 22), (24, 20), (30, 22), (16, 28), (22, 27), (28, 28), (34, 27), (20, 34), (26, 33), (32, 34), (24, 39)]
    for sx, sy in seeds:
        draw.rectangle([sx, sy, sx+1, sy+1], fill=(240, 240, 100, 255))

# 42. TANGERINE
def draw_tangerine(draw):
    draw.ellipse([10, 19, 40, 41], fill=(245, 120, 20, 255))
    draw.line([(25, 19), (25, 13)], fill=(100, 70, 30, 255), width=2)
    draw.polygon([(25, 14), (30, 10), (28, 15)], fill=(50, 150, 50, 255))

# 43. WATERMELON
def draw_watermelon(draw):
    draw.ellipse([4, 18, 32, 40], fill=(40, 120, 50, 255))
    draw.arc([4, 18, 32, 40], 30, 150, fill=(20, 80, 30, 255), width=2)
    draw.polygon([(22, 38), (44, 18), (44, 38)], fill=(40, 120, 50, 255))
    draw.polygon([(23, 37), (42, 20), (42, 37)], fill=(255, 255, 255, 255))
    draw.polygon([(25, 36), (40, 22), (40, 36)], fill=(235, 45, 45, 255))
    draw.point((32, 32), fill=(0,0,0,255))
    draw.point((35, 29), fill=(0,0,0,255))

# 44. STAR APPLE
def draw_star_apple(draw):
    draw.ellipse([8, 16, 32, 40], fill=(80, 50, 100, 255))
    draw.ellipse([22, 22, 46, 46], fill=(80, 50, 100, 255))
    draw.ellipse([24, 24, 44, 44], fill=(245, 240, 245, 255))
    for angle in [0, 72, 144, 216, 288]:
        draw.line([(34, 34), (34, 28)], fill=(120, 80, 140, 255), width=1)

# 45. BOYSENBERRY
def draw_boysenberry(draw):
    for offset in [(0,0), (-3, 3), (3, 3), (-5, 7), (0, 7), (5, 7), (-4, 12), (4, 12), (-2, 17), (2, 17), (0, 21)]:
        draw.ellipse([22+offset[0], 16+offset[1], 28+offset[0], 22+offset[1]], fill=(100, 25, 60, 255))
        draw.ellipse([23+offset[0], 17+offset[1], 26+offset[0], 20+offset[1]], fill=(130, 45, 90, 255))
    draw.polygon([(20, 16), (25, 11), (30, 16)], fill=(50, 140, 50, 255))

# 46. ELDERBERRY
def draw_elderberry(draw):
    draw.line([(25, 10), (15, 26)], fill=(180, 40, 50, 255), width=1)
    draw.line([(25, 10), (35, 26)], fill=(180, 40, 50, 255), width=1)
    for bx, by in [(13, 24), (17, 27), (21, 23), (25, 26), (29, 23), (33, 27), (37, 24)]:
        draw.ellipse([bx, by, bx+4, by+4], fill=(15, 15, 20, 255))

# 47. GOOSEBERRY
def draw_gooseberry(draw):
    draw.ellipse([12, 16, 38, 42], fill=(140, 210, 110, 255))
    draw.arc([12, 16, 38, 42], 45, 135, fill=(180, 240, 150, 255), width=1)
    draw.arc([12, 16, 38, 42], 225, 315, fill=(180, 240, 150, 255), width=1)
    draw.line([(25, 16), (25, 42)], fill=(180, 240, 150, 255), width=1)

# 48. KEY LIME
def draw_key_lime(draw):
    draw.ellipse([14, 20, 36, 42], fill=(180, 210, 50, 255))
    draw.ellipse([18, 23, 32, 37], fill=(205, 235, 80, 255))

# 49. BLOOD ORANGE
def draw_blood_orange(draw):
    draw.ellipse([6, 12, 36, 42], fill=(230, 100, 30, 255))
    draw.ellipse([22, 22, 46, 46], fill=(230, 100, 30, 255))
    draw.ellipse([24, 24, 44, 44], fill=(255, 255, 255, 255))
    draw.ellipse([26, 26, 42, 42], fill=(180, 10, 30, 255))
    draw.line([(34, 26), (34, 42)], fill=(255, 255, 255, 255), width=1)
    draw.line([(26, 34), (42, 34)], fill=(255, 255, 255, 255), width=1)

# 50. RED CURRANT
def draw_red_currant(draw):
    draw.line([(25, 8), (15, 38)], fill=(120, 150, 80, 255), width=1)
    for bx, by in [(16, 16), (23, 20), (14, 26), (21, 30), (12, 36), (19, 40)]:
        draw.ellipse([bx, by, bx+6, by+6], fill=(235, 45, 55, 255))
        draw.ellipse([bx+1, by+1, bx+3, by+3], fill=(255, 120, 120, 255))

# 51. BLACK CURRANT
def draw_black_currant(draw):
    draw.line([(25, 8), (15, 38)], fill=(120, 150, 80, 255), width=1)
    for bx, by in [(16, 16), (23, 20), (14, 26), (21, 30), (12, 36), (19, 40)]:
        draw.ellipse([bx, by, bx+6, by+6], fill=(25, 15, 35, 255))
        draw.ellipse([bx+1, by+1, bx+3, by+3], fill=(70, 50, 90, 255))

# 52. MANGOSTEEN
def draw_mangosteen(draw):
    draw.ellipse([6, 18, 34, 42], fill=(60, 30, 60, 255))
    draw.rectangle([16, 14, 24, 18], fill=(120, 140, 50, 255))
    draw.ellipse([22, 20, 46, 44], fill=(60, 30, 60, 255))
    draw.ellipse([24, 22, 44, 42], fill=(230, 30, 60, 255))
    draw.ellipse([28, 26, 40, 38], fill=(255, 255, 255, 255))
    draw.line([(34, 26), (34, 38)], fill=(220, 220, 220, 255), width=1)
    draw.line([(28, 32), (40, 32)], fill=(220, 220, 220, 255), width=1)

fruits_to_generate = [
    ("apple", draw_apple), ("apricot", draw_apricot), ("avocado", draw_avocado), ("banana", draw_banana),
    ("blackberry", draw_blackberry), ("blueberry", draw_blueberry), ("cantaloupe", draw_cantaloupe), ("cherry", draw_cherry),
    ("coconut", draw_coconut), ("cranberry", draw_cranberry), ("date", draw_date), ("dragonfruit", draw_dragonfruit),
    ("durian", draw_durian), ("fig", draw_fig), ("grape", draw_grape), ("grapefruit", draw_grapefruit),
    ("guava", draw_guava), ("honeydew", draw_honeydew), ("jackfruit", draw_jackfruit), ("kiwi", draw_kiwi),
    ("kumquat", draw_kumquat), ("lemon", draw_lemon), ("lime", draw_lime), ("lychee", draw_lychee),
    ("mango", draw_mango), ("mulberry", draw_mulberry), ("nectarine", draw_nectarine), ("orange", draw_orange),
    ("papaya", draw_papaya), ("passionfruit", draw_passionfruit), ("peach", draw_peach), ("pear", draw_pear),
    ("persimmon", draw_persimmon), ("pineapple", draw_pineapple), ("plum", draw_plum), ("pomegranate", draw_pomegranate),
    ("pomelo", draw_pomelo), ("quince", draw_quince), ("raspberry", draw_raspberry), ("starfruit", draw_starfruit),
    ("strawberry", draw_strawberry), ("tangerine", draw_tangerine), ("watermelon", draw_watermelon), ("star_apple", draw_star_apple),
    ("boysenberry", draw_boysenberry), ("elderberry", draw_elderberry), ("gooseberry", draw_gooseberry), ("key_lime", draw_key_lime),
    ("blood_orange", draw_blood_orange), ("red_currant", draw_red_currant), ("black_currant", draw_black_currant), ("mangosteen", draw_mangosteen)
]

fruits_metadata = [
    {"id": "apple", "name": "Apple", "category": "pome", "diet": "Sweet & Crisp", "habitat": "Central Asia", "rarity": "★★☆☆☆", "description": "A crisp and sweet pome fruit. One of the most widely cultivated fruits worldwide."},
    {"id": "apricot", "name": "Apricot", "category": "stone", "diet": "Sweet & Tart", "habitat": "Armenia", "rarity": "★★★☆☆", "description": "A soft, orange stone fruit with a velvety skin and sweet-tart flavor."},
    {"id": "avocado", "name": "Avocado", "category": "tropical", "diet": "Rich & Buttery", "habitat": "Mexico", "rarity": "★★★☆☆", "description": "A botanically large berry with a single large seed and a rich, buttery green flesh."},
    {"id": "banana", "name": "Banana", "category": "tropical", "diet": "Sweet & Creamy", "habitat": "Southeast Asia", "rarity": "★☆☆☆☆", "description": "An elongated, edible yellow fruit produced by large herbaceous flowering plants."},
    {"id": "blackberry", "name": "Blackberry", "category": "berry", "diet": "Deep & Tart", "habitat": "North America", "rarity": "★★★☆☆", "description": "An aggregate fruit composed of small drupelets, deep purple-black when ripe."},
    {"id": "blueberry", "name": "Blueberry", "category": "berry", "diet": "Sweet & Mild", "habitat": "North America", "rarity": "★★☆☆☆", "description": "Small, indigo-colored round berries with a sweet, crown-like tip."},
    {"id": "cantaloupe", "name": "Cantaloupe", "category": "melon", "diet": "Sweet & Musky", "habitat": "South Asia", "rarity": "★★★☆☆", "description": "A netted orange-fleshed melon with a sweet, refreshing, and aromatic taste."},
    {"id": "cherry", "name": "Cherry", "category": "stone", "diet": "Sweet or Sour", "habitat": "Black Sea Region", "rarity": "★★☆☆☆", "description": "A small, fleshy stone fruit hanging from long stems, popular in desserts."},
    {"id": "coconut", "name": "Coconut", "category": "tropical", "diet": "Sweet & Nutty", "habitat": "Melanesia", "rarity": "★★★☆☆", "description": "A large seed of a palm tree with a fibrous husk, white meat, and sweet water."},
    {"id": "cranberry", "name": "Cranberry", "category": "berry", "diet": "Very Tart", "habitat": "North America", "rarity": "★★★☆☆", "description": "Hard, red acidic berries grown on low vines in marshy peat bogs."},
    {"id": "date", "name": "Date", "category": "tropical", "diet": "Rich & Honey-like", "habitat": "Middle East", "rarity": "★★★☆☆", "description": "Sweet, chewy fruit of the date palm tree, often dried and consumed as a delicacy."},
    {"id": "dragonfruit", "name": "Dragonfruit", "category": "tropical", "diet": "Mild & Pear-like", "habitat": "Central America", "rarity": "★★★★☆", "description": "Stunning pink fruit with green scales, white flesh, and tiny black seeds."},
    {"id": "durian", "name": "Durian", "category": "tropical", "diet": "Custard-like & Pungent", "habitat": "Southeast Asia", "rarity": "★★★★★", "description": "The King of Fruits, famed for its large spiky shell and strong, unique aroma."},
    {"id": "fig", "name": "Fig", "category": "tropical", "diet": "Sweet & Jammy", "habitat": "Mediterranean", "rarity": "★★★★☆", "description": "A teardrop-shaped fruit with a soft purple skin, pink flesh, and crunchy seeds."},
    {"id": "grape", "name": "Grape", "category": "berry", "diet": "Sweet & Juicy", "habitat": "Near East", "rarity": "★☆☆☆☆", "description": "Small oval fruits growing in clusters, used for juice, raisins, and wine."},
    {"id": "grapefruit", "name": "Grapefruit", "category": "citrus", "diet": "Tart & Bitter", "habitat": "Barbados", "rarity": "★★★☆☆", "description": "A large citrus hybrid with yellow-orange skin and tart, pink segmented flesh."},
    {"id": "guava", "name": "Guava", "category": "tropical", "diet": "Sweet & Fragrant", "habitat": "Tropical America", "rarity": "★★★★☆", "description": "Round green tropical fruit with a fragrant smell and pink, seed-filled center."},
    {"id": "honeydew", "name": "Honeydew", "category": "melon", "diet": "Sweet & Juicy", "habitat": "Middle East", "rarity": "★★★☆☆", "description": "A smooth, pale-green skinned melon with sweet, juicy light-green flesh."},
    {"id": "jackfruit", "name": "Jackfruit", "category": "tropical", "diet": "Sweet & Fruity", "habitat": "India", "rarity": "★★★★☆", "description": "The largest tree-borne fruit, with a green spiky rind and sweet yellow pods."},
    {"id": "kiwi", "name": "Kiwi", "category": "tropical", "diet": "Tangy & Sweet", "habitat": "China", "rarity": "★★☆☆☆", "description": "A fuzzy brown oval fruit with green flesh, white core, and black seeds."},
    {"id": "kumquat", "name": "Kumquat", "category": "citrus", "diet": "Sweet Skin & Sour Flesh", "habitat": "China", "rarity": "★★★★☆", "description": "A tiny orange citrus fruit eaten whole, skins and all."},
    {"id": "lemon", "name": "Lemon", "category": "citrus", "diet": "Very Sour", "habitat": "Northeast India", "rarity": "★☆☆☆☆", "description": "A bright yellow ellipsoidal citrus fruit, highly prized for its juice."},
    {"id": "lime", "name": "Lime", "category": "citrus", "diet": "Sour & Zesty", "habitat": "Southeast Asia", "rarity": "★☆☆☆☆", "description": "A green citrus fruit, rounder and slightly more bitter than lemons."},
    {"id": "lychee", "name": "Lychee", "category": "tropical", "diet": "Sweet & Floral", "habitat": "China", "rarity": "★★★★☆", "description": "A red bumpy-skinned fruit with translucent white flesh and a dark seed."},
    {"id": "mango", "name": "Mango", "category": "tropical", "diet": "Sweet & Tropical", "habitat": "South Asia", "rarity": "★★☆☆☆", "description": "The national fruit of India, renowned for its rich orange flesh and sweet taste."},
    {"id": "mulberry", "name": "Mulberry", "category": "berry", "diet": "Sweet & Earthy", "habitat": "Asia & North America", "rarity": "★★★★☆", "description": "Elongated, blackberry-like fruits that grow on fast-growing deciduous trees."},
    {"id": "nectarine", "name": "Nectarine", "category": "stone", "diet": "Sweet & Juicy", "habitat": "China", "rarity": "★★★☆☆", "description": "A smooth-skinned peach variant with sweet, juicy yellow-orange flesh."},
    {"id": "orange", "name": "Orange", "category": "citrus", "diet": "Sweet & Citrusy", "habitat": "Southeast Asia", "rarity": "★☆☆☆☆", "description": "A popular round orange citrus fruit, famous for its vitamin C content."},
    {"id": "papaya", "name": "Papaya", "category": "tropical", "diet": "Sweet & Musky", "habitat": "Mesoamerica", "rarity": "★★★☆☆", "description": "An elongated tropical fruit with orange flesh and hundreds of black seeds."},
    {"id": "passionfruit", "name": "Passionfruit", "category": "tropical", "diet": "Tangy & Aromatic", "habitat": "Brazil", "rarity": "★★★★☆", "description": "Wrinkled purple fruit filled with aromatic, tart yellow pulp and crunchy seeds."},
    {"id": "peach", "name": "Peach", "category": "stone", "diet": "Sweet & Velvety", "habitat": "China", "rarity": "★★☆☆☆", "description": "A fuzzy, soft-skinned stone fruit with sweet, juicy yellow-orange flesh."},
    {"id": "pear", "name": "Pear", "category": "pome", "diet": "Sweet & Mellow", "habitat": "Europe & Asia", "rarity": "★★☆☆☆", "description": "A teardrop-shaped pome fruit with a sweet, mild, and slightly grainy flesh."},
    {"id": "persimmon", "name": "Persimmon", "category": "tropical", "diet": "Honey-like & Sweet", "habitat": "East Asia", "rarity": "★★★★☆", "description": "Bright orange squarish-round fruits that are sweet and honey-like when ripe."},
    {"id": "pineapple", "name": "Pineapple", "category": "tropical", "diet": "Sweet & Acidic", "habitat": "South America", "rarity": "★★☆☆☆", "description": "A large tropical fruit with a tough spiky skin and a crown of green leaves."},
    {"id": "plum", "name": "Plum", "category": "stone", "diet": "Sweet & Tart", "habitat": "Caucasus Region", "rarity": "★★☆☆☆", "description": "A smooth-skinned, deep purple stone fruit with tart skin and sweet flesh."},
    {"id": "pomegranate", "name": "Pomegranate", "category": "tropical", "diet": "Sweet & Tart", "habitat": "Persia", "rarity": "★★★★☆", "description": "A round red fruit containing hundreds of edible ruby-red juicy arils."},
    {"id": "pomelo", "name": "Pomelo", "category": "citrus", "diet": "Sweet & Mild", "habitat": "Southeast Asia", "rarity": "★★★★☆", "description": "The largest citrus fruit, with a very thick skin and mild, sweet segmented flesh."},
    {"id": "quince", "name": "Quince", "category": "pome", "diet": "Aromatic & Sour", "habitat": "Caucasus", "rarity": "★★★★☆", "description": "A lumpy yellow fruit related to apples and pears, usually cooked before eating."},
    {"id": "raspberry", "name": "Raspberry", "category": "berry", "diet": "Sweet & Tart", "habitat": "Europe & North America", "rarity": "★★☆☆☆", "description": "A hollow, red aggregate berry composed of small drupelets, very fragrant."},
    {"id": "starfruit", "name": "Starfruit", "category": "tropical", "diet": "Tart & Juicy", "habitat": "Southeast Asia", "rarity": "★★★★☆", "description": "A yellow-green ribbed fruit that creates star shapes when sliced."},
    {"id": "strawberry", "name": "Strawberry", "category": "berry", "diet": "Sweet & Fragrant", "habitat": "Europe", "rarity": "★☆☆☆☆", "description": "A popular red aggregate accessory fruit with external seeds and a green cap."},
    {"id": "tangerine", "name": "Tangerine", "category": "citrus", "diet": "Sweet & Easy to Peel", "habitat": "Morocco", "rarity": "★★☆☆☆", "description": "A small, sweet citrus fruit related to oranges, but easy to peel."},
    {"id": "watermelon", "name": "Watermelon", "category": "melon", "diet": "Sweet & Refreshing", "habitat": "Southern Africa", "rarity": "★★☆☆☆", "description": "A massive melon with a hard green striped rind and sweet red watery flesh."},
    {"id": "star_apple", "name": "Star Apple", "category": "tropical", "diet": "Sweet & Milky", "habitat": "West Indies", "rarity": "★★★★★", "description": "A round purple tropical fruit that shows a star pattern when sliced."},
    {"id": "boysenberry", "name": "Boysenberry", "category": "berry", "diet": "Tangy & Sweet", "habitat": "California", "rarity": "★★★★☆", "description": "A hybrid between blackberry, raspberry, dewberry, and loganberry."},
    {"id": "elderberry", "name": "Elderberry", "category": "berry", "diet": "Tart & Earthy", "habitat": "Europe & North America", "rarity": "★★★★☆", "description": "Tiny dark purple berries growing in clusters, commonly used in syrups."},
    {"id": "gooseberry", "name": "Gooseberry", "category": "berry", "diet": "Tart & Grape-like", "habitat": "Eurasia", "rarity": "★★★★☆", "description": "Small translucent green veined berries with a sharp, tangy taste."},
    {"id": "key_lime", "name": "Key Lime", "category": "citrus", "diet": "Tart & Acidic", "habitat": "Florida Keys", "rarity": "★★★★☆", "description": "Small, round yellow-green citrus, famous for its use in Key Lime Pie."},
    {"id": "blood_orange", "name": "Blood Orange", "category": "citrus", "diet": "Sweet & Raspberry-like", "habitat": "Sicily", "rarity": "★★★★☆", "description": "An orange variety with dark crimson-red flesh and a raspberry-like flavor."},
    {"id": "red_currant", "name": "Red Currant", "category": "berry", "diet": "Tart & Acidic", "habitat": "Western Europe", "rarity": "★★★★☆", "description": "Translucent shiny red berries growing in dangling clusters."},
    {"id": "black_currant", "name": "Black Currant", "category": "berry", "diet": "Strong & Woody-sweet", "habitat": "Northern Europe", "rarity": "★★★★☆", "description": "Dark purple-black berries prized for their high vitamin C content."},
    {"id": "mangosteen", "name": "Mangosteen", "category": "tropical", "diet": "Sweet & Tangy", "habitat": "Sundaland", "rarity": "★★★★★", "description": "Tropical fruit with a thick purple rind enclosing sweet, white segments."}
]

def main():
    out_dir = "images/fruits"
    os.makedirs(out_dir, exist_ok=True)
    
    # Generate fruit images
    for name, func in fruits_to_generate:
        path = os.path.join(out_dir, f"{name}_50x50.png")
        create_sprite(path, func)
        print(f"Generated {path}")

    # Append to app.js database
    if not os.path.exists("app.js"):
        print("Error: app.js not found, cannot append fruit data!")
        return

    with open("app.js", "r") as f:
        content = f.read()

    app_state_idx = content.find("// Application State")
    idx = content.rfind("];", 0, app_state_idx)
    if idx != -1:
        js_arr = []
        for a in fruits_metadata:
            # Check if fruit is already in app.js
            if f'id: "{a["id"]}"' in content:
                print(f"Fruit {a['id']} already exists in app.js, skipping database append.")
                continue
                
            js_str = f"""    {{
        id: "{a['id']}",
        name: "{a['name']}",
        filename: "images/fruits/{a['id']}_50x50.png",
        category: "{a['category']}",
        isPredator: false,
        diet: "{a['diet']}",
        habitat: "{a['habitat']}",
        rarity: "{a['rarity']}",
        description: "{a['description']}",
        isFruit: true
    }}"""
            js_arr.append(js_str)
            
        if not js_arr:
            print("No new fruits needed to be added to app.js database.")
            return

        last_obj_end = content.rfind("}", 0, idx)
        prefix = ""
        if last_obj_end != -1:
            between = content[last_obj_end+1:idx].strip()
            if not between.startswith(","):
                prefix = ","

        insert_str = prefix + "\n" + ",\n".join(js_arr) + "\n"
        new_content = content[:idx] + insert_str + content[idx:]

        with open("app.js", "w") as f:
            f.write(new_content)
        print("app.js successfully updated with 52 fruit entries.")
    else:
        print("Error: Could not find closing brace of animals/fruits array in app.js")

if __name__ == "__main__":
    main()
