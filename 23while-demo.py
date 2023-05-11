sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
x=0
while not (x==len(sayilar)):
    print(sayilar[x])
    x+=1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
# tek sayıları ekrana yazdırın.
bas=int(input("başlangıç sayısı: "))
bit=int(input("bitiş sayısı: "))

while not (bas==bit+1):
    print(bas)
    bas+=1
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
sayi=100
while not(sayi<=0):
    print(sayi)
    sayi-=1
    
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
# yazdırın.

a=int(input("sayi: "))
b=int(input("sayi: "))
c=int(input("sayi: "))
d=int(input("sayi: "))
e=int(input("sayi: "))
sayilar=[a,b,c,d,e]
x=0
while x<5:
    print(max(sayilar))
    sayilar.remove(max(sayilar))
    x+=1
    
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı {name, price} şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunsayisi=int(input("Kaç ürün girmek istersiniz: "))
urunler=[]
x=0
while x<urunsayisi:
    name=input("Ürün adı : ")
    price=int(input("Ürün fiyatı : "))
    urunler.append({"name": name, "price":price})
    x+=1
x=0
while x<urunsayisi:
    print(urunler[x])
    x+=1