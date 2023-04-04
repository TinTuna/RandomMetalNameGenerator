import random

def getLyrics():
    # Get a random artist
    artist = random.choice(list(data.keys()))
    # Get a random song from the artist
    song = random.choice(list(data[artist].keys()))
    # Get the lyrics of the song
    lyrics = data[artist][song]
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
    return artist, song, lyrics, wrongChoice1, wrongChoice2

data = {
    # artist: {
    #    'song': 'lyrics',
    #    'song': 'lyrics'
    # }
    'artist1': {
        'song1': 'lyrics1',
        'song2': 'lyrics2'
    },
    'artist2': {
        'song3': 'lyrics3',
        'song4': 'lyrics4'
    },
    'artist3': {
        'song5': 'lyrics5',
        'song6': 'lyrics6'
    },
    'artist4': {
        'song7': 'lyrics7',
        'song8': 'lyrics8'
    },
    'artist5': {
        'song9': 'lyrics9',
        'song0': 'lyrics0'
    }

}