import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS details (
    sid INT PRIMARY KEY, 
    sname VARCHAR(10), 
    age INT, 
    score INT, 
    city VARCHAR(10)
)
""")
def insert_student():
    sid = int(input("Enter student ID (sid): "))
    sname = input("Enter student name (sname): ")
    age = int(input("Enter student age (age): "))
    score = int(input("Enter student score (score): "))
    city = input("Enter student city (city): ")
    mycursor.execute("INSERT INTO details (sid, sname, age, score, city) VALUES (%s, %s, %s, %s, %s)", 
                     (sid, sname, age, score, city))
    mydb.commit()

    print(f"Student {sname} with ID {sid} has been inserted successfully.")
num_records = int(input("How many student records do you want to insert? "))

for _ in range(num_records):
    insert_student()
mycursor.execute("SELECT * FROM details")
students = mycursor.fetchall()

print("\nAll Students in the details table:")
for student in students:
    print(student)
