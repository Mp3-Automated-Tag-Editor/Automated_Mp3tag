from pywinauto import application
import pywinauto
import time
import sqlite3
from googlesearch import search
import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import data_scraper

#app = Application(backend='uia').start(r"C:\Program Files (x86)\Mp3tag\Mp3tag.exe").connect(title=r'Mp3tag v3.03 - C:\Users\jonat\Music\Latest Songs',timeout=100)


#Music Records etc
songs_list =  os.listdir(r'C:\Users\jonat\Music\Latest Songs')
#database = {'key',[file_name, path, Tag, ]}
for i in songs_list:
    print(i)
    for j in search("wikipedia "+i, tld="co.in", num=20, stop=20, pause=2):
        print(j)
    print("wikipedia "+i)
    print()

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
    #print(i)
    #for j in search(i, tld="co.in", num=10, stop=10, pause=2):
        #print(j)
    cursor.execute("INSERT INTO MUSIC values (?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)",(count, i))
print()

cursor.execute("SELECT file_name FROM MUSIC WHERE key = 58")
results = cursor.fetchall()
print(results)