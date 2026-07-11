// Pixel Zoo Application Logic

// Dataset of 45 animals with metadata
const animals = [
    // 15 Original Animals
    {
        id: "panda",
        name: "Panda",
        filename: "images/animals/panda_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Bamboo Forests",
        rarity: "★★★★★",
        description: "Giant pandas are beloved icons of conservation. They are famous for their black-and-white coat and spend up to 12 hours a day munching on bamboo."
    },
    {
        id: "koala",
        name: "Koala",
        filename: "images/animals/koala_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Eucalyptus Forests",
        rarity: "★★★★★",
        description: "Native to Australia, koalas are highly specialized marsupials. They eat exclusively eucalyptus leaves and sleep up to 20 hours a day to conserve energy."
    },
    {
        id: "lion",
        name: "Lion",
        filename: "images/animals/lion_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Savanna",
        rarity: "★★★★★",
        description: "Known as the King of the Jungle, lions are social predators that live in family groups called prides. A lion's roar can be heard up to 5 miles away."
    },
    {
        id: "tiger",
        name: "Tiger",
        filename: "images/animals/tiger_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Jungle & Forests",
        rarity: "★★★★★",
        description: "Tigers are the largest of all the wild cat species. They are solitary hunters with uniquely patterned stripes that act as camouflage in the wild."
    },
    {
        id: "bear",
        name: "Bear",
        filename: "images/animals/bear_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Forests & Mountains",
        rarity: "★★★★☆",
        description: "Bears are highly intelligent mammals with an extraordinary sense of smell. They build fat reserves in autumn to sustain them through winter hibernation."
    },
    {
        id: "fox",
        name: "Fox",
        filename: "images/animals/fox_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Woodlands & Plains",
        rarity: "★★★★☆",
        description: "Foxes are resourceful, nocturnal hunters known for their cleverness. They make use of the Earth's magnetic field to accurately pounce on hidden prey."
    },
    {
        id: "dog",
        name: "Dog",
        filename: "images/animals/dog_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Domestic",
        rarity: "★★☆☆☆",
        description: "Commonly referred to as human's best friend, dogs were the first species to be domesticated. They possess exceptional social intelligence and loyalty."
    },
    {
        id: "cat",
        name: "Cat",
        filename: "images/animals/cat_50x50.png",
        category: "domestic",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Domestic",
        rarity: "★★☆☆☆",
        description: "Domestic cats are skilled hunters known for their agility, flexible bodies, and night vision. They communicate through over 100 distinct vocalizations."
    },
    {
        id: "rabbit",
        name: "Rabbit",
        filename: "images/animals/rabbit_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Meadows & Gardens",
        rarity: "★★☆☆☆",
        description: "Rabbits are small, hopping herbivores characterized by their long ears and fluffy tails. Their teeth never stop growing, requiring constant chewing."
    },
    {
        id: "monkey",
        name: "Monkey",
        filename: "images/animals/monkey_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Rainforest Canopy",
        rarity: "★★★☆☆",
        description: "Monkeys are agile tree-dwellers with highly developed brains. They live in social groups and are capable of using tools and basic math."
    },
    {
        id: "frog",
        name: "Frog",
        filename: "images/animals/frog_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Wetlands & Ponds",
        rarity: "★★★☆☆",
        description: "Frogs are diverse amphibians that undergo metamorphosis from tadpoles. They absorb water directly through their thin, permeable skin."
    },
    {
        id: "elephant",
        name: "Elephant",
        filename: "images/animals/elephant_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Savannas & Forests",
        rarity: "★★★★★",
        description: "Elephants are the largest land animals on Earth, famous for their cognitive empathy, long trunks, and tusks. They are the only mammals that cannot jump."
    },
    {
        id: "penguin",
        name: "Penguin",
        filename: "images/animals/penguin_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Antarctic Ice",
        rarity: "★★★★☆",
        description: "Penguins are flightless marine birds dressed in natural tuxedos. They are master swimmers, spending up to half of their lives hunting in freezing waters."
    },
    {
        id: "pig",
        name: "Pig",
        filename: "images/animals/pig_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Farms & Forests",
        rarity: "★★☆☆☆",
        description: "Pigs are clean, highly intelligent animals that are faster and smarter than dogs. Some can even learn to navigate simple video games using joystick controls."
    },
    {
        id: "owl",
        name: "Owl",
        filename: "images/animals/owl_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Forests & Woodlands",
        rarity: "★★★★☆",
        description: "Owls are stealthy nocturnal birds of prey. Their silent flight feathers and ability to rotate their necks 270 degrees make them deadly hunters."
    },
    
    // 30 New Generated Animals
    {
        id: "deer",
        name: "Deer",
        filename: "images/animals/deer_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Forests & Meadows",
        rarity: "★★★☆☆",
        description: "Deer are graceful quadrupeds known for their speed and agility. Male deer, or bucks, grow and shed antlers annually."
    },
    {
        id: "wolf",
        name: "Wolf",
        filename: "images/animals/wolf_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Forests & Tundra",
        rarity: "★★★★☆",
        description: "Wolves are highly social apex predators that hunt in packs. They communicate through complex vocalizations, body posture, and howling."
    },
    {
        id: "sheep",
        name: "Sheep",
        filename: "images/animals/sheep_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands & Pastures",
        rarity: "★☆☆☆☆",
        description: "Sheep are curly-coated domestic ruminants kept primarily for their wool, milk, and meat. They have a strong flocking instinct."
    },
    {
        id: "cow",
        name: "Cow",
        filename: "images/animals/cow_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Farms & Valleys",
        rarity: "★☆☆☆☆",
        description: "Cows are large, domesticated bovines. They spend a significant part of their day chewing cud and have highly social relationships with others in their herd."
    },
    {
        id: "horse",
        name: "Horse",
        filename: "images/animals/horse_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Farms & Plains",
        rarity: "★★★☆☆",
        description: "Horses are powerful, domesticated herbivores renowned for their speed, intelligence, and companionship with humans throughout history."
    },
    {
        id: "chicken",
        name: "Chicken",
        filename: "images/animals/chicken_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Farms & Yards",
        rarity: "★☆☆☆☆",
        description: "Chickens are the most common domestic fowl. They communicate using dozens of distinct calls and are descendants of the red junglefowl."
    },
    {
        id: "duck",
        name: "Duck",
        filename: "images/animals/duck_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Ponds & Lakes",
        rarity: "★★☆☆☆",
        description: "Ducks are aquatic birds with webbed feet and waterproof feathers. They filter-feed using bills equipped with tiny comb-like structures."
    },
    {
        id: "turtle",
        name: "Turtle",
        filename: "images/animals/turtle_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Ponds & Ocean",
        rarity: "★★★☆☆",
        description: "Turtles are ancient reptiles protected by a hard shell developed from their ribs. They can retreat inside their shells for defense."
    },
    {
        id: "snake",
        name: "Snake",
        filename: "images/animals/snake_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Deserts & Forests",
        rarity: "★★★☆☆",
        description: "Snakes are legless, carnivorous reptiles. They smell using their bifurcated tongues and swallow their prey whole by unhinging their jaws."
    },
    {
        id: "lizard",
        name: "Lizard",
        filename: "images/animals/lizard_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Rocks & Deserts",
        rarity: "★★★☆☆",
        description: "Lizards are cold-blooded reptiles that love basking in the sun. Some species can detach their tails to escape predators, growing them back later."
    },
    {
        id: "shark",
        name: "Shark",
        filename: "images/animals/shark_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Ocean Depths",
        rarity: "★★★★★",
        description: "Sharks are marine predators with skeletons made of cartilage instead of bone. They have multiple rows of teeth and a highly acute sense of smell."
    },
    {
        id: "whale",
        name: "Whale",
        filename: "images/animals/whale_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Planktivore",
        habitat: "Open Ocean",
        rarity: "★★★★★",
        description: "Whales are massive marine mammals. Despite their immense size, baleen whales eat tiny krill and sing complex, haunting songs underwater."
    },
    {
        id: "dolphin",
        name: "Dolphin",
        filename: "images/animals/dolphin_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Coastal Waters",
        rarity: "★★★★☆",
        description: "Dolphins are playful, highly intelligent marine mammals. They use echolocation to navigate and communicate using a language of whistles and clicks."
    },
    {
        id: "octopus",
        name: "Octopus",
        filename: "images/animals/octopus_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Coral Reefs",
        rarity: "★★★★☆",
        description: "Octopuses are incredibly intelligent invertebrates. They possess three hearts, blue blood, and can change their skin color and texture instantly to camouflage."
    },
    {
        id: "crab",
        name: "Crab",
        filename: "images/animals/crab_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Beaches & Reefs",
        rarity: "★★☆☆☆",
        description: "Crabs are decapod crustaceans covered by a thick exoskeleton. They walk sideways and are equipped with a pair of pincers called chelae."
    },
    {
        id: "spider",
        name: "Spider",
        filename: "images/animals/spider_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Caves & Gardens",
        rarity: "★★☆☆☆",
        description: "Spiders are eight-legged arachnids that spin silk webs to capture prey. They inject venom to liquefy the insides of their meals."
    },
    {
        id: "bee",
        name: "Bee",
        filename: "images/animals/bee_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Flower Meadows",
        rarity: "★★☆☆☆",
        description: "Bees are flying insects key to pollination. They build complex wax hives, dance to direct others to flowers, and produce sweet honey."
    },
    {
        id: "butterfly",
        name: "Butterfly",
        filename: "images/animals/butterfly_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Gardens & Meadows",
        rarity: "★★★☆☆",
        description: "Butterflies are beautiful flying insects with scale-covered wings. They undergo complete metamorphosis from crawling caterpillars."
    },
    {
        id: "bat",
        name: "Bat",
        filename: "images/animals/bat_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Caves & Forests",
        rarity: "★★★☆☆",
        description: "Bats are the only mammals capable of sustained, flapping flight. They use ultrasonic echolocation to find insects in pitch darkness."
    },
    {
        id: "squirrel",
        name: "Squirrel",
        filename: "images/animals/squirrel_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Woodlands & Parks",
        rarity: "★★☆☆☆",
        description: "Squirrels are bushy-tailed rodents known for burying nuts in the ground, inadvertently planting thousands of trees every year."
    },
    {
        id: "raccoon",
        name: "Raccoon",
        filename: "images/animals/raccoon_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Urban & Forests",
        rarity: "★★★☆☆",
        description: "Raccoons are medium-sized nocturnal mammals with a black 'bandit mask' around their eyes. They are extremely dextrous and wash food in water."
    },
    {
        id: "beaver",
        name: "Beaver",
        filename: "images/animals/beaver_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Rivers & Wetlands",
        rarity: "★★★☆☆",
        description: "Beavers are ecosystem engineers. Using their sharp orange teeth, they chop down trees to construct wooden dams, creating custom wetlands."
    },
    {
        id: "kangaroo",
        name: "Kangaroo",
        filename: "images/animals/kangaroo_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Australian Outback",
        rarity: "★★★★☆",
        description: "Kangaroos are large marsupials that hop on powerful back legs. Females carry their undeveloped babies, or joeys, in a front protective pouch."
    },
    {
        id: "zebra",
        name: "Zebra",
        filename: "images/animals/zebra_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Savannas & Plains",
        rarity: "★★★★☆",
        description: "Zebras are African equines immediately recognizable by their black-and-white stripes. The stripes deter biting insects and confuse predators."
    },
    {
        id: "giraffe",
        name: "Giraffe",
        filename: "images/animals/giraffe_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Savannas & Woodlands",
        rarity: "★★★★★",
        description: "Giraffes are the tallest land animals. Their extremely long necks allow them to feed on nutrient-rich acacia leaves high up in trees."
    },
    {
        id: "hippo",
        name: "Hippo",
        filename: "images/animals/hippo_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Rivers & Lakes",
        rarity: "★★★★☆",
        description: "Hippopotamuses are massive, semi-aquatic African mammals. Despite their bulky size, they can run faster than humans on land."
    },
    {
        id: "rhino",
        name: "Rhino",
        filename: "images/animals/rhino_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands & Shrublands",
        rarity: "★★★★★",
        description: "Rhinoceroses are large, armor-plated herbivores distinguished by horn structures on their snouts. Their horns are made of keratin."
    },
    {
        id: "cheetah",
        name: "Cheetah",
        filename: "images/animals/cheetah_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Savannas",
        rarity: "★★★★★",
        description: "Cheetahs are the fastest land mammals, capable of reaching speeds up to 70 mph in short bursts, thanks to flexible spines and semi-retractable claws."
    },
    {
        id: "eagle",
        name: "Eagle",
        filename: "images/animals/eagle_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Cliffs & Mountains",
        rarity: "★★★★☆",
        description: "Eagles are powerful birds of prey with incredible vision, large hooked beaks, and strong talons to capture animals from mid-air or land."
    },
    {
        id: "parrot",
        name: "Parrot",
        filename: "images/animals/parrot_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Frugivore",
        habitat: "Tropical Rainforests",
        rarity: "★★★★☆",
        description: "Parrots are colorful, mimicry-capable tropical birds. They use strong curved beaks to crack seeds and nuts and are highly sociable."
    },
    {
        id: "apple",
        name: "Apple",
        filename: "images/fruits/apple_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Sweet & Crisp",
        habitat: "Central Asia",
        rarity: "★★☆☆☆",
        description: "A crisp and sweet pome fruit. One of the most widely cultivated fruits worldwide.",
        isFruit: true
    },
    {
        id: "apricot",
        name: "Apricot",
        filename: "images/fruits/apricot_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Armenia",
        rarity: "★★★☆☆",
        description: "A soft, orange stone fruit with a velvety skin and sweet-tart flavor.",
        isFruit: true
    },
    {
        id: "avocado",
        name: "Avocado",
        filename: "images/fruits/avocado_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Rich & Buttery",
        habitat: "Mexico",
        rarity: "★★★☆☆",
        description: "A botanically large berry with a single large seed and a rich, buttery green flesh.",
        isFruit: true
    },
    {
        id: "banana",
        name: "Banana",
        filename: "images/fruits/banana_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Creamy",
        habitat: "Southeast Asia",
        rarity: "★☆☆☆☆",
        description: "An elongated, edible yellow fruit produced by large herbaceous flowering plants.",
        isFruit: true
    },
    {
        id: "blackberry",
        name: "Blackberry",
        filename: "images/fruits/blackberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Deep & Tart",
        habitat: "North America",
        rarity: "★★★☆☆",
        description: "An aggregate fruit composed of small drupelets, deep purple-black when ripe.",
        isFruit: true
    },
    {
        id: "blueberry",
        name: "Blueberry",
        filename: "images/fruits/blueberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Mild",
        habitat: "North America",
        rarity: "★★☆☆☆",
        description: "Small, indigo-colored round berries with a sweet, crown-like tip.",
        isFruit: true
    },
    {
        id: "cantaloupe",
        name: "Cantaloupe",
        filename: "images/fruits/cantaloupe_50x50.png",
        category: "melon",
        isPredator: false,
        diet: "Sweet & Musky",
        habitat: "South Asia",
        rarity: "★★★☆☆",
        description: "A netted orange-fleshed melon with a sweet, refreshing, and aromatic taste.",
        isFruit: true
    },
    {
        id: "cherry",
        name: "Cherry",
        filename: "images/fruits/cherry_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet or Sour",
        habitat: "Black Sea Region",
        rarity: "★★☆☆☆",
        description: "A small, fleshy stone fruit hanging from long stems, popular in desserts.",
        isFruit: true
    },
    {
        id: "coconut",
        name: "Coconut",
        filename: "images/fruits/coconut_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Nutty",
        habitat: "Melanesia",
        rarity: "★★★☆☆",
        description: "A large seed of a palm tree with a fibrous husk, white meat, and sweet water.",
        isFruit: true
    },
    {
        id: "cranberry",
        name: "Cranberry",
        filename: "images/fruits/cranberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Very Tart",
        habitat: "North America",
        rarity: "★★★☆☆",
        description: "Hard, red acidic berries grown on low vines in marshy peat bogs.",
        isFruit: true
    },
    {
        id: "date",
        name: "Date",
        filename: "images/fruits/date_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Rich & Honey-like",
        habitat: "Middle East",
        rarity: "★★★☆☆",
        description: "Sweet, chewy fruit of the date palm tree, often dried and consumed as a delicacy.",
        isFruit: true
    },
    {
        id: "dragonfruit",
        name: "Dragonfruit",
        filename: "images/fruits/dragonfruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Mild & Pear-like",
        habitat: "Central America",
        rarity: "★★★★☆",
        description: "Stunning pink fruit with green scales, white flesh, and tiny black seeds.",
        isFruit: true
    },
    {
        id: "durian",
        name: "Durian",
        filename: "images/fruits/durian_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Custard-like & Pungent",
        habitat: "Southeast Asia",
        rarity: "★★★★★",
        description: "The King of Fruits, famed for its large spiky shell and strong, unique aroma.",
        isFruit: true
    },
    {
        id: "fig",
        name: "Fig",
        filename: "images/fruits/fig_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Jammy",
        habitat: "Mediterranean",
        rarity: "★★★★☆",
        description: "A teardrop-shaped fruit with a soft purple skin, pink flesh, and crunchy seeds.",
        isFruit: true
    },
    {
        id: "grape",
        name: "Grape",
        filename: "images/fruits/grape_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Juicy",
        habitat: "Near East",
        rarity: "★☆☆☆☆",
        description: "Small oval fruits growing in clusters, used for juice, raisins, and wine.",
        isFruit: true
    },
    {
        id: "grapefruit",
        name: "Grapefruit",
        filename: "images/fruits/grapefruit_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Tart & Bitter",
        habitat: "Barbados",
        rarity: "★★★☆☆",
        description: "A large citrus hybrid with yellow-orange skin and tart, pink segmented flesh.",
        isFruit: true
    },
    {
        id: "guava",
        name: "Guava",
        filename: "images/fruits/guava_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Fragrant",
        habitat: "Tropical America",
        rarity: "★★★★☆",
        description: "Round green tropical fruit with a fragrant smell and pink, seed-filled center.",
        isFruit: true
    },
    {
        id: "honeydew",
        name: "Honeydew",
        filename: "images/fruits/honeydew_50x50.png",
        category: "melon",
        isPredator: false,
        diet: "Sweet & Juicy",
        habitat: "Middle East",
        rarity: "★★★☆☆",
        description: "A smooth, pale-green skinned melon with sweet, juicy light-green flesh.",
        isFruit: true
    },
    {
        id: "jackfruit",
        name: "Jackfruit",
        filename: "images/fruits/jackfruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Fruity",
        habitat: "India",
        rarity: "★★★★☆",
        description: "The largest tree-borne fruit, with a green spiky rind and sweet yellow pods.",
        isFruit: true
    },
    {
        id: "kiwi",
        name: "Kiwi",
        filename: "images/fruits/kiwi_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "China",
        rarity: "★★☆☆☆",
        description: "A fuzzy brown oval fruit with green flesh, white core, and black seeds.",
        isFruit: true
    },
    {
        id: "kumquat",
        name: "Kumquat",
        filename: "images/fruits/kumquat_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet Skin & Sour Flesh",
        habitat: "China",
        rarity: "★★★★☆",
        description: "A tiny orange citrus fruit eaten whole, skins and all.",
        isFruit: true
    },
    {
        id: "lemon",
        name: "Lemon",
        filename: "images/fruits/lemon_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Very Sour",
        habitat: "Northeast India",
        rarity: "★☆☆☆☆",
        description: "A bright yellow ellipsoidal citrus fruit, highly prized for its juice.",
        isFruit: true
    },
    {
        id: "lime",
        name: "Lime",
        filename: "images/fruits/lime_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sour & Zesty",
        habitat: "Southeast Asia",
        rarity: "★☆☆☆☆",
        description: "A green citrus fruit, rounder and slightly more bitter than lemons.",
        isFruit: true
    },
    {
        id: "lychee",
        name: "Lychee",
        filename: "images/fruits/lychee_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Floral",
        habitat: "China",
        rarity: "★★★★☆",
        description: "A red bumpy-skinned fruit with translucent white flesh and a dark seed.",
        isFruit: true
    },
    {
        id: "mango",
        name: "Mango",
        filename: "images/fruits/mango_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Tropical",
        habitat: "South Asia",
        rarity: "★★☆☆☆",
        description: "The national fruit of India, renowned for its rich orange flesh and sweet taste.",
        isFruit: true
    },
    {
        id: "mulberry",
        name: "Mulberry",
        filename: "images/fruits/mulberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Earthy",
        habitat: "Asia & North America",
        rarity: "★★★★☆",
        description: "Elongated, blackberry-like fruits that grow on fast-growing deciduous trees.",
        isFruit: true
    },
    {
        id: "nectarine",
        name: "Nectarine",
        filename: "images/fruits/nectarine_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Juicy",
        habitat: "China",
        rarity: "★★★☆☆",
        description: "A smooth-skinned peach variant with sweet, juicy yellow-orange flesh.",
        isFruit: true
    },
    {
        id: "orange",
        name: "Orange",
        filename: "images/fruits/orange_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Citrusy",
        habitat: "Southeast Asia",
        rarity: "★☆☆☆☆",
        description: "A popular round orange citrus fruit, famous for its vitamin C content.",
        isFruit: true
    },
    {
        id: "papaya",
        name: "Papaya",
        filename: "images/fruits/papaya_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Musky",
        habitat: "Mesoamerica",
        rarity: "★★★☆☆",
        description: "An elongated tropical fruit with orange flesh and hundreds of black seeds.",
        isFruit: true
    },
    {
        id: "passionfruit",
        name: "Passionfruit",
        filename: "images/fruits/passionfruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tangy & Aromatic",
        habitat: "Brazil",
        rarity: "★★★★☆",
        description: "Wrinkled purple fruit filled with aromatic, tart yellow pulp and crunchy seeds.",
        isFruit: true
    },
    {
        id: "peach",
        name: "Peach",
        filename: "images/fruits/peach_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Velvety",
        habitat: "China",
        rarity: "★★☆☆☆",
        description: "A fuzzy, soft-skinned stone fruit with sweet, juicy yellow-orange flesh.",
        isFruit: true
    },
    {
        id: "pear",
        name: "Pear",
        filename: "images/fruits/pear_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Sweet & Mellow",
        habitat: "Europe & Asia",
        rarity: "★★☆☆☆",
        description: "A teardrop-shaped pome fruit with a sweet, mild, and slightly grainy flesh.",
        isFruit: true
    },
    {
        id: "persimmon",
        name: "Persimmon",
        filename: "images/fruits/persimmon_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Honey-like & Sweet",
        habitat: "East Asia",
        rarity: "★★★★☆",
        description: "Bright orange squarish-round fruits that are sweet and honey-like when ripe.",
        isFruit: true
    },
    {
        id: "pineapple",
        name: "Pineapple",
        filename: "images/fruits/pineapple_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Acidic",
        habitat: "South America",
        rarity: "★★☆☆☆",
        description: "A large tropical fruit with a tough spiky skin and a crown of green leaves.",
        isFruit: true
    },
    {
        id: "plum",
        name: "Plum",
        filename: "images/fruits/plum_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Caucasus Region",
        rarity: "★★☆☆☆",
        description: "A smooth-skinned, deep purple stone fruit with tart skin and sweet flesh.",
        isFruit: true
    },
    {
        id: "pomegranate",
        name: "Pomegranate",
        filename: "images/fruits/pomegranate_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Persia",
        rarity: "★★★★☆",
        description: "A round red fruit containing hundreds of edible ruby-red juicy arils.",
        isFruit: true
    },
    {
        id: "pomelo",
        name: "Pomelo",
        filename: "images/fruits/pomelo_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Mild",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "The largest citrus fruit, with a very thick skin and mild, sweet segmented flesh.",
        isFruit: true
    },
    {
        id: "quince",
        name: "Quince",
        filename: "images/fruits/quince_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Aromatic & Sour",
        habitat: "Caucasus",
        rarity: "★★★★☆",
        description: "A lumpy yellow fruit related to apples and pears, usually cooked before eating.",
        isFruit: true
    },
    {
        id: "raspberry",
        name: "Raspberry",
        filename: "images/fruits/raspberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Europe & North America",
        rarity: "★★☆☆☆",
        description: "A hollow, red aggregate berry composed of small drupelets, very fragrant.",
        isFruit: true
    },
    {
        id: "starfruit",
        name: "Starfruit",
        filename: "images/fruits/starfruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tart & Juicy",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "A yellow-green ribbed fruit that creates star shapes when sliced.",
        isFruit: true
    },
    {
        id: "strawberry",
        name: "Strawberry",
        filename: "images/fruits/strawberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Fragrant",
        habitat: "Europe",
        rarity: "★☆☆☆☆",
        description: "A popular red aggregate accessory fruit with external seeds and a green cap.",
        isFruit: true
    },
    {
        id: "tangerine",
        name: "Tangerine",
        filename: "images/fruits/tangerine_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Easy to Peel",
        habitat: "Morocco",
        rarity: "★★☆☆☆",
        description: "A small, sweet citrus fruit related to oranges, but easy to peel.",
        isFruit: true
    },
    {
        id: "watermelon",
        name: "Watermelon",
        filename: "images/fruits/watermelon_50x50.png",
        category: "melon",
        isPredator: false,
        diet: "Sweet & Refreshing",
        habitat: "Southern Africa",
        rarity: "★★☆☆☆",
        description: "A massive melon with a hard green striped rind and sweet red watery flesh.",
        isFruit: true
    },
    {
        id: "star_apple",
        name: "Star Apple",
        filename: "images/fruits/star_apple_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Milky",
        habitat: "West Indies",
        rarity: "★★★★★",
        description: "A round purple tropical fruit that shows a star pattern when sliced.",
        isFruit: true
    },
    {
        id: "boysenberry",
        name: "Boysenberry",
        filename: "images/fruits/boysenberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "California",
        rarity: "★★★★☆",
        description: "A hybrid between blackberry, raspberry, dewberry, and loganberry.",
        isFruit: true
    },
    {
        id: "elderberry",
        name: "Elderberry",
        filename: "images/fruits/elderberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Earthy",
        habitat: "Europe & North America",
        rarity: "★★★★☆",
        description: "Tiny dark purple berries growing in clusters, commonly used in syrups.",
        isFruit: true
    },
    {
        id: "gooseberry",
        name: "Gooseberry",
        filename: "images/fruits/gooseberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Grape-like",
        habitat: "Eurasia",
        rarity: "★★★★☆",
        description: "Small translucent green veined berries with a sharp, tangy taste.",
        isFruit: true
    },
    {
        id: "key_lime",
        name: "Key Lime",
        filename: "images/fruits/key_lime_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Tart & Acidic",
        habitat: "Florida Keys",
        rarity: "★★★★☆",
        description: "Small, round yellow-green citrus, famous for its use in Key Lime Pie.",
        isFruit: true
    },
    {
        id: "blood_orange",
        name: "Blood Orange",
        filename: "images/fruits/blood_orange_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Raspberry-like",
        habitat: "Sicily",
        rarity: "★★★★☆",
        description: "An orange variety with dark crimson-red flesh and a raspberry-like flavor.",
        isFruit: true
    },
    {
        id: "red_currant",
        name: "Red Currant",
        filename: "images/fruits/red_currant_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Acidic",
        habitat: "Western Europe",
        rarity: "★★★★☆",
        description: "Translucent shiny red berries growing in dangling clusters.",
        isFruit: true
    },
    {
        id: "black_currant",
        name: "Black Currant",
        filename: "images/fruits/black_currant_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Strong & Woody-sweet",
        habitat: "Northern Europe",
        rarity: "★★★★☆",
        description: "Dark purple-black berries prized for their high vitamin C content.",
        isFruit: true
    },
    {
        id: "mangosteen",
        name: "Mangosteen",
        filename: "images/fruits/mangosteen_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Tangy",
        habitat: "Sundaland",
        rarity: "★★★★★",
        description: "Tropical fruit with a thick purple rind enclosing sweet, white segments.",
        isFruit: true
    },
    {
        id: "rambutan",
        name: "Rambutan",
        filename: "images/fruits/rambutan_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Juicy",
        habitat: "Southeast Asia",
        rarity: "★★★★★",
        description: "A bright red, hairy tropical fruit containing sweet, translucent white flesh.",
        isFruit: true
    },
    {
        id: "breadfruit",
        name: "Breadfruit",
        filename: "images/fruits/breadfruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Starchy & Mild",
        habitat: "South Pacific",
        rarity: "★★★★☆",
        description: "A large green textured fruit with a potato-like flavor when cooked.",
        isFruit: true
    },
    {
        id: "salak",
        name: "Snake Fruit",
        filename: "images/fruits/salak_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Acidic",
        habitat: "Indonesia",
        rarity: "★★★★★",
        description: "Known for its scaly brown skin resembling snake scales, with dry, crunchy sweet flesh.",
        isFruit: true
    },
    {
        id: "soursop",
        name: "Soursop",
        filename: "images/fruits/soursop_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Citrusy & Creamy",
        habitat: "Tropical Americas",
        rarity: "★★★★★",
        description: "A spiky green tropical fruit with white creamy pulp tasting like strawberry and pineapple.",
        isFruit: true
    },
    {
        id: "custard_apple",
        name: "Custard Apple",
        filename: "images/fruits/custard_apple_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Custard-like",
        habitat: "West Indies",
        rarity: "★★★★☆",
        description: "A green, knobby fruit with sweet, creamy white flesh and large black seeds.",
        isFruit: true
    },
    {
        id: "longan",
        name: "Longan",
        filename: "images/fruits/longan_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Musky",
        habitat: "Southern China",
        rarity: "★★★★☆",
        description: "A close relative of the lychee, featuring a tan shell and sweet, translucent flesh.",
        isFruit: true
    },
    {
        id: "medlar",
        name: "Medlar",
        filename: "images/fruits/medlar_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Rich & Apple-sauce-like",
        habitat: "Southeast Europe",
        rarity: "★★★★★",
        description: "An unusual winter fruit eaten when overripe, offering a rich applesauce-like texture.",
        isFruit: true
    },
    {
        id: "loquat",
        name: "Loquat",
        filename: "images/fruits/loquat_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Citrusy",
        habitat: "China",
        rarity: "★★★☆☆",
        description: "Small yellow stone fruits with thin skin and a flavor combining peach, citrus, and mango.",
        isFruit: true
    },
    {
        id: "bilberry",
        name: "Bilberry",
        filename: "images/fruits/bilberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Fruity",
        habitat: "Europe",
        rarity: "★★★★☆",
        description: "Dark blue wild berries related to blueberries but with dark pulp and a stronger tart flavor.",
        isFruit: true
    },
    {
        id: "cloudberry",
        name: "Cloudberry",
        filename: "images/fruits/cloudberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Honey-like",
        habitat: "Arctic Regions",
        rarity: "★★★★★",
        description: "Amber-colored wild berries prized in Nordic countries for their tart, honey-like flavor.",
        isFruit: true
    },
    {
        id: "huckleberry",
        name: "Huckleberry",
        filename: "images/fruits/huckleberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "North America",
        rarity: "★★★★☆",
        description: "Small, deep purple berries similar to wild blueberries, offering a bold sweet-tart flavor.",
        isFruit: true
    },
    {
        id: "lingonberry",
        name: "Lingonberry",
        filename: "images/fruits/lingonberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Acidic",
        habitat: "Boreal Forests",
        rarity: "★★★☆☆",
        description: "Bright red, tart berries commonly harvested in northern forests for jams and sauces.",
        isFruit: true
    },
    {
        id: "feijoa",
        name: "Feijoa",
        filename: "images/fruits/feijoa_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Aromatic & Sweet",
        habitat: "South America",
        rarity: "★★★★☆",
        description: "Also known as pineapple guava, this green egg-shaped fruit is highly aromatic and sweet.",
        isFruit: true
    },
    {
        id: "tamarind",
        name: "Tamarind",
        filename: "images/fruits/tamarind_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sour & Sweet",
        habitat: "Africa",
        rarity: "★★★☆☆",
        description: "Brown pod-like fruits containing sour-sweet pulp widely used in cooking and confections.",
        isFruit: true
    },
    {
        id: "ugli_fruit",
        name: "Ugli Fruit",
        filename: "images/fruits/ugli_fruit_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Tangy",
        habitat: "Jamaica",
        rarity: "★★★★☆",
        description: "A Jamaican tangelo with a rough, wrinkled yellow-green skin and sweet, juicy interior.",
        isFruit: true
    },
    {
        id: "clementine",
        name: "Clementine",
        filename: "images/fruits/clementine_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Seedless",
        habitat: "Mediterranean",
        rarity: "★★★☆☆",
        description: "A small, sweet hybrid mandarin orange that is virtually seedless and easy to peel.",
        isFruit: true
    },
    {
        id: "satsuma",
        name: "Satsuma",
        filename: "images/fruits/satsuma_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sweet & Juicy",
        habitat: "Japan",
        rarity: "★★★☆☆",
        description: "A seedless citrus variety with loose, easy-to-peel skin and very sweet segments.",
        isFruit: true
    },
    {
        id: "yuzu",
        name: "Yuzu",
        filename: "images/fruits/yuzu_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Highly Acidic & Aromatic",
        habitat: "East Asia",
        rarity: "★★★★☆",
        description: "A bumpy yellow citrus fruit prized for its intensely aromatic zest and sour juice.",
        isFruit: true
    },
    {
        id: "buddhas_hand",
        name: "Buddha's Hand",
        filename: "images/fruits/buddhas_hand_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Fragrant & Zesty",
        habitat: "India",
        rarity: "★★★★★",
        description: "An unusual citrus fruit with long yellow finger-like segments containing no pulp or juice.",
        isFruit: true
    },
    {
        id: "rowanberry",
        name: "Rowanberry",
        filename: "images/fruits/rowanberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Bitter & Tart",
        habitat: "Europe",
        rarity: "★★★☆☆",
        description: "Small orange-red berries growing in clusters, usually cooked or made into jellies.",
        isFruit: true
    },
    {
        id: "barberry",
        name: "Barberry",
        filename: "images/fruits/barberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Sour",
        habitat: "Asia & Europe",
        rarity: "★★★★☆",
        description: "Long, bright red berries known for their sharp, sour taste and use in rice dishes.",
        isFruit: true
    },
    {
        id: "juniper_berry",
        name: "Juniper Berry",
        filename: "images/fruits/juniper_berry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Piney & Sharp",
        habitat: "Northern Hemisphere",
        rarity: "★★★★☆",
        description: "Female seed cones resembling blue-purple berries, used as a spice for savory dishes.",
        isFruit: true
    },
    {
        id: "marionberry",
        name: "Marionberry",
        filename: "images/fruits/marionberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Rich",
        habitat: "Oregon, USA",
        rarity: "★★★★☆",
        description: "A complex blackberry cultivar with a rich, earthy, and sweet-tart flavor profile.",
        isFruit: true
    },
    {
        id: "physalis",
        name: "Physalis",
        filename: "images/fruits/physalis_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "South America",
        rarity: "★★★★☆",
        description: "Also called Cape Gooseberry, this yellow-orange berry is wrapped in a papery husk.",
        isFruit: true
    },
    {
        id: "miracle_fruit",
        name: "Miracle Fruit",
        filename: "images/fruits/miracle_fruit_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Mild",
        habitat: "West Africa",
        rarity: "★★★★★",
        description: "A small red berry containing miraculin, making sour foods taste incredibly sweet.",
        isFruit: true
    },
    {
        id: "damson",
        name: "Damson",
        filename: "images/fruits/damson_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Tart & Sweet",
        habitat: "Great Britain",
        rarity: "★★★☆☆",
        description: "A small, oval stone fruit with dark blue skin and a pleasantly tart, rich flavor.",
        isFruit: true
    },
    {
        id: "honeyberry",
        name: "Honeyberry",
        filename: "images/fruits/honeyberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Tangy",
        habitat: "Siberia",
        rarity: "★★★★☆",
        description: "Also known as Haskap, this elongated blue berry tastes like a mix of blueberry and raspberry.",
        isFruit: true
    },
    {
        id: "acai",
        name: "Acai",
        filename: "images/fruits/acai_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Earthy & Berry-like",
        habitat: "Amazon Rainforest",
        rarity: "★★★☆☆",
        description: "Small, dark purple berries packed with antioxidants, growing in clusters on palm trees.",
        isFruit: true
    },
    {
        id: "goji_berry",
        name: "Goji Berry",
        filename: "images/fruits/goji_berry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Herbaceous",
        habitat: "Himalayas",
        rarity: "★★★★☆",
        description: "Bright red-orange oblong berries, also known as wolfberries, famous for their health benefits.",
        isFruit: true
    },
    {
        id: "seabuckthorn",
        name: "Seabuckthorn",
        filename: "images/fruits/seabuckthorn_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sour & Citrusy",
        habitat: "Eurasian Coasts",
        rarity: "★★★★☆",
        description: "Small golden-orange berries that grow on thorny shrubs and have an intense citrus-like tartness.",
        isFruit: true
    },
    {
        id: "salmonberry",
        name: "Salmonberry",
        filename: "images/fruits/salmonberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Mildly Sweet",
        habitat: "North America",
        rarity: "★★★☆☆",
        description: "A raspberry-like yellow-orange wild fruit that resembles salmon roe.",
        isFruit: true
    },
    {
        id: "thimbleberry",
        name: "Thimbleberry",
        filename: "images/fruits/thimbleberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Soft",
        habitat: "North America",
        rarity: "★★★★☆",
        description: "A bright red, flat, cap-like wild berry that is incredibly soft and dissolves in the mouth.",
        isFruit: true
    },
    {
        id: "ackee",
        name: "Ackee",
        filename: "images/fruits/ackee_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Rich & Savory",
        habitat: "West Africa & Caribbean",
        rarity: "★★★★★",
        description: "Jamaica's national fruit. Its red pod opens when ripe to reveal creamy yellow arils and black seeds.",
        isFruit: true
    },
    {
        id: "langsat",
        name: "Langsat",
        filename: "images/fruits/langsat_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Slightly Sour",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "Small, translucent, segmented fruits with a thin pale-brown skin that grow in grape-like clusters.",
        isFruit: true
    },
    {
        id: "santol",
        name: "Santol",
        filename: "images/fruits/santol_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sour & Sweet",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "Also known as cotton fruit, it features a thick golden rind and pillowy white sweet pulp.",
        isFruit: true
    },
    {
        id: "jabuticaba",
        name: "Jabuticaba",
        filename: "images/fruits/jabuticaba_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Grape-like",
        habitat: "Brazil",
        rarity: "★★★★★",
        description: "A unique dark purple, grape-like fruit that grows directly on the trunk of the jabuticabeira tree.",
        isFruit: true
    },
    {
        id: "naranjilla",
        name: "Naranjilla",
        filename: "images/fruits/naranjilla_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tart & Citrusy",
        habitat: "Andes Mountains",
        rarity: "★★★★★",
        description: "A golden-orange fuzzy fruit with a green, jelly-like citrus-tasting pulp inside.",
        isFruit: true
    },
    {
        id: "cocona",
        name: "Cocona",
        filename: "images/fruits/cocona_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sour & Fruity",
        habitat: "Amazon Basin",
        rarity: "★★★★☆",
        description: "A smooth yellow-red fruit closely related to the naranjilla, used for refreshing drinks and salsas.",
        isFruit: true
    },
    {
        id: "pepino",
        name: "Pepino Melon",
        filename: "images/fruits/pepino_50x50.png",
        category: "melon",
        isPredator: false,
        diet: "Sweet & Refreshing",
        habitat: "South America",
        rarity: "★★★☆☆",
        description: "An oval cream-yellow fruit with purple stripes, tasting like a blend of honeydew and cucumber.",
        isFruit: true
    },
    {
        id: "tamarillo",
        name: "Tamarillo",
        filename: "images/fruits/tamarillo_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "Andes Mountains",
        rarity: "★★★★☆",
        description: "An egg-shaped red-orange tree tomato with a tart, complex flavor profile.",
        isFruit: true
    },
    {
        id: "canistel",
        name: "Canistel",
        filename: "images/fruits/canistel_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Musky",
        habitat: "Central America",
        rarity: "★★★★★",
        description: "Known as eggfruit, it has a rich, yellow-orange flesh with a texture resembling cooked egg yolk.",
        isFruit: true
    },
    {
        id: "sapodilla",
        name: "Sapodilla",
        filename: "images/fruits/sapodilla_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Brown Sugar Sweet",
        habitat: "Central America",
        rarity: "★★★★☆",
        description: "A brown scurfy fruit with exceptionally sweet pear-like flesh that tastes like brown sugar and pear.",
        isFruit: true
    },
    {
        id: "mamey_sapote",
        name: "Mamey Sapote",
        filename: "images/fruits/mamey_sapote_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Creamy",
        habitat: "Central America",
        rarity: "★★★★★",
        description: "A football-shaped brown fruit with creamy, vibrant orange pulp tasting of pumpkin and almond.",
        isFruit: true
    },
    {
        id: "black_sapote",
        name: "Black Sapote",
        filename: "images/fruits/black_sapote_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Custard-like",
        habitat: "Mexico",
        rarity: "★★★★★",
        description: "The chocolate pudding fruit. A green tomato-like fruit with black, pudding-like sweet flesh.",
        isFruit: true
    },
    {
        id: "white_sapote",
        name: "White Sapote",
        filename: "images/fruits/white_sapote_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Custardy",
        habitat: "Central America",
        rarity: "★★★★☆",
        description: "A yellowish-green fruit with creamy white pulp that has a flavor like banana, peach, and vanilla.",
        isFruit: true
    },
    {
        id: "cherimoya",
        name: "Cherimoya",
        filename: "images/fruits/cherimoya_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Custardy",
        habitat: "Andes Mountains",
        rarity: "★★★★★",
        description: "Mark Twain called it the most delicious fruit known. It has green scaly skin and sweet white custard pulp.",
        isFruit: true
    },
    {
        id: "monstera_deliciosa",
        name: "Monstera Deliciosa",
        filename: "images/fruits/monstera_deliciosa_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Pineapple-Banana Mix",
        habitat: "Central America",
        rarity: "★★★★★",
        description: "The fruit of the popular split-leaf houseplant, tasting like a mix of banana, pineapple, and mango.",
        isFruit: true
    },
    {
        id: "prickly_pear",
        name: "Prickly Pear",
        filename: "images/fruits/prickly_pear_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Melon-like",
        habitat: "Americas",
        rarity: "★★★☆☆",
        description: "The bright magenta/purple fruit of the opuntia cactus, sweet with small crunchy seeds.",
        isFruit: true
    },
    {
        id: "pitanga",
        name: "Pitanga",
        filename: "images/fruits/pitanga_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "South America",
        rarity: "★★★★☆",
        description: "Surinam cherry. An 8-ribbed bright red fruit shaped like a tiny pumpkin with a tart cherry-like taste.",
        isFruit: true
    },
    {
        id: "rose_apple",
        name: "Rose Apple",
        filename: "images/fruits/rose_apple_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Floral",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "Wax apple. A bell-shaped pinkish-red fruit with a crisp, watery bite and a delicate rose-water scent.",
        isFruit: true
    },
    {
        id: "jambolan",
        name: "Jambolan",
        filename: "images/fruits/jambolan_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Astringent",
        habitat: "India",
        rarity: "★★★★☆",
        description: "Java plum. An oblong shiny dark purple fruit known for its sweet, sour, and dry/mouth-puckering quality.",
        isFruit: true
    },
    {
        id: "bignay",
        name: "Bignay",
        filename: "images/fruits/bignay_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Berry-like",
        habitat: "Southeast Asia",
        rarity: "★★★★☆",
        description: "Clusters of tiny round berries that ripen from green to bright red and finally glossy black.",
        isFruit: true
    },
    {
        id: "ambarella",
        name: "Ambarella",
        filename: "images/fruits/ambarella_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sour & Crunchy",
        habitat: "Polynesia",
        rarity: "★★★★☆",
        description: "A green-yellow oval stone fruit with crunchy flesh, often eaten green with salt or chili.",
        isFruit: true
    },
    {
        id: "calamondin",
        name: "Calamondin",
        filename: "images/fruits/calamondin_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sour & Zesty",
        habitat: "Philippines",
        rarity: "★★★☆☆",
        description: "A tiny round orange-green citrus hybrid, extremely sour inside with a sweet rind.",
        isFruit: true
    },
    {
        id: "sudachi",
        name: "Sudachi",
        filename: "images/fruits/sudachi_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Very Sour",
        habitat: "Japan",
        rarity: "★★★★☆",
        description: "A small round green citrus used like lemon/lime, prized in Japanese cuisine for its distinct aroma.",
        isFruit: true
    },
    {
        id: "kabosu",
        name: "Kabosu",
        filename: "images/fruits/kabosu_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Sour & Fragrant",
        habitat: "Japan",
        rarity: "★★★★☆",
        description: "A green round citrus related to yuzu, with a sharp sour juice and a very refreshing fragrance.",
        isFruit: true
    },
    {
        id: "finger_lime",
        name: "Finger Lime",
        filename: "images/fruits/finger_lime_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Tart & Caviar-like",
        habitat: "Australia",
        rarity: "★★★★★",
        description: "The caviar lime. A long pod containing round pearl-like vesicles that pop with tart lime juice.",
        isFruit: true
    },
    {
        id: "citron",
        name: "Citron",
        filename: "images/fruits/citron_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Bitter & Sweet Rind",
        habitat: "Mediterranean",
        rarity: "★★★★☆",
        description: "A large, bumpy, thick-skinned yellow citrus, one of the original ancestral citrus species.",
        isFruit: true
    },
    {
        id: "ponderosa_lemon",
        name: "Ponderosa Lemon",
        filename: "images/fruits/ponderosa_lemon_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Tart & Juicy",
        habitat: "United States",
        rarity: "★★★★☆",
        description: "A massive lemon hybrid producing giant bumpy fruits with thick skins and abundant juice.",
        isFruit: true
    },
    {
        id: "bergamot",
        name: "Bergamot",
        filename: "images/fruits/bergamot_50x50.png",
        category: "citrus",
        isPredator: false,
        diet: "Bitter & Aromatic",
        habitat: "Italy",
        rarity: "★★★★☆",
        description: "A bumpy green-yellow citrus whose peel oil gives Earl Grey tea its signature scent and flavor.",
        isFruit: true
    },
    {
        id: "jujube",
        name: "Jujube",
        filename: "images/fruits/jujube_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Apple-like",
        habitat: "China",
        rarity: "★★★☆☆",
        description: "Red date. An oblong fruit that tastes like a sweet apple when fresh and like a date when dried.",
        isFruit: true
    },
    {
        id: "hawthorn",
        name: "Hawthorn",
        filename: "images/fruits/hawthorn_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Tangy & Sweet",
        habitat: "Eurasia",
        rarity: "★★★☆☆",
        description: "Small, red, apple-like berries used for jams, jellies, and traditional Chinese haw flakes.",
        isFruit: true
    },
    {
        id: "crabapple",
        name: "Crabapple",
        filename: "images/fruits/crabapple_50x50.png",
        category: "pome",
        isPredator: false,
        diet: "Sour & Tart",
        habitat: "Northern Hemisphere",
        rarity: "★★☆☆☆",
        description: "Miniature wild apples on long stems, very tart and high in pectin, excellent for jelly.",
        isFruit: true
    },
    {
        id: "salal_berry",
        name: "Salal Berry",
        filename: "images/fruits/salal_berry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Earthy",
        habitat: "Pacific Northwest",
        rarity: "★★★★☆",
        description: "Dark blue-black wild berries growing on evergreen shrubs, tasting sweet with a unique earthy tone.",
        isFruit: true
    },
    {
        id: "serviceberry",
        name: "Serviceberry",
        filename: "images/fruits/serviceberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Almond-like",
        habitat: "North America",
        rarity: "★★★★☆",
        description: "Juneberry. Dark purplish-blue berries resembling blueberries, but with a sweet, almond-like flavor.",
        isFruit: true
    },
    {
        id: "chokeberry",
        name: "Chokeberry",
        filename: "images/fruits/chokeberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Highly Astringent",
        habitat: "North America",
        rarity: "★★★☆☆",
        description: "Aronia. Glossy black berries with a high antioxidant content and a sharp, drying astringency.",
        isFruit: true
    },
    {
        id: "dewberry",
        name: "Dewberry",
        filename: "images/fruits/dewberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Northern Hemisphere",
        rarity: "★★★☆☆",
        description: "A close relative of blackberries that grows on trailing vines close to the forest floor.",
        isFruit: true
    },
    {
        id: "tayberry",
        name: "Tayberry",
        filename: "images/fruits/tayberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Aromatic",
        habitat: "Scotland",
        rarity: "★★★★☆",
        description: "A cross between a blackberry and a red raspberry, named after the River Tay in Scotland.",
        isFruit: true
    },
    {
        id: "loganberry",
        name: "Loganberry",
        filename: "images/fruits/loganberry_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Tart & Sweet",
        habitat: "California",
        rarity: "★★★☆☆",
        description: "An accidental hybrid of a red raspberry and a blackberry, with a deep red color and tart flavor.",
        isFruit: true
    },
    {
        id: "mulberry_white",
        name: "White Mulberry",
        filename: "images/fruits/mulberry_white_50x50.png",
        category: "berry",
        isPredator: false,
        diet: "Sweet & Honey-like",
        habitat: "East Asia",
        rarity: "★★★☆☆",
        description: "A white to pinkish sweet mulberry species, originally cultivated to feed silkworms.",
        isFruit: true
    },
    {
        id: "ice_cream_bean",
        name: "Ice Cream Bean",
        filename: "images/fruits/ice_cream_bean_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Vanilla Sweet",
        habitat: "Amazon Basin",
        rarity: "★★★★★",
        description: "A long green pod filled with fluffy, white, cottony pulp that tastes exactly like vanilla ice cream.",
        isFruit: true
    },
    {
        id: "marula",
        name: "Marula",
        filename: "images/fruits/marula_50x50.png",
        category: "stone",
        isPredator: false,
        diet: "Sweet & Tart",
        habitat: "Africa",
        rarity: "★★★★★",
        description: "A yellow plum-sized wild fruit with citrusy flesh, famous as the source of Amarula cream liqueur.",
        isFruit: true
    },
    {
        id: "baobab_fruit",
        name: "Baobab Fruit",
        filename: "images/fruits/baobab_fruit_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Tart & Powdery",
        habitat: "African Savanna",
        rarity: "★★★★★",
        description: "Large woody pods with a dry, white, powdery pulp inside that tastes like tart, citrusy chalk.",
        isFruit: true
    },
    {
        id: "cupuacu",
        name: "Cupuacu",
        filename: "images/fruits/cupuacu_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Chocolate-Pineapple",
        habitat: "Amazon Rainforest",
        rarity: "★★★★★",
        description: "A large brown fuzzy pod containing white pulp with an aroma of cocoa, pineapple, and banana.",
        isFruit: true
    },
    {
        id: "bacuri",
        name: "Bacuri",
        filename: "images/fruits/bacuri_50x50.png",
        category: "tropical",
        isPredator: false,
        diet: "Sweet & Acidic",
        habitat: "Brazil",
        rarity: "★★★★★",
        description: "A round yellow fruit with thick skin and fragrant, white pulp that is highly prized in Brazil.",
        isFruit: true
    },
    {
        id: "alligator",
        name: "Alligator",
        filename: "images/animals/alligator_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Swamps",
        rarity: "★★★☆☆",
        description: "Large reptilian predators known for their powerful jaws."
    },
    {
        id: "alpaca",
        name: "Alpaca",
        filename: "images/animals/alpaca_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Mountains",
        rarity: "★★☆☆☆",
        description: "Fluffy herd animals bred for their soft fleece."
    },
    {
        id: "ant",
        name: "Ant",
        filename: "images/animals/ant_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Everywhere",
        rarity: "★☆☆☆☆",
        description: "Tiny industrious insects that can lift many times their body weight."
    },
    {
        id: "armadillo",
        name: "Armadillo",
        filename: "images/animals/armadillo_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Deserts",
        rarity: "★★☆☆☆",
        description: "Armored mammals that can roll into a ball for defense."
    },
    {
        id: "badger",
        name: "Badger",
        filename: "images/animals/badger_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Woodlands",
        rarity: "★★★☆☆",
        description: "Fierce, burrowing mammals with striking black and white striped faces."
    },
    {
        id: "bison",
        name: "Bison",
        filename: "images/animals/bison_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Plains",
        rarity: "★★★☆☆",
        description: "Massive herd animals that roam the open prairies."
    },
    {
        id: "camel",
        name: "Camel",
        filename: "images/animals/camel_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Deserts",
        rarity: "★★★☆☆",
        description: "Desert-dwelling animals adapted to survive without water for long periods."
    },
    {
        id: "chameleon",
        name: "Chameleon",
        filename: "images/animals/chameleon_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Rainforests",
        rarity: "★★★★☆",
        description: "Reptiles famous for their ability to change skin color."
    },
    {
        id: "chimpanzee",
        name: "Chimpanzee",
        filename: "images/animals/chimpanzee_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Jungles",
        rarity: "★★★★☆",
        description: "Highly intelligent apes closely related to humans."
    },
    {
        id: "crocodile",
        name: "Crocodile",
        filename: "images/animals/crocodile_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Rivers",
        rarity: "★★★★☆",
        description: "Ancient, stealthy predators that lurk in shallow waters."
    },
    {
        id: "emu",
        name: "Emu",
        filename: "images/animals/emu_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Outback",
        rarity: "★★★☆☆",
        description: "Tall, flightless birds known for their incredible running speed."
    },
    {
        id: "falcon",
        name: "Falcon",
        filename: "images/animals/falcon_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Mountains",
        rarity: "★★★★☆",
        description: "High-speed birds of prey that dive at breakneck speeds."
    },
    {
        id: "flamingo",
        name: "Flamingo",
        filename: "images/animals/flamingo_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Lakes",
        rarity: "★★★☆☆",
        description: "Elegant wading birds with distinctive pink plumage."
    },
    {
        id: "gorilla",
        name: "Gorilla",
        filename: "images/animals/gorilla_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Jungles",
        rarity: "★★★★★",
        description: "Powerful but gentle giant apes that live in troops."
    },
    {
        id: "hedgehog",
        name: "Hedgehog",
        filename: "images/animals/hedgehog_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Gardens",
        rarity: "★★☆☆☆",
        description: "Small, spiky mammals that roll up into a prickly ball."
    },
    {
        id: "iguana",
        name: "Iguana",
        filename: "images/animals/iguana_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Tropics",
        rarity: "★★★☆☆",
        description: "Large, sun-loving lizards with a row of spines down their back."
    },
    {
        id: "jaguar",
        name: "Jaguar",
        filename: "images/animals/jaguar_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Rainforests",
        rarity: "★★★★★",
        description: "Fearsome big cats with stunning rosette patterns."
    },
    {
        id: "lemur",
        name: "Lemur",
        filename: "images/animals/lemur_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Madagascar",
        rarity: "★★★★☆",
        description: "Agile primates with long, often ringed tails."
    },
    {
        id: "leopard",
        name: "Leopard",
        filename: "images/animals/leopard_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Savannas",
        rarity: "★★★★☆",
        description: "Stealthy big cats capable of dragging prey up into trees."
    },
    {
        id: "moose",
        name: "Moose",
        filename: "images/animals/moose_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Boreal Forests",
        rarity: "★★★★☆",
        description: "The largest living species in the deer family, sporting massive antlers."
    },
    {
        id: "ostrich",
        name: "Ostrich",
        filename: "images/animals/ostrich_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Savannas",
        rarity: "★★★☆☆",
        description: "The world's largest bird, capable of running very fast."
    },
    {
        id: "panther",
        name: "Panther",
        filename: "images/animals/panther_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Jungles",
        rarity: "★★★★★",
        description: "Melanistic big cats known for their sleek black coats."
    },
    {
        id: "pelican",
        name: "Pelican",
        filename: "images/animals/pelican_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Coasts",
        rarity: "★★★☆☆",
        description: "Large water birds featuring a distinctive throat pouch."
    },
    {
        id: "sloth",
        name: "Sloth",
        filename: "images/animals/sloth_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Rainforests",
        rarity: "★★★★☆",
        description: "Extremely slow-moving mammals that spend their lives hanging in trees."
    },
    {
        id: "walrus",
        name: "Walrus",
        filename: "images/animals/walrus_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Arctic",
        rarity: "★★★★☆",
        description: "Large marine mammals recognized by their prominent tusks and whiskers."
    }
,
    {
        id: "platypus",
        name: "Platypus",
        filename: "images/animals/platypus_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Rivers",
        rarity: "★★★★★",
        description: "Semi-aquatic egg-laying mammal native to eastern Australia."
    },
    {
        id: "meerkat",
        name: "Meerkat",
        filename: "images/animals/meerkat_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Deserts",
        rarity: "★★★☆☆",
        description: "Small mongooses known for their sentinel behavior of standing on hind legs."
    },
    {
        id: "otter",
        name: "Otter",
        filename: "images/animals/otter_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Rivers & Coasts",
        rarity: "★★★★☆",
        description: "Playful semi-aquatic mammals known for holding hands while sleeping."
    },
    {
        id: "puffin",
        name: "Puffin",
        filename: "images/animals/puffin_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Cliffs & Ocean",
        rarity: "★★★★☆",
        description: "Colorfully beaked seabirds that nest in clifftop colonies."
    },
    {
        id: "capybara",
        name: "Capybara",
        filename: "images/animals/capybara_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Swamps & Rivers",
        rarity: "★★★★☆",
        description: "The largest living rodents in the world, known for their gentle and social nature."
    },
    {
        id: "seal",
        name: "Seal",
        filename: "images/animals/seal_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Polar & Coasts",
        rarity: "★★★☆☆",
        description: "Sleek marine mammals that are clumsy on land but extremely agile in water."
    },
    {
        id: "swan",
        name: "Swan",
        filename: "images/animals/swan_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Lakes & Ponds",
        rarity: "★★★☆☆",
        description: "Large, elegant waterfowl famous for their graceful necks and lifelong mating bonds."
    },
    {
        id: "goose",
        name: "Goose",
        filename: "images/animals/goose_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Farms & Ponds",
        rarity: "★★☆☆☆",
        description: "Highly territorial waterfowl known for their loud honks and guard-dog behavior."
    },
    {
        id: "donkey",
        name: "Donkey",
        filename: "images/animals/donkey_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Farms & Deserts",
        rarity: "★★☆☆☆",
        description: "Sturdy domesticated beasts of burden known for their intelligence and caution."
    },
    {
        id: "goat",
        name: "Goat",
        filename: "images/animals/goat_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Mountains & Farms",
        rarity: "★★☆☆☆",
        description: "Sure-footed herbivores famous for their climbing agility and curious eating habits."
    },
    {
        id: "yak",
        name: "Yak",
        filename: "images/animals/yak_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "High Mountains",
        rarity: "★★★★☆",
        description: "Long-haired domesticated bovines native to the Himalayan region."
    },
    {
        id: "hamster",
        name: "Hamster",
        filename: "images/animals/hamster_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands & Homes",
        rarity: "★☆☆☆☆",
        description: "Small, burrowing rodents with expandable cheek pouches used to carry food."
    },
    {
        id: "skunk",
        name: "Skunk",
        filename: "images/animals/skunk_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Forests",
        rarity: "★★★☆☆",
        description: "Mammals famous for their ability to spray a liquid with a strong, unpleasant odor."
    },
    {
        id: "peacock",
        name: "Peacock",
        filename: "images/animals/peacock_50x50.png",
        category: "domestic",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Gardens & Forests",
        rarity: "★★★★☆",
        description: "Male peafowls renowned for their iridescent blue and green tail plumage."
    },
    {
        id: "red_panda",
        name: "Red Panda",
        filename: "images/animals/red_panda_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Himalayas",
        rarity: "★★★★★",
        description: "A small reddish-brown arboreal mammal native to the eastern Himalayas."
    },
    {
        id: "wombat",
        name: "Wombat",
        filename: "images/animals/wombat_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Australian Forests",
        rarity: "★★★★☆",
        description: "A stocky, burrowing Australian marsupial known for its cube-shaped droppings."
    },
    {
        id: "echidna",
        name: "Echidna",
        filename: "images/animals/echidna_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Australia & New Guinea",
        rarity: "★★★★☆",
        description: "A spiny, egg-laying mammal with a long snout used for eating ants."
    },
    {
        id: "quokka",
        name: "Quokka",
        filename: "images/animals/quokka_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Rottnest Island",
        rarity: "★★★★★",
        description: "A small wallaby species famous for its happy, smiling facial expression."
    },
    {
        id: "tasmanian_devil",
        name: "Tasmanian Devil",
        filename: "images/animals/tasmanian_devil_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Tasmania",
        rarity: "★★★★★",
        description: "A carnivorous marsupial known for its black fur, loud screech, and strong bite."
    },
    {
        id: "anteater",
        name: "Anteater",
        filename: "images/animals/anteater_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Savannas & Forests",
        rarity: "★★★★☆",
        description: "A mammal with a long tubular snout and sticky tongue adapted for eating ants."
    },
    {
        id: "pangolin",
        name: "Pangolin",
        filename: "images/animals/pangolin_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Forests & Grasslands",
        rarity: "★★★★★",
        description: "A scaly mammal that rolls into a tight ball when threatened by predators."
    },
    {
        id: "tapir",
        name: "Tapir",
        filename: "images/animals/tapir_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Jungle & Swamps",
        rarity: "★★★★☆",
        description: "A large herbivorous mammal with a short, flexible prehensile snout."
    },
    {
        id: "okapi",
        name: "Okapi",
        filename: "images/animals/okapi_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Congo Rainforest",
        rarity: "★★★★★",
        description: "A solitary forest animal with striped legs, closely related to the giraffe."
    },
    {
        id: "hyena",
        name: "Hyena",
        filename: "images/animals/hyena_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Savanna & Plains",
        rarity: "★★★★☆",
        description: "A highly social carnivore known for its spotted coat and laughing vocalizations."
    },
    {
        id: "mongoose",
        name: "Mongoose",
        filename: "images/animals/mongoose_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Woodlands & Scrublands",
        rarity: "★★★★☆",
        description: "A small, agile carnivore famous for its ability to fight venomous snakes."
    },
    {
        id: "weasel",
        name: "Weasel",
        filename: "images/animals/weasel_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Forests & Grasslands",
        rarity: "★★★☆☆",
        description: "A slender, active predator with a long body and short legs."
    },
    {
        id: "ferret",
        name: "Ferret",
        filename: "images/animals/ferret_50x50.png",
        category: "domestic",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Domestic",
        rarity: "★★☆☆☆",
        description: "A domesticated, curious, and playful form of the European polecat."
    },
    {
        id: "mole",
        name: "Mole",
        filename: "images/animals/mole_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Insectivore",
        habitat: "Underground",
        rarity: "★★★☆☆",
        description: "A small burrowing mammal with large paws adapted for digging tunnels."
    },
    {
        id: "opossum",
        name: "Opossum",
        filename: "images/animals/opossum_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Forests & Urban Areas",
        rarity: "★★☆☆☆",
        description: "A marsupial native to North America, known for playing dead when threatened."
    },
    {
        id: "bandicoot",
        name: "Bandicoot",
        filename: "images/animals/bandicoot_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Australian Woodlands",
        rarity: "★★★★☆",
        description: "A small marsupial with a long pointed snout, native to Australia."
    },
    {
        id: "porcupine",
        name: "Porcupine",
        filename: "images/animals/porcupine_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Forests & Deserts",
        rarity: "★★★★☆",
        description: "A large rodent covered in sharp quills that detaches to defend against predators."
    },
    {
        id: "gopher",
        name: "Gopher",
        filename: "images/animals/gopher_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands",
        rarity: "★★★☆☆",
        description: "A burrowing rodent known for creating extensive underground tunnel networks."
    },
    {
        id: "groundhog",
        name: "Groundhog",
        filename: "images/animals/groundhog_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Fields & Woodlands",
        rarity: "★★★☆☆",
        description: "Also known as a woodchuck, a large ground squirrel species that hibernates."
    },
    {
        id: "chipmunk",
        name: "Chipmunk",
        filename: "images/animals/chipmunk_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Forests & Parks",
        rarity: "★★★☆☆",
        description: "A small striped ground squirrel known for storing nuts in its cheek pouches."
    },
    {
        id: "prairie_dog",
        name: "Prairie Dog",
        filename: "images/animals/prairie_dog_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands",
        rarity: "★★★☆☆",
        description: "A burrowing rodent that lives in large underground colonies called towns."
    },
    {
        id: "narwhal",
        name: "Narwhal",
        filename: "images/animals/narwhal_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Arctic Ocean",
        rarity: "★★★★★",
        description: "An Arctic whale famous for the long, spiral tusk protruding from its head."
    },
    {
        id: "manatee",
        name: "Manatee",
        filename: "images/animals/manatee_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Warm Coastal Waters",
        rarity: "★★★★☆",
        description: "A gentle, slow-moving marine mammal often called a sea cow."
    },
    {
        id: "dugong",
        name: "Dugong",
        filename: "images/animals/dugong_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Warm Coastal Waters",
        rarity: "★★★★★",
        description: "A strictly marine herbivore related to the manatee, with a fluked tail."
    },
    {
        id: "sea_lion",
        name: "Sea Lion",
        filename: "images/animals/sea_lion_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Coastal Waters",
        rarity: "★★★★☆",
        description: "An eared seal species capable of walking on all fours using its flippers."
    },
    {
        id: "orca",
        name: "Orca",
        filename: "images/animals/orca_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Oceans",
        rarity: "★★★★★",
        description: "Also known as the killer whale, a highly intelligent apex predator whale."
    },
    {
        id: "beluga",
        name: "Beluga Whale",
        filename: "images/animals/beluga_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Arctic Waters",
        rarity: "★★★★★",
        description: "An all-white Arctic whale known for its bulbous forehead and vocal nature."
    },
    {
        id: "manta_ray",
        name: "Manta Ray",
        filename: "images/animals/manta_ray_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Planktivore",
        habitat: "Tropical Oceans",
        rarity: "★★★★★",
        description: "A giant ray with large triangular pectoral fins and horn-like mouth lobes."
    },
    {
        id: "stingray",
        name: "Stingray",
        filename: "images/animals/stingray_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Coastal Ocean Floor",
        rarity: "★★★★☆",
        description: "A flat cartilaginous fish with a long venomous barb on its tail whip."
    },
    {
        id: "seahorse",
        name: "Seahorse",
        filename: "images/animals/seahorse_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Seagrass Beds",
        rarity: "★★★★☆",
        description: "A small fish species with a horse-like head and prehensile tail."
    },
    {
        id: "jellyfish",
        name: "Jellyfish",
        filename: "images/animals/jellyfish_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Oceans",
        rarity: "★★★☆☆",
        description: "A gelatinous sea creature with stinging tentacles floating in the current."
    },
    {
        id: "starfish",
        name: "Starfish",
        filename: "images/animals/starfish_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Tide Pools & Reefs",
        rarity: "★★★☆☆",
        description: "A star-shaped echinoderm that crawls on the ocean floor using tube feet."
    },
    {
        id: "lobster",
        name: "Lobster",
        filename: "images/animals/lobster_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Rocky Ocean Bottoms",
        rarity: "★★★★☆",
        description: "A bottom-dwelling marine crustacean with large powerful claws."
    },
    {
        id: "shrimp",
        name: "Shrimp",
        filename: "images/animals/shrimp_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Oceans & Rivers",
        rarity: "★★☆☆☆",
        description: "A small swimming crustacean with long antennae and a semi-translucent body."
    },
    {
        id: "squid",
        name: "Squid",
        filename: "images/animals/squid_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Deep Ocean",
        rarity: "★★★★☆",
        description: "A fast-swimming mollusk with ten tentacles and an arrow-shaped head."
    },
    {
        id: "cuttlefish",
        name: "Cuttlefish",
        filename: "images/animals/cuttlefish_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Reefs & Shallows",
        rarity: "★★★★★",
        description: "A relative of the octopus, famous for its color-changing camouflage abilities."
    },
    {
        id: "eel",
        name: "Eel",
        filename: "images/animals/eel_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Reefs & Rivers",
        rarity: "★★★☆☆",
        description: "An elongated fish resembling a snake, crawling through rocky crevasses."
    },
    {
        id: "gecko",
        name: "Gecko",
        filename: "images/animals/gecko_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Warm Regions",
        rarity: "★★★☆☆",
        description: "A small lizard known for sticky toe pads that allow it to walk on walls."
    },
    {
        id: "komodo_dragon",
        name: "Komodo Dragon",
        filename: "images/animals/komodo_dragon_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Indonesian Islands",
        rarity: "★★★★★",
        description: "The largest living species of lizard, featuring a venomous bite."
    },
    {
        id: "salamander",
        name: "Salamander",
        filename: "images/animals/salamander_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Damp Woodlands",
        rarity: "★★★★☆",
        description: "An amphibian resembling a lizard, usually with shiny black and yellow skin."
    },
    {
        id: "toad",
        name: "Toad",
        filename: "images/animals/toad_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Gardens & Forests",
        rarity: "★★☆☆☆",
        description: "A warty-skinned amphibian that lives mostly on dry land."
    },
    {
        id: "scorpion",
        name: "Scorpion",
        filename: "images/animals/scorpion_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Deserts & Forests",
        rarity: "★★★★☆",
        description: "An arachnid with pincers and a curved tail tipped with a venomous stinger."
    },
    {
        id: "centipede",
        name: "Centipede",
        filename: "images/animals/centipede_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Carnivore",
        habitat: "Soil & Leaf Litter",
        rarity: "★★★☆☆",
        description: "A fast, predatory arthropod with one pair of legs per body segment."
    },
    {
        id: "snail",
        name: "Snail",
        filename: "images/animals/snail_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Gardens & Damp Places",
        rarity: "★★☆☆☆",
        description: "A slow-moving mollusk that carries a hard coiled shell on its back."
    },
    {
        id: "ladybug",
        name: "Ladybug",
        filename: "images/animals/ladybug_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Gardens & Fields",
        rarity: "★★☆☆☆",
        description: "A small red dome-shaped beetle with black spots, beneficial for pest control."
    },
    {
        id: "dragonfly",
        name: "Dragonfly",
        filename: "images/animals/dragonfly_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Ponds & Wetlands",
        rarity: "★★★☆☆",
        description: "A fast-flying insect with large eyes and two pairs of transparent wings."
    },
    {
        id: "grasshopper",
        name: "Grasshopper",
        filename: "images/animals/grasshopper_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Meadows & Fields",
        rarity: "★★☆☆☆",
        description: "A plant-eating insect with powerful hind legs adapted for jumping."
    },
    {
        id: "mantis",
        name: "Praying Mantis",
        filename: "images/animals/mantis_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Insectivore",
        habitat: "Gardens & Shrubs",
        rarity: "★★★★☆",
        description: "A predatory insect known for holding its front legs in a praying position."
    },
    {
        id: "beetle",
        name: "Scarab Beetle",
        filename: "images/animals/beetle_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Herbivore",
        habitat: "Grasslands",
        rarity: "★★★☆☆",
        description: "A shiny green beetle family representing one of the largest insect groups."
    },
    {
        id: "firefly",
        name: "Firefly",
        filename: "images/animals/firefly_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Omnivore",
        habitat: "Wetlands & Forests",
        rarity: "★★★★☆",
        description: "An insect famous for bioluminescent tail segments that glow in the dark."
    }
];

