import os
from PIL import Image, ImageDraw
import generate_electronics as ge

OUTPUT_DIR = "images/electronics"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_sprite(name, draw_func):
    base_img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(base_img)
    draw_func(draw)
    
    r, g, b, a = base_img.split()
    shadow_mask = a.point(lambda p: 255 if p > 128 else 0)
    
    combined = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    shadow_color = Image.new("RGBA", (50, 50), (30, 30, 35, 255))
    combined.paste(shadow_color, (2, 2), mask=shadow_mask)
    combined = Image.alpha_composite(combined, base_img)
    
    gloss = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_draw = ImageDraw.Draw(gloss)
    gloss_draw.polygon([(0, 0), (35, 0), (0, 35)], fill=(255, 255, 255, 45))
    gloss_draw.polygon([(50, 25), (50, 50), (25, 50)], fill=(0, 0, 0, 45))
    gloss_masked = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    gloss_masked.paste(gloss, (0, 0), mask=shadow_mask)
    combined = Image.alpha_composite(combined, gloss_masked)
    
    flat = Image.new("RGB", (50, 50), (255, 255, 255))
    comb_a = combined.split()[3].point(lambda p: 255 if p > 128 else 0)
    flat.paste(combined, mask=comb_a)
    
    q = flat.quantize(colors=8, method=Image.MEDIANCUT)
    final = q.convert("RGBA")
    
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
    print(f"Saved: {path}")

# Default colors to restore
ORIGINAL_COLORS = {
    "BLACK": ge.BLACK,
    "SILVER": ge.SILVER,
    "DKGREY": ge.DKGREY,
    "GREY": ge.GREY,
    "STEEL": ge.STEEL,
    "WHITE": ge.WHITE,
    "BROWN": ge.BROWN,
    "RED": ge.RED,
    "DKRED": ge.DKRED,
    "BLUE": ge.BLUE,
    "YELLOW": ge.YELLOW,
    "ORANGE": ge.ORANGE
}

def set_colors(**kwargs):
    for k, v in kwargs.items():
        setattr(ge, k, v)

def restore_colors():
    for k, v in ORIGINAL_COLORS.items():
        setattr(ge, k, v)

# Color palettes
GOLD = (212, 175, 55, 255)
ROSE_GOLD = (183, 110, 121, 255)
NAVY = (0, 0, 128, 255)
TEAL = (0, 128, 128, 255)
MINT = (152, 255, 152, 255)
PURPLE = (128, 0, 128, 255)
PINK = (255, 105, 180, 255)
CRIMSON = (220, 20, 60, 255)
NEON_GREEN = (57, 255, 20, 255)
WHITE_VAR = (245, 245, 245, 255)
GREY = ge.GREY
WHITE = ge.WHITE
BLACK = ge.BLACK
SILVER = ge.SILVER

