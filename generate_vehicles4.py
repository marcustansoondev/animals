import os
from PIL import Image, ImageDraw, ImageFilter

def create_image():
    return Image.new('RGBA', (50, 50), (255, 255, 255, 0))

def draw_lowrider(d):
    # Extremely detailed lowrider with pinstriping, wire wheels, hydraulics lifted
    # Shadow
    d.ellipse([5, 42, 45, 48], fill=(30, 30, 30, 100))
    # Wheels
    for x in [12, 38]:
        d.ellipse([x-5, 35, x+5, 45], fill=(20, 20, 20))
        d.ellipse([x-4, 36, x+4, 44], fill=(200, 200, 200)) # whitewall
        d.ellipse([x-2, 38, x+2, 42], fill=(255, 215, 0)) # gold rims
        for i in range(4): # Spokes
            d.line([x, 37+i, x, 43-i], fill=(255,255,255))
    # Body lower
    d.polygon([(4, 35), (46, 30), (48, 32), (48, 38), (4, 38)], fill=(138, 43, 226))
    d.polygon([(4, 35), (46, 30), (45, 32), (4, 36)], fill=(180, 80, 250)) # highlight
    # Pinstriping
    d.line([(5, 33), (45, 29)], fill=(255, 215, 0), width=1)
    # Cabin
    d.polygon([(12, 33), (18, 22), (32, 20), (38, 28)], fill=(15, 15, 15))
    d.polygon([(13, 32), (18, 24), (24, 23), (24, 31)], fill=(100, 150, 200, 150)) # Window left
    d.polygon([(26, 31), (26, 22), (31, 22), (35, 27)], fill=(100, 150, 200, 150)) # Window right
    # Highlights
    d.line([(18, 22), (32, 20)], fill=(200, 200, 200), width=1)
    # Bumper and grille
    d.rectangle([4, 35, 6, 38], fill=(220, 220, 220))
    d.rectangle([46, 30, 49, 36], fill=(220, 220, 220))
    d.ellipse([47, 31, 48, 33], fill=(255, 255, 0)) # headlight