// ─── Kitchen Items Dataset ───────────────────────────────────────────────────
const kitchen = [
    { id: "pot", name: "Pot", filename: "images/kitchen/pot_50x50.png", category: "kitchen", type: "Cookware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A versatile stainless steel cooking pot used for boiling, simmering soups, stews and pasta." },
    { id: "pan", name: "Frying Pan", filename: "images/kitchen/pan_50x50.png", category: "kitchen", type: "Cookware", material: "Cast Iron", rarity: "★★★☆☆", description: "A flat-bottomed pan ideal for frying, searing and sautéing over high heat." },
    { id: "knife", name: "Chef's Knife", filename: "images/kitchen/knife_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel + Wood", rarity: "★★★★☆", description: "An all-purpose kitchen knife used for chopping, slicing and dicing ingredients." },
    { id: "fork", name: "Fork", filename: "images/kitchen/fork_50x50.png", category: "kitchen", type: "Cutlery", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A four-tined dining utensil used for spearing and picking up food." },
    { id: "spoon", name: "Spoon", filename: "images/kitchen/spoon_50x50.png", category: "kitchen", type: "Cutlery", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A classic oval-bowled spoon for scooping liquids, soups and soft foods." },
    { id: "mug", name: "Mug", filename: "images/kitchen/mug_50x50.png", category: "kitchen", type: "Drinkware", material: "Ceramic", rarity: "★★☆☆☆", description: "A large handled cup perfect for hot drinks like coffee, tea and hot chocolate." },
    { id: "bowl", name: "Bowl", filename: "images/kitchen/bowl_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "A round open vessel used for serving soups, cereal and salads." },
    { id: "plate", name: "Plate", filename: "images/kitchen/plate_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "A flat serving dish used as the base of every meal setting." },
    { id: "kettle", name: "Kettle", filename: "images/kitchen/kettle_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★☆☆", description: "A stovetop kettle for boiling water quickly for tea, coffee and instant noodles." },
    { id: "rolling_pin", name: "Rolling Pin", filename: "images/kitchen/rolling_pin_50x50.png", category: "kitchen", type: "Bakeware", material: "Wood", rarity: "★★★☆☆", description: "A cylindrical tool used for rolling and flattening dough when baking." },
    { id: "whisk", name: "Whisk", filename: "images/kitchen/whisk_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A balloon whisk for beating eggs, cream and mixing batters with air." },
    { id: "cutting_board", name: "Cutting Board", filename: "images/kitchen/cutting_board_50x50.png", category: "kitchen", type: "Prep", material: "Wood", rarity: "★★★☆☆", description: "A sturdy wooden board providing a safe surface for chopping vegetables and meat." },
    { id: "grater", name: "Grater", filename: "images/kitchen/grater_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A box grater for shredding cheese, vegetables and citrus zest with ease." },
    { id: "oven_mitt", name: "Oven Mitt", filename: "images/kitchen/oven_mitt_50x50.png", category: "kitchen", type: "Safety", material: "Cotton", rarity: "★★☆☆☆", description: "An insulated glove that protects hands when handling hot pots and baking trays." },
    { id: "timer", name: "Kitchen Timer", filename: "images/kitchen/timer_50x50.png", category: "kitchen", type: "Tool", material: "Plastic", rarity: "★★★☆☆", description: "A mechanical countdown timer to track cooking times and avoid burnt meals." },
    { id: "spatula", name: "Spatula", filename: "images/kitchen/spatula_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Wood", rarity: "★★★☆☆", description: "A broad flat blade for flipping pancakes, burgers and sautéed vegetables." },
    { id: "colander", name: "Colander", filename: "images/kitchen/colander_50x50.png", category: "kitchen", type: "Prep", material: "Stainless Steel", rarity: "★★★☆☆", description: "A perforated bowl for draining pasta, washing produce and straining liquids." },
    { id: "ladle", name: "Ladle", filename: "images/kitchen/ladle_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A deep-bowled long-handled spoon for serving soups, stews and sauces." },
    { id: "toaster", name: "Toaster", filename: "images/kitchen/toaster_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★☆☆", description: "A compact electric appliance for toasting bread slices to golden perfection." },
    { id: "blender", name: "Blender", filename: "images/kitchen/blender_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★★☆", description: "A countertop blender for creating smoothies, soups, sauces and crushed ice drinks." },
    { id: "pot_lid", name: "Pot Lid", filename: "images/kitchen/pot_lid_50x50.png", category: "kitchen", type: "Cookware", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A tight-fitting lid that traps steam to cook food faster and retain moisture." },
    { id: "wooden_spoon", name: "Wooden Spoon", filename: "images/kitchen/wooden_spoon_50x50.png", category: "kitchen", type: "Utensil", material: "Wood", rarity: "★★☆☆☆", description: "A gentle non-scratch stirring spoon ideal for non-stick pots and jams." },
    { id: "cheese_grater", name: "Cheese Grater", filename: "images/kitchen/cheese_grater_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A pyramid-style grater with sharp rasps perfectly sized for hard cheeses." },
    { id: "tongs", name: "Tongs", filename: "images/kitchen/tongs_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "Spring-loaded tongs for safely gripping hot meats, pasta and salad ingredients." },
    { id: "measuring_cup", name: "Measuring Cup", filename: "images/kitchen/measuring_cup_50x50.png", category: "kitchen", type: "Bakeware", material: "Glass", rarity: "★★★☆☆", description: "A clear glass measuring cup for accurately portioning liquids and ingredients." },
    { id: "salt_shaker", name: "Salt Shaker", filename: "images/kitchen/salt_shaker_50x50.png", category: "kitchen", type: "Condiment", material: "Glass", rarity: "★★☆☆☆", description: "A classic salt shaker for seasoning food at the table with a precise sprinkle." },
    { id: "pepper_shaker", name: "Pepper Shaker", filename: "images/kitchen/pepper_shaker_50x50.png", category: "kitchen", type: "Condiment", material: "Glass", rarity: "★★☆☆☆", description: "A matching pepper shaker that pairs with the salt shaker as a table staple." },
    { id: "wine_glass", name: "Wine Glass", filename: "images/kitchen/wine_glass_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★★☆☆", description: "An elegant stemmed glass designed to aerate and enhance the flavour of wine." },
    { id: "glass", name: "Tumbler", filename: "images/kitchen/glass_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★☆☆☆", description: "A sturdy straight-sided tumbler for water, juice and cold beverages over ice." },
    { id: "cheese", name: "Cheese Block", filename: "images/kitchen/cheese_50x50.png", category: "kitchen", type: "Food", material: "Dairy", rarity: "★★★☆☆", description: "A yellow wedge of aged cheese with distinctive holes — a kitchen pantry staple." },
    { id: "bread", name: "Bread Loaf", filename: "images/kitchen/bread_50x50.png", category: "kitchen", type: "Food", material: "Wheat", rarity: "★★☆☆☆", description: "A freshly baked loaf of bread with a golden-brown crust and soft interior." },
    { id: "dough", name: "Dough", filename: "images/kitchen/dough_50x50.png", category: "kitchen", type: "Food", material: "Flour", rarity: "★★☆☆☆", description: "A flat round of lightly floured dough ready to be rolled, cut and baked." },
    { id: "apron", name: "Apron", filename: "images/kitchen/apron_50x50.png", category: "kitchen", type: "Safety", material: "Cotton", rarity: "★★☆☆☆", description: "A kitchen apron that keeps clothes clean while cooking and protects against splashes." },
    { id: "strainer", name: "Strainer", filename: "images/kitchen/strainer_50x50.png", category: "kitchen", type: "Prep", material: "Stainless Steel", rarity: "★★★☆☆", description: "A fine-mesh strainer for sifting flour, straining stocks and rinsing small grains." },
    { id: "mortar_pestle", name: "Mortar & Pestle", filename: "images/kitchen/mortar_pestle_50x50.png", category: "kitchen", type: "Prep", material: "Stone", rarity: "★★★★☆", description: "An ancient grinding tool for crushing spices, herbs and garlic into fine pastes." },
    { id: "garlic_press", name: "Garlic Press", filename: "images/kitchen/garlic_press_50x50.png", category: "kitchen", type: "Utensil", material: "Steel", rarity: "★★★☆☆", description: "A hinged press that minces garlic cloves quickly without the need for a knife." },
    { id: "bottle_opener", name: "Bottle Opener", filename: "images/kitchen/bottle_opener_50x50.png", category: "kitchen", type: "Tool", material: "Steel", rarity: "★★☆☆☆", description: "A dual-purpose opener for popping bottle caps and uncorking wine bottles." },
    { id: "can_opener", name: "Can Opener", filename: "images/kitchen/can_opener_50x50.png", category: "kitchen", type: "Tool", material: "Steel", rarity: "★★★☆☆", description: "A manual rotary can opener with a serrated cutting wheel for opening tins safely." },
    { id: "sponge", name: "Kitchen Sponge", filename: "images/kitchen/sponge_50x50.png", category: "kitchen", type: "Cleaning", material: "Foam", rarity: "★☆☆☆☆", description: "A soft absorbent sponge for washing up dishes, pots and surfaces with soapy water." },
    { id: "dish_rack", name: "Dish Rack", filename: "images/kitchen/dish_rack_50x50.png", category: "kitchen", type: "Cleaning", material: "Steel", rarity: "★★☆☆☆", description: "A wire drying rack that holds plates, bowls and glasses upright to air-dry." },
    { id: "cookbook", name: "Cookbook", filename: "images/kitchen/cookbook_50x50.png", category: "kitchen", type: "Tool", material: "Paper", rarity: "★★★☆☆", description: "A recipe book packed with culinary inspiration and step-by-step cooking guides." },
    { id: "sugar_jar", name: "Sugar Jar", filename: "images/kitchen/sugar_jar_50x50.png", category: "kitchen", type: "Storage", material: "Glass", rarity: "★★☆☆☆", description: "A sealed glass jar for storing sugar, keeping it fresh and dry on the counter." },
    { id: "coffee_pot", name: "Coffee Pot", filename: "images/kitchen/coffee_pot_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★☆☆", description: "A stovetop coffee pot for brewing rich, aromatic coffee the old-fashioned way." },
    { id: "peeler", name: "Peeler", filename: "images/kitchen/peeler_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Plastic", rarity: "★★★☆☆", description: "A Y-shaped vegetable peeler for quickly removing skins from carrots, potatoes and apples." },
    { id: "mixing_bowl", name: "Mixing Bowl", filename: "images/kitchen/mixing_bowl_50x50.png", category: "kitchen", type: "Bakeware", material: "Ceramic", rarity: "★★★☆☆", description: "A large deep bowl for mixing dough, batters, salads and marinated ingredients." },
    { id: "bread_knife", name: "Bread Knife", filename: "images/kitchen/bread_knife_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel + Wood", rarity: "★★★☆☆", description: "A long serrated knife designed to cleanly slice through crusty bread and soft cakes." },
    { id: "trivet", name: "Trivet", filename: "images/kitchen/trivet_50x50.png", category: "kitchen", type: "Safety", material: "Wood", rarity: "★★☆☆☆", description: "A hexagonal trivet that protects countertops from hot pots and pans." },
    { id: "plate_cover", name: "Plate Cover", filename: "images/kitchen/plate_cover_50x50.png", category: "kitchen", type: "Serveware", material: "Steel", rarity: "★★★☆☆", description: "A polished domed cover for keeping plated food warm and presentation-ready." },
    { id: "juicer", name: "Juicer", filename: "images/kitchen/juicer_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A citrus juicer for extracting fresh juice from oranges, lemons and limes." },
    { id: "chopsticks", name: "Chopsticks", filename: "images/kitchen/chopsticks_50x50.png", category: "kitchen", type: "Cutlery", material: "Bamboo", rarity: "★★★☆☆", description: "Traditional East Asian eating utensils used for picking up food with precision." },
    { id: "wok", name: "Wok", filename: "images/kitchen/wok_50x50.png", category: "kitchen", type: "Cookware", material: "Carbon Steel", rarity: "★★★★☆", description: "A round-bottomed wok for stir-frying at high heat, a staple of Asian cooking." },
    { id: "waffle_iron", name: "Waffle Iron", filename: "images/kitchen/waffle_iron_50x50.png", category: "kitchen", type: "Appliance", material: "Cast Iron", rarity: "★★★☆☆", description: "A hinged iron press that cooks batter into crisp golden waffles with a grid pattern." },
    { id: "ice_cream_scoop", name: "Ice Cream Scoop", filename: "images/kitchen/ice_cream_scoop_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A spring-loaded scoop for portioning perfect balls of ice cream and sorbet." },
    { id: "pizza_cutter", name: "Pizza Cutter", filename: "images/kitchen/pizza_cutter_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel + Plastic", rarity: "★★★☆☆", description: "A rotating wheel blade for slicing pizzas and flatbreads cleanly in one roll." },
    { id: "meat_tenderizer", name: "Meat Tenderizer", filename: "images/kitchen/meat_tenderizer_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Wood", rarity: "★★★☆☆", description: "A mallet with a spiked face for pounding and tenderizing tough cuts of meat." },
    { id: "kitchen_scale", name: "Kitchen Scale", filename: "images/kitchen/kitchen_scale_50x50.png", category: "kitchen", type: "Tool", material: "Plastic + Steel", rarity: "★★★★☆", description: "A digital kitchen scale for precisely weighing ingredients when baking." },
    { id: "slotted_spoon", name: "Slotted Spoon", filename: "images/kitchen/slotted_spoon_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A spoon with drainage holes for lifting solid foods out of boiling liquid." },
    { id: "pastry_brush", name: "Pastry Brush", filename: "images/kitchen/pastry_brush_50x50.png", category: "kitchen", type: "Bakeware", material: "Wood + Bristle", rarity: "★★☆☆☆", description: "A soft-bristled brush for glazing pastries, basting meats and buttering pans." },
    { id: "melon_baller", name: "Melon Baller", filename: "images/kitchen/melon_baller_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A small hemispherical scoop for carving decorative fruit balls from melons." },
    { id: "zester", name: "Zester", filename: "images/kitchen/zester_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Plastic", rarity: "★★★☆☆", description: "A fine-toothed grater for scraping citrus zest and grating hard spices like nutmeg." },
    { id: "mandoline_slicer", name: "Mandoline Slicer", filename: "images/kitchen/mandoline_slicer_50x50.png", category: "kitchen", type: "Prep", material: "Steel + Plastic", rarity: "★★★★☆", description: "An angled slicing board with an ultra-sharp blade for razor-thin uniform cuts." },
    { id: "stockpot", name: "Stockpot", filename: "images/kitchen/stockpot_50x50.png", category: "kitchen", type: "Cookware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A tall large-capacity pot for making stocks, broths, soups and boiling lobster." },
    { id: "skillet", name: "Cast Iron Skillet", filename: "images/kitchen/skillet_50x50.png", category: "kitchen", type: "Cookware", material: "Cast Iron", rarity: "★★★★☆", description: "A heavy cast iron skillet that retains heat perfectly for searing and baking." },
    { id: "dutch_oven", name: "Dutch Oven", filename: "images/kitchen/dutch_oven_50x50.png", category: "kitchen", type: "Cookware", material: "Enameled Cast Iron", rarity: "★★★★★", description: "A heavy enameled pot ideal for slow braises, roasts and baking artisan bread." },
    { id: "salad_spinner", name: "Salad Spinner", filename: "images/kitchen/salad_spinner_50x50.png", category: "kitchen", type: "Prep", material: "Plastic", rarity: "★★★☆☆", description: "A pump-driven spinner that uses centrifugal force to dry freshly washed salad greens." },
    { id: "egg_cup", name: "Egg Cup", filename: "images/kitchen/egg_cup_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "A small cup that holds a soft-boiled egg upright for easy dipping with toast soldiers." },
    { id: "butter_dish", name: "Butter Dish", filename: "images/kitchen/butter_dish_50x50.png", category: "kitchen", type: "Storage", material: "Glass", rarity: "★★☆☆☆", description: "A covered glass dish that keeps a block of butter fresh and spreadable on the counter." },
    { id: "bread_box", name: "Bread Box", filename: "images/kitchen/bread_box_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★★☆☆", description: "A ventilated wooden box that keeps bread fresh longer by regulating humidity." },
    { id: "spice_rack", name: "Spice Rack", filename: "images/kitchen/spice_rack_50x50.png", category: "kitchen", type: "Storage", material: "Wood + Glass", rarity: "★★★☆☆", description: "A wall-mounted rack holding rows of labelled spice jars for quick access while cooking." },
    { id: "kitchen_towel", name: "Kitchen Towel", filename: "images/kitchen/kitchen_towel_50x50.png", category: "kitchen", type: "Cleaning", material: "Cotton", rarity: "★☆☆☆☆", description: "A striped cotton towel for drying hands, wiping surfaces and handling hot dishes." },
    { id: "microwave", name: "Microwave Oven", filename: "images/kitchen/microwave_50x50.png", category: "kitchen", type: "Appliance", material: "Steel + Glass", rarity: "★★★☆☆", description: "An electric oven that heats and cooks food by exposing it to electromagnetic radiation." },
    { id: "coffee_maker", name: "Coffee Maker", filename: "images/kitchen/coffee_maker_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Glass", rarity: "★★★☆☆", description: "A drip coffee maker that brews hot coffee automatically into a glass carafe." },
    { id: "espresso_machine", name: "Espresso Machine", filename: "images/kitchen/espresso_machine_50x50.png", category: "kitchen", type: "Appliance", material: "Stainless Steel", rarity: "★★★★★", description: "A high-pressure machine that brews concentrated espresso coffee." },
    { id: "tea_infuser", name: "Tea Infuser", filename: "images/kitchen/tea_infuser_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A perforated metal ball for steeping loose tea leaves in a cup of hot water." },
    { id: "garbage_can", name: "Trash Can", filename: "images/kitchen/garbage_can_50x50.png", category: "kitchen", type: "Storage", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A step-pedal trash can for disposing of kitchen waste cleanly." },
    { id: "paper_towel_holder", name: "Paper Towel Holder", filename: "images/kitchen/paper_towel_holder_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★☆☆☆", description: "A standing wooden holder for keeping a roll of paper towels handy on the counter." },
    { id: "dish_soap", name: "Dish Soap", filename: "images/kitchen/dish_soap_50x50.png", category: "kitchen", type: "Cleaning", material: "Plastic", rarity: "★☆☆☆☆", description: "A bottle of liquid dishwashing soap for cleaning plates, cups, and pans." },
    { id: "steel_wool", name: "Steel Wool Pad", filename: "images/kitchen/steel_wool_50x50.png", category: "kitchen", type: "Cleaning", material: "Steel", rarity: "★☆☆☆☆", description: "A wire sponge scrubber for scouring tough grease and burnt food off pots." },
    { id: "funnel", name: "Kitchen Funnel", filename: "images/kitchen/funnel_50x50.png", category: "kitchen", type: "Utensil", material: "Plastic", rarity: "★★☆☆☆", description: "A wide-mouthed cone funnel for transferring liquids into narrow jars." },
    { id: "ice_cube_tray", name: "Ice Cube Tray", filename: "images/kitchen/ice_cube_tray_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★★☆☆☆", description: "A flexible plastic tray for freezing water into ice cubes." },
    { id: "corkscrew", name: "Corkscrew", filename: "images/kitchen/corkscrew_50x50.png", category: "kitchen", type: "Tool", material: "Steel + Wood", rarity: "★★★☆☆", description: "A T-shaped tool with a spiral metal screw for drawing corks from bottles." },
    { id: "nutcracker", name: "Nutcracker", filename: "images/kitchen/nutcracker_50x50.png", category: "kitchen", type: "Tool", material: "Steel", rarity: "★★★☆☆", description: "A heavy-duty hand tool designed to crack open hard shells of walnuts and pecans." },
    { id: "egg_timer", name: "Egg Timer", filename: "images/kitchen/egg_timer_50x50.png", category: "kitchen", type: "Tool", material: "Wood + Glass", rarity: "★★★☆☆", description: "A classic sand hourglass for timing eggs and cooking tasks precisely." },
    { id: "garlic_peeler", name: "Garlic Peeler", filename: "images/kitchen/garlic_peeler_50x50.png", category: "kitchen", type: "Utensil", material: "Silicone", rarity: "★★☆☆☆", description: "A flexible silicone tube that removes garlic skin when rolled under pressure." },
    { id: "honey_dipper", name: "Honey Dipper", filename: "images/kitchen/honey_dipper_50x50.png", category: "kitchen", type: "Utensil", material: "Wood", rarity: "★★★☆☆", description: "A grooved wooden wand for drizzling honey without creating a sticky mess." },
    { id: "oil_dispenser", name: "Oil Dispenser", filename: "images/kitchen/oil_dispenser_50x50.png", category: "kitchen", type: "Storage", material: "Glass + Metal", rarity: "★★★☆☆", description: "A glass bottle with a metal spout for pouring olive oil smoothly." },
    { id: "thermos", name: "Thermos Flask", filename: "images/kitchen/thermos_50x50.png", category: "kitchen", type: "Storage", material: "Stainless Steel", rarity: "★★★☆☆", description: "An insulated flask that keeps hot soup or coffee warm for hours." },
    { id: "bento_box", name: "Bento Box", filename: "images/kitchen/bento_box_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★★★☆☆", description: "A divided lunch container for packing neat, portion-controlled meals." },
    { id: "cake_stand", name: "Cake Stand", filename: "images/kitchen/cake_stand_50x50.png", category: "kitchen", type: "Serveware", material: "Steel + Glass", rarity: "★★★★☆", description: "A pedestal serving stand with a glass dome for displaying cakes and pies." },
    { id: "cookie_cutter", name: "Cookie Cutter", filename: "images/kitchen/cookie_cutter_50x50.png", category: "kitchen", type: "Bakeware", material: "Metal", rarity: "★★☆☆☆", description: "A star-shaped metal mold for cutting shapes out of cookie dough." },
    { id: "muffin_tin", name: "Muffin Tin", filename: "images/kitchen/muffin_tin_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel", rarity: "★★★☆☆", description: "A multi-cup baking pan for baking cupcakes, muffins, and mini quiches." },
    { id: "baking_sheet", name: "Baking Sheet", filename: "images/kitchen/baking_sheet_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel", rarity: "★★★☆☆", description: "A flat sheet pan for baking cookies, pastries, and roasting vegetables." },
    { id: "cooling_rack", name: "Cooling Rack", filename: "images/kitchen/cooling_rack_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel", rarity: "★★★☆☆", description: "A wire rack that allows air to circulate around hot baked goods to cool them." },
    { id: "piping_bag", name: "Piping Bag", filename: "images/kitchen/piping_bag_50x50.png", category: "kitchen", type: "Bakeware", material: "Plastic + Metal", rarity: "★★★☆☆", description: "A cone pastry bag with a metal tip for decorating cakes with icing." },
    { id: "pastry_wheel", name: "Pastry Wheel", filename: "images/kitchen/pastry_wheel_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Wood", rarity: "★★★☆☆", description: "A fluted wheel cutter for crimping and cutting dough for ravioli or pies." },
    { id: "egg_separator", name: "Egg Separator", filename: "images/kitchen/egg_separator_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A slot-designed spoon that separates egg whites from the yolk." },
    { id: "garlic_keeper", name: "Garlic Keeper", filename: "images/kitchen/garlic_keeper_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★★☆☆", description: "A ventilated ceramic jar that keeps garlic bulbs fresh and dry." },
    { id: "trivet_silicone", name: "Silicone Trivet", filename: "images/kitchen/trivet_silicone_50x50.png", category: "kitchen", type: "Safety", material: "Silicone", rarity: "★★☆☆☆", description: "A heat-resistant silicone hot pad for protecting tables from hot cookware." },
    { id: "grill_pan", name: "Grill Pan", filename: "images/kitchen/grill_pan_50x50.png", category: "kitchen", type: "Cookware", material: "Cast Iron", rarity: "★★★★☆", description: "A square pan with raised ridges that sear beautiful grill marks onto meats." },
    { id: "double_boiler", name: "Double Boiler", filename: "images/kitchen/double_boiler_50x50.png", category: "kitchen", type: "Cookware", material: "Stainless Steel", rarity: "★★★★☆", description: "A nested pot setup that uses steam to melt chocolate or prepare delicate sauces." },
    { id: "pressure_cooker", name: "Pressure Cooker", filename: "images/kitchen/pressure_cooker_50x50.png", category: "kitchen", type: "Cookware", material: "Stainless Steel", rarity: "★★★★☆", description: "A sealed cooking pot that cooks food rapidly using high-pressure steam." },
    { id: "slow_cooker", name: "Slow Cooker", filename: "images/kitchen/slow_cooker_50x50.png", category: "kitchen", type: "Appliance", material: "Ceramic + Steel", rarity: "★★★★☆", description: "A countertop appliance used for simmering food at low temperatures for hours." },
    { id: "air_fryer", name: "Air Fryer", filename: "images/kitchen/air_fryer_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★★☆", description: "A rapid hot air convection oven that mimics deep-frying without oil." },
    { id: "food_processor", name: "Food Processor", filename: "images/kitchen/food_processor_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★★☆", description: "A motorized kitchen appliance used for chopping, pureeing, and mixing ingredients." },
    { id: "hand_mixer", name: "Hand Mixer", filename: "images/kitchen/hand_mixer_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A handheld electric mixer with rotating beaters for whipping cream and eggs." },
    { id: "stand_mixer", name: "Stand Mixer", filename: "images/kitchen/stand_mixer_50x50.png", category: "kitchen", type: "Appliance", material: "Cast Metal", rarity: "★★★★★", description: "A powerful stationary stand mixer equipped with a large bowl and dough hooks." },
    { id: "crepe_pan", name: "Crepe Pan", filename: "images/kitchen/crepe_pan_50x50.png", category: "kitchen", type: "Cookware", material: "Cast Iron", rarity: "★★★★☆", description: "A flat, heavy pan with very low rims for flipping and cooking thin crepes." },
    { id: "fondue_pot", name: "Fondue Pot", filename: "images/kitchen/fondue_pot_50x50.png", category: "kitchen", type: "Cookware", material: "Ceramic + Steel", rarity: "★★★★☆", description: "A communal heated pot for keeping cheese or chocolate melted for dipping." },
    { id: "sushi_mat", name: "Sushi Mat", filename: "images/kitchen/sushi_mat_50x50.png", category: "kitchen", type: "Prep", material: "Bamboo", rarity: "★★☆☆☆", description: "A flexible bamboo mat used for rolling sushi rolls tightly and neatly." },
    { id: "tea_cozy", name: "Tea Cozy", filename: "images/kitchen/tea_cozy_50x50.png", category: "kitchen", type: "Safety", material: "Cotton", rarity: "★★★☆☆", description: "An insulated fabric cover placed over a teapot to keep the tea warm." },
    { id: "bread_lame", name: "Bread Lame", filename: "images/kitchen/bread_lame_50x50.png", category: "kitchen", type: "Prep", material: "Wood + Steel", rarity: "★★★★☆", description: "A handle holding a thin razor blade used for scoring decorative cuts on bread dough." },
    { id: "cherry_pitter", name: "Cherry Pitter", filename: "images/kitchen/cherry_pitter_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A pliers-like tool for plunging the pit out of fresh cherries and olives." },
    { id: "butter_curler", name: "Butter Curler", filename: "images/kitchen/butter_curler_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Wood", rarity: "★★★☆☆", description: "A decorative kitchen utensil used for creating scrolls or curls of butter." },
    { id: "gravy_boat", name: "Gravy Boat", filename: "images/kitchen/gravy_boat_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "An elongated jug with a handle and spout for serving sauce or gravy." },
    { id: "salt_pig", name: "Salt Pig", filename: "images/kitchen/salt_pig_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★★☆☆", description: "A pottery jar with a wide, open snout for keeping salt dry and easy to pinch." },
    { id: "pepper_mill", name: "Pepper Mill", filename: "images/kitchen/pepper_mill_50x50.png", category: "kitchen", type: "Tool", material: "Wood", rarity: "★★★☆☆", description: "A wooden grinder that cracks fresh peppercorns over food." },
    { id: "cheese_board", name: "Cheese Board", filename: "images/kitchen/cheese_board_50x50.png", category: "kitchen", type: "Serveware", material: "Slate", rarity: "★★★★☆", description: "A dark slate board used for presenting cheeses, crackers, and fruits." },
    { id: "knife_block", name: "Knife Block", filename: "images/kitchen/knife_block_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★★☆☆", description: "A heavy slotted wooden block for storing kitchen knives safely on the counter." },
    { id: "trivet_cast_iron", name: "Cast Iron Trivet", filename: "images/kitchen/trivet_cast_iron_50x50.png", category: "kitchen", type: "Safety", material: "Cast Iron", rarity: "★★★☆☆", description: "An ornate metal hot stand designed to keep piping hot pots off the table." },
    { id: "matchbox", name: "Matchbox", filename: "images/kitchen/matchbox_50x50.png", category: "kitchen", type: "Tool", material: "Paper", rarity: "★☆☆☆☆", description: "A sliding cardboard box containing safety matches for lighting gas stoves." },
    { id: "egg_slicer", name: "Egg Slicer", filename: "images/kitchen/egg_slicer_50x50.png", category: "kitchen", type: "Prep", material: "White Plastic", rarity: "★★☆☆☆", description: "A simple mechanical slicer with fine wire blades to slice hard-boiled eggs evenly." },
    { id: "oil_sprayer", name: "Oil Sprayer", filename: "images/kitchen/oil_sprayer_50x50.png", category: "kitchen", type: "Storage", material: "Glass + Steel", rarity: "★★★☆☆", description: "A pump-action spray bottle to mist cooking oil evenly over foods and pans." },
    { id: "dough_scraper", name: "Dough Scraper", filename: "images/kitchen/dough_scraper_50x50.png", category: "kitchen", type: "Bakeware", material: "Wood + Steel", rarity: "★★★☆☆", description: "A flat metal scraper for cutting dough and scraping flour off work surfaces." },
    { id: "flour_sifter", name: "Flour Sifter", filename: "images/kitchen/flour_sifter_50x50.png", category: "kitchen", type: "Bakeware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A hand-cranked mesh canister for sifting flour and aerating baking ingredients." },
    { id: "garlic_grater", name: "Garlic Grater", filename: "images/kitchen/garlic_grater_50x50.png", category: "kitchen", type: "Utensil", material: "Ceramic", rarity: "★★★☆☆", description: "A shallow ceramic dish with sharp textured ridges for pureeing garlic and ginger." },
    { id: "potato_masher", name: "Potato Masher", filename: "images/kitchen/potato_masher_50x50.png", category: "kitchen", type: "Utensil", material: "Wood + Steel", rarity: "★★☆☆☆", description: "A vertical masher with a wavy steel plate for crushing cooked potatoes and root vegetables." },
    { id: "basting_bulb", name: "Basting Bulb", filename: "images/kitchen/basting_bulb_50x50.png", category: "kitchen", type: "Prep", material: "Silicone + Glass", rarity: "★★★☆☆", description: "A pipette with a large rubber bulb for suctioning pan juices to baste roasting meats." },
    { id: "meat_thermometer", name: "Meat Thermometer", filename: "images/kitchen/meat_thermometer_50x50.png", category: "kitchen", type: "Tool", material: "Steel + Glass", rarity: "★★★☆☆", description: "An analog probe thermometer for checking the internal temperature of roasting meats." },
    { id: "herb_stripper", name: "Herb Stripper", filename: "images/kitchen/herb_stripper_50x50.png", category: "kitchen", type: "Prep", material: "Stainless Steel", rarity: "★★★☆☆", description: "A handheld metal card with holes of various sizes for stripping leaves off leafy herbs." },
    { id: "jar_opener", name: "Jar Opener", filename: "images/kitchen/jar_opener_50x50.png", category: "kitchen", type: "Tool", material: "Rubber", rarity: "★☆☆☆☆", description: "A high-grip textured rubber disc to help twist open stubborn jar lids." },
    { id: "melon_slicer", name: "Melon Slicer", filename: "images/kitchen/melon_slicer_50x50.png", category: "kitchen", type: "Prep", material: "Steel + Plastic", rarity: "★★★★☆", description: "A circular multi-blade slicer that cuts whole melons into uniform wedges in one press." },
    { id: "avocado_slicer", name: "Avocado Slicer", filename: "images/kitchen/avocado_slicer_50x50.png", category: "kitchen", type: "Prep", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A 3-in-1 tool designed to split, pit, and slice fresh avocados cleanly." },
    { id: "salad_tongs", name: "Salad Tongs", filename: "images/kitchen/salad_tongs_50x50.png", category: "kitchen", type: "Utensil", material: "Wood", rarity: "★★☆☆☆", description: "A pair of hand-shaped wooden serving spoons designed for tossing and serving salad." },
    { id: "butter_crock", name: "Butter Crock", filename: "images/kitchen/butter_crock_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★★★☆", description: "A French butter keeper that uses water seal to store butter soft and spreadable." },
    { id: "honey_pot", name: "Honey Pot", filename: "images/kitchen/honey_pot_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★★☆☆", description: "A round ceramic pot with a honey bee design for storing fresh honey." },
    { id: "salt_cellar", name: "Salt Cellar", filename: "images/kitchen/salt_cellar_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★★☆☆", description: "A countertop container with a magnetic pivoting lid for storing kosher salt." },
    { id: "ice_bucket", name: "Ice Bucket", filename: "images/kitchen/ice_bucket_50x50.png", category: "kitchen", type: "Serveware", material: "Stainless Steel", rarity: "★★★★☆", description: "A double-walled insulated ice bucket with hanging tongs for serving cold drinks." },
    { id: "cocktail_shaker", name: "Cocktail Shaker", filename: "images/kitchen/cocktail_shaker_50x50.png", category: "kitchen", type: "Drinkware", material: "Stainless Steel", rarity: "★★★★☆", description: "A three-piece shaker with a built-in strainer for mixing iced cocktails." },
    { id: "jigger", name: "Measuring Jigger", filename: "images/kitchen/jigger_50x50.png", category: "kitchen", type: "Drinkware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A dual-sided measuring cup for portioning spirits and cocktail ingredients." },
    { id: "muddler", name: "Muddler", filename: "images/kitchen/muddler_50x50.png", category: "kitchen", type: "Utensil", material: "Wood", rarity: "★★★☆☆", description: "A wooden pestle for mashing fresh fruit, sugar, and herbs in cocktail glasses." },
    { id: "cocktail_strainer", name: "Hawthorne Strainer", filename: "images/kitchen/cocktail_strainer_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A metal disc strainer with a wire spring coil designed for cocktail mixing cups." },
    { id: "bottle_stopper", name: "Bottle Stopper", filename: "images/kitchen/bottle_stopper_50x50.png", category: "kitchen", type: "Storage", material: "Cork + Ceramic", rarity: "★★☆☆☆", description: "A decorative stopper to reseal opened wine bottles and preserve freshness." },
    { id: "wine_decanter", name: "Wine Decanter", filename: "images/kitchen/wine_decanter_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★★★☆", description: "A wide-based glass carafe used to aerate and serve red wine." },
    { id: "wine_aerator", name: "Wine Aerator", filename: "images/kitchen/wine_aerator_50x50.png", category: "kitchen", type: "Drinkware", material: "Acrylic", rarity: "★★★★☆", description: "An in-line pourer that injects air directly into wine as it is poured." },
    { id: "wine_cooler", name: "Wine Chiller", filename: "images/kitchen/wine_cooler_50x50.png", category: "kitchen", type: "Storage", material: "Stainless Steel", rarity: "★★★★☆", description: "An insulated double-walled cylinder designed to keep wine bottles chilled." },
    { id: "champagne_stopper", name: "Champagne Stopper", filename: "images/kitchen/champagne_stopper_50x50.png", category: "kitchen", type: "Storage", material: "Stainless Steel", rarity: "★★★★☆", description: "A heavy pressure-locking cap designed to preserve bubbles in sparkling wines." },
    { id: "beer_mug", name: "Beer Stein", filename: "images/kitchen/beer_mug_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★☆☆☆", description: "A heavy-duty glass mug with a thick handle for serving cold beer." },
    { id: "shot_glass", name: "Shot Glass", filename: "images/kitchen/shot_glass_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★☆☆☆", description: "A small, heavy-based glass designed for serving shots of spirits." },
    { id: "whiskey_stones", name: "Whiskey Stones", filename: "images/kitchen/whiskey_stones_50x50.png", category: "kitchen", type: "Drinkware", material: "Soapstone", rarity: "★★★★☆", description: "A set of chilled natural soapstone cubes used to cool whiskey without diluting it." },
    { id: "flask", name: "Hip Flask", filename: "images/kitchen/flask_50x50.png", category: "kitchen", type: "Storage", material: "Stainless Steel", rarity: "★★★☆☆", description: "A thin, curved pocket flask designed for carrying liquor on the go." },
    { id: "tea_caddy", name: "Tea Caddy", filename: "images/kitchen/tea_caddy_50x50.png", category: "kitchen", type: "Storage", material: "Tin", rarity: "★★★☆☆", description: "A sealed metal storage canister for keeping loose tea leaves fresh and dry." },
    { id: "coffee_canister", name: "Coffee Canister", filename: "images/kitchen/coffee_canister_50x50.png", category: "kitchen", type: "Storage", material: "Steel", rarity: "★★★★☆", description: "An airtight canister with a vacuum valve for storing roasted coffee beans." },
    { id: "sugar_bowl", name: "Sugar Bowl", filename: "images/kitchen/sugar_bowl_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "A lidded ceramic dish designed for serving table sugar." },
    { id: "cream_pitcher", name: "Creamer Pitcher", filename: "images/kitchen/cream_pitcher_50x50.png", category: "kitchen", type: "Serveware", material: "Ceramic", rarity: "★★☆☆☆", description: "A small ceramic pitcher designed for serving milk or cream with coffee." },
    { id: "tea_tray", name: "Gongfu Tea Tray", filename: "images/kitchen/tea_tray_50x50.png", category: "kitchen", type: "Serveware", material: "Wood", rarity: "★★★★☆", description: "A slotted wooden tray designed to catch runoff water during traditional tea brewing." },
    { id: "tea_timer", name: "Tea Timer", filename: "images/kitchen/tea_timer_50x50.png", category: "kitchen", type: "Tool", material: "Wood + Glass", rarity: "★★★☆☆", description: "A triple-sand timer for timing green, black, and herbal teas." },
    { id: "coffee_grinder", name: "Coffee Grinder", filename: "images/kitchen/coffee_grinder_50x50.png", category: "kitchen", type: "Tool", material: "Wood + Steel", rarity: "★★★★☆", description: "A manual crank grinder with adjustable ceramic burrs for grinding coffee beans." },
    { id: "milk_frother", name: "Milk Frother", filename: "images/kitchen/milk_frother_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A handheld battery-operated whisk for frothing milk for lattes and cappuccinos." },
    { id: "french_press", name: "French Press", filename: "images/kitchen/french_press_50x50.png", category: "kitchen", type: "Appliance", material: "Glass + Steel", rarity: "★★★☆☆", description: "A classic glass press with a mesh plunger for steeping and filtering coffee." },
    { id: "pour_over_cone", name: "Pour Over Cone", filename: "images/kitchen/pour_over_cone_50x50.png", category: "kitchen", type: "Appliance", material: "Ceramic", rarity: "★★★☆☆", description: "A ceramic V60 cone designed for slow pour-over coffee filtration." },
    { id: "gooseneck_kettle", name: "Gooseneck Kettle", filename: "images/kitchen/gooseneck_kettle_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★★☆", description: "An electric kettle with a slender gooseneck spout for precise water flow control." },
    { id: "digital_timer", name: "Digital Timer", filename: "images/kitchen/digital_timer_50x50.png", category: "kitchen", type: "Tool", material: "Plastic", rarity: "★★★☆☆", description: "A digital LCD timer with start/stop buttons and a magnetic back." },
    { id: "recipe_holder", name: "Recipe Holder", filename: "images/kitchen/recipe_holder_50x50.png", category: "kitchen", type: "Tool", material: "Wood", rarity: "★★★☆☆", description: "A wooden easel stand designed for holding cookbooks or tablets in the kitchen." },
    { id: "trivet_cork", name: "Cork Trivet", filename: "images/kitchen/trivet_cork_50x50.png", category: "kitchen", type: "Safety", material: "Cork", rarity: "★★☆☆☆", description: "A thick heat-absorbing cork hot pad for protecting tables." },
    { id: "pinch_bowls", name: "Pinch Bowls", filename: "images/kitchen/pinch_bowls_50x50.png", category: "kitchen", type: "Prep", material: "Ceramic", rarity: "★★☆☆☆", description: "A set of miniature prep bowls for holding pre-measured spices and herbs." },
    { id: "toothpick_holder", name: "Toothpick Holder", filename: "images/kitchen/toothpick_holder_50x50.png", category: "kitchen", type: "Storage", material: "Glass", rarity: "★★☆☆☆", description: "A small glass shaker jar containing bamboo toothpicks." },
    { id: "coaster", name: "Slate Coaster", filename: "images/kitchen/coaster_50x50.png", category: "kitchen", type: "Serveware", material: "Slate", rarity: "★★☆☆☆", description: "A square slate coaster with foam feet to protect tables from drink rings." },
    { id: "napkin_holder", name: "Napkin Holder", filename: "images/kitchen/napkin_holder_50x50.png", category: "kitchen", type: "Storage", material: "Steel", rarity: "★★☆☆☆", description: "A vertical wire rack for holding paper napkins upright on the table." },
    { id: "dish_brush", name: "Dish Brush", filename: "images/kitchen/dish_brush_50x50.png", category: "kitchen", type: "Cleaning", material: "Wood + Bristle", rarity: "★★☆☆☆", description: "A wooden scrub brush with stiff bristles for heavy-duty dish cleaning." },
    { id: "lemon_squeezer", name: "Lemon Squeezer", filename: "images/kitchen/lemon_squeezer_50x50.png", category: "kitchen", type: "Utensil", material: "Yellow Metal", rarity: "★★★☆☆", description: "A hinged handheld press for squeezing maximum juice out of citrus halves." },
    { id: "garlic_roaster", name: "Garlic Roaster", filename: "images/kitchen/garlic_roaster_50x50.png", category: "kitchen", type: "Cookware", material: "Terracotta", rarity: "★★★☆☆", description: "A terracotta baking dish designed specifically for roasting whole garlic bulbs." },
    { id: "tea_kettle_whistling", name: "Whistling Kettle", filename: "images/kitchen/tea_kettle_whistling_50x50.png", category: "kitchen", type: "Appliance", material: "Copper", rarity: "★★★★☆", description: "A classic whistling copper kettle that sings when water reaches boiling point." },
    { id: "trivet_wooden", name: "Slat Wooden Trivet", filename: "images/kitchen/trivet_wooden_50x50.png", category: "kitchen", type: "Safety", material: "Wood", rarity: "★★☆☆☆", description: "A slatted wooden hot pad designed to keep hot dishes from burning surfaces." },
    { id: "cake_tester", name: "Cake Tester", filename: "images/kitchen/cake_tester_50x50.png", category: "kitchen", type: "Tool", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A thin metal pin inserted into cakes to check if they are fully baked inside." },
    { id: "pot_scraper", name: "Pot Scraper", filename: "images/kitchen/pot_scraper_50x50.png", category: "kitchen", type: "Cleaning", material: "Plastic", rarity: "★☆☆☆☆", description: "A small, curved plastic scraper designed to scrape stuck food off pots and pans." },
    { id: "oil_cruet", name: "Ceramic Oil Cruet", filename: "images/kitchen/oil_cruet_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★★☆☆", description: "An opaque ceramic bottle with a metal spout for pouring olive oil smoothly." },
    { id: "funnel_collapsible", name: "Collapsible Funnel", filename: "images/kitchen/funnel_collapsible_50x50.png", category: "kitchen", type: "Utensil", material: "Silicone", rarity: "★★☆☆☆", description: "A flexible silicone funnel that folds flat for space-saving kitchen storage." },
    { id: "spoon_rest", name: "Spoon Rest", filename: "images/kitchen/spoon_rest_50x50.png", category: "kitchen", type: "Utensil", material: "Ceramic", rarity: "★★☆☆☆", description: "A shallow ceramic dish for holding messy spoons on the stove while cooking." },
    { id: "bag_clip", name: "Bag Clip", filename: "images/kitchen/bag_clip_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★☆☆☆☆", description: "A spring-loaded plastic clip to seal opened chip bags and keep snacks fresh." },
    { id: "egg_rack", name: "Egg Counter Rack", filename: "images/kitchen/egg_rack_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★☆☆☆", description: "A wooden display stand for holding fresh eggs upright on the kitchen counter." },
    { id: "kitchen_shears", name: "Kitchen Shears", filename: "images/kitchen/kitchen_shears_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "Heavy-duty kitchen scissors designed for cutting herbs, packaging, and meat." },
    { id: "poultry_shears", name: "Poultry Shears", filename: "images/kitchen/poultry_shears_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel", rarity: "★★★★☆", description: "Curved spring-loaded shears designed to cut through tough chicken bones." },
    { id: "meat_claws", name: "Meat Claws", filename: "images/kitchen/meat_claws_50x50.png", category: "kitchen", type: "Utensil", material: "Plastic + Steel", rarity: "★★★☆☆", description: "Spiked claw handles used for shredding pulled pork, beef, and chicken." },
    { id: "fish_scaler", name: "Fish Scaler", filename: "images/kitchen/fish_scaler_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Wood", rarity: "★★★☆☆", description: "A textured steel scraping tool for removing scales from fresh fish." },
    { id: "apple_corer", name: "Apple Corer", filename: "images/kitchen/apple_corer_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A circular plunge tool designed to extract cores from apples and pears." },
    { id: "pineapple_corer", name: "Pineapple Corer", filename: "images/kitchen/pineapple_corer_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Yellow Plastic", rarity: "★★★★☆", description: "A spiral slicing tool that peels, cores, and slices pineapples." },
    { id: "olive_spoon", name: "Olive Spoon", filename: "images/kitchen/olive_spoon_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A long-handled spoon with drainage holes for scooping olives from deep jars." },
    { id: "cheese_slicer", name: "Cheese Slicer", filename: "images/kitchen/cheese_slicer_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A flat shovel-style cheese plane designed to cut thin, even cheese slices." },
    { id: "cheese_wire", name: "Cheese Wire Board", filename: "images/kitchen/cheese_wire_50x50.png", category: "kitchen", type: "Prep", material: "Wood + Steel", rarity: "★★★★☆", description: "A wooden board equipped with a wire cutter arm for slicing cheese." },
    { id: "dough_whisk", name: "Dough Whisk", filename: "images/kitchen/dough_whisk_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Wood", rarity: "★★★★☆", description: "A Danish dough whisk with circular wire loops for mixing thick bread dough." },
    { id: "pastry_blender", name: "Pastry Blender", filename: "images/kitchen/pastry_blender_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Wood", rarity: "★★★☆☆", description: "A dough blender tool with parallel curved blades for cutting butter into flour." },
    { id: "bowl_scraper", name: "Bowl Scraper", filename: "images/kitchen/bowl_scraper_50x50.png", category: "kitchen", type: "Bakeware", material: "Silicone", rarity: "★★☆☆☆", description: "A flexible silicone card designed for scraping clean the curves of bowls." },
    { id: "pie_weights", name: "Pie Weights", filename: "images/kitchen/pie_weights_50x50.png", category: "kitchen", type: "Bakeware", material: "Glass + Ceramic", rarity: "★★★☆☆", description: "A jar of ceramic baking beads used to weight down pie crusts during blind baking." },
    { id: "pie_bird", name: "Pie Bird", filename: "images/kitchen/pie_bird_50x50.png", category: "kitchen", type: "Bakeware", material: "Ceramic", rarity: "★★★★☆", description: "A hollow ceramic chimney bird placed in pies to vent steam and prevent boil-overs." },
    { id: "pie_crust_shield", name: "Pie Crust Shield", filename: "images/kitchen/pie_crust_shield_50x50.png", category: "kitchen", type: "Bakeware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A metal ring protector placed over pie edges to prevent the crust from burning." },
    { id: "cake_leveler", name: "Cake Leveler", filename: "images/kitchen/cake_leveler_50x50.png", category: "kitchen", type: "Bakeware", material: "Stainless Steel", rarity: "★★★★☆", description: "An adjustable wire frame leveler designed to slice cakes into flat layers." },
    { id: "icing_spatula", name: "Icing Spatula", filename: "images/kitchen/icing_spatula_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Wood", rarity: "★★★☆☆", description: "An offset palette knife spatula designed to spread frosting flat on cakes." },
    { id: "cake_scraper", name: "Cake Scraper", filename: "images/kitchen/cake_scraper_50x50.png", category: "kitchen", type: "Bakeware", material: "Stainless Steel", rarity: "★★★☆☆", description: "A tall metal card with serrated edges for smoothing cake icing." },
    { id: "cookie_scoop", name: "Cookie Scoop", filename: "images/kitchen/cookie_scoop_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Yellow", rarity: "★★★☆☆", description: "A spring-loaded dough scoop for portioning cookies, muffins, or meatballs." },
    { id: "biscuit_cutter", name: "Biscuit Cutter", filename: "images/kitchen/biscuit_cutter_50x50.png", category: "kitchen", type: "Bakeware", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A circular metal ring mold with a handle for cutting biscuits and scones." },
    { id: "rolling_mat", name: "Rolling Mat", filename: "images/kitchen/rolling_mat_50x50.png", category: "kitchen", type: "Bakeware", material: "Silicone", rarity: "★★★☆☆", description: "A non-stick silicone baking mat with circular measurements for rolling dough." },
    { id: "pizza_stone", name: "Pizza Stone", filename: "images/kitchen/pizza_stone_50x50.png", category: "kitchen", type: "Cookware", material: "Ceramic", rarity: "★★★★☆", description: "A round ceramic stone that retains heat for baking crisp pizza crusts." },
    { id: "pizza_peel", name: "Pizza Peel", filename: "images/kitchen/pizza_peel_50x50.png", category: "kitchen", type: "Prep", material: "Wood", rarity: "★★★★☆", description: "A wide wooden paddle used to slide pizzas safely in and out of hot ovens." },
    { id: "trivet_wool", name: "Wool Ball Trivet", filename: "images/kitchen/trivet_wool_50x50.png", category: "kitchen", type: "Safety", material: "Wool", rarity: "★★★★☆", description: "A colorful round hot pad composed of stitched felt wool balls." },
    { id: "trivet_bamboo", name: "Bamboo Trivet", filename: "images/kitchen/trivet_bamboo_50x50.png", category: "kitchen", type: "Safety", material: "Bamboo", rarity: "★★☆☆☆", description: "A lattice-structured bamboo hot pad designed to insulate tables." },
    { id: "pan_protectors", name: "Pan Protectors", filename: "images/kitchen/pan_protectors_50x50.png", category: "kitchen", type: "Safety", material: "Felt", rarity: "★★☆☆☆", description: "Felt separator pads placed between stacked pans to prevent scratches." },
    { id: "bag_sealer", name: "Bag Sealer", filename: "images/kitchen/bag_sealer_50x50.png", category: "kitchen", type: "Tool", material: "White Plastic", rarity: "★★★☆☆", description: "A handheld heat sealer tool designed for sealing plastic food bags." },
    { id: "yogurt_maker", name: "Yogurt Maker", filename: "images/kitchen/yogurt_maker_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic", rarity: "★★★★☆", description: "A slow-heating electric base designed to incubate homemade yogurt jars." },
    { id: "soda_maker", name: "Soda Maker", filename: "images/kitchen/soda_maker_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Glass", rarity: "★★★★☆", description: "A carbonator machine designed to inject carbon dioxide into tap water." },
    { id: "ice_crusher", name: "Ice Crusher", filename: "images/kitchen/ice_crusher_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★☆☆", description: "A manual crank crusher box that grinds whole ice cubes into crushed ice." },
    { id: "salad_bowl", name: "Wooden Salad Bowl", filename: "images/kitchen/salad_bowl_50x50.png", category: "kitchen", type: "Serveware", material: "Wood", rarity: "★★★☆☆", description: "A large wooden serving bowl filled with fresh green salad." },
    { id: "salad_servers", name: "Salad Servers", filename: "images/kitchen/salad_servers_50x50.png", category: "kitchen", type: "Utensil", material: "Wood", rarity: "★★☆☆☆", description: "A pair of large wooden serving spoons designed for tossing salads." },
    { id: "butter_spreader", name: "Butter Spreader", filename: "images/kitchen/butter_spreader_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Wood", rarity: "★★☆☆☆", description: "A small blunt knife designed specifically for spreading butter and soft spreads." },
    { id: "honey_jar", name: "Honey Jar", filename: "images/kitchen/honey_jar_50x50.png", category: "kitchen", type: "Storage", material: "Glass", rarity: "★★☆☆☆", description: "A glass storage jar designed to hold honey, with a lid slot for a honey dipper." },
    { id: "salt_grinder", name: "Salt Grinder", filename: "images/kitchen/salt_grinder_50x50.png", category: "kitchen", type: "Tool", material: "Glass + Steel", rarity: "★★★☆☆", description: "An acrylic grinder that cracks coarse salt crystals over food." },
    { id: "oil_can", name: "Oil Can", filename: "images/kitchen/oil_can_50x50.png", category: "kitchen", type: "Storage", material: "Steel", rarity: "★★★☆☆", description: "A retro metal dispenser can with a long, thin curved spout for pouring oil." },
    { id: "bottle_capper", name: "Bottle Capper", filename: "images/kitchen/bottle_capper_50x50.png", category: "kitchen", type: "Tool", material: "Red Metal + Steel", rarity: "★★★★☆", description: "A twin-lever hand capper tool designed to lock caps onto glass bottles." },
    { id: "wine_rack", name: "Wine Rack", filename: "images/kitchen/wine_rack_50x50.png", category: "kitchen", type: "Storage", material: "Wood", rarity: "★★★☆☆", description: "A small wooden storage display rack for organizing wine bottles." },
    { id: "wine_thermometer", name: "Wine Thermometer", filename: "images/kitchen/wine_thermometer_50x50.png", category: "kitchen", type: "Tool", material: "Silver Metal", rarity: "★★★★☆", description: "A snap-on thermometer band designed to monitor wine bottle temperatures." },
    { id: "ice_scoop", name: "Ice Scoop", filename: "images/kitchen/ice_scoop_50x50.png", category: "kitchen", type: "Tool", material: "Wood + Steel", rarity: "★★★☆☆", description: "A metal shovel-shaped scoop with a wooden handle for scooping ice." },
    { id: "rice_cooker", name: "Rice Cooker", filename: "images/kitchen/rice_cooker_50x50.png", category: "kitchen", type: "Appliance", material: "Metal + Plastic", rarity: "★★★☆☆", description: "An automatic electric cooker designed to steam or boil rice to perfection." },
    { id: "sous_vide", name: "Immersion Circulator", filename: "images/kitchen/sous_vide_50x50.png", category: "kitchen", type: "Appliance", material: "Stainless Steel", rarity: "★★★★☆", description: "A precision temperature control wand used for sous vide water bath cooking." },
    { id: "dehydrator", name: "Food Dehydrator", filename: "images/kitchen/dehydrator_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic", rarity: "★★★☆☆", description: "A multi-tier drying chamber used to dehydrate fruits, vegetables, and jerky." },
    { id: "vacuum_sealer", name: "Vacuum Sealer", filename: "images/kitchen/vacuum_sealer_50x50.png", category: "kitchen", type: "Appliance", material: "Plastic + Steel", rarity: "★★★☆☆", description: "An airtight heat-sealing machine designed to preserve food freshness in vacuum bags." },
    { id: "panini_press", name: "Panini Press", filename: "images/kitchen/panini_press_50x50.png", category: "kitchen", type: "Appliance", material: "Cast Iron + Steel", rarity: "★★★☆☆", description: "A contact grill with ribbed plates to toast sandwiches and paninis." },
    { id: "water_pitcher", name: "Water Pitcher", filename: "images/kitchen/water_pitcher_50x50.png", category: "kitchen", type: "Serveware", material: "Glass", rarity: "★★☆☆☆", description: "A glass serving jug used for dispensing chilled water, juice, or iced tea." },
    { id: "dough_cutter", name: "Dough Cutter", filename: "images/kitchen/dough_cutter_50x50.png", category: "kitchen", type: "Bakeware", material: "Steel + Wood", rarity: "★★★☆☆", description: "A flat metal scraper with a wooden handle for cutting dough and scraping boards." },
    { id: "pie_server", name: "Pie Server", filename: "images/kitchen/pie_server_50x50.png", category: "kitchen", type: "Serveware", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A wedge-shaped server designed for lifting and serving slices of pie and cake." },
    { id: "cookie_jar", name: "Cookie Jar", filename: "images/kitchen/cookie_jar_50x50.png", category: "kitchen", type: "Storage", material: "Ceramic", rarity: "★★☆☆☆", description: "A ceramic storage jar with a lid to keep biscuits and cookies fresh." },
    { id: "bagel_cutter", name: "Bagel Guillotine", filename: "images/kitchen/bagel_cutter_50x50.png", category: "kitchen", type: "Prep", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A safe guillotine-style slicer designed to cut bagels cleanly in half." },
    { id: "juicer_press", name: "Citrus Press", filename: "images/kitchen/juicer_press_50x50.png", category: "kitchen", type: "Utensil", material: "Cast Iron", rarity: "★★★★☆", description: "A heavy lever-operated press designed to squeeze juice from citrus fruits." },
    { id: "pot_holder", name: "Pot Holder", filename: "images/kitchen/pot_holder_50x50.png", category: "kitchen", type: "Safety", material: "Fabric", rarity: "★☆☆☆☆", description: "A quilted fabric hot pad used to handle hot cookware and protect tables." },
    { id: "cupcake_carrier", name: "Cupcake Carrier", filename: "images/kitchen/cupcake_carrier_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★★★☆☆", description: "A portable storage dome with nested trays for carrying cupcakes safely." },
    { id: "taco_holder", name: "Taco Holder", filename: "images/kitchen/taco_holder_50x50.png", category: "kitchen", type: "Serveware", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A wavy metal wire rack designed to keep hard or soft tacos standing upright." },
    { id: "ice_pop_mold", name: "Ice Pop Mold", filename: "images/kitchen/ice_pop_mold_50x50.png", category: "kitchen", type: "Storage", material: "Silicone", rarity: "★★☆☆☆", description: "A multi-slot silicone mold with wooden sticks for freezing homemade popsicles." },
    { id: "lunch_box", name: "Lunch Box", filename: "images/kitchen/lunch_box_50x50.png", category: "kitchen", type: "Storage", material: "Metal", rarity: "★★☆☆☆", description: "A classic metal container with latches used for packing and carrying meals." },
    { id: "apron_hook", name: "Apron Hook", filename: "images/kitchen/apron_hook_50x50.png", category: "kitchen", type: "Storage", material: "Wood + Steel", rarity: "★★☆☆☆", description: "A decorative wall plaque with a heavy metal hook to hang kitchen aprons." },
    { id: "sponge_holder", name: "Sponge Holder", filename: "images/kitchen/sponge_holder_50x50.png", category: "kitchen", type: "Cleaning", material: "Ceramic", rarity: "★☆☆☆☆", description: "A compact countertop caddy designed to hold and drain wet kitchen sponges." },
    { id: "soap_dispenser", name: "Soap Dispenser", filename: "images/kitchen/soap_dispenser_50x50.png", category: "kitchen", type: "Cleaning", material: "Glass + Metal", rarity: "★★☆☆☆", description: "A pump-top dispenser bottle used for dispensing liquid dish or hand soap." },
    { id: "knife_sharpener", name: "Knife Sharpener", filename: "images/kitchen/knife_sharpener_50x50.png", category: "kitchen", type: "Tool", material: "Steel + Plastic", rarity: "★★★☆☆", description: "A manual pull-through abrasive tool to restore sharp edges to knives." },
    { id: "timer_hourglass", name: "Hourglass Timer", filename: "images/kitchen/timer_hourglass_50x50.png", category: "kitchen", type: "Tool", material: "Glass + Wood", rarity: "★★★☆☆", description: "A classic sand hourglass timer for tracking brief culinary intervals." },
    { id: "sink_strainer", name: "Sink Strainer", filename: "images/kitchen/sink_strainer_50x50.png", category: "kitchen", type: "Cleaning", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A perforated drain basket insert to catch food debris in the kitchen sink." },
    { id: "wine_cradle", name: "Wine Cradle", filename: "images/kitchen/wine_cradle_50x50.png", category: "kitchen", type: "Serveware", material: "Wood", rarity: "★★★★☆", description: "A wooden table stand that holds a wine bottle at a pouring angle." },
    { id: "corn_holders", name: "Corn Holders", filename: "images/kitchen/corn_holders_50x50.png", category: "kitchen", type: "Utensil", material: "Plastic + Steel", rarity: "★★☆☆☆", description: "A pair of double-pronged handles to insert into corn cobs for clean eating." },
    { id: "meat_hook", name: "Butcher Hook", filename: "images/kitchen/meat_hook_50x50.png", category: "kitchen", type: "Prep", material: "Stainless Steel", rarity: "★★★☆☆", description: "A heavy-duty S-shaped hook used by butchers to hang and cure meat carcasses." },
    { id: "pepper_corer", name: "Pepper Corer", filename: "images/kitchen/pepper_corer_50x50.png", category: "kitchen", type: "Utensil", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A serrated loop tool designed to cleanly extract seeds and cores from peppers." },
    { id: "herb_scissors", name: "Herb Scissors", filename: "images/kitchen/herb_scissors_50x50.png", category: "kitchen", type: "Cutlery", material: "Steel + Plastic", rarity: "★★★☆☆", description: "Multi-blade scissors designed for rapidly mincing fresh culinary herbs." },
    { id: "trivet_stone", name: "Stone Trivet", filename: "images/kitchen/trivet_stone_50x50.png", category: "kitchen", type: "Safety", material: "Marble", rarity: "★★★★☆", description: "A polished marble hot pad used to protect tables from hot pots." },
    { id: "whiskey_decanter", name: "Whiskey Decanter", filename: "images/kitchen/whiskey_decanter_50x50.png", category: "kitchen", type: "Serveware", material: "Glass", rarity: "★★★★☆", description: "A heavy, decorative glass decanter with a stopper for fine spirits." },
    { id: "oil_mister", name: "Oil Mister", filename: "images/kitchen/oil_mister_50x50.png", category: "kitchen", type: "Storage", material: "Stainless Steel", rarity: "★★★☆☆", description: "A pressurized spray bottle that dispenses a fine mist of cooking oil." },
    { id: "pot_lid_holder", name: "Lid Holder", filename: "images/kitchen/pot_lid_holder_50x50.png", category: "kitchen", type: "Storage", material: "Steel", rarity: "★★☆☆☆", description: "A wire rack organizer stand designed to hold pot and pan lids upright." },
    { id: "banana_hanger", name: "Banana Hanger", filename: "images/kitchen/banana_hanger_50x50.png", category: "kitchen", type: "Storage", material: "Steel", rarity: "★★☆☆☆", description: "An elevated hook stand designed to keep bananas hanging to prevent bruising." },
    { id: "egg_piercer", name: "Egg Piercer", filename: "images/kitchen/egg_piercer_50x50.png", category: "kitchen", type: "Tool", material: "Plastic + Steel", rarity: "★★★☆☆", description: "A small spring-loaded needle punch to poke holes in eggs before boiling." },
    { id: "tapioca_scoop", name: "Boba Scoop", filename: "images/kitchen/tapioca_scoop_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★★☆☆", description: "A mesh wire scoop designed for straining tapioca boba pearls from hot syrup." },
    { id: "sauce_dispenser", name: "Squeeze Bottle", filename: "images/kitchen/sauce_dispenser_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★☆☆☆☆", description: "A flexible plastic dispenser bottle for ketchup, mustard, or sauces." },
    { id: "toothpick_dispenser", name: "Toothpick Dispenser", filename: "images/kitchen/toothpick_dispenser_50x50.png", category: "kitchen", type: "Storage", material: "Plastic", rarity: "★★☆☆☆", description: "A pop-up dispenser box that ejects a single toothpick at the press of a button." },
    { id: "tea_bag_squeezer", name: "Tea Bag Squeezer", filename: "images/kitchen/tea_bag_squeezer_50x50.png", category: "kitchen", type: "Utensil", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A pair of tong-like squeezing plates to extract tea from hot bags." },
    { id: "can_punch", name: "Can Punch", filename: "images/kitchen/can_punch_50x50.png", category: "kitchen", type: "Tool", material: "Steel + Plastic", rarity: "★★☆☆☆", description: "A classic churchkey metal punch to pierce triangular holes in beverage tins." },
    { id: "ice_bag", name: "Ice Bag", filename: "images/kitchen/ice_bag_50x50.png", category: "kitchen", type: "Prep", material: "Canvas", rarity: "★★★☆☆", description: "A heavy canvas Lewis bag used with a mallet to crush ice cubes cleanly." },
    { id: "cocktail_pick", name: "Cocktail Picks", filename: "images/kitchen/cocktail_pick_50x50.png", category: "kitchen", type: "Serveware", material: "Stainless Steel", rarity: "★★☆☆☆", description: "Sleek metal garnish skewers topped with decorative beads for drinks." },
    { id: "champagne_flute", name: "Champagne Flute", filename: "images/kitchen/champagne_flute_50x50.png", category: "kitchen", type: "Drinkware", material: "Glass", rarity: "★★★☆☆", description: "A tall, narrow glass designed to preserve carbonation in sparkling wines." },
    { id: "carafe", name: "Water Carafe", filename: "images/kitchen/carafe_50x50.png", category: "kitchen", type: "Serveware", material: "Glass", rarity: "★★★☆☆", description: "A flared glass table container used for serving chilled water or wine." },
    { id: "ramekin", name: "Ramekin", filename: "images/kitchen/ramekin_50x50.png", category: "kitchen", type: "Bakeware", material: "Ceramic", rarity: "★★☆☆☆", description: "A small glazed ceramic dish ideal for baking souffles and serving dips." },
    { id: "moka_pot", name: "Moka Pot", filename: "images/kitchen/moka_pot_50x50.png", category: "kitchen", type: "Appliance", material: "Aluminum", rarity: "★★★★☆", description: "A stovetop espresso maker that brews coffee by passing pressurized steam." },
    { id: "siphon_coffee", name: "Siphon Coffee Maker", filename: "images/kitchen/siphon_coffee_50x50.png", category: "kitchen", type: "Appliance", material: "Glass + Metal", rarity: "★★★★★", description: "A vacuum brew system that produces clean, flavorful coffee via vapor pressure." },
    { id: "whipped_cream_dispenser", name: "Cream Dispenser", filename: "images/kitchen/whipped_cream_dispenser_50x50.png", category: "kitchen", type: "Appliance", material: "Steel", rarity: "★★★★☆", description: "A pressurized siphon bottle designed to dispense fresh whipped cream." },
    { id: "gravy_separator", name: "Gravy Separator", filename: "images/kitchen/gravy_separator_50x50.png", category: "kitchen", type: "Prep", material: "Glass", rarity: "★★★☆☆", description: "A measuring pitcher with a low spout designed to separate fat from gravy." },
    { id: "roasting_rack", name: "Roasting Rack", filename: "images/kitchen/roasting_rack_50x50.png", category: "kitchen", type: "Cookware", material: "Steel", rarity: "★★★☆☆", description: "A V-shaped wire rack placed in roasting pans to elevate meats." },
    { id: "splatter_screen", name: "Splatter Screen", filename: "images/kitchen/splatter_screen_50x50.png", category: "kitchen", type: "Safety", material: "Stainless Steel", rarity: "★★☆☆☆", description: "A fine mesh pan cover that prevents hot oil splatters while frying." },
    { id: "steamer_basket", name: "Steamer Basket", filename: "images/kitchen/steamer_basket_50x50.png", category: "kitchen", type: "Cookware", material: "Wood", rarity: "★★★☆☆", description: "A traditional woven bamboo basket nested over pots to steam food." }
];

// ─── Vehicles Dataset ────────────────────────────────────────────────────────
const vehicles = [
    { id: "sedan", name: "Sedan", filename: "images/vehicles/sedan_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A standard four-door passenger car with a separate trunk compartment." },
    { id: "sports_car", name: "Sports Car", filename: "images/vehicles/sports_car_50x50.png", category: "vehicles", type: "Land", material: "Premium Gas", rarity: "★★★★☆", description: "A sleek, low-slung automobile designed for high-speed performance and agile handling." },
    { id: "pickup_truck", name: "Pickup Truck", filename: "images/vehicles/pickup_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A light duty truck featuring an open cargo tailgate bed for utility haulage." },
    { id: "suv", name: "SUV", filename: "images/vehicles/suv_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A spacious sport utility vehicle offering elevated ground clearance and cargo capacity." },
    { id: "minivan", name: "Minivan", filename: "images/vehicles/minivan_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A family passenger van featuring sliding rear doors and modular three-row seating." },
    { id: "convertible", name: "Convertible", filename: "images/vehicles/convertible_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A passenger car with a retractable roof, allowing open-air driving." },
    { id: "limousine", name: "Limousine", filename: "images/vehicles/limousine_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "An ultra-long luxury sedan driven by a chauffeur, featuring a partitioned cabin." },
    { id: "race_car", name: "Formula 1 Car", filename: "images/vehicles/race_car_50x50.png", category: "vehicles", type: "Land", material: "Racing Fuel", rarity: "★★★★★", description: "An open-wheel, single-seat racing car with extreme aerodynamic wings." },
    { id: "monster_truck", name: "Monster Truck", filename: "images/vehicles/monster_truck_50x50.png", category: "vehicles", type: "Land", material: "Methanol", rarity: "★★★★☆", description: "A specialized truck with giant oversized wheels and heavy-duty suspension." },
    { id: "fire_truck", name: "Fire Truck", filename: "images/vehicles/fire_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "An emergency rescue vehicle equipped with ladders, pumps, and water hoses." },
    { id: "police_car", name: "Police Car", filename: "images/vehicles/police_car_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A law enforcement cruiser fitted with emergency sirens, decals, and police lights." },
    { id: "ambulance", name: "Ambulance", filename: "images/vehicles/ambulance_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A medical emergency vehicle outfitted for transporting patients with life support." },
    { id: "school_bus", name: "School Bus", filename: "images/vehicles/school_bus_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★☆☆☆", description: "A classic yellow transit bus dedicated to student safety and school commutes." },
    { id: "double_decker_bus", name: "Double Decker Bus", filename: "images/vehicles/double_decker_bus_50x50.png", category: "vehicles", type: "Land", material: "Diesel / Electric", rarity: "★★★☆☆", description: "A high-capacity two-level transit bus commonly used for city sightseeing." },
    { id: "garbage_truck", name: "Garbage Truck", filename: "images/vehicles/garbage_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy utility truck equipped with an automated hydraulic waste compactor." },
    { id: "cement_mixer", name: "Cement Mixer", filename: "images/vehicles/cement_mixer_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A specialty truck carrying a rotating drum to keep concrete wet during transport." },
    { id: "dump_truck", name: "Dump Truck", filename: "images/vehicles/dump_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy construction truck with a hydraulic open-box bed for dumping bulk material." },
    { id: "tractor", name: "Tractor", filename: "images/vehicles/tractor_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "An agricultural utility vehicle designed to pull heavy farm machinery and plows." },
    { id: "forklift", name: "Forklift", filename: "images/vehicles/forklift_50x50.png", category: "vehicles", type: "Land", material: "Electric / Propane", rarity: "★★★☆☆", description: "A warehouse utility vehicle with front metal prongs to lift and move pallets." },
    { id: "bulldozer", name: "Bulldozer", filename: "images/vehicles/bulldozer_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy-tracked construction crawler fitted with a wide front grading blade." },
    { id: "excavator", name: "Excavator", filename: "images/vehicles/excavator_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A construction vehicle featuring a rotating cab and a hinged boom arm with a shovel." },
    { id: "steamroller", name: "Steamroller", filename: "images/vehicles/steamroller_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A road compaction vehicle fitted with a heavy circular steel drum roller." },
    { id: "golf_cart", name: "Golf Cart", filename: "images/vehicles/golf_cart_50x50.png", category: "vehicles", type: "Land", material: "Electric", rarity: "★★☆☆☆", description: "A small, lightweight open vehicle used to transport golfers and bags." },
    { id: "gokart", name: "Go-Kart", filename: "images/vehicles/gokart_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A miniature, open-frame four-wheeled racing kart for track amusement." },
    { id: "bicycle", name: "Bicycle", filename: "images/vehicles/bicycle_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★☆☆☆☆", description: "A classic two-wheeled vehicle powered entirely by human pedaling." },
    { id: "motorcycle", name: "Motorcycle", filename: "images/vehicles/motorcycle_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A motorized two-wheeled vehicle designed for swift road transport." },
    { id: "scooter", name: "Vespa Scooter", filename: "images/vehicles/scooter_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A retro step-through motor scooter popular for urban cruising." },
    { id: "segway", name: "Segway", filename: "images/vehicles/segway_50x50.png", category: "vehicles", type: "Land", material: "Electric", rarity: "★★★☆☆", description: "A self-balancing two-wheeled personal transporter with electric gyro guidance." },
    { id: "tuk_tuk", name: "Tuk Tuk", filename: "images/vehicles/tuk_tuk_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A three-wheeled motorized urban taxi cabin common in tropical nations." },
    { id: "hovercraft", name: "Hovercraft", filename: "images/vehicles/hovercraft_50x50.png", category: "vehicles", type: "Amphibious", material: "Aviation Fuel", rarity: "★★★★★", description: "An amphibious craft that glides over land or water supported by a cushion of air." },
    { id: "speed_boat", name: "Speed Boat", filename: "images/vehicles/speed_boat_50x50.png", category: "vehicles", type: "Water", material: "Gasoline", rarity: "★★★☆☆", description: "A small motorized watercraft designed for high-speed cruising and skiing." },
    { id: "sailboat", name: "Sailboat", filename: "images/vehicles/sailboat_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★☆☆", description: "A marine vessel powered primarily by the force of wind catching canvas sails." },
    { id: "submarine", name: "Submarine", filename: "images/vehicles/submarine_50x50.png", category: "vehicles", type: "Water", material: "Nuclear / Diesel", rarity: "★★★★★", description: "A naval vessel capable of independent underwater operations deep below the sea." },
    { id: "cruise_ship", name: "Cruise Ship", filename: "images/vehicles/cruise_ship_50x50.png", category: "vehicles", type: "Water", material: "Heavy Fuel Oil", rarity: "★★★★★", description: "A giant ocean liner equipped with cabins and entertainment for vacation voyages." },
    { id: "jet_ski", name: "Jet Ski", filename: "images/vehicles/jet_ski_50x50.png", category: "vehicles", type: "Water", material: "Gasoline", rarity: "★★★☆☆", description: "A small personal watercraft that the rider stands or sits on." },
    { id: "kayak", name: "Kayak", filename: "images/vehicles/kayak_50x50.png", category: "vehicles", type: "Water", material: "Paddle Power", rarity: "★★☆☆☆", description: "A narrow, double-pointed canoe paddled manually with a double-bladed paddle." },
    { id: "cargo_ship", name: "Cargo Ship", filename: "images/vehicles/cargo_ship_50x50.png", category: "vehicles", type: "Water", material: "Heavy Fuel Oil", rarity: "★★★★★", description: "A massive container ship designed to transport global shipping containers." },
    { id: "helicopter", name: "Helicopter", filename: "images/vehicles/helicopter_50x50.png", category: "vehicles", type: "Air", material: "Jet Fuel", rarity: "★★★★☆", description: "An aircraft with overhead rotors capable of vertical takeoff, landing, and hovering." },
    { id: "biplane", name: "Biplane", filename: "images/vehicles/biplane_50x50.png", category: "vehicles", type: "Air", material: "Aviation Gas", rarity: "★★★★☆", description: "A vintage propeller aircraft built with two stacked parallel wing structures." },
    { id: "jet_fighter", name: "Fighter Jet", filename: "images/vehicles/jet_fighter_50x50.png", category: "vehicles", type: "Air", material: "Jet Fuel", rarity: "★★★★★", description: "A high-speed supersonic military aircraft designed for aerial combat." },
    { id: "hot_air_balloon", name: "Hot Air Balloon", filename: "images/vehicles/hot_air_balloon_50x50.png", category: "vehicles", type: "Air", material: "Propane Gas", rarity: "★★★★☆", description: "A quiet, floating aircraft raised by heating air inside a large fabric envelope." },
    { id: "blimp", name: "Blimp", filename: "images/vehicles/blimp_50x50.png", category: "vehicles", type: "Air", material: "Helium + Gas", rarity: "★★★★☆", description: "A non-rigid airship that floats using helium gas and is steered by propellers." },
    { id: "passenger_plane", name: "Airliner", filename: "images/vehicles/passenger_plane_50x50.png", category: "vehicles", type: "Air", material: "Jet Fuel", rarity: "★★★★☆", description: "A commercial jet airliner designed to transport passengers over long distances." },
    { id: "space_shuttle", name: "Space Shuttle", filename: "images/vehicles/space_shuttle_50x50.png", category: "vehicles", type: "Space", material: "Rocket Fuel", rarity: "★★★★★", description: "A partially reusable spacecraft designed for orbital spaceflight missions." },
    { id: "train_locomotive", name: "Steam Train", filename: "images/vehicles/train_locomotive_50x50.png", category: "vehicles", type: "Rail", material: "Coal / Water", rarity: "★★★★☆", description: "A classic steam railway engine powered by coal-fired steam boilers." },
    { id: "bullet_train", name: "Bullet Train", filename: "images/vehicles/bullet_train_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★★★", description: "A high-speed aerodynamic train utilizing electric overhead lines." },
    { id: "tram", name: "Tram Streetcar", filename: "images/vehicles/tram_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★☆☆", description: "A street railway trolley car running on tracks embedded in public roads." },
    { id: "cable_car", name: "Cable Car", filename: "images/vehicles/cable_car_50x50.png", category: "vehicles", type: "Rail", material: "Underground Cable", rarity: "★★★★☆", description: "A classic street transit car pulled by an underground moving steel cable." },
    { id: "monorail", name: "Monorail", filename: "images/vehicles/monorail_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★★☆", description: "A straddle-type railway running on a single elevated concrete beam track." },
    { id: "hoverboard", name: "Hoverboard", filename: "images/vehicles/hoverboard_50x50.png", category: "vehicles", type: "Land", material: "Neon Battery", rarity: "★★★★★", description: "A futuristic self-propelling skate deck that hovers slightly above ground." },
    { id: "unicycle", name: "Unicycle", filename: "images/vehicles/unicycle_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★★☆☆", description: "A one-wheeled vehicle powered entirely by pedaling, requiring extreme balance." },
    { id: "tandem_bicycle", name: "Tandem Bicycle", filename: "images/vehicles/tandem_bicycle_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★★☆☆", description: "A bicycle designed to be pedaled by two people sitting one behind the other." },
    { id: "penny_farthing", name: "Penny Farthing", filename: "images/vehicles/penny_farthing_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★★★☆", description: "An early style of bicycle featuring a giant front wheel and tiny rear wheel." },
    { id: "dirt_bike", name: "Dirt Bike", filename: "images/vehicles/dirt_bike_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A lightweight motorcycle equipped with rugged tires for off-road dirt racing." },
    { id: "chopper_motorcycle", name: "Chopper", filename: "images/vehicles/chopper_motorcycle_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A custom motorcycle featuring an extended front fork and reclined seat." },
    { id: "snowmobile", name: "Snowmobile", filename: "images/vehicles/snowmobile_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A motorized vehicle designed for winter travel on snow, using front ski steering." },
    { id: "atv", name: "Quad ATV", filename: "images/vehicles/atv_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "An all-terrain vehicle with four low-pressure tires designed for rugged off-road tracks." },
    { id: "dune_buggy", name: "Dune Buggy", filename: "images/vehicles/dune_buggy_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A recreational vehicle with oversized tires and an open roll-cage frame for sand dunes." },
    { id: "ice_resurfacer", name: "Ice Resurfacer", filename: "images/vehicles/ice_resurfacer_50x50.png", category: "vehicles", type: "Land", material: "Electric / Propane", rarity: "★★★★☆", description: "A specialty utility vehicle used to clean and smooth the surface of ice rinks." },
    { id: "street_sweeper", name: "Street Sweeper", filename: "images/vehicles/street_sweeper_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A city sanitation truck fitted with rotating brushes for sweeping streets." },
    { id: "tow_truck", name: "Tow Truck", filename: "images/vehicles/tow_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A recovery vehicle equipped with a crane and winch to impound or rescue disabled cars." },
    { id: "tank_truck", name: "Tanker Truck", filename: "images/vehicles/tank_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy-duty transport truck fitted with a large cylindrical tank for carrying liquids." },
    { id: "car_transporter", name: "Car Transporter", filename: "images/vehicles/car_transporter_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A multi-tier carrier trailer truck designed to ship multiple automobiles." },
    { id: "logging_truck", name: "Logging Truck", filename: "images/vehicles/logging_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy flatbed tractor trailer configured to haul massive tree logs." },
    { id: "armored_car", name: "Armored Car", filename: "images/vehicles/armored_car_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A bulletproof security van used to transport valuable cash and gold." },
    { id: "ice_cream_truck", name: "Ice Cream Truck", filename: "images/vehicles/ice_cream_truck_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A commercial delivery van fitted with a freezer and music speaker to sell ice cream." },
    { id: "food_truck", name: "Food Truck", filename: "images/vehicles/food_truck_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A mobile kitchen truck designed to cook and sell hot street food." },
    { id: "camper_van", name: "Camper Van", filename: "images/vehicles/camper_van_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A self-propelled recreational vehicle equipped with sleeping and kitchen quarters." },
    { id: "milk_float", name: "Milk Float", filename: "images/vehicles/milk_float_50x50.png", category: "vehicles", type: "Land", material: "Electric", rarity: "★★★☆☆", description: "A slow-moving electric delivery cart designed for distributing fresh milk bottles." },
    { id: "electric_unicycle", name: "Electric Unicycle", filename: "images/vehicles/electric_unicycle_50x50.png", category: "vehicles", type: "Land", material: "Electric Battery", rarity: "★★★★☆", description: "A futuristic self-balancing electric wheel transporter ridden standing up." },
    { id: "electric_scooter", name: "Electric Scooter", filename: "images/vehicles/electric_scooter_50x50.png", category: "vehicles", type: "Land", material: "Electric Battery", rarity: "★★☆☆☆", description: "A folding urban kick scooter equipped with an electric hub motor." },
    { id: "rickshaw", name: "Pulled Rickshaw", filename: "images/vehicles/rickshaw_50x50.png", category: "vehicles", type: "Land", material: "Human Power", rarity: "★★★☆☆", description: "A two-wheeled passenger cart pulled manually by a runner on foot." },
    { id: "carriage", name: "Horse Carriage", filename: "images/vehicles/carriage_50x50.png", category: "vehicles", type: "Land", material: "Horse Power", rarity: "★★★★☆", description: "A historical wheeled passenger coach pulled by harnessed horses." },
    { id: "sleigh", name: "Sleigh", filename: "images/vehicles/sleigh_50x50.png", category: "vehicles", type: "Land", material: "Horse Power", rarity: "★★★★☆", description: "A horse-drawn winter transport sled designed to glide smoothly over ice and snow." },
    { id: "dog_sled", name: "Dog Sled", filename: "images/vehicles/dog_sled_50x50.png", category: "vehicles", type: "Land", material: "Dog Power", rarity: "★★★★☆", description: "A wooden winter sled pulled by a team of trained sled dogs over ice." },
    { id: "handcar", name: "Railroad Handcar", filename: "images/vehicles/handcar_50x50.png", category: "vehicles", type: "Rail", material: "Human Power", rarity: "★★★★☆", description: "A railway handcar propelled by riders pumping a central seesaw lever." },
    { id: "trolley_bus", name: "Trolley Bus", filename: "images/vehicles/trolley_bus_50x50.png", category: "vehicles", type: "Land", material: "Overhead Electric", rarity: "★★★☆☆", description: "An electric passenger transit bus powered by twin overhead contact wires." },
    { id: "steam_wagon", name: "Steam Wagon", filename: "images/vehicles/steam_wagon_50x50.png", category: "vehicles", type: "Land", material: "Coal / Water", rarity: "★★★★☆", description: "An early road freight utility vehicle driven by a steam engine boiler." },
    { id: "paddle_steamer", name: "Paddle Steamer", filename: "images/vehicles/paddle_steamer_50x50.png", category: "vehicles", type: "Water", material: "Coal / Steam", rarity: "★★★★★", description: "A river boat propelled by a large steam-driven paddle wheel at the stern." },
    { id: "rowboat", name: "Rowboat", filename: "images/vehicles/rowboat_50x50.png", category: "vehicles", type: "Water", material: "Oar Power", rarity: "★★☆☆☆", description: "A small wooden utility boat propelled manually using a pair of oars." },
    { id: "gondola_boat", name: "Gondola", filename: "images/vehicles/gondola_boat_50x50.png", category: "vehicles", type: "Water", material: "Oar Power", rarity: "★★★★☆", description: "A traditional flat-bottomed Venetian rowing boat navigated by a gondolier." },
    { id: "canoe", name: "Canoe", filename: "images/vehicles/canoe_50x50.png", category: "vehicles", type: "Water", material: "Paddle Power", rarity: "★★☆☆☆", description: "A lightweight open boat propelled with single-bladed paddles." },
    { id: "jetfoil", name: "Hydrofoil", filename: "images/vehicles/jetfoil_50x50.png", category: "vehicles", type: "Water", material: "Gasoline", rarity: "★★★★☆", description: "A passenger vessel fitted with wing-like foils that lift the hull out of water at speed." },
    { id: "catamaran", name: "Catamaran", filename: "images/vehicles/catamaran_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★☆", description: "A yacht featuring two parallel hulls, offering superior stability under sail." },
    { id: "aircraft_carrier", name: "Aircraft Carrier", filename: "images/vehicles/aircraft_carrier_50x50.png", category: "vehicles", type: "Water", material: "Nuclear / Heavy Oil", rarity: "★★★★★", description: "A colossal naval warship designed as a seaborne runway for fighter planes." },
    { id: "tugboat", name: "Tugboat", filename: "images/vehicles/tugboat_50x50.png", category: "vehicles", type: "Water", material: "Diesel", rarity: "★★★☆☆", description: "A powerful harbor boat designed to maneuver large ocean liners and barges." },
    { id: "barge", name: "Barge", filename: "images/vehicles/barge_50x50.png", category: "vehicles", type: "Water", material: "Towed", rarity: "★★★☆☆", description: "A flat-bottomed cargo boat designed for carrying bulk materials on canals." },
    { id: "lifeboat", name: "Lifeboat", filename: "images/vehicles/lifeboat_50x50.png", category: "vehicles", type: "Water", material: "Diesel", rarity: "★★★★☆", description: "A highly buoyant orange rescue craft deployed to save lives in marine emergencies." },
    { id: "pirate_ship", name: "Galleon", filename: "images/vehicles/pirate_ship_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★★", description: "A historical multi-decked sailing ship equipped with cannons." },
    { id: "hang_glider", name: "Hang Glider", filename: "images/vehicles/hang_glider_50x50.png", category: "vehicles", type: "Air", material: "Wind Power", rarity: "★★★★☆", description: "An unpowered glider consisting of a triangular wing sail ridden harness-down." },
    { id: "paraglider", name: "Paraglider", filename: "images/vehicles/paraglider_50x50.png", category: "vehicles", type: "Air", material: "Wind Power", rarity: "★★★★☆", description: "A recreational foot-launched glider aircraft using a curved fabric canopy." },
    { id: "ultralight_plane", name: "Ultralight", filename: "images/vehicles/ultralight_plane_50x50.png", category: "vehicles", type: "Air", material: "Aviation Gas", rarity: "★★★★☆", description: "A lightweight, slow-flying open-cockpit hobby airplane." },
    { id: "glider_plane", name: "Glider", filename: "images/vehicles/glider_plane_50x50.png", category: "vehicles", type: "Air", material: "Thermal Updrafts", rarity: "★★★★☆", description: "An unpowered aerodynamic aircraft designed to soar on rising air currents." },
    { id: "seaplane", name: "Seaplane", filename: "images/vehicles/seaplane_50x50.png", category: "vehicles", type: "Air", material: "Aviation Gas", rarity: "★★★★☆", description: "An aircraft equipped with pontoons instead of wheels to take off and land on water." },
    { id: "chinook_helicopter", name: "Chinook", filename: "images/vehicles/chinook_helicopter_50x50.png", category: "vehicles", type: "Air", material: "Jet Fuel", rarity: "★★★★★", description: "A heavy-lift transport helicopter utilizing twin tandem main rotors." },
    { id: "space_rover", name: "Lunar Rover", filename: "images/vehicles/space_rover_50x50.png", category: "vehicles", type: "Space", material: "Solar Battery", rarity: "★★★★★", description: "An extravehicular space rover designed to explore the surface of the Moon or Mars." },
    { id: "space_rocket", name: "Space Rocket", filename: "images/vehicles/space_rocket_50x50.png", category: "vehicles", type: "Space", material: "Rocket Fuel", rarity: "★★★★★", description: "A vertical launch spacecraft rocket designed to deliver payloads into Earth orbit." },
    { id: "lunar_lander", name: "Lunar Lander", filename: "images/vehicles/lunar_lander_50x50.png", category: "vehicles", type: "Space", material: "Rocket Fuel", rarity: "★★★★★", description: "A specialized descent module designed to touch down on the lunar surface." },
    { id: "hand_truck", name: "Hand Truck", filename: "images/vehicles/hand_truck_50x50.png", category: "vehicles", type: "Land", material: "Human Power", rarity: "★★☆☆☆", description: "An L-shaped hand trolley used for tilting and rolling heavy cargo boxes." },
    { id: "snowplow", name: "Snowplow", filename: "images/vehicles/snowplow_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy utility truck fitted with a front curved metal blade to clear snow." },
    { id: "military_tank", name: "Military Tank", filename: "images/vehicles/military_tank_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★★", description: "A heavy armored combat vehicle moving on tracks, equipped with a large revolving turret gun." },
    { id: "quadcopter", name: "Quadcopter", filename: "images/vehicles/quadcopter_50x50.png", category: "vehicles", type: "Air", material: "Electric Battery", rarity: "★★★☆☆", description: "An unmanned multirotor helicopter propelled by four rotors for aerial recording." },
    { id: "tricycle", name: "Tricycle", filename: "images/vehicles/tricycle_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★☆☆☆☆", description: "A small three-wheeled kids vehicle powered by pedals on the front wheel." },
    { id: "amphibious_car", name: "Amphibious Car", filename: "images/vehicles/amphibious_car_50x50.png", category: "vehicles", type: "Amphibious", material: "Gasoline", rarity: "★★★★★", description: "A unique dual-purpose automobile designed to drive on roads and float on water." },
    { id: "hot_rod", name: "Hot Rod", filename: "images/vehicles/hot_rod_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A classic American car modified with a large exposed engine and flame decals for speed." },
    { id: "recumbent_bike", name: "Recumbent Bike", filename: "images/vehicles/recumbent_bike_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★★☆☆", description: "A bicycle that places the rider in a laid-back reclining ergonomic position." },
    { id: "cargo_bike", name: "Cargo Bike", filename: "images/vehicles/cargo_bike_50x50.png", category: "vehicles", type: "Land", material: "Pedal / Electric", rarity: "★★★☆☆", description: "A utility bicycle designed with a heavy-duty cargo carrier box to transport goods." },
    { id: "electric_skateboard", name: "Electric Skateboard", filename: "images/vehicles/electric_skateboard_50x50.png", category: "vehicles", type: "Land", material: "Electric Battery", rarity: "★★★☆☆", description: "A modified skateboard propelled by an electric motor, controlled with a hand remote." },
    { id: "solar_car", name: "Solar Car", filename: "images/vehicles/solar_car_50x50.png", category: "vehicles", type: "Land", material: "Solar Power", rarity: "★★★★★", description: "An experimental aerodynamic vehicle covered with solar panels to run on sunlight." },
    { id: "cable_ferry", name: "Cable Ferry", filename: "images/vehicles/cable_ferry_50x50.png", category: "vehicles", type: "Water", material: "Cable-Guided", rarity: "★★★★☆", description: "A transit ferry guided across water channels by underwater steel cables." },
    { id: "jetpack", name: "Jetpack", filename: "images/vehicles/jetpack_50x50.png", category: "vehicles", type: "Air", material: "Kerosene", rarity: "★★★★★", description: "A sci-fi backpack device emitting gas jets to lift a single pilot into the air." },
    { id: "flying_car", name: "Flying Car", filename: "images/vehicles/flying_car_50x50.png", category: "vehicles", type: "Amphibious", material: "Electric Battery", rarity: "★★★★★", description: "A futuristic vertical takeoff and landing passenger vehicle designed for the skies." },
    { id: "zeppelin", name: "Zeppelin", filename: "images/vehicles/zeppelin_50x50.png", category: "vehicles", type: "Air", material: "Helium", rarity: "★★★★★", description: "A rigid, passenger-carrying airship of early aviation utilizing helium gas chambers." },
    { id: "ironclad", name: "Ironclad Warship", filename: "images/vehicles/ironclad_50x50.png", category: "vehicles", type: "Water", material: "Coal / Steam", rarity: "★★★★★", description: "A mid-19th century steam-powered wooden warship protected by thick iron armor plating." },
    { id: "hydroplane", name: "Hydroplane", filename: "images/vehicles/hydroplane_50x50.png", category: "vehicles", type: "Water", material: "Aviation Gas", rarity: "★★★★☆", description: "A high-speed racing motorboat designed to skim on the water's surface." },
    { id: "bathyscaphe", name: "Bathyscaphe", filename: "images/vehicles/bathyscaphe_50x50.png", category: "vehicles", type: "Water", material: "Battery", rarity: "★★★★★", description: "A deep-sea submersible vessel designed for deep scientific exploration of the ocean floor." },
    { id: "airboat", name: "Swamp Airboat", filename: "images/vehicles/airboat_50x50.png", category: "vehicles", type: "Water", material: "Aviation Gas", rarity: "★★★★☆", description: "A flat-bottomed watercraft powered by an aircraft engine and propeller for shallow swamps." },
    { id: "hoverbike", name: "Hoverbike", filename: "images/vehicles/hoverbike_50x50.png", category: "vehicles", type: "Air", material: "Electric Battery", rarity: "★★★★★", description: "A futuristic vertical takeoff hovercraft ridden like a motorcycle." },
    { id: "mobility_scooter", name: "Mobility Scooter", filename: "images/vehicles/mobility_scooter_50x50.png", category: "vehicles", type: "Land", material: "Electric Battery", rarity: "★★☆☆☆", description: "A personal mobility assistance device configured with electric controls and basket." },
    { id: "front_loader", name: "Front Loader", filename: "images/vehicles/front_loader_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A heavy construction tractor fitted with a front-mounted shovel to lift earth." },
    { id: "backhoe", name: "Backhoe", filename: "images/vehicles/backhoe_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A utility tractor equipped with a front loader and a rear-mounted excavator arm." },
    { id: "crane_truck", name: "Crane Truck", filename: "images/vehicles/crane_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A mobile truck platform mounted with a heavy hydraulic telescoping lift crane." },
    { id: "concrete_pump", name: "Concrete Pump", filename: "images/vehicles/concrete_pump_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy utility truck equipped with a folding mechanical boom to pump wet concrete." },
    { id: "cherry_picker", name: "Cherry Picker", filename: "images/vehicles/cherry_picker_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A utility service vehicle featuring an extendable boom with a worker basket." },
    { id: "snowcat", name: "Snowcat", filename: "images/vehicles/snowcat_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy tracked cabin vehicle designed to groom and traverse steep snow slopes." },
    { id: "baggage_tug", name: "Baggage Tug", filename: "images/vehicles/baggage_tug_50x50.png", category: "vehicles", type: "Land", material: "Electric / Diesel", rarity: "★★★☆☆", description: "A compact airport tractor pulling series of flat carts containing luggage." },
    { id: "pushback_tractor", name: "Pushback Tractor", filename: "images/vehicles/pushback_tractor_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "An extremely heavy airport vehicle used to push aircraft away from terminal gates." },
    { id: "trencher", name: "Trencher", filename: "images/vehicles/trencher_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy-duty construction machine designed to cut continuous narrow trenches." },
    { id: "mining_truck", name: "Mining Truck", filename: "images/vehicles/mining_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★★", description: "An ultra-large dump truck designed for hauling ore and rock in heavy mining sites." },
    { id: "road_grader", name: "Road Grader", filename: "images/vehicles/road_grader_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy construction grader vehicle with a long blade to level road dirt." },
    { id: "asphalt_paver", name: "Asphalt Paver", filename: "images/vehicles/asphalt_paver_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A road pavement laying machine that distributes asphalt evenly on roads." },
    { id: "combine_harvester", name: "Harvester", filename: "images/vehicles/combine_harvester_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A massive agricultural harvester that cuts, threshes, and cleans grain crops." },
    { id: "hay_baler", name: "Hay Baler", filename: "images/vehicles/hay_baler_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★☆☆", description: "A farm implement machine that compresses cut hay crops into tight square bales." },
    { id: "reach_stacker", name: "Reach Stacker", filename: "images/vehicles/reach_stacker_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "A heavy industrial port vehicle that lifts and stacks shipping cargo containers." },
    { id: "maglev", name: "Maglev Train", filename: "images/vehicles/maglev_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★★★", description: "A high-speed train utilizing magnetic levitation to hover and glide over tracks." },
    { id: "draisine", name: "Rail Draisine", filename: "images/vehicles/draisine_50x50.png", category: "vehicles", type: "Rail", material: "Human / Engine", rarity: "★★★★☆", description: "A light railway service cart designed to inspect railway tracks." },
    { id: "subway_car", name: "Subway Car", filename: "images/vehicles/subway_car_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★☆☆", description: "An urban electric passenger train carriage running on underground tracks." },
    { id: "funicular", name: "Funicular", filename: "images/vehicles/funicular_50x50.png", category: "vehicles", type: "Rail", material: "Cable", rarity: "★★★★☆", description: "A cable-guided cliff railway car designed to climb steep mountain slopes." },
    { id: "cog_railway", name: "Cog Railway", filename: "images/vehicles/cog_railway_50x50.png", category: "vehicles", type: "Rail", material: "Coal / Diesel", rarity: "★★★★☆", description: "A rack railway locomotive using a center cog wheel to climb steep tracks." },
    { id: "outrigger_canoe", name: "Outrigger Canoe", filename: "images/vehicles/outrigger_canoe_50x50.png", category: "vehicles", type: "Water", material: "Paddle Power", rarity: "★★★☆☆", description: "A traditional canoe hull stabilized by one or more lateral support floats." },
    { id: "banana_boat", name: "Banana Boat", filename: "images/vehicles/banana_boat_50x50.png", category: "vehicles", type: "Water", material: "Towed", rarity: "★★☆☆☆", description: "An inflatable yellow banana-shaped watercraft towed behind a speed boat." },
    { id: "gondola_lift", name: "Gondola Lift", filename: "images/vehicles/gondola_lift_50x50.png", category: "vehicles", type: "Air", material: "Electricity", rarity: "★★★★☆", description: "An aerial cable car cabin suspended from overhead moving steel cables." },
    { id: "flying_boat", name: "Flying Boat", filename: "images/vehicles/flying_boat_50x50.png", category: "vehicles", type: "Air", material: "Aviation Gas", rarity: "★★★★★", description: "A historical aircraft with a boat hull fuselage, allowing landing on water." },
    { id: "space_capsule", name: "Space Capsule", filename: "images/vehicles/space_capsule_50x50.png", category: "vehicles", type: "Space", material: "Rocket Fuel", rarity: "★★★★★", description: "A spacecraft capsule module designed to re-enter Earth's atmosphere under parachute." },
    { id: "asteroid_miner", name: "Asteroid Miner", filename: "images/vehicles/asteroid_miner_50x50.png", category: "vehicles", type: "Space", material: "Ion Engine", rarity: "★★★★★", description: "A futuristic mining spaceship equipped with lasers to harvest space rock minerals." },
    { id: "amphibious_atv", name: "Amphibious ATV", filename: "images/vehicles/amphibious_atv_50x50.png", category: "vehicles", type: "Amphibious", material: "Gasoline", rarity: "★★★★☆", description: "An 8x8 all-terrain vehicle with a watertight body that swims and rolls." },
    { id: "dragster", name: "Jet Dragster", filename: "images/vehicles/dragster_50x50.png", category: "vehicles", type: "Land", material: "Kerosene", rarity: "★★★★☆", description: "An extremely long-nose racing vehicle designed for top speeds on straight drag strips." },
    { id: "mars_rover", name: "Mars Rover", filename: "images/vehicles/mars_rover_50x50.png", category: "vehicles", type: "Space", material: "Solar / Nuclear", rarity: "★★★★★", description: "An automated robotic explorer probe sent to study the geology of Mars." },
    { id: "diesel_locomotive", name: "Diesel Locomotive", filename: "images/vehicles/diesel_locomotive_50x50.png", category: "vehicles", type: "Rail", material: "Diesel / Electric", rarity: "★★★★☆", description: "A modern heavy railway engine powered by a diesel-electric motor." },
    { id: "sidecar_motorcycle", name: "Sidecar Motorcycle", filename: "images/vehicles/sidecar_motorcycle_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A vintage three-wheeled motorcycle fitted with a passenger sidecar compartment." },
    { id: "lowrider", name: "Lowrider Car", filename: "images/vehicles/lowrider_50x50.png", category: "vehicles", type: "Land", material: "Hydraulics", rarity: "★★★★☆", description: "A custom classic car fitted with hydraulic suspension to bounce and tilt." },
    { id: "apc", name: "Armored Personnel Carrier", filename: "images/vehicles/apc_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★☆", description: "An 8-wheeled military armored vehicle designed to transport personnel under fire." },
    { id: "lawn_mower", name: "Ride-On Lawn Mower", filename: "images/vehicles/lawn_mower_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★☆☆☆", description: "A ride-on garden vehicle equipped with rotary cutting blades to trim grass." },
    { id: "hearse", name: "Hearse", filename: "images/vehicles/hearse_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A solemn long-wheelbase passenger vehicle designed to carry a coffin." },
    { id: "microcar", name: "Microcar", filename: "images/vehicles/microcar_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "An ultra-compact bubble car from the retro era with a single front door." },
    { id: "bucket_wheel_excavator", name: "Bucket Wheel Excavator", filename: "images/vehicles/bucket_wheel_excavator_50x50.png", category: "vehicles", type: "Land", material: "Electricity", rarity: "★★★★★", description: "A colossal super-heavy strip mining machine featuring a giant wheel of buckets." },
    { id: "bubble_car", name: "Bubble Car", filename: "images/vehicles/bubble_car_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A 3-wheeled microcar characterized by its transparent bubble-like canopy." },
    { id: "trireme", name: "Greek Trireme", filename: "images/vehicles/trireme_50x50.png", category: "vehicles", type: "Water", material: "Rowers / Wind", rarity: "★★★★★", description: "An ancient maritime galley warship propelled by three tiers of oars." },
    { id: "chinese_junk", name: "Chinese Junk", filename: "images/vehicles/chinese_junk_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★☆", description: "A classic Chinese sailing vessel featuring fully battened rectangular sails." },
    { id: "fireboat", name: "Fireboat", filename: "images/vehicles/fireboat_50x50.png", category: "vehicles", type: "Water", material: "Diesel", rarity: "★★★★☆", description: "A specialized marine vessel equipped with high-pressure firefighting water cannons." },
    { id: "luxury_yacht", name: "Luxury Yacht", filename: "images/vehicles/luxury_yacht_50x50.png", category: "vehicles", type: "Water", material: "Diesel", rarity: "★★★★★", description: "A massive, multi-deck motor yacht designed for high-end leisure cruising." },
    { id: "trimaran", name: "Trimaran", filename: "images/vehicles/trimaran_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★☆", description: "A multi-hull sailing vessel featuring a main hull and two outrigger hulls." },
    { id: "bathysphere", name: "Bathysphere", filename: "images/vehicles/bathysphere_50x50.png", category: "vehicles", type: "Water", material: "Cable-Guided", rarity: "★★★★★", description: "A spherical deep-sea observation chamber lowered into the abyss by a steel cable." },
    { id: "dhow", name: "Arabian Dhow", filename: "images/vehicles/dhow_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★☆", description: "A traditional merchant sailing vessel fitted with lateen triangular sails." },
    { id: "gyrocopter", name: "Gyrocopter", filename: "images/vehicles/gyrocopter_50x50.png", category: "vehicles", type: "Air", material: "Gasoline", rarity: "★★★★☆", description: "An open rotorcraft utilizing a free-spinning rotor and a rear pusher prop." },
    { id: "tiltrotor", name: "Tiltrotor Aircraft", filename: "images/vehicles/tiltrotor_50x50.png", category: "vehicles", type: "Air", material: "Aviation Fuel", rarity: "★★★★★", description: "An aircraft combining helicopter vertical lift with turboprop speed using tilting rotors." },
    { id: "stealth_bomber", name: "Stealth Bomber", filename: "images/vehicles/stealth_bomber_50x50.png", category: "vehicles", type: "Air", material: "Jet Fuel", rarity: "★★★★★", description: "A flying-wing military bomber engineered to bypass radar detection." },
    { id: "triplane", name: "Fokker Triplane", filename: "images/vehicles/triplane_50x50.png", category: "vehicles", type: "Air", material: "Aviation Gas", rarity: "★★★★☆", description: "A classic WWI fighter aircraft equipped with three parallel stacked wings." },
    { id: "wingsuit", name: "Wingsuit Flyer", filename: "images/vehicles/wingsuit_50x50.png", category: "vehicles", type: "Air", material: "Gravity", rarity: "★★★★☆", description: "A personal skydiving jumpsuit with fabric webbing to glide horizontally." },
    { id: "spaceplane", name: "Spaceplane", filename: "images/vehicles/spaceplane_50x50.png", category: "vehicles", type: "Space", material: "Rocket Fuel", rarity: "★★★★★", description: "An aerodynamic spacecraft designed to fly like an airplane in orbit and atmosphere." },
    { id: "turbotrain", name: "Turbotrain", filename: "images/vehicles/turbotrain_50x50.png", category: "vehicles", type: "Rail", material: "Gas Turbine", rarity: "★★★★☆", description: "A high-speed train passenger engine powered by gas turbine turbines." },
    { id: "hyperloop_pod", name: "Hyperloop Pod", filename: "images/vehicles/hyperloop_pod_50x50.png", category: "vehicles", type: "Rail", material: "Magnetic Induc", rarity: "★★★★★", description: "A futuristic high-speed transit pod riding in vacuum tubes via magnetic levitation." },
    { id: "container_flatcar", name: "Container Flatcar", filename: "images/vehicles/container_flatcar_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★☆☆", description: "A railcar flatbed carrying stacked standard shipping containers." },
    { id: "suspension_railway", name: "Suspension Railway", filename: "images/vehicles/suspension_railway_50x50.png", category: "vehicles", type: "Rail", material: "Electricity", rarity: "★★★★☆", description: "An elevated monorail carriage suspended underneath an overhead steel rail track." },
    { id: "mine_cart", name: "Mine Cart", filename: "images/vehicles/mine_cart_50x50.png", category: "vehicles", type: "Rail", material: "Human Power", rarity: "★★☆☆☆", description: "A classic steel rail cart used in underground mines to haul mineral ores." },
    { id: "solar_sail", name: "Solar Sail Probe", filename: "images/vehicles/solar_sail_50x50.png", category: "vehicles", type: "Space", material: "Solar Photons", rarity: "★★★★★", description: "A spacecraft propelled through deep space by solar light pressure on giant sails." },
    { id: "space_station", name: "Space Station", filename: "images/vehicles/space_station_50x50.png", category: "vehicles", type: "Space", material: "Solar / Fuel", rarity: "★★★★★", description: "A modular orbital facility serving as a long-term research hub for astronauts." },
    { id: "space_tug", name: "Space Tug", filename: "images/vehicles/space_tug_50x50.png", category: "vehicles", type: "Space", material: "Chemical Rocket", rarity: "★★★★★", description: "A utility spacecraft designed to relocate satellites and orbital payloads." },
    { id: "soapbox_car", name: "Soapbox Racer", filename: "images/vehicles/soapbox_car_50x50.png", category: "vehicles", type: "Land", material: "Gravity", rarity: "★★☆☆☆", description: "A simple unpowered cart made of wood and rope, built for gravity racing." },
    { id: "mountainboard", name: "Mountainboard", filename: "images/vehicles/mountainboard_50x50.png", category: "vehicles", type: "Land", material: "Gravity", rarity: "★★★☆☆", description: "An all-terrain skateboard fitted with bindings and large pneumatic knobby wheels." },
    { id: "quadricycle", name: "Tourist Quadricycle", filename: "images/vehicles/quadricycle_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★☆☆☆", description: "A four-wheeled pedal passenger carriage designed for two or more riders." },
    { id: "velomobile", name: "Velomobile", filename: "images/vehicles/velomobile_50x50.png", category: "vehicles", type: "Land", material: "Pedal Power", rarity: "★★★★☆", description: "An aerodynamic bullet-shaped shell enclosing a recumbent bicycle." },
    { id: "snowplow_train", name: "Snowplow Train", filename: "images/vehicles/snowplow_train_50x50.png", category: "vehicles", type: "Rail", material: "Diesel", rarity: "★★★★☆", description: "A rail locomotive fitted with a massive wedge plow to clear snow from tracks." },
    { id: "monowheel", name: "Monowheel", filename: "images/vehicles/monowheel_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A unique vehicle consisting of a single large ring inside which the rider sits." },
    { id: "interceptor", name: "High-Speed Interceptor", filename: "images/vehicles/interceptor_50x50.png", category: "vehicles", type: "Land", material: "Premium Gas", rarity: "★★★★★", description: "A futuristic custom-built police patrol car tuned for extreme pursuits." },
    { id: "crawler_transporter", name: "Crawler Transporter", filename: "images/vehicles/crawler_transporter_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★★★★", description: "A tracked platform transporter used by NASA to carry rockets to launchpads." },
    { id: "funny_car", name: "Funny Car Dragster", filename: "images/vehicles/funny_car_50x50.png", category: "vehicles", type: "Land", material: "Nitro / Methanol", rarity: "★★★★☆", description: "A drag racing car with a custom single-piece carbon fiber flip-top shell." },
    { id: "swamp_buggy", name: "Swamp Buggy", filename: "images/vehicles/swamp_buggy_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A custom recreational vehicle with extremely tall wheels to cross marshland." },
    { id: "iceboat", name: "Iceboat", filename: "images/vehicles/iceboat_50x50.png", category: "vehicles", type: "Water", material: "Wind Power", rarity: "★★★★☆", description: "A high-speed sail craft designed to slide on ice using metal runner blades." },
    { id: "efoil", name: "eFoil Surfboard", filename: "images/vehicles/efoil_50x50.png", category: "vehicles", type: "Water", material: "Electric Battery", rarity: "★★★★☆", description: "An electric hydrofoil surfboard that glides above water using a submerged wing." },
    { id: "jet_truck", name: "Jet Powered Truck", filename: "images/vehicles/jet_truck_50x50.png", category: "vehicles", type: "Land", material: "Aviation Fuel", rarity: "★★★★★", description: "An exhibition semi-truck equipped with jet engines that spits fire." },
    { id: "semi_truck", name: "Semi-Truck Cab", filename: "images/vehicles/semi_truck_50x50.png", category: "vehicles", type: "Land", material: "Diesel", rarity: "★★☆☆☆", description: "A classic heavy-duty semi-trailer truck cab with a chrome grille." },
    { id: "motorhome", name: "Class A Motorhome", filename: "images/vehicles/motorhome_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★☆☆", description: "A luxury mobile home built on a heavy bus chassis with amenities." },
    { id: "woodie_wagon", name: "Woodie Wagon", filename: "images/vehicles/woodie_wagon_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A classic station wagon with wooden side paneling, popular in surf culture." },
    { id: "rat_rod", name: "Rat Rod", filename: "images/vehicles/rat_rod_50x50.png", category: "vehicles", type: "Land", material: "Gasoline", rarity: "★★★★☆", description: "A custom hot rod stylized with a deliberately rusted vintage body and bare V8 engine." },
    { id: "trikke", name: "Trikke Carving Scooter", filename: "images/vehicles/trikke_50x50.png", category: "vehicles", type: "Land", material: "Human Power", rarity: "★★★☆☆", description: "A three-wheeled carving scooter propelled by rhythmic side-to-side body motion." },
    { id: "flying_platform", name: "Flying Platform", filename: "images/vehicles/flying_platform_50x50.png", category: "vehicles", type: "Air", material: "Gasoline", rarity: "★★★★★", description: "A personal vertical takeoff vehicle featuring a ducted fan platform." },
    { id: "cargo_drone", name: "Cargo Drone", filename: "images/vehicles/cargo_drone_50x50.png", category: "vehicles", type: "Air", material: "Electric Battery", rarity: "★★★★☆", description: "A heavy-lift multirotor drone configured to transport cargo crates." },
    { id: "personal_sub", name: "Personal Submersible", filename: "images/vehicles/personal_sub_50x50.png", category: "vehicles", type: "Water", material: "Electric Battery", rarity: "★★★★★", description: "A pocket submarine with a spherical glass cockpit for undersea exploration." },
    { id: "steam_yacht", name: "Luxury Steam Yacht", filename: "images/vehicles/steam_yacht_50x50.png", category: "vehicles", type: "Water", material: "Coal / Steam", rarity: "★★★★★", description: "An elegant late 19th-century pleasure yacht powered by a steam boiler." }
];

// ─── Merge all collections ────────────────────────────────────────────────────
// Tag each item with its top-level group so filters work uniformly
animals.forEach(a => { a.group = (a.category === "berry" || a.category === "citrus" || a.category === "melon" || a.category === "stone" || a.category === "tropical" || a.category === "pome") ? "fruits" : "animals"; });
kitchen.forEach(k => { k.group = "kitchen"; });
vehicles.forEach(v => { v.group = "vehicles"; });
const allItems = [...animals, ...kitchen, ...vehicles,
    {
        id: "crow",
        name: "Crow",
        filename: "images/animals/crow_50x50.png",
        category: "wild",
        isPredator: true,
        group: "animals",
        diet: "Omnivore",
        habitat: "Everywhere",
        rarity: "★★☆☆☆",
        description: "Highly intelligent black birds capable of problem-solving and recognizing human faces."
    }
];

// Application State
let activeFilter = "all";
let searchQuery = "";
let cardScale = 2.0; // multiplier (x50px)
let spriteResolution = "50x50"; // kitchen only has 50x50

// DOM Elements
const grid = document.getElementById("animal-grid");
const searchInput = document.getElementById("search-input");
const filterBtns = document.querySelectorAll(".filter-btn");
const speciesCount = document.getElementById("species-count");
const globalScaleSlider = document.getElementById("global-scale-slider");
const globalScaleBadge = document.getElementById("global-scale-badge");
const resolutionSelector = document.getElementById("resolution-selector");
const themeSelector = document.getElementById("theme-selector");
const noResultsEl = document.getElementById("no-results-element");
const clearSearchBtn = document.getElementById("clear-search-btn");

// Modal Elements
const detailModal = document.getElementById("detail-modal");
const modalCloseBtn = document.getElementById("modal-close-btn");
const modalImg = document.getElementById("modal-animal-img");
const modalTitle = document.getElementById("modal-title");
const modalCategory = document.getElementById("modal-category");
const modalDescription = document.getElementById("modal-description");
const modalDiet = document.getElementById("modal-diet");
const modalHabitat = document.getElementById("modal-habitat");
const modalRarity = document.getElementById("modal-rarity");
const modalDownloadLink = document.getElementById("modal-download-link");
const modalCopyBtn = document.getElementById("modal-copy-btn");
const zoomSlider = document.getElementById("zoom-slider");
const zoomBadge = document.getElementById("zoom-badge");
const paletteBtns = document.querySelectorAll(".palette-btn");

// Init Render
function renderGallery() {
    grid.innerHTML = "";
    
    const filtered = allItems.filter(item => {
        // Search: match name, type/diet, material/habitat
        const searchFields = [
            item.name,
            item.diet || item.type || "",
            item.habitat || item.material || "",
            item.category
        ].join(" ").toLowerCase();
        const matchesSearch = searchFields.includes(searchQuery.toLowerCase());
        
        // Top-level category filter
        let matchesCategory = false;
        if (activeFilter === "all") {
            matchesCategory = true;
        } else if (activeFilter === "animals") {
            matchesCategory = (item.group === "animals");
        } else if (activeFilter === "fruits") {
            matchesCategory = (item.group === "fruits");
        } else if (activeFilter === "kitchen") {
            matchesCategory = (item.group === "kitchen");
        } else {
            matchesCategory = (item.category === activeFilter);
        }
        
        return matchesSearch && matchesCategory;
    });

    // Update species counter
    speciesCount.textContent = filtered.length;

    // Show/hide empty state
    if (filtered.length === 0) {
        noResultsEl.style.display = "block";
        grid.style.display = "none";
        return;
    } else {
        noResultsEl.style.display = "none";
        grid.style.display = "grid";
    }

    // Populate grid
    filtered.forEach(item => {
        const card = document.createElement("div");
        card.className = "card animal-card";
        card.setAttribute("tabindex", "0");
        card.setAttribute("role", "button");
        card.setAttribute("aria-label", `View details of ${item.name}`);
        
        // Dynamic image dimensions — kitchen items only have 50x50
        const res = item.group === "kitchen" ? "50x50" : spriteResolution;
        const sizePx = parseInt(res) * cardScale;
        const displaySrc = item.filename.replace("_50x50.png", `_${res}.png?v=clean`);
        const badgeLabel = item.diet || item.type || item.category;
        
        card.innerHTML = `
            <div class="card-img-wrapper" style="height: ${sizePx + 40}px">
                <img src="${displaySrc}" alt="${item.name}" class="pixelated" style="width: ${sizePx}px; height: ${sizePx}px;">
            </div>
            <span class="card-category">${item.group || item.category}</span>
            <h4>${item.name}</h4>
            <span class="badge-tag">${badgeLabel}</span>
        `;
        
        // Open modal on click or Enter key
        const openModalAction = () => openModal(item);
        card.addEventListener("click", openModalAction);
        card.addEventListener("keydown", (e) => {
            if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                openModalAction();
            }
        });

        grid.appendChild(card);
    });
}

// Search Handler
searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value;
    renderGallery();
});

// Category Filter Handlers
filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        activeFilter = btn.getAttribute("data-category");
        renderGallery();
    });
});

// Clear Search Handler
clearSearchBtn.addEventListener("click", () => {
    searchInput.value = "";
    searchQuery = "";
    renderGallery();
});

// Default Scale Slider Handler
globalScaleSlider.addEventListener("input", (e) => {
    cardScale = parseFloat(e.target.value);
    globalScaleBadge.textContent = cardScale.toFixed(1) + "x";
    renderGallery();
});

// Resolution Switcher Handler
resolutionSelector.addEventListener("change", (e) => {
    spriteResolution = e.target.value;
    renderGallery();
});

// Theme Switcher Handler
themeSelector.addEventListener("change", (e) => {
    const selectedTheme = e.target.value;
    document.body.className = ""; // Reset themes
    if (selectedTheme !== "midnight") {
        document.body.classList.add(`theme-${selectedTheme}`);
    }
});

// Modal Logic
let currentSelectedAnimal = null;

function openModal(item) {
    currentSelectedAnimal = item;
    
    // Set text elements
    modalTitle.textContent = item.name;
    const catLabel = item.isPredator ? `${item.category.toUpperCase()} • PREDATOR` : (item.group || item.category).toUpperCase();
    modalCategory.textContent = catLabel;
    modalDescription.textContent = item.description;
    
    // Spec fields differ: animals use diet/habitat, kitchen uses type/material, vehicles use type/fuel
    modalDiet.textContent = item.diet || item.type || "-";
    modalHabitat.textContent = item.habitat || item.material || "-";
    modalRarity.textContent = item.rarity;
    
    // Label the spec cards appropriately
    document.getElementById("modal-spec-1-label").textContent = item.diet ? "Diet" : "Type";
    document.getElementById("modal-spec-2-label").textContent = item.habitat ? "Habitat" : (item.group === "vehicles" ? "Power Source" : "Material");
    
    // Set image — kitchen and vehicles only have 50x50
    const res = (item.group === "kitchen" || item.group === "vehicles") ? "50x50" : spriteResolution;
    const displaySrc = item.filename.replace("_50x50.png", `_${res}.png?v=clean`);
    modalImg.src = displaySrc;
    modalImg.alt = `${item.name} Sprite`;
    modalDownloadLink.href = displaySrc;
    modalDownloadLink.setAttribute("download", `${item.id}_sprite_${res}.png`);

    // Reset Zoom slider and display
    zoomSlider.value = 6;
    zoomBadge.textContent = "6x";
    updateModalImgScale(6);

    // Reset filters
    modalImg.className = "pixelated-large";
    paletteBtns.forEach(b => b.classList.remove("active"));
    document.querySelector('.palette-btn[data-filter="normal"]').classList.add("active");

    // Display modal
    detailModal.style.display = "flex";
    modalCloseBtn.focus();
    
    // Trap tab key focus inside modal for accessibility
    document.addEventListener("keydown", trapFocus);
}

function closeModal() {
    detailModal.style.display = "none";
    document.removeEventListener("keydown", trapFocus);
    currentSelectedAnimal = null;
}

// Close Modal Events
modalCloseBtn.addEventListener("click", closeModal);
detailModal.addEventListener("click", (e) => {
    if (e.target === detailModal) {
        closeModal();
    }
});
window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && detailModal.style.display === "flex") {
        closeModal();
    }
});

// Zoom Slider Handler in Modal
zoomSlider.addEventListener("input", (e) => {
    const zoomVal = parseInt(e.target.value);
    zoomBadge.textContent = zoomVal + "x";
    updateModalImgScale(zoomVal);
});

function updateModalImgScale(factor) {
    const size = 50 * factor;
    modalImg.style.width = size + "px";
    modalImg.style.height = size + "px";
}

// Screen/Shaders/Filter Buttons
paletteBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        paletteBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        
        const filterType = btn.getAttribute("data-filter");
        // Reset class to base large pixelated
        modalImg.className = "pixelated-large";
        
        if (filterType !== "normal") {
            modalImg.classList.add(`filter-${filterType}`);
        }
    });
});

// Action: Copy metadata to clipboard
modalCopyBtn.addEventListener("click", () => {
    if (!currentSelectedAnimal) return;
    
    const item = currentSelectedAnimal;
    const text = [
        `Name: ${item.name}`,
        `Category: ${item.group || item.category}`,
        item.diet   ? `Diet: ${item.diet}`         : `Type: ${item.type}`,
        item.habitat? `Habitat: ${item.habitat}`   : `Material: ${item.material}`,
        `Rarity: ${item.rarity}`,
        `Description: ${item.description}`
    ].join("\n");

    navigator.clipboard.writeText(text).then(() => {
        const originalText = modalCopyBtn.textContent;
        modalCopyBtn.textContent = "Copied! ✓";
        modalCopyBtn.style.borderColor = "var(--accent)";
        setTimeout(() => {
            modalCopyBtn.textContent = originalText;
            modalCopyBtn.style.borderColor = "";
        }, 1500);
    }).catch(err => {
        console.error("Could not copy text: ", err);
    });
});

// Accessibility: Trap focus inside modal
function trapFocus(e) {
    if (detailModal.style.display !== "flex") return;
    
    const focusableEls = detailModal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]');
    const firstFocusable = focusableEls[0];
    const lastFocusable = focusableEls[focusableEls.length - 1];
    
    if (e.key === "Tab") {
        if (e.shiftKey) { // Shift + Tab
            if (document.activeElement === firstFocusable) {
                lastFocusable.focus();
                e.preventDefault();
            }
        } else { // Tab
            if (document.activeElement === lastFocusable) {
                firstFocusable.focus();
                e.preventDefault();
            }
        }
    }
}

// Load Gallery initially
renderGallery();
