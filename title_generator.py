import os

def regex_title_gen(x):
    fname = x
    c = 0
    song = fname.split(" - ")[c]

    if(".is" in (song) or ".com" in (song) or ".info" in (song)):
        c += 1
        song = fname.split("-")[c]
    artist = os.path.splitext("".join(fname.split(" - ")[c+1:]))[0]
    if("Official" in artist):
        idx = artist.rfind("Official")
        artist = artist[0:idx]

    elif("official" in artist):
        idx = artist.rfind("official")
        artist = artist[0:idx]

    elif("Music" in artist):
        idx = artist.rfind("Music")
        artist = artist[0:idx]

    elif("Lyric" in artist):
        idx = artist.rfind("Lyric")
        artist = artist[0:idx]

    else:
        artist = artist

    if(len(song) == 0):
        song = artist

    if(song == ""):
        song = artist
    if (artist == ""):
        artist = song

    artist = artist.replace("_", " ").replace("(", " ")
    song = song.replace("_", " ").replace("(", "")
    temp = song
    song = artist
    artist = temp

    song = song.strip()
    artist = artist.strip()

    #print("song: " + song)
    #print("artist: "+artist)

    return song,artist
