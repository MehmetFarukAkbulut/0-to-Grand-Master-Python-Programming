# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile

# buldurmaya çalışın.

# ** 100 üzerinden puanlama yapın. Her soru 20 puan.

# #** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
# üzerinden hesaplansın.

# ** "random modülü" için "python random" şeklinde arama yapın.
import random
num=random.randint(1,100)
score=100
hak=int(input("Kaç hak istersiniz: "))
ceza=100//hak
sayac=0
while hak>0:
    sayac+=1
    tahmin=int(input("Tahmininiz: "))
    
    if tahmin==num:
        print(f"Tebrikler, {sayac}. defada doğru bildiniz!")
        break
    elif tahmin< num:
        print("Daha yüksek bir sayı girin.")
        score-=ceza
    else:
        print("Daha düşük bir sayı girin.")
        score -=ceza
    hak -= 1
if hak==0:
    print("Hakkınız kalmadı.Doğru cevap: ",num)
        
print("Puanınız: ", score)