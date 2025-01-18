import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",password="1234",database="mysql"
)
mycursor=mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS student")
mycursor.execute("CREATE TABLE student(sid INT, sname VARCHAR(10), age INT)")
mycursor.execute("INSERT INTO student VALUES(1, 'ananya', 20)")
mycursor.execute("INSERT INTO student VALUES(2, 'akshara', 13)")
mycursor.execute("update student set sname='rama' where sid=2")
mycursor.execute("delete from student where sid=2")
mydb.commit()