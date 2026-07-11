import os
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/electronics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    # --- Add realistic 3D detail (pixel drop shadow and glossy reflection) ---
    r, g, b, a = base_img.split()
    shadow_mask = a.point(lambda p: 255 if p > 128 else 0)
    
    combined = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    # 1. Drop Shadow (offset by 2,2)
    shadow_color = Image.new("RGBA", (50, 50), (30, 30, 35, 255))
    combined.paste(shadow_color, (2, 2), mask=shadow_mask)
    
    # 2. Base Image
    combined = Image.alpha_composite(combined, base_img)
    
    # 3. Glossy Reflection Glare
    gloss = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.polygon([(0, 0), (35, 0), (0, 35)], fill=(255, 255, 255, 60))
    gloss_draw.polygon([(50, 25), (50, 50), (25, 50)], fill=(0, 0, 0, 60))
    gloss_masked = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_masked.paste(gloss, (0, 0), mask=shadow_mask)
    combined = Image.alpha_composite(combined, gloss_masked)
    
    # --- Quantize to strictly <= 9 colors ---
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    comb_a = combined.split()[3].point(lambda p: 255 if p > 128 else 0)
    flat.paste(combined, mask=comb_a)
    
    q = flat.quantize(colors=8, method=Image.MEDIANCUT)
    final = q.convert("RGBA")
    
    # Force all transparent pixels to a single identical RGBA value
    data = final.getdata()
    alpha_data = comb_a.getdata()
    new_data = []
    for i in range(len(data)):
        if alpha_data[i] == 0:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append((data[i][0], data[i][1], data[i][2], 255))
    final.putdata(new_data)
    
    path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
    final.save(path)
    print(f"  Saved: {path}")

# Color constants
RED       = (210, 45, 45, 255)
DKRED     = (130, 20, 20, 255)
BLUE      = (50, 110, 210, 255)
DKBLUE    = (20, 50, 140, 255)
YELLOW    = (240, 200, 30, 255)
GREEN     = (50, 160, 60, 255)
DKGREEN   = (20, 90, 20, 255)
WHITE     = (245, 245, 245, 255)
BLACK     = (25, 25, 25, 255)
GREY      = (160, 160, 165, 255)
DKGREY    = (80, 80, 85, 255)
ORANGE    = (235, 110, 25, 255)
BROWN     = (130, 85, 45, 255)
PURPLE    = (130, 60, 180, 255)
LIGHTBLUE = (170, 220, 250, 255)
STEEL     = (120, 125, 135, 255)
SILVER    = (180, 180, 190, 255)
CYAN      = (0, 255, 255, 255)
DKCYAN    = (0, 130, 130, 255)
GOLD      = (212, 175, 55, 255)
DKCYAN    = (0, 130, 130, 255)

# --- 1. Smartphone ---
def draw_smartphone(draw):
    draw.rounded_rectangle([17, 8, 37, 46], radius=3, fill=DKGREY) # underbody shadow
    draw.rounded_rectangle([15, 6, 35, 44], radius=3, fill=BLACK, outline=SILVER, width=1) # body + metallic bezel
    draw.rectangle([17, 9, 33, 41], fill=DKGREY) # screen
    # status bar
    draw.line([18, 10, 32, 10], fill=GREY, width=1)
    draw.line([18, 10, 20, 10], fill=GREEN, width=1) # battery indicator
    # app icons grid
    draw.rectangle([19, 12, 22, 15], fill=BLUE)
    draw.rectangle([25, 12, 28, 15], fill=GREEN)
    draw.rectangle([30, 12, 32, 15], fill=YELLOW)
    draw.rectangle([19, 18, 22, 21], fill=RED)
    draw.rectangle([25, 18, 28, 21], fill=WHITE)
    draw.rectangle([30, 18, 32, 21], fill=BLUE)
    # diagonal screen reflection glare
    draw.line([17, 30, 30, 17], fill=WHITE, width=1)
    draw.line([17, 35, 33, 19], fill=WHITE, width=1)
    # home button and speaker
    draw.ellipse([23, 42, 27, 43], fill=SILVER)
    draw.line([23, 7, 27, 7], fill=GREY, width=1)

# --- 2. Laptop ---
def draw_laptop(draw):
    # screen lid
    draw.rectangle([12, 10, 38, 29], fill=BLACK)
    draw.rectangle([13, 11, 37, 28], fill=SILVER)
    draw.rectangle([15, 13, 35, 26], fill=BLUE) # screen content
    # screen shine glare
    draw.line([15, 22, 29, 13], fill=WHITE, width=1)
    draw.rectangle([17, 15, 23, 20], fill=WHITE) # application window representation
    # keyboard base
    draw.polygon([(8, 29), (42, 29), (46, 36), (4, 36)], fill=GREY)
    draw.polygon([(9, 30), (41, 30), (45, 35), (5, 35)], fill=DKGREY) # key area
    # trackpad and hinge
    draw.rectangle([19, 33, 31, 35], fill=SILVER)
    draw.line([11, 29, 39, 29], fill=BLACK, width=1)

