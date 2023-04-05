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

# data = {
#     # 'artist name': {
#     #    'album': 'album name',
#     #    'date': month year,
#     #    'average rating': average rating,
#     # }
#     'Hulder': {
#         'Godslastering: Hymns of a Forlorn Peasantry': {
#             'date': 'January 2021',
#             'average rating': 62,
#         },
#     },
#     'Dread Sovereign': {
#         'Alchemical Warfare': {
#             'date': 'January 2021',
#             'average rating': 64,
#         },
#     },
#     'Asphyx': {
#         'Necroceros': {
#             'date': 'January 2021',
#             'average rating': 74,
#         },
#     },
# }
data = {
    # 'artistName': {
    #     'id': 123,
    #     'albums': {
    #         'albumName': {
    #             'id': 123,
    #             'date': 'date',
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
}