#import test_MT
#import title_generator

# = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")
#print(songs_list)

#songs_list = test_MT.improve_name("[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3")
#print(songs_list)

#artist, album , song_name, albumart = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")

#x,y = title_generator.regex_title_gen("[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3")


from mutagen.id3 import ID3, APIC, _util
from mutagen.mp3 import EasyMP3
import requests
import eyed3
import image_downloader
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
    print(audiofile.tag.images)
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