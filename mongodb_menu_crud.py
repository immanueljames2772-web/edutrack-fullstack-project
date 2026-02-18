import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sms_nosql"]
students_col = db["students"]
achievements_col = db["achievements"]

def add_student():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    reg_no = input("Enter Register Number: ")
    course = input("Enter Course: ")
    batch = input("Enter Batch: ")
    dept = input("Enter Department: ")
    student = {
        "name": name,
        "email": email,
        "register_number": reg_no,
        "course": course,
        "batch": batch,
        "department": dept,
        "status": "Active",
        "created_at": datetime.now(),
        "achievements": [] # Embedded achievements demo
    }
    try:
        students_col.insert_one(student)
        print("Student added successfully.")
    except Exception as e:
        print(f"Error: {e}")

def view_students():
    for student in students_col.find():
        print(student)

def update_student():
    reg_no = input("Enter Register Number to update: ")
    new_name = input("Enter new Name: ")
    query = {"register_number": reg_no}
    new_values = {"$set": {"name": new_name}}
    students_col.update_one(query, new_values)
    print("Student updated.")

def delete_student():
    reg_no = input("Enter Register Number to delete: ")
    query = {"register_number": reg_no}
    students_col.delete_one(query)
    print("Student deleted.")

def filter_by_dept():
    dept = input("Enter Department: ")
    query = {"department": dept}
    for student in students_col.find(query):
        print(student)

def agg_count_dept():
    pipeline = [
        {"$group": {"_id": "$department", "count": {"$sum": 1}}}
    ]
    results = students_col.aggregate(pipeline)
    print("Student Count by Department:")
    for result in results:
        print(f"{result['_id']}: {result['count']}")

def main():
    while True:
        print("
MongoDB CRUD Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Filter by Department")
        print("6. Aggregation Count per Department")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': update_student()
        elif choice == '4': delete_student()
        elif choice == '5': filter_by_dept()
        elif choice == '6': agg_count_dept()
        elif choice == '7': break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
