import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()

def update_student():
    sid = int(input("Enter the student ID (sid) to update: "))
    sname = input("Enter the new student name (sname): ")
    age = int(input("Enter the new student age (age): "))
    
    mycursor.execute("UPDATE details SET sname = %s, age = %s WHERE sid = %s", (sname, age, sid))

    mydb.commit()

    print(f"Student with ID {sid} has been updated successfully.")
update_student()
mycursor.execute("SELECT * FROM details")
students = mycursor.fetchall()

print("\nUpdated Students in the details table:")
for student in students:
    print(student)
