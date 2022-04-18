from click import group
from pywinauto import application
import sqlite3
from googlesearch import search
import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

cli_ID = "e7ed7bbc0a5f4a7db0223a507f48be9a"
cli_se = "bf5d451b496b47d795fdf6b5d556ea75"

#Music Records etc
#Create options for choosing directory
fdir = r'C:/Users/jonat/Music/Latest Songs'
songs_list =  os.listdir(fdir)

#Database Creation, Format: 
#{'Sl no. (Key)',[file_name, path, Tag, Title, Artist, Album, Year, Track, Genre, Comment, Album Artist, Composer, Discnumber, album art jpg file]}
connection  = sqlite3.connect('Music_database.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS MUSIC")
command1 = """CREATE TABLE IF NOT EXISTS
MUSIC( key INTEGER PRIMARY KEY, file_name TEXT, path TEXT, title TEXT, artist TEXT, album TEXT, year NUMBER, track NUMBER, genre TEXT, comment TEXT, album_artist TEXT, composer TEXT, discno NUMBER, album_art TEXT)"""
cursor.execute(command1)

count = 0
for i in songs_list:
    count+=1
    complete_path = f"{fdir}/{i}"
    print(complete_path)
    cursor.execute("INSERT INTO MUSIC values (?, ?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)",(count, i, complete_path))
print()

results = cursor.execute("SELECT * FROM MUSIC")
for row in results:
    print(row)
print(count)

#import title_generator

import re
import os
import data_scraper_final

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

counter = 0
for i in range(1,count):
    query = f"SELECT file_name FROM MUSIC WHERE key = {i}"
    fname = cursor.execute(query)
    c = 0
    for x in fname:
        x = convertTuple(x)
    song = x.split(" - ")[c]
    if(".is" in (song) or ".com" in (song) or ".info" in (song)):
        c += 1
        song = x.split("-")[c]
    artist = os.path.splitext("".join(x.split(" - ")[c+1:]))[0]
    idx = artist.rfind("Official")
    artist = artist[0:idx]
    idx = artist.rfind("Music")
    artist = artist[0:idx]
    idx = artist.rfind("Lyric")
    artist = artist[0:idx]
    if(len(song) == 0):
        song = artist

    #print("Song: " + artist)
    #print("Artist: "+ song)

    command2 = f"{artist} {song}"
    art, album , song_name, albumart, status = data_scraper_final.get_metadata(command2, cli_ID, cli_se,i)
    #print(art,album,song_name, albumart)
    #query = 
    #print(query)
    cursor.execute(f"UPDATE MUSIC SET title = ? , artist = ? , album = ? , album_art = ?  WHERE key = {i}",(song_name, art, album, albumart))
    #print(cursor.rowcount, f"Record inserted, {status}")

results = cursor.execute("SELECT * FROM MUSIC")
for row in results:
    print(row)
print(count)

import automation_script