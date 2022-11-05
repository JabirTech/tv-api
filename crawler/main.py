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
    name = name.replace('\n', '')
    image = datum.img['data-src']
    watch_link = datum.a['href']

    connection = sqlite3.connect(os.path.join(os.getcwd(), 'db.sqlite3'))
    cur = connection.cursor()
    query = f"INSERT INTO movies VALUES ('{name}', '{image}', '{watch_link}')"
    cur.execute(query)
    cur.close()
    connection.commit()
    
    print(f'{name} added to the DB')