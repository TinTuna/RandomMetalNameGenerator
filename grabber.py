import lyricsgenius
import json
import getGoogleSheet
import nanoid
import useEnvVars

client_access_token = useEnvVars.env_vars['GENIUS_ACCESS_TOKEN']

LyricsGenius = lyricsgenius.Genius(client_access_token)

# load artist_data.json existing dict
with open('artist_data.json') as f:
    data = json.load(f)


def getIDs(artist_name, album_name, date, Izual, Tinngles, TinTuna, avgScore):
    artist = LyricsGenius.search_artist(artist_name, max_songs=0)
    # if no artist found, return
    if artist is None:
        return
    if str(artist.name).lower() != str(artist_name).lower():
        print(artist.name + " is not " + artist_name)
        return
    album = LyricsGenius.search_album(artist_name, album_name)
    # if no album found, return
    if album is None:
        return
    # get the artist ID
    data[artist.name] = {}
    data[artist.name]['id'] = artist.id
    data[artist.name]['albums'] = {}
    data[artist.name]['albums'][album.name] = {}
    data[artist.name]['albums'][album.name]['id'] = album.id
    data[artist.name]['albums'][album.name]['date'] = date
    data[artist.name]['albums'][album.name]['avgScore'] = avgScore
    data[artist.name]['albums'][album.name]['TinTuna#2453'] = TinTuna
    data[artist.name]['albums'][album.name]['Tinngles#8236'] = Tinngles
    data[artist.name]['albums'][album.name]['Izual#1552'] = Izual
    data[artist.name]['albums'][album.name]['songs'] = {}
    # for each track in the album, get the track ID
    album_tracks = LyricsGenius.album_tracks(album.id)['tracks']
    print('Adding tracks from ' + album.name + ' by ' + artist.name)
    for track in album_tracks:
        data[artist.name]['albums'][album.name]['songs'][track['song']['title']] = track['song']['id']

band_data = getGoogleSheet.main('2023')
for band in band_data:
    # if the band name is blank, skip it
    if band[0] == '':
        continue
    # if the band is already in the dict, skip it
    for existingbandData in data:
        if str(band[0]).lower() == str(existingbandData).lower():
            continue
        
    # create the band in the dict
    data[band[0]] = {}
    data[band[0]]['id'] = nanoid.generate(size=10)
    data[band[0]]['geniusArtist'] = False
    data[band[0]]['albums'] = {}
    data[band[0]]['albums'][band[1]] = {}
    data[band[0]]['albums'][band[1]]['id'] = nanoid.generate(size=10)
    data[band[0]]['albums'][band[1]]['date'] = band[3]
    data[band[0]]['albums'][band[1]]['avgScore'] = band[7]
    data[band[0]]['albums'][band[1]]['TinTuna#2453'] = band[6]
    data[band[0]]['albums'][band[1]]['Tinngles#8236'] = band[5]
    data[band[0]]['albums'][band[1]]['Izual#1552'] = band[4]
    data[band[0]]['albums'][band[1]]['songs'] = {}

# remove duplicate keys
result = {}
for key,value in data.items():
    if value not in result.values():
        result[key] = value

# output data into a local file
with open('artist_data.json', 'w') as outfile:
    json.dump(result, outfile)


# with open('lyric_data.json') as f:
#     ldata = json.load(f)

# songs = [
#     'Vasio',
#     'Marcha Fúnebre',
#     'Magno Caos',
#     'Hecatombe'
# ]

# for song in songs:
#     ldata[nanoid.generate(size=10)] = song

# with open('lyric_data.json', 'w') as outfile:
#     json.dump(ldata, outfile)