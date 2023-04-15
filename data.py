helpText =  'Metal Genre Generator Help\n\n'
helpText += 'New random genre: !newGenre\n'
helpText += 'Random picker: !picker [space delimited list]\n'
helpText += 'Who first: !whoFirst [space delimited list]\n'
helpText += 'BB3 Team Name: !BB3Team\n'
helpText += 'Lyrics guessing game: !lyrics\n'
helpText += 'Lyrics guessing stats: !stats\n'
helpText += 'Help: !bothelp'

genreWords = {
    "nationality": [
        "Afghan",
        "Albanian",
        "Algerian",
        "American",
        "Andorran",
        "Angolan",
        "Antiguans",
        "Argentinean",
        "Armenian",
        "Australian",
        "Austrian",
        "Azerbaijani",
        "Bahamian",
        "Bahraini",
        "Bangladeshi",
        "Barbadian",
        "Barbudans",
        "Batswana",
        "Belarusian",
        "Belgian",
        "Belizean",
        "Beninese",
        "Bhutanese",
        "Bolivian",
        "Bosnian",
        "Brazilian",
        "British",
        "Bruneian",
        "Bulgarian",
        "Burkinabe",
        "Burmese",
        "Burundian",
        "Cambodian",
        "Cameroonian",
        "Canadian",
        "Cape Verdean",
        "Central African",
        "Chadian",
        "Chilean",
        "Chinese",
        "Colombian",
        "Comoran",
        "Congolese",
        "Costa Rican",
        "Croatian",
        "Cuban",
        "Cypriot",
        "Czech",
        "Danish",
        "Djibouti",
        "Dominican",
        "Dutch",
        "East Timorese",
        "Ecuadorean",
        "Egyptian",
        "Emirian",
        "Equatorial Guinean",
        "Eritrean",
        "Estonian",
        "Ethiopian",
        "Fijian",
        "Filipino",
        "Finnish",
        "French",
        "Gabonese",
        "Gambian",
        "Georgian",
        "German",
        "Ghanaian",
        "Greek",
        "Grenadian",
        "Guatemalan",
        "Guinea-Bissauan",
        "Guinean",
        "Guyanese",
        "Haitian",
        "Herzegovinian",
        "Honduran",
        "Hungarian",
        "I-Kiribati",
        "Icelander",
        "Indian",
        "Indonesian",
        "Iranian",
        "Iraqi",
        "Irish",
        "Israeli",
        "Italian",
        "Ivorian",
        "Jamaican",
        "Japanese",
        "Jordanian",
        "Kazakhstani",
        "Kenyan",
        "Kittian and Nevisian",
        "Kuwaiti",
        "Kyrgyz",
        "Laotian",
        "Latvian",
        "Lebanese",
        "Liberian",
        "Libyan",
        "Liechtensteiner",
        "Lithuanian",
        "Luxembourger",
        "Macedonian",
        "Malagasy",
        "Malawian",
        "Malaysian",
        "Maldivan",
        "Malian",
        "Maltese",
        "Marshallese",
        "Mauritanian",
        "Mauritian",
        "Mexican",
        "Micronesian",
        "Moldovan",
        "Monacan",
        "Mongolian",
        "Moroccan",
        "Mosotho",
        "Motswana",
        "Mozambican",
        "Namibian",
        "Nauruan",
        "Nepalese",
        "New Zealander",
        "Nicaraguan",
        "Nigerian",
        "Nigerien",
        "North Korean",
        "Northern Irish",
        "Norwegian",
        "Omani",
        "Pakistani",
        "Palauan",
        "Panamanian",
        "Papua New Guinean",
        "Paraguayan",
        "Peruvian",
        "Polish",
        "Portuguese",
        "Qatari",
        "Romanian",
        "Russian",
        "Rwandan",
        "Saint Lucian",
        "Salvadoran",
        "Samoan",
        "San Marinese",
        "Sao Tomean",
        "Saudi",
        "Scottish",
        "Senegalese",
        "Serbian",
        "Seychellois",
        "Sierra Leonean",
        "Singaporean",
        "Slovakian",
        "Slovenian",
        "Solomon Islander",
        "Somali",
        "South African",
        "South Korean",
        "Spanish",
        "Sri Lankan",
        "Sudanese",
        "Surinamer",
        "Swazi",
        "Swedish",
        "Swiss",
        "Syrian",
        "Taiwanese",
        "Tajik",
        "Tanzanian",
        "Thai",
        "Togolese",
        "Tongan",
        "Trinidadian",
        "Tobagonian",
        "Tunisian",
        "Turkish",
        "Tuvaluan",
        "Ugandan",
        "Ukrainian",
        "Uruguayan",
        "Uzbekistani",
        "Venezuelan",
        "Vietnamese",
        "Welsh",
        "Yemenite",
        "Zambian",
        "Zimbabwean",
        "Chorennian",
        "Xaigonian",
        "Achaian",
        "Oxarean",
        "Qaidellian",
        "Mosian",
        "Gulberg",
        "Tollian",
        "Shrewgamic"
    ],
    "starters": [
        "New Wave",
        "Blackened",
        "Christian",
        "Melodic",
        "Symphonic",
        "Ambient"
    ],
    "fillers": [
        "Technical",
        "Progressive",
        "Avant-Garde",
        "Brutal",
        "Folk",
        "Viking",
        "Pirate",
        "Stoner",
        "Pagan",
        "Power",
        "Groove",
        "Alternative",
        "Funk",
        "Rap",
        "Black",
        "Atmospheric",
        "Depressive",
        "War",
        "Funeral",
        "Traditional",
        "Glam",
        "Gothic",
        "Hard",
        "Rock",
        "Heavy",
        "Psych",
        "Punk",
        "Industrial",
        "Neoclassical",
        "Speed",
        "Trance"
    ],
    "core": [
        "Hardcore",
        "Metalcore",
        "Deathcore",
        "Electronicore",
        "Mathcore",
        "Nintendocore",
        "Grindcore",
    ],
    "grind": [
        "Cybergrind",
        "Goregrind",
        "Pornogrind",
    ],
    "prefix": [
        "Nu",
        "Proto",
        "Crust"
    ],
    "enders": [
        "Death",
        "Thrash",
        "Doom",
        "Sludge",
        "Drone",
        "Crossover"
    ]
}

