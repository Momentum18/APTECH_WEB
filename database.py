import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="aptech"
)
"""
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print()
"""

"""
mycursor.execute(
    "CREATE TABLE staff (full_name VARCHAR(20), email VARCHAR(50), phone_number BIGINT(20))"
)
"""
'''
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print()
'''

"""
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
"""

mycursor = mydb.cursor()

sql = "INSERT INTO STAFF (full_name, email, phone_number) VALUES (%s, %s, %s)"
val = ("Olanrewaju Adeshewa", "adeshewa@gmail.com", "08145237890")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
