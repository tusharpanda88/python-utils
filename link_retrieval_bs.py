import requests as req
from bs4 import BeautifulSoup

url = "http://www.theplantlist.org/browse/-/"
response = req.get(url=url)

soup = BeautifulSoup(response.content,"lxml")
urls = [a_tag.get('href') for a_tag in soup.find_all('a') if a_tag.get('href').startswith('http')]

print(urls)
