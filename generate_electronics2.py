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
    
    # --- Quantize to strictly <= 9 colors (colors=8 + 1 transparent) ---
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

# --- 151. Satellite Phone ---
def draw_sat_phone(draw):
    # Antenna
    draw.rectangle([13, 4, 16, 20], fill=DKGREY)
    # Body
    draw.rounded_rectangle([15, 14, 35, 46], radius=2, fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([17, 16, 33, 28], fill=GREEN) # screen
    draw.line([19, 18, 25, 18], fill=BLACK, width=1) # signal bars
    # Keypad
    for y in range(32, 44, 3):
        for x in range(18, 33, 5):
            draw.rectangle([x, y, x+3, y+2], fill=BLACK)

# --- 152. Car Dashcam ---
def draw_dashcam(draw):
    # Suction cup mount
    draw.ellipse([21, 4, 29, 8], fill=DKGREY)
    draw.line([25, 8, 25, 14], fill=BLACK, width=2)
    # Camera body
    draw.rounded_rectangle([12, 14, 38, 32], radius=2, fill=BLACK, outline=GREY, width=1)
    # Lens
    draw.ellipse([18, 16, 32, 30], fill=DKGREY, outline=SILVER, width=1)
    draw.ellipse([22, 20, 28, 26], fill=DKBLUE)
    draw.ellipse([24, 21, 26, 23], fill=CYAN)
    # Rec LED
    draw.ellipse([34, 16, 36, 18], fill=RED)

# --- 153. PoE Injector Block ---
def draw_poe_injector(draw):
    # Casing
    draw.rounded_rectangle([14, 12, 36, 38], radius=2, fill=BLACK, outline=DKGREY, width=1)
    # Port holes
    draw.rectangle([18, 30, 24, 35], fill=GREY)
    draw.rectangle([26, 30, 32, 35], fill=GREY)
    # Green LED
    draw.ellipse([24, 18, 26, 20], fill=GREEN)

# --- 154. Surge Protector Power Strip ---
def draw_power_strip(draw):
    # Body
    draw.rounded_rectangle([18, 6, 32, 44], radius=2, fill=WHITE, outline=GREY, width=1)
    # Sockets
    for y in range(14, 40, 6):
        draw.rectangle([22, y, 28, y+2], fill=GREY)
        draw.line([25, y+2, 25, y+4], fill=GREY, width=1)
    # Illuminated switch
    draw.rectangle([22, 8, 28, 11], fill=RED)

# --- 155. HDMI Cable ---
def draw_hdmi_cable(draw):
    # Cable connector
    draw.rounded_rectangle([16, 14, 34, 32], radius=1, fill=DKGREY, outline=BLACK, width=1)
    # Gold Tip
    draw.rectangle([18, 8, 32, 14], fill=GOLD, outline=BLACK, width=1)
    for x in range(20, 32, 3):
        draw.line([x, 10, x, 13], fill=BLACK, width=1)
    # Thick cable
    draw.line([25, 32, 25, 46], fill=BLACK, width=4)

# --- 156. RF Wireless Remote ---
def draw_rf_remote(draw):
    # Slim remote body
    draw.rounded_rectangle([16, 8, 34, 44], radius=4, fill=BLACK, outline=GREY, width=1)
    # Buttons
    draw.ellipse([23, 11, 27, 15], fill=RED) # Power button
    for y in range(18, 38, 4):
        for x in range(20, 32, 4):
            draw.rectangle([x, y, x+2, y+2], fill=GREY)
    # Blue LED
    draw.ellipse([20, 12, 21, 13], fill=BLUE)

# --- 157. Smart Thermostat Valve ---
def draw_smart_thermostat_valve(draw):
    # Base metallic collar
    draw.rectangle([18, 38, 32, 44], fill=SILVER, outline=BLACK, width=1)
    # Cylindrical valve body
    draw.rounded_rectangle([14, 10, 36, 38], radius=2, fill=WHITE, outline=GREY, width=1)
    # Display screen
    draw.ellipse([20, 18, 30, 28], fill=BLACK)
    # Numbers "21"
    draw.line([23, 21, 25, 21], fill=CYAN, width=1)
    draw.line([25, 21, 23, 25], fill=CYAN, width=1)
    draw.line([27, 21, 27, 25], fill=CYAN, width=1)

# --- 158. Digital Battery Tester ---
def draw_battery_tester(draw):
    # Housing
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    # Battery under test
    draw.rounded_rectangle([14, 28, 28, 34], radius=1, fill=ORANGE)
    draw.rectangle([28, 30, 30, 32], fill=GOLD)
    # Test slider arm
    draw.rectangle([30, 22, 36, 36], fill=RED)
    # LED scale screen
    draw.rectangle([14, 16, 26, 22], fill=DKGREY)
    draw.line([16, 19, 24, 19], fill=GREEN, width=2)

# --- 159. Wireless Charging Pad ---
def draw_wireless_charger(draw):
    # Charging pad
    draw.ellipse([10, 14, 40, 38], fill=DKGREY, outline=SILVER, width=1)
    # Phone laying on top
    draw.rectangle([16, 12, 34, 34], fill=BLACK, outline=GREY, width=1)
    # Charging icon
    draw.polygon([(25, 18), (22, 24), (25, 24), (24, 30), (28, 22), (25, 22)], fill=GREEN)

# --- 160. Sound Level Meter ---
def draw_sound_level_meter(draw):
    # Microphone windscreen
    draw.ellipse([21, 4, 29, 12], fill=DKGREY)
    # Main body
    draw.rounded_rectangle([15, 12, 35, 46], radius=2, fill=ORANGE, outline=BLACK, width=1)
    draw.rectangle([15, 26, 35, 46], fill=BLACK)
    # Blue display screen
    draw.rectangle([18, 16, 32, 24], fill=CYAN)
    draw.line([20, 20, 30, 20], fill=BLACK, width=1)

# --- 161. Digital Vernier Caliper ---
def draw_digital_caliper(draw):
    # Metallic scale bar
    draw.line([6, 24, 44, 24], fill=SILVER, width=3)
    # Caliper Jaws
    draw.line([8, 14, 8, 34], fill=SILVER, width=2)
    # Sliding module
    draw.rectangle([18, 18, 32, 30], fill=BLACK, outline=GREY, width=1)
    draw.rectangle([21, 21, 29, 27], fill=LIGHTBLUE)
    draw.line([23, 24, 27, 24], fill=BLACK, width=1)

# --- 162. Electronic Stethoscope ---
def draw_e_stethoscope(draw):
    # Stethoscope chestpiece
    draw.ellipse([20, 34, 30, 42], fill=SILVER, outline=BLACK, width=1)
    # Tubing
    draw.line([25, 34, 25, 24], fill=BLACK, width=2)
    # Pod
    draw.rounded_rectangle([16, 10, 34, 24], radius=2, fill=BLACK, outline=SILVER, width=1)
    # Circular screen showing pulse wave
    draw.ellipse([20, 12, 30, 22], fill=DKBLUE)
    draw.line([22, 17, 24, 17], fill=CYAN, width=1)
    draw.line([24, 17, 26, 14], fill=CYAN, width=1)
    draw.line([26, 14, 28, 20], fill=CYAN, width=1)

# --- 163. Fingertip Pulse Oximeter ---
def draw_pulse_oximeter(draw):
    # Finger clamp body
    draw.rounded_rectangle([14, 14, 36, 36], radius=2, fill=WHITE, outline=GREY, width=1)
    draw.rectangle([14, 25, 36, 36], fill=GREY)
    # Red display
    draw.rectangle([18, 18, 32, 23], fill=BLACK)
    draw.line([20, 20, 24, 20], fill=RED, width=1)
    draw.line([26, 20, 30, 20], fill=RED, width=1)

# --- 164. UV Sanitizer Box ---
def draw_uv_sanitizer(draw):
    # Box
    draw.rounded_rectangle([8, 12, 42, 38], radius=3, fill=WHITE, outline=GREY, width=1)
    # Glass window
    draw.rectangle([12, 16, 38, 34], fill=PURPLE)
    # UV light bulbs glow
    draw.line([14, 18, 36, 18], fill=CYAN, width=1)
    draw.line([14, 32, 36, 32], fill=CYAN, width=1)
    # Phone silhouette
    draw.rectangle([18, 22, 32, 28], fill=BLACK)

# --- 165. Retro Vinyl Turntable ---
def draw_turntable(draw):
    # Wooden case
    draw.rounded_rectangle([8, 10, 42, 40], radius=2, fill=BROWN, outline=BLACK, width=1)
    # Platter and record
    draw.ellipse([11, 14, 33, 36], fill=BLACK)
    draw.ellipse([19, 22, 25, 28], fill=RED)
    # Tone arm
    draw.line([38, 14, 38, 24], fill=SILVER, width=2)
    draw.line([38, 24, 28, 30], fill=SILVER, width=1)

# --- 166. Digital Wall Stud Finder ---
def draw_stud_finder(draw):
    # Yellow plastic body
    draw.rounded_rectangle([16, 12, 34, 44], radius=3, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([16, 28, 34, 44], fill=BLACK)
    # LCD Display
    draw.rectangle([19, 16, 31, 24], fill=DKGREY)
    # Arrow indicators
    draw.polygon([(25, 17), (22, 21), (28, 21)], fill=GREEN)
    # Red LED
    draw.ellipse([24, 26, 26, 28], fill=RED)

# --- 167. Smart Door Window Sensor ---
def draw_smart_door_sensor(draw):
    # Large block
    draw.rounded_rectangle([10, 10, 24, 40], radius=2, fill=WHITE, outline=GREY, width=1)
    # Small block
    draw.rounded_rectangle([28, 10, 38, 40], radius=2, fill=WHITE, outline=GREY, width=1)
    # Status LED
    draw.ellipse([16, 14, 18, 16], fill=GREEN)

# --- 168. Digital Manometer ---
def draw_digital_manometer(draw):
    # Nozzles
    draw.rectangle([20, 6, 22, 10], fill=SILVER)
    draw.rectangle([28, 6, 30, 10], fill=SILVER)
    # Main body
    draw.rounded_rectangle([14, 10, 36, 44], radius=2, fill=GREY, outline=BLACK, width=1)
    # Blue display screen
    draw.rectangle([17, 16, 33, 26], fill=BLUE)
    draw.line([20, 21, 30, 21], fill=WHITE, width=1)

# --- 169. Mini Solar Panel Module ---
def draw_solar_panel_module(draw):
    # Aluminum frame
    draw.rectangle([6, 10, 44, 40], fill=SILVER, outline=BLACK, width=1)
    # Blue solar grid
    draw.rectangle([8, 12, 42, 38], fill=DKBLUE)
    # Grid lines
    for x in range(13, 40, 5):
        draw.line([x, 12, x, 38], fill=WHITE, width=1)
    for y in range(18, 38, 6):
        draw.line([8, y, 42, y], fill=WHITE, width=1)

# --- 170. LED Plant Grow Light ---
def draw_led_grow_light(draw):
    # Light fixture housing
    draw.rectangle([8, 8, 42, 18], fill=GREY, outline=BLACK, width=1)
    # Glow light beams
    draw.polygon([(10, 18), (2, 44), (48, 44), (40, 18)], fill=(210, 120, 210, 80))
    # Matrix of LED chips
    for x in range(12, 40, 6):
        draw.rectangle([x, 12, x+2, 14], fill=PURPLE)
        draw.rectangle([x+3, 12, x+5, 14], fill=RED)

# --- 171. OBD2 Car Diagnostic Scanner ---
def draw_obd2_scanner(draw):
    # Orange diagnostic handset
    draw.rounded_rectangle([15, 10, 35, 38], radius=2, fill=ORANGE, outline=BLACK, width=1)
    # Screen
    draw.rectangle([18, 14, 32, 24], fill=GREEN)
    draw.line([20, 17, 28, 17], fill=BLACK, width=1)
    draw.line([20, 20, 30, 20], fill=BLACK, width=1)
    # Cable out of bottom
    draw.line([25, 38, 25, 46], fill=BLACK, width=2)
    # Connector
    draw.rectangle([21, 42, 29, 46], fill=DKGREY)

# --- 172. Robotic Window Cleaner ---
def draw_smart_window_cleaner(draw):
    # Square robot body
    draw.rounded_rectangle([10, 10, 40, 40], radius=3, fill=WHITE, outline=GREY, width=1)
    # Center handle
    draw.rounded_rectangle([18, 18, 32, 32], radius=1, fill=DKGREY)
    # Status ring
    draw.ellipse([21, 21, 29, 29], fill=CYAN)
    draw.ellipse([23, 23, 27, 27], fill=BLUE)

# --- 173. Digital Multimeter ---
def draw_digital_multimeter(draw):
    # Orange protective shell
    draw.rounded_rectangle([14, 10, 36, 42], radius=2, fill=ORANGE, outline=BLACK, width=1)
    # Screen
    draw.rectangle([17, 14, 33, 22], fill=DKGREY)
    draw.line([20, 18, 28, 18], fill=GREEN, width=1)
    # Rotary switch dial
    draw.ellipse([21, 26, 29, 34], fill=BLACK)
    draw.line([25, 26, 25, 30], fill=WHITE, width=2)
    # Test leads
    draw.line([20, 40, 10, 46], fill=RED, width=1)
    draw.line([30, 40, 40, 46], fill=BLACK, width=1)

# --- 174. RC Flight Drone Controller ---
def draw_drone_controller(draw):
    # Transmitter box
    draw.rounded_rectangle([12, 16, 38, 44], radius=2, fill=BLACK, outline=GREY, width=1)
    # Gimbals
    draw.ellipse([16, 24, 22, 30], fill=DKGREY)
    draw.line([19, 24, 19, 30], fill=SILVER, width=1)
    draw.ellipse([28, 24, 34, 30], fill=DKGREY)
    draw.line([31, 24, 31, 30], fill=SILVER, width=1)
    # Smartphone holder with phone screen
    draw.rectangle([14, 6, 36, 16], fill=LIGHTBLUE, outline=SILVER, width=1)
    # Antenna
    draw.line([25, 16, 25, 2], fill=SILVER, width=2)

# --- 175. LED Strip Light Reel ---
def draw_led_strip_lights(draw):
    # Outer circular spool
    draw.ellipse([8, 8, 42, 42], fill=GREY, outline=BLACK, width=1)
    # Inner wound roll
    draw.ellipse([14, 14, 36, 36], fill=BLACK)
    # Glowing color chips
    draw.rectangle([18, 18, 20, 20], fill=RED)
    draw.rectangle([25, 16, 27, 18], fill=GREEN)
    draw.rectangle([30, 22, 32, 24], fill=BLUE)
    draw.rectangle([22, 30, 24, 32], fill=YELLOW)

# --- 176. Multi Card Reader Hub ---
def draw_card_reader_hub(draw):
    # Hub block
    draw.rounded_rectangle([12, 16, 38, 36], radius=2, fill=SILVER, outline=GREY, width=1)
    # Slots
    draw.rectangle([16, 20, 34, 22], fill=BLACK) # SD slot
    draw.rectangle([18, 26, 32, 28], fill=BLACK) # MicroSD slot
    # Partially inserted blue SD card
    draw.rectangle([18, 18, 28, 21], fill=BLUE)
    # Blue power LED
    draw.ellipse([32, 31, 34, 33], fill=CYAN)

# --- 177. Electronic Key Safe Cabinet ---
def draw_smart_key_cabinet(draw):
    # Wall safe box
    draw.rounded_rectangle([12, 10, 38, 42], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Keypad lock panel
    draw.rectangle([18, 16, 32, 26], fill=BLACK)
    draw.rectangle([22, 18, 28, 20], fill=GREEN) # glowing status light
    for y in range(22, 26, 2):
        for x in range(20, 31, 3):
            draw.rectangle([x, y, x+1, y+1], fill=GREY)
    # Safe handle knob
    draw.ellipse([23, 31, 27, 35], fill=SILVER)

# --- 178. Handheld Digital Stopwatch ---
def draw_digital_stopwatch(draw):
    # Top buttons
    draw.rectangle([18, 6, 22, 10], fill=GREY)
    draw.rectangle([28, 6, 32, 10], fill=GREY)
    # Crown trigger button
    draw.rectangle([23, 5, 27, 9], fill=RED)
    # Oval body
    draw.ellipse([12, 10, 38, 44], fill=BLACK, outline=GREY, width=1)
    # LCD Display
    draw.rounded_rectangle([16, 18, 34, 30], radius=1, fill=GREY)
    # Digital numbers representation
    draw.line([19, 24, 31, 24], fill=BLACK, width=2)

# --- 179. Combustible Gas Leak Detector ---
def draw_smart_gas_detector(draw):
    # Wall alarm panel
    draw.rounded_rectangle([14, 12, 36, 40], radius=3, fill=WHITE, outline=GREY, width=1)
    # Circular gas sensing vents grill
    draw.ellipse([20, 24, 30, 34], fill=DKGREY)
    for i in range(22, 30, 2):
        draw.line([i, 26, i, 32], fill=BLACK, width=1)
    # Red alarm flashing light
    draw.ellipse([23, 16, 27, 20], fill=RED)

# --- 180. Mini Desktop PC Console ---
def draw_mini_pc(draw):
    # Sleek square mini computer
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    # Side ventilation grid
    for x in range(12, 38, 4):
        draw.line([x, 15, x, 18], fill=DKGREY, width=1)
    # Front USB Ports and power button
    draw.rectangle([14, 28, 20, 30], fill=SILVER)
    draw.rectangle([22, 28, 28, 30], fill=SILVER)
    draw.ellipse([32, 27, 35, 30], fill=BLUE)

# --- 181. White USB to Lightning Cable ---
def draw_lightning_cable(draw):
    # Slim connector collar
    draw.rectangle([21, 16, 29, 32], fill=WHITE, outline=GREY, width=1)
    # Lightning tip
    draw.rectangle([22, 8, 28, 16], fill=SILVER, outline=GREY, width=1)
    # Gold contacts
    for x in range(23, 28, 2):
        draw.line([x, 9, x, 11], fill=GOLD, width=1)
    # White cable
    draw.line([25, 32, 25, 46], fill=WHITE, width=2)

# --- 182. Braided USB-C Cable ---
def draw_usb_c_cable(draw):
    # Metal connector casing
    draw.rectangle([20, 16, 30, 32], fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([20, 20, 30, 28], fill=SILVER)
    # USB-C oval tip
    draw.rounded_rectangle([22, 8, 28, 16], radius=1, fill=SILVER, outline=BLACK, width=1)
    # Braided black cable cord
    draw.line([25, 32, 25, 46], fill=BLACK, width=3)

# --- 183. RF Signal Jammer ---
def draw_rf_jammer(draw):
    # Military-style chassis
    draw.rounded_rectangle([14, 18, 36, 44], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Multiple antennas
    for x in [18, 23, 27, 32]:
        draw.line([x, 18, x, 4], fill=BLACK, width=2)
    # Controls LEDs
    draw.ellipse([18, 24, 20, 26], fill=RED)
    draw.ellipse([23, 24, 25, 26], fill=GREEN)

# --- 184. POS Credit Card Terminal ---
def draw_pos_terminal(draw):
    # POS Handset casing
    draw.rounded_rectangle([14, 8, 36, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    # LCD screen showing swipe prompt
    draw.rectangle([18, 12, 32, 22], fill=GREEN)
    draw.line([20, 17, 30, 17], fill=BLACK, width=1)
    # Numeric Keypad buttons
    for y in range(28, 40, 3):
        for x in range(18, 33, 5):
            draw.rectangle([x, y, x+3, y+2], fill=DKGREY)
    # Swiping credit card
    draw.line([34, 14, 34, 38], fill=BLUE, width=2)
    draw.rectangle([33, 20, 35, 28], fill=RED)

# --- 185. Electronic Lab Pipette ---
def draw_e_pipette(draw):
    # Handle & screen
    draw.rounded_rectangle([21, 6, 29, 32], radius=1, fill=BLUE, outline=BLACK, width=1)
    draw.rectangle([23, 12, 27, 18], fill=CYAN)
    # Adjustment plunger button at top
    draw.ellipse([23, 4, 27, 6], fill=WHITE)
    # Slender nozzle shaft
    draw.line([25, 32, 25, 42], fill=GREY, width=2)
    # Plastic tip
    draw.polygon([(24, 42), (26, 42), (25, 46)], fill=LIGHTBLUE)

# --- 186. Smart Travel Mug ---
def draw_smart_mug(draw):
    # Travel mug
    draw.rounded_rectangle([16, 12, 34, 40], radius=4, fill=BLACK, outline=GREY, width=1)
    # Digital temperature base glow
    draw.rectangle([16, 34, 34, 40], fill=DKGREY)
    draw.line([20, 37, 24, 37], fill=CYAN, width=1)
    draw.line([26, 37, 30, 37], fill=CYAN, width=1)
    # Coaster pad
    draw.ellipse([12, 38, 38, 44], fill=DKGREY)

# --- 187. Smart Suitcase Biometric Lock ---
def draw_smart_luggage(draw):
    # Luggage fabric background
    draw.rectangle([4, 4, 46, 46], fill=DKGREY)
    # Zipper lock module
    draw.rounded_rectangle([12, 14, 38, 36], radius=2, fill=BLACK, outline=GREY, width=1)
    # Glowing fingerprint ring scanner
    draw.ellipse([20, 20, 30, 30], fill=CYAN)
    draw.ellipse([22, 22, 28, 28], fill=BLUE)
    # Zip pull tabs locked
    draw.rectangle([14, 18, 16, 26], fill=SILVER)
    draw.rectangle([34, 18, 36, 26], fill=SILVER)

# --- 188. Wind Speed Anemometer ---
def draw_digital_anemometer(draw):
    # Handheld body
    draw.rounded_rectangle([18, 20, 32, 44], radius=2, fill=GREY, outline=BLACK, width=1)
    # Screen
    draw.rectangle([21, 24, 29, 32], fill=LIGHTBLUE)
    draw.line([23, 28, 27, 28], fill=BLACK, width=1)
    # Impeller head spinner cups
    draw.line([25, 20, 25, 12], fill=BLACK, width=2)
    draw.line([17, 12, 33, 12], fill=BLACK, width=2)
    draw.ellipse([14, 9, 18, 15], fill=DKGREY)
    draw.ellipse([32, 9, 36, 15], fill=DKGREY)
    draw.ellipse([23, 6, 27, 12], fill=DKGREY)

# --- 189. Smart Fridge Panel ---
def draw_smart_fridge_panel(draw):
    # Steel door
    draw.rectangle([6, 6, 44, 44], fill=SILVER)
    # Inside handle outline
    draw.line([8, 6, 8, 44], fill=GREY, width=2)
    # Integrated tablet screen
    draw.rectangle([16, 10, 38, 40], fill=BLACK, outline=GREY, width=1)
    # UI Checklist boxes
    draw.rectangle([18, 14, 36, 36], fill=WHITE)
    draw.rectangle([20, 18, 23, 21], fill=BLUE)
    draw.rectangle([20, 24, 23, 27], fill=GREY)
    draw.rectangle([20, 30, 23, 33], fill=BLUE)

# --- 190. Sugar Brix Refractometer ---
def draw_digital_refractometer(draw):
    # Prism sample cup
    draw.polygon([(22, 14), (28, 14), (25, 8)], fill=SILVER, outline=BLACK)
    # Refractometer body
    draw.rounded_rectangle([16, 14, 34, 44], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Screen
    draw.rectangle([19, 22, 31, 30], fill=GREEN)
    draw.line([22, 26, 28, 26], fill=BLACK, width=1)

# --- 191. LED Ring Light Studio ---
def draw_led_ring_light(draw):
    # Ring light
    draw.ellipse([12, 6, 38, 32], fill=WHITE, outline=GREY, width=4)
    # Center smartphone holder
    draw.rectangle([22, 16, 28, 24], fill=BLACK)
    # Tripod stand
    draw.line([25, 32, 25, 46], fill=DKGREY, width=2)
    draw.line([25, 42, 16, 46], fill=BLACK, width=2)
    draw.line([25, 42, 34, 46], fill=BLACK, width=2)

# --- 192. Dual Hard Drive Dock ---
def draw_hard_drive_dock(draw):
    # Dock base
    draw.rounded_rectangle([10, 26, 40, 42], radius=2, fill=BLACK, outline=GREY, width=1)
    # Hard Drive 1
    draw.rounded_rectangle([14, 10, 24, 28], radius=1, fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([14, 22, 24, 28], fill=BLACK)
    # Hard Drive 2
    draw.rounded_rectangle([26, 10, 36, 28], radius=1, fill=SILVER, outline=BLACK, width=1)
    draw.rectangle([26, 22, 36, 28], fill=BLACK)
    # Indicator LEDs
    draw.ellipse([16, 34, 18, 36], fill=BLUE)
    draw.ellipse([20, 34, 22, 36], fill=BLUE)

# --- 193. Wall Smart Switch Panel ---
def draw_smart_switch(draw):
    # Wall plate
    draw.rounded_rectangle([10, 10, 40, 40], radius=3, fill=WHITE, outline=GREY, width=1)
    # Smart button switch ring
    draw.ellipse([18, 18, 32, 32], fill=GREY, outline=CYAN, width=2)
    draw.ellipse([21, 21, 29, 29], fill=WHITE)

# --- 194. Thermal Receipt Printer ---
def draw_thermal_receipt_printer(draw):
    # Printer cube body
    draw.rounded_rectangle([12, 18, 38, 42], radius=2, fill=BLACK, outline=GREY, width=1)
    # Output paper slot
    draw.rectangle([14, 22, 36, 24], fill=DKGREY)
    # Receipt paper emerging
    draw.rectangle([16, 10, 34, 22], fill=WHITE, outline=GREY, width=1)
    # Barcode/Text lines printed
    draw.line([18, 14, 32, 14], fill=BLACK, width=1)
    draw.line([18, 18, 28, 18], fill=BLACK, width=1)

# --- 195. Digital Water Flow Meter ---
def draw_smart_water_meter(draw):
    # Pipe fitting base
    draw.line([6, 25, 44, 25], fill=GOLD, width=6)
    # Meter attachment housing
    draw.ellipse([14, 12, 36, 34], fill=GREY, outline=BLACK, width=1)
    # LCD display screen
    draw.rounded_rectangle([18, 16, 32, 26], radius=1, fill=GREEN)
    draw.line([20, 21, 30, 21], fill=BLACK, width=1)

# --- 196. MicroSD Memory Card ---
def draw_micro_sd_card(draw):
    # Card casing
    draw.rectangle([14, 12, 36, 38], fill=BLACK, outline=DKGREY, width=1)
    # Red stripe branding
    draw.rectangle([14, 16, 36, 20], fill=RED)
    # Gold contacts fingers
    for x in range(16, 36, 4):
        draw.line([x, 12, x, 15], fill=GOLD, width=1)

# --- 197. Secure Digital SD Card ---
def draw_sd_card(draw):
    # Blue SD Card body
    draw.polygon([(14, 12), (32, 12), (36, 16), (36, 38), (14, 38)], fill=BLUE, outline=BLACK, width=1)
    # Write protect tab
    draw.rectangle([14, 20, 16, 24], fill=YELLOW)
    # Label stripe
    draw.rectangle([18, 16, 32, 34], fill=WHITE)
    draw.line([20, 20, 30, 20], fill=BLUE, width=2)

# --- 198. Bluetooth Audio Transceiver ---
def draw_audio_transceiver(draw):
    # Circular puck box
    draw.ellipse([12, 12, 38, 38], fill=BLACK, outline=GREY, width=1)
    # Glowing pairing ring LED
    draw.ellipse([18, 18, 32, 32], fill=CYAN, width=2)
    # Aux audio jack out
    draw.line([25, 38, 25, 46], fill=GREY, width=3)
    draw.rectangle([23, 42, 27, 46], fill=GOLD)

# --- 199. Smart Sprinkler Controller ---
def draw_smart_sprinkler_controller(draw):
    # Wall sprinkler box panel
    draw.rounded_rectangle([12, 10, 38, 42], radius=2, fill=WHITE, outline=GREY, width=1)
    # LCD Display showing watering zones
    draw.rectangle([16, 14, 34, 28], fill=DKGREY)
    # Active zones indicator
    draw.rectangle([18, 16, 23, 26], fill=GREEN)
    draw.rectangle([27, 16, 32, 26], fill=GREEN)
    # Dial selector wheel
    draw.ellipse([22, 32, 28, 38], fill=GREY)

# --- 200. Electric Fence Energizer ---
def draw_electric_fence_energizer(draw):
    # Yellow warning power unit
    draw.rounded_rectangle([14, 12, 36, 42], radius=3, fill=YELLOW, outline=BLACK, width=1)
    # High-voltage terminals
    draw.ellipse([18, 36, 22, 40], fill=RED)
    draw.ellipse([28, 36, 32, 40], fill=BLACK)
    # Red Warning lightning bolt symbol
    draw.polygon([(25, 16), (21, 24), (25, 24), (23, 32), (29, 22), (25, 22)], fill=RED)

DRAWINGS = {
    # Items 151 to 200
    "sat_phone": draw_sat_phone,
    "dashcam": draw_dashcam,
    "poe_injector": draw_poe_injector,
    "power_strip": draw_power_strip,
    "hdmi_cable": draw_hdmi_cable,
    "rf_remote": draw_rf_remote,
    "smart_thermostat_valve": draw_smart_thermostat_valve,
    "battery_tester": draw_battery_tester,
    "wireless_charger": draw_wireless_charger,
    "sound_level_meter": draw_sound_level_meter,
    "digital_caliper": draw_digital_caliper,
    "e_stethoscope": draw_e_stethoscope,
    "pulse_oximeter": draw_pulse_oximeter,
    "uv_sanitizer": draw_uv_sanitizer,
    "turntable": draw_turntable,
    "stud_finder": draw_stud_finder,
    "smart_door_sensor": draw_smart_door_sensor,
    "digital_manometer": draw_digital_manometer,
    "solar_panel_module": draw_solar_panel_module,
    "led_grow_light": draw_led_grow_light,
    "obd2_scanner": draw_obd2_scanner,
    "smart_window_cleaner": draw_smart_window_cleaner,
    "digital_multimeter": draw_digital_multimeter,
    "drone_controller": draw_drone_controller,
    "led_strip_lights": draw_led_strip_lights,
    "card_reader_hub": draw_card_reader_hub,
    "smart_key_cabinet": draw_smart_key_cabinet,
    "digital_stopwatch": draw_digital_stopwatch,
    "smart_gas_detector": draw_smart_gas_detector,
    "mini_pc": draw_mini_pc,
    "lightning_cable": draw_lightning_cable,
    "usb_c_cable": draw_usb_c_cable,
    "rf_jammer": draw_rf_jammer,
    "pos_terminal": draw_pos_terminal,
    "e_pipette": draw_e_pipette,
    "smart_mug": draw_smart_mug,
    "smart_luggage": draw_smart_luggage,
    "digital_anemometer": draw_digital_anemometer,
    "smart_fridge_panel": draw_smart_fridge_panel,
    "digital_refractometer": draw_digital_refractometer,
    "led_ring_light": draw_led_ring_light,
    "hard_drive_dock": draw_hard_drive_dock,
    "smart_switch": draw_smart_switch,
    "thermal_receipt_printer": draw_thermal_receipt_printer,
    "smart_water_meter": draw_smart_water_meter,
    "micro_sd_card": draw_micro_sd_card,
    "sd_card": draw_sd_card,
    "audio_transceiver": draw_audio_transceiver,
    "smart_sprinkler_controller": draw_smart_sprinkler_controller,
    "electric_fence_energizer": draw_electric_fence_energizer
}

if __name__ == "__main__":
    print(f"Generating 50 new detailed electronics sprites inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating 50 new detailed electronics sprites!")
