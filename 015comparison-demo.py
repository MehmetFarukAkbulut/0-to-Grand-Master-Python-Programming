# girilen 2 sayıdan hangisi büyük
a=int(input("sayı: "))
b=int(input("sayı: "))
if a>b:
    print("girilen 2 sayıdan hangisi büyük:",a)
elif a==b:print("girilen 2 sayıdan hangisi büyük: ikiside eşit")
else: print("girilen 2 sayıdan hangisi büyük: ",b)

# 2 vize (%60) ve final(%40) notunu alıp ortalama hesapla
vize1=float(input("vize1: "))
vize2=float(input("vize2: "))
final=float(input("final: "))
ort=(vize1+vize2)*0.3+final*0.4
print("2 vize (%60) ve final(%40) notunu alıp ortalama hesapla: ",ort)
#  eğer ort 50 üstüyse geçti değilse kaldı yazdırın
if ort>=50: print("geçti")
else: print("kaldı")
# girilen bir sayının tek mi çift mi olduğunu yazdırın
print("girilen bir sayının tek mi çift mi olduğunu yazdırın")
x=int(input("sayı: "))
if x%2:print("tek")
else:print("çift")
# girilen bir sayının negatif mi pozitif mi olduğunu yazdırın 
print("girilen bir sayının negatif mi pozitif mi olduğunu yazdırın ")
y=int(input("sayı: "))
if y<0:print("negatif")
else: print("poazitif")
# parola ve email bilgisini isteyip doğruluğunu kontrol edin
email="mefarukakbulut@gmail.com" 
password= "mfa123456"
e=input("email: ")
p=input("password: ")
if e==email and p==password:print("Hoşgeldiniz...")
else:print("yanlış email veya password girişi yaptınız")
    
    
    