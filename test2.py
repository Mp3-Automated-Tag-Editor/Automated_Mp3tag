# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
page = requests.get("https://en.wikipedia.org/wiki/Runaway_(Aurora_song)")

# display status code
print(page.status_code)

# display scrapped data
print(page.content)

# import required modules

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# display scrapped data
print(soup.prettify())

# import required modules


list(soup.children)

# find all occurrence of p in HTML
# includes HTML tags
print(soup.find_all('table'))

# return only text
# does not include HTML tags
print(soup.find_all('p')[0].get_text())

object = soup.find(id="mp-left")
 
# find tags
items = object.find_all('td')
result = items[0]
 
# display tags
print(result.prettify())