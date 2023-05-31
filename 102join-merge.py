import pandas as pd
# customers={
#     "CustomerId":[1,2,3,4],
#     "FirstName":["Ahmet","Faruk","Fatih","Rümeysa"],
#     "LastName":["Yılmaz","Akbulut","Bal","Şener"] 
# }

# orders={
#     "OrderId":[10,11,12,13],
#     "CustomerId":[1,2,5,7],
#     "OrderDate":["2010-07-04","2018-09-04","2022-02-14","2019-10-04"]
    
# }

# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)


# result= pd.merge(df_customers,df_orders,how="inner") 
# #    CustomerId FirstName LastName  OrderId   OrderDate
# # 0           1     Ahmet   Yılmaz       10  2010-07-04
# # 1           2     Faruk  Akbulut       11  2018-09-04

# result= pd.merge(df_customers,df_orders,how="left") 
# #    CustomerId FirstName LastName  OrderId   OrderDate
# # 0           1     Ahmet   Yılmaz     10.0  2010-07-04
# # 1           2     Faruk  Akbulut     11.0  2018-09-04
# # 2           3     Fatih      Bal      NaN         NaN
# # 3           4   Rümeysa    Şener      NaN         NaN

# result= pd.merge(df_customers,df_orders,how="right") 
# #    CustomerId FirstName LastName  OrderId   OrderDate
# # 0           1     Ahmet   Yılmaz       10  2010-07-04
# # 1           2     Faruk  Akbulut       11  2018-09-04
# # 2           5       NaN      NaN       12  2022-02-14
# # 3           7       NaN      NaN       13  2019-10-04

# result= pd.merge(df_customers,df_orders,how="outer") 
# #    CustomerId FirstName LastName  OrderId   OrderDate
# # 0           1     Ahmet   Yılmaz     10.0  2010-07-04
# # 1           2     Faruk  Akbulut     11.0  2018-09-04
# # 2           3     Fatih      Bal      NaN         NaN
# # 3           4   Rümeysa    Şener      NaN         NaN
# # 4           5       NaN      NaN     12.0  2022-02-14
# # 5           7       NaN      NaN     13.0  2019-10-04

customersA={
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Faruk","Fatih","Rümeysa"],
    "LastName":["Yılmaz","Akbulut","Bal","Şener"] 
}
customersB={
    "CustomerId":[4,5,6,7],
    "FirstName":["Hanife","Yusuf","Umut","Tuğba"],
    "LastName":["Yılmaz","Akbulut","Bulut","Can"] 
}

df_customersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result=pd.concat([df_customersA,df_customersB])
result=pd.concat([df_customersA,df_customersB],axis=1)

print(result)