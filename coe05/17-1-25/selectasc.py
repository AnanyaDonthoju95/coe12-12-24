import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mysql"
)

mycursor = mydb.cursor()

def select_and_sort_students():
    print("Choose a column to sort by:")
    print("1. sid")
    print("2. sname")
    print("3. age")
    print("4. score")
    print("5. city")
    
    column_choice = int(input("Enter your choice (1-5): "))
    
    columns = {1: 'sid', 2: 'sname', 3: 'age', 4: 'score', 5: 'city'}
    
    if column_choice not in columns:
        print("Invalid choice. Exiting.")
        return
    order = "ASC"

    column_name = columns[column_choice]
    query = f"SELECT * FROM details ORDER BY {column_name} {order}"

    mycursor.execute(query)
    students = mycursor.fetchall()
    
    print(f"\nStudents sorted by {column_name} in {order} order:")
    for std in students:
        print(std)
select_and_sort_students()
