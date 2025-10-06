import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "SELECT * FROM products WHERE id=1"  
    sql = "SELECT * FROM products WHERE name='iphone 14+'" 
    # sql = "SELECT * FROM products WHERE name='iphone 14+' AND price=30000"   
    # sql = "SELECT * FROM products WHERE name='iphone 14+' OR price=30000"   
    # sql = "SELECT * FROM products WHERE price BETWEEN 20000 AND 40000"   
    # sql = "SELECT * FROM products WHERE name LIKE '%iphone%'" # içinde iphone geçen
    # sql = "SELECT * FROM products WHERE name LIKE 'iphone%'" # iphone ile başlayan
    # sql = "SELECT * FROM products WHERE name LIKE '%pro'" # pro ile biten
    sql = "SELECT * FROM products ORDER BY name" # sıralı isim
    # sql = "SELECT * FROM products ORDER BY name DESC" # ters sıralı isim
    sql = "SELECT * FROM products ORDER BY name, price" # önce isme göre sonra fiyata göre sıralar

    mycursor.execute(sql)

    """ fetchall() tüm kayıtları çeker ve liste olarak döner
    fetchone() tek kayıt çeker ve tek bir tuple döner """
    results = mycursor.fetchall() #tüm kayıtları çek
 
    for product in results:
        print(f' Name: {product[1]} Price: {product[2]}')
       

    connection.close()

def getProductById(product_id):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "SELECT * FROM products WHERE id=%s"
    mycursor.execute(sql, (product_id,)) # tek elemanlı tuple için sonuna virgül koyduk

    result = mycursor.fetchone() # tek kayıt çek
    if result:
        print(f' Name: {result[1]} Price: {result[2]}') 
    else:
        print("Product not found.")

    connection.close()

getProducts()
getProductById(5)





