"""
ogrenciler={
    '120':{
        'ad': 'Faruk',
        'soyad': 'Akbulut',
        'telefon': '542 000 00 00'
    },
    '128':{
        'ad': 'Fatih',
        'soyad': 'Akbulut',
        'telefon': '542 000 00 01'
    },
    '130':{
        'ad': 'Rümeysa',
        'soyad': 'Akbulut',
        'telefon': '542 000 00 02'
    },
 }
 
1-   Bilgileri verilen öğrencileri kullanıcıdan aldığınz bilgilerle dictionary içinde saklayınız
2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz
"""

ogrenciNo1=input("İlk Öğrenci Numarasını giriniz: ")
ad1=input("Öğrenci Adını giriniz: ")
soyad1=input("Öğrenci Soyadını giriniz: ")
telefon1=input("Öğrenci Telefon Numarsını giriniz: ")
ogrenciNo2=input("İkinci Öğrenci Numarasını giriniz: ")
ad2=input("Öğrenci Adını giriniz: ")
soyad2=input("Öğrenci Soyadını giriniz: ")
telefon2=input("Öğrenci Telefon Numarsını giriniz: ")
ogrenciNo3=input("Üçüncü Öğrenci Numarasını giriniz: ")
ad3=input("Öğrenci Adını giriniz: ")
soyad3=input("Öğrenci Soyadını giriniz: ")
telefon3=input("Öğrenci Telefon Numarsını giriniz: ")
ogrenciler={
    ogrenciNo1:{
        'Ad':ad1,
        'Soyad':soyad1,
        'Telefon':telefon1
    },
    ogrenciNo2:{
        'Ad':ad2,
        'Soyad':soyad2,
        'Telefon':telefon2
    },
    ogrenciNo3:{
        'Ad':ad3,
        'Soyad':soyad3,
        'Telefon':telefon3
    },
}
print("*"*50)
ogrenciNo=input("Bilgilerini öğrenmek istediğiniz \nÖğrenci Numarasını giriniz: ")
ogrenci= ogrenciler[ogrenciNo]
print(f"Aradığınız {ogrenciNo} nolu öğrencinin \n   adı: {ogrenci['Ad']}\n   soyadı: {ogrenci['Soyad']}\n   Telefonu: {ogrenci['Telefon']}")