# --- 3. Desktop PC ---
def draw_desktop_pc(draw):
    # Monitor Screen
    draw.rectangle([8, 6, 36, 26], fill=BLACK, outline=GREY, width=1)
    draw.rectangle([10, 8, 34, 24], fill=DKBLUE)
    # screen shine glare
    draw.line([10, 18, 20, 8], fill=WHITE, width=1)
    # stand
    draw.rectangle([21, 26, 23, 32], fill=SILVER)
    draw.rectangle([16, 32, 28, 34], fill=BLACK)
    # CPU Tower
    draw.rectangle([39, 8, 47, 34], fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([41, 11, 45, 13], fill=BLACK) # disc tray
    draw.ellipse([42, 30, 44, 31], fill=GREEN) # power LED
    # vents lines on CPU side
    for y in range(16, 28, 3):
        draw.line([41, y, 45, y], fill=BLACK, width=1)
    # Keyboard & Mouse
    draw.line([10, 36, 32, 36], fill=SILVER, width=2)
    draw.rectangle([34, 35, 36, 37], fill=WHITE)

# --- 4. Retro Television ---
def draw_retro_television(draw):
    # Wooden Cabinet with bevel and underbody shadow
    draw.rectangle([8, 12, 44, 42], fill=BLACK) # shadow
    draw.rounded_rectangle([6, 10, 42, 40], radius=2, fill=BROWN, outline=BLACK, width=1)
    # Glass Screen
    draw.rectangle([9, 13, 31, 37], fill=BLACK)
    draw.ellipse([10, 14, 30, 36], fill=DKGREY)
    draw.line([12, 16, 24, 28], fill=WHITE, width=1) # screen shine
    # Control Panel (Knobs with indicator marks)
    draw.ellipse([36, 15, 39, 18], fill=SILVER)
    draw.line([37, 16, 37, 15], fill=BLACK, width=1) # dial indicator
    draw.ellipse([36, 22, 39, 25], fill=SILVER)
    # speaker grill lines
    for y in range(30, 38, 2):
        draw.line([34, y, 40, y], fill=BLACK, width=1)
    # Antenna
    draw.line([20, 10, 10, 2], fill=SILVER, width=1)
    draw.line([20, 10, 30, 2], fill=SILVER, width=1)

# --- 5. Headphones ---
def draw_headphones(draw):
    # headband with underbody cushioning
    draw.arc([10, 10, 40, 40], 180, 360, fill=BLACK, width=4)
    draw.arc([11, 11, 39, 39], 180, 360, fill=GREY, width=2)
    # Ear cups & cushions
    draw.rounded_rectangle([7, 22, 14, 36], radius=2, fill=RED, outline=BLACK, width=1)
    draw.rounded_rectangle([36, 22, 43, 36], radius=2, fill=RED, outline=BLACK, width=1)
    draw.rectangle([12, 24, 14, 34], fill=BLACK)
    draw.rectangle([36, 24, 38, 34], fill=BLACK)
    # Telescopic metallic sliders
    draw.line([10, 18, 10, 23], fill=SILVER, width=2)
    draw.line([40, 18, 40, 23], fill=SILVER, width=2)

# --- 6. Smartwatch ---
def draw_smartwatch(draw):
    # Straps with buckle highlights
    draw.rectangle([21, 4, 29, 46], fill=GREY)
    draw.line([21, 45, 29, 45], fill=BLACK, width=1)
    # Watch Body + bezel outline
    draw.rounded_rectangle([15, 15, 35, 35], radius=3, fill=BLACK, outline=SILVER, width=1)
    # Screen with diagonal reflection
    draw.rectangle([18, 18, 32, 32], fill=DKCYAN)
    draw.line([18, 26, 26, 18], fill=WHITE, width=1)
    # Digital Clock digits
    draw.line([21, 23, 29, 23], fill=CYAN, width=1)
    draw.line([21, 27, 29, 27], fill=CYAN, width=1)

# --- 7. Gaming Console ---
def draw_gaming_console(draw):
    # Console Unit with shading
    draw.rectangle([8, 16, 42, 34], fill=GREY, outline=BLACK, width=1)
    draw.rectangle([8, 28, 42, 34], fill=DKGREY) # shade
    # Controller ports and CD tray lines
    draw.rectangle([12, 22, 17, 25], fill=BLACK)
    draw.rectangle([20, 22, 25, 25], fill=BLACK)
    draw.line([10, 20, 32, 20], fill=BLACK, width=1)
    # Power Button and glowing LED
    draw.ellipse([35, 21, 38, 24], fill=BLACK)
    draw.ellipse([36, 22, 37, 23], fill=GREEN) # power LED

# --- 8. Game Controller ---
def draw_game_controller(draw):
    # D-pad controller shape + shadow underbody
    draw.rounded_rectangle([10, 18, 40, 32], radius=4, fill=GREY, outline=BLACK, width=1)
    draw.polygon([(10, 30), (8, 40), (16, 40), (16, 32)], fill=DKGREY)
    draw.polygon([(40, 30), (42, 40), (34, 40), (34, 32)], fill=DKGREY)
    # D-pad details
    draw.line([14, 25, 20, 25], fill=BLACK, width=2)
    draw.line([17, 22, 17, 28], fill=BLACK, width=2)
    # colored buttons
    draw.ellipse([29, 21, 31, 23], fill=RED)
    draw.ellipse([32, 24, 34, 26], fill=YELLOW)
    draw.ellipse([29, 26, 31, 28], fill=GREEN)
    draw.ellipse([32, 20, 34, 22], fill=BLUE)

# --- 9. Digital Camera ---
def draw_digital_camera(draw):
    # Camera Body & textured grip
    draw.rounded_rectangle([8, 14, 42, 38], radius=2, fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([8, 20, 42, 38], fill=STEEL)
    draw.rectangle([9, 20, 14, 37], fill=DKGREY) # rubber grip texture
    # Lens elements with circular shine
    draw.ellipse([16, 17, 34, 35], fill=BLACK)
    draw.ellipse([18, 19, 32, 33], fill=DKBLUE)
    draw.ellipse([23, 21, 29, 27], fill=CYAN)
    # Flash & buttons
    draw.rectangle([12, 16, 16, 18], fill=BLACK)
    draw.rectangle([33, 16, 38, 18], fill=WHITE)

# --- 10. Tablet ---
def draw_tablet(draw):
    draw.rounded_rectangle([11, 7, 39, 45], radius=3, fill=DKGREY) # shadow
    draw.rounded_rectangle([9, 5, 37, 43], radius=3, fill=BLACK, outline=SILVER, width=1)
    draw.rectangle([12, 8, 34, 40], fill=BLUE) # screen
    # display shine
    draw.line([12, 25, 29, 8], fill=WHITE, width=1)
    draw.ellipse([23, 41, 25, 42], fill=GREY) # home button

# --- 11. Mechanical Keyboard ---
def draw_mechanical_keyboard(draw):
    # keyboard base
    draw.rounded_rectangle([4, 16, 46, 34], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([4, 27, 46, 34], fill=DKGREY)
    # Keycaps with highlighted edges for depth
    for y in [18, 22, 26, 30]:
        for x in range(6, 44, 4):
            key_color = RED if (x == 6 and y == 18) else (BLUE if x == 38 else BLACK)
            draw.rectangle([x, y, x+2, y+2], fill=key_color)
            draw.line([x, y, x+2, y], fill=WHITE, width=1) # top cap highlight

# --- 12. Optical Mouse ---
def draw_optical_mouse(draw):
    # Mouse Body with ergonomic side styling
    draw.ellipse([16, 16, 34, 38], fill=GREY, outline=BLACK)
    draw.rectangle([16, 26, 34, 38], fill=DKGREY)
    draw.line([25, 16, 25, 26], fill=BLACK, width=1)
    # glowing red scroll wheel
    draw.rectangle([24, 20, 26, 24], fill=RED)
    # wire connection
    draw.line([25, 16, 25, 6], fill=STEEL, width=1)

# --- 13. VR Headset ---
def draw_vr_headset(draw):
    # Head straps
    draw.rectangle([6, 20, 44, 24], fill=BLACK)
    # Visor body with curved bezel styling
    draw.rounded_rectangle([10, 14, 40, 34], radius=4, fill=WHITE, outline=BLACK, width=1)
    draw.rounded_rectangle([10, 24, 40, 34], radius=4, fill=GREY)
    # Glowing visor light
    draw.line([16, 24, 34, 24], fill=CYAN, width=2)
    # logo/lens
    draw.ellipse([13, 16, 15, 18], fill=STEEL)

# --- 14. Audio Speaker ---
def draw_audio_speaker(draw):
    # Wood cabinet cabinet
    draw.rounded_rectangle([14, 6, 36, 44], radius=2, fill=BROWN, outline=BLACK, width=1)
    draw.rectangle([16, 8, 34, 42], fill=BLACK)
    # Tweeter & Woofer detailing
    draw.ellipse([21, 11, 29, 19], fill=GREY)
    draw.ellipse([23, 13, 27, 17], fill=SILVER)
    draw.ellipse([17, 23, 33, 39], fill=GREY)
    draw.ellipse([20, 26, 30, 36], fill=DKGREY)
    draw.ellipse([23, 29, 27, 33], fill=SILVER)

# --- 15. Studio Microphone ---
def draw_studio_microphone(draw):
    # Mic grill with textured grid lines
    draw.rounded_rectangle([18, 8, 32, 22], radius=4, fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([18, 15, 32, 22], fill=GREY)
    draw.line([21, 8, 21, 22], fill=STEEL, width=1)
    draw.line([25, 8, 25, 22], fill=STEEL, width=1)
    draw.line([29, 8, 29, 22], fill=STEEL, width=1)
    # Shock mount ring
    draw.arc([14, 18, 36, 28], 0, 180, fill=BLACK, width=2)
    # Stand base
    draw.line([25, 26, 25, 42], fill=STEEL, width=3)
    draw.ellipse([16, 40, 34, 45], fill=BLACK)

# --- 16. Electronic Calculator ---
def draw_electronic_calculator(draw):
    draw.rounded_rectangle([12, 8, 38, 44], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Screen & characters
    draw.rectangle([15, 12, 35, 18], fill=DKGREEN)
    draw.rectangle([17, 14, 19, 16], fill=GREEN)
    draw.rectangle([21, 14, 23, 16], fill=GREEN)
    draw.rectangle([25, 14, 27, 16], fill=GREEN)
    # Keys
    for y in range(22, 42, 5):
        for x in range(15, 35, 5):
            btn_color = ORANGE if x == 30 else (GREY if y == 22 else WHITE)
            draw.rectangle([x, y, x+3, y+3], fill=btn_color)

# --- 17. Wi-Fi Router ---
def draw_wifi_router(draw):
    # Main Body + vents
    draw.rounded_rectangle([8, 26, 42, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    for x in range(10, 40, 4):
        draw.line([x, 26, x, 28], fill=BLACK, width=1) # vents
    # Antennas
    draw.line([12, 26, 12, 8], fill=BLACK, width=2)
    draw.line([38, 26, 38, 8], fill=BLACK, width=2)
    # Blinking status LEDs
    draw.ellipse([14, 31, 16, 33], fill=GREEN)
    draw.ellipse([20, 31, 22, 33], fill=GREEN)
    draw.ellipse([26, 31, 28, 33], fill=GREEN)

# --- 18. Floppy Disk ---
def draw_floppy_disk(draw):
    draw.rectangle([8, 8, 42, 42], fill=BLUE, outline=BLACK, width=1)
    draw.polygon([(36, 8), (42, 14), (42, 8)], fill=(0,0,0,0))
    # Write protect tab slot
    draw.rectangle([36, 38, 40, 40], fill=BLACK)
    # Metal slider
    draw.rectangle([16, 8, 28, 20], fill=SILVER)
    draw.line([20, 10, 20, 18], fill=BLACK, width=1)
    # Sticker label
    draw.rectangle([12, 24, 38, 42], fill=WHITE)
    draw.line([15, 28, 35, 28], fill=RED, width=1)
    draw.line([15, 33, 35, 33], fill=BLUE, width=1)

# --- 19. USB Flash Drive ---
def draw_usb_flash_drive(draw):
    # Metal USB Connector
    draw.rectangle([6, 20, 14, 30], fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([8, 22, 10, 24], fill=BLACK)
    draw.rectangle([8, 26, 10, 28], fill=BLACK)
    # Plastic casing with key ring slot
    draw.rounded_rectangle([14, 16, 44, 34], radius=2, fill=RED, outline=BLACK, width=1)
    draw.rectangle([14, 25, 44, 34], fill=DKRED)
    draw.ellipse([40, 23, 42, 26], fill=CYAN) # status LED

# --- 20. CD Player ---
def draw_cd_player(draw):
    # Main Unit
    draw.rounded_rectangle([8, 14, 42, 38], radius=2, fill=STEEL, outline=BLACK, width=1)
    draw.rectangle([8, 26, 42, 38], fill=DKGREY)
    # CD slot / tray ejected
    draw.rectangle([12, 20, 38, 25], fill=BLACK)
    draw.arc([16, 14, 34, 32], 0, 180, fill=SILVER, width=3)
    draw.arc([16, 14, 34, 32], 45, 135, fill=CYAN, width=3)
    # Display screen
    draw.rectangle([14, 30, 26, 34], fill=CYAN)
    draw.ellipse([36, 30, 38, 32], fill=RED)

# --- 21. Cassette Tape ---
def draw_cassette_tape(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Label sticker with write lines
    draw.rectangle([12, 16, 38, 30], fill=WHITE)
    draw.rectangle([12, 16, 38, 20], fill=RED)
    # Spools & gear gears
    draw.ellipse([16, 21, 22, 27], fill=BLACK)
    draw.ellipse([28, 21, 34, 27], fill=BLACK)
    draw.ellipse([18, 23, 20, 25], fill=WHITE)
    draw.ellipse([30, 23, 32, 25], fill=WHITE)
    # tape ribbon shell bottom
    draw.polygon([(14, 34), (36, 34), (32, 38), (18, 38)], fill=GREY)

# --- 22. MP3 Player ---
def draw_mp3_player(draw):
    # Body
    draw.rounded_rectangle([14, 8, 36, 42], radius=4, fill=WHITE, outline=GREY, width=1)
    # screen with music playback line
    draw.rectangle([18, 12, 32, 22], fill=BLUE)
    draw.rectangle([20, 14, 30, 20], fill=LIGHTBLUE)
    draw.line([21, 18, 25, 18], fill=BLUE, width=1) # track line
    # Click wheel
    draw.ellipse([20, 26, 30, 36], fill=GREY)
    draw.ellipse([23, 29, 27, 33], fill=WHITE)

# --- 23. Retro Radio ---
def draw_retro_radio(draw):
    # Wood Cabinet
    draw.rounded_rectangle([8, 14, 42, 38], radius=2, fill=BROWN, outline=BLACK, width=1)
    # Dial track needle
    draw.rectangle([12, 18, 28, 22], fill=YELLOW)
    draw.line([20, 18, 20, 22], fill=RED, width=1)
    # Speaker cloth weave grille
    for x in range(12, 28, 3):
        draw.line([x, 26, x, 34], fill=BLACK, width=1)
    # knobs
    draw.ellipse([32, 24, 38, 30], fill=GREY)
    draw.ellipse([32, 31, 38, 37], fill=GREY)
    draw.line([10, 14, 30, 4], fill=SILVER, width=1)

# --- 24. Smart Speaker ---
def draw_smart_speaker(draw):
    # fabric weave design cylinder
    for y in range(14, 38, 2):
        draw.ellipse([15, y, 35, y+4], fill=DKGREY)
    # blue glowing light ring
    draw.ellipse([15, 12, 35, 18], fill=BLACK)
    draw.ellipse([16, 13, 34, 17], fill=CYAN)
    draw.ellipse([18, 14, 32, 16], fill=BLUE)

# --- 25. Walkie Talkie ---
def draw_walkie_talkie(draw):
    # rugged body
    draw.rounded_rectangle([16, 16, 34, 44], radius=2, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([16, 26, 34, 44], fill=ORANGE)
    # LCD screen & antenna
    draw.rectangle([19, 19, 31, 24], fill=DKGREEN)
    draw.rectangle([20, 4, 23, 16], fill=BLACK)
    draw.rectangle([28, 12, 32, 16], fill=BLACK) # volume knob
    # speaker grill dots
    draw.ellipse([23, 30, 25, 32], fill=BLACK)
    draw.ellipse([27, 30, 29, 32], fill=BLACK)
    draw.ellipse([25, 34, 27, 36], fill=BLACK)

# --- 26. Quadcopter Drone ---
def draw_quadcopter_drone(draw):
    # Arms and frame
    draw.line([10, 10, 40, 40], fill=GREY, width=3)
    draw.line([10, 40, 40, 10], fill=GREY, width=3)
    draw.line([6, 10, 14, 10], fill=BLACK, width=2)
    draw.line([36, 10, 44, 10], fill=BLACK, width=2)
    draw.line([6, 40, 14, 40], fill=BLACK, width=2)
    draw.line([36, 40, 44, 40], fill=BLACK, width=2)
    # main pod body + camera gimbal
    draw.ellipse([20, 18, 30, 32], fill=DKGREY)
    draw.ellipse([22, 20, 28, 30], fill=SILVER)
    draw.ellipse([24, 28, 26, 30], fill=CYAN) # camera lens

# --- 27. Video Projector ---
def draw_video_projector(draw):
    # Body
    draw.rounded_rectangle([8, 18, 42, 34], radius=2, fill=WHITE, outline=GREY, width=1)
    draw.rectangle([8, 26, 42, 34], fill=GREY)
    # focus lens with beam projection
    draw.ellipse([12, 20, 22, 30], fill=BLACK)
    draw.ellipse([14, 22, 20, 28], fill=CYAN)
    draw.polygon([(17,25), (4,15), (4,35)], fill=(255, 255, 200, 100))
    # buttons
    draw.ellipse([30, 22, 32, 24], fill=BLACK)
    draw.ellipse([34, 22, 36, 24], fill=BLACK)

# --- 28. Laser Printer ---
def draw_laser_printer(draw):
    # Housing
    draw.rounded_rectangle([10, 16, 40, 38], radius=2, fill=GREY, outline=BLACK, width=1)
    # paper stack loading
    draw.rectangle([14, 10, 36, 16], fill=WHITE)
    # output guide slot
    draw.rectangle([12, 24, 38, 27], fill=BLACK)
    draw.rectangle([14, 26, 36, 34], fill=WHITE) # paper emerging
    draw.line([18, 29, 32, 29], fill=DKGREY, width=1)
    draw.line([18, 32, 28, 32], fill=DKGREY, width=1)

# --- 29. Flatbed Scanner ---
def draw_flatbed_scanner(draw):
    draw.rectangle([6, 20, 44, 38], fill=BLACK, outline=GREY, width=1)
    # lid hinge details
    draw.polygon([(6, 20), (38, 6), (44, 12), (44, 20)], fill=GREY)
    # glowing scanning pane
    draw.rectangle([10, 22, 40, 34], fill=LIGHTBLUE)
    draw.line([22, 22, 22, 34], fill=GREEN, width=2)

# --- 30. High-Def Webcam ---
def draw_webcam(draw):
    # clamp stand base
    draw.line([25, 24, 25, 40], fill=BLACK, width=2)
    draw.ellipse([16, 38, 34, 43], fill=BLACK)
    # Eyeball body & focus lens
    draw.ellipse([16, 10, 34, 28], fill=DKGREY)
    draw.ellipse([18, 12, 32, 26], fill=GREY)
    draw.ellipse([21, 15, 29, 23], fill=BLACK)
    draw.ellipse([23, 17, 27, 21], fill=BLUE)
    draw.ellipse([20, 12, 21, 13], fill=GREEN)

# --- 31. Portable Power Bank ---
def draw_portable_power_bank(draw):
    # casing
    draw.rounded_rectangle([14, 10, 36, 40], radius=3, fill=ORANGE, outline=BLACK, width=1)
    draw.rectangle([14, 25, 36, 40], fill=DKRED)
    # ports
    draw.rectangle([18, 12, 24, 15], fill=STEEL)
    draw.rectangle([26, 12, 32, 15], fill=STEEL)
    # capacity status indicator LEDs
    draw.ellipse([18, 20, 20, 22], fill=GREEN)
    draw.ellipse([22, 20, 24, 22], fill=GREEN)
    draw.ellipse([26, 20, 28, 22], fill=GREEN)
    draw.ellipse([30, 20, 32, 22], fill=GREY)

# --- 32. Wall Charger ---
def draw_wall_charger(draw):
    # body
    draw.rounded_rectangle([15, 12, 35, 32], radius=3, fill=WHITE, outline=GREY, width=1)
    draw.rectangle([15, 22, 35, 32], fill=GREY)
    # metal prongs with holes
    draw.rectangle([19, 32, 22, 42], fill=SILVER)
    draw.rectangle([28, 32, 31, 42], fill=SILVER)
    draw.rectangle([21, 16, 29, 20], fill=BLACK)

# --- 33. CPU Microchip ---
def draw_cpu_microchip(draw):
    # Green PCB base
    draw.rectangle([10, 10, 40, 40], fill=DKGREEN, outline=BLACK, width=1)
    # metal connection pins
    for i in range(12, 40, 4):
        draw.line([i, 8, i, 10], fill=SILVER, width=1)
        draw.line([i, 40, i, 42], fill=SILVER, width=1)
        draw.line([8, i, 10, i], fill=SILVER, width=1)
        draw.line([40, i, 42, i], fill=SILVER, width=1)
    # Silicon die cap
    draw.rounded_rectangle([16, 16, 34, 34], radius=2, fill=SILVER)
    draw.rectangle([16, 25, 34, 34], fill=GREY)

# --- 34. Motherboard ---
def draw_motherboard(draw):
    draw.rectangle([6, 6, 44, 44], fill=DKGREEN, outline=BLACK, width=1)
    # CPU socket block
    draw.rectangle([14, 14, 26, 26], fill=GREY)
    draw.rectangle([16, 16, 24, 24], fill=BLACK)
    # RAM and PCIe expansion slots
    draw.line([30, 10, 30, 38], fill=BLUE, width=1)
    draw.line([33, 10, 33, 38], fill=BLUE, width=1)
    draw.line([36, 10, 36, 38], fill=BLACK, width=1)
    # capacitors
    draw.ellipse([10, 32, 12, 34], fill=GOLD)
    draw.ellipse([14, 32, 16, 34], fill=GOLD)
    draw.line([10, 40, 28, 40], fill=WHITE, width=2)

# --- 35. Graphics Card (GPU) ---
def draw_graphics_card(draw):
    # Shroud
    draw.rectangle([8, 14, 42, 34], fill=DKGREY, outline=BLACK, width=1)
    # Fans
    draw.ellipse([12, 18, 24, 30], fill=BLACK)
    draw.ellipse([26, 18, 38, 30], fill=BLACK)
    draw.ellipse([16, 22, 20, 26], fill=STEEL)
    draw.ellipse([30, 22, 34, 26], fill=STEEL)
    # PCIe connector pins
    draw.line([12, 34, 38, 34], fill=GOLD, width=2)
    draw.line([38, 14, 41, 14], fill=RED, width=2)

# --- 36. Hard Disk Drive (HDD) ---
def draw_hard_disk_drive(draw):
    # enclosure open
    draw.rounded_rectangle([12, 8, 38, 42], radius=2, fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([14, 10, 36, 40], fill=BLACK)
    # magnetic platters
    draw.ellipse([15, 18, 35, 38], fill=GREY)
    draw.ellipse([18, 21, 32, 35], fill=SILVER)
    draw.ellipse([23, 26, 27, 30], fill=BLACK)
    # read arm actuator
    draw.line([33, 12, 25, 28], fill=SILVER, width=2)
    draw.ellipse([31, 11, 35, 15], fill=BLUE)

# --- 37. Solid State Drive (SSD) ---
def draw_solid_state_drive(draw):
    draw.rounded_rectangle([12, 8, 38, 42], radius=2, fill=BLACK, outline=GREY, width=1)
    # branding decal and serial block
    draw.rectangle([14, 14, 36, 30], fill=BLUE)
    draw.rectangle([14, 22, 36, 30], fill=CYAN)
    draw.line([18, 18, 30, 18], fill=WHITE, width=1)
    draw.line([18, 22, 26, 22], fill=WHITE, width=1)
    # gold SATA connectors
    draw.line([16, 42, 34, 42], fill=GOLD, width=1)

# --- 38. RAM Memory Module ---
def draw_ram_memory_module(draw):
    # green strip PCB
    draw.rectangle([4, 20, 46, 30], fill=DKGREEN, outline=BLACK, width=1)
    # memory chips
    for x in range(8, 44, 6):
        draw.rectangle([x, 22, x+4, 26], fill=BLACK)
    # gold contact fingers
    draw.line([6, 30, 44, 30], fill=GOLD, width=1)

# --- 39. Oscilloscope ---
def draw_oscilloscope(draw):
    # casing
    draw.rounded_rectangle([8, 10, 42, 40], radius=2, fill=GREY, outline=BLACK, width=1)
    # grid screen and waveform
    draw.rectangle([11, 14, 28, 28], fill=BLACK)
    draw.arc([12, 16, 20, 24], 180, 360, fill=GREEN, width=1)
    draw.arc([19, 18, 27, 26], 0, 180, fill=GREEN, width=1)
    # dials controls
    draw.ellipse([33, 16, 36, 19], fill=BLACK)
    draw.ellipse([37, 16, 40, 19], fill=RED)
    draw.ellipse([35, 23, 38, 26], fill=BLUE)
    # connectors BNC
    draw.ellipse([33, 32, 36, 35], fill=SILVER)
    draw.ellipse([37, 32, 40, 35], fill=SILVER)

# --- 40. Soldering Iron ---
def draw_soldering_iron(draw):
    draw.ellipse([10, 35, 40, 45], fill=(0,0,0,80)) # stand shadow
    # handle
    draw.line([10, 10, 22, 22], fill=BLUE, width=5)
    # metal shaft and tip
    draw.line([21, 21, 38, 38], fill=SILVER, width=2)
    draw.ellipse([20, 20, 23, 23], fill=BLACK) # sleeve
    draw.line([37, 37, 40, 40], fill=ORANGE, width=2)

# --- 41. Alkaline AA Battery ---
def draw_alkaline_battery(draw):
    # battery body cylinder
    draw.rounded_rectangle([18, 10, 32, 42], radius=1, fill=BLACK, outline=GREY, width=1)
    # copper cap half
    draw.rectangle([18, 10, 32, 22], fill=ORANGE)
    draw.rectangle([23, 7, 27, 10], fill=ORANGE) # plus terminal nipple
    # label stripe
    draw.rectangle([18, 26, 32, 34], fill=GREEN)
    # indicators
    draw.line([23, 16, 27, 16], fill=WHITE, width=1)
    draw.line([25, 14, 25, 18], fill=WHITE, width=1)

# --- 42. Smart LED Bulb ---
def draw_smart_led_bulb(draw):
    # diffuser bulb glass
    draw.ellipse([14, 8, 36, 30], fill=CYAN, outline=BLACK, width=1)
    # glowing filaments
    draw.arc([20, 14, 30, 24], 180, 360, fill=PURPLE, width=2)
    # metal socket base threads
    draw.rectangle([20, 30, 30, 38], fill=GREY)
    draw.line([20, 32, 30, 32], fill=BLACK, width=1)
    draw.line([20, 35, 30, 35], fill=BLACK, width=1)
    draw.ellipse([23, 38, 27, 41], fill=BLACK)

# --- 43. USB Desk Fan ---
def draw_usb_desk_fan(draw):
    # stand
    draw.line([25, 26, 25, 42], fill=BLACK, width=2)
    draw.ellipse([18, 40, 32, 44], fill=BLACK)
    # cage guard
    draw.ellipse([14, 8, 36, 30], fill=GREY, outline=BLACK, width=1)
    # fan blades pitch
    draw.polygon([(25,19), (21,11), (25,11)], fill=CYAN)
    draw.polygon([(25,19), (31,23), (31,19)], fill=CYAN)
    draw.polygon([(25,19), (18,22), (21,25)], fill=CYAN)
    draw.ellipse([23, 17, 27, 21], fill=RED)

# --- 44. Retro Arcade Cabinet ---
def draw_retro_arcade_cabinet(draw):
    # wood cabinet frame
    draw.polygon([(12,44), (38,44), (36,10), (14,10)], fill=PURPLE, outline=BLACK, width=1)
    # marquee glowing header
    draw.rectangle([14, 10, 36, 16], fill=YELLOW)
    # CRT screen
    draw.rectangle([15, 18, 35, 30], fill=BLACK)
    draw.ellipse([17, 19, 33, 29], fill=DKBLUE)
    # control deck & joystick buttons
    draw.rectangle([12, 32, 38, 36], fill=BLACK)
    draw.ellipse([18, 31, 20, 33], fill=RED)
    draw.line([19, 32, 19, 34], fill=SILVER, width=1)
    draw.ellipse([28, 33, 30, 35], fill=YELLOW)

# --- 45. Digital Wristwatch ---
def draw_digital_wristwatch(draw):
    # steel links band
    draw.rectangle([21, 4, 29, 46], fill=SILVER, outline=BLACK, width=1)
    draw.line([25, 4, 25, 46], fill=GREY, width=1)
    # octagonal case
    draw.rounded_rectangle([15, 16, 35, 34], radius=3, fill=BLACK, outline=GREY, width=1)
    # LCD display panel
    draw.rectangle([18, 20, 32, 30], fill=GREY)
    draw.line([21, 24, 24, 24], fill=DKGREEN, width=1)
    draw.line([26, 24, 29, 24], fill=DKGREEN, width=1)

# --- 46. Robot Vacuum ---
def draw_robot_vacuum(draw):
    draw.ellipse([8, 12, 42, 42], fill=(0,0,0,80)) # floor shadow
    # main circular body
    draw.ellipse([8, 8, 42, 38], fill=DKGREY, outline=BLACK, width=1)
    draw.ellipse([10, 10, 40, 36], fill=BLACK)
    # bumper curve
    draw.arc([8, 8, 42, 38], 45, 135, fill=GREY, width=2)
    # power indicator green LED
    draw.ellipse([23, 21, 27, 25], fill=GREEN)

# --- 47. Digital Camcorder ---
def draw_digital_camcorder(draw):
    # body + hand strap
    draw.rounded_rectangle([12, 14, 38, 34], radius=2, fill=BLACK, outline=GREY, width=1)
    # lens cylinder
    draw.ellipse([10, 16, 16, 26], fill=GREY)
    draw.ellipse([11, 18, 15, 24], fill=CYAN)
    # flip-out preview screen
    draw.rectangle([20, 16, 36, 30], fill=GREY)
    draw.rectangle([22, 18, 34, 28], fill=BLUE)
    draw.line([14, 30, 36, 30], fill=DKGREY, width=2)

# --- 48. Personal Walkman ---
def draw_personal_walkman(draw):
    # casing
    draw.rounded_rectangle([12, 10, 38, 42], radius=2, fill=BLUE, outline=BLACK, width=1)
    draw.rectangle([12, 26, 38, 42], fill=DKBLUE)
    # cassette gear window
    draw.rectangle([16, 14, 34, 26], fill=BLACK)
    draw.ellipse([20, 18, 24, 22], fill=WHITE)
    draw.ellipse([26, 18, 30, 22], fill=WHITE)
    # playback control buttons
    draw.rectangle([38, 16, 40, 20], fill=SILVER)
    draw.rectangle([38, 22, 40, 26], fill=SILVER)

# --- 49. Retro Game Handheld ---
def draw_retro_game_handheld(draw):
    # console body
    draw.rounded_rectangle([12, 6, 38, 44], radius=3, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([12, 25, 38, 44], fill=DKGREY)
    # green matrix screen
    draw.rectangle([16, 10, 34, 22], fill=BLACK)
    draw.rectangle([18, 12, 32, 20], fill=DKGREEN)
    # controls D-pad & action buttons
    draw.line([16, 31, 22, 31], fill=BLACK, width=2)
    draw.line([19, 28, 19, 34], fill=BLACK, width=2)
    draw.ellipse([28, 32, 30, 34], fill=RED)
    draw.ellipse([32, 29, 34, 31], fill=RED)

# --- 50. Smart Thermostat ---
def draw_smart_thermostat(draw):
    # dial outer ring
    draw.ellipse([10, 10, 40, 40], fill=SILVER, outline=BLACK, width=1)
    draw.ellipse([12, 12, 38, 38], fill=BLACK)
    # digital screen display
    draw.ellipse([15, 15, 35, 35], fill=DKBLUE)
    draw.arc([13, 13, 37, 37], 0, 360, fill=CYAN, width=1)
    # temperature numbers
    draw.line([22, 22, 25, 22], fill=WHITE, width=2)
    draw.line([25, 22, 22, 28], fill=WHITE, width=2)
    draw.line([27, 24, 29, 24], fill=WHITE, width=2)

# --- 51. CRT Monitor ---
def draw_crt_monitor(draw):
    # back housing casing
    draw.rectangle([15, 14, 35, 30], fill=DKGREY, outline=BLACK, width=1)
    for y in range(16, 28, 3):
        draw.line([17, y, 33, y], fill=BLACK, width=1) # vents
    # front screen bezel
    draw.rounded_rectangle([11, 9, 39, 31], radius=3, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([14, 12, 36, 28], fill=BLACK)
    draw.ellipse([15, 13, 35, 27], fill=STEEL)
    draw.line([17, 15, 22, 20], fill=WHITE, width=1)
    # base
    draw.rectangle([22, 31, 28, 35], fill=GREY)
    draw.ellipse([18, 34, 32, 37], fill=BLACK)

# --- 52. Plasma TV ---
def draw_plasma_tv(draw):
    # television chassis
    draw.rectangle([6, 12, 44, 32], fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([9, 13, 41, 31], fill=BLACK)
    draw.rectangle([10, 14, 40, 30], fill=DKBLUE)
    # side speaker grills
    draw.rectangle([6, 12, 8, 32], fill=GREY)
    draw.rectangle([42, 12, 44, 32], fill=GREY)
    # wall mount stand
    draw.rectangle([21, 32, 29, 36], fill=BLACK)
    draw.ellipse([16, 35, 34, 38], fill=SILVER)

# --- 53. Pager ---
def draw_pager(draw):
    # pager housing
    draw.rounded_rectangle([12, 14, 38, 36], radius=2, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([14, 18, 36, 26], fill=DKGREEN)
    # digital pager message text
    draw.line([16, 22, 20, 22], fill=BLACK, width=1)
    draw.line([23, 22, 27, 22], fill=BLACK, width=1)
    # buttons & pager clip representation
    draw.rectangle([16, 29, 22, 32], fill=GREY)
    draw.ellipse([30, 30, 33, 33], fill=RED)

# --- 54. Satellite Dish ---
def draw_satellite_dish(draw):
    # white parabolic dish
    draw.ellipse([8, 8, 36, 32], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([12, 11, 32, 29], fill=GREY)
    # feed LNB arm receiver
    draw.line([22, 20, 42, 28], fill=BLACK, width=2)
    draw.rectangle([40, 25, 44, 31], fill=RED)
    # stand pole mount
    draw.line([22, 20, 22, 44], fill=STEEL, width=2)
    draw.line([16, 44, 28, 44], fill=BLACK, width=3)

# --- 55. E-Reader ---
def draw_e_reader(draw):
    # bezel frame
    draw.rounded_rectangle([12, 6, 38, 44], radius=2, fill=GREY, outline=BLACK, width=1)
    # e-ink screen & text lines
    draw.rectangle([15, 9, 35, 38], fill=WHITE)
    for y in range(12, 36, 3):
        draw.line([18, y, 32, y], fill=DKGREY, width=1)
    # home button
    draw.rectangle([22, 40, 28, 42], fill=BLACK)

# --- 56. Pocket Gaming Pet (Tamagotchi) ---
def draw_pocket_gaming_pet(draw):
    # egg body design
    draw.ellipse([12, 10, 38, 42], fill=PURPLE, outline=BLACK, width=1)
    draw.ellipse([14, 12, 36, 40], fill=YELLOW)
    # LCD panel display screen
    draw.rectangle([18, 16, 32, 28], fill=GREY, outline=BLACK, width=1)
    # digital pet character dots
    draw.rectangle([23, 21, 27, 23], fill=BLACK)
    # 3 action buttons
    draw.ellipse([18, 32, 21, 35], fill=RED)
    draw.ellipse([24, 34, 27, 37], fill=RED)
    draw.ellipse([30, 32, 33, 35], fill=RED)

# --- 57. Synthesizer ---
def draw_synthesizer(draw):
    draw.rectangle([4, 14, 46, 36], fill=BLACK, outline=GREY, width=1)
    # black and white keys
    draw.rectangle([6, 26, 44, 34], fill=WHITE)
    for x in range(8, 44, 4):
        draw.line([x, 26, x, 34], fill=BLACK, width=1)
        if x in [12, 16, 24, 28, 32, 40]:
            draw.rectangle([x-1, 26, x+1, 31], fill=BLACK)
    # controls dial knobs and sliders
    for x in range(8, 42, 6):
        draw.ellipse([x, 18, x+2, 20], fill=RED if x == 8 else YELLOW)
    draw.line([30, 22, 40, 22], fill=CYAN, width=1)

# --- 58. Laser Pointer ---
def draw_laser_pointer(draw):
    # metallic steel barrel tube
    draw.line([8, 12, 34, 38], fill=SILVER, width=4)
    draw.line([9, 13, 35, 39], fill=GREY, width=2)
    # brass aperture cap tip
    draw.line([33, 37, 36, 40], fill=GOLD, width=3)
    # red power button
    draw.ellipse([18, 22, 20, 24], fill=RED)
    # red laser line path
    draw.line([36, 40, 48, 48], fill=RED, width=1)
    draw.ellipse([46, 46, 49, 49], fill=CYAN)

# --- 59. Barcode Scanner ---
def draw_barcode_scanner(draw):
    # scanner pistol head and handle body
    draw.polygon([(14, 24), (24, 20), (28, 26), (18, 30)], fill=DKGREY, outline=BLACK, width=1)
    draw.polygon([(18, 30), (24, 26), (28, 38), (22, 42)], fill=GREY)
    # safety yellow shell bumper
    draw.line([12, 23, 16, 29], fill=YELLOW, width=3)
    # laser beam scan output
    draw.line([10, 32, 10, 44], fill=RED, width=1)
    draw.polygon([(14,24), (10,32), (10,44)], fill=(255, 0, 0, 80))

# --- 60. DVD Player ---
def draw_dvd_player(draw):
    # chassis deck
    draw.rounded_rectangle([6, 20, 44, 34], radius=1, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([6, 28, 44, 34], fill=DKGREY)
    # ejected disc drawer tray
    draw.rectangle([14, 26, 36, 30], fill=GREY)
    # DVD disc reflective ring
    draw.ellipse([19, 26, 31, 30], fill=CYAN)
    draw.ellipse([23, 27, 27, 29], fill=BLACK)
    # display panel
    draw.rectangle([10, 30, 20, 32], fill=BLUE)

# --- 61. Digital Scale ---
def draw_digital_scale(draw):
    # steel weighing platform
    draw.rectangle([8, 22, 42, 27], fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([8, 26, 42, 27], fill=GREY)
    # scale base casing
    draw.polygon([(10, 27), (40, 27), (42, 38), (8, 38)], fill=DKGREY)
    # LCD digital screen weight readout
    draw.rectangle([18, 30, 32, 35], fill=BLACK)
    draw.rectangle([19, 31, 31, 34], fill=GREEN)

# --- 62. Metal Detector ---
def draw_metal_detector(draw):
    # electromagnetic search coil sensor plate
    draw.ellipse([10, 38, 34, 43], fill=BLACK, outline=GREY, width=1)
    draw.ellipse([14, 39, 30, 42], fill=WHITE)
    # shaft stem support
    draw.line([22, 39, 28, 16], fill=SILVER, width=2)
    # control dials panel housing
    draw.rectangle([25, 14, 32, 20], fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([27, 16, 30, 18], fill=CYAN)

# --- 63. Laserdisc Player ---
def draw_laserdisc_player(draw):
    # deck unit
    draw.rounded_rectangle([6, 14, 44, 36], radius=2, fill=GREY, outline=BLACK, width=1)
    # tray drawer slot
    draw.rectangle([8, 22, 42, 30], fill=BLACK)
    # 12-inch Laserdisc silver mirror surface
    draw.ellipse([10, 20, 40, 32], fill=SILVER)
    draw.ellipse([12, 22, 38, 30], fill=CYAN)
    draw.ellipse([23, 25, 27, 27], fill=BLACK)

# --- 64. Electronic Drum Kit ---
def draw_e_drum_kit(draw):
    # rack framework bars
    draw.line([10, 38, 40, 38], fill=BLACK, width=2)
    draw.line([16, 20, 16, 42], fill=BLACK, width=2)
    draw.line([34, 20, 34, 42], fill=BLACK, width=2)
    # trigger pads
    draw.ellipse([10, 24, 18, 29], fill=GREY, outline=BLACK, width=1)
    draw.ellipse([21, 26, 29, 31], fill=GREY, outline=BLACK, width=1)
    draw.ellipse([32, 24, 40, 29], fill=GREY, outline=BLACK, width=1)
    # yellow cymbal pads
    draw.polygon([(8,14), (16,12), (18,18)], fill=YELLOW)
    draw.polygon([(32,14), (40,12), (34,18)], fill=YELLOW)

# --- 65. HDMI Switch ---
def draw_hdmi_switch(draw):
    draw.rounded_rectangle([10, 18, 40, 32], radius=1, fill=DKGREY, outline=BLACK, width=1)
    # ports markings
    for x in range(14, 38, 6):
        draw.rectangle([x, 18, x+3, 20], fill=BLACK)
    # select button
    draw.ellipse([20, 25, 24, 28], fill=GREY)
    # indicators active channel
    draw.ellipse([30, 26, 32, 28], fill=GREEN)
    draw.ellipse([34, 26, 36, 28], fill=RED)

# --- 66. Smart Plug ---
def draw_smart_plug(draw):
    draw.ellipse([14, 14, 36, 36], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([15, 15, 35, 35], fill=GREY)
    # Outlet receptacles
    draw.rectangle([20, 20, 22, 24], fill=BLACK)
    draw.rectangle([28, 20, 30, 24], fill=BLACK)
    draw.ellipse([23, 28, 27, 31], fill=BLACK)
    # Halo glow ring
    draw.arc([14, 14, 36, 36], 0, 360, fill=CYAN, width=1)

# --- 67. Fingerprint Scanner ---
def draw_fingerprint_scanner(draw):
    draw.rounded_rectangle([12, 10, 38, 42], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # scanning window
    draw.rectangle([16, 14, 34, 34], fill=BLACK)
    draw.rectangle([18, 16, 32, 32], fill=DKBLUE)
    # fingerprint lines
    draw.arc([22, 20, 28, 28], 180, 360, fill=BLUE, width=1)
    draw.arc([20, 22, 30, 30], 180, 360, fill=BLUE, width=1)
    # green scanning beam line
    draw.line([16, 24, 34, 24], fill=GREEN, width=2)

# --- 68. GPS Navigator ---
def draw_gps_navigator(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([10, 14, 40, 36], fill=DKGREY)
    # map road route screen
    draw.rectangle([12, 16, 38, 34], fill=GREEN)
    draw.line([14, 20, 22, 28, 36, 22], fill=RED, width=2)

# --- 69. Pocket Translator ---
def draw_pocket_translator(draw):
    # folding translator clamshell design
    draw.polygon([(10, 24), (40, 24), (44, 8), (6, 8)], fill=GREY, outline=BLACK, width=1)
    draw.polygon([(10, 24), (40, 24), (36, 40), (14, 40)], fill=DKGREY)
    # translation LCD screen
    draw.polygon([(12, 22), (38, 22), (40, 10), (10, 10)], fill=BLUE)
    # buttons grid
    for y in range(27, 39, 3):
        draw.line([16, y, 34, y], fill=WHITE, width=1)

# --- 70. Smart Lock ---
def draw_smart_lock(draw):
    # metal handle plate
    draw.rounded_rectangle([18, 6, 32, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    # touch digit screen pad
    draw.rectangle([21, 10, 29, 24], fill=DKGREY)
    for y in range(12, 24, 3):
        draw.line([23, y, 27, y], fill=WHITE, width=1)
    # handle door lever
    draw.rectangle([22, 28, 28, 32], fill=SILVER)
    draw.line([25, 30, 42, 30], fill=SILVER, width=4)

# --- 71. Step Pedometer ---
def draw_pedometer(draw):
    # belt clip-on case
    draw.rounded_rectangle([14, 14, 36, 36], radius=4, fill=ORANGE, outline=BLACK, width=1)
    draw.rectangle([14, 25, 36, 36], fill=DKRED)
    # step display screen
    draw.rectangle([17, 18, 33, 24], fill=GREY)
    draw.line([19, 21, 23, 21], fill=BLACK, width=1)
    draw.line([25, 21, 29, 21], fill=BLACK, width=1)

# --- 72. Audio Mixer ---
def draw_audio_mixer(draw):
    # sound board desk console
    draw.rectangle([6, 8, 44, 42], fill=GREY, outline=BLACK, width=1)
    # knobs array
    for x in range(10, 42, 6):
        draw.ellipse([x, 12, x+2, 14], fill=RED)
        draw.ellipse([x, 18, x+2, 20], fill=GREEN)
        draw.ellipse([x, 24, x+2, 26], fill=YELLOW)
    # sliding level faders
    for x in range(10, 42, 6):
        draw.line([x+1, 30, x+1, 38], fill=BLACK, width=1)
        draw.rectangle([x, 33, x+2, 35], fill=WHITE)

# --- 73. Karaoke Machine ---
def draw_karaoke_machine(draw):
    # speaker cabinet enclosure
    draw.rounded_rectangle([12, 8, 38, 42], radius=2, fill=PURPLE, outline=BLACK, width=1)
    draw.rectangle([12, 25, 38, 42], fill=BLACK)
    # lyrics display screen
    draw.rectangle([15, 12, 35, 22], fill=BLUE)
    draw.line([18, 15, 32, 15], fill=YELLOW, width=1)
    draw.line([18, 18, 28, 18], fill=YELLOW, width=1)
    # speaker driver cone
    draw.ellipse([20, 28, 30, 38], fill=GREY)
    draw.ellipse([15, 40, 17, 42], fill=SILVER)

# --- 74. Hearing Aid ---
def draw_hearing_aid(draw):
    # beige unit body
    draw.ellipse([20, 16, 30, 32], fill=BROWN, outline=BLACK, width=1)
    draw.ellipse([22, 18, 28, 30], fill=(255, 255, 255, 0))
    # acoustic output tubing
    draw.line([25, 16, 25, 8], fill=WHITE, width=1)
    draw.line([25, 8, 16, 8], fill=WHITE, width=1)
    draw.ellipse([14, 6, 18, 12], fill=BROWN)

# --- 75. Laser Engraver ---
def draw_laser_engraver(draw):
    # wood board workpiece
    draw.rectangle([12, 30, 38, 40], fill=BROWN, outline=BLACK, width=1)
    draw.line([16, 35, 28, 35], fill=BLACK, width=2) # laser engraving path
    # overhead laser gantry emitter
    draw.rectangle([21, 6, 29, 14], fill=DKGREY, outline=BLACK, width=1)
    draw.line([25, 14, 25, 35], fill=CYAN, width=1)
    draw.ellipse([23, 33, 27, 37], fill=WHITE)

# --- 76. Geiger Counter ---
def draw_geiger_counter(draw):
    # yellow radiation testing box
    draw.rounded_rectangle([14, 12, 36, 38], radius=2, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([14, 25, 36, 38], fill=DKGREY)
    # radiation level needle gauge
    draw.rectangle([17, 15, 33, 22], fill=WHITE)
    draw.arc([19, 19, 31, 25], 180, 360, fill=BLACK, width=1)
    draw.line([25, 22, 29, 17], fill=RED, width=1)
    # clicker sound speaker holes
    draw.ellipse([20, 28, 22, 30], fill=BLACK)
    draw.ellipse([24, 28, 26, 30], fill=BLACK)

# --- 77. Electric Guitar ---
def draw_e_guitar(draw):
    # red solid guitar body styling
    draw.ellipse([14, 24, 30, 42], fill=RED, outline=BLACK, width=1)
    draw.ellipse([16, 26, 28, 38], fill=DKRED)
    # neck with frets
    draw.line([22, 28, 22, 4], fill=BROWN, width=2)
    # headstock tuners
    draw.rectangle([21, 4, 24, 8], fill=BLACK)
    draw.rectangle([20, 32, 24, 34], fill=SILVER)
    draw.rectangle([20, 36, 24, 38], fill=SILVER)

# --- 78. Dial-Up Modem ---
def draw_modem(draw):
    # modem chassis
    draw.rounded_rectangle([8, 20, 42, 36], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([8, 28, 42, 36], fill=DKGREY)
    # telephone ports
    draw.rectangle([10, 20, 14, 23], fill=BLACK)
    draw.rectangle([18, 20, 22, 23], fill=BLACK)
    # flashing status indicators
    draw.ellipse([12, 31, 14, 33], fill=GREEN)
    draw.ellipse([18, 31, 20, 33], fill=GREEN)
    draw.ellipse([24, 31, 26, 33], fill=YELLOW)
    draw.ellipse([30, 31, 32, 33], fill=RED)

# --- 79. RFID Reader ---
def draw_rfid_reader(draw):
    # wall access controller unit
    draw.rounded_rectangle([15, 10, 35, 42], radius=3, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([18, 14, 32, 34], fill=DKGREY)
    # waves wireless indicator icon
    draw.arc([21, 18, 29, 26], 315, 45, fill=SILVER, width=2)
    draw.arc([23, 20, 27, 24], 315, 45, fill=SILVER, width=2)
    # swipe access card
    draw.rectangle([12, 28, 26, 38], fill=BLUE, outline=BLACK, width=1)
    draw.ellipse([25, 12, 27, 14], fill=GREEN)

# --- 80. Digital Frame ---
def draw_digital_frame(draw):
    # display frame
    draw.rounded_rectangle([8, 12, 42, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    # pixel artwork slide showing sunset scene
    draw.rectangle([11, 15, 39, 35], fill=BLUE)
    draw.ellipse([30, 24, 38, 32], fill=YELLOW)
    draw.rectangle([11, 28, 39, 35], fill=GREEN)

# --- 81. Magnifying Lamp ---
def draw_magnifying_lamp(draw):
    # heavy desk clamp base
    draw.ellipse([12, 38, 28, 43], fill=BLACK)
    # flexible joints arm
    draw.line([20, 40, 20, 24], fill=STEEL, width=2)
    draw.line([20, 24, 32, 18], fill=STEEL, width=2)
    # magnifier ring lamp head
    draw.ellipse([28, 10, 42, 20], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([31, 12, 39, 18], fill=LIGHTBLUE)

# --- 82. Car Key Fob ---
def draw_car_key_fob(draw):
    # black remote fob
    draw.rounded_rectangle([16, 12, 34, 38], radius=3, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([16, 25, 34, 38], fill=DKGREY)
    # locking buttons
    draw.rectangle([21, 16, 25, 20], fill=GREY)
    draw.rectangle([21, 23, 25, 27], fill=GREY)
    # key ring loop
    draw.arc([22, 36, 28, 42], 0, 180, fill=SILVER, width=2)
    draw.ellipse([29, 16, 31, 18], fill=RED)

# --- 83. Electronic Construction Level ---
def draw_electronic_level(draw):
    # yellow aluminum block level frame
    draw.rounded_rectangle([4, 20, 46, 30], radius=1, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([4, 26, 46, 30], fill=ORANGE)
    # bubble vial detail
    draw.rectangle([15, 22, 25, 26], fill=GREEN)
    draw.ellipse([19, 23, 21, 25], fill=BLACK)
    # digital angle screen
    draw.rectangle([29, 22, 40, 26], fill=BLACK)
    draw.line([31, 24, 35, 24], fill=CYAN, width=1)

# --- 84. Hair Dryer ---
def draw_hair_dryer(draw):
    # gun nozzle handle
    draw.line([24, 26, 24, 42], fill=BLACK, width=4)
    # blower heating barrel body
    draw.line([14, 18, 34, 18], fill=RED, width=8)
    draw.line([14, 22, 34, 22], fill=DKRED, width=6)
    # front outlet nozzle and switches
    draw.rectangle([12, 14, 15, 25], fill=BLACK)
    draw.ellipse([32, 14, 36, 25], fill=GREY)
    draw.ellipse([24, 32, 25, 34], fill=RED)

# --- 85. Label Maker ---
def draw_label_maker(draw):
    # handheld label maker body
    draw.rounded_rectangle([14, 12, 36, 42], radius=4, fill=BLUE, outline=BLACK, width=1)
    # print message LCD screen
    draw.rectangle([18, 16, 32, 22], fill=GREY)
    # keyboard print buttons
    for y in range(26, 40, 3):
        draw.line([18, y, 32, y], fill=WHITE, width=1)
    # printed label tape emerging from print slot
    draw.rectangle([21, 8, 29, 12], fill=WHITE, outline=BLACK, width=1)
    draw.line([23, 10, 27, 10], fill=BLACK, width=1)

# --- 86. Smart Mirror ---
def draw_smart_mirror(draw):
    # vanity mirror frame
    draw.rectangle([8, 6, 42, 44], fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([10, 8, 40, 42], fill=LIGHTBLUE)
    # white pixels glowing smart information overlays
    draw.rectangle([14, 12, 20, 16], fill=WHITE)
    draw.line([26, 12, 34, 12], fill=WHITE, width=1)
    draw.line([28, 15, 32, 15], fill=WHITE, width=1)

# --- 87. Stage Strobe Light ---
def draw_strobe_light(draw):
    # mounting swing bracket
    draw.arc([10, 12, 40, 38], 0, 180, fill=BLACK, width=2)
    # lamp body cylinder casing
    draw.rounded_rectangle([14, 16, 36, 32], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([14, 24, 36, 32], fill=DKGREY)
    # xenon strobe flash glass tube
    draw.ellipse([20, 18, 30, 28], fill=CYAN)
    draw.line([22, 23, 28, 23], fill=WHITE, width=2)

# --- 88. Electronic Drum Sampler (MPC) ---
def draw_electronic_drum_pad(draw):
    draw.rounded_rectangle([10, 10, 40, 40], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([12, 12, 38, 18], fill=CYAN)
    # 4x4 matrix of drum sampler trigger pads
    for y in [22, 26, 30, 34]:
        for x in [14, 20, 26, 32]:
            pad_color = RED if (x == 20 and y == 30) else GREY
            draw.rectangle([x, y, x+4, y+3], fill=pad_color, outline=BLACK, width=1)

# --- 89. Solar Inverter ---
def draw_solar_inverter(draw):
    # inverter block
    draw.rounded_rectangle([14, 10, 36, 42], radius=2, fill=WHITE, outline=GREY, width=1)
    # cooling fins
    draw.rectangle([12, 16, 14, 36], fill=GREY)
    draw.rectangle([36, 16, 38, 36], fill=GREY)
    # LCD readout
    draw.rectangle([18, 16, 32, 22], fill=BLACK)
    draw.rectangle([19, 17, 31, 21], fill=GREEN)
    draw.ellipse([21, 26, 23, 28], fill=GREEN)
    draw.ellipse([27, 26, 29, 28], fill=YELLOW)

# --- 90. RJ45 Cable Tester ---
def draw_cable_tester(draw):
    draw.rounded_rectangle([12, 12, 38, 40], radius=2, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([16, 16, 34, 22], fill=DKGREY)
    # line testing progress indicators LEDs
    for i, x in enumerate(range(16, 34, 4)):
        led_color = GREEN if i < 3 else GREY
        draw.ellipse([x, 26, x+2, 28], fill=led_color)
    draw.line([25, 12, 25, 40], fill=BLACK, width=1)

# --- 91. Apartment Intercom ---
def draw_intercom(draw):
    # wall station plate
    draw.rounded_rectangle([15, 8, 35, 42], radius=2, fill=WHITE, outline=GREY, width=1)
    draw.rectangle([15, 25, 35, 42], fill=GREY)
    # speaker grill
    for y in range(12, 22, 2):
        draw.line([18, y, 32, y], fill=BLACK, width=1)
    # call controls
    draw.ellipse([20, 28, 23, 31], fill=RED)
    draw.ellipse([27, 28, 30, 31], fill=GREEN)
    draw.line([17, 34, 33, 34], fill=BLACK, width=2)

# --- 92. Smart Battery Charger ---
def draw_battery_charger(draw):
    # charger bay
    draw.rounded_rectangle([12, 10, 38, 42], radius=2, fill=BLACK, outline=GREY, width=1)
    for x in [15, 20, 25, 30]:
        draw.rectangle([x, 14, x+3, 34], fill=DKGREY)
        # charging AA cells
        draw.rectangle([x, 18, x+3, 32], fill=ORANGE)
        draw.ellipse([x+1, 37, x+2, 39], fill=GREEN if x < 25 else RED)

# --- 93. Weather Station ---
def draw_weather_station(draw):
    draw.rounded_rectangle([10, 10, 40, 40], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([12, 12, 38, 38], fill=BLACK)
    # LCD charts graphics weather icon
    draw.ellipse([16, 18, 22, 24], fill=YELLOW)
    draw.line([15, 32, 20, 28, 25, 33, 35, 29], fill=CYAN, width=1)

# --- 94. DVD-ROM PC Drive ---
def draw_dvd_rom_drive(draw):
    draw.rectangle([8, 18, 42, 34], fill=GREY, outline=BLACK, width=1)
    # ejected optical tray
    draw.rectangle([10, 24, 40, 30], fill=BLACK)
    # DVD silver layout
    draw.ellipse([14, 22, 36, 32], fill=SILVER)
    draw.ellipse([21, 24, 29, 30], fill=CYAN)
    draw.ellipse([23, 26, 27, 28], fill=BLACK)

# --- 95. Television Soundbar ---
def draw_soundbar(draw):
    # soundbar slim profile
    draw.rounded_rectangle([4, 22, 46, 28], radius=1, fill=BLACK, outline=GREY, width=1)
    # mesh grille patterns
    for x in range(6, 44, 3):
        draw.line([x, 23, x, 27], fill=DKGREY, width=1)
    # center readout
    draw.rectangle([21, 23, 29, 27], fill=BLACK)
    draw.line([23, 25, 27, 25], fill=CYAN, width=1)

# --- 96. Sports Car VHS Rewinder ---
def draw_vhs_rewinder(draw):
    # red sports car shape
    draw.rounded_rectangle([10, 16, 40, 36], radius=4, fill=RED, outline=BLACK, width=1)
    draw.rectangle([10, 24, 40, 36], fill=DKRED)
    # hood hatch window
    draw.polygon([(14, 22), (20, 16), (30, 16), (36, 22)], fill=BLACK)
    # wheels
    draw.ellipse([12, 32, 18, 38], fill=BLACK)
    draw.ellipse([32, 32, 38, 38], fill=BLACK)
    draw.ellipse([38, 22, 40, 24], fill=GREEN)

# --- 97. Digital USB Microscope ---
def draw_e_microscope(draw):
    # specimen stage clamp plate
    draw.ellipse([14, 38, 36, 43], fill=BLACK)
    # stand rod
    draw.line([25, 20, 25, 40], fill=SILVER, width=2)
    # focus barrel zoom lens cylinder
    draw.line([16, 14, 30, 28], fill=DKGREY, width=4)
    draw.ellipse([21, 19, 25, 23], fill=BLUE) # focus dial
    draw.ellipse([26, 32, 32, 36], fill=(0, 255, 255, 100)) # light spot

# --- 98. Electric Skateboard ---
def draw_e_skateboard(draw):
    # wooden board deck
    draw.polygon([(8, 22), (42, 22), (44, 25), (42, 28), (8, 28), (6, 25)], fill=BROWN, outline=BLACK, width=1)
    # battery case pack block underneath
    draw.rectangle([14, 28, 36, 31], fill=BLACK)
    # hub motor orange wheels
    draw.ellipse([10, 28, 14, 32], fill=ORANGE)
    draw.ellipse([36, 28, 40, 32], fill=ORANGE)

# --- 99. Gimbal Camera Stabilizer ---
def draw_gimbal_stabilizer(draw):
    # handheld stabilizer grip stick
    draw.line([25, 26, 25, 44], fill=GREY, width=3)
    # gyro joints brackets arm
    draw.arc([16, 16, 34, 28], 0, 180, fill=BLACK, width=2)
    # smartphone mount clamp
    draw.rounded_rectangle([18, 10, 32, 20], radius=1, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([20, 12, 30, 18], fill=CYAN)

# --- 100. Smart Video Doorbell ---
def draw_smart_doorbell(draw):
    # wall plate unit
    draw.rounded_rectangle([18, 8, 32, 42], radius=2, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([18, 25, 32, 42], fill=GREY)
    # camera lens eye
    draw.ellipse([22, 12, 28, 18], fill=DKGREY)
    draw.ellipse([24, 14, 26, 16], fill=BLUE)
    # doorbell push button with glowing cyan ring
    draw.ellipse([22, 30, 28, 36], fill=CYAN)
    draw.ellipse([23, 31, 27, 35], fill=WHITE)

# Compile drawing list (100 items total)
# DRAWINGS compiled at the bottom of the file to avoid NameErrors

# --- 101. Laser Printer Toner ---
def draw_laser_printer_toner(draw):
    draw.rounded_rectangle([10, 14, 40, 36], radius=3, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([14, 18, 36, 22], fill=CYAN)
    draw.rectangle([18, 32, 32, 35], fill=GREY)
    draw.ellipse([11, 23, 13, 27], fill=YELLOW)

# --- 102. USB Hub ---
def draw_usb_hub(draw):
    draw.rounded_rectangle([12, 16, 38, 34], radius=2, fill=GREY, outline=BLACK, width=1)
    for y in range(20, 32, 4):
        draw.rectangle([34, y, 38, y+2], fill=BLACK)
    draw.ellipse([18, 20, 20, 22], fill=GREEN)
    draw.line([25, 16, 25, 6], fill=STEEL, width=2)

# --- 103. HDMI Splitter ---
def draw_hdmi_splitter(draw):
    draw.rounded_rectangle([10, 18, 40, 32], radius=1, fill=DKGREY, outline=BLACK, width=1)
    for x in range(14, 38, 6):
        draw.rectangle([x, 18, x+3, 20], fill=BLACK)
    draw.ellipse([16, 26, 18, 28], fill=RED)
    draw.ellipse([24, 26, 26, 28], fill=GREEN)
    draw.ellipse([32, 26, 34, 28], fill=GREEN)

# --- 104. Car Radar Detector ---
def draw_car_radar_detector(draw):
    draw.polygon([(12, 36), (38, 36), (34, 18), (16, 18)], fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([16, 22, 34, 30], fill=BLACK)
    draw.line([18, 26, 22, 26], fill=RED, width=1)
    draw.line([24, 26, 28, 26], fill=YELLOW, width=1)
    draw.line([30, 26, 32, 26], fill=GREEN, width=1)
    draw.line([25, 18, 25, 12], fill=SILVER, width=1)

# --- 105. Electronic Dictionary ---
def draw_electronic_dictionary(draw):
    draw.polygon([(8, 24), (42, 24), (46, 8), (4, 8)], fill=GREY, outline=BLACK, width=1)
    draw.polygon([(8, 24), (42, 24), (38, 40), (12, 40)], fill=DKGREY)
    draw.polygon([(11, 22), (39, 22), (42, 10), (8, 10)], fill=BLUE)
    draw.line([14, 15, 36, 15], fill=WHITE, width=1)
    draw.line([16, 18, 34, 18], fill=WHITE, width=1)
    for y in range(27, 39, 3):
        draw.line([15, y, 35, y], fill=WHITE, width=1)

# --- 106. LED Flashlight ---
def draw_led_flashlight(draw):
    draw.line([12, 34, 32, 14], fill=DKGREY, width=6)
    draw.line([14, 32, 30, 16], fill=BLACK, width=2)
    draw.polygon([(26, 10), (38, 22), (32, 28), (20, 16)], fill=SILVER, outline=BLACK, width=1)
    draw.line([27, 13, 33, 19], fill=YELLOW, width=2)
    draw.polygon([(30,16), (46,6), (46,26)], fill=(255, 255, 200, 100))

# --- 107. Electric Toothbrush ---
def draw_electric_toothbrush(draw):
    draw.ellipse([18, 38, 32, 44], fill=GREY, outline=BLACK, width=1)
    draw.rounded_rectangle([22, 16, 28, 39], radius=1, fill=WHITE, outline=BLACK, width=1)
    draw.rectangle([22, 22, 28, 32], fill=CYAN)
    draw.ellipse([24, 34, 26, 36], fill=GREEN)
    draw.line([25, 16, 25, 6], fill=SILVER, width=2)
    draw.rectangle([23, 6, 27, 10], fill=WHITE)
    draw.line([23, 7, 23, 9], fill=BLUE, width=1)

# --- 108. Baby Monitor ---
def draw_baby_monitor(draw):
    draw.rounded_rectangle([8, 14, 26, 36], radius=2, fill=WHITE, outline=BLACK, width=1)
    draw.rectangle([10, 18, 24, 30], fill=BLUE)
    draw.ellipse([17, 32, 19, 34], fill=GREY)
    draw.ellipse([32, 24, 42, 36], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([34, 26, 40, 32], fill=BLACK)
    draw.ellipse([36, 28, 38, 30], fill=CYAN)

# --- 109. Electronic Luggage Scale ---
def draw_e_luggage_scale(draw):
    draw.rounded_rectangle([10, 12, 40, 18], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([18, 14, 32, 20], fill=BLACK)
    draw.rectangle([19, 15, 31, 19], fill=GREEN)
    draw.line([25, 18, 25, 34], fill=SILVER, width=2)
    draw.arc([20, 32, 30, 42], 0, 180, fill=STEEL, width=2)

# --- 110. Smart Water Leak Sensor ---
def draw_smart_water_leak_sensor(draw):
    draw.ellipse([10, 12, 40, 38], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([12, 14, 38, 34], fill=SILVER)
    draw.arc([14, 16, 36, 32], 0, 360, fill=BLUE, width=2)
    draw.ellipse([23, 22, 27, 26], fill=CYAN)
    draw.ellipse([18, 36, 20, 38], fill=GOLD)
    draw.ellipse([30, 36, 32, 38], fill=GOLD)

# --- 111. Digital Reading Magnifier ---
def draw_digital_magnifier(draw):
    draw.rounded_rectangle([8, 10, 42, 40], radius=3, fill=BLUE, outline=BLACK, width=1)
    draw.rectangle([11, 13, 39, 31], fill=WHITE)
    draw.rectangle([16, 18, 22, 26], fill=BLACK)
    draw.rectangle([28, 18, 34, 26], fill=BLACK)
    draw.ellipse([15, 34, 18, 37], fill=RED)
    draw.ellipse([23, 34, 26, 37], fill=WHITE)
    draw.ellipse([31, 34, 34, 37], fill=GREEN)

# --- 112. Smart Smoke Detector ---
def draw_smart_smoke_detector(draw):
    draw.ellipse([8, 8, 42, 42], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([12, 12, 38, 38], fill=SILVER)
    draw.ellipse([20, 20, 30, 30], fill=BLACK)
    draw.ellipse([22, 22, 28, 28], fill=GREEN)
    for x in range(14, 38, 4):
        draw.line([x, 14, x, 16], fill=DKGREY, width=1)
        draw.line([x, 34, x, 36], fill=DKGREY, width=1)

# --- 113. Wireless Earbuds ---
def draw_wireless_earbuds(draw):
    draw.rounded_rectangle([10, 16, 40, 42], radius=4, fill=WHITE, outline=BLACK, width=1)
    draw.rectangle([10, 26, 40, 42], fill=GREY)
    draw.ellipse([16, 20, 22, 26], fill=BLACK)
    draw.ellipse([28, 20, 34, 26], fill=BLACK)
    draw.ellipse([17, 21, 21, 25], fill=WHITE)
    draw.ellipse([29, 21, 33, 25], fill=WHITE)
    draw.ellipse([23, 32, 27, 36], fill=CYAN)

# --- 114. Graphics Tablet ---
def draw_graphics_tablet(draw):
    draw.rounded_rectangle([6, 12, 44, 38], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([12, 14, 42, 36], fill=BLACK)
    draw.ellipse([9, 18, 10, 20], fill=GREY)
    draw.ellipse([9, 24, 10, 26], fill=GREY)
    draw.ellipse([9, 30, 10, 32], fill=GREEN)
    draw.line([14, 14, 36, 36], fill=SILVER, width=2)
    draw.line([14, 14, 16, 16], fill=BLACK, width=2)

# --- 115. Digital Portable Air Pump ---
def draw_digital_air_pump(draw):
    draw.rounded_rectangle([16, 10, 34, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([19, 14, 31, 20], fill=DKGREY)
    draw.rectangle([21, 16, 29, 18], fill=CYAN)
    draw.ellipse([23, 25, 27, 29], fill=WHITE)
    draw.arc([14, 4, 32, 18], 180, 360, fill=BLACK, width=3)

# --- 116. Smart Irrigation Timer ---
def draw_smart_irrigation_timer(draw):
    draw.rectangle([22, 6, 28, 12], fill=BLACK, outline=SILVER, width=1)
    draw.rounded_rectangle([12, 12, 38, 42], radius=2, fill=GREEN, outline=BLACK, width=1)
    draw.rectangle([12, 24, 38, 42], fill=DKGREEN)
    draw.rectangle([16, 16, 34, 26], fill=GREY)
    draw.ellipse([23, 20, 27, 24], fill=BLUE)
    draw.ellipse([22, 30, 28, 36], fill=GREY)

# --- 117. Electric Rotary Razor ---
def draw_electric_razor(draw):
    draw.polygon([(16, 18), (34, 18), (30, 42), (20, 42)], fill=GREY, outline=BLACK, width=1)
    draw.rectangle([20, 24, 30, 42], fill=DKGREY)
    draw.polygon([(14, 18), (36, 18), (32, 10), (18, 10)], fill=SILVER)
    draw.ellipse([18, 11, 22, 15], fill=BLACK)
    draw.ellipse([28, 11, 32, 15], fill=BLACK)
    draw.ellipse([23, 14, 27, 18], fill=BLACK)
    draw.ellipse([24, 34, 26, 36], fill=GREEN)

# --- 118. RF Bug Signal Detector ---
def draw_rf_signal_detector(draw):
    draw.rounded_rectangle([15, 16, 35, 44], radius=2, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([18, 20, 32, 24], fill=DKGREY)
    draw.line([19, 22, 23, 22], fill=GREEN, width=2)
    draw.line([24, 22, 28, 22], fill=YELLOW, width=2)
    draw.line([29, 22, 31, 22], fill=RED, width=2)
    draw.line([18, 16, 18, 4], fill=SILVER, width=2)
    draw.ellipse([17, 3, 19, 5], fill=BLACK)

# --- 119. Smart Pet Feeder ---
def draw_smart_pet_feeder(draw):
    draw.rounded_rectangle([15, 8, 35, 38], radius=2, fill=WHITE, outline=BLACK, width=1)
    draw.rectangle([15, 26, 35, 38], fill=GREY)
    draw.ellipse([23, 14, 27, 18], fill=BLACK)
    draw.ellipse([24, 15, 26, 17], fill=CYAN)
    draw.ellipse([12, 36, 38, 44], fill=SILVER, outline=BLACK, width=1)
    draw.ellipse([21, 38, 24, 41], fill=BROWN)
    draw.ellipse([26, 38, 29, 41], fill=BROWN)

# --- 120. Digital Soil Tester ---
def draw_digital_soil_tester(draw):
    draw.line([21, 26, 21, 46], fill=SILVER, width=2)
    draw.line([29, 26, 29, 46], fill=SILVER, width=2)
    draw.rounded_rectangle([14, 8, 36, 26], radius=3, fill=GREEN, outline=BLACK, width=1)
    draw.rectangle([18, 12, 32, 20], fill=BLACK)
    draw.line([21, 16, 29, 16], fill=GREEN, width=2)

# --- 121. Laser Distance Tape Measure ---
def draw_laser_tape_measure(draw):
    draw.rounded_rectangle([14, 10, 36, 42], radius=2, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([14, 25, 36, 42], fill=BLACK)
    draw.rectangle([17, 14, 33, 22], fill=GREY)
    draw.line([20, 18, 30, 18], fill=BLACK, width=1)
    draw.line([25, 10, 25, 4], fill=RED, width=1)
    draw.ellipse([23, 30, 27, 34], fill=RED)

# --- 122. Thermal Imaging Camera ---
def draw_thermal_camera(draw):
    draw.polygon([(14, 24), (24, 20), (28, 26), (18, 30)], fill=YELLOW, outline=BLACK, width=1)
    draw.polygon([(18, 30), (24, 26), (28, 42), (22, 42)], fill=BLACK)
    draw.rectangle([12, 14, 26, 23], fill=BLACK)
    draw.ellipse([14, 16, 24, 21], fill=RED)
    draw.rectangle([14, 18, 18, 21], fill=BLUE)
    draw.ellipse([28, 21, 31, 25], fill=SILVER)

# --- 123. Smart Key Tracker Finder ---
def draw_smart_key_finder(draw):
    draw.ellipse([10, 10, 40, 40], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([12, 12, 38, 38], fill=SILVER)
    draw.ellipse([21, 21, 29, 29], fill=BLUE)
    draw.ellipse([23, 14, 27, 18], fill=BLACK)

# --- 124. Wireless HDMI Transmitter ---
def draw_wireless_hdmi_transmitter(draw):
    draw.rounded_rectangle([15, 16, 35, 44], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([20, 8, 30, 16], fill=GOLD, outline=BLACK, width=1)
    draw.line([23, 8, 27, 8], fill=BLACK, width=1)
    draw.ellipse([24, 26, 26, 28], fill=CYAN)

# --- 125. HD Capture Card ---
def draw_hd_capture_card(draw):
    draw.rounded_rectangle([8, 16, 42, 34], radius=2, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([12, 16, 17, 19], fill=GOLD)
    draw.rectangle([33, 16, 38, 19], fill=GOLD)
    draw.ellipse([24, 24, 26, 26], fill=RED)

# --- 126. Digital Tuning Fork ---
def draw_digital_tuning_fork(draw):
    draw.line([21, 6, 21, 22], fill=SILVER, width=2)
    draw.line([29, 6, 29, 22], fill=SILVER, width=2)
    draw.line([21, 22, 29, 22], fill=SILVER, width=2)
    draw.line([25, 22, 25, 34], fill=SILVER, width=3)
    draw.rounded_rectangle([20, 32, 30, 44], radius=1, fill=BLACK, outline=GREY, width=1)
    draw.rectangle([22, 34, 28, 39], fill=GREEN)

# --- 127. Electronic Whistle ---
def draw_electronic_whistle(draw):
    draw.rounded_rectangle([16, 14, 34, 38], radius=3, fill=RED, outline=BLACK, width=1)
    draw.rectangle([16, 26, 34, 38], fill=DKRED)
    for y in range(18, 25, 3):
        draw.line([20, y, 30, y], fill=BLACK, width=1)
    draw.ellipse([23, 30, 27, 34], fill=YELLOW)
    draw.arc([22, 38, 28, 44], 0, 180, fill=SILVER, width=2)

# --- 128. Digital Breathalyzer ---
def draw_breathalyzer(draw):
    draw.rounded_rectangle([15, 14, 35, 42], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([18, 18, 32, 26], fill=BLACK)
    draw.line([21, 22, 29, 22], fill=RED, width=2)
    draw.rectangle([8, 10, 15, 13], fill=WHITE, outline=BLACK, width=1)

# --- 129. Smart Tower Air Purifier ---
def draw_smart_air_purifier(draw):
    draw.rounded_rectangle([15, 6, 35, 44], radius=3, fill=WHITE, outline=GREY, width=1)
    for y in range(16, 36, 4):
        draw.line([18, y, 32, y], fill=DKGREY, width=2)
    draw.ellipse([20, 8, 30, 12], fill=BLACK)
    draw.ellipse([22, 9, 28, 11], fill=CYAN)

# --- 130. Digital Lux Light Meter ---
def draw_digital_lux_meter(draw):
    draw.rounded_rectangle([10, 16, 32, 42], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([13, 20, 29, 28], fill=GREY)
    draw.line([16, 24, 26, 24], fill=BLACK, width=1)
    draw.line([21, 16, 38, 16], fill=BLACK, width=1)
    draw.line([38, 16, 38, 22], fill=BLACK, width=1)
    draw.ellipse([34, 22, 42, 30], fill=WHITE, outline=BLACK, width=1)
    draw.ellipse([36, 24, 40, 28], fill=SILVER)

# --- 131. Smart Body Fat Scale ---
def draw_smart_scale_body_fat(draw):
    draw.rounded_rectangle([8, 12, 42, 38], radius=3, fill=LIGHTBLUE, outline=BLACK, width=1)
    draw.rectangle([12, 16, 16, 34], fill=SILVER)
    draw.rectangle([34, 16, 38, 34], fill=SILVER)
    draw.rectangle([20, 14, 30, 18], fill=BLACK)
    draw.line([22, 16, 28, 16], fill=RED, width=1)

# --- 132. Microchip Tag Reader Wand ---
def draw_electronic_tag_reader(draw):
    draw.ellipse([14, 6, 36, 24], fill=BLUE, outline=BLACK, width=2)
    draw.ellipse([18, 10, 32, 20], fill=(255, 255, 255, 0))
    draw.line([25, 24, 25, 42], fill=GREY, width=4)
    draw.rounded_rectangle([21, 32, 29, 40], radius=1, fill=BLACK, outline=GREY, width=1)
    draw.ellipse([24, 35, 26, 37], fill=GREEN)

# --- 133. Solar Charge Controller ---
def draw_solar_charge_controller(draw):
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([14, 16, 36, 24], fill=BLACK)
    draw.rectangle([16, 17, 34, 21], fill=GREEN)
    draw.rectangle([12, 32, 38, 36], fill=BLACK)
    for x in range(15, 36, 4):
        draw.ellipse([x, 33, x+2, 35], fill=GOLD)

# --- 134. Credit Card Swiper Reader ---
def draw_magnetic_stripe_card_reader(draw):
    draw.rounded_rectangle([12, 16, 38, 36], radius=2, fill=GREY, outline=BLACK, width=1)
    draw.rectangle([23, 16, 27, 36], fill=BLACK)
    draw.ellipse([16, 20, 18, 22], fill=GREEN)
    draw.rectangle([21, 8, 25, 24], fill=BLUE, outline=BLACK, width=1)
    draw.line([21, 12, 25, 12], fill=BLACK, width=2)

# --- 135. LED Dot Matrix Panel ---
def draw_led_matrix_panel(draw):
    draw.rectangle([8, 8, 42, 42], fill=DKGREY, outline=BLACK, width=1)
    for y in range(11, 40, 4):
        for x in range(11, 40, 4):
            led_color = RED if (x in [15, 19, 23, 27, 31] and y in [15, 19, 23, 27, 31]) else BLACK
            draw.ellipse([x, y, x+2, y+2], fill=led_color)

# --- 136. Server Rack PDU Power Bar ---
def draw_power_distributor_pdu(draw):
    draw.rectangle([4, 22, 46, 28], fill=BLACK, outline=GREY, width=1)
    draw.rectangle([8, 23, 14, 27], fill=RED)
    for x in range(18, 44, 5):
        draw.rectangle([x, 23, x+3, 27], fill=DKGREY)

# --- 137. Network Ethernet Switch ---
def draw_network_switch(draw):
    draw.rounded_rectangle([6, 18, 44, 32], radius=1, fill=DKGREY, outline=BLACK, width=1)
    for x in range(10, 30, 4):
        draw.rectangle([x, 22, x+2, 25], fill=BLACK)
    for x in range(32, 42, 3):
        draw.ellipse([x, 24, x+1, 25], fill=GREEN)

# --- 138. Server Cabinet Patch Panel ---
def draw_patch_panel(draw):
    draw.rectangle([4, 18, 46, 32], fill=GREY, outline=BLACK, width=1)
    for x in range(8, 42, 4):
        draw.rectangle([x, 20, x+2, 23], fill=BLACK)
    draw.arc([10, 22, 18, 34], 0, 180, fill=BLUE, width=2)
    draw.arc([22, 22, 30, 34], 0, 180, fill=YELLOW, width=2)
    draw.arc([30, 22, 38, 34], 0, 180, fill=RED, width=2)

# --- 139. NAS Cloud Storage Server ---
def draw_nas_drive(draw):
    draw.rounded_rectangle([14, 8, 36, 42], radius=3, fill=BLACK, outline=SILVER, width=1)
    draw.rectangle([18, 12, 32, 24], fill=DKGREY)
    draw.line([18, 18, 32, 18], fill=BLACK, width=1)
    draw.ellipse([21, 30, 23, 32], fill=GREEN)
    draw.ellipse([27, 30, 29, 32], fill=CYAN)

# --- 140. Uninterruptible Power Supply (UPS) ---
def draw_uninterruptible_power_supply(draw):
    draw.rounded_rectangle([15, 8, 35, 42], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([15, 26, 35, 42], fill=BLACK)
    draw.rectangle([19, 14, 31, 20], fill=BLACK)
    draw.line([21, 17, 29, 17], fill=CYAN, width=1)
    draw.line([21, 21, 25, 21], fill=CYAN, width=1)

# --- 141. HDMI to VGA Converter Cord ---
def draw_vga_adapter(draw):
    draw.rectangle([8, 10, 14, 18], fill=GOLD, outline=BLACK, width=1)
    draw.line([14, 14, 26, 26], fill=BLACK, width=2)
    draw.rounded_rectangle([24, 24, 42, 40], radius=1, fill=BLUE, outline=BLACK, width=1)
    draw.rectangle([28, 28, 38, 36], fill=DKGREY)

# --- 142. Smart NFC Ring ---
def draw_smart_ring(draw):
    draw.polygon([(18, 30), (32, 30), (36, 44), (14, 44)], fill=BLACK)
    draw.ellipse([18, 12, 32, 26], fill=SILVER, outline=BLACK, width=1)
    draw.ellipse([21, 15, 29, 23], fill=(255, 255, 255, 0))
    draw.rectangle([23, 11, 27, 14], fill=CYAN)

# --- 143. Pocket LED Projector ---
def draw_pocket_led_projector(draw):
    draw.rounded_rectangle([12, 14, 38, 38], radius=3, fill=BLACK, outline=GREY, width=1)
    draw.ellipse([16, 18, 26, 28], fill=GREY)
    draw.ellipse([18, 20, 24, 26], fill=CYAN)
    for x in range(29, 36, 2):
        draw.line([x, 20, x, 30], fill=GREY, width=1)

# --- 144. GPS Dog Collar Tracker ---
def draw_smart_collar(draw):
    draw.arc([10, 12, 40, 42], 0, 180, fill=BROWN, width=3)
    draw.rounded_rectangle([18, 24, 32, 36], radius=2, fill=BLACK, outline=SILVER, width=1)
    draw.line([20, 30, 30, 30], fill=CYAN, width=2)

# --- 145. Digital Smart Pen ---
def draw_smart_pen(draw):
    draw.line([8, 38, 38, 8], fill=BLACK, width=4)
    draw.line([9, 37, 37, 9], fill=SILVER, width=2)
    draw.line([7, 39, 9, 41], fill=GOLD, width=3)
    draw.ellipse([13, 31, 15, 33], fill=BLUE)
    draw.line([34, 12, 36, 10], fill=GOLD, width=1)

# --- 146. USB Hand Warmer ---
def draw_pocket_hand_warmer(draw):
    draw.rounded_rectangle([14, 10, 36, 40], radius=6, fill=LIGHTBLUE, outline=BLACK, width=1)
    draw.rectangle([14, 25, 36, 40], fill=BLUE)
    draw.rectangle([21, 36, 29, 39], fill=BLACK)
    draw.ellipse([23, 20, 27, 24], fill=RED)

# --- 147. Audio DAC Digital Converter ---
def draw_analog_to_digital_converter(draw):
    draw.rounded_rectangle([10, 18, 40, 34], radius=2, fill=STEEL, outline=BLACK, width=1)
    draw.ellipse([15, 23, 19, 27], fill=RED, outline=GOLD, width=1)
    draw.ellipse([23, 23, 27, 27], fill=WHITE, outline=GOLD, width=1)
    draw.rectangle([31, 23, 35, 27], fill=BLACK)

# --- 148. Solar Panel Backpack ---
def draw_solar_backpack(draw):
    draw.rounded_rectangle([12, 8, 38, 42], radius=4, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([16, 12, 34, 28], fill=BLACK)
    draw.line([25, 12, 25, 28], fill=CYAN, width=1)
    draw.line([16, 20, 34, 20], fill=CYAN, width=1)

# --- 149. Electric Rechargeable Screwdriver ---
def draw_electric_screwdriver(draw):
    draw.polygon([(14, 24), (24, 20), (28, 26), (18, 30)], fill=BLUE, outline=BLACK, width=1)
    draw.polygon([(18, 30), (24, 26), (28, 40), (22, 40)], fill=DKGREY)
    draw.line([25, 20, 35, 20], fill=SILVER, width=3)
    draw.line([35, 20, 42, 20], fill=BLACK, width=2)
    draw.ellipse([24, 30, 26, 32], fill=RED)

# --- 150. Smart Vapor Diffuser ---
def draw_smart_diffuser(draw):
    draw.polygon([(20, 12), (30, 12), (36, 40), (14, 40)], fill=WHITE, outline=BLACK, width=1)
    draw.line([15, 34, 35, 34], fill=PURPLE, width=2)
    draw.ellipse([22, 6, 28, 10], fill=CYAN)
    draw.ellipse([20, 2, 25, 6], fill=CYAN)

# Compile drawing list (150 items total)
DRAWINGS = {
    "smartphone": draw_smartphone,
    "laptop": draw_laptop,
    "desktop_pc": draw_desktop_pc,
    "retro_television": draw_retro_television,
    "headphones": draw_headphones,
    "smartwatch": draw_smartwatch,
    "gaming_console": draw_gaming_console,
    "game_controller": draw_game_controller,
    "digital_camera": draw_digital_camera,
    "tablet": draw_tablet,
    "mechanical_keyboard": draw_mechanical_keyboard,
    "optical_mouse": draw_optical_mouse,
    "vr_headset": draw_vr_headset,
    "audio_speaker": draw_audio_speaker,
    "studio_microphone": draw_studio_microphone,
    "electronic_calculator": draw_electronic_calculator,
    "wifi_router": draw_wifi_router,
    "floppy_disk": draw_floppy_disk,
    "usb_flash_drive": draw_usb_flash_drive,
    "cd_player": draw_cd_player,
    "cassette_tape": draw_cassette_tape,
    "mp3_player": draw_mp3_player,
    "retro_radio": draw_retro_radio,
    "smart_speaker": draw_smart_speaker,
    "walkie_talkie": draw_walkie_talkie,
    "quadcopter_drone": draw_quadcopter_drone,
    "video_projector": draw_video_projector,
    "laser_printer": draw_laser_printer,
    "flatbed_scanner": draw_flatbed_scanner,
    "highdef_webcam": draw_webcam,
    "portable_power_bank": draw_portable_power_bank,
    "wall_charger": draw_wall_charger,
    "cpu_microchip": draw_cpu_microchip,
    "motherboard": draw_motherboard,
    "graphics_card": draw_graphics_card,
    "hard_disk_drive": draw_hard_disk_drive,
    "solid_state_drive": draw_solid_state_drive,
    "ram_memory_module": draw_ram_memory_module,
    "oscilloscope": draw_oscilloscope,
    "soldering_iron": draw_soldering_iron,
    "alkaline_battery": draw_alkaline_battery,
    "smart_led_bulb": draw_smart_led_bulb,
    "usb_desk_fan": draw_usb_desk_fan,
    "retro_arcade_cabinet": draw_retro_arcade_cabinet,
    "digital_wristwatch": draw_digital_wristwatch,
    "robot_vacuum": draw_robot_vacuum,
    "digital_camcorder": draw_digital_camcorder,
    "personal_walkman": draw_personal_walkman,
    "retro_game_handheld": draw_retro_game_handheld,
    "smart_thermostat": draw_smart_thermostat,
    
    # Items 51 to 100
    "crt_monitor": draw_crt_monitor,
    "plasma_tv": draw_plasma_tv,
    "pager": draw_pager,
    "satellite_dish": draw_satellite_dish,
    "e_reader": draw_e_reader,
    "pocket_gaming_pet": draw_pocket_gaming_pet,
    "synthesizer": draw_synthesizer,
    "laser_pointer": draw_laser_pointer,
    "barcode_scanner": draw_barcode_scanner,
    "dvd_player": draw_dvd_player,
    "digital_scale": draw_digital_scale,
    "metal_detector": draw_metal_detector,
    "laserdisc_player": draw_laserdisc_player,
    "e_drum_kit": draw_e_drum_kit,
    "hdmi_switch": draw_hdmi_switch,
    "smart_plug": draw_smart_plug,
    "fingerprint_scanner": draw_fingerprint_scanner,
    "gps_navigator": draw_gps_navigator,
    "pocket_translator": draw_pocket_translator,
    "smart_lock": draw_smart_lock,
    "pedometer": draw_pedometer,
    "audio_mixer": draw_audio_mixer,
    "karaoke_machine": draw_karaoke_machine,
    "hearing_aid": draw_hearing_aid,
    "laser_engraver": draw_laser_engraver,
    "geiger_counter": draw_geiger_counter,
    "e_guitar": draw_e_guitar,
    "modem": draw_modem,
    "rfid_reader": draw_rfid_reader,
    "digital_frame": draw_digital_frame,
    "magnifying_lamp": draw_magnifying_lamp,
    "car_key_fob": draw_car_key_fob,
    "electronic_level": draw_electronic_level,
    "hair_dryer": draw_hair_dryer,
    "label_maker": draw_label_maker,
    "smart_mirror": draw_smart_mirror,
    "strobe_light": draw_strobe_light,
    "electronic_drum_pad": draw_electronic_drum_pad,
    "solar_inverter": draw_solar_inverter,
    "cable_tester": draw_cable_tester,
    "intercom": draw_intercom,
    "battery_charger": draw_battery_charger,
    "weather_station": draw_weather_station,
    "dvd_rom_drive": draw_dvd_rom_drive,
    "soundbar": draw_soundbar,
    "vhs_rewinder": draw_vhs_rewinder,
    "e_microscope": draw_e_microscope,
    "e_skateboard": draw_e_skateboard,
    "gimbal_stabilizer": draw_gimbal_stabilizer,
    "smart_doorbell": draw_smart_doorbell,
    
    # Items 101 to 150
    "laser_printer_toner": draw_laser_printer_toner,
    "usb_hub": draw_usb_hub,
    "hdmi_splitter": draw_hdmi_splitter,
    "car_radar_detector": draw_car_radar_detector,
    "electronic_dictionary": draw_electronic_dictionary,
    "led_flashlight": draw_led_flashlight,
    "electric_toothbrush": draw_electric_toothbrush,
    "baby_monitor": draw_baby_monitor,
    "e_luggage_scale": draw_e_luggage_scale,
    "smart_water_leak_sensor": draw_smart_water_leak_sensor,
    "digital_magnifier": draw_digital_magnifier,
    "smart_smoke_detector": draw_smart_smoke_detector,
    "wireless_earbuds": draw_wireless_earbuds,
    "graphics_tablet": draw_graphics_tablet,
    "digital_air_pump": draw_digital_air_pump,
    "smart_irrigation_timer": draw_smart_irrigation_timer,
    "electric_razor": draw_electric_razor,
    "rf_signal_detector": draw_rf_signal_detector,
    "smart_pet_feeder": draw_smart_pet_feeder,
    "digital_soil_tester": draw_digital_soil_tester,
    "laser_tape_measure": draw_laser_tape_measure,
    "thermal_camera": draw_thermal_camera,
    "smart_key_finder": draw_smart_key_finder,
    "wireless_hdmi_transmitter": draw_wireless_hdmi_transmitter,
    "hd_capture_card": draw_hd_capture_card,
    "digital_tuning_fork": draw_digital_tuning_fork,
    "electronic_whistle": draw_electronic_whistle,
    "breathalyzer": draw_breathalyzer,
    "smart_air_purifier": draw_smart_air_purifier,
    "digital_lux_meter": draw_digital_lux_meter,
    "smart_scale_body_fat": draw_smart_scale_body_fat,
    "electronic_tag_reader": draw_electronic_tag_reader,
    "solar_charge_controller": draw_solar_charge_controller,
    "magnetic_stripe_card_reader": draw_magnetic_stripe_card_reader,
    "led_matrix_panel": draw_led_matrix_panel,
    "power_distributor_pdu": draw_power_distributor_pdu,
    "network_switch": draw_network_switch,
    "patch_panel": draw_patch_panel,
    "nas_drive": draw_nas_drive,
    "uninterruptible_power_supply": draw_uninterruptible_power_supply,
    "vga_adapter": draw_vga_adapter,
    "smart_ring": draw_smart_ring,
    "pocket_led_projector": draw_pocket_led_projector,
    "smart_collar": draw_smart_collar,
    "smart_pen": draw_smart_pen,
    "pocket_hand_warmer": draw_pocket_hand_warmer,
    "analog_to_digital_converter": draw_analog_to_digital_converter,
    "solar_backpack": draw_solar_backpack,
    "electric_screwdriver": draw_electric_screwdriver,
    "smart_diffuser": draw_smart_diffuser
}

if __name__ == "__main__":
    print(f"Generating 150 detailed electronics sprites inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating detailed electronics sprites!")

