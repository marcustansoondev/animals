import os
import re
from PIL import Image, ImageDraw

OUTPUT_DIR = "images/weather"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define the 102 weather items
weather_data = [
    # Sunny/Clear
    {"id": "sunny_day", "name": "Sunny Day", "type": "Sunny", "material": "Light", "rarity": "★☆☆☆☆", "desc": "A bright, clear day with blue skies and a radiant sun.", "draw_type": "sunny_day"},
    {"id": "sunny_intervals", "name": "Sunny Intervals", "type": "Cloudy", "material": "Water Vapor", "rarity": "★☆☆☆☆", "desc": "Bright sunshine peering through fluffy white clouds.", "draw_type": "sunny_intervals"},
    {"id": "clear_night", "name": "Clear Night Sky", "type": "Clear", "material": "Vacuum", "rarity": "★★☆☆☆", "desc": "A quiet, dark night sky illuminated by a crescent moon and twinkling stars.", "draw_type": "clear_night"},
    {"id": "starry_night", "name": "Starry Night", "type": "Clear", "material": "Light", "rarity": "★★☆☆☆", "desc": "A deep indigo night sky filled with countless sparkling stars and constellations.", "draw_type": "starry_night"},
    {"id": "heatwave", "name": "Heatwave", "type": "Extreme", "material": "Thermal Energy", "rarity": "★★★☆☆", "desc": "Intense summer heatwave with shimmering heat distortion waves rising from dry ground.", "draw_type": "heatwave"},
    {"id": "solar_wind", "name": "Solar Wind", "type": "Space", "material": "Plasma", "rarity": "★★★★★", "desc": "A stream of charged particles released from the upper atmosphere of the Sun.", "draw_type": "solar_wind"},
    {"id": "sun_dog", "name": "Sun Dog", "type": "Atmospheric", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "An atmospheric optical phenomenon causing bright spots on either side of the Sun.", "draw_type": "sun_dog"},
    {"id": "crepuscular_rays", "name": "Crepuscular Rays", "type": "Atmospheric", "material": "Light", "rarity": "★★★☆☆", "desc": "Beams of sunlight radiating from a single point in the sky, breaking through clouds.", "draw_type": "crepuscular_rays"},
    {"id": "green_flash", "name": "Green Flash", "type": "Atmospheric", "material": "Light", "rarity": "★★★★★", "desc": "A brief green ray visible at the upper rim of the Sun's disk at sunrise or sunset.", "draw_type": "green_flash"},
    {"id": "morning_sun", "name": "Morning Sun", "type": "Sunny", "material": "Light", "rarity": "★☆☆☆☆", "desc": "The gentle, warm light of the early morning sun rising above the horizon.", "draw_type": "morning_sun"},
    {"id": "noon_glare", "name": "Noon Glare", "type": "Sunny", "material": "Light", "rarity": "★☆☆☆☆", "desc": "The intense, bright glare of the sun at its highest point in the sky.", "draw_type": "noon_glare"},
    {"id": "hazy_sun", "name": "Hazy Sun", "type": "Atmospheric", "material": "Aerosols", "rarity": "★★☆☆☆", "desc": "The sun appearing as a soft, blurred disc through a thin layer of atmospheric haze.", "draw_type": "hazy_sun"},

    # Clouds
    {"id": "cloudy", "name": "Cloudy Sky", "type": "Cloudy", "material": "Water Vapor", "rarity": "★☆☆☆☆", "desc": "A sky filled with friendly, puffy white cumulus clouds.", "draw_type": "cloudy"},
    {"id": "overcast", "name": "Overcast Sky", "type": "Cloudy", "material": "Water Vapor", "rarity": "★☆☆☆☆", "desc": "A solid blanket of dull grey stratus clouds covering the entire sky.", "draw_type": "overcast"},
    {"id": "cirrus_clouds", "name": "Cirrus Clouds", "type": "Cloudy", "material": "Ice Crystals", "rarity": "★★☆☆☆", "desc": "Thin, wispy, feather-like clouds high in the atmosphere.", "draw_type": "cirrus_clouds"},
    {"id": "cumulus_clouds", "name": "Cumulus Clouds", "type": "Cloudy", "material": "Water Vapor", "rarity": "★☆☆☆☆", "desc": "Fluffy, cotton-like clouds with distinct flat bases.", "draw_type": "cumulus_clouds"},
    {"id": "stratus_clouds", "name": "Stratus Clouds", "type": "Cloudy", "material": "Water Vapor", "rarity": "★☆☆☆☆", "desc": "Low-level grey clouds that form a uniform, featureless sheet.", "draw_type": "stratus_clouds"},
    {"id": "altocumulus", "name": "Altocumulus Clouds", "type": "Cloudy", "material": "Water Vapor", "rarity": "★★☆☆☆", "desc": "Patches of small, roll-like cloud elements clustered together.", "draw_type": "altocumulus"},
    {"id": "noctilucent_clouds", "name": "Noctilucent Clouds", "type": "Atmospheric", "material": "Ice Crystals", "rarity": "★★★★★", "desc": "Rare, glowing blue-white clouds visible in deep twilight at high latitudes.", "draw_type": "noctilucent_clouds"},
    {"id": "shelf_cloud", "name": "Shelf Cloud", "type": "Stormy", "material": "Water Vapor", "rarity": "★★★★☆", "desc": "A low, wedge-shaped cloud formation associated with the leading edge of a thunderstorm.", "draw_type": "shelf_cloud"},
    {"id": "roll_cloud", "name": "Roll Cloud", "type": "Cloudy", "material": "Water Vapor", "rarity": "★★★★☆", "desc": "A rare, tube-shaped cloud that appears to roll along a horizontal axis.", "draw_type": "roll_cloud"},
    {"id": "lenticular_cloud", "name": "Lenticular Cloud", "type": "Cloudy", "material": "Water Vapor", "rarity": "★★★★☆", "desc": "Saucer-shaped clouds that form over mountains, often mistaken for UFOs.", "draw_type": "lenticular_cloud"},
    {"id": "mammatus_clouds", "name": "Mammatus Clouds", "type": "Stormy", "material": "Ice & Water", "rarity": "★★★★☆", "desc": "Pouch-like structures hanging from the underside of a thunderstorm anvil.", "draw_type": "mammatus_clouds"},
    {"id": "thundercloud", "name": "Thundercloud", "type": "Stormy", "material": "Water Vapor", "rarity": "★★☆☆☆", "desc": "A massive, dark cumulonimbus cloud pulsing with potential energy.", "draw_type": "thundercloud"},

    # Rain
    {"id": "light_rain", "name": "Light Rain", "type": "Rainy", "material": "Water Drops", "rarity": "★☆☆☆☆", "desc": "A gentle drizzle of small water droplets falling from a grey cloud.", "draw_type": "light_rain"},
    {"id": "heavy_rain", "name": "Heavy Rain", "type": "Rainy", "material": "Water Drops", "rarity": "★★☆☆☆", "desc": "Torrential rain falling in thick, vertical sheets from dark storm clouds.", "draw_type": "heavy_rain"},
    {"id": "sun_shower", "name": "Sun Shower", "type": "Rainy", "material": "Water & Light", "rarity": "★★★☆☆", "desc": "A beautiful meteorological event where rain falls while the sun is shining.", "draw_type": "sun_shower"},
    {"id": "monsoon", "name": "Monsoon Rain", "type": "Rainy", "material": "Water Drops", "rarity": "★★★★☆", "desc": "Torrential seasonal rainfall typical of tropical regions, creating local flooding.", "draw_type": "monsoon"},
    {"id": "acid_rain", "name": "Acid Rain", "type": "Extreme", "material": "Acidic Water", "rarity": "★★★★★", "desc": "Corrosive rain containing high levels of nitric and sulfuric acids.", "draw_type": "acid_rain"},
    {"id": "virga", "name": "Virga", "type": "Atmospheric", "material": "Water Vapor", "rarity": "★★★★☆", "desc": "Streaks of rain that evaporate in mid-air before reaching the ground.", "draw_type": "virga"},
    {"id": "squall_line", "name": "Squall Line Rain", "type": "Stormy", "material": "Water Drops", "rarity": "★★★☆☆", "desc": "A narrow, fast-moving band of high winds and violent rain showers.", "draw_type": "squall_line"},
    {"id": "downburst", "name": "Downburst", "type": "Stormy", "material": "Water & Wind", "rarity": "★★★★☆", "desc": "A localized column of sinking air producing destructive straight-line winds.", "draw_type": "downburst"},
    {"id": "drizzle", "name": "Drizzle", "type": "Rainy", "material": "Water Drops", "rarity": "★☆☆☆☆", "desc": "Very fine, light rain droplets that seem to float in the air.", "draw_type": "drizzle"},
    {"id": "cloudburst", "name": "Cloudburst", "type": "Rainy", "material": "Water Drops", "rarity": "★★★★☆", "desc": "An extreme, sudden, and brief downpour of immense intensity.", "draw_type": "cloudburst"},
    {"id": "cold_rain", "name": "Cold Rain", "type": "Rainy", "material": "Water Drops", "rarity": "★★☆☆☆", "desc": "Rain falling in near-freezing temperatures, chilled and stinging.", "draw_type": "cold_rain"},
    {"id": "misty_rain", "name": "Misty Rain", "type": "Rainy", "material": "Water Drops", "rarity": "★★☆☆☆", "desc": "A mixture of light rain and heavy mist, creating poor visibility.", "draw_type": "misty_rain"},

    # Thunderstorm
    {"id": "thunderstorm", "name": "Thunderstorm", "type": "Stormy", "material": "Electricity", "rarity": "★★☆☆☆", "desc": "A classic thunderstorm with rain and a bright bolt of lightning.", "draw_type": "thunderstorm"},
    {"id": "severe_thunderstorm", "name": "Severe Thunderstorm", "type": "Stormy", "material": "Electricity", "rarity": "★★★☆☆", "desc": "A violent storm featuring multiple lightning strikes, wind, and rain.", "draw_type": "severe_thunderstorm"},
    {"id": "dry_thunderstorm", "name": "Dry Thunderstorm", "type": "Stormy", "material": "Electricity", "rarity": "★★★★☆", "desc": "Thunderstorm with lightning but no rain reaching the dry ground.", "draw_type": "dry_thunderstorm"},
    {"id": "heat_lightning", "name": "Heat Lightning", "type": "Stormy", "material": "Electricity", "rarity": "★★★☆☆", "desc": "Silent flashes of lightning reflecting off clouds on the horizon.", "draw_type": "heat_lightning"},
    {"id": "ball_lightning", "name": "Ball Lightning", "type": "Extreme", "material": "Plasma", "rarity": "★★★★★", "desc": "A rare, glowing spherical electrical phenomenon floating near the ground.", "draw_type": "ball_lightning"},
    {"id": "st_elmos_fire", "name": "St. Elmo's Fire", "type": "Atmospheric", "material": "Plasma", "rarity": "★★★★★", "desc": "A glowing blue or violet corona discharge from pointed objects in storms.", "draw_type": "st_elmos_fire"},
    {"id": "lightning_strike", "name": "Lightning Strike", "type": "Stormy", "material": "Electricity", "rarity": "★★★☆☆", "desc": "A single powerful bolt of lightning striking the earth directly.", "draw_type": "lightning_strike"},
    {"id": "sheet_lightning", "name": "Sheet Lightning", "type": "Stormy", "material": "Electricity", "rarity": "★★☆☆☆", "desc": "Lightning that occurs within a cloud, illuminating the entire cloud sheet.", "draw_type": "sheet_lightning"},
    {"id": "forked_lightning", "name": "Forked Lightning", "type": "Stormy", "material": "Electricity", "rarity": "★★★☆☆", "desc": "Lightning that branches out into multiple paths as it strikes down.", "draw_type": "forked_lightning"},
    {"id": "purple_storm", "name": "Purple Storm", "type": "Stormy", "material": "Electricity", "rarity": "★★★☆☆", "desc": "A storm cloud glowing with a beautiful deep purple hue from lightning.", "draw_type": "purple_storm"},
    {"id": "supercell", "name": "Supercell Storm", "type": "Stormy", "material": "Water Vapor", "rarity": "★★★★☆", "desc": "A massive, rotating thunderstorm with a deep, persistent updraft.", "draw_type": "supercell"},
    {"id": "winter_lightning", "name": "Winter Lightning", "type": "Stormy", "material": "Electricity", "rarity": "★★★★☆", "desc": "Lightning occurring during a snowstorm, also known as thundersnow.", "draw_type": "winter_lightning"},

    # Snow & Ice
    {"id": "light_snow", "name": "Light Snow", "type": "Snowy", "material": "Ice Crystals", "rarity": "★☆☆☆☆", "desc": "A gentle snowfall with small, fluffy flakes drifting down.", "draw_type": "light_snow"},
    {"id": "heavy_snow", "name": "Heavy Snow", "type": "Snowy", "material": "Ice Crystals", "rarity": "★★☆☆☆", "desc": "A dense snowfall blanketing the ground under a grey sky.", "draw_type": "heavy_snow"},
    {"id": "blizzard", "name": "Blizzard", "type": "Extreme", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "A severe snowstorm with high winds and near-zero visibility.", "draw_type": "blizzard"},
    {"id": "hailstorm", "name": "Hailstorm", "type": "Extreme", "material": "Ice Pellets", "rarity": "★★★☆☆", "desc": "Small chunks of ice falling from a severe thunderstorm cloud.", "draw_type": "hailstorm"},
    {"id": "freezing_rain", "name": "Freezing Rain", "type": "Extreme", "material": "Glaze Ice", "rarity": "★★★☆☆", "desc": "Rain that freezes immediately upon contact with cold surfaces.", "draw_type": "freezing_rain"},
    {"id": "diamond_dust", "name": "Diamond Dust", "type": "Atmospheric", "material": "Ice Crystals", "rarity": "★★★★★", "desc": "Tiny, sparkling ice crystals suspended in clear, cold air.", "draw_type": "diamond_dust"},
    {"id": "frost_pattern", "name": "Frost Pattern", "type": "Snowy", "material": "Ice Crystals", "rarity": "★★★☆☆", "desc": "Intricate, feather-like ice crystal structures formed on window glass.", "draw_type": "frost_pattern"},
    {"id": "rime_ice", "name": "Rime Ice", "type": "Snowy", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "A white, opaque coating of ice needles deposited by freezing fog.", "draw_type": "rime_ice"},
    {"id": "glaze_ice", "name": "Glaze Ice", "type": "Snowy", "material": "Smooth Ice", "rarity": "★★★☆☆", "desc": "A smooth, clear coating of ice that covers all outdoor objects.", "draw_type": "glaze_ice"},
    {"id": "thundersnow", "name": "Thundersnow", "type": "Stormy", "material": "Ice & Electricity", "rarity": "★★★★★", "desc": "An unusual winter storm where lightning occurs during heavy snowfall.", "draw_type": "thundersnow"},
    {"id": "whiteout", "name": "Whiteout", "type": "Extreme", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "Weather conditions in which visibility and contrast are severely reduced by snow.", "draw_type": "whiteout"},
    {"id": "ice_fog", "name": "Ice Fog", "type": "Snowy", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "A type of fog consisting of fine ice particles suspended in air.", "draw_type": "ice_fog"},

    # Wind
    {"id": "windy", "name": "Windy Day", "type": "Windy", "material": "Air Currents", "rarity": "★☆☆☆☆", "desc": "A breezy day with visible wind gusts blowing green leaves.", "draw_type": "windy"},
    {"id": "tornado", "name": "Tornado", "type": "Extreme", "material": "Air Currents", "rarity": "★★★★☆", "desc": "A violent, rotating column of air extending from a cloud to the ground.", "draw_type": "tornado"},
    {"id": "hurricane", "name": "Hurricane", "type": "Extreme", "material": "Water & Wind", "rarity": "★★★★★", "desc": "A massive, rotating tropical storm system with high winds and rain.", "draw_type": "hurricane"},
    {"id": "cyclone", "name": "Cyclone", "type": "Extreme", "material": "Air Currents", "rarity": "★★★★☆", "desc": "A large-scale atmospheric wind rotation centered on low pressure.", "draw_type": "cyclone"},
    {"id": "typhoon", "name": "Typhoon", "type": "Extreme", "material": "Water & Wind", "rarity": "★★★★☆", "desc": "A tropical cyclone developing in the northwestern Pacific basin.", "draw_type": "typhoon"},
    {"id": "dust_devil", "name": "Dust Devil", "type": "Windy", "material": "Dust & Air", "rarity": "★★★☆☆", "desc": "A small, rapidly rotating whirlwind made visible by swirling dust.", "draw_type": "dust_devil"},
    {"id": "waterspout", "name": "Waterspout", "type": "Extreme", "material": "Water & Wind", "rarity": "★★★★☆", "desc": "A swirling column of wind and water mist forming over the ocean.", "draw_type": "waterspout"},
    {"id": "gale_force_wind", "name": "Gale Force Wind", "type": "Windy", "material": "Air Currents", "rarity": "★★★☆☆", "desc": "Very strong, damaging winds bending tree branches and blowing debris.", "draw_type": "gale_force_wind"},
    {"id": "derecho", "name": "Derecho", "type": "Extreme", "material": "Air Currents", "rarity": "★★★★★", "desc": "A widespread, long-lived, straight-line windstorm associated with fast storms.", "draw_type": "derecho"},
    {"id": "microburst", "name": "Microburst", "type": "Stormy", "material": "Air Currents", "rarity": "★★★★☆", "desc": "A small, localized column of sinking air that drops straight down.", "draw_type": "microburst"},
    {"id": "sea_breeze", "name": "Sea Breeze", "type": "Windy", "material": "Air Currents", "rarity": "★☆☆☆☆", "desc": "A cool breeze blowing from the sea toward the land during the day.", "draw_type": "sea_breeze"},
    {"id": "land_breeze", "name": "Land Breeze", "type": "Windy", "material": "Air Currents", "rarity": "★☆☆☆☆", "desc": "A breeze blowing from the land toward the sea at night.", "draw_type": "land_breeze"},

    # Fog & Dust
    {"id": "foggy", "name": "Foggy Day", "type": "Foggy", "material": "Water Droplets", "rarity": "★☆☆☆☆", "desc": "A thick blanket of fog near the ground obscuring details.", "draw_type": "foggy"},
    {"id": "sandstorm", "name": "Sandstorm", "type": "Extreme", "material": "Sand & Dust", "rarity": "★★★☆☆", "desc": "A strong wind carrying clouds of sand through the air in dry areas.", "draw_type": "sandstorm"},
    {"id": "dust_storm", "name": "Dust Storm", "type": "Extreme", "material": "Soil Particles", "rarity": "★★★☆☆", "desc": "A wall of dust blown by strong winds, reducing visibility to zero.", "draw_type": "dust_storm"},
    {"id": "haboob", "name": "Haboob", "type": "Extreme", "material": "Dust & Air", "rarity": "★★★★☆", "desc": "A giant, dramatic wall of dust rolling over a desert landscape.", "draw_type": "haboob"},
    {"id": "smog", "name": "Smoggy Sky", "type": "Foggy", "material": "Pollutants", "rarity": "★★☆☆☆", "desc": "A thick, yellowish haze caused by industrial air pollution.", "draw_type": "smog"},
    {"id": "misty_morning", "name": "Misty Morning", "type": "Foggy", "material": "Water Droplets", "rarity": "★★☆☆☆", "desc": "A soft, peaceful morning mist rising from the cool ground.", "draw_type": "misty_morning"},
    {"id": "steam_fog", "name": "Steam Fog", "type": "Foggy", "material": "Water Vapor", "rarity": "★★★☆☆", "desc": "Fog formed when very cold air passes over warmer open water.", "draw_type": "steam_fog"},
    {"id": "radiation_fog", "name": "Radiation Fog", "type": "Foggy", "material": "Water Droplets", "rarity": "★★☆☆☆", "desc": "Ground fog formed on clear, calm nights as the earth cools.", "draw_type": "radiation_fog"},
    {"id": "upslope_fog", "name": "Upslope Fog", "type": "Foggy", "material": "Water Droplets", "rarity": "★★★☆☆", "desc": "Fog formed as humid air flows up mountain slopes and cools.", "draw_type": "upslope_fog"},
    {"id": "inversion_layer", "name": "Inversion Fog", "type": "Foggy", "material": "Water Droplets", "rarity": "★★★★☆", "desc": "Fog trapped in valleys beneath a layer of warm air.", "draw_type": "inversion_layer"},
    {"id": "haze", "name": "Atmospheric Haze", "type": "Foggy", "material": "Aerosols", "rarity": "★★☆☆☆", "desc": "A slight obscuration of the lower atmosphere by dry particles.", "draw_type": "haze"},
    {"id": "volcanic_ash_cloud", "name": "Volcanic Ash Cloud", "type": "Extreme", "material": "Pulverized Rock", "rarity": "★★★★★", "desc": "A dark, hazardous cloud of volcanic ash and gas erupting into the sky.", "draw_type": "volcanic_ash_cloud"},

    # Rainbow & Optical
    {"id": "rainbow", "name": "Rainbow", "type": "Atmospheric", "material": "Water & Light", "rarity": "★★☆☆☆", "desc": "A beautiful multicolored arc in the sky caused by refraction of sunlight.", "draw_type": "rainbow"},
    {"id": "double_rainbow", "name": "Double Rainbow", "type": "Atmospheric", "material": "Water & Light", "rarity": "★★★★☆", "desc": "A secondary, fainter rainbow seen outside the primary arc.", "draw_type": "double_rainbow"},
    {"id": "fog_bow", "name": "Fog Bow", "type": "Atmospheric", "material": "Water & Light", "rarity": "★★★★★", "desc": "A rare, colorless rainbow produced by sunlight reflecting in fog.", "draw_type": "fog_bow"},
    {"id": "moon_bow", "name": "Moon Bow", "type": "Atmospheric", "material": "Water & Light", "rarity": "★★★★★", "desc": "A rare rainbow produced by the light of the moon instead of the sun.", "draw_type": "moon_bow"},
    {"id": "halo_optical", "name": "Solar Halo", "type": "Atmospheric", "material": "Ice Crystals", "rarity": "★★★★☆", "desc": "A ring of light forming around the Sun due to ice crystal refraction.", "draw_type": "halo_optical"},
    {"id": "glory_optical", "name": "Glory", "type": "Atmospheric", "material": "Water Droplets", "rarity": "★★★★★", "desc": "An optical phenomenon of concentric rings of color around the observer's shadow.", "draw_type": "glory_optical"},
    {"id": "fata_morgana", "name": "Fata Morgana", "type": "Atmospheric", "material": "Air & Light", "rarity": "★★★★★", "desc": "A complex, rapidly changing mirage seen on horizons in cold regions.", "draw_type": "fata_morgana"},
    {"id": "corona_optical", "name": "Solar Corona", "type": "Atmospheric", "material": "Water Droplets", "rarity": "★★★★☆", "desc": "Concentric colored rings surrounding the Sun or Moon through thin clouds.", "draw_type": "corona_optical"},

    # Sky & Sunset
    {"id": "sunrise", "name": "Sunrise", "type": "Sunny", "material": "Light", "rarity": "★☆☆☆☆", "desc": "The sun rising above the horizon in a beautiful orange sky.", "draw_type": "sunrise"},
    {"id": "sunset", "name": "Sunset", "type": "Sunny", "material": "Light", "rarity": "★☆☆☆☆", "desc": "A beautiful crimson and purple sky as the sun sinks below the horizon.", "draw_type": "sunset"},
    {"id": "cloudy_night", "name": "Cloudy Night", "type": "Cloudy", "material": "Water Vapor", "rarity": "★★☆☆☆", "desc": "A dark night sky with clouds partially covering the crescent moon.", "draw_type": "cloudy_night"},
    {"id": "full_moon", "name": "Full Moon", "type": "Clear", "material": "Reflected Light", "rarity": "★★☆☆☆", "desc": "A bright, glowing full moon hanging in a clear night sky.", "draw_type": "full_moon"},
    {"id": "solar_eclipse", "name": "Solar Eclipse", "type": "Atmospheric", "material": "Shadow", "rarity": "★★★★★", "desc": "The moon blocking out the sun, showing a glowing ring of light.", "draw_type": "solar_eclipse"},
    {"id": "lunar_eclipse", "name": "Lunar Eclipse", "type": "Atmospheric", "material": "Shadow", "rarity": "★★★★★", "desc": "The earth's shadow casting a deep reddish-orange glow on the moon.", "draw_type": "lunar_eclipse"},
    {"id": "blood_moon", "name": "Blood Moon", "type": "Atmospheric", "material": "Reflected Light", "rarity": "★★★★★", "desc": "A full moon glowing with an eerie, deep blood-red color.", "draw_type": "blood_moon"},
    {"id": "aurora_borealis", "name": "Aurora Borealis", "type": "Space", "material": "Charged Particles", "rarity": "★★★★★", "desc": "Beautiful green and purple light curtains dancing in polar skies.", "draw_type": "aurora_borealis"},
    {"id": "aurora_australis", "name": "Aurora Australis", "type": "Space", "material": "Charged Particles", "rarity": "★★★★★", "desc": "The southern lights, dancing in red and green hues over Antarctica.", "draw_type": "aurora_australis"},
    {"id": "meteor_shower", "name": "Meteor Shower", "type": "Space", "material": "Meteoroids", "rarity": "★★★★☆", "desc": "Multiple bright shooting stars streaking across the night sky.", "draw_type": "meteor_shower"},

    # Other & Extreme
    {"id": "firestorm", "name": "Firestorm", "type": "Extreme", "material": "Combusting Gas", "rarity": "★★★★★", "desc": "A conflagration which attains such intensity that it creates its own wind system.", "draw_type": "firestorm"},
    {"id": "plasma_rain", "name": "Plasma Rain", "type": "Space", "material": "Plasma", "rarity": "★★★★★", "desc": "Hot coronal plasma loops condensing and raining back onto the Sun's surface.", "draw_type": "plasma_rain"},
    {"id": "cosmic_dust", "name": "Cosmic Dust", "type": "Space", "material": "Silicates & Carbon", "rarity": "★★★★★", "desc": "Clouds of dust and gas drifting through space, catching star light.", "draw_type": "cosmic_dust"},
    {"id": "space_weather", "name": "Space Weather", "type": "Space", "material": "Solar Particles", "rarity": "★★★★★", "desc": "Environmental conditions in space driven by solar activity and winds.", "draw_type": "space_weather"},
    {"id": "frostbite_cold", "name": "Frostbite Cold", "type": "Extreme", "material": "Frost", "rarity": "★★★☆☆", "desc": "Extreme sub-zero cold causing ice crystals to instantly form on objects.", "draw_type": "frostbite_cold"},
    {"id": "thaw_melt", "name": "Thaw Melt", "type": "Sunny", "material": "Meltwater", "rarity": "★★☆☆☆", "desc": "A warming period causing snow and icicles to melt and drip rapidly.", "draw_type": "thaw_melt"},

    # 2 more to satisfy "more than 100" (total 102)
    {"id": "sand_dunes_wind", "name": "Sand Dunes Wind", "type": "Windy", "material": "Sand", "rarity": "★★★☆☆", "desc": "Wind blowing ripples of sand off golden desert dunes.", "draw_type": "sand_dunes_wind"},
    {"id": "morning_dew", "name": "Morning Dew", "type": "Clear", "material": "Water Droplets", "rarity": "★★☆☆☆", "desc": "Tiny, pristine drops of morning dew sparkling on a green leaf.", "draw_type": "morning_dew"}
]

