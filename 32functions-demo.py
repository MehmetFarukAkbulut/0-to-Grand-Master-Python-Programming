# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def kezGoster(letter="letter",num=1):
    return letter*num
print(kezGoster("faruk",3))
print(kezGoster("faruk"))
print(kezGoster())
# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
def lister(*args):
    return list(args)
print(lister(1,5,6,2,5,3,4,5,78,"Merhaba",4,531321,59,12,7))
# Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalMi(num):
    if num<2:
        return False
    else: 
        to=int((num**0.5+1))
        for x in range(2,to+1):
            if num%x==0:
                return False
            elif x==to:
                return True
def aradakiAsallar(sayi1,sayi2):
    print(f"{sayi1} ile {sayi2} arasındaki asallar:")
    if sayi1>sayi2:
        for a in range(sayi2,sayi1):
            if asalMi(a):
                print(a)
    elif sayi2>sayi1:
        for a in range(sayi1,sayi2):
            if asalMi(a):
                print(a)
    else :   
        if asalMi(a):
            print(a)   
aradakiAsallar(15,20)
# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def tambolen(num):
    list=[]
    for a in range(1,num+1):
        if num%a==0:
            list.append(a)
    return list
print(tambolen(250))