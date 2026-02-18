# Project Report: EduTrack (Student Management System)

## 1. Project Overview
This project is a Full-Stack Student Management System (EduTrack) built using Django 6.0. It utilizes MySQL as the primary relational database and includes a MongoDB integration for NoSQL demonstrations. The system allows for comprehensive management of student records and their academic/extra-curricular achievements.

## 2. Technologies Used
- **Backend Framework:** Django (Python)
- **Primary Database:** MySQL (via `mysqlclient`)
- **NoSQL Database:** MongoDB (via `pymongo`)
- **Frontend:** HTML5, Bootstrap 5 (CSS/JS)
- **Data Generation:** Faker library
- **Scripting:** Python (Menu-driven CRUD scripts)

## 3. Implementation Steps
1.  **Project Initialization:** Created the Django project `venv` and the application `students`.
2.  **Database Configuration:** Set up the MySQL connection in `settings.py` and defined the schema in `models.py`.
3.  **Model Design:** Implemented three core models:
    - `Student`: Stores personal and academic details.
    - `Category`: Defines achievement types (Sports, Technical, etc.).
    - `Achievement`: Links students to specific accomplishments with proof (image) support.
4.  **Backend Logic:** Developed Class-Based Views (CBVs) for List, Detail, Create, Update, and Delete (CRUD) operations.
5.  **Authentication:** Integrated Django's built-in auth system to restrict modification access to logged-in users.
6.  **UI/UX:** Designed a responsive dashboard and forms using Bootstrap 5.
7.  **Data Seeding:** Created a custom management command (`seed_data`) to automate the population of 30 realistic student records.
8.  **NoSQL Integration:** Developed a parallel CRUD script for MongoDB to demonstrate non-relational data handling.
9.  **Automation:** Created a `setup.bat` file for one-click environment preparation.

## 4. Functionalities
- **Dashboard:** Real-time statistics of students and achievements.
- **Search & Pagination:** Advanced filtering on the student list page.
- **Achievement Management:** Tracking achievements with status (Approved/Pending/Rejected).
- **Public/Private Access:** Public users can view data; only authenticated users can modify it.
