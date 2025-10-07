import mysql.connector

def updateProduct(productId, newName, price=None):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "UPDATE products SET name = %s, price = %s WHERE id = %s"
    val = (newName, price, productId)
    mycursor.execute(sql, val)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} kayıt güncellendi.')

    except mysql.connector.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()
        print("Connection closed.")

def menu():
    print("1- Ürün Güncelle")
    print("2- Çıkış")
    choice = input("Seçiminiz: ")

    if choice == '1':
        productId = int(input("Güncellenecek ürün ID'si: "))
        newName = input("Yeni ürün adı: ")
        price_input = input("Yeni ürün fiyatı (boş bırakılırsa güncellenmez): ")
        price = float(price_input) if price_input else None
        updateProduct(productId, newName, price)
        menu()  # Menüye geri dön
    elif choice == '2':
        print("Çıkış yapılıyor...")
    else:
        print("Geçersiz seçim, tekrar deneyin.")
        menu()  # Menüye geri dön

if __name__ == "__main__":
    menu()