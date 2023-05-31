import datetime


def sayHello(name="My Son"):
    return "Hello "+name
    
msg= sayHello("Faruk")

print(msg)


def total(num1,num2):
    return num1+num2
result=total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2023- dogumYili

ageFaruk=yasHesapla(2000)
ageGoksu=yasHesapla(2002)
ageRum=yasHesapla(1998)
ageFatih=yasHesapla(1991)
print(ageFaruk,ageGoksu,ageFatih,ageRum)

def EmekliligeKacYilKaldi(dogumYili,isim="Vatandaş"):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT:Dogum yili
    OUTPUT:Hesaplanan yil bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    
    if emeklilik> 0:
        print(f'Merhaba Sayın {isim}. Emekliliğinize {emeklilik} yıl kaldı')
    elif emeklilik==0:
        print(f'Merhaba Sayın {isim}. Emekliliğiniz için tebrikler.')
    else:
        print(f"Merhaba Sayın {isim}. Zaten {-(emeklilik)} yıl önce emekli oldunuz")

EmekliligeKacYilKaldi(2000,"Faruk")
EmekliligeKacYilKaldi(1958)
EmekliligeKacYilKaldi(1957,"Mehmet")

print(help(EmekliligeKacYilKaldi))