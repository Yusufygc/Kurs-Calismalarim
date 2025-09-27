import mysql.connector

#******************************************************************
# TEK SEFERDE TEK KAYIT EKLEME
#******************************************************************
def insertProduction(name, price,imageUrl,description):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "INSERT INTO products (name, price,imageUrl,description) VALUES (%s, %s, %s, %s)"
    val = (name, price, imageUrl, description)
    mycursor.execute(sql, val)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} kayıt ekledi.')
        print(f'son eklenen ürün id: {mycursor.lastrowid}')

    except mysql.connector.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()
        print("Connection closed.")
#******************************************************************
# TEK SEFERDE ÇOKLU KAYIT EKLEME
#******************************************************************
def insertProductions(list):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="btkpython"
    )

    mycursor = connection.cursor()

    sql = "INSERT INTO products (name, price,imageUrl,description) VALUES (%s, %s, %s, %s)"
    val = list
    mycursor.executemany(sql, val) #çoklu kayıt ekleme

    try:
        connection.commit()
        print(f'{mycursor.rowcount} kayıt ekledi.')
        print(f'son eklenen ürün id: {mycursor.lastrowid}')

    except mysql.connector.Error as e:
        print("Error occurred:", e)
    finally:
        connection.close()
        print("Connection closed.")

#******************************************************************
# MENÜ VE KULLANICI GİRİŞİ
#******************************************************************
list = [] # her seferinde veritabanı ile bağlantı kurulmasın tek seferde çoklu veri eklemek için liste oluşturuldu
print("Ürün ekleme menüsüne hoşgeldiniz...")

while True:
    name = input("Ürün Adı: ")
    price = float(input("Ürün Fiyatı: "))
    imageUrl = input("Ürün Resim URL'si: ")
    description = input("Ürün Açıklaması: ")

    list.append((name, price, imageUrl, description))

    result = input("Devam etmek istiyor musunuz? (e/h): ")
    if result.lower() == 'h':
        print("Ürün ekleme işlemi sonlandırıldı.")
        print(list)
        insertProductions(list)  # Çoklu kayıt ekleme fonksiyonunu çağır
        break

#insertProduction(name, price, imageUrl, description)