def draw_apc(d):
    # Armored Personnel Carrier: 8 wheels, angles, rivets, camo pattern, turret
    d.ellipse([5, 42, 45, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [10, 20, 30, 40]:
        d.ellipse([x-4, 36, x+4, 44], fill=(20, 20, 20))
        d.ellipse([x-2, 38, x+2, 42], fill=(80, 80, 80))
        d.ellipse([x-1, 39, x+1, 41], fill=(40, 40, 40))
    # Hull base
    d.polygon([(4, 38), (4, 28), (10, 24), (35, 24), (45, 28), (46, 38)], fill=(60, 80, 60))
    # Camo
    d.polygon([(4, 34), (8, 30), (16, 34), (18, 38)], fill=(40, 50, 40))
    d.polygon([(25, 24), (30, 28), (40, 26), (36, 24)], fill=(40, 50, 40))
    d.polygon([(30, 38), (35, 32), (45, 36), (46, 38)], fill=(80, 100, 80))
    # Turret
    d.polygon([(18, 24), (20, 18), (28, 18), (30, 24)], fill=(60, 80, 60))
    # Gun barrel
    d.rectangle([28, 19, 44, 21], fill=(40, 40, 40))
    d.rectangle([40, 18, 43, 22], fill=(30, 30, 30)) # muzzle brake
    # Details and rivets
    for x in range(6, 44, 4):
        d.point((x, 37), fill=(30, 40, 30))
        d.point((x, 26), fill=(80, 100, 80))
    # Hatches
    d.rectangle([22, 16, 26, 18], fill=(50, 70, 50))
    # Front angled highlight
    d.line([(45, 28), (35, 24)], fill=(100, 120, 100), width=1)

def draw_lawn_mower(d):
    # Ride-on lawn mower
    d.ellipse([8, 42, 42, 45], fill=(0, 0, 0, 120))
    # Wheels
    d.ellipse([10, 32, 20, 42], fill=(20, 20, 20)) # Rear large wheel
    d.ellipse([13, 35, 17, 39], fill=(200, 200, 200))
    d.ellipse([34, 36, 40, 42], fill=(20, 20, 20)) # Front small wheel
    d.ellipse([36, 38, 38, 40], fill=(200, 200, 200))
    # Mower deck
    d.polygon([(20, 40), (34, 40), (32, 37), (22, 37)], fill=(200, 50, 50))
    d.rectangle([26, 37, 28, 39], fill=(50, 50, 50))
    # Chassis
    d.polygon([(10, 32), (10, 24), (20, 24), (22, 30), (35, 30), (38, 36), (20, 36)], fill=(50, 150, 50))
    # Highlights
    d.line([(10, 24), (20, 24), (22, 30), (35, 30)], fill=(100, 200, 100), width=1)
    # Seat
    d.polygon([(12, 24), (12, 18), (14, 18), (14, 24), (18, 24), (18, 22), (14, 22)], fill=(20, 20, 20))
    # Steering wheel
    d.line([(22, 28), (20, 20)], fill=(40, 40, 40), width=2)
    d.ellipse([18, 18, 22, 20], fill=(30, 30, 30))
    # Engine details
    d.rectangle([26, 26, 32, 30], fill=(100, 100, 100))
    d.line([(26, 27), (32, 27)], fill=(60, 60, 60))
    d.line([(26, 29), (32, 29)], fill=(60, 60, 60))

def draw_hearse(d):
    # Hearse: Long black car with large rear windows, drapery
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [12, 38]:
        d.ellipse([x-5, 36, x+5, 46], fill=(20, 20, 20))
        d.ellipse([x-2, 39, x+2, 43], fill=(200, 200, 200))
    # Lower Body
    d.polygon([(2, 36), (48, 36), (46, 28), (4, 28)], fill=(20, 20, 20))
    # Silver trim
    d.line([(4, 28), (46, 28)], fill=(150, 150, 150), width=1)
    d.line([(2, 36), (48, 36)], fill=(100, 100, 100), width=1)
    # Cabin / Roof
    d.polygon([(4, 28), (6, 16), (30, 16), (36, 28)], fill=(30, 30, 30))
    d.line([(6, 16), (30, 16)], fill=(80, 80, 80), width=1)
    # Front Window
    d.polygon([(28, 27), (26, 18), (31, 18), (35, 27)], fill=(80, 100, 120, 180))
    # Side Windows
    d.polygon([(8, 27), (9, 18), (16, 18), (16, 27)], fill=(80, 100, 120, 180))
    d.polygon([(18, 27), (18, 18), (24, 18), (24, 27)], fill=(80, 100, 120, 180))
    # Drapery inside windows
    for x_start in [8, 18]:
        d.polygon([(x_start, 18), (x_start+2, 27), (x_start+8, 27), (x_start+6, 18)], fill=(100, 20, 20, 150))
    # Ornaments
    d.polygon([(2, 34), (4, 32), (4, 36)], fill=(220, 220, 220)) # Tail light
    d.ellipse([46, 32, 49, 35], fill=(255, 255, 150)) # Headlight

def draw_microcar(d):
    # Tiny bubble-like microcar
    d.ellipse([10, 40, 40, 44], fill=(0, 0, 0, 150))
    for x in [16, 34]:
        d.ellipse([x-4, 36, x+4, 44], fill=(30, 30, 30))
        d.ellipse([x-1, 39, x+1, 41], fill=(220, 220, 220))
    # Body
    d.ellipse([12, 20, 38, 38], fill=(255, 165, 0))
    d.ellipse([14, 22, 35, 35], fill=(255, 200, 80)) # Highlight
    # Windows
    d.polygon([(18, 26), (32, 26), (35, 32), (15, 32)], fill=(150, 200, 255, 200))
    d.line([(25, 26), (25, 32)], fill=(20, 20, 20), width=1) # Window split
    d.polygon([(19, 27), (24, 27), (24, 31), (16, 31)], fill=(200, 230, 255, 200)) # Glass reflection
    # Headlight
    d.ellipse([34, 30, 38, 34], fill=(255, 255, 200))
    d.ellipse([35, 31, 37, 33], fill=(255, 255, 255))
    # Tail light
    d.ellipse([12, 30, 14, 34], fill=(255, 50, 50))
    # Bumper
    d.line([(12, 37), (38, 37)], fill=(150, 150, 150), width=2)

def draw_bucket_wheel_excavator(d):
    # Massive excavator: Complex truss, huge wheel
    # Base crawler
    d.polygon([(10, 42), (40, 42), (42, 46), (8, 46)], fill=(50, 50, 50))
    for i in range(10, 42, 4):
        d.ellipse([i, 43, i+3, 46], fill=(30, 30, 30))
    # Main body / Cab
    d.polygon([(15, 36), (35, 36), (35, 42), (15, 42)], fill=(200, 180, 50))
    d.polygon([(18, 32), (28, 32), (28, 36), (18, 36)], fill=(150, 130, 40))
    d.rectangle([20, 33, 26, 35], fill=(50, 100, 150)) # Window
    # Counterweight boom
    d.polygon([(18, 34), (4, 38), (4, 40), (18, 36)], fill=(180, 160, 40))
    d.rectangle([2, 37, 6, 42], fill=(80, 80, 80))
    # Main boom truss
    d.polygon([(25, 36), (42, 22), (44, 24), (25, 38)], fill=(180, 160, 40))
    # Truss cross-beams
    for i in range(4):
        x = 28 + i * 3
        y = 35 - i * 3
        d.line([(x, y), (x+3, y-1)], fill=(100, 80, 20), width=1)
    # Bucket Wheel
    cx, cy = 43, 23
    r = 7
    d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(50, 50, 50), width=2)
    # Buckets
    import math
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        bx = cx + r * math.cos(rad)
        by = cy + r * math.sin(rad)
        d.ellipse([bx-1.5, by-1.5, bx+1.5, by+1.5], fill=(100, 100, 100))
        d.line([(cx, cy), (bx, by)], fill=(100, 100, 100), width=1)

def draw_bubble_car(d):
    # Classic Isetta style bubble car
    d.ellipse([12, 42, 38, 45], fill=(0, 0, 0, 150))
    d.ellipse([14, 20, 36, 40], fill=(220, 50, 50))
    d.ellipse([16, 22, 32, 36], fill=(250, 100, 100)) # Highlight
    # Wheels
    d.ellipse([16, 36, 22, 44], fill=(20, 20, 20))
    d.ellipse([30, 36, 36, 44], fill=(20, 20, 20))
    d.ellipse([18, 38, 20, 42], fill=(200, 200, 200))
    d.ellipse([32, 38, 34, 42], fill=(200, 200, 200))
    # Front door (entire front opens)
    d.arc([14, 20, 36, 40], start=270, end=90, fill=(150, 20, 20), width=1)
    d.line([(36, 20), (36, 40)], fill=(150, 20, 20), width=1)
    # Huge panoramic window
    d.polygon([(18, 22), (34, 22), (36, 28), (16, 28)], fill=(180, 220, 255, 180))
    d.polygon([(20, 23), (32, 23), (33, 27), (18, 27)], fill=(230, 240, 255, 180))
    # Headlights mounted high
    d.ellipse([32, 32, 36, 36], fill=(255, 255, 200))
    d.ellipse([33, 33, 35, 35], fill=(255, 255, 255))
    # Door handle
    d.rectangle([34, 30, 36, 31], fill=(200, 200, 200))

def draw_trireme(d):
    # Ancient Greek Trireme, 3 tiers of oars, bronze ram
    d.ellipse([4, 40, 46, 44], fill=(0, 50, 100, 100))
    # Hull
    d.polygon([(6, 32), (40, 34), (46, 38), (38, 42), (10, 42), (4, 38)], fill=(120, 70, 30))
    d.polygon([(6, 32), (40, 34), (42, 36), (8, 36)], fill=(150, 100, 50)) # Highlight
    # Bronze Ram
    d.polygon([(40, 38), (48, 40), (46, 42), (38, 42)], fill=(180, 130, 30))
    d.ellipse([46, 39, 49, 41], fill=(255, 200, 50))
    # Eye painted on bow
    d.ellipse([38, 35, 42, 37], fill=(255, 255, 255))
    d.ellipse([39, 35.5, 41, 36.5], fill=(0, 0, 0))
    # 3 tiers of oars
    for y, length in [(36, 5), (38, 6), (40, 7)]:
        for x in range(12, 36, 3):
            d.line([(x, y), (x+length, y+3)], fill=(200, 180, 150), width=1)
    # Mast and Sail
    d.line([(24, 10), (24, 34)], fill=(100, 50, 20), width=2)
    d.polygon([(14, 14), (34, 14), (32, 28), (16, 28)], fill=(240, 230, 210))
    d.line([(14, 14), (34, 14)], fill=(100, 50, 20), width=2) # Yardarm
    # Sail folds
    for i in range(16, 28, 3):
        d.line([(15, i), (33, i)], fill=(200, 190, 170), width=1)

def draw_chinese_junk(d):
    # Traditional Chinese Junk ship: high stern, battened sails
    d.ellipse([5, 40, 45, 44], fill=(0, 50, 100, 100))
    # Hull
    d.polygon([(8, 28), (16, 34), (38, 36), (44, 30), (40, 42), (12, 40)], fill=(139, 69, 19))
    # Hull highlight & planks
    d.polygon([(10, 30), (16, 34), (38, 36), (42, 32)], fill=(160, 82, 45))
    for y in range(36, 40, 2):
        d.line([(14, y), (38, y)], fill=(100, 50, 10), width=1)
    # Stern gallery
    d.rectangle([8, 24, 14, 28], fill=(200, 50, 50))
    d.rectangle([9, 25, 11, 27], fill=(255, 255, 0)) # Window
    # Masts
    d.line([(18, 15), (18, 36)], fill=(100, 50, 20), width=2)
    d.line([(30, 8), (30, 36)], fill=(100, 50, 20), width=2)
    # Battened Sails (Red)
    # Main sail
    d.polygon([(22, 10), (38, 12), (40, 32), (30, 32)], fill=(180, 40, 40))
    for y in range(12, 32, 4):
        d.line([(25+ (y-10)//3, y), (38+(y-10)//5, y)], fill=(50, 20, 20), width=1)
    # Fore sail
    d.polygon([(12, 18), (22, 20), (22, 34), (18, 34)], fill=(180, 40, 40))
    for y in range(20, 34, 3):
        d.line([(14+ (y-20)//3, y), (22, y)], fill=(50, 20, 20), width=1)

def draw_fireboat(d):
    # Fireboat spraying water
    d.ellipse([4, 40, 46, 45], fill=(0, 50, 100, 100))
    # Hull
    d.polygon([(4, 32), (42, 32), (46, 38), (38, 42), (8, 42)], fill=(200, 30, 30))
    d.polygon([(4, 32), (42, 32), (44, 35), (6, 35)], fill=(250, 80, 80)) # Red highlight
    d.line([(4, 32), (42, 32)], fill=(255, 255, 255), width=2) # White stripe
    # Cabin
    d.polygon([(12, 32), (16, 24), (28, 24), (28, 32)], fill=(255, 255, 255))
    d.rectangle([17, 26, 21, 30], fill=(100, 150, 200)) # Window
    d.rectangle([23, 26, 27, 30], fill=(100, 150, 200)) # Window
    # Radar / lights
    d.rectangle([20, 20, 22, 24], fill=(150, 150, 150))
    d.ellipse([20, 18, 22, 20], fill=(255, 50, 50)) # Siren
    # Water cannons
    d.polygon([(34, 32), (36, 28), (38, 28), (36, 32)], fill=(180, 180, 180))
    d.polygon([(8, 32), (10, 26), (12, 26), (10, 32)], fill=(180, 180, 180))
    # Water spray (arcs of blue/white)
    for i in range(5):
        d.arc([36, 15+i, 48, 35+i], start=180, end=270, fill=(150, 200, 255, 180), width=1)
        d.arc([2, 10+i, 12, 30+i], start=270, end=0, fill=(150, 200, 255, 180), width=1)

def draw_luxury_yacht(d):
    # Sleek modern luxury yacht: sharp lines, tinted windows
    d.ellipse([4, 40, 46, 45], fill=(0, 50, 100, 100))
    # Hull
    d.polygon([(4, 30), (40, 30), (48, 36), (36, 42), (8, 42)], fill=(240, 240, 240))
    d.polygon([(4, 30), (40, 30), (43, 34), (6, 34)], fill=(255, 255, 255))
    # Lower hull stripe
    d.polygon([(8, 38), (42, 34), (45, 36), (36, 42)], fill=(20, 20, 40))
    # Superstructure
    d.polygon([(10, 30), (14, 22), (32, 22), (36, 30)], fill=(220, 220, 220))
    d.polygon([(16, 22), (18, 16), (28, 16), (30, 22)], fill=(200, 200, 200))
    # Tinted Windows
    d.polygon([(11, 29), (15, 23), (31, 23), (35, 29)], fill=(10, 10, 20, 200))
    d.polygon([(17, 21), (19, 17), (27, 17), (29, 21)], fill=(10, 10, 20, 200))
    # Decks and railings
    d.line([(4, 30), (40, 30)], fill=(150, 150, 150), width=1)
    d.line([(10, 22), (32, 22)], fill=(150, 150, 150), width=1)
    # Radar dome
    d.ellipse([21, 13, 25, 16], fill=(255, 255, 255))
    d.rectangle([22, 15, 24, 16], fill=(100, 100, 100))
    # Helipad at stern
    d.ellipse([6, 29, 14, 31], fill=(100, 100, 100))
    d.ellipse([8, 29.5, 12, 30.5], outline=(200, 200, 50))

def draw_trimaran(d):
    # Multi-hull racing sailboat
    d.ellipse([4, 40, 46, 44], fill=(0, 50, 100, 100))
    # Main hull
    d.polygon([(10, 36), (40, 36), (44, 40), (12, 40)], fill=(255, 255, 255))
    d.polygon([(10, 36), (40, 36), (42, 38), (11, 38)], fill=(200, 200, 200))
    # Outrigger hull (foreground)
    d.polygon([(16, 42), (36, 38), (46, 42), (18, 44)], fill=(255, 50, 50))
    d.polygon([(16, 42), (36, 38), (40, 40), (17, 43)], fill=(255, 100, 100))
    # Crossbeams
    d.polygon([(20, 36), (22, 40), (24, 40), (22, 36)], fill=(100, 100, 100))
    d.polygon([(30, 36), (36, 39), (38, 39), (32, 36)], fill=(100, 100, 100))
    # Mast
    d.line([(26, 10), (26, 36)], fill=(50, 50, 50), width=2)
    # High-tech sails
    d.polygon([(27, 12), (40, 34), (27, 34)], fill=(200, 220, 255, 200)) # Mainsail
    d.polygon([(25, 16), (12, 34), (25, 34)], fill=(150, 200, 255, 200)) # Jib
    # Sail logos/patterns
    d.polygon([(28, 18), (34, 28), (28, 28)], fill=(50, 100, 200))

def draw_bathysphere(d):
    # Deep sea spherical submersible
    # Water background glow
    d.ellipse([10, 10, 40, 40], fill=(10, 30, 60, 100))
    # Spherical hull
    d.ellipse([15, 15, 35, 35], fill=(200, 180, 50))
    d.ellipse([17, 17, 30, 30], fill=(255, 230, 80)) # Highlight
    d.ellipse([20, 28, 35, 35], fill=(150, 130, 30)) # Shadow
    # Huge thick front window
    d.ellipse([22, 20, 30, 28], fill=(100, 100, 100)) # Rim
    d.ellipse([23, 21, 29, 27], fill=(50, 150, 200)) # Glass
    d.ellipse([24, 22, 27, 25], fill=(150, 200, 255)) # Glass highlight
    # Bolts on rim
    for angle in range(0, 360, 45):
        import math
        rad = math.radians(angle)
        x = 26 + 3.5 * math.cos(rad)
        y = 24 + 3.5 * math.sin(rad)
        d.point((x, y), fill=(50, 50, 50))
    # Top hatch
    d.rectangle([22, 12, 28, 15], fill=(180, 160, 40))
    d.line([(25, 10), (25, 12)], fill=(100, 100, 100), width=2) # Cable attach
    # Light fixtures
    d.polygon([(34, 22), (38, 20), (38, 24)], fill=(100, 100, 100))
    d.polygon([(38, 18), (48, 12), (48, 30)], fill=(255, 255, 150, 100)) # Beam

def draw_dhow(d):
    # Traditional Arab sailing vessel: long thin hull, lateen sail
    d.ellipse([5, 40, 45, 44], fill=(0, 50, 100, 100))
    # Hull
    d.polygon([(6, 30), (14, 36), (36, 36), (46, 28), (40, 42), (10, 42)], fill=(139, 69, 19))
    d.polygon([(8, 32), (14, 36), (36, 36), (42, 30)], fill=(160, 82, 45)) # Highlight
    # Hull planks
    for y in range(36, 42, 2):
        d.line([(10+(y-36), y), (40-(y-36)//2, y)], fill=(100, 50, 10), width=1)
    # Aft cabin/deck
    d.polygon([(6, 26), (12, 30), (16, 30), (10, 26)], fill=(200, 180, 150))
    # Mast, raked forward
    d.line([(24, 36), (30, 12)], fill=(100, 50, 20), width=2)
    # Lateen Sail (Triangular, attached to long yard)
    d.line([(10, 32), (42, 6)], fill=(80, 40, 10), width=2) # Yard
    d.polygon([(12, 30), (40, 8), (28, 34)], fill=(240, 230, 210))
    # Sail shading
    d.polygon([(26, 20), (38, 10), (28, 34)], fill=(200, 190, 170))
    # Rigging
    d.line([(30, 12), (46, 28)], fill=(50, 50, 50), width=1)
    d.line([(30, 12), (6, 30)], fill=(50, 50, 50), width=1)

def draw_gyrocopter(d):
    # Small helicopter-like aircraft with unpowered rotor and rear pusher prop
    # Air frame
    d.polygon([(12, 34), (20, 28), (30, 28), (26, 36), (16, 36)], fill=(200, 50, 50))
    d.polygon([(14, 32), (20, 28), (28, 28), (24, 34)], fill=(255, 100, 100)) # Highlight
    # Tail boom
    d.line([(28, 32), (42, 30)], fill=(150, 150, 150), width=2)
    # Tail fin
    d.polygon([(40, 30), (44, 24), (44, 34)], fill=(50, 50, 200))
    # Landing gear
    d.line([(16, 36), (14, 42)], fill=(100, 100, 100), width=1)
    d.line([(24, 36), (26, 42)], fill=(100, 100, 100), width=1)
    d.ellipse([12, 40, 16, 44], fill=(20, 20, 20))
    d.ellipse([24, 40, 28, 44], fill=(20, 20, 20))
    # Pilot seat & pilot (abstract)
    d.rectangle([20, 24, 24, 28], fill=(50, 50, 50))
    d.ellipse([21, 20, 25, 24], fill=(200, 180, 150)) # Helmet
    # Top Rotor mast
    d.line([(24, 28), (24, 16)], fill=(100, 100, 100), width=2)
    # Top Rotor blades (blurred disc)
    d.ellipse([6, 14, 42, 18], fill=(150, 150, 150, 100))
    d.line([(6, 16), (42, 16)], fill=(100, 100, 100, 150), width=1)
    # Rear Pusher Prop
    d.line([(30, 26), (30, 36)], fill=(150, 150, 150), width=2)
    d.ellipse([28, 24, 32, 38], fill=(150, 150, 150, 100))

def draw_tiltrotor(d):
    # Aircraft like V-22 Osprey: large rotors on wingtips tilted up
    # Fuselage
    d.polygon([(6, 28), (36, 28), (44, 26), (46, 24), (36, 24), (8, 24)], fill=(100, 120, 100))
    d.polygon([(8, 24), (36, 24), (34, 26), (10, 26)], fill=(140, 160, 140)) # Highlight
    # Cockpit
    d.polygon([(8, 26), (14, 22), (20, 22), (22, 24), (8, 24)], fill=(50, 150, 200, 200))
    # Tail fin
    d.polygon([(40, 24), (44, 16), (46, 16), (44, 24)], fill=(80, 100, 80))
    # Wings (seen from slight angle)
    d.polygon([(20, 26), (30, 20), (32, 20), (24, 26)], fill=(90, 110, 90)) # Far wing
    d.polygon([(18, 26), (28, 34), (30, 34), (22, 26)], fill=(110, 130, 110)) # Near wing
    # Nacelles and Rotors (tilted up 45 degrees)
    # Far nacelle
    d.polygon([(28, 20), (32, 16), (34, 18), (30, 22)], fill=(80, 100, 80))
    d.ellipse([26, 10, 38, 14], fill=(150, 150, 150, 150)) # Rotor blur
    # Near nacelle
    d.polygon([(26, 34), (30, 28), (34, 30), (30, 36)], fill=(100, 120, 100))
    d.ellipse([20, 26, 38, 32], fill=(200, 200, 200, 150)) # Rotor blur
    # Details
    d.line([(6, 26), (36, 26)], fill=(80, 100, 80), width=1) # Panel line

def draw_stealth_bomber(d):
    # B-2 Spirit flying wing
    # Flying wing shape
    d.polygon([(25, 10), (46, 30), (35, 34), (25, 28), (15, 34), (4, 30)], fill=(30, 30, 30))
    d.polygon([(25, 12), (40, 28), (35, 30), (25, 26), (15, 30), (10, 28)], fill=(60, 60, 60)) # Highlight
    d.polygon([(25, 10), (35, 20), (25, 26), (15, 20)], fill=(40, 40, 40)) # Center hump
    # Cockpit
    d.polygon([(24, 14), (26, 14), (27, 18), (23, 18)], fill=(10, 10, 30))
    # Engine intakes/exhausts
    d.polygon([(18, 24), (22, 22), (24, 26), (20, 28)], fill=(10, 10, 10))
    d.polygon([(28, 22), (32, 24), (30, 28), (26, 26)], fill=(10, 10, 10))
    # Trailing edge zig-zag details
    d.line([(15, 34), (25, 28)], fill=(20, 20, 20), width=2)
    d.line([(25, 28), (35, 34)], fill=(20, 20, 20), width=2)
    # Subtle panel lines
    d.line([(25, 10), (25, 28)], fill=(50, 50, 50), width=1)

def draw_triplane(d):
    # WWI Triplane (like the Red Baron)
    # Fuselage
    d.polygon([(12, 28), (36, 28), (42, 26), (36, 24), (12, 24)], fill=(200, 30, 30))
    d.polygon([(14, 24), (36, 24), (34, 26), (14, 26)], fill=(255, 80, 80)) # Highlight
    # Tail
    d.polygon([(38, 24), (44, 18), (46, 22), (42, 26)], fill=(200, 30, 30))
    d.line([(44, 18), (46, 22)], fill=(255, 255, 255), width=2) # Rudder stripe
    # Cockpit
    d.arc([22, 22, 26, 26], start=180, end=0, fill=(50, 50, 50), width=2)
    d.ellipse([23, 18, 26, 22], fill=(150, 100, 50)) # Pilot leather cap
    # Engine and Propeller
    d.rectangle([8, 23, 12, 29], fill=(100, 100, 100))
    d.ellipse([6, 14, 10, 38], fill=(200, 200, 200, 150)) # Spinning prop
    d.ellipse([7, 24, 9, 28], fill=(50, 50, 50)) # Prop hub
    # 3 Wings
    for y in [16, 22, 28]:
        d.polygon([(14, y), (26, y-4), (30, y-2), (18, y+2)], fill=(220, 40, 40))
        d.polygon([(14, y), (26, y-4), (28, y-3), (16, y+1)], fill=(255, 100, 100)) # Wing highlight
    # Wing struts
    d.line([(18, 18), (18, 30)], fill=(100, 80, 50), width=1)
    d.line([(24, 14), (24, 26)], fill=(100, 80, 50), width=1)
    # Landing gear
    d.line([(16, 30), (14, 38)], fill=(100, 100, 100), width=1)
    d.line([(20, 30), (22, 38)], fill=(100, 100, 100), width=1)
    d.ellipse([12, 36, 16, 42], fill=(20, 20, 20))
    d.ellipse([20, 36, 24, 42], fill=(20, 20, 20))

def draw_wingsuit(d):
    # Person flying in a wingsuit (top-down / angled view)
    # Body/Suit core
    d.polygon([(25, 10), (32, 20), (30, 40), (20, 40), (18, 20)], fill=(255, 100, 0))
    # Highlight
    d.polygon([(25, 12), (30, 20), (28, 38), (22, 38), (20, 20)], fill=(255, 150, 50))
    # Helmet
    d.ellipse([22, 8, 28, 14], fill=(50, 50, 50))
    d.ellipse([23, 9, 27, 11], fill=(200, 200, 255)) # Visor
    # Arm wings
    d.polygon([(22, 16), (6, 26), (18, 30), (20, 24)], fill=(200, 50, 0))
    d.polygon([(28, 16), (44, 26), (32, 30), (30, 24)], fill=(200, 50, 0))
    # Leg wing
    d.polygon([(22, 30), (16, 42), (25, 46), (34, 42), (28, 30)], fill=(200, 50, 0))
    # Straps and details
    d.line([(20, 20), (30, 20)], fill=(50, 50, 50), width=2)
    d.line([(22, 30), (28, 30)], fill=(50, 50, 50), width=2)
    # Air trails
    d.line([(6, 26), (2, 36)], fill=(200, 220, 255, 150), width=1)
    d.line([(44, 26), (48, 36)], fill=(200, 220, 255, 150), width=1)
    d.line([(25, 46), (25, 49)], fill=(200, 220, 255, 150), width=2)

def draw_spaceplane(d):
    # Futuristic spaceplane (like Space Shuttle or X-37) returning to earth
    # Plasma trail (re-entry)
    d.polygon([(2, 34), (16, 26), (20, 42), (10, 48)], fill=(255, 100, 0, 150))
    d.polygon([(4, 36), (14, 28), (18, 40), (12, 46)], fill=(255, 200, 0, 200))
    # Fuselage
    d.polygon([(36, 12), (46, 18), (30, 36), (20, 30)], fill=(240, 240, 240))
    d.polygon([(36, 12), (44, 18), (32, 32), (24, 28)], fill=(255, 255, 255)) # Highlight
    # Heat shield (black belly)
    d.polygon([(20, 30), (30, 36), (26, 40), (16, 34)], fill=(30, 30, 30))
    # Delta wings
    d.polygon([(32, 20), (44, 26), (38, 32)], fill=(220, 220, 220)) # Right wing
    d.polygon([(26, 16), (20, 8), (16, 24)], fill=(200, 200, 200)) # Left wing
    # Black wing leading edges
    d.line([(44, 26), (32, 20)], fill=(30, 30, 30), width=2)
    d.line([(20, 8), (26, 16)], fill=(30, 30, 30), width=2)
    # Tail fin
    d.polygon([(26, 30), (18, 22), (22, 26)], fill=(220, 220, 220))
    # Cockpit windows
    d.polygon([(36, 16), (40, 18), (38, 20), (34, 18)], fill=(50, 100, 150))
    # Engines
    d.ellipse([18, 32, 22, 36], fill=(100, 100, 100))
    d.ellipse([22, 34, 26, 38], fill=(100, 100, 100))
    d.ellipse([19, 33, 21, 35], fill=(255, 200, 100)) # Glow

def draw_turbotrain(d):
    # Sleek high-speed train with turbine engine on top
    # Track
    d.line([(0, 44), (50, 44)], fill=(100, 100, 100), width=2)
    d.line([(0, 46), (50, 46)], fill=(150, 150, 150), width=1)
    # Train Body
    d.polygon([(4, 42), (40, 42), (46, 36), (40, 26), (4, 26)], fill=(200, 200, 200))
    d.polygon([(4, 42), (40, 42), (45, 36), (40, 30), (4, 30)], fill=(240, 240, 240)) # Highlight
    # Red styling stripe
    d.polygon([(4, 34), (42, 34), (44, 36), (42, 38), (4, 38)], fill=(220, 30, 30))
    # Windows
    for x in range(8, 36, 6):
        d.rectangle([x, 30, x+4, 33], fill=(30, 30, 40))
    # Front angled window
    d.polygon([(41, 30), (44, 33), (41, 33)], fill=(30, 30, 40))
    # Jet Turbine on roof
    d.rectangle([10, 20, 26, 26], fill=(150, 150, 150))
    d.polygon([(26, 20), (30, 22), (30, 24), (26, 26)], fill=(100, 100, 100)) # Intake
    d.polygon([(10, 20), (6, 22), (6, 24), (10, 26)], fill=(50, 50, 50)) # Exhaust
    # Exhaust smoke/fire
    d.polygon([(6, 22), (2, 20), (2, 26), (6, 24)], fill=(255, 150, 50, 150))
    # Bogies/Wheels
    d.rectangle([8, 42, 16, 44], fill=(50, 50, 50))
    d.rectangle([32, 42, 40, 44], fill=(50, 50, 50))

def draw_hyperloop_pod(d):
    # Futuristic pod inside a transparent tube
    # Tube (Glass)
    d.arc([2, 10, 48, 48], start=180, end=0, fill=(200, 240, 255, 100), width=2)
    d.arc([2, 10, 48, 48], start=0, end=180, fill=(150, 200, 255, 150), width=4)
    # Tube structural rings
    for x in [10, 25, 40]:
        d.ellipse([x-2, 12, x+2, 46], outline=(150, 180, 200), width=1)
    # The Pod
    d.polygon([(10, 32), (36, 32), (42, 28), (36, 24), (10, 24), (6, 28)], fill=(255, 255, 255))
    d.polygon([(10, 30), (36, 30), (40, 28), (36, 26), (10, 26)], fill=(200, 200, 200)) # Shadow
    # Pod blue accent lights
    d.line([(12, 28), (38, 28)], fill=(0, 255, 255), width=1)
    # Maglev track base
    d.rectangle([8, 34, 42, 38], fill=(100, 100, 100))
    d.rectangle([10, 32, 40, 34], fill=(50, 50, 50))
    # Magnetic glow
    d.line([(10, 33), (40, 33)], fill=(100, 150, 255), width=2)
    # Pod windows (slim)
    d.line([(14, 26), (34, 26)], fill=(20, 20, 20), width=2)

def draw_container_flatcar(d):
    # Freight train flatcar carrying two colorful shipping containers
    # Track
    d.line([(0, 44), (50, 44)], fill=(100, 100, 100), width=2)
    # Flatcar chassis
    d.rectangle([4, 38, 46, 42], fill=(80, 20, 20))
    d.rectangle([4, 38, 46, 39], fill=(120, 40, 40)) # Highlight
    # Wheels
    for x in [8, 14, 36, 42]:
        d.ellipse([x-3, 41, x+3, 46], fill=(40, 40, 40))
        d.ellipse([x-1, 43, x+1, 45], fill=(100, 100, 100))
    # Couplers
    d.rectangle([0, 39, 4, 41], fill=(50, 50, 50))
    d.rectangle([46, 39, 50, 41], fill=(50, 50, 50))
    # Container 1 (Blue)
    d.rectangle([6, 20, 24, 38], fill=(30, 80, 150))
    d.rectangle([6, 20, 24, 22], fill=(50, 120, 200)) # Top highlight
    # Container 1 ribs
    for x in range(8, 24, 2):
        d.line([(x, 22), (x, 38)], fill=(20, 60, 120), width=1)
    # Container 1 logo
    d.rectangle([10, 26, 20, 30], fill=(255, 255, 255))
    d.line([(12, 28), (18, 28)], fill=(255, 0, 0), width=2)
    # Container 2 (Orange)
    d.rectangle([26, 20, 44, 38], fill=(200, 100, 30))
    d.rectangle([26, 20, 44, 22], fill=(250, 140, 50)) # Top highlight
    # Container 2 ribs
    for x in range(28, 44, 2):
        d.line([(x, 22), (x, 38)], fill=(160, 80, 20), width=1)
    # Container 2 markings
    d.rectangle([38, 22, 42, 28], fill=(255, 255, 255))

def draw_suspension_railway(d):
    # Wuppertal style hanging monorail
    # Overhead track beam
    d.rectangle([0, 6, 50, 12], fill=(100, 120, 100))
    d.line([(0, 12), (50, 12)], fill=(50, 70, 50), width=2) # Shadow
    # Support pillars/truss
    d.line([(20, 6), (15, 0)], fill=(80, 100, 80), width=2)
    d.line([(30, 6), (35, 0)], fill=(80, 100, 80), width=2)
    # Bogies on track
    d.rectangle([12, 10, 18, 14], fill=(50, 50, 50))
    d.rectangle([32, 10, 38, 14], fill=(50, 50, 50))
    # Suspension arms
    d.polygon([(14, 14), (16, 14), (18, 20), (12, 20)], fill=(200, 50, 50))
    d.polygon([(34, 14), (36, 14), (38, 20), (32, 20)], fill=(200, 50, 50))
    # Train car
    d.polygon([(6, 20), (44, 20), (46, 24), (46, 36), (44, 40), (6, 40), (4, 36), (4, 24)], fill=(200, 50, 50))
    d.polygon([(6, 20), (44, 20), (45, 24), (45, 36), (44, 39), (6, 39)], fill=(250, 80, 80)) # Highlight
    # Cream stripe
    d.rectangle([4, 28, 46, 32], fill=(240, 230, 200))
    # Windows
    for x in range(10, 40, 8):
        d.rectangle([x, 22, x+6, 28], fill=(50, 100, 150))
    d.polygon([(4, 24), (8, 24), (8, 28), (4, 28)], fill=(50, 100, 150)) # Front window
    d.polygon([(42, 24), (46, 24), (46, 28), (42, 28)], fill=(50, 100, 150)) # Rear window

def draw_mine_cart(d):
    # Rustic wooden/metal mine cart full of gold/coal on rails
    # Rails and ties
    d.line([(0, 46), (50, 46)], fill=(100, 100, 100), width=2)
    for x in range(5, 50, 10):
        d.rectangle([x, 46, x+4, 48], fill=(80, 50, 30))
    # Wheels (flanged)
    d.ellipse([10, 38, 20, 46], fill=(50, 50, 50))
    d.ellipse([12, 40, 18, 44], fill=(30, 30, 30))
    d.ellipse([30, 38, 40, 46], fill=(50, 50, 50))
    d.ellipse([32, 40, 38, 44], fill=(30, 30, 30))
    # Chassis frame
    d.rectangle([8, 34, 42, 38], fill=(80, 80, 80))
    # Cart body (wood planks)
    d.polygon([(6, 16), (44, 16), (40, 34), (10, 34)], fill=(120, 80, 40))
    for y in range(20, 34, 4):
        d.line([(8 + (y-16)//3, y), (42 - (y-16)//3, y)], fill=(80, 50, 20), width=1)
    # Metal corner brackets
    d.polygon([(6, 16), (10, 16), (12, 34), (10, 34)], fill=(100, 100, 100))
    d.polygon([(40, 16), (44, 16), (40, 34), (38, 34)], fill=(100, 100, 100))
    # Rivets
    for y in range(18, 32, 4):
        d.point((9, y), fill=(50, 50, 50))
        d.point((41, y), fill=(50, 50, 50))
    # Cargo (Gold ore)
    d.polygon([(10, 16), (16, 8), (24, 12), (32, 6), (40, 16)], fill=(255, 215, 0))
    d.polygon([(14, 10), (20, 6), (28, 14), (36, 8), (38, 16)], fill=(218, 165, 32))
    # Sparkles
    d.line([(18, 5), (18, 9)], fill=(255, 255, 255))
    d.line([(16, 7), (20, 7)], fill=(255, 255, 255))

def draw_solar_sail(d):
    # Spacecraft propelled by a massive shiny sail
    # Space background
    d.ellipse([5, 5, 45, 45], fill=(0, 0, 20, 255))
    # Stars
    d.point((10, 10), fill=(255, 255, 255))
    d.point((40, 15), fill=(255, 255, 255))
    d.point((15, 40), fill=(255, 255, 255))
    # Central probe
    d.polygon([(24, 20), (26, 20), (28, 24), (25, 28), (22, 24)], fill=(200, 200, 200))
    d.ellipse([24, 23, 26, 25], fill=(50, 200, 255)) # Lens/sensor
    # Booms supporting sail
    d.line([(25, 24), (4, 4)], fill=(100, 100, 100), width=1)
    d.line([(25, 24), (46, 4)], fill=(100, 100, 100), width=1)
    d.line([(25, 24), (4, 44)], fill=(100, 100, 100), width=1)
    d.line([(25, 24), (46, 44)], fill=(100, 100, 100), width=1)
    # The Sail (ultra-thin reflective material)
    # Drawn in quadrants to allow transparency overlay
    d.polygon([(25, 24), (4, 4), (46, 4)], fill=(200, 230, 255, 100))
    d.polygon([(25, 24), (46, 4), (46, 44)], fill=(180, 210, 255, 100))
    d.polygon([(25, 24), (46, 44), (4, 44)], fill=(150, 180, 255, 100))
    d.polygon([(25, 24), (4, 44), (4, 4)], fill=(180, 210, 255, 100))
    # Sail panel lines (grid)
    for i in range(10, 40, 10):
        d.line([(4, i), (46, i)], fill=(255, 255, 255, 50), width=1)
        d.line([(i, 4), (i, 44)], fill=(255, 255, 255, 50), width=1)
    # Sunlight reflection glare
    d.polygon([(10, 10), (40, 15), (15, 20)], fill=(255, 255, 255, 150))

def draw_space_station(d):
    # Modular orbital station with solar panels and habitation rings
    # Earth curve background
    d.arc([-20, 30, 70, 90], start=180, end=0, fill=(50, 150, 255), width=2)
    # Central core module
    d.rectangle([22, 10, 28, 40], fill=(200, 200, 200))
    d.rectangle([22, 10, 24, 40], fill=(255, 255, 255)) # Highlight
    d.rectangle([26, 10, 28, 40], fill=(150, 150, 150)) # Shadow
    # Habitation Ring (Centrifuge)
    d.ellipse([10, 20, 40, 30], outline=(180, 180, 180), width=4)
    d.ellipse([10, 20, 40, 30], outline=(220, 220, 220), width=1) # Ring highlight
    # Ring connecting spokes
    d.line([(10, 25), (40, 25)], fill=(150, 150, 150), width=2)
    # Solar Panels
    d.polygon([(2, 12), (20, 16), (20, 18), (2, 14)], fill=(50, 80, 180))
    d.polygon([(48, 12), (30, 16), (30, 18), (48, 14)], fill=(50, 80, 180))
    d.polygon([(2, 32), (20, 36), (20, 38), (2, 34)], fill=(50, 80, 180))
    d.polygon([(48, 32), (30, 36), (30, 38), (48, 34)], fill=(50, 80, 180))
    # Panel grid lines
    d.line([(10, 13), (10, 17)], fill=(100, 150, 255), width=1)
    d.line([(40, 13), (40, 17)], fill=(100, 150, 255), width=1)
    # Antennas/dishes
    d.line([(25, 10), (25, 4)], fill=(150, 150, 150), width=1)
    d.arc([22, 2, 28, 6], start=0, end=180, fill=(200, 200, 200), width=1)

def draw_space_tug(d):
    # Utilitarian spaceship for moving cargo/satellites
    # Engine bell
    d.polygon([(6, 20), (14, 22), (14, 28), (6, 30)], fill=(100, 100, 100))
    d.ellipse([4, 20, 8, 30], outline=(80, 80, 80), width=1)
    # Exhaust
    d.polygon([(4, 22), (0, 24), (0, 26), (4, 28)], fill=(0, 255, 255))
    d.polygon([(2, 23), (0, 25), (2, 27)], fill=(255, 255, 255))
    # Main Body (boxy, industrial)
    d.polygon([(14, 16), (34, 16), (36, 20), (36, 30), (34, 34), (14, 34)], fill=(220, 180, 50))
    d.polygon([(14, 16), (34, 16), (35, 20), (35, 30), (34, 32), (14, 32)], fill=(255, 220, 100)) # Highlight
    # Cockpit window
    d.polygon([(30, 20), (36, 22), (36, 28), (30, 30)], fill=(50, 50, 50))
    d.polygon([(32, 22), (35, 24), (35, 26), (32, 28)], fill=(100, 150, 200)) # Reflection
    # Robotic grabber arms
    d.line([(34, 18), (42, 12), (46, 12)], fill=(150, 150, 150), width=2)
    d.line([(34, 32), (42, 38), (46, 38)], fill=(150, 150, 150), width=2)
    # Claws
    d.arc([44, 10, 48, 14], start=90, end=270, fill=(200, 200, 200), width=1)
    d.arc([44, 36, 48, 40], start=90, end=270, fill=(200, 200, 200), width=1)
    # Thruster blocks (RCS)
    d.rectangle([16, 14, 20, 16], fill=(150, 150, 150))
    d.rectangle([16, 34, 20, 36], fill=(150, 150, 150))

def draw_soapbox_car(d):
    # Homemade gravity racer
    # Wheels (bicycle style)
    for x in [10, 40]:
        d.ellipse([x-6, 34, x+6, 46], outline=(50, 50, 50), width=1)
        d.ellipse([x-1, 39, x+1, 41], fill=(100, 100, 100))
        # Spokes
        d.line([(x, 34), (x, 46)], fill=(150, 150, 150), width=1)
        d.line([(x-6, 40), (x+6, 40)], fill=(150, 150, 150), width=1)
    # Axles
    d.line([(10, 40), (40, 40)], fill=(80, 80, 80), width=2)
    # Wooden Body (cigar shape or box)
    d.polygon([(4, 34), (46, 38), (44, 30), (8, 28)], fill=(180, 120, 60))
    # Wood grain lines
    d.line([(6, 32), (44, 36)], fill=(150, 100, 50), width=1)
    d.line([(10, 30), (42, 34)], fill=(150, 100, 50), width=1)
    # Racing Number
    d.ellipse([20, 30, 30, 36], fill=(255, 255, 255))
    # Draw an '8'
    d.ellipse([23, 31, 27, 33], outline=(0, 0, 0), width=1)
    d.ellipse([23, 33, 27, 35], outline=(0, 0, 0), width=1)
    # Driver helmet (kid sticking out)
    d.ellipse([24, 20, 32, 28], fill=(200, 50, 50))
    d.ellipse([28, 22, 32, 26], fill=(50, 50, 50)) # Visor

def draw_mountainboard(d):
    # Oversized off-road skateboard
    # Large pneumatic tires
    for x in [10, 40]:
        d.ellipse([x-6, 36, x+6, 48], fill=(30, 30, 30))
        d.ellipse([x-3, 39, x+3, 45], fill=(200, 200, 200)) # Rims
        # Treads
        for angle in range(0, 360, 45):
            import math
            rad = math.radians(angle)
            px = x + 5 * math.cos(rad)
            py = 42 + 5 * math.sin(rad)
            d.point((px, py), fill=(0, 0, 0))
    # Trucks (suspension)
    d.polygon([(10, 36), (12, 32), (8, 32)], fill=(150, 150, 150))
    d.polygon([(40, 36), (42, 32), (38, 32)], fill=(150, 150, 150))
    # Deck
    d.polygon([(4, 30), (46, 30), (44, 32), (6, 32)], fill=(150, 100, 50))
    # Grip tape pattern
    for i in range(8, 44, 4):
        d.line([(i, 30), (i+2, 32)], fill=(50, 50, 50), width=1)
    # Foot bindings
    d.arc([12, 26, 20, 30], start=180, end=0, fill=(20, 20, 20), width=2)
    d.arc([30, 26, 38, 30], start=180, end=0, fill=(20, 20, 20), width=2)

def draw_quadricycle(d):
    # 4-wheeled human-powered pedal car (surrey bike)
    # Wheels
    for x in [10, 40]:
        d.ellipse([x-6, 36, x+6, 48], outline=(20, 20, 20), width=1)
        d.ellipse([x-1, 41, x+1, 43], fill=(100, 100, 100))
        d.line([(x, 36), (x, 48)], fill=(150, 150, 150), width=1)
        d.line([(x-6, 42), (x+6, 42)], fill=(150, 150, 150), width=1)
    # Chassis
    d.rectangle([8, 40, 42, 42], fill=(200, 50, 50))
    # Seats (bench style)
    d.polygon([(14, 40), (14, 32), (24, 32), (24, 40)], fill=(50, 50, 50))
    d.polygon([(26, 40), (26, 32), (36, 32), (36, 40)], fill=(50, 50, 50))
    # Pedals and chains
    d.ellipse([18, 42, 22, 46], outline=(150, 150, 150), width=1)
    d.ellipse([30, 42, 34, 46], outline=(150, 150, 150), width=1)
    # Canopy supports
    for x in [8, 42]:
        d.line([(x, 40), (x, 16)], fill=(200, 200, 200), width=1)
    # Surrey fringed canopy
    d.polygon([(4, 16), (46, 16), (42, 10), (8, 10)], fill=(50, 150, 255))
    # Fringes
    for x in range(4, 46, 2):
        d.line([(x, 16), (x, 18)], fill=(255, 255, 255), width=1)
    # Steering wheel
    d.line([(14, 36), (10, 32)], fill=(100, 100, 100), width=1)
    d.ellipse([8, 30, 12, 34], outline=(50, 50, 50), width=1)

def draw_velomobile(d):
    # Aerodynamic recumbent tricycle enclosed in a shell
    # Wheels (only two visible from side, front and rear)
    d.ellipse([8, 36, 16, 44], fill=(20, 20, 20))
    d.ellipse([34, 36, 42, 44], fill=(20, 20, 20))
    d.ellipse([11, 39, 13, 41], fill=(200, 200, 200))
    d.ellipse([37, 39, 39, 41], fill=(200, 200, 200))
    # Aerodynamic shell (teardrop)
    d.polygon([(4, 38), (14, 20), (30, 20), (46, 38), (30, 42), (14, 42)], fill=(255, 255, 0))
    d.polygon([(6, 36), (16, 22), (28, 22), (42, 36), (28, 38), (16, 38)], fill=(255, 255, 100)) # Highlight
    # Window/canopy
    d.polygon([(16, 28), (20, 22), (28, 22), (32, 28)], fill=(100, 150, 200, 200))
    # Racing stripe
    d.line([(4, 38), (46, 38)], fill=(200, 50, 50), width=2)
    # Headlight
    d.ellipse([42, 34, 46, 38], fill=(255, 255, 255))
    # Vents
    d.line([(34, 32), (38, 32)], fill=(50, 50, 50), width=1)
    d.line([(34, 34), (38, 34)], fill=(50, 50, 50), width=1)

def draw_snowplow_train(d):
    # Train with a massive rotary snowplow on the front
    # Track with snow
    d.line([(0, 44), (50, 44)], fill=(100, 100, 100), width=2)
    d.polygon([(0, 42), (10, 42), (15, 48), (0, 48)], fill=(240, 240, 255)) # Snow drift
    # Train body
    d.polygon([(12, 16), (46, 16), (46, 42), (12, 42)], fill=(150, 50, 50))
    d.polygon([(12, 16), (46, 16), (44, 20), (14, 20)], fill=(200, 80, 80)) # Roof highlight
    # Cab window
    d.rectangle([36, 20, 42, 28], fill=(50, 100, 150))
    # Rotary Plow Assembly (Front left)
    d.polygon([(4, 18), (12, 24), (12, 38), (4, 44)], fill=(100, 100, 100))
    # Huge rotary blades
    d.ellipse([2, 20, 14, 42], fill=(50, 50, 50))
    d.ellipse([3, 21, 13, 41], fill=(200, 200, 200)) # Outer ring
    # Fan blades
    import math
    cx, cy = 8, 31
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        bx = cx + 5 * math.cos(rad)
        by = cy + 5 * math.sin(rad)
        d.line([(cx, cy), (bx, by)], fill=(100, 100, 100), width=2)
    # Snow flying out top chute
    d.polygon([(6, 18), (10, 18), (8, 12), (4, 14)], fill=(100, 100, 100)) # Chute
    d.ellipse([2, 4, 12, 12], fill=(255, 255, 255, 200)) # Snow spray

def draw_monowheel(d):
    # Single giant wheel with rider sitting inside
    # Giant outer wheel
    d.ellipse([10, 10, 40, 48], outline=(30, 30, 30), width=4)
    d.ellipse([12, 12, 38, 46], outline=(150, 150, 150), width=1) # Rim highlight
    # Tread marks
    for angle in range(0, 360, 30):
        import math
        rad = math.radians(angle)
        x1 = 25 + 15 * math.cos(rad)
        y1 = 29 + 19 * math.sin(rad)
        x2 = 25 + 13 * math.cos(rad)
        y2 = 29 + 17 * math.sin(rad)
        d.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=1)
    # Inner track/chassis
    d.ellipse([16, 16, 34, 42], outline=(200, 50, 50), width=2)
    # Engine/Seat inside
    d.rectangle([20, 34, 30, 40], fill=(100, 100, 100))
    d.polygon([(20, 34), (22, 28), (28, 28), (30, 34)], fill=(50, 50, 50)) # Seat
    # Handlebars
    d.line([(28, 28), (34, 24)], fill=(150, 150, 150), width=2)
    # Exhaust
    d.line([(20, 38), (14, 38)], fill=(80, 80, 80), width=2)
    d.ellipse([10, 36, 14, 40], fill=(200, 200, 200, 150)) # Smoke

def draw_interceptor(d):
    # High-speed police interceptor (sleek sports car with lightbar)
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [12, 38]:
        d.ellipse([x-5, 36, x+5, 46], fill=(20, 20, 20))
        d.ellipse([x-3, 38, x+3, 44], fill=(50, 50, 50))
        d.ellipse([x-1, 40, x+1, 42], fill=(200, 200, 200))
    # Body (Black and White)
    d.polygon([(2, 38), (16, 26), (30, 26), (48, 38), (46, 42), (4, 42)], fill=(255, 255, 255))
    d.polygon([(10, 38), (16, 26), (30, 26), (40, 38)], fill=(20, 20, 20)) # Black center
    d.polygon([(12, 38), (17, 27), (29, 27), (38, 38)], fill=(40, 40, 40)) # Highlight
    # Windows
    d.polygon([(18, 28), (22, 20), (32, 20), (36, 28)], fill=(50, 100, 150))
    d.polygon([(20, 27), (23, 21), (31, 21), (34, 27)], fill=(100, 150, 200)) # Reflection
    # Lightbar
    d.rectangle([23, 16, 31, 19], fill=(50, 50, 50))
    d.rectangle([23, 16, 27, 19], fill=(255, 50, 50)) # Red
    d.rectangle([27, 16, 31, 19], fill=(50, 50, 255)) # Blue
    # Glow
    d.ellipse([21, 14, 29, 21], fill=(255, 50, 50, 100))
    d.ellipse([25, 14, 33, 21], fill=(50, 50, 255, 100))
    # Bullbar
    d.line([(46, 38), (48, 38), (48, 42), (46, 42)], fill=(100, 100, 100), width=1)

def draw_crawler_transporter(d):
    # Massive NASA-style crawler for moving rockets
    # Tracks (4 huge bogies)
    d.rectangle([4, 36, 18, 46], fill=(50, 50, 50))
    d.rectangle([32, 36, 46, 46], fill=(50, 50, 50))
    for i in range(4, 18, 3):
        d.ellipse([i, 40, i+2, 46], fill=(30, 30, 30))
    for i in range(32, 46, 3):
        d.ellipse([i, 40, i+2, 46], fill=(30, 30, 30))
    # Main platform
    d.polygon([(2, 28), (48, 28), (48, 36), (2, 36)], fill=(150, 150, 150))
    d.polygon([(2, 28), (48, 28), (46, 30), (4, 30)], fill=(200, 200, 200)) # Highlight
    # Truss structure under platform
    for x in range(4, 46, 6):
        d.line([(x, 30), (x+3, 36)], fill=(100, 100, 100), width=1)
        d.line([(x+3, 30), (x, 36)], fill=(100, 100, 100), width=1)
    # Control cabs at corners
    d.rectangle([2, 24, 8, 28], fill=(200, 200, 200))
    d.rectangle([4, 25, 6, 27], fill=(50, 100, 150)) # Window
    d.rectangle([42, 24, 48, 28], fill=(200, 200, 200))
    d.rectangle([44, 25, 46, 27], fill=(50, 100, 150)) # Window
    # Launch pad base on top
    d.polygon([(10, 20), (40, 20), (44, 28), (6, 28)], fill=(180, 180, 180))
    # Exhaust trench hole
    d.rectangle([20, 22, 30, 28], fill=(50, 50, 50))

def draw_funny_car(d):
    # Drag racing funny car: exaggerated proportions, huge rear wheels, massive engine
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Huge rear wheels
    d.ellipse([6, 26, 22, 46], fill=(20, 20, 20))
    d.ellipse([11, 33, 17, 39], fill=(150, 150, 150))
    d.ellipse([13, 35, 15, 37], fill=(50, 50, 50))
    # Tiny front wheels
    d.ellipse([38, 38, 44, 46], fill=(20, 20, 20))
    d.ellipse([40, 41, 42, 43], fill=(200, 200, 200))
    # Body (wedge shape)
    d.polygon([(4, 38), (14, 24), (28, 24), (46, 36), (46, 42), (4, 42)], fill=(200, 50, 200))
    # Flames decal
    d.polygon([(30, 36), (46, 36), (46, 42), (36, 42)], fill=(255, 150, 0))
    d.polygon([(34, 38), (44, 38), (44, 42), (38, 42)], fill=(255, 255, 0))
    # Massive blower engine protruding from hood
    d.rectangle([30, 18, 36, 26], fill=(200, 200, 200))
    d.rectangle([32, 14, 38, 18], fill=(150, 150, 150)) # Intake scoop
    d.line([(32, 16), (38, 16)], fill=(50, 50, 50), width=1)
    # Exhaust pipes (headers) angling up
    for i in range(4):
        d.line([(24+i*2, 38), (22+i*2, 34)], fill=(150, 150, 150), width=2)
    # Rear spoiler
    d.polygon([(4, 26), (10, 20), (14, 20), (8, 26)], fill=(150, 50, 150))

def draw_swamp_buggy(d):
    # Tall open buggy with giant paddle tires for mud
    # Giant paddle tires
    for x in [12, 38]:
        d.ellipse([x-8, 26, x+8, 46], fill=(30, 30, 30))
        # Paddles
        for angle in range(0, 360, 30):
            import math
            rad = math.radians(angle)
            px1 = x + 6 * math.cos(rad)
            py1 = 36 + 8 * math.sin(rad)
            px2 = x + 9 * math.cos(rad)
            py2 = 36 + 11 * math.sin(rad)
            d.line([(px1, py1), (px2, py2)], fill=(20, 20, 20), width=2)
        d.ellipse([x-2, 34, x+2, 38], fill=(150, 150, 150))
    # Lifted chassis
    d.rectangle([10, 24, 40, 28], fill=(50, 150, 50))
    # Suspension links
    d.line([(12, 36), (20, 28)], fill=(100, 100, 100), width=2)
    d.line([(38, 36), (30, 28)], fill=(100, 100, 100), width=2)
    # Engine in back
    d.rectangle([10, 16, 18, 24], fill=(150, 150, 150))
    d.polygon([(10, 12), (18, 12), (16, 16), (12, 16)], fill=(100, 100, 100)) # Exhaust stack
    # Driver seat and roll cage
    d.arc([22, 10, 36, 24], start=180, end=0, fill=(200, 200, 200), width=2)
    d.rectangle([24, 18, 30, 24], fill=(50, 50, 50))
    # Steering wheel
    d.line([(30, 20), (34, 16)], fill=(100, 100, 100), width=1)

def draw_iceboat(d):
    # Sailboat on skate runners for ice
    # Ice surface
    d.polygon([(0, 44), (50, 44), (50, 50), (0, 50)], fill=(220, 240, 255))
    d.line([(0, 44), (50, 44)], fill=(150, 200, 255), width=1)
    # Cross plank (hull)
    d.polygon([(8, 38), (42, 38), (40, 40), (10, 40)], fill=(200, 50, 50))
    # Runners (Skates)
    # Front runner
    d.line([(40, 40), (40, 46)], fill=(100, 100, 100), width=1)
    d.line([(36, 46), (44, 46)], fill=(150, 150, 150), width=2)
    # Rear runners
    d.line([(12, 40), (12, 44)], fill=(100, 100, 100), width=1)
    d.line([(8, 44), (16, 44)], fill=(150, 150, 150), width=2)
    d.line([(28, 38), (28, 42)], fill=(100, 100, 100), width=1)
    d.line([(24, 42), (32, 42)], fill=(150, 150, 150), width=2)
    # Cockpit
    d.ellipse([18, 34, 30, 38], fill=(150, 50, 50))
    # Mast and Sail
    d.line([(24, 8), (24, 38)], fill=(150, 150, 150), width=2) # Metal mast
    d.polygon([(26, 10), (42, 34), (26, 34)], fill=(255, 255, 255)) # Sail
    d.polygon([(28, 14), (38, 32), (28, 32)], fill=(240, 240, 240)) # Sail highlight
    # Boom
    d.line([(24, 34), (44, 34)], fill=(100, 100, 100), width=2)

def draw_efoil(d):
    # Electric hydrofoil surfboard with rider
    # Water surface
    d.polygon([(0, 40), (50, 40), (50, 50), (0, 50)], fill=(0, 100, 200, 150))
    # Foil mast (underwater)
    d.line([(25, 34), (25, 46)], fill=(50, 50, 50), width=2)
    # Foil wings (underwater)
    d.ellipse([20, 45, 30, 48], fill=(30, 30, 30))
    d.ellipse([27, 44, 32, 46], fill=(50, 50, 50)) # Motor pod
    # Propeller wash
    d.ellipse([30, 43, 40, 47], fill=(150, 200, 255, 150))
    # Surfboard (hovering above water)
    d.polygon([(10, 32), (40, 32), (36, 34), (14, 34)], fill=(255, 100, 0))
    d.polygon([(12, 32), (38, 32), (35, 33), (15, 33)], fill=(255, 150, 50)) # Highlight
    # Rider (abstract silhouette)
    d.polygon([(22, 14), (28, 14), (30, 22), (26, 26), (28, 32), (24, 32), (22, 26), (20, 22)], fill=(20, 20, 20))
    d.ellipse([23, 8, 27, 12], fill=(20, 20, 20)) # Head
    # Handheld controller and wire
    d.line([(28, 18), (32, 22)], fill=(20, 20, 20), width=1)
    d.ellipse([31, 21, 33, 23], fill=(255, 0, 0))

def draw_jet_truck(d):
    # Shockwave style jet-powered semi truck
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Six wheels
    for x in [8, 16, 24, 36, 44]:
        d.ellipse([x-4, 36, x+4, 46], fill=(20, 20, 20))
        d.ellipse([x-2, 39, x+2, 43], fill=(200, 200, 200))
    # Truck cab (aerodynamic)
    d.polygon([(6, 36), (12, 16), (24, 16), (26, 36)], fill=(255, 0, 0))
    d.polygon([(14, 18), (22, 18), (23, 24), (13, 24)], fill=(50, 50, 50)) # Window
    # Jet engines on the back (massive)
    d.rectangle([26, 20, 48, 30], fill=(150, 150, 150))
    d.polygon([(26, 20), (48, 20), (46, 22), (26, 22)], fill=(200, 200, 200)) # Highlight
    # Afterburner flames
    d.polygon([(48, 20), (50, 25), (48, 30)], fill=(255, 255, 255))
    d.polygon([(48, 16), (50, 25), (48, 34)], fill=(255, 200, 50, 200))
    d.polygon([(46, 12), (50, 25), (46, 38)], fill=(255, 100, 0, 150))
    # Exhaust smoke
    d.ellipse([40, 0, 50, 20], fill=(100, 100, 100, 100))
    d.ellipse([40, 30, 50, 50], fill=(100, 100, 100, 100))
    # Chrome stacks
    d.rectangle([18, 6, 20, 16], fill=(220, 220, 220))

def draw_semi_truck(d):
    # Classic long-nose American semi truck
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [8, 34, 42]:
        d.ellipse([x-4, 36, x+4, 46], fill=(20, 20, 20))
        d.ellipse([x-2, 39, x+2, 43], fill=(200, 200, 200))
    # Hood and grill
    d.polygon([(4, 36), (16, 28), (16, 36)], fill=(50, 100, 200))
    d.rectangle([4, 28, 6, 36], fill=(220, 220, 220)) # Grill
    d.line([(5, 28), (5, 36)], fill=(150, 150, 150), width=1)
    # Cab and sleeper
    d.polygon([(16, 28), (18, 16), (30, 16), (30, 36), (16, 36)], fill=(50, 100, 200))
    d.polygon([(17, 27), (19, 17), (24, 17), (24, 27)], fill=(50, 50, 50)) # Window
    # Highlight
    d.polygon([(16, 28), (18, 16), (30, 16), (28, 20), (18, 28)], fill=(100, 150, 255))
    # Chrome exhaust stack
    d.rectangle([28, 6, 30, 20], fill=(220, 220, 220))
    d.polygon([(28, 6), (30, 4), (30, 6)], fill=(220, 220, 220)) # Angled tip
    # Fifth wheel hitch
    d.polygon([(36, 34), (44, 34), (42, 36), (38, 36)], fill=(50, 50, 50))
    # Fuel tanks
    d.ellipse([18, 34, 28, 38], fill=(200, 200, 200))

def draw_motorhome(d):
    # Large RV / Motorhome
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [12, 38]:
        d.ellipse([x-4, 38, x+4, 46], fill=(20, 20, 20))
        d.ellipse([x-2, 40, x+2, 44], fill=(200, 200, 200))
    # Main Body (boxy)
    d.polygon([(4, 40), (46, 40), (46, 16), (8, 16), (4, 24)], fill=(240, 230, 210))
    d.polygon([(4, 40), (46, 40), (45, 38), (5, 38)], fill=(200, 190, 170)) # Shadow
    # Swooping decal stripes
    d.polygon([(4, 30), (20, 26), (46, 30), (46, 34), (20, 30), (4, 34)], fill=(150, 50, 50))
    d.polygon([(10, 26), (30, 22), (46, 26), (46, 28), (30, 24), (10, 28)], fill=(200, 150, 50))
    # Panoramic Front Window
    d.polygon([(4, 24), (8, 18), (14, 18), (14, 24)], fill=(50, 100, 150))
    # Side windows
    for x in range(18, 40, 8):
        d.rectangle([x, 18, x+6, 24], fill=(50, 100, 150))
    # Roof AC units
    d.rectangle([16, 12, 22, 16], fill=(200, 200, 200))
    d.rectangle([32, 12, 38, 16], fill=(200, 200, 200))
    # Awning rolled up
    d.rectangle([16, 16, 44, 18], fill=(255, 255, 255))

def draw_woodie_wagon(d):
    # Classic 1940s Woodie station wagon with surfboard on top
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels
    for x in [12, 38]:
        d.ellipse([x-5, 36, x+5, 46], fill=(20, 20, 20))
        d.ellipse([x-3, 38, x+3, 44], fill=(255, 255, 255)) # Whitewall
        d.ellipse([x-1, 40, x+1, 42], fill=(200, 200, 200)) # Hubcap
    # Front Hood/Fenders (Metal)
    d.polygon([(4, 38), (16, 38), (16, 28), (6, 30)], fill=(50, 100, 50))
    d.ellipse([2, 32, 8, 38], fill=(40, 80, 40)) # Fender curve
    # Wood panels (rear body)
    d.polygon([(16, 38), (46, 38), (46, 20), (22, 20), (16, 28)], fill=(200, 150, 100))
    # Wood framing lines
    d.rectangle([16, 28, 46, 38], outline=(100, 50, 20), width=2)
    d.line([(30, 28), (30, 38)], fill=(100, 50, 20), width=2)
    d.line([(16, 33), (46, 33)], fill=(100, 50, 20), width=2)
    # Windows
    d.polygon([(20, 27), (24, 22), (29, 22), (29, 27)], fill=(150, 200, 255, 200))
    d.rectangle([31, 22, 44, 27], fill=(150, 200, 255, 200))
    # Surfboard on roof
    d.polygon([(14, 16), (48, 16), (46, 18), (16, 18)], fill=(255, 200, 50))
    d.line([(14, 17), (48, 17)], fill=(200, 50, 50), width=1) # Stripe

def draw_rat_rod(d):
    # Rusted, stripped-down hot rod with huge engine and chopped roof
    d.ellipse([4, 42, 46, 46], fill=(0, 0, 0, 150))
    # Wheels (mismatched)
    # Front (thin)
    d.ellipse([6, 36, 12, 46], fill=(20, 20, 20))
    d.ellipse([8, 40, 10, 42], fill=(200, 50, 50)) # Red steelie
    # Rear (huge slick)
    d.ellipse([34, 30, 46, 46], fill=(20, 20, 20))
    d.ellipse([38, 36, 42, 40], fill=(50, 50, 50))
    # Rusty Body/Cabin
    d.polygon([(18, 38), (34, 38), (34, 24), (22, 24), (22, 30), (18, 30)], fill=(139, 69, 19))
    d.polygon([(18, 38), (34, 38), (33, 36), (19, 36)], fill=(160, 82, 45)) # Rust highlight
    # Chopped Window
    d.rectangle([24, 26, 32, 30], fill=(20, 20, 20))
    # Exposed Engine (V8)
    d.rectangle([10, 30, 18, 38], fill=(100, 100, 100))
    d.polygon([(12, 26), (16, 26), (18, 30), (10, 30)], fill=(150, 150, 150)) # Intake
    # Tall exhaust pipes
    d.line([(14, 30), (14, 16)], fill=(200, 200, 200), width=2)
    d.line([(16, 30), (16, 18)], fill=(200, 200, 200), width=2)
    # Grill (small)
    d.rectangle([6, 34, 8, 40], fill=(80, 80, 80))

def draw_trikke(d):
    # 3-wheeled carving scooter (cambering vehicle)
    # Wheels (small polyurethene)
    d.ellipse([22, 42, 26, 46], fill=(50, 50, 50)) # Front
    d.ellipse([10, 40, 14, 44], fill=(50, 50, 50)) # Back left
    d.ellipse([34, 40, 38, 44], fill=(50, 50, 50)) # Back right
    # Frame (Y-shape)
    d.line([(24, 42), (24, 20)], fill=(200, 200, 200), width=2) # Steering column
    d.line([(24, 34), (12, 40)], fill=(200, 200, 200), width=2) # Left arm
    d.line([(24, 34), (36, 40)], fill=(200, 200, 200), width=2) # Right arm
    # Foot platforms
    d.polygon([(10, 38), (14, 38), (16, 40), (8, 40)], fill=(255, 100, 50))
    d.polygon([(34, 38), (38, 38), (40, 40), (32, 40)], fill=(255, 100, 50))
    # Handlebars
    d.line([(18, 18), (30, 18)], fill=(100, 100, 100), width=2)
    d.line([(24, 20), (24, 18)], fill=(200, 200, 200), width=2)
    d.ellipse([16, 17, 18, 19], fill=(50, 50, 50)) # Grip
    d.ellipse([30, 17, 32, 19], fill=(50, 50, 50)) # Grip
    # Action lines (leaning)
    d.line([(6, 44), (20, 48)], fill=(200, 200, 200, 150), width=1)

def draw_flying_platform(d):
    # Retro-futuristic personal flying disc (Hiller VZ-1 style)
    # The ducted fan base
    d.ellipse([10, 30, 40, 40], outline=(150, 150, 150), width=4)
    d.ellipse([12, 32, 38, 38], fill=(100, 100, 100)) # Inside duct
    d.ellipse([12, 32, 38, 38], outline=(200, 200, 200), width=1)
    # Fan blades (blur)
    for i in range(12, 38, 4):
        d.line([(25, 35), (i, 32)], fill=(50, 50, 50), width=1)
        d.line([(25, 35), (i, 38)], fill=(50, 50, 50), width=1)
    # Rider platform grille
    d.ellipse([18, 28, 32, 32], fill=(200, 200, 200))
    for i in range(20, 32, 2):
        d.line([(i, 29), (i, 31)], fill=(100, 100, 100), width=1)
    # Rider (retro pilot)
    # Body
    d.polygon([(22, 14), (28, 14), (30, 28), (20, 28)], fill=(50, 150, 100))
    # Helmet
    d.ellipse([21, 6, 29, 14], fill=(255, 255, 255))
    d.ellipse([23, 8, 29, 12], fill=(50, 100, 150)) # Visor
    # Control ring
    d.ellipse([16, 20, 34, 24], outline=(255, 50, 50), width=2)
    # Arms holding ring
    d.line([(22, 16), (16, 22)], fill=(50, 150, 100), width=2)
    d.line([(28, 16), (34, 22)], fill=(50, 150, 100), width=2)
    # Thrust distortion
    d.ellipse([10, 40, 40, 48], fill=(150, 200, 255, 100))

def draw_cargo_drone(d):
    # Heavy-lift multirotor drone carrying a package
    # Drone core
    d.polygon([(20, 18), (30, 18), (32, 22), (18, 22)], fill=(200, 200, 200))
    d.ellipse([24, 16, 26, 18], fill=(50, 200, 255)) # Camera/Sensor
    # 4 Rotor arms
    d.line([(20, 20), (10, 16)], fill=(100, 100, 100), width=2)
    d.line([(30, 20), (40, 16)], fill=(100, 100, 100), width=2)
    d.line([(22, 20), (14, 26)], fill=(100, 100, 100), width=2)
    d.line([(28, 20), (36, 26)], fill=(100, 100, 100), width=2)
    # Rotors (spinning blurs)
    centers = [(10, 16), (40, 16), (14, 26), (36, 26)]
    for cx, cy in centers:
        d.ellipse([cx-6, cy-2, cx+6, cy+2], fill=(150, 150, 150, 150))
        d.ellipse([cx-1, cy-1, cx+1, cy+1], fill=(50, 50, 50))
    # Tether cables
    d.line([(20, 22), (20, 32)], fill=(50, 50, 50), width=1)
    d.line([(30, 22), (30, 32)], fill=(50, 50, 50), width=1)
    # Cargo Box
    d.polygon([(16, 32), (34, 32), (36, 42), (18, 42)], fill=(200, 150, 100))
    d.polygon([(16, 32), (34, 32), (33, 34), (17, 34)], fill=(240, 190, 140)) # Highlight
    # Box tape
    d.polygon([(24, 32), (26, 32), (28, 42), (26, 42)], fill=(255, 255, 255, 150))

def draw_personal_sub(d):
    # Small sleek underwater scooter / personal submarine
    # Water background
    d.ellipse([5, 5, 45, 45], fill=(0, 100, 200, 100))
    # Main torpedo-shaped body
    d.polygon([(10, 20), (30, 16), (40, 24), (30, 32), (10, 28)], fill=(255, 255, 0))
    d.polygon([(12, 22), (28, 18), (36, 24), (28, 28), (12, 26)], fill=(255, 255, 100)) # Highlight
    # Transparent canopy
    d.ellipse([20, 14, 36, 26], fill=(200, 240, 255, 150))
    d.ellipse([22, 16, 34, 24], outline=(255, 255, 255), width=1) # Reflection
    # Pilot silhouette inside
    d.ellipse([26, 18, 30, 22], fill=(50, 50, 50))
    # Side fins
    d.polygon([(20, 28), (14, 36), (18, 38), (26, 30)], fill=(200, 200, 0))
    # Propeller / Jet at rear
    d.polygon([(10, 20), (4, 18), (4, 30), (10, 28)], fill=(100, 100, 100))
    d.ellipse([2, 20, 6, 28], fill=(150, 150, 150))
    # Bubbles trail
    d.ellipse([4, 16, 6, 18], fill=(255, 255, 255, 150))
    d.ellipse([2, 12, 5, 15], fill=(255, 255, 255, 150))
    d.ellipse([6, 8, 8, 10], fill=(255, 255, 255, 150))
    # Headlight beams
    d.polygon([(40, 24), (50, 18), (50, 30)], fill=(255, 255, 200, 100))

def draw_steam_yacht(d):
    # Elegant Victorian steam-powered yacht
    d.ellipse([4, 40, 46, 45], fill=(0, 50, 100, 100))
    # Long graceful hull
    d.polygon([(4, 32), (40, 34), (48, 38), (40, 42), (8, 42)], fill=(255, 255, 255))
    d.polygon([(4, 32), (40, 34), (42, 36), (6, 34)], fill=(240, 240, 240)) # Highlight
    # Hull underside (red)
    d.polygon([(8, 40), (42, 38), (46, 40), (40, 42)], fill=(150, 50, 50))
    # Gold trim line
    d.line([(6, 34), (46, 38)], fill=(255, 215, 0), width=1)
    # Cabins (varnished wood)
    d.polygon([(12, 32), (16, 26), (32, 26), (36, 33)], fill=(139, 69, 19))
    d.polygon([(14, 26), (16, 22), (28, 22), (30, 26)], fill=(160, 82, 45))
    # Windows (portholes)
    for x in range(16, 30, 4):
        d.ellipse([x, 28, x+2, 30], fill=(255, 255, 200))
    # Tall Smokestack (raked back)
    d.polygon([(20, 22), (24, 10), (28, 10), (24, 22)], fill=(255, 255, 150))
    d.polygon([(23, 10), (24, 6), (28, 6), (27, 10)], fill=(50, 50, 50)) # Black top
    # Smoke
    d.ellipse([18, 2, 24, 6], fill=(150, 150, 150, 150))
    d.ellipse([14, 0, 20, 4], fill=(150, 150, 150, 100))
    # Rigging/Masts (slim)
    d.line([(12, 10), (14, 32)], fill=(100, 50, 20), width=1)
    d.line([(34, 12), (32, 32)], fill=(100, 50, 20), width=1)

# List of all vehicles and their drawing functions
vehicles = [
    ("lowrider", draw_lowrider),
    ("apc", draw_apc),
    ("lawn_mower", draw_lawn_mower),
    ("hearse", draw_hearse),
    ("microcar", draw_microcar),
    ("bucket_wheel_excavator", draw_bucket_wheel_excavator),
    ("bubble_car", draw_bubble_car),
    ("trireme", draw_trireme),
    ("chinese_junk", draw_chinese_junk),
    ("fireboat", draw_fireboat),
    ("luxury_yacht", draw_luxury_yacht),
    ("trimaran", draw_trimaran),
    ("bathysphere", draw_bathysphere),
    ("dhow", draw_dhow),
    ("gyrocopter", draw_gyrocopter),
    ("tiltrotor", draw_tiltrotor),
    ("stealth_bomber", draw_stealth_bomber),
    ("triplane", draw_triplane),
    ("wingsuit", draw_wingsuit),
    ("spaceplane", draw_spaceplane),
    ("turbotrain", draw_turbotrain),
    ("hyperloop_pod", draw_hyperloop_pod),
    ("container_flatcar", draw_container_flatcar),
    ("suspension_railway", draw_suspension_railway),
    ("mine_cart", draw_mine_cart),
    ("solar_sail", draw_solar_sail),
    ("space_station", draw_space_station),
    ("space_tug", draw_space_tug),
    ("soapbox_car", draw_soapbox_car),
    ("mountainboard", draw_mountainboard),
    ("quadricycle", draw_quadricycle),
    ("velomobile", draw_velomobile),
    ("snowplow_train", draw_snowplow_train),
    ("monowheel", draw_monowheel),
    ("interceptor", draw_interceptor),
    ("crawler_transporter", draw_crawler_transporter),
    ("funny_car", draw_funny_car),
    ("swamp_buggy", draw_swamp_buggy),
    ("iceboat", draw_iceboat),
    ("efoil", draw_efoil),
    ("jet_truck", draw_jet_truck),
    ("semi_truck", draw_semi_truck),
    ("motorhome", draw_motorhome),
    ("woodie_wagon", draw_woodie_wagon),
    ("rat_rod", draw_rat_rod),
    ("trikke", draw_trikke),
    ("flying_platform", draw_flying_platform),
    ("cargo_drone", draw_cargo_drone),
    ("personal_sub", draw_personal_sub),
    ("steam_yacht", draw_steam_yacht)
]

def generate_all():
    os.makedirs("images/vehicles", exist_ok=True)
    for name, draw_fn in vehicles:
        img = create_image()
        d = ImageDraw.Draw(img, 'RGBA')
        draw_fn(d)
        
        # Optimize palette to max 10 colors
        # Ensure we have a pure transparency color
        alpha = img.split()[3]
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        img.paste((0,0,0,0), mask=mask)
        
        # Use MAXCOVERAGE to handle the detailed multi-layered gradients and highlights better
        img = img.quantize(colors=9).convert('RGBA')
        
        # Double check and force any slightly transparent pixel to full transparent to save color slots
        pixels = img.load()
        for y in range(img.height):
            for x in range(img.width):
                r,g,b,a = pixels[x,y]
                if a < 255:
                    pixels[x,y] = (0,0,0,0)

        filename = f"images/vehicles/{name}.png"
        img.save(filename)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate_all()
