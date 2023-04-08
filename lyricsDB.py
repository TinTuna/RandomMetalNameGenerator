import random
import useGeniusLyrics
import json

async def getLyrics():
    # Get a random artist
    artist = random.choice(list(data.keys()))
    artistData = data[artist]
    # Get a random song from the artist
    album = random.choice(list(data[artist]['albums'].keys()))
    # Get a random song from the artist and check if it has lyrics
    song, lyrics = await getSong(artist, album)
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

# load data from data.json

with open('data.json') as f:
    data = json.load(f)

async def getSong(artist, album):
    # Get a random song from the artist and check if it has lyrics
    song = random.choice(list(data[artist]['albums'][album]['songs'].keys()))
    # Get the lyrics of the song
    lyrics = await useGeniusLyrics.getLyrics(artist, album, song, data[artist]['albums'][album]['songs'][song])
    if lyrics == None:
        return getSong(artist, album)
    return song, lyrics