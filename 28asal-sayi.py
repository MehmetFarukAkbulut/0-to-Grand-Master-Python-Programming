# Girilen bir sayının asal olup olmadığını bulun
a=float(input("Sayı girin: "))
to=(a**0.5)+1
if a<=1: asalMi=False
    
else:
    asalMi= True
    for x in range(2,int(to)):
        if a%x==0:
            asalMi=False 
            break
if asalMi:print(f"{int(a)} sayısı asaldır.")
else:print(f"{int(a)} sayısı asal değildir.")