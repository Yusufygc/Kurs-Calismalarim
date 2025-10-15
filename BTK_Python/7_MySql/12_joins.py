import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    #sql = "SELECT * FROM products inner join categories on Categories.id = Products.Categoryid"
    #sql = "SELECT products.name, products.price, categories.name FROM products inner join categories on categories.id = products.categoryid"
    #sql = "SELECT products.name, products.price, categories.name FROM products inner join categories on categories.id = products.categoryid where Categories.name = 'Telefon'"
    sql = "SELECT p.name, p.price, c.name FROM products as p inner join categories as c on c.id = p.categoryid where c.name = 'Telefon'"

    mycursor.execute(sql)

    try:
        results = mycursor.fetchall() #tüm kayıtları çek
        for product in results:
            print(product)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        connection.close()


getProducts()