# Color constants
YELLOW     = (255, 220, 0, 255)
GOLD       = (240, 180, 20, 255)
ORANGE     = (255, 120, 0, 255)
RED        = (240, 50, 40, 255)
WHITE      = (255, 255, 255, 255)
SNOW_WHITE = (245, 250, 255, 255)
GREY       = (180, 180, 185, 255)
LIGHT_GREY = (220, 220, 225, 255)
CLOUD_LIGHT = (240, 240, 245, 255)
DARK_GREY  = (90, 95, 105, 255)
BLUE       = (50, 130, 240, 255)
LIGHT_BLUE = (120, 190, 255, 255)
DARK_BLUE  = (20, 40, 100, 255)
PURPLE     = (150, 60, 220, 255)
GREEN      = (60, 190, 80, 255)
LIGHT_GREEN= (130, 230, 100, 255)
DARK_GREEN = (30, 100, 45, 255)
BROWN      = (140, 90, 50, 255)
CYAN       = (50, 230, 230, 255)
SHADOW     = (0, 0, 0, 70)

# Helper drawing functions
def draw_cloud(draw, cx, cy, color, shadow=None):
    if shadow:
        draw.ellipse([cx-13, cy+2, cx+17, cy+16], fill=shadow)
        draw.ellipse([cx-6, cy-6, cx+10, cy+10], fill=shadow)
        draw.ellipse([cx-20, cy+6, cx-8, cy+16], fill=shadow)
        draw.ellipse([cx+12, cy+6, cx+24, cy+16], fill=shadow)
    draw.ellipse([cx-15, cy, cx+15, cy+14], fill=color)
    draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill=color)
    draw.ellipse([cx-22, cy+4, cx-10, cy+14], fill=color)
    draw.ellipse([cx+10, cy+4, cx+22, cy+14], fill=color)

