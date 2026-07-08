// Pixel Zoo Application Logic

// Dataset of 45 animals with metadata
const animals = [
    // 15 Original Animals
    {
        id: "panda",
        name: "Panda",
        filename: "panda_50x50.png",
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
        filename: "koala_50x50.png",
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
        filename: "lion_50x50.png",
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
        filename: "tiger_50x50.png",
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
        filename: "bear_50x50.png",
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
        filename: "fox_50x50.png",
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
        filename: "dog_50x50.png",
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
        filename: "cat_50x50.png",
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
        filename: "rabbit_50x50.png",
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
        filename: "monkey_50x50.png",
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
        filename: "frog_50x50.png",
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
        filename: "elephant_50x50.png",
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
        filename: "penguin_50x50.png",
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
        filename: "pig_50x50.png",
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
        filename: "owl_50x50.png",
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
        filename: "deer_50x50.png",
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
        filename: "wolf_50x50.png",
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
        filename: "sheep_50x50.png",
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
        filename: "cow_50x50.png",
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
        filename: "horse_50x50.png",
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
        filename: "chicken_50x50.png",
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
        filename: "duck_50x50.png",
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
        filename: "turtle_50x50.png",
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
        filename: "snake_50x50.png",
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
        filename: "lizard_50x50.png",
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
        filename: "shark_50x50.png",
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
        filename: "whale_50x50.png",
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
        filename: "dolphin_50x50.png",
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
        filename: "octopus_50x50.png",
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
        filename: "crab_50x50.png",
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
        filename: "spider_50x50.png",
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
        filename: "bee_50x50.png",
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
        filename: "butterfly_50x50.png",
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
        filename: "bat_50x50.png",
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
        filename: "squirrel_50x50.png",
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
        filename: "raccoon_50x50.png",
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
        filename: "beaver_50x50.png",
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
        filename: "kangaroo_50x50.png",
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
        filename: "zebra_50x50.png",
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
        filename: "giraffe_50x50.png",
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
        filename: "hippo_50x50.png",
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
        filename: "rhino_50x50.png",
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
        filename: "cheetah_50x50.png",
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
        filename: "eagle_50x50.png",
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
        filename: "parrot_50x50.png",
        category: "wild",
        isPredator: false,
        diet: "Frugivore",
        habitat: "Tropical Rainforests",
        rarity: "★★★★☆",
        description: "Parrots are colorful, mimicry-capable tropical birds. They use strong curved beaks to crack seeds and nuts and are highly sociable."
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
