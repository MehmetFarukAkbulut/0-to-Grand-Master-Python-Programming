import pandas as pd

list= [["Ahmet",50],["Ali",60],["Faruk",70],["Fatih",80]]
dict={"Name":["Ahmet","Ali","Faruk","Fatih"],"Grade":[50,60,70,80]}
dict_list=  [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Faruk","Grade":70},
                {"Name":"Fatih","Grade":80}
            ]
# df= pd.DataFrame()
# df= pd.DataFrame([1,2,3,4])
# df=pd.DataFrame(list,columns=["Name","Grade"],index=[1,2,3,4])#istersek böyle yapabiliriz
# df=pd.DataFrame(list,[1,2,3,4],["Name","Grade"])#olması gereken sıra: list,index,columns
# df=pd.DataFrame(list,index=[1,2,3,4],columns=["Name","Grade"])#tavsiye edilen
#     Name  Grade
# 1  Ahmet     50
# 2    Ali     60
# 3  Faruk     70
# 4  Fatih     80

# df=pd.DataFrame(dict)
#     Name  Grade
# 0  Ahmet     50
# 1    Ali     60
# 2  Faruk     70
# 3  Fatih     80

df=pd.DataFrame(dict,index=["212","232","236","456"])
#       Name  Grade
# 212  Ahmet     50
# 232    Ali     60
# 236  Faruk     70
# 456  Fatih     80

df=pd.DataFrame(dict_list)
#     Name  Grade
# 0  Ahmet     50
# 1    Ali     60
# 2  Faruk     70
# 3  Fatih     80
df=pd.DataFrame(dict_list,index=["212","232","236","456"])
#       Name  Grade
# 212  Ahmet     50
# 232    Ali     60
# 236  Faruk     70
# 456  Fatih     80

print(df)




# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data= dict(apples=s1, oranges=s2)

# df=pd.DataFrame(data)
# #    apples  oranges
# # 0       3        0
# # 1       2        3
# # 2       0        7
# # 3       1        2

# print(df) 