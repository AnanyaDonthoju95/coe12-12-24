import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()

def select_students_by_city():
    city = input("Enter the city to filter students by: ")
    
    mycursor.execute("SELECT * FROM details WHERE city = %s", (city,))
    
    students = mycursor.fetchall()
    
    if students:
        print(f"\nStudents from city '{city}':")
        for std in students:
            print(std)
    else:
        print(f"\nNo students found from city '{city}'.")

select_students_by_city()
