import mysql.connector


def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()

    sql="INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)
    
    
    cursor.execute(sql,values)
    try:    
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:  {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")
        
def insertProducts(list):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()

    sql="INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values=list
    
    
    cursor.executemany(sql,values)
    try:    
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id:  {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")

def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    
    cursor.execute("Select * From Products")
    # cursor.execute("Select * From Products Where id=1")
    # cursor.execute("Select * From Products Where name='Samsung S8'")
    # cursor.execute("Select * From Products Where name='Samsung S8' and price>=3000 ")
    # cursor.execute("Select * From Products Where name='Samsung S8' or price>=3000 ")
    # cursor.execute("Select * From Products Where name LIKE '%Samsung%' ")
    # cursor.execute("Select * From Products Where name LIKE 'Samsung%' ")
    # cursor.execute("Select * From Products Where name LIKE '%Samsung%' and price=3000 ")
    
    
    result=cursor.fetchall()
    
    for product in result:
        # print(f"name: {product[1]} price: {product[2]}")
        print(f"id: {product[0]} name: {product[1]} price: {product[2]}")
    
def getProductById(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    sql="Select * From Products Where id=%s"
    params=(id,)
    cursor.execute(sql,params)
    
    
    result=cursor.fetchone()
    
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

getProductById(6)