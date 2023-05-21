import requests
from bs4 import BeautifulSoup

main = "https://platform.win-eurasia.com"



for a in range(1,676):
    
    print(f"{a}. sayfa: ")
    url = 'https://platform.win-eurasia.com/participants?page='+str(a)    
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    list_items = soup.find_all("div", {"class": "list__item"})
    try:
        for item in list_items:
            name = item.find("div", {"class": "list__company"}).text.strip()
            print(name)

            description = item.find_all("div", {"class": "list__description"})[0].text.strip()
            print(description)

            link = item.find("div", {"class": "list__company"}).find("a")["href"]
            link = main + link
            print(link)

            html1 = requests.get(link).content
            soup1 = BeautifulSoup(html1, 'html.parser')
            communication = soup1.find_all("a", {"class": "company-info-platform"})

            for comm_link in communication:
                info = comm_link.text.strip().split(": ")
                print(info[0] + ":", info[1])
    except Exception as e:
        print("Hata: ",e)
        continue