"""import requests
from data_scraper_final import add_album_art
import testing

x = "C:/Users/jonat/Music/Latest Songs/[YT2mp3.info] - Arctic Monkeys - R U Mine_ (Official Video) (320kbps).mp3"
y = "https://i.scdn.co/image/ab67616d0000b2734ae1c4c5c45aabe565499163"

add_album_art(x,y)

r = requests.get(y)
with open("wind-turbine.jpg", "wb") as f:
    f.write(r.content)"""

import os
import requests  # request img from web
import shutil  # save img locally

# url = input('Please enter an image URL (string):') #prompt user for img url
# file_name = input('Save image as (string):') #prompt user for file_name


def download(url, file_name):
    res = requests.get(url, stream=True)

    com_path = f"C:/Users/jonat/Music/Album Art/"+file_name
    print(com_path)
    if res.status_code == 200:
        with open(com_path, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        #print('Image sucessfully Downloaded: ',com_path)

        #os.startfile(com_path)
        #print(os.path.abspath(com_path))
        return com_path
