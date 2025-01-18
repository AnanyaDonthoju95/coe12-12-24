import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()

def delete_student():
    sid = int(input("Enter the student ID (sid) to delete: "))

    mycursor.execute("DELETE FROM details WHERE sid = %s", (sid,))

    mydb.commit()

    print(f"Student with ID {sid} has been deleted successfully.")
delete_student()
mycursor.execute("SELECT * FROM details")
students = mycursor.fetchall()

print("\nRemaining Students in the details table:")
for student in students:
    print(student)
