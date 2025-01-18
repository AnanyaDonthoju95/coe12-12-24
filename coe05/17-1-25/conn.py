import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="test"
)
mycursor = mydb.cursor()

sname=input("Enter your name:")
id = input("Enter your id:")
mycursor.execute("insert into stu1 values(%s,%s)",(id,sname))
mydb.commit()