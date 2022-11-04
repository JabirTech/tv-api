import requests
from bs4 import BeautifulSoup
import os

url = os.getenv("BASE_URL")
res = requests.get(url)
data = BeautifulSoup(res.text, 'lxml')
data = data.find_all('div', class_="flw-item")

print(len(data))