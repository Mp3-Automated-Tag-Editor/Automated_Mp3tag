from pywinauto import application
import pywinauto
import time
import sqlite3
from googlesearch import search
import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
#import data_scraper

#app = Application(backend='uia').start(r"C:\Program Files (x86)\Mp3tag\Mp3tag.exe").connect(title=r'Mp3tag v3.03 - C:\Users\jonat\Music\Latest Songs',timeout=100)


#Music Records etc
songs_list =  os.listdir(r'C:/Users/jonat/Music/Latest Songs')
#database = {'key',[file_name, path, Tag, ]}
#for i in songs_list:
    #print(i)
    #for j in search("wikipedia "+i, tld="co.in", num=20, stop=20, pause=2):
    #    print(j)
    #print("wikipedia "+i)
    #print()

#Database Creation, Format: 
#{'Sl no. (Key)',[file_name, path, Tag, Title, Artist, Album, Year, Track, Genre, Comment, Album Artist, Composer, Discnumber, album art jpg file]}
connection  = sqlite3.connect('Music_database.db')
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
MUSIC( key INTEGER PRIMARY KEY, file_name TEXT, tag TEXT, title TEXT, artist TEXT, album TEXT, year NUMBER, track NUMBER, genre TEXT, comment TEXT, album_artist TEXT, composer TEXT, discno NUMBER, album_art TEXT)"""
cursor.execute(command1)

count = 0
for i in songs_list:
    count+=1
    cursor.execute("INSERT INTO MUSIC values (?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)",(count, i))
print()

results = cursor.execute("SELECT * FROM MUSIC")
for row in results:
    print(row)
print(count)

#import title_generator

import re
import os

counter = 0
for i in range(1,count):
    fname = cursor.execute("SELECT file_name FROM MUSIC WHERE key = %d", (i))
    #fname = "[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3"
    c = 0
    song = fname.split(" - ")[c]
    if(".is" in (song) or ".com" in (song) or ".info" in (song)):
        c += 1
        song = fname.split("-")[c]
    artist = os.path.splitext("".join(fname.split(" - ")[c+1:]))[0]
    idx = artist.rfind("Official")
    artist = artist[0:idx]
    idx = artist.rfind("Music")
    artist = artist[0:idx]
    idx = artist.rfind("Lyric")
    artist = artist[0:idx]
    if(len(song) == 0):
        song = artist

    print("song:- " + song)
    print("artist:- "+artist)


    cursor.execute("INSERT INTO MUSIC (title, artist) VALUES (?, ?)", (song, artist))

    #print(mycursor.rowcount, "record inserted. successfully")

for row in results:
    print(row)
print(count)

#import data_scraper

#import automation_script