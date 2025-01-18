import mysql.connector

# Establish connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()
def select_students_by_score_range():
   
    min_score = int(input("Enter the minimum score: "))
    max_score = int(input("Enter the maximum score: "))
    
    mycursor.execute("SELECT * FROM details WHERE score BETWEEN %s AND %s", (min_score, max_score))

    students = mycursor.fetchall()
    
    if students:
        print(f"\nStudents with score between {min_score} and {max_score}:")
        for std in students:
            print(std)
    else:
        print(f"\nNo students found with score between {min_score} and {max_score}.")

select_students_by_score_range()
