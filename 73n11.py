import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'

html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

print(html)

