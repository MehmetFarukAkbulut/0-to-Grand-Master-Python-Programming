import numpy as np

# (10,15,30,45,60) değerleirne sahip numpy dizisi oluşturunuz.
result=np.array([10,15,30,45,60])
# (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
result=np.arange(5,15)
# (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result=np.arange(50,100,5)

# 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result=np.zeros(10)

# 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result=np.ones(10)

# (0-100) arasında eşit aralıklı 5 sayı üretin.
result=np.linspace(0,100,5)

# (10-30) arasında rastgele 5 tane tamsayı üretin.
result=np.random.randint(10,30,5)


# (-1 ile 1) arasında 10 adet sayı üretin.
result=np.random.randn(10)

# (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
np_array=np.random.randint(10,50,15)
np_multi=np_array.reshape(3,5)

# 10-Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?
result=np_multi.sum(axis=1)
result=np_multi.sum(axis=0)
# 11-Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
result=np_multi.max()
result=np_multi.min()
result=np_multi.mean()

# 12-Üretilen matrisin en büyük değerinin indeksi kaçtır 
result=np_multi.argmax()

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
np_array=np.arange(10,20)
result=np_array[:3]
# 14- Üretilen dizinin elemanlarını tersten yazdırın.
result=np_array[::-1]
# 15- Üretilen matrisin ilk satırını seçiniz.
result=np_multi[0,:]

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?
result=np_multi[1,2]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result=np_multi[:,0]

# 18- Üretilen matrisin her bir elemanının karesinin alınız. 
result=np_multi*np_multi

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#           Aralığı (-50,+50) arasında yapınız.
np_array=np.random.randint(-50,50,15)
np_multi=np_array.reshape(3,5)
cift=np_multi[np_multi%2==0]
result=cift[cift>=0]

print(np_multi)
print(result)