def draw_sun(draw, cx, cy, r, color, rays=False, ray_color=None):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    if rays:
        rc = ray_color if ray_color else color
        # Draw rays
        draw.line([cx-r-5, cy, cx-r-2, cy], fill=rc, width=2)
        draw.line([cx+r+2, cy, cx+r+5, cy], fill=rc, width=2)
        draw.line([cx, cy-r-5, cx, cy-r-2], fill=rc, width=2)
        draw.line([cx, cy+r+2, cx, cy+r+5], fill=rc, width=2)
        draw.line([cx-r-3, cy-r-3, cx-r-1, cy-r-1], fill=rc, width=2)
        draw.line([cx+r+1, cy+r+1, cx+r+3, cy+r+3], fill=rc, width=2)
        draw.line([cx+r+1, cy-r-3, cx+r+3, cy-r-1], fill=rc, width=2)
        draw.line([cx-r-3, cy+r+1, cx-r-1, cy+r+3], fill=rc, width=2)

def draw_crescent_moon(img, cx, cy, r, color, shadow_offset=6):
    mask = Image.new("L", (50, 50), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=255)
    m_draw.ellipse([cx-r+shadow_offset, cy-r-1, cx+r+shadow_offset, cy+r+1], fill=0)
    
    temp = Image.new("RGBA", (50, 50), (0,0,0,0))
    t_draw = ImageDraw.Draw(temp)
    t_draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    img.paste(temp, mask=mask)

