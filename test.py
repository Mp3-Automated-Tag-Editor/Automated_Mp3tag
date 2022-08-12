#import test_MT
#import title_generator

# = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")
#print(songs_list)

#songs_list = test_MT.improve_name("[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3")
#print(songs_list)

#artist, album , song_name, albumart = test_MT.get_metadata("Do I wanna know", "e7ed7bbc0a5f4a7db0223a507f48be9a","bf5d451b496b47d795fdf6b5d556ea75")

#x,y = title_generator.regex_title_gen("[YT2mp3.info] - Arctic Monkeys - Do I Wanna Know_ (Official Video) (320kbps).mp3")

import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    
    return response

def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
        }
        
        output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)


results = google_search("web scraping")
results