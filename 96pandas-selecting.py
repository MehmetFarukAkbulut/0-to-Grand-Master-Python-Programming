import pandas as pd 
from numpy.random import randn

df=pd.DataFrame(randn(3,3), index=["A","B","C"],columns=["Column1","Column2","Column3"])
#     Column1   Column2   Column3
# A  0.520129  0.044361  0.365237
# B -0.476420  0.271533 -0.683728
# C  1.828554  2.075625  1.620518

result=df
result=df["Column1"]
# A    0.465468
# B    0.783657
# C   -0.291373
# Name: Column1, dtype: float64

result=type(df["Column1"])
# <class 'pandas.core.series.Series'>

result=df[["Column1","Column2"]]
#     Column1   Column2
# A  1.242764 -0.986966
# B -0.958101  1.867637
# C  0.477860 -0.312726
    
result=df.loc["A"]
# Column1    0.520129  
# Column2    0.044361  
# Column3    0.365237
# Name: A, dtype: float64

result=type(df.loc["A"])
# <class 'pandas.core.series.Series'>

result=df.iloc[2] #index numarsı ile çağırmak için iloc
# Column1   -2.735332
# Column2    1.631114
# Column3    0.414378
# Name: C, dtype: float64

# loc["row","column"] => loc["row"]=> loc[:,"column"]

result=df.loc[:,"Column1"]
# A   -0.639999
# B   -1.403322
# C   -0.579069
# Name: Column1, dtype: float64

result=df.loc[:,["Column1","Column2"]]
#     Column1   Column2
# A  0.162255 -0.353831
# B  1.741845  0.124315
# C -0.842529 -0.908416

result=df.loc[:,"Column1":"Column3"]
#     Column1   Column2   Column3
# A  0.826483  0.735595  0.728696
# B -0.484237  1.362562 -0.616748
# C  0.524779 -0.763938  0.803698
result=df.loc[:,:"Column2"]
#     Column1   Column2
# A  2.148077  0.490610
# B -1.068895 -1.497528
# C -0.525926 -0.521828
result=df.loc["A":"B",:"Column2"]
result=df.loc[:"B",:"Column2"]
#     Column1   Column2
# A -1.168933  0.912076
# B  0.343859 -0.573893
result=df.loc["A","Column2"]
# -0.9645410399157738
result=df.loc["C","Column1"]
# 0.4524829281587439
result=df.loc[["A","B"],["Column1","Column2"]]
#     Column1   Column2
# A  0.261808 -1.469668
# B -0.049207 -0.104174

df["Column4"]=pd.Series(randn(3),["A","B","C"])
#     Column1   Column2   Column3   Column4
# A  1.017867  0.381653 -0.429703 -1.941897
# B  0.290527 -0.786197 -1.149566 -1.026594
# C -0.768416 -0.166715 -0.803716 -2.411891

df["Column5"]=df["Column1"]+df["Column3"]
#     Column1   Column2   Column3   Column4   Column5
# A -0.563920  2.074155  0.107125  0.249550 -0.456796
# B -0.733263  0.140448 -0.223963  1.370424 -0.957226
# C -1.149860 -0.442619 -0.024359  0.310711 -1.174220

result=df.drop("Column5",axis=1)
#     Column1   Column2   Column3   Column4
# A -0.652239  1.027662  0.728289 -0.703243
# B  0.950384 -0.063093 -0.287206 -0.831605
# C -1.417034 -0.941035  2.400922 -0.912594
# print(df)
#     Column1   Column2   Column3   Column4   Column5
# A -0.652239  1.027662  0.728289 -0.703243  0.076051
# B  0.950384 -0.063093 -0.287206 -0.831605  0.663178
# C -1.417034 -0.941035  2.400922 -0.912594  0.983887

result=df.drop("Column5",axis=1,inplace=False)#droptan dönecek değeri değiştiriyor orjinal hali kalıyor
# result=df.drop("Column5",axis=1,inplace=True)#droptan dönecek değeri orjinal hali yapıyor

print(result)
#     Column1   Column2   Column3   Column4
# A  0.541377  0.722057 -0.534439 -0.584232
# B  1.517077 -1.091207 -1.827052  2.090768
# C -0.056812  0.381997  1.837619  1.175075
print(df)
#     Column1   Column2   Column3   Column4   Column5
# A  0.541377  0.722057 -0.534439 -0.584232  0.006938
# B  1.517077 -1.091207 -1.827052  2.090768 -0.309975
# C -0.056812  0.381997  1.837619  1.175075  1.780807