def draw_stars(draw, count, color, seed=42):
    import random
    random.seed(seed)
    for _ in range(count):
        x = random.randint(3, 47)
        y = random.randint(3, 40)
        draw.point([x, y], fill=color)

def draw_rain(draw, count, color, length=5, seed=42):
    import random
    random.seed(seed)
    for _ in range(count):
        x = random.randint(3, 47)
        y = random.randint(12, 47)
        draw.line([x, y, x - 1, y + length], fill=color, width=1)

def draw_snow(draw, count, color, seed=42):
    import random
    random.seed(seed)
    for _ in range(count):
        x = random.randint(3, 47)
        y = random.randint(12, 47)
        draw.point([x, y], fill=color)
        if random.choice([True, False]):
            draw.point([x+1, y], fill=color)
            draw.point([x-1, y], fill=color)
            draw.point([x, y+1], fill=color)
            draw.point([x, y-1], fill=color)

def draw_lightning(draw, x0, y0, x1, y1, color):
    mx = (x0 + x1) // 2
    my = (y0 + y1) // 2 + 3
    draw.line([x0, y0, mx, my], fill=color, width=2)
    draw.line([mx, my, x1, y1], fill=color, width=2)

def draw_tornado(draw, cx, cy, color):
    for i in range(12):
        y = cy - 15 + i * 3
        w = 18 - i * 1.5
        draw.ellipse([cx - w, y, cx + w, y + 2], fill=color)

def draw_wind_lines(draw, color, seed=42):
    import random
    random.seed(seed)
    for _ in range(3):
        y = random.randint(10, 40)
        draw.arc([10, y, 25, y+8], 180, 360, fill=color, width=1)
        draw.arc([25, y+2, 40, y+10], 0, 180, fill=color, width=1)

def draw_rainbow(draw, cx, cy, colors):
    for idx, color in enumerate(colors):
        r = 20 - idx * 2
        draw.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=color, width=2)

