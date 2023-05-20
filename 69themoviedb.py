# themoviedb.org -> film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi

import requests


class theMovieDb:
    def __init__(self):
        self.api_url='https://api.themoviedb.org/3'
        self.api_key="442fe3f63bbdaa9d3bb7526dc579ff13"

        
    def getPopulars(self):
        response=requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getNowPlaying(self):
        response=requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getTopRated(self):
        response=requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getUpcoming(self):
        response=requests.get(f"{self.api_url}/movie/upcoming?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getSearchResults(self,keyword):
        response=requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
    
movieApi=theMovieDb()

while True:
    secim= input("1- Popular Movies\n2- Now Playing Movies\n3- Top Rated Movies\n4- Upcoming Movies\n5- Search Movies\n6- Exit\nSeçiminiz: ")

    if secim=="6":
        break
    else:
        if secim=="1":
            movies=movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim=="2":
            movies=movieApi.getNowPlaying()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim=="2":
            movies=movieApi.getNowPlaying()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim=="3":
            movies=movieApi.getTopRated()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim=="4":
            movies=movieApi.getUpcoming()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim=="5":
            keyword=input("Ara: ")
            movies=movieApi.getSearchResults({keyword})
            for movie in movies["results"]:
                print(movie["title"])
        else:
            print("Yanlış seçim yaptınız.")

