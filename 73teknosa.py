import requests
from bs4 import BeautifulSoup
main="https://www.teknosa.com"


url = 'https://www.teknosa.com/bilgisayar-tablet-c-116?page='
html=requests.get(url).content
soup=BeautifulSoup(html,'html.parser')


list= soup.find_all("div",{"id":"product-item"})

for l in list:
    try:
        name =l.get('data-product-name')
        link=l.find_all("a",{"class":"prd-link gowitPlp-js"})[0]["href"]
        link=main+link
        price=l.find("input")["value"]
        print(f"Name: {name}\nLink: {link}\nPrice: {price}")
    except Exception as e:
        print("Hata: ",e)
        break
    