# Bankamatik uygulaması

FarukHesap={
    "ad": "Faruk Akbulut",
    "hesapNo": "123456789",
    "bakiye": 3000,
    "ekHesap": 2000,
    "ekHesapLimiti": 2000
    
}
FatihHesap={
    "ad": "Fatih Akbulut",
    "hesapNo": "223456789",
    "bakiye": 15000,
    "ekHesap": 5000,
    "ekHesapLimiti": 5000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"]>= miktar):
        hesap["bakiye"]-= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam=hesap['bakiye']+ hesap['ekHesap']
        if (toplam>= miktar):
            ekHesapKullanimi=input("Ek hesap kullanılsın mı(e/h)")
            if ekHesapKullanimi=="e":
                ekHesapKullanilacakMiktar= miktar- hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else: print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:print("Üzgünüz, bakiye yetersiz.")
    bakiyeSorgula(hesap)
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. \nEk hesap liminitiniz ise {hesap['ekHesap']} Tl bulunmaktadır.")

def paraYatir(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap["ekHesapLimiti"]==hesap["ekHesap"] ):
        hesap["bakiye"]+= miktar
        print(f"Toplam {miktar} TL bakiyenize yatırdınız.")
    else:
        eksik=hesap["ekHesapLimiti"]-hesap["ekHesap"]
        if miktar>eksik:
            hesap["ekHesap"]+= eksik
            hesap["bakiye"]+= miktar-eksik
            print(f"Toplam {eksik} TL ek hesabınıza yatırdınız.\n{miktar-eksik} TL bakiyenize yatırdınız.")
        else:
            hesap["ekHesap"]+= miktar
            print(f"Toplam {miktar} TL ek hesabınıza yatırdınız.")
    bakiyeSorgula(hesap)
paraCek(FarukHesap, 2000)
print("*****************")
paraCek(FarukHesap, 3000)
print("*****************")
paraYatir(FarukHesap,2000)
print("*****************")
paraYatir(FarukHesap,3000)








