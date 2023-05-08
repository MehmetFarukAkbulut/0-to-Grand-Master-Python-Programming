import datetime
musteriAdi="Faruk"
musteriSoyadi="Akbulut"
musteriAdSoyad=musteriAdi+' '+musteriSoyadi
musteriCinsiyet= True #Erkek
musteriTC= "12345678901"
musteriDGYili= 2000
musteriAdres="Başakşehir/İstanbul"
musteriYas= datetime.datetime.now().year-musteriDGYili
print(musteriAdi)
print(musteriSoyadi)
print(musteriAdSoyad)
print(musteriCinsiyet)
print(musteriTC)
print(musteriDGYili)
print(musteriAdres)
print(musteriYas)

order1=110
order2=110.5
order3=356.95
total= order1+ order2+ order3
print("Total: ",total," TL")
