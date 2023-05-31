import pandas as pd
import numpy as np
# data
numbers=[20,30,40,50]
letters=["a","b","c","d"]
scalar=5
dict={"a":10,"b":20,"c":30,"d":40}
random_numbers=np.random.randint(10,100,6)

# pandas_series= pd.Series()
# pandas_series=pd.Series(numbers)
# pandas_series=pd.Series(letters)  
# 0    a
# 1    b
# 2    c
# 3    d

# pandas_series=pd.Series(scalar,[0,1,2,3]) 
#0  5
#1  5
#2  5
#3  5
# pandas_series=pd.Series(numbers,["a","b","c","d"])
#a  20
#b  30 
#c  40
#d  50
# pandas_series=pd.Series(dict)
# a    10
# b    20
# c    30
# d    40
# pandas_series=pd.Series(random_numbers)
# 0    47
# 1    63
# 2    98
# 3    11
# 4    21
# 5    38

pandas_series=pd.Series([20,30,40,50],["a","b","c","d"])


# result=pandas_series[0]
# a   20
# result=pandas_series[-1]
# d   50
# result=pandas_series[:2]
# a   20
# b   30
# result=pandas_series[-2:]
# c   40
# d   50
# result=pandas_series["a"]
# 20
# result=pandas_series["d"]
# 50
# result=pandas_series[["a","c"]]
# a    20
# c    40
# result=pandas_series[["a","c","e"]]
# Exception has occurred: KeyError
# "['e'] not in index"
# result=pandas_series.ndim#1
# result=pandas_series.dtype#int64
# result=pandas_series.shape#(4,)
# result=pandas_series.sum()#140
# result=pandas_series.max()#50
# result=pandas_series.min()#20
# result=pandas_series.mean()#35.0
# result=pandas_series+pandas_series
# a     40
# b     60
# c     80
# d    100
# result=pandas_series+50
# a     70
# b     80
# c     90
# d    100
# result=np.sqrt(pandas_series)
# a    4.472136
# b    5.477226
# c    6.324555
# d    7.071068
# result=pandas_series>=50
# a    False 
# b    False
# c    False
# d     True
# result=pandas_series%3==0
# a    True
# b    True
# c    True
# d    True

 
# print(pandas_series[pandas_series%3==0])
# print(pandas_series)
# print(result)


# opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
# opel2023=pd.Series([70,100,80,60],["astra","corsa","Grandland","insignia"])

# total=opel2018+opel2023
# Grandland      NaN
# astra         90.0
# corsa        130.0
# insignia      70.0
# mokka          NaN

# print(total["astra"])
# 90.0
# print(total["combo"])
# KeyError: 'combo'


# print(total)