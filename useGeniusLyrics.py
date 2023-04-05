from bs4 import BeautifulSoup
import re
import lyricsgenius
import requests
from pathlib import Path


env_vars = {}
with open('.env') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        env_vars[key] = value

client_access_token = env_vars['genius_access_token']

LyricsGenius = lyricsgenius.Genius(client_access_token)

async def getLyrics(artist_name, album_name, song_name, song_id):
    # Get the lyrics of the song
    lyrics = LyricsGenius.lyrics(song_id)
    # if lyrics ends with "You might also likeEmbed" remove it
    if lyrics.endswith('You might also likeEmbed'):
        lyrics = lyrics[:-24]
    # if lyrics still ends in "Embed", remove it
    if lyrics.endswith('Embed'):
        lyrics = lyrics[:-5]
    # cut out all content before and including the word 'Lyrics'
    lyrics = re.sub(r'.*Lyrics', '', lyrics) 
    return lyrics

def download_album_lyrics(artist, album_name): 
    
    # Set up LyricsGenius with your Genius API client access token
    #client_access_token = Your-Client-Access-Token
    LyricsGenius = lyricsgenius.Genius(client_access_token)
    LyricsGenius.remove_section_headers = True
    
    # With the function that we previously created, go to Genius.com and get all song titles for a particular artist's album
    clean_songs = get_all_songs_from_album(artist, album_name)
    
    for song in clean_songs:
        
        #For each song in the list, search for that song with LyricsGenius
        song_object = LyricsGenius.search_song(song, artist)
        
        #If the song is not empty
        if song_object != None:
            
            #Do some cleaning and prep for the filename of the song
            artist_title = artist.replace(" ", "-")
            album_title = album_name.replace(" ", "-")
            song_title = song.replace("/", "-")
            song_title = song.replace(" ", "-")
            
            #Establish the filename for each song inside a directory that begins with the artist's name and album title
            custom_filename=f"{artist_title}_{album_title}/{song_title}"
            
            #A line of code that we need to create a directory
             #os.makedirs(os.path.dirname(filename), exist_ok=True)
            Path(f"{artist_title}_{album_title}").mkdir(parents=True, exist_ok=True)
            
            #Save the lyrics for the song as a text file
            song_object.save_lyrics(filename=custom_filename, extension='txt', sanitize=False)
        
        #If the song doesn't contain lyrics
        else:
            print('No lyrics')

def get_all_songs_from_album(artist, album_name):
    
    artist = artist.replace(" ", "-")
    album_name = album_name.replace(" ", "-")
    
    response = requests.get(f"https://genius.com/albums/{artist}/{album_name}")
    html_string = response.text
    document = BeautifulSoup(html_string, "html.parser")
    song_title_tags = document.find_all("h3", attrs={"class": "chart_row-content-title"})
    song_titles = [song_title.text for song_title in song_title_tags]
    
    clean_songs = []
    for song_title in song_titles:
        clean_song = clean_up(song_title)
        clean_songs.append(clean_song)
        
    return clean_songs

def clean_up(song_title):

    if "Ft" in song_title:
        before_ft_pattern = re.compile(".*(?=\(Ft)")
        song_title_before_ft = before_ft_pattern.search(song_title).group(0)
        clean_song_title = song_title_before_ft.strip()
        clean_song_title = clean_song_title.replace("/", "-")
    
    else:
        song_title_no_lyrics = song_title.replace("Lyrics", "")
        clean_song_title = song_title_no_lyrics.strip()
        clean_song_title = clean_song_title.replace("/", "-")
    
    return clean_song_title