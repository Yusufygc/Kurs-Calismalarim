import mysql.connector

def deleteProduct(productId):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "DELETE FROM products WHERE id = %s"
    val = (productId,)
    mycursor.execute(sql, val)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} kayıt silindi.')

    except mysql.connector.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()
        print("Connection closed.")

deleteProduct(3)  # Örnek olarak ID'si 3 olan ürünü sil