nationalities = {
    "Chorenn": {
        "noun": "Chorenn",
        "verb": "Chorennian"
    },
    "Xagon": {
        "noun": "Xagon",
        "verb": "Xaigonian"
    },
    "Achaea": {
        "noun": "Achaea",
        "verb": "Achaian"
    },
    "Oxares": {
        "noun": "Oxares",
        "verb": "Oxarean"
    },
    "Qaidel": {
        "noun": "Qaidel",
        "verb": "Qaidellian"
    },
    "Mose": {
        "noun": "Mose",
        "verb": "Mosian"
    },
    "Gulbering": {
        "noun": "Gulbering",
        "verb": "Gulberg"
    },
    "Tollian": {
        "noun": "Tollian",
        "verb": "Tollian"
    },
    "Shregami": {
        "noun": "Shregami",
        "verb": "Shrewgamic"
    },
}

titleStructure = {
    "default": {
        "ruler": {
            "male": "King",
            "female": "Queen",
        },
        "noble": {
            "male": "Lord",
            "female": "Lady",
        },
        "ovinatel": {
            "male": "Ovinatel",
            "female": "Ovinatel",
        },
        "religious": {
            "male": "Canon",
            "female": "Canon",
        },
        "military": {
            "male": "Sir",
            "female": "Lady",
        },
        "serf": {
            "male": "",
            "female": "",
        },
    }
}

nameStructure = {

}

cultures = {
    "Chorennian": {
        "titleStructure": titleStructure["default"],
        "nameStructure": "",
    },
    "Xaigonian": {},
    "Achaian": {},
    "Oxarean": {},
    "Qaidellian": {},
    "Mosian": {},
    "Gulberg": {},
    "Tollian": {},
    "Shrewgamic": {},
}

nouns = [
    'steel',
    'spiders',
    'haircut',
    'reward',
    'hate',
    'shoe',
    'shoes',
    'locket',
    'thing',
    'bucket',
    'rail',
    'laborer',
    'group',
    'cellar',
    'effect',
    'butter',
    'powder',
    'car',
    'attack',
    'number',
    'baseball',
    'bike',
    'toad',
    'tomatoes',
    'bone',
    'daughter',
    'muscle',
    'push',
    'death',
    'plantation',
    'stretch',
    'coil',
    'zebra',
    'tree',
    'fire',
    'spark',
    'sense',
    'existence',
    'earthquake',
    'play',
    'twist',
    'dad',
    'ground',
    'rings',
    'quiet',
    'language',
    'lamp',
    'current',
    'measure',
    'hand',
    'orange',
    'giraffe',
    'flower',
    'impulse',
    'blow',
    'knife',
    'creature',
    'baby',
    'train',
    'treatment',
    'growth',
    'mountain',
    'cannon',
    'sidewalk',
    'act',
    'account',
    'monkey',
    'caption',
    'smash',
    'quarter',
    'experience',
    'mask',
    'zipper',
    'basket',
    'cheese',
    'form',
    'hill',
    'girl',
    'month',
    'substance',
    'arithmetic',
    'pin',
    'record',
    'icicle',
    'river',
    'nut',
    'birthday',
    'walk',
    'carpenter',
    'sister',
    'vein',
    'plate',
    'fact',
    'mitten',
    'sleet',
    'soda',
    'connection',
    'yak',
    'cows',
    'duck',
    'writer',
    'cherries',
    'bridge',
    'breath',
    'horse',
    'trees',
    'boy',
    'oranges',
    'discussion',
    'bulb',
    'engine',
    'recess',
    'sticks',
    'match',
    'ladybug',
    'legs',
    'wheel',
    'theory',
    'condition',
    'flock',
    'rose',
    'wealth',
    'thunder',
    'eyes',
    'clam',
    'direction',
    'pest',
    'neck',
    'woman',
    'pail',
    'north',
    'pen',
    'fly',
    'pets',
    'camp',
    'trail',
    'animal',
    'ducks',
    'sky',
    'hook',
    'fog',
    'plant',
    'knot',
    'kick',
    'bubble',
    'meat',
    'veil',
    'tooth',
    'sugar',
    'touch',
    'dock',
    'toothpaste',
    'sock',
    'approval',
    'reason',
    'sign',
    'person',
    'ray',
    'potato',
    'cough',
    'thought',
    'science',
    'watch',
    'property',
    'coal',
    'calculator',
    'seed',
    'voyage',
    'desk',
    'join',
    'expansion',
    'rice',
    'advertisement',
    'fairies',
    'lumber',
    'tax',
    'summer',
    'pig',
    'geese',
    'top',
    'bottle',
    'work',
    'queen',
    'ocean',
    'airport',
    'amount',
    'name',
    'underwear',
    'hospital',
    'wood',
    'carriage',
    'achiever',
    'whip',
    'way',
    'price',
    'man',
    'hands',
    'land',
    'bat',
    'fold',
]

