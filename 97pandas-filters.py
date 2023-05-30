import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5",] )


result=df
result=df.columns
# Index(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'], dtype='object')

result=df.head()#ilk 5 satır
result=df.head(10)#ilk 10 satır
result=df.tail()#son 5 satır
result=df.tail(10)#son 10 satır
result=df["Column1"].head()#colon1 in ilk 5 kaydı
result=df.Column1.head()#colon1 in ilk 5 kaydı
result=df[["Column1","Column2"]]#colon1 colon2 nin kayıtları
result=df[["Column1","Column2"]].head()#colon1 colon2 nin ilk 5 kaydı
result=df[["Column1","Column2"]].tail()#colon1 colon2 nin son 5 kaydı
result=df[5:15][["Column1","Column2"]].head()#colon1 colon2 nin 5 ve 15 kayıtları için ilk 5 kaydı(5,6,7,8,9)
result=df[5:15][["Column1","Column2"]].tail()#colon1 colon2 nin 5 ve 15 kayıtları için son 5 kaydı(10,11,12,13,14)

result=df>50#tüm değerler için 50 den büyüklere true yazar, olmayanlara false yazar
result=df[df>50]#tüm değerler için 50 den büyükleri yazar, olmayanlara değer girmez(NaN)
result=df[df%2==0]#tüm değerler için çift olanları yazar, olmayanlara değer girmez(NaN)
result=df["Column1"]>50#colon1 de 50 den büyük olanlara true olmayanlara false yazar
result=df[df["Column1"]>50]#tüm kolonlarda colon1 in 50 den büyük olduğu satırları getirir.
result=df[df["Column1"]>50][["Column1","Column2"]]# colon1 in 50 den büyük olduğu satırlarda colon1 ve colon2 nin kayıtlatını getirir.
result=df[(df["Column1"]>50)& (df["Column1"]<=70)]# colon1 in 50 den büyük 70den küçük olduğu tüm kolonların satırlarını  getirir.
result=df[(df["Column1"]>50)& (df["Column2"]<=70)]# colon1 in 50 den büyük ve colon2 nin 70den küçük olduğu tüm kolonların satırlarını  getirir.
result=df[(df["Column1"]>50)| (df["Column2"]<=70)]# colon1 in 50 den büyük veya colon2 nin 70den küçük olduğu tüm kolonların satırlarını  getirir.
result=df[(df["Column1"]>50)| (df["Column2"]>50)][["Column1","Column2"]]# colon1 veya colon2 nin 50 den büyük olduğu colon1 ve colon2 nin satırlarını  getirir.
result=df.query("Column1 >= 50 & Column1 % 2 == 0")# colon1 in çift, 50 den büyük eşit olduğu tüm kolonların satırlarını  getirir.
result=df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]# colon1 in çift, 50 den büyük eşit olduğu colon1 ve colon2 nin  satırlarını  getirir.
result=df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]# colon1 in çift veya 50 den büyük eşit olduğu colon1 ve colon2 nin  satırlarını  getirir.


print(result)
