import lyricsgenius
import json
import getGoogleSheet

env_vars = {}
with open('.env') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        env_vars[key] = value

client_access_token = env_vars['genius_access_token']

LyricsGenius = lyricsgenius.Genius(client_access_token)

# load data.json existing dict
with open('data.json') as f:
    data = json.load(f)


def getIDs(artist_name, album_name, date,Izual,Tinngles,TinTuna,avgScore):
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


band_data = getGoogleSheet.main('2021')
for band in band_data:
    if band[0] == '':
        continue
    getIDs(band[0],band[1],band[2],band[3],band[4],band[5],band[6])

band_data = getGoogleSheet.main('2022')
for band in band_data:
    if band[0] == '':
        continue
    getIDs(band[0],band[1],band[2],band[3],band[4],band[5],band[6])
    
band_data = getGoogleSheet.main('2023')
for band in band_data:
    if band[0] == '':
        continue
    getIDs(band[0],band[1],band[2],band[3],band[4],band[5],band[6])

# remove duplicate keys
result = {}
for key,value in data.items():
    if value not in result.values():
        result[key] = value

# output data into a local file
with open('data.json', 'w') as outfile:
    json.dump(result, outfile)