adjectives = [
    'loud',
    'cute',
    'hapless',
    'pretty',
    'open',
    'chilly',
    'repulsive',
    'fallacious',
    'coordinated',
    'thankful',
    'nonstop',
    'rigid',
    'knowing',
    'obtainable',
    'old-fashioned',
    'imaginary',
    'dizzy',
    'fabulous',
    'ordinary',
    'silly',
    'steadfast',
    'waggish',
    'frequent',
    'selective',
    'obscene',
    'industrious',
    'cold',
    'orange',
    'maniacal',
    'purring',
    'careful',
    'poor',
    'aberrant',
    'honorable',
    'mere',
    'ill-informed',
    'knotty',
    'nostalgic',
    'highfalutin',
    'enormous',
    'lazy',
    'knowledgeable',
    'ugly',
    'modern',
    'able',
    'needless',
    'woozy',
    'unsightly',
    'lovely',
    'shy',
    'scrawny',
    'average',
    'ancient',
    'arrogant',
    'tart',
    'unaccountable',
    'bored',
    'fixed',
    'stale',
    'ludicrous',
    'grandiose',
    'swanky',
    'superficial',
    'acoustic',
    'smiling',
    'slim',
    'ritzy',
    'wary',
    'placid',
    'simple',
    'voracious',
    'ten',
    'conscious',
    'pale',
    'gray',
    'equable',
    'absorbing',
    'hallowed',
    'exultant',
    'lonely',
    'charming',
    'cuddly',
    'clean',
    'oafish',
    'early',
    'nebulous',
    'long-term',
    'screeching',
    'worried',
    'beautiful',
    'imperfect',
    'uttermost',
    'vagabond',
    'lively',
    'far',
    'mighty',
    'momentous',
    'nippy',
    'actually',
    'numerous',
    'rapid',
    'statuesque',
    'pumped',
    'abusive',
    'instinctive',
    'jazzy',
    'childlike',
    'befitting',
    'greasy',
    'true',
    'prickly',
    'whispering',
    'stingy',
    'resonant',
    'ill-fated',
    'faulty',
    'polite',
    'toothsome',
    'rustic',
    'cruel',
    'unused',
    'malicious',
    'omniscient',
    'soggy',
    'poised',
    'worthless',
    'fierce',
    'six',
    'maddening',
    'grumpy',
    'crazy',
    'careless',
    'extra-large',
    'valuable',
    'adamant',
    'minor',
    'temporary',
    'ready',
    'neighborly',
    'chief',
    'four',
    'nervous',
    'mute',
    'fretful',
    'untidy',
    'victorious',
    'keen',
    'frail',
    'lying',
    'complete',
    'blue-eyed',
    'psychotic',
    'swift',
    'meaty',
    'marvelous',
    'thick',
    'dear',
    'jagged',
    'nice',
    'impolite',
    'upset',
    'dependent',
    'dusty',
    'talented',
    'sore',
    'colorful',
    'cute',
    'royal',
    'alive',
    'sneaky',
    'hellish',
    'thundering',
    'gifted',
    'bashful',
    'possible',
    'amusing',
    'natural',
    'wiggly',
    'offbeat',
    'rainy',
    'super',
    'waiting',
    'testy',
    'synonymous',
    'sincere',
    'scattered',
    'zippy',
    'shivering',
    'graceful',
    'educated',
    'flowery',
    'clammy',
    'acceptable',
    'cultured',
    'telling',
    'electric',
    'hilarious',
    'wide',
    'direful',
    'successful',
]

affermativeWords = ['Understood',
                    'Got it',
                    'Roger',
                    'Point taken',
                    'Roger that',
                    'Fine',
                    'Acknowledged',
                    'OK',
                    'I understand',
                    'Got you',
                    'Received',
                    'All right',
                    'Very well',
                    'Very good',
                    'I hear you',
                    'Loud and clear',
                    'Sure',
                    'Right',
                    'Alright',
                    'Righto',
                    'Okeydokey',
                    ]
