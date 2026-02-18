# GenAI Prompts and Understanding

## Prompt 1: Project Scaffolding
**Prompt:** "Expert Django Developer. Generate a Student Management System with MySQL, MongoDB demo, Bootstrap 5, and 30 sample students."
**Understanding:** This prompt sets the high-level architecture and technology stack. It ensures the AI understands the complexity (dual-DB) and the specific styling requirements (Bootstrap).

## Prompt 2: Data Modeling
**Prompt:** "Create Django models for Student, Category, and Achievement with Foreign Key relationships and status choices."
**Understanding:** This focuses on the database schema. It ensures data integrity through relationships and defines the business logic for achievement tracking.

## Prompt 3: Data Seeding
**Prompt:** "Write a Django management command to seed 30 realistic students and 2 achievements per student using the Faker library."
**Understanding:** This is used to automate the populating of the database. Using `Faker` ensures the data looks professional and diverse, which is better for a demo than hardcoded "Student A, Student B".

## Prompt 4: CRUD Menu Programs
**Prompt:** "Create standalone Python scripts for MySQL and MongoDB CRUD operations with a menu-driven interface."
**Understanding:** This fulfills the requirement for external (non-Django) database interaction demos, proving the underlying database connectivity works independently of the web framework.
