#!/usr/bin/env python

import image_downloader
from eyed3.id3.frames import ImageFrame
import eyed3
from asyncio.windows_events import NULL
from itertools import count
import requests
import youtube_dl
import spotipy
import os
import re
from mutagen.id3 import ID3, APIC, _util
from mutagen.mp3 import EasyMP3
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials

x = 0

# Words to omit from song title for better results through spotify's API
chars_filter = "()[]{}-:_/=+\"\'"
words_filter = ('official', 'lyrics', 'audio', 'remixed', 'remix', 'video',
                'full', 'version', 'music', 'mp3', 'hd', 'hq', 'uploaded', 'explicit')


def improve_name(song_name):
    """
    Improves file name by removing words such as HD, Official,etc
    eg : Hey Jude (Official HD) lyrics -> Hey Jude
    This helps in better searching of metadata since a spotify search of
    'Hey Jude (Official HD) lyrics' fetches 0 results
    """

    try:
        song_name = os.path.splitext(song_name)[0]
    except IndexError:
        pass

    song_name = song_name.partition('ft')[0]

    # Replace characters to filter with spaces
    song_name = ''.join(
        map(lambda c: " " if c in chars_filter else c, song_name))

    # Remove crap words
    song_name = re.sub('|'.join(re.escape(key) for key in words_filter),
                       "", song_name, flags=re.IGNORECASE)

    # Remove duplicate spaces
    song_name = re.sub(' +', ' ', song_name)

    return song_name.strip()


def get_metadata(file_name, client_id, client_secret, fno):
    """
    Tries finding metadata through Spotify
    """
    counter = 0
    song_name = improve_name(file_name)  # Remove useless words from title
    client_credentials_manager = SpotifyClientCredentials(
        client_id, client_secret)

    spotify = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager)
    results = spotify.search(song_name, limit=1)
    try:
        results = results['tracks']['items'][0]  # Find top result
        album = results['album']['name']  # Parse json dictionary
        artist = results['album']['artists'][0]['name']
        song_title = results['name']
        album_art = results['album']['images'][0]['url']
        
        status = "successfully"
    except:
        print("Error Occured: Fno: ", fno, " - Data nulled")
        artist = album = song_title = album_art = NULL
        # count()
        status = "However metadata Scrape failed (Error Code: 1)"

    
    genre = album["genres"]
    year = album["release_date"]
    print(year)
    print(genre)

    return artist, album, song_title, album_art, status

# def count():
    # x+=1


def add_album_art(file_name, album_art, fno):
    """
    Add album_art in .mp3's tags
    """
    # print(file_name,album_art)
    if album_art == None or album_art == 0:
        print("Error: No Album Art")
        return 0

    com_path = image_downloader.download(album_art, f"{fno}.jpg")
    # 204/365 = 55.89% success rate - CAn be implemented

    audiofile = eyed3.load(file_name)


    if (audiofile.tag == None):
        audiofile.initTag()
    audiofile.tag.images.set(3, open(com_path, 'rb').read(), 'image/jpeg')

    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)            
    print("Successfull")
    
    try:
        """audio = EasyMP3(file_name, ID3=ID3)
        audio.add_tags()

        print("Error")
        audio.tags.add(
        APIC(
            encoding=3,  # UTF-8
            mime='image/png',
            type=3,  # 3 is for album art
            desc='Cover',
            data=open(com_path).read()  # Reads and adds album art
            )
        )
        audio.save()"""

        
    except _util.error:
        pass
    
    """audio.tags.add(
    APIC(
        encoding=3,  # UTF-8
        mime='image/png',
        type=3,  # 3 is for album art
        desc='Cover',
        data=open(com_path).read()  # Reads and adds album art
        )
    )
    audio.save()
    print("Successfull")"""
 
    return 1



def add_metadata(file_name, title, artist, album):
    """
    As the method name suggests
    """
    try:
        tags = EasyMP3(file_name)
        if title: 
            tags["title"] = title
        if artist:     
            tags["artist"] = artist
        if album:
            tags["album"] = album
        tags.save()
    except:
        print("Error: ",file_name)
    
    return 1


def get_current_metadata_tag(file_name, tag):
    tags = EasyMP3(file_name)
    if tag in tags:
        return tags[tag].pop()
    else:
        return "The metadata tag could not be found."


def revert_metadata(file_path):
    """
    Removes all tags from a mp3 file
    """
    tags = EasyMP3(file_path)
    try:
        tags.delete()
    except:
        print("The metadata tag could not be found.") 
    tags.save()

