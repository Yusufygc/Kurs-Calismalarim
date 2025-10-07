import mysql.connector

def getProductInfo():
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Ysfsql25",
      database="btkpython"
    )
    mycursor = connection.cursor()

    # SUM, AVG, MIN, MAX, COUNT -> aggregate functions
    sql = "SELECT COUNT(*) FROM products " # toplam kayıt sayısı satır sayısı
    sql1 = "SELECT SUM(price) FROM products " # fiyatların toplamı
    sql2 = "SELECT AVG(price) FROM products " # fiyatların ortalaması
    sql3 = "SELECT MIN(price) FROM products " # fiyatların minimumu
    sql4 = "SELECT MAX(price) FROM products " # fiyatların maksimumu
    sql5 = "SELECT Name, Price FROM Products WHERE Price =(SELECT MAX(price) FROM products) "
    mycursor.execute(sql) 
    result = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql1)
    result1 = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql2)
    result2 = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql3)
    result3 = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql4)
    result4 = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql5)
    result5 = mycursor.fetchall() # tüm kayıtları çek

    print(f' Total Products: {result[0]}')
    print(f' Total Price: {result1[0]}')
    print(f' Average Price: {result2[0]}')
    print(f' Minimum Price: {result3[0]}')
    print(f' Maximum Price: {result4[0]}')
    print(f' Most Expensive Product: {result5[0][0]} - {result5[0][1]}')
    connection.close()


getProductInfo()





