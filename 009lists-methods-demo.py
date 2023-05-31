names=['Faruk','Mehmet','Fatih','Rümeysa']
years=[1998,2000,1991,1989,2000]

# Cenk ismini sona ekle
names.append('Cenk')
print(names)
# Sena ismini başa ekle
names.insert(0,'Sena')
print(names)
# Mehmet ismini sil
# names.pop(2)
names.remove('Mehmet')
print(names)
# Rümeysa isminin indeksi
index= names.index('Rümeysa')
print(index)

# Faruk listenin elemanı mı
print('Faruk' in names)
# liste elemanlarını ters çevir
names.reverse()
print(names)
# liste elemanlarını alfabetik sırala
print(names.sort())
# years listesini büyüklüğe göre sırala
print(years.sort())
# str="Chevrolet,Dacia" karakter dizisini listeye çevir
str="Chevrolet,Dacia".split(',')
print(str)
# years dizisinin en büyük en küçük elemanı
print(max(years))
print(min(years))
# years dzisinini kaç tane 2000 değeri var
print(years.count(2000))
#years dizisinin tüm elemanlarını sil
years.clear()
print(years)
#kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
marka1=input("Marka giriniz: ")
marka2=input("Marka giriniz: ")
marka3=input("Marka giriniz: ")
markalar=[marka1,marka2,marka3]
print(markalar)