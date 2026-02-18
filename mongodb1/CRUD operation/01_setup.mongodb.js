use ("collegeDB")


//db.students.drop()

db.createCollection("students")

db.students.insertMany([
{ name: "Anshika", age: 21, department: "Computer Science", semester: 4, marks: 85, city: "Chennai" },
{ name: "Rahul", age: 22, department: "Electronics", semester: 6, marks: 78, city: "Bangalore" },
{ name: "Meera", age: 20, department: "Mathematics", semester: 2, marks: 92, city: "Hyderabad" },
{ name: "Kiran", age: 23, department: "Physics", semester: 8, marks: 74, city: "Mumbai" },
{ name: "Arjun", age: 21, department: "Computer Science", semester: 4, marks: 88, city: "Chennai" },
{ name: "Divya", age: 22, department: "Electronics", semester: 6, marks: 95, city: "Delhi" },
{ name: "Sneha", age: 19, department: "Mathematics", semester: 2, marks: 67, city: "Bangalore" },
{ name: "Vikram", age: 24, department: "Physics", semester: 8, marks: 81, city: "Hyderabad" },
{ name: "Pooja", age: 21, department: "Computer Science", semester: 4, marks: 73, city: "Mumbai" },
{ name: "Rohit", age: 22, department: "Electronics", semester: 6, marks: 84, city: "Chennai" },
{ name: "Neha", age: 20, department: "Mathematics", semester: 2, marks: 90, city: "Delhi" },
{ name: "Manoj", age: 23, department: "Physics", semester: 8, marks: 76, city: "Bangalore" }
])

