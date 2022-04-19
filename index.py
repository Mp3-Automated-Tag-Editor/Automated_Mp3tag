import imp
from click import group
from pywinauto import application
import sqlite3
from googlesearch import search
import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from tqdm import tqdm

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
    #print(complete_path)
    cursor.execute("INSERT INTO MUSIC values (?, ?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)",(count, i, complete_path))
print()

results = cursor.execute("SELECT * FROM MUSIC")
for row in results:
    print(row)
print(count)

import data_scraper_final
import title_generator

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

counter = 0
for i in tqdm(range(1,count)):
    query = f"SELECT file_name FROM MUSIC WHERE key = {i}"
    fname = cursor.execute(query)
    for x in fname:
        x = convertTuple(x)
    
    song,artist = title_generator.regex_title_gen(x)

    #print("Song: " + song)
    #print("Artist: "+ artist)

    command2 = f"{song} {artist}"
    art, album , song_name, albumart, status = data_scraper_final.get_metadata(command2, cli_ID, cli_se,i)
    #print(art,album,song_name, albumart)
    cursor.execute(f"UPDATE MUSIC SET title = ? , artist = ? , album = ? , album_art = ?  WHERE key = {i}",(song_name, art, album, albumart))
    #print(cursor.rowcount, f"Record inserted, {status}")

    query = f"SELECT path FROM MUSIC WHERE key = {i}"
    fname = cursor.execute(query)
    for x2 in fname:
        x2 = convertTuple(x2)

    #data_scraper_final.revert_metadata(x2) #mutagen.mp3.HeaderNotFoundError: can't sync to MPEG frame ERROR
    ret2 = 1
    ret = data_scraper_final.add_metadata(x2, song_name, art, album)
    ret2 = data_scraper_final.add_album_art(x2, albumart, i)
    if ret == 0 or ret2 == 0:
        continue

    print(x2)

results = cursor.execute("SELECT * FROM MUSIC")
for row in results:
    print(row)
print(count)

#import automation_script

os.startfile(fdir)