x,y,z=2,5,107
numbers=1,5,7,10,6
print("x,y,z: ",x,y,z)
print("numbers: ",numbers)
# kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı
a=int(input("sayı:"))
b=int(input("sayı:"))
print("Verdiğiniz 2 sayının çarpımı ile x,y,z toplamının farkı: ",a*b-(x+y+z))
# y nin x e kalansız bölümünü hesaplayınız
print("y nin x e kalansız bölümünü hesaplayınız: ",y//x)
# x,y,z nin toplamının mod 3 ü
print("x,y,z nin toplamının mod 3 ü:",(x+y+z)%3)
# ynin xinci kuvvetini hesaplayınız
print("ynin xinci kuvvetini hesaplayınız: ",y**x)
# x, *y,z= numbers işlemine göre z nin küpü kaçtır
x, *y,z= numbers
print("x, *y,z= numbers işlemine göre z nin küpü kaçtır: ",z**3)
# x, *y,z= numbers işlemine göre y nin değerleri toplamı kaçtır
print(y)
print("x, *y,z= numbers işlemine göre y nin değerleri toplamı kaçtır: ",y[0]+y[1]+y[2])
