import requests
import re
from bs4 import BeautifulSoup

url = "http://stackoverflow.com"
html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")
find_href = soup.findAll('a')
for x in find_href:
    print(x['href'])
