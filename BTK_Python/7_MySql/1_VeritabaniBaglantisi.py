import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ysfsql25",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Tablo oluşturma
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

"""
# Veritabanı oluşturma
mycursor.execute("CREATE DATABASE mydatabase") 
print("Database created...")

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

"""