from itertools import count
import re
import os

counter = 0
#for i in index.count:
 #   fname = cursor.execute("SELECT file_name FROM MUSIC WHERE key = ?", (i))
fname = "y2mate.com - all_sons_daughters_great_are_you_lord_official_live_concert_uHz0w-HG4iU_256kbps.mp3"
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
#if(len(song) == 0):
#   artist=song

print("song: " +  artist)
print("artist: "+ song )


mycursor = mydb.cursor()

mycursor.execute("INSERT INTO MUSIC (title, artist) VALUES (?, ?)", (song, artist))

    #print(mycursor.rowcount, "record inserted. successfully")

