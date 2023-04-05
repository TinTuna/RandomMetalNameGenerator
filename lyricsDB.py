import random
import useGeniusLyrics

async def getLyrics():
    # Get a random artist
    artist = random.choice(list(data.keys()))
    artistData = data[artist]
    # Get a random song from the artist
    album = random.choice(list(data[artist]['albums'].keys()))
    # Get a random song from the artist
    song = random.choice(list(data[artist]['albums'][album]['songs'].keys()))
    # Get the lyrics of the song
    lyrics = await useGeniusLyrics.getLyrics(artist, album, song, data[artist]['albums'][album]['songs'][song])
    # Get a random wrong choice
    wrongChoice1 = random.choice(list(data.keys()))
    # check if the wrong choice is the same as the artist
    while wrongChoice1 == artist:
        wrongChoice1 = random.choice(list(data.keys()))
    # Get a random wrong choice
    wrongChoice2 = random.choice(list(data.keys()))
    # check if the wrong choice is the same as the artist or the first wrong choice
    while wrongChoice2 == artist or wrongChoice2 == wrongChoice1:
        wrongChoice2 = random.choice(list(data.keys()))
    return artistData, artist, album, song, lyrics, wrongChoice1, wrongChoice2


data = {
    # 'artistName': {
    #     'id': 123,
    #     'albums': {
    #         'albumName': {
    #             'id': 123,
    #             'date': 'date',
    #             'avgScore': 100,
    #             'TinTuna#2453': 100,
    #             'Tinngles#8236': 100,
    #             'Izual#1552': 100,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },

    # 'Dipygus': {
    #     'id': 123,
    #     'albums': {
    #         'Bushmeat': {
    #             'id': 123,
    #             'date': 'January 2021',
    #             'avgScore': 49,
    #             'TinTuna#2453': 30,
    #             'Tinngles#8236': 60,
    #             'Izual#1552': 58,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    'Hulder': {
        'id': 2574565,
        'albums': {
            'Godslastering: Hymns of a Forlorn Peasantry': {
                'id': 726987,
                'date': 'January 2021',
                'avgScore': 62,
                'TinTuna#2453': 50,
                'Tinngles#8236': 80,
                'Izual#1552': 55,
                'songs': {
                    'Upon Frigid Winds': 6412989,
                    'Creature of Demonic Majesty': 6412997,
                    'Sown in Barren Soil': 6413002,
                    'De Dijle': 6413013,
                    'Purgations of Bodily Corruptions': 6413018,
                    'Lowland Famine': 6413022,
                    'A Forlorn Peasant’s Hymn': 6413031,
                    'From Whence an Ancient Evil Once Reigned': 6413034,
                },
            },
        },
    },
    'Asphyx': {
        'id': 349384,
        'albums': {
            'Necroceros': {
                'id': 710556,
                'date': 'January 2021',
                'avgScore': 74,
                'TinTuna#2453': 65,
                'Tinngles#8236': 75,
                'Izual#1552': 83,
                'songs': {
                    'The Sole Cure Is Death':  6264229,
                    'Molten Black Earth':  6264232,
                    'Mount Skull':  6264237,
                    'Knights Templar Stand':  6264210,
                    'Three Years of Famine':  6264239,
                    'Botox Implosion':  6264241,
                    'In Blazing Oceans':  6264248,
                    'The Nameless Elite':  6264251,
                    'Yield or Die':  6264254,
                    'Necrocer``os':  6264254,
                },
            },    
        },
    },
    'Dread Sovereign': {
        'id': 2491635,
        'albums': {
            'Alchemical Warfare': {
                'id': 704366,
                'date': 'January 2021',
                'avgScore': 64,
                'TinTuna#2453': 50,
                'Tinngles#8236': 70,
                'Izual#1552': 72,
                'songs': {
                    'She Wolves of the Savage Season': 6206591,
                    'The Great Beast We Serve':  206592,
                    'Nature Is the Devil’s Church':  6206583,
                    'Her Master’s Voice':  6206593,
                    'Devil’s Bane':  6206595,
                    'Ruin Upon the Temple Mount':  6206596,
                    'You Don’t Move Me (I Don’t Give a Fuck)': 6206597,
                },
            },  
        },
    },
    'Crystal Viper': {
        'id': 373835,
        'albums': {
            'The Cult': {
                'id': 729197,
                'date': 'January 2021',
                'avgScore': 63,
                'TinTuna#2453': 50,
                'Tinngles#8236': 65,
                'Izual#1552': 74,
                'songs': {
                    'The Cult': 6433125,
                    'Whispers from Beyond': 6912669,
                    'Down in the Crypt': 6912671,
                    'Sleeping Giants': 6912679,
                    'Forgotten Land': 6912686,
                    'Asenath Waite': 6912708,
                    'The Calling': 6912711,
                    'Flaring Madness': 6912726,
                    'Lost in the Dark': 6645732,
                    'Welcome Home': 6645754,
                },
            },  
        },
    },
    'Iotunn': {
        'id': 2552599,
        'albums': {
            'Access All Worlds': {
                'id': 720770,
                'date': 'Febuary 2021',
                'avgScore': 76,
                'TinTuna#2453': 85,
                'Tinngles#8236': 70,
                'Izual#1552': 72,
                'songs': {
                    'Voyage of the Garganey I': 6356081,
                    'Access All Worlds': 6356175,
                    'Laihem’s Golden Pits': 6356176,
                    'Waves Below': 6356177,
                    'The Tower of Cosmic Nihility': 6356178,
                    'The Weaver System': 6356179,
                    'Safe Across the Endless Night': 6356180,
                },
            },  
        },
    },
    'Paranorm': {
        'id': 1076772,
        'albums': {
            'Empyrean': {
                'id': 750317,
                'date': 'Febuary 2021',
                'avgScore': 69,
                'TinTuna#2453': 60,
                'Tinngles#8236': 60,
                'Izual#1552': 87,
                'songs': {
                    'Critical Mass': 6620918,
                    'The Immortal Generation': 6620923,
                    'Edge of the Horizon': 6620924,
                    'Intelligence Explosion': 6620925,
                    'Cannibal': 6620926,
                    'Empyrean': 6620927,
                    'Lost Cause': 6620928,
                    'Desolate Worlds (Distant Dimensions)': 6620930,
                },
            },  
        },
    },
    # 'Revulsion': {
    #     'id': 123,
    #     'albums': {
    #         'Revulsion': {
    #             'id': 123,
    #             'date': 'Febuary 2021',
    #             'avgScore': 82,
    #             'TinTuna#2453': 75,
    #             'Tinngles#8236': 80,
    #             'Izual#1552': 92,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    # 'Black Totem': {
    #     'id': 123,
    #     'albums': {
    #         'II: Shapeshifting': {
    #             'id': 123,
    #             'date': 'Febuary 2021',
    #             'avgScore': 61,
    #             'TinTuna#2453': 48,
    #             'Tinngles#8236': 60,
    #             'Izual#1552': 76,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    'Significant Point': {
        'id': 2623024,
        'albums': {
            'Into the Storm': {
                'id': 740564,
                'date': 'Febuary 2021',
                'avgScore': 58,
                'TinTuna#2453': 50,
                'Tinngles#8236': 50,
                'Izual#1552': 75,
                'songs': {
                    'Attacker': 6533512,
                    'Heavy Attack': 6533519,
                    'You’ve Got the Power': 6533520,
                    'Riders Under the Sun': 6533521,
                    'Night of the Axe': 6533522,
                    'Run for Your Life': 6533523,
                    'Into the Storm': 6533524,
                    'Deathrider': 6533525,
                    'Danger Zone': 6533526,
                    'Running Alone': 6533527,
                },
            },  
        },
    },
    # 'Sepulcros': {
    #     'id': 123,
    #     'albums': {
    #         'Vazio': {
    #             'id': 123,
    #             'date': 'March 2021',
    #             'avgScore': 67,
    #             'TinTuna#2453': 70,
    #             'Tinngles#8236': 75,
    #             'Izual#1552': 55,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    'Demiser': {
        'id': 2677630,
        'albums': {
            'Through the Gate Eternal': {
                'id': 756626,
                'date': 'March 2021',
                'avgScore': 92,
                'TinTuna#2453': 95,
                'Tinngles#8236': 92,
                'Izual#1552': 89,
                'songs': {
                    'Through the Gate Eternal': 6675837,
                    'Offering': 6675840,
                    'Deathstrike': 6675841,
                    'Raw Fucking Vomit': 6675842,
                    'Unholy Sacrifices': 6675845,
                    'Hook and Torment': 6675846,
                    'Demiser the Demiser': 6675847,
                    'Warfuck Demonlust': 6675848,
                },
            },  
        },
    },
    # 'Malist': {
    #     'id': 123,
    #     'albums': {
    #         'Karst Relict': {
    #             'id': 123,
    #             'date': 'March 2021',
    #             'avgScore': 78,
    #             'TinTuna#2453': 75,
    #             'Tinngles#8236': 82,
    #             'Izual#1552': 78,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    # 'Celestial Sanctuary': {
    #     'id': 123,
    #     'albums': {
    #         'Soul Diminished': {
    #             'id': 123,
    #             'date': 'March 2021',
    #             'avgScore': 65,
    #             'TinTuna#2453': 60,
    #             'Tinngles#8236': 70,
    #             'Izual#1552': 65,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    'Herzel': {
        'id': 2653858,
        'albums': {
            'Le Dernier Rempart': {
                'id': 749668,
                'date': 'March 2021',
                'avgScore': 71,
                'TinTuna#2453': 72,
                'Tinngles#8236': 75,
                'Izual#1552': 67,
                'songs': {
                    'Maîtres de L’océan': 6614709,
                    'La Flamme': 6614712,
                    'Berceau de Cendre': 6614717,
                    'L’épée des Dieux': 6614719,
                    'L’ultime Combat': 6614723,
                },
            },  
        },
    },
    'Bewitcher': {
        'id': 1820997,
        'albums': {
            'Cursed be thy Kingdom': {
                'id': 746405,
                'date': 'April 2021',
                'avgScore': 84,
                'TinTuna#2453': 87,
                'Tinngles#8236': 82,
                'Izual#1552': 84,
                'songs': {
                    'Death Returns...': 6584203,
                    'Satanic Magick Attack': 6382766,
                    'Electric Phantoms': 6584204,
                    'Mystifier (White Night City)': 6457433,
                    'Cursed Be Thy Kingdom': 6584205,
                    'Valley of the Ravens': 6584184,
                    'Metal Burner': 6584206,
                    'The Widow’s Blade': 6584207,
                    'Sign of the Wolf': 6584208,
                },
            },  
        },
    },
    # 'Helslave': {
    #     'id': 123,
    #     'albums': {
    #         'From the Sulphur Depths': {
    #             'id': 123,
    #             'date': 'April 2021',
    #             'avgScore': 78,
    #             'TinTuna#2453': 79,
    #             'Tinngles#8236': 78,
    #             'Izual#1552': 78,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    # 'Steel Bearing Hand': {
    #     'id': 123,
    #     'albums': {
    #         'Slay in Hell': {
    #             'id': 123,
    #             'date': 'April 2021',
    #             'avgScore': 72,
    #             'TinTuna#2453': 73,
    #             'Tinngles#8236': 72,
    #             'Izual#1552': 72,
    #             'songs': {
    #                 'songName': 123,
    #             },
    #         },  
    #     },
    # },
    'Kauan': {
        'id': 369046,
        'albums': {
            'Ice Fleet': {
                'id': 762884,
                'date': 'April 2021',
                'avgScore': 78,
                'TinTuna#2453': 92,
                'Tinngles#8236': 76,
                'Izual#1552': 66,
                'songs': {
                    'Maanpako': 6731487,
                    'Kutsu': 6731488,
                    'Raivo': 6731489,
                    'Ote': 6731490,
                },
            },  
        },
    },
}