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
BEIGE     = (245, 222, 179, 255)

# --- 201. Smart Water Heater Panel ---
def draw_water_heater_panel(draw):
    draw.rounded_rectangle([12, 10, 38, 42], radius=3, fill=WHITE, outline=GREY, width=1)
    draw.rectangle([16, 14, 34, 26], fill=BLACK)
    # temperature "120F"
    draw.line([20, 18, 22, 18], fill=CYAN, width=1)
    draw.line([25, 18, 27, 18], fill=CYAN, width=1)
    # Dial
    draw.ellipse([21, 30, 29, 38], fill=GREY, outline=BLACK, width=1)

# --- 202. E-Bike Display Console ---
def draw_e_bike_display(draw):
    # Handlebar brackets
    draw.line([10, 36, 40, 36], fill=DKGREY, width=3)
    # Console box
    draw.rounded_rectangle([12, 12, 38, 32], radius=2, fill=BLACK, outline=GREY, width=1)
    # Screen displaying speed "25"
    draw.rectangle([15, 15, 35, 29], fill=DKBLUE)
    draw.line([20, 20, 24, 20], fill=GREEN, width=2)
    draw.line([27, 20, 31, 20], fill=GREEN, width=2)

# --- 203. FIDO Security Key ---
def draw_fido_key(draw):
    # USB plug
    draw.rectangle([21, 6, 29, 14], fill=SILVER, outline=BLACK)
    for x in range(23, 29, 2):
        draw.line([x, 7, x, 12], fill=GOLD, width=1)
    # Body keyhole
    draw.rounded_rectangle([15, 14, 35, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    # Fingerprint scanner circle
    draw.ellipse([20, 22, 30, 32], fill=GOLD, outline=BROWN, width=1)

# --- 204. RFID Access Card ---
def draw_rfid_card(draw):
    # Plastic badge
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=BLUE, outline=DKBLUE, width=1)
    # RF waves symbol
    draw.ellipse([21, 21, 29, 29], fill=WHITE)
    draw.ellipse([23, 23, 27, 27], fill=BLUE)
    draw.ellipse([24, 24, 26, 26], fill=WHITE)

# --- 205. Police Laser Speed Gun ---
def draw_laser_speed_gun(draw):
    # Handle
    draw.line([20, 28, 20, 44], fill=BLACK, width=4)
    # Barrel body
    draw.rounded_rectangle([10, 14, 32, 28], radius=2, fill=YELLOW, outline=BLACK, width=1)
    # Optical lens aperture
    draw.ellipse([26, 16, 34, 24], fill=DKGREY, outline=SILVER, width=1)
    draw.ellipse([28, 18, 32, 22], fill=RED)
    # Screen on back
    draw.rectangle([11, 16, 13, 24], fill=BLACK)

# --- 206. Digital Barometer ---
def draw_digital_barometer(draw):
    # Sensor dome
    draw.ellipse([22, 6, 28, 12], fill=SILVER)
    # Handheld body
    draw.rounded_rectangle([14, 12, 36, 44], radius=2, fill=GREY, outline=BLACK, width=1)
    # LCD
    draw.rectangle([17, 18, 33, 28], fill=LIGHTBLUE)
    draw.line([19, 23, 31, 23], fill=BLACK, width=1)

# --- 207. UV Light Index Meter ---
def draw_uv_lux_meter(draw):
    # Light dome
    draw.ellipse([21, 6, 29, 14], fill=WHITE, outline=GREY)
    # Body
    draw.rounded_rectangle([15, 14, 35, 46], radius=2, fill=WHITE, outline=BLACK, width=1)
    # Screen
    draw.rectangle([18, 20, 32, 28], fill=CYAN)
    draw.line([20, 24, 30, 24], fill=BLACK, width=2)

# --- 208. Smart Air Quality Monitor ---
def draw_smart_air_quality_monitor(draw):
    # Monitor block
    draw.rounded_rectangle([12, 12, 38, 38], radius=3, fill=WHITE, outline=GREY, width=1)
    # Grille vents
    for y in range(16, 22, 2):
        draw.line([16, y, 22, y], fill=DKGREY, width=1)
    # Display panel
    draw.rectangle([16, 24, 34, 34], fill=BLACK)
    draw.line([18, 28, 26, 28], fill=GREEN, width=2)

# --- 209. Smart Kettle Base ---
def draw_electric_kettle_base(draw):
    # Circular dock
    draw.ellipse([10, 20, 40, 42], fill=BLACK, outline=GREY, width=1)
    # Connector pins in center
    draw.ellipse([22, 27, 28, 33], fill=GOLD)
    draw.ellipse([24, 29, 26, 31], fill=BLACK)
    # LED settings slider
    draw.line([16, 38, 34, 38], fill=ORANGE, width=2)

# --- 210. E-Ink Shelf Label ---
def draw_e_label(draw):
    # Plastic frame
    draw.rectangle([6, 16, 44, 34], fill=DKGREY, outline=BLACK, width=1)
    # White e-ink display
    draw.rectangle([8, 18, 42, 32], fill=WHITE)
    # Barcode representation
    for x in range(10, 28, 3):
        draw.line([x, 20, x, 28], fill=BLACK, width=1)
    # Price text
    draw.line([30, 24, 40, 24], fill=BLACK, width=2)

# --- 211. USB Soldering Pen ---
def draw_usb_soldering_iron(draw):
    # Pen shaft body
    draw.line([12, 12, 34, 34], fill=DKGREY, width=4)
    # Metal collar
    draw.line([30, 30, 36, 36], fill=SILVER, width=3)
    # Tip
    draw.line([35, 35, 42, 42], fill=SILVER, width=1)
    # USB-C port at back
    draw.ellipse([9, 9, 13, 13], fill=BLACK)

# --- 212. Smart Window Blind Motor ---
def draw_smart_blind_motor(draw):
    # Cylindrical motor
    draw.rounded_rectangle([18, 10, 32, 36], radius=2, fill=WHITE, outline=GREY, width=1)
    # Gear sprocket
    draw.ellipse([21, 32, 29, 40], fill=DKGREY)
    # Beaded chain loop
    draw.line([22, 36, 22, 46], fill=GREY, width=1)
    draw.line([28, 36, 28, 46], fill=GREY, width=1)

# --- 213. E-Drum Sound Module ---
def draw_e_drum_module(draw):
    # Console box
    draw.rounded_rectangle([10, 12, 40, 38], radius=2, fill=GREY, outline=BLACK, width=1)
    # LED screen
    draw.rectangle([14, 16, 26, 26], fill=BLUE)
    # Output knobs & sliders
    draw.line([30, 18, 30, 26], fill=BLACK, width=2)
    draw.ellipse([29, 21, 31, 23], fill=RED)
    draw.ellipse([34, 18, 37, 21], fill=BLACK)
    draw.ellipse([34, 23, 37, 26], fill=BLACK)

# --- 214. HDMI Audio Extractor ---
def draw_hdmi_audio_extractor(draw):
    # Audio splitter box
    draw.rounded_rectangle([12, 16, 38, 34], radius=2, fill=BLACK, outline=DKGREY, width=1)
    # HDMI Ports
    draw.rectangle([16, 22, 22, 26], fill=SILVER)
    # Glowing optical audio port
    draw.rectangle([28, 22, 34, 26], fill=BLACK)
    draw.ellipse([30, 23, 32, 25], fill=RED)

# --- 215. Electricity Monitor Plug ---
def draw_smart_power_meter(draw):
    # Wall plug block
    draw.rounded_rectangle([15, 10, 35, 40], radius=3, fill=WHITE, outline=GREY, width=1)
    # Embedded LCD displaying energy load
    draw.rectangle([18, 14, 32, 22], fill=GREEN)
    draw.line([20, 18, 30, 18], fill=BLACK, width=1)
    # Sockets outlets
    draw.ellipse([21, 30, 23, 32], fill=GREY)
    draw.ellipse([27, 30, 29, 32], fill=GREY)

# --- 216. Thermal Shipping Label Printer ---
def draw_thermal_label_printer(draw):
    # Desktop label printer box
    draw.rounded_rectangle([10, 18, 40, 42], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Wide exit slot
    draw.rectangle([12, 22, 38, 25], fill=BLACK)
    # Ejecting mailing label page
    draw.rectangle([14, 8, 36, 22], fill=WHITE, outline=GREY, width=1)
    # Barcode block printed
    draw.rectangle([16, 12, 24, 18], fill=BLACK)
    draw.line([26, 14, 34, 14], fill=BLACK, width=1)

# --- 217. Bluetooth Audio Dongle ---
def draw_wireless_audio_receiver(draw):
    # USB tip
    draw.rectangle([20, 6, 30, 14], fill=SILVER, outline=BLACK)
    # Transmitter casing
    draw.rounded_rectangle([16, 14, 34, 44], radius=2, fill=BLUE, outline=BLACK, width=1)
    # Pairing button
    draw.ellipse([22, 24, 28, 30], fill=CYAN)
    draw.ellipse([24, 26, 26, 28], fill=WHITE)

# --- 218. Lightning to Headphone Jack Adapter ---
def draw_lightning_to_jack_adapter(draw):
    # Lightning plug
    draw.rectangle([22, 6, 28, 14], fill=WHITE, outline=GREY)
    # Adapter thin cord
    draw.line([25, 14, 25, 30], fill=WHITE, width=2)
    # Female 3.5mm headphone socket
    draw.rounded_rectangle([21, 30, 29, 44], radius=1, fill=WHITE, outline=GREY, width=1)
    draw.ellipse([23, 40, 27, 44], fill=SILVER)

# --- 219. USB-C to HDMI Adapter Hub ---
def draw_usb_c_to_hdmi_dongle(draw):
    # USB-C plug
    draw.rectangle([22, 6, 28, 12], fill=SILVER, outline=BLACK)
    # Short connecting cable
    draw.line([25, 12, 25, 26], fill=DKGREY, width=2)
    # HDMI dock casing
    draw.rounded_rectangle([14, 26, 36, 44], radius=2, fill=GREY, outline=BLACK, width=1)
    # HDMI slot
    draw.rectangle([18, 34, 32, 38], fill=BLACK)

# --- 220. Industrial Thermocouple Module ---
def draw_smart_thermocouple(draw):
    # Control terminal box
    draw.rounded_rectangle([14, 12, 36, 32], radius=2, fill=YELLOW, outline=BLACK, width=1)
    draw.rectangle([18, 16, 32, 24], fill=BLACK)
    draw.line([20, 20, 28, 20], fill=RED, width=1)
    # Braided thermocouple probe cord
    draw.line([25, 32, 25, 42], fill=GREY, width=2)
    draw.ellipse([23, 40, 27, 44], fill=SILVER)

# --- 221. E-Paper Screen Module ---
def draw_e_paper_display_module(draw):
    # Blue PCB board
    draw.rectangle([8, 8, 42, 42], fill=BLUE, outline=BLACK, width=1)
    # E-paper display panel
    draw.rectangle([12, 12, 38, 34], fill=WHITE, outline=GREY, width=1)
    # Drawing on screen
    draw.polygon([(25, 15), (18, 28), (32, 28)], fill=BLACK)
    # Connection pin header
    draw.line([10, 38, 40, 38], fill=GOLD, width=2)

# --- 222. DC Power Distribution Block ---
def draw_power_distribution_block(draw):
    # Heavy plastic block
    draw.rounded_rectangle([10, 14, 40, 38], radius=2, fill=BLACK, outline=GREY, width=1)
    # Brass terminal bars and screws
    for x in range(14, 38, 6):
        draw.rectangle([x, 18, x+3, 24], fill=GOLD)
        draw.ellipse([x, 28, x+3, 31], fill=SILVER)

# --- 223. Smart Shower Water Controller ---
def draw_smart_shower_head_controller(draw):
    # Wall plate panel
    draw.ellipse([10, 10, 40, 40], fill=SILVER, outline=BLACK, width=1)
    # Screen displaying water temperature "104F"
    draw.ellipse([14, 14, 36, 36], fill=BLACK)
    draw.line([19, 22, 22, 22], fill=CYAN, width=2)
    draw.line([24, 22, 27, 22], fill=CYAN, width=2)
    draw.line([29, 22, 31, 22], fill=CYAN, width=2)

# --- 224. Car HUD OBD Screen Projector ---
def draw_car_hud(draw):
    # Projected display beam
    draw.polygon([(25, 26), (6, 6), (44, 6)], fill=(50, 240, 50, 60))
    # Low-profile dash projector unit
    draw.rectangle([14, 26, 36, 38], fill=DKGREY, outline=BLACK, width=1)
    draw.rectangle([16, 28, 34, 32], fill=BLACK)

# --- 225. Wireless Laser Presenter Remote ---
def draw_wireless_presenter(draw):
    # Slender handheld pointer remote
    draw.rounded_rectangle([18, 8, 32, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    # Red laser button trigger
    draw.ellipse([23, 14, 27, 18], fill=RED)
    # Forward/Back buttons
    draw.rectangle([24, 22, 26, 25], fill=GREY)
    draw.rectangle([24, 28, 26, 31], fill=GREY)

# --- 226. Rotary Laser Level Tripod ---
def draw_laser_level_tripod(draw):
    # Tripod legs
    draw.line([25, 26, 14, 46], fill=SILVER, width=2)
    draw.line([25, 26, 36, 46], fill=SILVER, width=2)
    draw.line([25, 26, 25, 46], fill=SILVER, width=2)
    # Laser level unit
    draw.rectangle([18, 14, 32, 26], fill=YELLOW, outline=BLACK, width=1)
    # Spinning laser head throwing horizontal red line
    draw.line([4, 18, 46, 18], fill=RED, width=1)

# --- 227. Portable CD Player ---
def draw_portable_cd_player(draw):
    # Circular Discman body
    draw.ellipse([10, 10, 40, 40], fill=SILVER, outline=GREY, width=1)
    # Glass inspection lid showing CD
    draw.ellipse([14, 14, 36, 36], fill=DKGREY)
    draw.ellipse([22, 22, 28, 28], fill=RED)
    # Playback buttons
    draw.rectangle([21, 38, 25, 40], fill=BLACK)
    draw.rectangle([26, 38, 29, 40], fill=BLACK)

# --- 228. Compact Pocket Radio ---
def draw_pocket_radio(draw):
    # Radio body
    draw.rounded_rectangle([14, 14, 36, 44], radius=2, fill=BLACK, outline=GREY, width=1)
    # Speaker mesh grille lines
    for y in range(28, 40, 3):
        draw.line([18, y, 32, y], fill=DKGREY, width=1)
    # Dial track tuner
    draw.rectangle([18, 18, 32, 22], fill=YELLOW)
    draw.line([25, 18, 25, 22], fill=RED, width=1)
    # Telescopic antenna
    draw.line([16, 14, 16, 4], fill=SILVER, width=1)

# --- 229. Handheld Dictaphone Audio Recorder ---
def draw_digital_audio_recorder(draw):
    # Top microphone grilles
    draw.ellipse([18, 6, 22, 12], fill=SILVER)
    draw.ellipse([28, 6, 32, 12], fill=SILVER)
    # Dictaphone body
    draw.rounded_rectangle([15, 12, 35, 46], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # LCD Display
    draw.rectangle([18, 16, 32, 24], fill=LIGHTBLUE)
    # Red Record button
    draw.ellipse([23, 30, 27, 34], fill=RED)

# --- 230. Smart Garage Door Opener ---
def draw_smart_garage_door_opener(draw):
    # Opener box
    draw.rounded_rectangle([12, 14, 38, 38], radius=2, fill=WHITE, outline=GREY, width=1)
    # Central status light bar
    draw.rectangle([18, 24, 32, 28], fill=CYAN)
    # Wire terminal screws
    for x in range(16, 36, 5):
        draw.ellipse([x, 34, x+2, 36], fill=GOLD)

# --- 231. LED Pixel Art Frame ---
def draw_led_pixel_art_frame(draw):
    # Wood frame border
    draw.rectangle([8, 8, 42, 42], fill=BROWN, outline=BLACK, width=1)
    # LED Matrix screen showing a pixel heart
    draw.rectangle([11, 11, 39, 39], fill=BLACK)
    # Red pixel heart
    draw.rectangle([21, 19, 29, 31], fill=RED)
    draw.rectangle([23, 21, 27, 29], fill=RED)

# --- 232. Bluetooth BBQ Meat Probe ---
def draw_smart_bbq_thermometer(draw):
    # Wireless transmitter block
    draw.rounded_rectangle([12, 24, 38, 42], radius=2, fill=DKRED, outline=BLACK, width=1)
    draw.rectangle([16, 28, 34, 34], fill=BLACK)
    # Long stainless steel probe
    draw.line([25, 24, 25, 6], fill=SILVER, width=2)
    # Sharp pointer tip
    draw.line([25, 6, 25, 4], fill=SILVER, width=1)

# --- 233. Biometric Fingerprint Padlock ---
def draw_fingerprint_padlock(draw):
    # Padlock shackle steel loop
    draw.arc([16, 8, 34, 24], 180, 360, fill=SILVER, width=3)
    # Padlock base body
    draw.rounded_rectangle([12, 20, 38, 44], radius=3, fill=BLACK, outline=GREY, width=1)
    # Fingerprint scanner plate
    draw.ellipse([20, 26, 30, 36], fill=CYAN, outline=BLUE, width=1)

# --- 234. Solar Electric Fence Energizer ---
def draw_solar_fence_charger(draw):
    # Heavy electrical unit housing
    draw.rounded_rectangle([14, 16, 36, 44], radius=3, fill=YELLOW, outline=BLACK, width=1)
    # Solar panel grid on top lid
    draw.rectangle([16, 18, 34, 28], fill=DKBLUE, outline=SILVER, width=1)
    # Red Warning lightning bolt symbol
    draw.polygon([(25, 30), (22, 36), (25, 36), (24, 42), (28, 34), (25, 34)], fill=RED)

# --- 235. Wireless Desk Intercom Station ---
def draw_wireless_intercom(draw):
    # Desk intercom base
    draw.rounded_rectangle([10, 16, 40, 42], radius=3, fill=GREY, outline=BLACK, width=1)
    # Speaker grille slots
    for y in range(20, 30, 3):
        draw.line([14, y, 26, y], fill=BLACK, width=1)
    # Call button
    draw.ellipse([30, 22, 36, 28], fill=RED)
    # Flexible gooseneck microphone
    draw.line([33, 16, 33, 6], fill=BLACK, width=2)
    draw.ellipse([31, 4, 35, 8], fill=BLACK)

# --- 236. E-Dictionary Pen Scanner ---
def draw_e_dictionary_translator(draw):
    # Scanner pen body
    draw.rounded_rectangle([18, 6, 32, 44], radius=2, fill=WHITE, outline=GREY, width=1)
    # Embedded reading screen display
    draw.rectangle([21, 12, 29, 28], fill=BLACK)
    draw.line([23, 16, 27, 16], fill=CYAN, width=1)
    # Scanner lens tip
    draw.polygon([(21, 44), (29, 44), (25, 48)], fill=SILVER)

# --- 237. Smart Flower Pot Screen ---
def draw_smart_plant_pot(draw):
    # White ceramic flower pot body
    draw.polygon([(14, 10), (36, 10), (32, 44), (18, 44)], fill=WHITE, outline=GREY, width=1)
    # Soil level
    draw.rectangle([15, 10, 35, 14], fill=BROWN)
    # Embedded LCD status screen showing face
    draw.rectangle([20, 22, 30, 32], fill=GREEN)
    draw.ellipse([22, 25, 24, 27], fill=BLACK)
    draw.ellipse([26, 25, 28, 27], fill=BLACK)

# --- 238. LED Tracing Light Pad ---
def draw_led_tracing_pad(draw):
    # Ultra thin white light tablet
    draw.rounded_rectangle([8, 8, 42, 42], radius=1, fill=WHITE, outline=GREY, width=1)
    # Glowing tracing surface
    draw.rectangle([11, 11, 39, 39], fill=CYAN)
    # Grid rule lines
    draw.line([11, 25, 39, 25], fill=WHITE, width=1)
    draw.line([25, 11, 25, 39], fill=WHITE, width=1)

# --- 239. Handheld USB Rechargeable Fan ---
def draw_usb_hand_fan(draw):
    # Handle base
    draw.rounded_rectangle([22, 26, 28, 46], radius=2, fill=WHITE, outline=GREY, width=1)
    # Fan guard cage
    draw.ellipse([14, 6, 36, 28], fill=GREY, outline=WHITE, width=1)
    # Teal blades
    draw.polygon([(25, 17), (21, 9), (25, 9)], fill=CYAN)
    draw.polygon([(25, 17), (31, 21), (31, 17)], fill=CYAN)

# --- 240. Smart Pet Feeding Weighing Bowl ---
def draw_smart_feeder_bowl(draw):
    # Bowl body base
    draw.polygon([(10, 22), (40, 22), (36, 42), (14, 42)], fill=WHITE, outline=GREY, width=1)
    # Bowl cavity
    draw.ellipse([12, 18, 38, 26], fill=GREY)
    # Digital weight LCD readout screen
    draw.rectangle([20, 32, 30, 38], fill=BLACK)
    draw.line([22, 35, 28, 35], fill=CYAN, width=1)

# --- 241. Synthesizer Pocket Instrument ---
def draw_pocket_synthesizer(draw):
    # PCB circuit board base
    draw.rectangle([10, 10, 40, 40], fill=DKGREEN, outline=BLACK, width=1)
    # Tiny LCD screen
    draw.rectangle([14, 14, 24, 22], fill=BLACK)
    # Matrix of colorful micro switch keys
    for y in range(26, 38, 4):
        for x in range(14, 38, 5):
            btn_color = RED if x == 14 else (YELLOW if y == 26 else BLUE)
            draw.rectangle([x, y, x+2, y+2], fill=btn_color)

# --- 242. E-Reader Ring Page Turner ---
def draw_e_reader_page_turner(draw):
    # Ring loop shank
    draw.ellipse([18, 22, 32, 38], fill=SILVER, outline=BLACK, width=2)
    # Button controller pod on top
    draw.rounded_rectangle([15, 10, 35, 26], radius=2, fill=BLACK, outline=GREY, width=1)
    # Page buttons
    draw.polygon([(22, 14), (28, 14), (25, 11)], fill=WHITE)
    draw.polygon([(22, 22), (28, 22), (25, 25)], fill=WHITE)

# --- 243. Smart Water Bottle UV Lid ---
def draw_smart_water_bottle(draw):
    # Stainless steel water bottle
    draw.rounded_rectangle([16, 18, 34, 46], radius=3, fill=SILVER, outline=GREY, width=1)
    # Bottle neck collar
    draw.rectangle([20, 14, 30, 18], fill=SILVER)
    # Smart cap lid containing UV-C indicator light ring
    draw.rounded_rectangle([19, 8, 31, 14], radius=1, fill=BLACK, outline=BLUE, width=1)
    draw.ellipse([22, 9, 28, 13], fill=CYAN)

# --- 244. LiPo Battery Multi-Charger ---
def draw_drone_battery_charger(draw):
    # Multi balance charger box
    draw.rounded_rectangle([10, 12, 40, 40], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Balance ports
    draw.rectangle([14, 28, 24, 34], fill=BLACK)
    draw.rectangle([26, 28, 36, 34], fill=BLACK)
    # Charging status LCD screen
    draw.rectangle([14, 16, 36, 24], fill=BLUE)
    draw.line([16, 20, 26, 20], fill=CYAN, width=1)

# --- 245. Vintage Analog Exposure Light Meter ---
def draw_analog_lux_meter(draw):
    # Meter body casing
    draw.rounded_rectangle([14, 14, 36, 44], radius=2, fill=DKGREY, outline=BLACK, width=1)
    # Dome sensor window
    draw.ellipse([21, 6, 29, 14], fill=WHITE, outline=GREY)
    # Analog needle dial scale
    draw.rectangle([17, 18, 33, 30], fill=BEIGE)
    draw.arc([19, 22, 31, 34], 180, 360, fill=BLACK, width=1)
    # Dial needle indicator
    draw.line([25, 30, 21, 22], fill=RED, width=1)

# --- 246. Dome Ceiling PoE Camera ---
def draw_network_poe_camera(draw):
    # Base ceiling mount block
    draw.rectangle([8, 8, 42, 14], fill=WHITE, outline=GREY, width=1)
    # Translucent glass dome sphere
    draw.ellipse([12, 12, 38, 38], fill=DKBLUE, outline=GREY, width=1)
    # Interior surveillance lens element
    draw.ellipse([20, 20, 30, 30], fill=BLACK)
    draw.ellipse([23, 23, 27, 27], fill=CYAN)

# --- 247. USB Arc Plasma Lighter ---
def draw_electric_arc_lighter(draw):
    # Lighter body casing
    draw.rounded_rectangle([18, 14, 32, 44], radius=2, fill=BLUE, outline=BLACK, width=1)
    # Hinged cap open
    draw.polygon([(18, 14), (8, 6), (12, 4), (22, 12)], fill=BLUE, outline=BLACK)
    # Ignition posts
    draw.line([22, 10, 22, 14], fill=SILVER, width=1)
    draw.line([28, 10, 28, 14], fill=SILVER, width=1)
    # Purple electric arc plasma beam
    draw.line([22, 11, 28, 11], fill=PURPLE, width=1)

# --- 248. Smartphone Thermal Camera Attachment ---
def draw_mini_thermal_imager(draw):
    # USB-C connection pin plug
    draw.rectangle([23, 6, 27, 12], fill=SILVER)
    # Thermal camera adapter box
    draw.rounded_rectangle([12, 12, 38, 28], radius=2, fill=BLACK, outline=GREY, width=1)
    # Gold thermal lens aperture
    draw.ellipse([18, 16, 26, 24], fill=GOLD, outline=BROWN, width=1)
    draw.ellipse([21, 19, 23, 21], fill=BLACK)

# --- 249. Motion Sensor Under-Cabinet Light ---
def draw_under_cabinet_led_bar(draw):
    # Silver light bar base
    draw.rounded_rectangle([4, 20, 46, 30], radius=1, fill=SILVER, outline=GREY, width=1)
    # Matrix of glowing white LEDs
    for x in range(8, 34, 6):
        draw.rectangle([x, 23, x+3, 27], fill=WHITE)
    # PIR motion sensor dome dome
    draw.ellipse([38, 22, 43, 28], fill=WHITE, outline=GREY)

# --- 250. Handheld Laser Tachometer ---
def draw_laser_tachometer(draw):
    # Handheld RPM tester body
    draw.rounded_rectangle([16, 12, 34, 44], radius=3, fill=ORANGE, outline=BLACK, width=1)
    # Top emitter hood
    draw.rectangle([22, 6, 28, 12], fill=BLACK)
    # Projecting red laser dot beam
    draw.line([25, 6, 25, 2], fill=RED, width=1)
    # Screen displaying measurement numbers
    draw.rectangle([19, 20, 31, 28], fill=DKGREY)
    draw.line([21, 24, 29, 24], fill=GREEN, width=1)

DRAWINGS = {
    # Items 201 to 250
    "water_heater_panel": draw_water_heater_panel,
    "e_bike_display": draw_e_bike_display,
    "fido_key": draw_fido_key,
    "rfid_card": draw_rfid_card,
    "laser_speed_gun": draw_laser_speed_gun,
    "digital_barometer": draw_digital_barometer,
    "uv_lux_meter": draw_uv_lux_meter,
    "smart_air_quality_monitor": draw_smart_air_quality_monitor,
    "electric_kettle_base": draw_electric_kettle_base,
    "e_label": draw_e_label,
    "usb_soldering_iron": draw_usb_soldering_iron,
    "smart_blind_motor": draw_smart_blind_motor,
    "e_drum_module": draw_e_drum_module,
    "hdmi_audio_extractor": draw_hdmi_audio_extractor,
    "smart_power_meter": draw_smart_power_meter,
    "thermal_label_printer": draw_thermal_label_printer,
    "wireless_audio_receiver": draw_wireless_audio_receiver,
    "lightning_to_jack_adapter": draw_lightning_to_jack_adapter,
    "usb_c_to_hdmi_dongle": draw_usb_c_to_hdmi_dongle,
    "smart_thermocouple": draw_smart_thermocouple,
    "e_paper_display_module": draw_e_paper_display_module,
    "power_distribution_block": draw_power_distribution_block,
    "smart_shower_head_controller": draw_smart_shower_head_controller,
    "car_hud": draw_car_hud,
    "wireless_presenter": draw_wireless_presenter,
    "laser_level_tripod": draw_laser_level_tripod,
    "portable_cd_player": draw_portable_cd_player,
    "pocket_radio": draw_pocket_radio,
    "digital_audio_recorder": draw_digital_audio_recorder,
    "smart_garage_door_opener": draw_smart_garage_door_opener,
    "led_pixel_art_frame": draw_led_pixel_art_frame,
    "smart_bbq_thermometer": draw_smart_bbq_thermometer,
    "fingerprint_padlock": draw_fingerprint_padlock,
    "solar_fence_charger": draw_solar_fence_charger,
    "wireless_intercom": draw_wireless_intercom,
    "e_dictionary_translator": draw_e_dictionary_translator,
    "smart_plant_pot": draw_smart_plant_pot,
    "led_tracing_pad": draw_led_tracing_pad,
    "usb_hand_fan": draw_usb_hand_fan,
    "smart_feeder_bowl": draw_smart_feeder_bowl,
    "pocket_synthesizer": draw_pocket_synthesizer,
    "e_reader_page_turner": draw_e_reader_page_turner,
    "smart_water_bottle": draw_smart_water_bottle,
    "drone_battery_charger": draw_drone_battery_charger,
    "analog_lux_meter": draw_analog_lux_meter,
    "network_poe_camera": draw_network_poe_camera,
    "electric_arc_lighter": draw_electric_arc_lighter,
    "mini_thermal_imager": draw_mini_thermal_imager,
    "under_cabinet_led_bar": draw_under_cabinet_led_bar,
    "laser_tachometer": draw_laser_tachometer
}

if __name__ == "__main__":
    print(f"Generating 50 new detailed electronics sprites (items 201-250) inside {OUTPUT_DIR}...")
    for name, func in DRAWINGS.items():
        create_sprite(name, func)
    print("Done generating 50 new detailed electronics sprites!")
