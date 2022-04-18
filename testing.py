import test_MT

songs_list = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")
print(songs_list)

songs_list = test_MT.improve_name("[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3")
print(songs_list)

artist, album , song_name, albumart = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")