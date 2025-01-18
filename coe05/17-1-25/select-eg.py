import mysql.connector

mydb=mysql.connector.connect(
host="localhost",
user="root",password="1234",database="mysql"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM details")
students = mycursor.fetchall()
for std in students:
    print(std)
