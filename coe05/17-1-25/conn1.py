import mysql.connector

# Establish connection to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="test"
)

mycursor = mydb.cursor()

# Fetch and display all records from the stu1 table
mycursor.execute("SELECT * FROM stu1")

# Fetch all results
students = mycursor.fetchall()

# Print each record
for std in students:
    print(std)