variants = [
    # 1. Smartphone
    ("smartphone_gold", ge.draw_smartphone, {"BLACK": ROSE_GOLD, "SILVER": GOLD}),
    ("smartphone_navy", ge.draw_smartphone, {"BLACK": NAVY, "SILVER": TEAL}),
    
    # 2. Laptop
    ("laptop_rose", ge.draw_laptop, {"BLACK": ROSE_GOLD, "SILVER": WHITE_VAR}),
    ("laptop_teal", ge.draw_laptop, {"BLACK": TEAL, "SILVER": MINT}),
    
    # 3. Headphones
    ("headphones_mint", ge.draw_headphones, {"RED": MINT, "BLACK": WHITE_VAR}),
    ("headphones_purple", ge.draw_headphones, {"RED": PURPLE, "BLACK": NAVY}),
    
    # 4. Smartwatch
    ("smartwatch_pink", ge.draw_smartwatch, {"GREY": PINK, "BLACK": PURPLE}),
    ("smartwatch_gold", ge.draw_smartwatch, {"GREY": GOLD, "BLACK": NAVY}),
    
    # 5. Gaming Console
    ("gaming_console_neon", ge.draw_gaming_console, {"GREY": NEON_GREEN, "DKGREY": TEAL}),
    ("gaming_console_crimson", ge.draw_gaming_console, {"GREY": CRIMSON, "DKGREY": NAVY}),
    
    # 6. Game Controller
    ("game_controller_mint", ge.draw_game_controller, {"GREY": MINT, "DKGREY": TEAL}),
    ("game_controller_purple", ge.draw_game_controller, {"GREY": PURPLE, "DKGREY": PINK}),
    
    # 7. Digital Camera
    ("digital_camera_rose", ge.draw_digital_camera, {"SILVER": ROSE_GOLD, "STEEL": PINK}),
    ("digital_camera_navy", ge.draw_digital_camera, {"SILVER": NAVY, "STEEL": TEAL}),
    
    # 8. Tablet
    ("tablet_gold", ge.draw_tablet, {"BLACK": GOLD, "SILVER": ROSE_GOLD}),
    ("tablet_mint", ge.draw_tablet, {"BLACK": TEAL, "SILVER": MINT}),
    
    # 9. Mechanical Keyboard
    ("mechanical_keyboard_neon", ge.draw_mechanical_keyboard, {"GREY": NEON_GREEN, "DKGREY": TEAL}),
    ("mechanical_keyboard_pink", ge.draw_mechanical_keyboard, {"GREY": PINK, "DKGREY": PURPLE}),
    
    # 10. Optical Mouse
    ("optical_mouse_crimson", ge.draw_optical_mouse, {"GREY": CRIMSON, "DKGREY": NAVY}),
    ("optical_mouse_mint", ge.draw_optical_mouse, {"GREY": MINT, "DKGREY": TEAL}),
    
    # 11. VR Headset
    ("vr_headset_purple", ge.draw_vr_headset, {"WHITE": PURPLE, "GREY": PINK}),
    ("vr_headset_navy", ge.draw_vr_headset, {"WHITE": NAVY, "GREY": TEAL}),
    
    # 12. Audio Speaker
    ("audio_speaker_white", ge.draw_audio_speaker, {"BROWN": WHITE_VAR, "BLACK": GREY}),
    ("audio_speaker_neon", ge.draw_audio_speaker, {"BROWN": NEON_GREEN, "BLACK": TEAL}),
    
    # 13. Studio Microphone
    ("studio_microphone_gold", ge.draw_studio_microphone, {"SILVER": GOLD, "GREY": ROSE_GOLD}),
    ("studio_microphone_pink", ge.draw_studio_microphone, {"SILVER": PINK, "GREY": PURPLE}),
    
    # 14. Electronic Calculator
    ("electronic_calculator_mint", ge.draw_electronic_calculator, {"DKGREY": MINT, "ORANGE": PURPLE}),
    ("electronic_calculator_rose", ge.draw_electronic_calculator, {"DKGREY": ROSE_GOLD, "ORANGE": PINK}),
    
    # 15. Wi-Fi Router
    ("wifi_router_white", ge.draw_wifi_router, {"BLACK": WHITE_VAR, "GREY": SILVER}),
    ("wifi_router_purple", ge.draw_wifi_router, {"BLACK": PURPLE, "GREY": PINK}),
    
    # 16. Floppy Disk
    ("floppy_disk_neon", ge.draw_floppy_disk, {"BLUE": NEON_GREEN, "BLACK": TEAL}),
    ("floppy_disk_crimson", ge.draw_floppy_disk, {"BLUE": CRIMSON, "BLACK": NAVY}),
    
    # 17. USB Flash Drive
    ("usb_flash_drive_gold", ge.draw_usb_flash_drive, {"RED": GOLD, "DKRED": ROSE_GOLD}),
    ("usb_flash_drive_mint", ge.draw_usb_flash_drive, {"RED": MINT, "DKRED": TEAL}),
    
    # 18. CD Player
    ("cd_player_pink", ge.draw_cd_player, {"STEEL": PINK, "DKGREY": PURPLE}),
    ("cd_player_navy", ge.draw_cd_player, {"STEEL": NAVY, "DKGREY": TEAL}),
    
    # 19. Cassette Tape
    ("cassette_tape_neon", ge.draw_cassette_tape, {"DKGREY": NEON_GREEN, "WHITE": TEAL}),
    ("cassette_tape_gold", ge.draw_cassette_tape, {"DKGREY": GOLD, "WHITE": ROSE_GOLD}),
    
    # 20. MP3 Player
    ("mp3_player_mint", ge.draw_mp3_player, {"WHITE": MINT, "GREY": TEAL}),
    ("mp3_player_crimson", ge.draw_mp3_player, {"WHITE": CRIMSON, "GREY": NAVY}),
    
    # 21. Retro Radio
    ("retro_radio_rose", ge.draw_retro_radio, {"BROWN": ROSE_GOLD, "YELLOW": PINK}),
    ("retro_radio_teal", ge.draw_retro_radio, {"BROWN": TEAL, "YELLOW": MINT}),
    
    # 22. Smart Speaker
    ("smart_speaker_white", ge.draw_smart_speaker, {"DKGREY": WHITE_VAR, "BLACK": GREY}),
    ("smart_speaker_purple", ge.draw_smart_speaker, {"DKGREY": PURPLE, "BLACK": PINK}),
    
    # 23. Walkie Talkie
    ("walkie_talkie_mint", ge.draw_walkie_talkie, {"YELLOW": MINT, "ORANGE": TEAL}),
    ("walkie_talkie_navy", ge.draw_walkie_talkie, {"YELLOW": NAVY, "ORANGE": CRIMSON}),
    
    # 24. Quadcopter Drone
    ("quadcopter_drone_neon", ge.draw_quadcopter_drone, {"GREY": NEON_GREEN, "DKGREY": TEAL}),
    ("quadcopter_drone_gold", ge.draw_quadcopter_drone, {"GREY": GOLD, "DKGREY": ROSE_GOLD}),
    
    # 25. Video Projector
    ("video_projector_pink", ge.draw_video_projector, {"WHITE": PINK, "GREY": PURPLE}),
    ("video_projector_navy", ge.draw_video_projector, {"WHITE": NAVY, "GREY": TEAL}),
]

for name, func, colors in variants:
    set_colors(**colors)
    create_sprite(name, func)
    restore_colors()
