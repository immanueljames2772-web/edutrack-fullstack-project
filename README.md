# EduTrack: Student Management System

EduTrack is a full-stack web application built with Django for managing student records, achievements, and academic data. It features a modern dashboard, authentication system, and administrative interface.

## Features

- **Student Management:** Create, Read, Update, and Delete student profiles.
- **Achievement Tracking:** Record and manage student achievements and proofs.
- **Modern UI:** Styled with a custom dashboard and templates.
- **Admin Dashboard:** Powered by `django-jazzmin` for an enhanced administrative experience.
- **Database Support:** Primary data storage using MySQL, with additional integration for MongoDB operations.
- **Authentication:** Secure login and session management.

## Tech Stack

- **Backend:** Django 6.0.2
- **Frontend:** HTML5, CSS (Vanilla), Django Templates
- **Primary Database:** MySQL
- **Secondary Database:** MongoDB (via pymongo)
- **UI Enhancements:** Django-Jazzmin, FontAwesome
- **Development Tools:** Faker (for seeding data), Matplotlib/Pandas (for analysis)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/immanueljames2772-web/edutrack-fullstack-project.git
   cd edutrack-fullstack-project
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration:**
   - Ensure MySQL is running on `localhost:3306`.
   - Create a database named `student_db`.
   - Update `config/settings.py` with your MySQL credentials if they differ.

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Seed Data (Optional):**
   ```bash
   python manage.py seed_data
   ```

7. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
   The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

- `config/`: Project configuration (settings, URLs).
- `students/`: Main application logic (models, views, forms).
- `static/`: CSS and JavaScript files.
- `media/`: Uploaded files (e.g., proof of achievements).
- `mongodb1/`: MongoDB related CRUD operations and scripts.

## License

[MIT License](LICENSE) (or specify your license)
