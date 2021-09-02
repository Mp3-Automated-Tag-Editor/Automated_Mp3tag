import nltk
from nltk.util import pr
from bs4 import BeautifulSoup
import urllib.request
import sys
import numpy

data_paragraph = "“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. “Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy. They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird"
tokens3_1 = nltk.word_tokenize(data_paragraph)
tokens3_2 = nltk.sent_tokenize(data_paragraph)
print("Tokens for the Sentence: "+data_paragraph+" are as follows: \n")
print (tokens3_1)
print()
print("Tokens for the multiple Sentence: "+data_paragraph+" are as follows: \n")
print (tokens3_2)
print()

data_url = 'https://thoughtcatalog.com/koty-neelis/2015/06/31-of-the-most-beautiful-and-profound-passages-in-literature-youll-want-to-read-over-and-over-again/'
#data_url = 'https://www.scrapethissite.com/pages/simple/'
response = urllib.request.urlopen(data_url)
html = response.read()
soup = BeautifulSoup(html,"html.parser")
text = soup.find('main')
tokens4 = []
for i in text.findAll('h4'): #, attrs={'class': 'row'}
    article_tokens = nltk.word_tokenize(i.text)
    print(article_tokens)
    tokens4 += article_tokens
    #tokens4.append(article_tokens)
    #print(i.text)
#print(text)


#print(tokens4)

#for j in tokens4:
    #print(j)

# Ask Sir why the list tokens4 stops midway without collecting all values of artiles_tokens