def build_images():
    print("Generating 102 Weather Sprites...")
    for item in weather_data:
        dtype = item["draw_type"]
        name = item["id"]
        
        img = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # --- Dispatch Drawing Logic ---
        if dtype == "sunny_day":
            draw_sun(draw, 25, 22, 12, YELLOW, rays=True, ray_color=GOLD)
            
        elif dtype == "sunny_intervals":
            draw_sun(draw, 32, 16, 10, YELLOW, rays=True, ray_color=GOLD)
            draw_cloud(draw, 20, 24, CLOUD_LIGHT, shadow=SHADOW)
            
        elif dtype == "clear_night":
            draw_stars(draw, 6, WHITE, seed=1)
            draw_crescent_moon(img, 22, 20, 12, YELLOW)
            
        elif dtype == "starry_night":
            draw_stars(draw, 15, WHITE, seed=2)
            # small constellations
            draw.line([10, 10, 18, 14, 25, 12], fill=LIGHT_BLUE, width=1)
            draw.line([30, 30, 35, 38, 42, 35], fill=LIGHT_BLUE, width=1)
            
        elif dtype == "heatwave":
            # Cracked earth
            draw.line([5, 45, 45, 45], fill=BROWN, width=2)
            draw.line([15, 45, 12, 48], fill=BROWN, width=1)
            draw.line([30, 45, 33, 48], fill=BROWN, width=1)
            # Heat waves
            for x in [10, 20, 30, 40]:
                draw.arc([x-3, 15, x+3, 25], 90, 270, fill=ORANGE, width=1)
                draw.arc([x-3, 25, x+3, 35], 270, 90, fill=RED, width=1)
                
        elif dtype == "solar_wind":
            draw_sun(draw, 0, 25, 10, ORANGE, rays=True, ray_color=YELLOW)
            for y in [15, 25, 35]:
                draw.line([15, y, 45, y + 2], fill=GREEN, width=1)
                draw.line([25, y-2, 35, y-2], fill=CYAN, width=1)
                
        elif dtype == "sun_dog":
            draw_sun(draw, 25, 25, 6, YELLOW)
            draw.arc([5, 5, 45, 45], 0, 360, fill=WHITE, width=1)
            draw_sun(draw, 8, 25, 3, GOLD)
            draw_sun(draw, 42, 25, 3, GOLD)
            
        elif dtype == "crepuscular_rays":
            draw_cloud(draw, 25, 12, CLOUD_LIGHT)
            draw.polygon([(25, 12), (5, 45), (15, 45)], fill=(255, 255, 200, 100))
            draw.polygon([(25, 12), (20, 45), (30, 45)], fill=(255, 255, 200, 100))
            draw.polygon([(25, 12), (35, 45), (45, 45)], fill=(255, 255, 200, 100))
            
        elif dtype == "green_flash":
            # Ocean
            draw.rectangle([0, 35, 50, 50], fill=DARK_BLUE)
            # setting sun
            draw.ellipse([15, 20, 35, 40], fill=ORANGE)
            # green flash at top
            draw.rectangle([22, 19, 28, 22], fill=CYAN)
            
        elif dtype == "morning_sun":
            draw.polygon([(0, 45), (20, 30), (50, 45)], fill=DARK_GREY)
            draw_sun(draw, 25, 32, 8, ORANGE, rays=True, ray_color=YELLOW)
            
        elif dtype == "noon_glare":
            draw_sun(draw, 25, 25, 9, WHITE)
            draw.polygon([(25, 5), (35, 25), (25, 45), (15, 25)], fill=YELLOW)
            draw_sun(draw, 25, 25, 7, WHITE)
            
        elif dtype == "hazy_sun":
            draw_sun(draw, 25, 25, 10, YELLOW)
            draw.rectangle([5, 20, 45, 30], fill=(220, 220, 220, 150))
            
        elif dtype == "cloudy":
            draw_cloud(draw, 18, 20, CLOUD_LIGHT, shadow=SHADOW)
            draw_cloud(draw, 32, 26, WHITE, shadow=SHADOW)
            
        elif dtype == "overcast":
            draw_cloud(draw, 15, 18, DARK_GREY)
            draw_cloud(draw, 28, 22, GREY)
            draw_cloud(draw, 35, 16, DARK_GREY)
            
        elif dtype == "cirrus_clouds":
            draw.line([5, 10, 45, 25], fill=WHITE, width=2)
            draw.line([10, 20, 40, 32], fill=WHITE, width=1)
            draw.line([2, 30, 30, 42], fill=WHITE, width=1)
            
        elif dtype == "cumulus_clouds":
            draw_cloud(draw, 25, 25, WHITE, shadow=SHADOW)
            
        elif dtype == "stratus_clouds":
            draw.rectangle([5, 15, 45, 22], fill=LIGHT_GREY)
            draw.rectangle([10, 25, 40, 32], fill=GREY)
            
        elif dtype == "altocumulus":
            for x in [12, 25, 38]:
                for y in [15, 28]:
                    draw.ellipse([x-5, y-3, x+5, y+3], fill=LIGHT_GREY)
                    
        elif dtype == "noctilucent_clouds":
            draw.line([2, 15, 48, 22], fill=CYAN, width=1)
            draw.line([5, 25, 45, 18], fill=BLUE, width=1)
            draw.line([10, 32, 40, 36], fill=CYAN, width=1)
            
        elif dtype == "shelf_cloud":
            draw.polygon([(0, 15), (50, 22), (50, 32), (0, 25)], fill=DARK_GREY)
            draw.line([(0, 25), (50, 32)], fill=LIGHT_GREY, width=2)
            
        elif dtype == "roll_cloud":
            draw.rectangle([5, 20, 45, 28], fill=GREY)
            draw.line([5, 20, 45, 20], fill=WHITE, width=1)
            draw.line([5, 28, 45, 28], fill=DARK_GREY, width=1)
            
        elif dtype == "lenticular_cloud":
            draw.polygon([(10, 45), (25, 30), (40, 45)], fill=DARK_GREY)
            draw.ellipse([15, 24, 35, 28], fill=WHITE)
            draw.ellipse([12, 28, 38, 32], fill=LIGHT_GREY)
            
        elif dtype == "mammatus_clouds":
            for x in [10, 25, 40]:
                draw.ellipse([x-8, 10, x+8, 24], fill=GREY)
                draw.ellipse([x-6, 12, x+6, 26], fill=DARK_GREY)
                
        elif dtype == "thundercloud":
            draw_cloud(draw, 25, 20, DARK_GREY)
            # internal glow
            draw.ellipse([15, 15, 35, 30], fill=PURPLE)
            draw_cloud(draw, 25, 20, DARK_GREY)
            
        elif dtype == "light_rain":
            draw_cloud(draw, 25, 20, GREY, shadow=SHADOW)
            draw_rain(draw, 8, BLUE, length=4)
            
        elif dtype == "heavy_rain":
            draw_cloud(draw, 25, 20, DARK_GREY)
            draw_rain(draw, 20, BLUE, length=8)
            
        elif dtype == "sun_shower":
            draw_sun(draw, 15, 15, 8, YELLOW)
            draw_cloud(draw, 30, 22, WHITE)
            draw_rain(draw, 8, BLUE)
            
        elif dtype == "monsoon":
            draw_rain(draw, 25, BLUE, length=10)
            draw.ellipse([5, 42, 45, 48], fill=BLUE) # puddle
            draw_wind_lines(draw, LIGHT_GREY)
            
        elif dtype == "acid_rain":
            # Leaf
            draw.polygon([(15, 40), (35, 32), (45, 42), (25, 45)], fill=DARK_GREEN)
            draw.line([(35, 32), (20, 42)], fill=LIGHT_GREEN, width=1)
            # rain
            draw_rain(draw, 10, GREEN, length=5)
            
        elif dtype == "virga":
            draw_cloud(draw, 25, 16, GREY)
            # evaporating streaks
            draw.line([15, 25, 13, 30], fill=BLUE, width=1)
            draw.line([25, 25, 23, 32], fill=BLUE, width=1)
            draw.line([35, 25, 33, 28], fill=BLUE, width=1)
            
        elif dtype == "squall_line":
            draw.polygon([(0, 10), (40, 10), (15, 45), (0, 45)], fill=DARK_GREY)
            draw_rain(draw, 12, BLUE)
            
        elif dtype == "downburst":
            draw_cloud(draw, 25, 15, GREY)
            # Downward wind blast
            draw.line([20, 22, 20, 40], fill=LIGHT_BLUE, width=2)
            draw.line([25, 22, 25, 42], fill=WHITE, width=2)
            draw.line([30, 22, 30, 40], fill=LIGHT_BLUE, width=2)
            # outward blast at bottom
            draw.line([10, 42, 20, 42], fill=LIGHT_BLUE, width=1)
            draw.line([30, 42, 40, 42], fill=LIGHT_BLUE, width=1)
            
        elif dtype == "drizzle":
            draw_cloud(draw, 25, 20, LIGHT_GREY)
            import random
            random.seed(3)
            for _ in range(25):
                draw.point([random.randint(5, 45), random.randint(25, 48)], fill=LIGHT_BLUE)
                
        elif dtype == "cloudburst":
            draw_cloud(draw, 25, 15, DARK_GREY)
            draw.rectangle([15, 22, 35, 48], fill=BLUE)
            
        elif dtype == "cold_rain":
            draw_cloud(draw, 25, 20, GREY)
            draw_rain(draw, 10, BLUE)
            draw_stars(draw, 8, WHITE, seed=15) # ice flakes
            
        elif dtype == "misty_rain":
            draw.rectangle([0, 15, 50, 45], fill=(200, 200, 200, 100))
            draw_rain(draw, 10, LIGHT_BLUE)
            
        elif dtype == "thunderstorm":
            draw_cloud(draw, 25, 20, GREY, shadow=SHADOW)
            draw_lightning(draw, 25, 20, 20, 40, YELLOW)
            
        elif dtype == "severe_thunderstorm":
            draw_cloud(draw, 25, 18, DARK_GREY)
            draw_lightning(draw, 20, 18, 12, 42, YELLOW)
            draw_lightning(draw, 30, 18, 38, 40, GOLD)
            draw_rain(draw, 15, BLUE)
            
        elif dtype == "dry_thunderstorm":
            draw.line([0, 45, 50, 45], fill=BROWN, width=2)
            draw_lightning(draw, 25, 10, 15, 45, YELLOW)
            draw_lightning(draw, 30, 10, 35, 45, ORANGE)
            
        elif dtype == "heat_lightning":
            draw_cloud(draw, 25, 25, GREY)
            draw.ellipse([15, 15, 35, 35], fill=YELLOW)
            draw_cloud(draw, 25, 25, DARK_GREY)
            
        elif dtype == "ball_lightning":
            draw_stars(draw, 10, DARK_BLUE, seed=7)
            draw.ellipse([15, 15, 35, 35], fill=CYAN)
            draw.ellipse([18, 18, 32, 32], fill=WHITE)
            draw.line([12, 25, 38, 25], fill=YELLOW, width=1)
            draw.line([25, 12, 25, 38], fill=YELLOW, width=1)
            
        elif dtype == "st_elmos_fire":
            draw.rectangle([23, 25, 27, 50], fill=BROWN)
            draw.polygon([(25, 10), (20, 25), (30, 25)], fill=PURPLE)
            draw.polygon([(25, 15), (22, 25), (28, 25)], fill=CYAN)
            
        elif dtype == "lightning_strike":
            draw_lightning(draw, 40, 5, 25, 45, YELLOW)
            draw.ellipse([20, 42, 30, 48], fill=YELLOW) # strike point glow
            
        elif dtype == "sheet_lightning":
            draw.rectangle([0, 0, 50, 50], fill=YELLOW)
            draw_cloud(draw, 25, 25, DARK_GREY)
            
        elif dtype == "forked_lightning":
            draw_lightning(draw, 25, 5, 25, 25, YELLOW)
            draw_lightning(draw, 25, 25, 15, 45, YELLOW)
            draw_lightning(draw, 25, 25, 35, 45, YELLOW)
            
        elif dtype == "purple_storm":
            draw_cloud(draw, 25, 20, PURPLE)
            draw_lightning(draw, 25, 20, 28, 42, WHITE)
            
        elif dtype == "supercell":
            for r in [22, 16, 10]:
                draw.ellipse([25-r, 25-r, 25+r, 25+r], fill=DARK_GREY)
                draw.arc([25-r, 25-r, 25+r, 25+r], 0, 270, fill=LIGHT_GREY, width=2)
                
        elif dtype == "winter_lightning":
            draw_cloud(draw, 25, 20, WHITE)
            draw_snow(draw, 8, SNOW_WHITE)
            draw_lightning(draw, 25, 20, 18, 42, BLUE)
            
        elif dtype == "light_snow":
            draw_cloud(draw, 25, 20, GREY)
            draw_snow(draw, 10, WHITE)
            
        elif dtype == "heavy_snow":
            draw_cloud(draw, 25, 18, DARK_GREY)
            draw.rectangle([0, 42, 50, 50], fill=WHITE)
            draw_snow(draw, 25, WHITE)
            
        elif dtype == "blizzard":
            draw_wind_lines(draw, WHITE)
            draw_snow(draw, 35, WHITE)
            
        elif dtype == "hailstorm":
            draw_cloud(draw, 25, 18, GREY)
            import random
            random.seed(9)
            for _ in range(12):
                x = random.randint(5, 45)
                y = random.randint(22, 45)
                draw.ellipse([x-2, y-2, x+2, y+2], fill=WHITE)
                
        elif dtype == "freezing_rain":
            # Branch
            draw.line([0, 30, 50, 30], fill=BROWN, width=4)
            # icy glaze overlay
            draw.line([0, 28, 50, 28], fill=CYAN, width=1)
            draw_rain(draw, 8, BLUE)
            
        elif dtype == "diamond_dust":
            draw_sun(draw, 25, 25, 5, YELLOW)
            draw_stars(draw, 20, CYAN, seed=12)
            
        elif dtype == "frost_pattern":
            draw.line([0, 0, 15, 15], fill=WHITE, width=2)
            draw.line([0, 0, 5, 25], fill=WHITE, width=1)
            draw.line([0, 0, 25, 5], fill=WHITE, width=1)
            draw.line([50, 50, 35, 35], fill=WHITE, width=2)
            
        elif dtype == "rime_ice":
            draw.rectangle([22, 10, 28, 50], fill=BROWN)
            # Rime ice needles pointing left
            for y in range(12, 48, 4):
                draw.line([22, y, 14, y], fill=CYAN, width=2)
                
        elif dtype == "glaze_ice":
            # Red Berry
            draw.ellipse([20, 20, 30, 30], fill=RED)
            draw.line([25, 20, 25, 15], fill=BROWN, width=2)
            # Shiny Ice Glaze
            draw.arc([18, 18, 32, 32], 0, 360, fill=CYAN, width=2)
            
        elif dtype == "thundersnow":
            draw_cloud(draw, 25, 18, DARK_GREY)
            draw_snow(draw, 15, WHITE)
            draw_lightning(draw, 25, 18, 32, 42, YELLOW)
            
        elif dtype == "whiteout":
            draw.rectangle([0, 0, 50, 50], fill=LIGHT_GREY)
            draw_wind_lines(draw, WHITE)
            
        elif dtype == "ice_fog":
            draw.rectangle([0, 15, 50, 45], fill=(220, 240, 240, 150))
            draw_stars(draw, 12, CYAN, seed=99)
            
        elif dtype == "windy":
            draw_wind_lines(draw, LIGHT_BLUE)
            # green leaves
            for x, y in [(12, 18), (35, 22), (22, 35)]:
                draw.ellipse([x-2, y-2, x+2, y+2], fill=GREEN)
                
        elif dtype == "tornado":
            draw_tornado(draw, 25, 25, GREY)
            
        elif dtype == "hurricane":
            draw.ellipse([10, 10, 40, 40], outline=WHITE, width=2)
            draw.ellipse([15, 15, 35, 35], fill=BLUE)
            draw.ellipse([22, 22, 28, 28], fill=(0,0,0,0)) # eye
            draw_tornado(draw, 25, 25, WHITE)
            
        elif dtype == "cyclone":
            draw_tornado(draw, 25, 25, LIGHT_GREY)
            draw_wind_lines(draw, BLUE)
            
        elif dtype == "typhoon":
            # waves
            draw.arc([5, 35, 25, 55], 180, 360, fill=BLUE, width=3)
            draw.arc([25, 35, 45, 55], 180, 360, fill=BLUE, width=3)
            draw_wind_lines(draw, WHITE)
            
        elif dtype == "dust_devil":
            draw_tornado(draw, 25, 25, BROWN)
            
        elif dtype == "waterspout":
            draw.rectangle([0, 42, 50, 50], fill=BLUE)
            draw_cloud(draw, 25, 12, GREY)
            draw.line([25, 15, 25, 42], fill=LIGHT_BLUE, width=4)
            
        elif dtype == "gale_force_wind":
            # Bending pole/tree
            draw.line([15, 50, 35, 15], fill=BROWN, width=3)
            draw_wind_lines(draw, GREY)
            
        elif dtype == "derecho":
            draw.polygon([(0, 15), (50, 10), (50, 25), (0, 30)], fill=DARK_GREY)
            draw_wind_lines(draw, BLUE)
            
        elif dtype == "microburst":
            draw_cloud(draw, 25, 12, GREY)
            draw.rectangle([22, 15, 28, 45], fill=LIGHT_BLUE)
            draw.line([10, 45, 40, 45], fill=WHITE, width=2)
            
        elif dtype == "sea_breeze":
            draw.rectangle([0, 35, 50, 50], fill=BLUE)
            draw_wind_lines(draw, CYAN)
            
        elif dtype == "land_breeze":
            draw.rectangle([0, 35, 50, 50], fill=DARK_BLUE)
            draw_wind_lines(draw, GREY)
            
        elif dtype == "foggy":
            # Pine tree silhouette
            draw.polygon([(25, 15), (15, 45), (35, 45)], fill=DARK_GREEN)
            draw.rectangle([0, 0, 50, 50], fill=(220, 220, 220, 160)) # fog layer
            
        elif dtype == "sandstorm":
            draw.rectangle([0, 0, 50, 50], fill=BROWN)
            draw_wind_lines(draw, GOLD)
            
        elif dtype == "dust_storm":
            draw.rectangle([0, 20, 50, 50], fill=BROWN)
            draw_wind_lines(draw, LIGHT_GREY)
            
        elif dtype == "haboob":
            draw.ellipse([5, 15, 45, 55], fill=BROWN)
            draw.ellipse([20, 25, 50, 55], fill=BROWN)
            
        elif dtype == "smog":
            # Skyscrapers
            draw.rectangle([10, 20, 20, 50], fill=DARK_GREY)
            draw.rectangle([25, 15, 40, 50], fill=DARK_GREY)
            draw.rectangle([0, 0, 50, 50], fill=(200, 180, 120, 140)) # yellow smog
            
        elif dtype == "misty_morning":
            # Blue lake
            draw.rectangle([0, 35, 50, 50], fill=BLUE)
            draw.rectangle([0, 28, 50, 34], fill=(245, 245, 245, 150))
            
        elif dtype == "steam_fog":
            draw.rectangle([0, 40, 50, 50], fill=BLUE)
            draw.line([10, 40, 12, 30], fill=WHITE, width=1)
            draw.line([25, 40, 23, 28], fill=WHITE, width=1)
            draw.line([40, 40, 42, 32], fill=WHITE, width=1)
            
        elif dtype == "radiation_fog":
            draw_stars(draw, 8, WHITE)
            draw.rectangle([0, 40, 50, 50], fill=LIGHT_GREY)
            
        elif dtype == "upslope_fog":
            draw.polygon([(0, 50), (50, 25), (50, 50)], fill=GREEN)
            draw.rectangle([25, 20, 50, 35], fill=LIGHT_GREY)
            
        elif dtype == "inversion_layer":
            draw.polygon([(0, 50), (20, 35), (50, 50)], fill=DARK_GREY)
            draw.rectangle([0, 35, 50, 45], fill=LIGHT_GREY)
            
        elif dtype == "haze":
            draw.rectangle([0, 0, 50, 50], fill=(230, 220, 200, 180))
            
        elif dtype == "volcanic_ash_cloud":
            draw.polygon([(15, 50), (25, 30), (35, 50)], fill=DARK_GREY)
            draw_cloud(draw, 25, 22, (50, 50, 50, 255))
            
        elif dtype == "rainbow":
            draw_rainbow(draw, 25, 32, [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
            draw_cloud(draw, 35, 28, WHITE)
            
        elif dtype == "double_rainbow":
            draw_rainbow(draw, 25, 32, [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
            draw_rainbow(draw, 25, 36, [PURPLE, BLUE, GREEN, YELLOW, ORANGE, RED])
            
        elif dtype == "fog_bow":
            draw_rainbow(draw, 25, 32, [WHITE, LIGHT_GREY, WHITE])
            
        elif dtype == "moon_bow":
            draw_stars(draw, 6, WHITE)
            draw_rainbow(draw, 25, 32, [WHITE, LIGHT_BLUE, WHITE])
            
        elif dtype == "halo_optical":
            draw_sun(draw, 25, 25, 4, WHITE)
            draw.ellipse([10, 10, 40, 40], outline=LIGHT_BLUE, width=1)
            
        elif dtype == "glory_optical":
            draw_rainbow(draw, 25, 25, [RED, YELLOW, BLUE])
            draw.ellipse([22, 22, 28, 28], fill=DARK_GREY)
            
        elif dtype == "fata_morgana":
            draw.line([0, 35, 50, 35], fill=BLUE, width=2)
            # floating ship silhouette
            draw.rectangle([18, 25, 32, 29], fill=DARK_GREY)
            draw.line([25, 25, 25, 18], fill=DARK_GREY, width=1)
            
        elif dtype == "corona_optical":
            draw_sun(draw, 25, 25, 5, WHITE)
            draw.ellipse([15, 15, 35, 35], outline=CYAN, width=1)
            draw.ellipse([12, 12, 38, 38], outline=RED, width=1)
            
        elif dtype == "sunrise":
            draw.line([0, 40, 50, 40], fill=GREEN, width=2)
            draw_sun(draw, 25, 40, 8, ORANGE, rays=True, ray_color=YELLOW)
            
        elif dtype == "sunset":
            draw.rectangle([0, 38, 50, 50], fill=BLUE)
            draw_sun(draw, 25, 38, 8, RED, rays=True, ray_color=ORANGE)
            
        elif dtype == "cloudy_night":
            draw_stars(draw, 6, WHITE, seed=3)
            draw_crescent_moon(img, 20, 20, 10, YELLOW)
            draw_cloud(draw, 28, 26, DARK_GREY)
            
        elif dtype == "full_moon":
            draw_stars(draw, 8, WHITE, seed=4)
            draw_sun(draw, 25, 25, 12, LIGHT_GREY)
            # craters
            draw.ellipse([18, 18, 21, 21], fill=GREY)
            draw.ellipse([26, 28, 30, 32], fill=GREY)
            
        elif dtype == "solar_eclipse":
            draw_sun(draw, 25, 25, 12, YELLOW, rays=True, ray_color=GOLD)
            draw_sun(draw, 25, 25, 10, (0, 0, 0, 255))
            
        elif dtype == "lunar_eclipse":
            draw_stars(draw, 6, WHITE, seed=5)
            draw_sun(draw, 25, 25, 12, RED)
            # shadow bite
            mask = Image.new("L", (50, 50), 0)
            m_draw = ImageDraw.Draw(mask)
            m_draw.ellipse([15, 15, 45, 45], fill=255)
            img.paste(Image.new("RGBA", (50, 50), (10, 10, 20, 255)), mask=mask)
            
        elif dtype == "blood_moon":
            draw_stars(draw, 10, WHITE, seed=6)
            draw_sun(draw, 25, 25, 11, RED)
            draw.ellipse([20, 20, 23, 23], fill=(120, 20, 20, 255))
            
        elif dtype == "aurora_borealis":
            draw_stars(draw, 12, WHITE, seed=11)
            # Green curtains
            draw.polygon([(5, 40), (15, 10), (25, 12), (10, 45)], fill=GREEN)
            draw.polygon([(25, 38), (35, 8), (45, 15), (30, 42)], fill=GREEN)
            
        elif dtype == "aurora_australis":
            draw_stars(draw, 12, WHITE, seed=12)
            draw.polygon([(5, 40), (15, 10), (25, 12), (10, 45)], fill=RED)
            draw.polygon([(25, 38), (35, 8), (45, 15), (30, 42)], fill=GREEN)
            
        elif dtype == "meteor_shower":
            draw_stars(draw, 8, WHITE, seed=15)
            draw.line([10, 5, 25, 20], fill=WHITE, width=2)
            draw.line([30, 10, 42, 22], fill=WHITE, width=1)
            draw.line([5, 20, 15, 30], fill=WHITE, width=1)
            
        elif dtype == "firestorm":
            # flames
            draw.polygon([(10, 50), (15, 20), (22, 50)], fill=RED)
            draw.polygon([(20, 50), (28, 10), (35, 50)], fill=ORANGE)
            draw.polygon([(30, 50), (40, 22), (45, 50)], fill=YELLOW)
            draw_cloud(draw, 25, 15, DARK_GREY)
            
        elif dtype == "plasma_rain":
            # Sun surface
            draw.rectangle([0, 40, 50, 50], fill=ORANGE)
            draw.arc([15, 20, 35, 40], 180, 360, fill=RED, width=3)
            
        elif dtype == "cosmic_dust":
            # colorful space nebula
            draw.ellipse([5, 5, 40, 40], fill=PURPLE)
            draw.ellipse([20, 15, 45, 45], fill=CYAN)
            draw_stars(draw, 10, WHITE, seed=22)
            
        elif dtype == "space_weather":
            draw_stars(draw, 8, WHITE, seed=25)
            # particles
            for x, y in [(5, 10), (12, 22), (8, 35)]:
                draw.point([x, y], fill=CYAN)
            # shield
            draw.arc([15, 5, 35, 45], 270, 90, fill=BLUE, width=3)
            
        elif dtype == "frostbite_cold":
            draw.rectangle([15, 15, 35, 35], fill=DARK_BLUE)
            # frost crystals
            draw.line([12, 12, 38, 38], fill=CYAN, width=1)
            draw.line([12, 38, 38, 12], fill=CYAN, width=1)
            
        elif dtype == "thaw_melt":
            # icicles at top
            draw.polygon([(10, 0), (13, 0), (11, 15)], fill=CYAN)
            draw.polygon([(25, 0), (29, 0), (27, 22)], fill=WHITE)
            draw.polygon([(40, 0), (43, 0), (41, 12)], fill=CYAN)
            # water drop
            draw.ellipse([26, 32, 28, 35], fill=BLUE)
            
        elif dtype == "sand_dunes_wind":
            draw.polygon([(0, 50), (25, 35), (50, 50)], fill=BROWN)
            draw.polygon([(20, 50), (40, 40), (50, 50)], fill=GOLD)
            draw_wind_lines(draw, LIGHT_GREY)
            
        elif dtype == "morning_dew":
            # leaf
            draw.ellipse([10, 20, 40, 35], fill=GREEN)
            draw.line([10, 27, 40, 27], fill=DARK_GREEN, width=1)
            # dew drops
            draw.ellipse([18, 22, 21, 25], fill=WHITE)
            draw.ellipse([30, 24, 32, 26], fill=WHITE)

        # Quantize to max 9 colors + transparency
        alpha = img.split()[3].point(lambda p: 255 if p > 128 else 0)
        rgb = Image.new("RGB", img.size, (255, 255, 255))
        rgb.paste(img, mask=alpha)
        q = rgb.quantize(colors=9, method=Image.MEDIANCUT, dither=0)
        final = q.convert("RGBA")
        final.putalpha(alpha)
        
        path = os.path.join(OUTPUT_DIR, f"{name}_50x50.png")
        final.save(path)
    print("All 102 Weather Sprites generated successfully!")

def update_app_js():
    print("Updating app.js with weather category dataset...")
    with open("app.js", "r") as f:
        content = f.read()
        
    # Check if weather array already exists
    if "const weather = [" in content:
        print("Weather array already exists in app.js, skipping insert.")
        return
        
    # Formulate javascript array
    js_lines = []
    for item in weather_data:
        js_lines.append(f"""    {{ id: "{item['id']}", name: "{item['name']}", filename: "images/weather/{item['id']}_50x50.png", category: "weather", type: "{item['type']}", material: "{item['material']}", rarity: "{item['rarity']}", description: "{item['desc']}" }}""")
    
    js_arr_str = "const weather = [\n" + ",\n".join(js_lines) + "\n];\n\n"
    
    # Locate where to insert the weather array: right before "const allItems ="
    insert_point = content.find("const allItems =")
    if insert_point == -1:
        print("Error: Could not find 'const allItems =' in app.js!")
        return
        
    # We will insert "const weather = [...];" and also update the merge logic
    # Find the merge logic section
    merge_lines_start = content.find("// ─── Merge all collections ───")
    if merge_lines_start == -1:
        merge_lines_start = content.find("animals.forEach(a =>")
        
    # Insert weather array definition
    new_content = content[:insert_point] + js_arr_str + content[insert_point:]
    
    # Now we need to update:
    # 1. weather.forEach(w => { w.group = "weather"; });
    # 2. Add ...weather to const allItems = [...];
    
    # Let's find "const allItems = [...animals," in new_content
    all_items_match = re.search(r'const allItems = \[\s*\.\.\.animals,', new_content)
    if all_items_match:
        span_start = all_items_match.start()
        # insert "weather.forEach(w => { w.group = "weather"; });"
        new_content = new_content[:span_start] + "weather.forEach(w => { w.group = \"weather\"; });\n" + new_content[span_start:]
        
    # Find where allItems is declared and add "...weather"
    new_content = new_content.replace("...vegetables,", "...vegetables, ...weather,")
    
    with open("app.js", "w") as f:
        f.write(new_content)
    print("app.js successfully updated!")

def update_index_html():
    print("Updating index.html with weather category filter & stats...")
    with open("index.html", "r") as f:
        html = f.read()
        
    # Check if weather button already exists
    if 'id="filter-weather"' in html:
        print("Weather filter button already exists in index.html, skipping.")
        return
        
    # Add filter button
    button_target = '<button class="filter-btn" data-category="clothing" id="filter-clothing">👕 Clothing</button>'
    button_replacement = button_target + '\n                    <button class="filter-btn" data-category="weather" id="filter-weather">🌤️ Weather</button>'
    html = html.replace(button_target, button_replacement)
    
    # Update stats
    # 1. Update total showing species count from 1432 to 1784
    html = html.replace('<span class="stat-val" id="species-count">1432</span>', '<span class="stat-val" id="species-count">1784</span>')
    
    # 2. Add stat-row for Weather
    stat_target = """                    <div class="stat-row">
                        <span class="stat-label">Clothing</span>
                        <span class="stat-val">300</span>
                    </div>"""
    stat_replacement = stat_target + """\n                    <div class="stat-row">
                        <span class="stat-label">Weather</span>
                        <span class="stat-val">102</span>
                    </div>"""
    html = html.replace(stat_target, stat_replacement)
    
    with open("index.html", "w") as f:
        f.write(html)
    print("index.html successfully updated!")

def update_instructions():
    print("Updating instructions.txt...")
    with open("instructions.txt", "r") as f:
        text = f.read()
        
    # Update species counts in headers and introductory texts
    # 135 animals, 127 fruits, 200 vegetables, 270 kitchen, 200 vehicles, 250 electronics, and 250 clothing (totaling 1432 items)
    # New counts: 135 animals, 127 fruits, 200 vegetables, 270 kitchen, 350 vehicles, 300 electronics, 300 clothing, 102 weather (totaling 1784 items)
    old_intro = "135 procedural animal sprites, 127 fruit sprites, 200 vegetable sprites, 270 kitchen sprites, 200 vehicle sprites, 250 electronics sprites, and 250 clothing sprites (totaling 1432 items)"
    new_intro = "135 procedural animal sprites, 127 fruit sprites, 200 vegetable sprites, 270 kitchen sprites, 350 vehicle sprites, 300 electronics sprites, 300 clothing sprites, and 102 weather sprites (totaling 1784 items)"
    text = text.replace(old_intro, new_intro)
    text = text.replace("total of 1432 items", "total of 1784 items")
    text = text.replace("all 1432 items", "all 1784 items")
    
    # Append weather step instructions
    # Check if already updated
    if "python3 generate_weather.py" not in text:
        step_target = """The PNG sprites will be located in `images/animals/`, `images/fruits/`, `images/vegetables/`, `images/kitchen/`, `images/vehicles/`, `images/electronics/`, and `images/clothing/`."""
        step_replacement = """The PNG sprites will be located in `images/animals/`, `images/fruits/`, `images/vegetables/`, `images/kitchen/`, `images/vehicles/`, `images/electronics/`, `images/clothing/`, and `images/weather/`.
        
19. Run `generate_weather.py` in the workspace to build the 102 weather sprites (enhanced with shading, details, and unique weather conditions; <= 10 colors):
```bash
python3 generate_weather.py
```"""
        text = text.replace(step_target, step_replacement)
        
    with open("instructions.txt", "w") as f:
        f.write(text)
    print("instructions.txt successfully updated!")

if __name__ == "__main__":
    build_images()
    update_app_js()
    update_index_html()
    update_instructions()
