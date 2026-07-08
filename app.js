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
        id: "crow",
        name: "Crow",
        filename: "images/animals/crow_50x50.png",
        category: "wild",
        isPredator: true,
        diet: "Omnivore",
        habitat: "Everywhere",
        rarity: "★★☆☆☆",
        description: "Highly intelligent black birds capable of problem-solving and recognizing human faces."
    }
,
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
    }
];

// Application State
let activeFilter = "all";
let searchQuery = "";
let cardScale = 2.0; // multiplier (x50px)

// DOM Elements
const grid = document.getElementById("animal-grid");
const searchInput = document.getElementById("search-input");
const filterBtns = document.querySelectorAll(".filter-btn");
const speciesCount = document.getElementById("species-count");
const globalScaleSlider = document.getElementById("global-scale-slider");
const globalScaleBadge = document.getElementById("global-scale-badge");
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
    
    const filteredAnimals = animals.filter(animal => {
        // Filter by Search Query
        const matchesSearch = animal.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
                             animal.diet.toLowerCase().includes(searchQuery.toLowerCase()) ||
                             animal.habitat.toLowerCase().includes(searchQuery.toLowerCase());
        
        // Filter by Category
        let matchesCategory = false;
        if (activeFilter === "all") {
            matchesCategory = true;
        } else if (activeFilter === "wild") {
            matchesCategory = (animal.category === "wild");
        } else if (activeFilter === "domestic") {
            matchesCategory = (animal.category === "domestic");
        } else if (activeFilter === "predator") {
            matchesCategory = animal.isPredator;
        }
        
        return matchesSearch && matchesCategory;
    });

    // Update species counter
    speciesCount.textContent = filteredAnimals.length;

    // Show/hide empty state
    if (filteredAnimals.length === 0) {
        noResultsEl.style.display = "block";
        grid.style.display = "none";
        return;
    } else {
        noResultsEl.style.display = "none";
        grid.style.display = "grid";
    }

    // Populate grid
    filteredAnimals.forEach(animal => {
        const card = document.createElement("div");
        card.className = "card animal-card";
        card.setAttribute("tabindex", "0");
        card.setAttribute("role", "button");
        card.setAttribute("aria-label", `View details of ${animal.name}`);
        
        // Dynamic image dimensions
        const sizePx = 50 * cardScale;
        
        card.innerHTML = `
            <div class="card-img-wrapper" style="height: ${sizePx + 40}px">
                <img src="${animal.filename}" alt="${animal.name}" class="pixelated" style="width: ${sizePx}px; height: ${sizePx}px;">
            </div>
            <span class="card-category">${animal.category}</span>
            <h4>${animal.name}</h4>
            <span class="badge-tag">${animal.diet}</span>
        `;
        
        // Open modal on click or Enter key
        const openModalAction = () => openModal(animal);
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

function openModal(animal) {
    currentSelectedAnimal = animal;
    
    // Set text elements
    modalTitle.textContent = animal.name;
    modalCategory.textContent = animal.isPredator ? `${animal.category.toUpperCase()} • PREDATOR` : animal.category.toUpperCase();
    modalDescription.textContent = animal.description;
    modalDiet.textContent = animal.diet;
    modalHabitat.textContent = animal.habitat;
    modalRarity.textContent = animal.rarity;
    
    // Set image path and download link
    modalImg.src = animal.filename;
    modalImg.alt = `${animal.name} Sprite`;
    modalDownloadLink.href = animal.filename;
    modalDownloadLink.setAttribute("download", `${animal.id}_sprite.png`);

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
    
    const text = `
Animal: ${currentSelectedAnimal.name}
Category: ${currentSelectedAnimal.category} (${currentSelectedAnimal.isPredator ? 'Predator' : 'Non-predator'})
Diet: ${currentSelectedAnimal.diet}
Habitat: ${currentSelectedAnimal.habitat}
Rarity: ${currentSelectedAnimal.rarity}
Description: ${currentSelectedAnimal.description}
    `.trim();

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
    const lastFocusable = focusableEls[focusableEls.length - 1,
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
];
    
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
