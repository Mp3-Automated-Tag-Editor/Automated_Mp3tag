from pywinauto import application
import pywinauto
import time
from googlesearch import search
import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

#app = Application(backend='uia').start(r"C:\Program Files (x86)\Mp3tag\Mp3tag.exe").connect(title=r'Mp3tag v3.03 - C:\Users\jonat\Music\Latest Songs',timeout=100)


#Music Records etc
songs_list =  os.listdir(r'C:\Users\jonat\Music\Latest Songs')
#database = {'key',[file_name, path, Tag, ]}
for i in songs_list:
    print(i)
    for j in search(i, tld="co.in", num=10, stop=10, pause=2):
        print(j)
    print()
