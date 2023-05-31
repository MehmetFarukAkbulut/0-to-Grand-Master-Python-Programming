import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Faruk Akbulut','Fatih Akbulut','Rümeysa Akbulut','Yusuf Şener','Umut Akbulut','Ayşe Neşe','Osman Can'],
    'Departman': ['Programlama','Muhasebe','Pazarlama','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [23,32,25,21,23,34,42],
    'Semt': ['Başakşehir','Tuzla','Başakşehir','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [15000,13000,18000,8500,8750,8500,8500]
}

df=pd.DataFrame(personeller)
result=df

result=df["Maaş"].sum()
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups

# for name,group in df.groupby("Semt"):
#     print(name)
#     print(group)
    
# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)

result=df.groupby("Semt").get_group("Başakşehir")
result=df.groupby("Departman").get_group("Muhasebe")
result=df.groupby("Departman").sum(["Yaş","Maaş"])#içine değer koymazsak stringleri de topluyor
result=df.groupby("Departman").mean(["Yaş","Maaş"])#içine değer koymazsak stringlerin ortalamasını alamıyor hata veriyor
result=df.groupby("Departman")["Maaş"].mean()
result=df.groupby("Semt")["Yaş"].mean()
result=df.groupby("Semt")["Maaş"].mean()
result=df.groupby("Semt")["Çalışan"].count()
result=df.groupby("Departman")["Yaş"].max()
result=df.groupby("Departman")["Maaş"].min()
result=df.groupby("Departman")["Maaş"].max()
result=df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result=df.groupby("Departman")[["Yaş","Maaş"]].agg(np.mean)#içine değer koymazsak stringlerin ortalamasını alamıyor hata veriyor
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]#içine değer koymazsak stringlerin ortalamasını alamıyor hata veriyor






print(result)