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
    
    # cursor.execute("Select * From Products Order By name")
    # cursor.execute("Select * From Products Order By price")
    # cursor.execute("Select * From Products Order By price DESC")
    # cursor.execute("Select * From Products Order By id DESC")
    cursor.execute("Select * From Products Order By price, name")
    
    try:
        result=cursor.fetchall()
        for product in result:
            print(f"id: {product[0]} name: {product[1]} price: {product[2]}")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")
    

    
def getProductById(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    sql="Select * From Products Where id=%s"
    params=(id,)
    cursor.execute(sql,params)
    
    
    result=cursor.fetchone()
    
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

def getProductInfo():
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    
    # sql="Select COUNT(*) From Products"
    # sql="Select AVG(Price) From Products"
    # sql="Select SUM(Price) From Products"
    # sql="Select MAX(Price) From Products"
    # sql="Select MIN(Price) From Products"
    sql="Select Name,Price From Products Where Price= (Select MAX(Price) From Products)"

    cursor.execute(sql)
    
    
    result=cursor.fetchone()
    
    print(f"result: {result[0]} {result[1]} ")

def updateProduct(id, name,price):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    sql="Update products Set name=%s, price=%s where id=%s "
    values=(name,price,id)
 
    cursor.execute(sql,values)
    try:    
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")
def deleteProduct(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="SQL1234",database="sys")
    cursor=connection.cursor()
    # sql="Delete from products where id=3 "
    # sql="Delete from products where name like '%S10%' "
    sql="Delete from products where id=%s "
    values=(id,)
    cursor.execute(sql,values)
    try:    
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı")
    
# deleteProduct(5)
getProducts()