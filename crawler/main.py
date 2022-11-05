import requests
from bs4 import BeautifulSoup
import os
import sqlite3

url = os.getenv("BASE_URL")
res = requests.get(url)
data = BeautifulSoup(res.text, 'lxml')
data = data.find_all('div', class_="flw-item")

for datum in data:
    name = datum.find('h3', class_="film-name")
    name = name.text
    image = datum.img['data-src']
    watch_link = datum.a['href']

    print(name, image, watch_link)