# 1-Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
# durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
# lise ya da üniversite olmalıdır.

isim=input("isim: ")
yas=int(input("yas: "))
egitim=input("eğitim(yok,ilkokul,ortaokul,lise,üniversite): ")
if yas>=18 and (egitim=="lise" or egitim=="üniversite" ):
    print(f"{isim} ehliyet alabilirsin.")
else:
    if yas<18:print(f"{isim} ehliyet alamazsın. Yaşın en az 18 olmalıdır.")
    elif not(egitim=="lise" or egitim=="üniversite" ):
        print(f"{isim} ehliyet alamazsın.Eğitim durumun lise ya da üniversite olmalıdır.")
    else: print(f"{isim} yanlış giriş yaptın.")

# 2-Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
# not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24 ->0
# 25-44 ->>1
# 45-54 ->2
# 55-69 -> 3
# 70-84 >4
# 85-100 -> 5
yazili1=float(input("Yazılı: "))
yazili2=float(input("Yazılı: "))
sozlu=float(input("Sözlü: "))
ortalama=(yazili1+yazili2+sozlu)/3
print("dersin ortalaması: ", ortalama)
if 100>=ortalama>=85:print("Dersin notu: 5")
elif 84>=ortalama>=70:print("Dersin notu: 4")
elif 69>=ortalama>=55:print("Dersin notu: 3")
elif 54>=ortalama>=45:print("Dersin notu: 2")
elif 44>=ortalama>=25:print("Dersin notu: 1")
elif 24>=ortalama>=0:print("Dersin notu: 0")
else: print("Yanlış bilgi girdiniz.")

# Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
# göre hesaplayınız.
# 1. Bakım -> 1. yıl
# 2. Bakım -> 2. yıl
# 3. Bakım -> 3. yıl
#* Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
# *** datetime modülünü kullanmanız gerekiyor.
import datetime
tarih=input("Aracın trafiğe çıkış yılını (yyyy/aa/gg) girin:")
tarih=tarih.split("/")
cikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
bugun = datetime.datetime.now()
fark = bugun - cikis
bakim1= datetime.timedelta(days=365)
bakim2= datetime.timedelta(days=365*2)
bakim3= datetime.timedelta(days=365*3)
if fark> bakim3:
    print("3. Bakım zamanı geçmiştir!")
elif fark > bakim2:
    print("3. Bakım zamanı yaklaşıyor!")
elif fark > bakim1:
    print("2. Bakım zamanı yaklaşıyor!")
else:
    print("1. Bakım zamanı yaklaşıyor!")