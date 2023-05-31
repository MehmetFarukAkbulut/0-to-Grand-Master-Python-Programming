import pandas as pd
import numpy as np

data={
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["ab","bcad","ade","c","de"],
    
}


df=pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2=lambda x: x*x


result=df
result=df["Column2"].unique()#[10 20 13 25]
result=df["Column2"].nunique()#4
result=df["Column2"].value_counts()
# Column2
# 20    2
# 10    1
# 13    1
# 25    1
# Name: count, dtype: int64
result=df["Column1"]*2
result=df["Column1"].apply(kareal) 
# 0     1
# 1     4
# 2     9
# 3    16
# 4    25
# Name: Column1, dtype: int64
 
result=df["Column1"].apply(kareal2) 
result=df["Column1"].apply(lambda x: x*x) 


result=df["Column3"].apply(len) 
df["Column4"]=df["Column3"].apply(len) 
result=df.columns
result=len(df.columns)
result=df.index
result=len(df.index)
result=df.info

result=df.sort_values("Column2")
result=df.sort_values("Column3")
result=df.sort_values("Column3",ascending=False)

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df=pd.DataFrame(data)
df=df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

print(df)