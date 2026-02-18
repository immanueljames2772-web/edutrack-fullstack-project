import mysql.connector
from datetime import date

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mindflayer2004",
        database="student_db"
    )

def add_student():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    reg_no = input("Enter Register Number: ")
    course = input("Enter Course: ")
    batch = input("Enter Batch: ")
    dept = input("Enter Department: ")
    sql = "INSERT INTO students_student (name, email, register_number, course, batch, department, status, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"
    val = (name, email, reg_no, course, batch, dept, 'Active')
    try:
        cursor.execute(sql, val)
        conn.commit()
        print("Student added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students_student")
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def update_student():
    conn = connect_db()
    cursor = conn.cursor()
    reg_no = input("Enter Register Number of student to update: ")
    new_name = input("Enter new Name: ")
    sql = "UPDATE students_student SET name = %s WHERE register_number = %s"
    val = (new_name, reg_no)
    try:
        cursor.execute(sql, val)
        conn.commit()
        print("Student updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    conn.close()

def delete_student():
    conn = connect_db()
    cursor = conn.cursor()
    reg_no = input("Enter Register Number of student to delete: ")
    sql = "DELETE FROM students_student WHERE register_number = %s"
    val = (reg_no,)
    try:
        cursor.execute(sql, val)
        conn.commit()
        print("Student deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    conn.close()

def filter_by_dept():
    conn = connect_db()
    cursor = conn.cursor()
    dept = input("Enter Department: ")
    sql = "SELECT * FROM students_student WHERE department = %s"
    val = (dept,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def count_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students_student")
    result = cursor.fetchone()
    print(f"Total Students: {result[0]}")
    conn.close()

def main():
    while True:
        print("
MySQL CRUD Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Filter by Department")
        print("6. Count Students")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': update_student()
        elif choice == '4': delete_student()
        elif choice == '5': filter_by_dept()
        elif choice == '6': count_students()
        elif choice == '7': break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
