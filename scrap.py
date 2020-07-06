from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


result = requests.get("https://medium.com/tag/artificial-intelligence")
src = result.content
soup = BeautifulSoup(src, 'html.parser')
title = []
claps= []
words = []
url2= []


for k in soup.find_all('span', {'class':"u-relative u-background js-actionMultirecommendCount u-marginLeft5"}):
      claps.append(k.text)

for k in soup.find_all(class_="cardChromeless u-marginTop20 u-paddingTop10 u-paddingBottom15 u-paddingLeft20 u-paddingRight20"):
        n = k.text
        n = len(n)
        words.append(n)

for k in soup.find_all(class_="postArticle-readMore"):
    for link in k.find_all('a'):
         url2.append(link.get('href'))

for k in soup.find_all('h3'):
        title.append(k.text)

print(claps)
print(len(claps))

print(words)
print(len(words))
print(len(title))
print(title)
print(url2)
print(len(url2))


medium = pd.DataFrame({'article_name':title,'url':url2,'words':words,'claps':claps})

print(medium)

np.savetxt('medium.txt', medium, fmt = '%s', delimiter='    /n     ')
medium.to_excel('medium.xlsx')
medium.to_csv('medium.csv')















