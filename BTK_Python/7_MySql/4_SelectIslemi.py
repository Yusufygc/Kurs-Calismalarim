import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "SELECT * FROM products"
    sql1 ="SELECT name, price FROM products"
    mycursor.execute(sql1)

    results = mycursor.fetchall() #tüm kayıtları çek
    #results = mycursor.fetchone() #tek kayıt çek
    for row in results:
        print(row)

    for product in results:
       # print(f' Name: {product[1]} Price: {product[2]}')
        print(f' Name: {product[0]} Price: {product[1]}')

    connection.close()


getProducts()







