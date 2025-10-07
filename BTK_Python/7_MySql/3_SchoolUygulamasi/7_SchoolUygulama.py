from connection import connection

def gorselCizgi():
    print("\n***************************************\n")
    


def getStudentInfo():
 
    mycursor = connection.cursor()

    # SUM, AVG, MIN, MAX, COUNT -> aggregate functions
    sql = "SELECT COUNT(*) FROM student " # toplam kayıt sayısı satır sayısı
    sql1 = "SELECT Name, Surname ,StudentNumber FROM student "
    sql2 ="Select Name, Surname from student where gender='K' "
    sql3 = "SELECT * FROM student WHERE YEAR(Birthdate) = 2003;"
    sql4 = "SELECT * FROM student WHERE YEAR(Birthdate) = 2005 and Name='Ali';  "
    sql5 = "SELECT * FROM student WHERE Name LIKE '%me%' or surname LIKE '%me%' ;"
    sql6 = "SELECT COUNT(*) FROM student WHERE gender='E' "
    sql7 = "SELECT * FROM student WHERE gender = 'k' ORDER BY name;"
    """ORDER BY ifadesi WHERE'den sonra gelir, önce değil.
        Ayrıca COUNT(*) ile sıralama (ORDER BY) genellikle anlamsız olur 
        çünkü COUNT(*) tek bir sonuç döndürür."""
    
    mycursor.execute(sql) 
    result = mycursor.fetchone() # tek kayıt çek

    mycursor.execute(sql1) 
    result1 = mycursor.fetchall()
    
    mycursor.execute(sql2) 
    result2 = mycursor.fetchall()

    mycursor.execute(sql3) 
    result3 = mycursor.fetchall()

    mycursor.execute(sql4) 
    result4 = mycursor.fetchall()

    mycursor.execute(sql5) 
    result5 = mycursor.fetchall()

    mycursor.execute(sql6) 
    result6 = mycursor.fetchone()

    mycursor.execute(sql7) 
    result7 = mycursor.fetchall()

    print(f' Total Students: {result[0]}')
    gorselCizgi()

    for student in result1:
        print(f' Student Info: {student[0]} - {student[1]} - {student[2]}')
    gorselCizgi()

    print(f' Female Students: {len(result2)}')
    for student in result2:
        print(f' Female Student Info: {student[0]} - {student[1]}')
    gorselCizgi()

    print(f' Students Born in 2003: {len(result3)}')
    for student in result3:
        print(f' Student Info: {student[0]} - {student[1]} - {student[2]}')
    gorselCizgi()

    print(f' Students Born in 2005 named Ali: {len(result4)}')
    for student in result4:
        print(f' Student Info: {student[0]} - {student[1]} - {student[2]}')
    gorselCizgi()

    print(f' Students whose Name contains "me": {len(result5)}')
    for student in result5:
        print(f' Student Info: {student[0]} - {student[1]} - {student[2]}')
    gorselCizgi()

    print(f' Male Students: {result6[0]}')
    gorselCizgi()

    print(f' Female Students: {len(result7)}')
    for student in result7:
        print(f' Student Info: {student[1]} - {student[2]} - {student[3]}')

    connection.close()

getStudentInfo()