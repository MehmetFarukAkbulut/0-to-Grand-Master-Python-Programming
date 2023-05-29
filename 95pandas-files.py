import sqlite3
import pandas as pd

df= pd.read_csv("datasets/sample.csv")
#        year industry_code_ANZSIC  ...    value               unit
# 0      2011                    A  ...    46134              COUNT
# 1      2011                    A  ...        0              COUNT
# 2      2011                    A  ...      279  DOLLARS(millions)
# 3      2011                    A  ...     8187  DOLLARS(millions)
# 4      2011                    A  ...     8866  DOLLARS(millions)
# ...     ...                  ...  ...      ...                ...
# 12379  2018                  all  ...   691859  DOLLARS(millions)
# 12380  2018                  all  ...   597623  DOLLARS(millions)
# 12381  2018                  all  ...    85574  DOLLARS(millions)
# 12382  2018                  all  ...  2068648  DOLLARS(millions)
# 12383  2018                  all  ...   499274  DOLLARS(millions)

# [12384 rows x 7 columns]
df=pd.read_json("datasets/sample.json",encoding="UTF-8")
#     Name  Grade
# 0  Ahmet     50
# 1    Ali     60
# 2  Faruk     70
# 3  Fatih     80
df=pd.read_excel("datasets/sample.xlsx")
#     Name  Grade
# 0    Ali     60
# 1  Ahmet     80
# 2  Faruk     90
# 3  Fatih     50
connection=sqlite3.connect("datasets/sample.db")
df=pd.read_sql_query("SELECT * FROM students",connection)
#    Id   Name  Grade
# 0   1  Ahmet     70
# 1   2    Ali     80
# 2   3  Faruk     90
# 3   4  Fatih     60

print(df)