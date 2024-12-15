import requests
from bs4 import BeautifulSoup

res = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(res.text, 'lxml')
soup.select('.author')
authors = set()
for name in soup.select('.author'):
    authors.add(name.text)

#######
quotes = []
for quote in soup.select('.quote'):
    quotes.append(quote.text)
soup.select('.text')

#######
for itme in soup.select('.tag-item'):
    print(itme.text)

######
url = 'http://quotes.toscrape.com/page/'
authors = set()
for page in range(1,10):
    page_url = url+str(page)
    res = requests.get(page_url)
    soup = BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
print(authors)