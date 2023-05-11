# logical demodaki soruların if elsele çözümü. zaten ben if else i bildiğim için böyle çözmüştüm
# bu yüzden direk o kodları yapıştırdım ve biraz düzenledim
# girilen bir sayının 0-100 arsında olup olmadığını kontrol edin
a=int(input("girilen bir sayının 0-100 arasında olup olmadığını kontrol edin: "))
if 0<a<100:print(f"{a} 0-100 arasında")
else:print(f"{a} 0-100 arasında değil")
# girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin

b=int(input("girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin: "))
if 0<=b and b%2==0:print(f"{b} pozitif çift sayı ")
else:print(f"{b} pozitif çift sayı değil")
# email ve parola bilgileri ile giriş kontrolü yapın
email="mefarukakbulut@gmail.com" 
password= "mfa123456"
print("mfa123456mefarukakbulut@gmail.com")
e=input("email: ")
p=input("password: ")
if e==email:
    if p==password:print("Hoşgeldiniz...")
    else: print("yanlış password girişi yaptınız")
else:print("girdiğiniz email bulunmuyor")
# girilen 3 sayıyı büyüklük olarak karşılaştır
print("Girilen 3 sayıyı büyüklük olarak karşılaştır")
a=int(input("sayı1: "))
b=int(input("sayı2: "))
c=int(input("sayı3: "))
if a==b:
    if a==c:print(f"{a}={b}={c}")
    elif c>a:print(f"{c}>{a}={b}")
    else:print(f"{a}={b}>{c}")
elif c==b:
    if a>b:print(f"{a}>{b}={c}")
    else:print(f"{b}={c}>{a}")
elif a>b:
    if b>c:print(f"{a}>{b}>{c}")
    elif a>c:print(f"{a}>{c}>{b}")
    else:print(f"{c}>{a}>{b}")
elif b>a:
    if a>c:print(f"{b}>{a}>{c}")
    elif b>c:print(f"{b}>{c}>{a}")
    else:print(f"{c}>{b}>{a}")
else: print("hatalı giriş")
# 2 vize (%60) ve final(%40) notunu alıp ortalama hesapla
vize1=float(input("vize1: "))
vize2=float(input("vize2: "))
final=float(input("final: "))
ort=(vize1+vize2)*0.3+final*0.4
print("2 vize (%60) ve final(%40) notunu alıp ortalama hesapla: ",ort)
#  eğer ort 50 ve üstüyse geçti değilse kaldı yazdırın
# a) eğer ort 50 olsa bilefinal notu en az 50 olmalıdır
# a) finalden 70 alındığında her türlü geçilsin
if ort>=50 and final>=50  : print("geçti")
elif final>=70:print("geçti")
else: print("kaldı")
# kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesapla
# vki=kilo/boy**2
# kişi hangi sınıftadır
# 0<vki<18.4 =>zayıf
# 18.5<vki<24.9 =>normal
# 25.0<vki<29.9 =>fazla kilolu
# 30.0<vki<34.9 =>şişman

ad=input("Ad: ")
c=input("Cinsiyet(e/k): ")
kilo=float(input("Kilo: "))
boy=float(input("Boy(cm): "))
vki=kilo/((boy/100)**2)
if c=='e':unvan='Bey'
elif c=='k':unvan='Hanım'
else:unvan=''
if 0<vki<18.4:print(f"Merhaba {ad} {unvan} Vücut kitle endeksinize göre siz zayıfsınız.")
elif 18.5<vki<24.9:print(f"Merhaba {ad} {unvan} Vücut kitle endeksinize göre siz normal kilodasınız.")
elif 25.0<vki<29.9:print(f"Merhaba {ad} {unvan} Vücut kitle endeksinize göre siz fazla kilolusunuz.")
else:print(f"Merhaba {ad} {unvan} Vücut kitle endeksinize göre siz şişmansınız.")