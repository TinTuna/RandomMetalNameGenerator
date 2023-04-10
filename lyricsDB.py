import random
import useGeniusLyrics
import json

# load data from artist_data.json

with open('artist_data.json') as f:
    artist_data = json.load(f)
with open('lyric_data.json') as f:
    lyric_data = json.load(f)

async def getLyrics():
    # Get a random artist and album
    artist, artistData, album = getArtist()
    # Get a random song from the artist and check if it has lyrics
    song, lyrics = await getSong(artist, album)
    # Get a random wrong choice
    wrongChoice1 = random.choice(list(artist_data.keys()))
    # check if the wrong choice is the same as the artist
    while wrongChoice1 == artist:
        wrongChoice1 = random.choice(list(artist_data.keys()))
    # Get a random wrong choice
    wrongChoice2 = random.choice(list(artist_data.keys()))
    # check if the wrong choice is the same as the artist or the first wrong choice
    while wrongChoice2 == artist or wrongChoice2 == wrongChoice1:
        wrongChoice2 = random.choice(list(artist_data.keys()))
    return artistData, artist, album, song, lyrics, wrongChoice1, wrongChoice2

async def getSong(artist, album):
    # Get a random song from the artist and check if it has lyrics
    song = random.choice(list(artist_data[artist]['albums'][album]['songs'].keys()))
    song_id = artist_data[artist]['albums'][album]['songs'][song]
    if artist_data[artist]['geniusArtist']:
        # artist is genius artist
        # Get the lyrics of the song
        lyrics = await useGeniusLyrics.getLyrics(artist, album, song, song_id)
        if lyrics == None:
            return await getSong(artist, album)
    else:
        # artist is not genius artist
        # Get the lyrics of the song from lyric_data
        lyrics = lyric_data[song_id]
    # limit lyrics to 1500 characters
    if len(lyrics) > 1500:
        lyrics = lyrics[:1500]
        lyrics = lyrics + '...\n\n'
        lyrics = lyrics + '**Damn those lyrics are long! I\'m only showing you the first 1500 characters.**'
    return song, lyrics

def getArtist():
    # Get a random artist
    artist = random.choice(list(artist_data.keys()))
    # check artist has albums
    if len(artist_data[artist]['albums']) == 0:
        return getArtist(artist)
    # check if artist is genius artist ## TODO will remove this condition later
    if artist_data[artist]['geniusArtist']:
        # artist is genius artist
        # Get a random album from the artist
        album = random.choice(list(artist_data[artist]['albums'].keys()))
        # check if album has songs
        if len(artist_data[artist]['albums'][album]['songs']) == 0:
            return getArtist()
        else:
            artistData = artist_data[artist]
            return artist, artistData, album
    else:
        # artist is not genius artist
        return getArtist()

    