import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Category, Student, Achievement
from faker import Faker
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with initial data using Kerala names'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created'))

        # Create Categories
        categories = ['Sports', 'Technical', 'Cultural', 'Research', 'Internship']
        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name, defaults={'description': f'{cat_name} activities'})
        self.stdout.write(self.style.SUCCESS('Categories created'))

        # Kerala Names List
        kerala_names = [
            "Rahul Nair", "Anjali Menon", "Vishnu Pillai", "Meera Krishnan", "Gokul Das",
            "Sneha Varma", "Akhil Joseph", "Riya Thomas", "Jithin Kurian", "Arya Rajesh",
            "Midhun Madhavan", "Kavya Sreekumar", "Arjun Panicker", "Parvathy Warrier", "Siddharth Namboothiri",
            "Deepa George", "Naveen Jacob", "Lakshmi Priya", "Bibin Babu", "Reshma Ramesh",
            "Adarsh Vijay", "Shilpa Santhosh", "Abhijith Ravi", "Divya Mohan", "Kiran Kumar",
            "Athira Sasi", "Sarath Chandran", "Neethu Pradeep", "Manu Prasad", "Greeshma Gopinath"
        ]

        # Clear existing data to avoid mixing
        Achievement.objects.all().delete()
        Student.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing student records cleared for fresh Kerala names.'))

        # Create Students
        departments = ['Computer Science', 'Data Science', 'Statistics', 'Mathematics', 'Physics']
        batches = ['2023-2025', '2024-2026']
        courses = ['M.Sc Data Science', 'M.Sc Statistics', 'M.Sc Computer Science']

        students = []
        for i, name in enumerate(kerala_names):
            reg_no = f'23MDS{i+1:03d}'
            student = Student.objects.create(
                name=name,
                email=f"{name.lower().replace(' ', '.')}@example.com",
                register_number=reg_no,
                course=random.choice(courses),
                batch=random.choice(batches),
                department=random.choice(departments),
                status=random.choice(['Active', 'Inactive']),
            )
            students.append(student)
        self.stdout.write(self.style.SUCCESS(f'{len(students)} Students with Kerala names created'))

        # Create Achievements
        cats = Category.objects.all()
        for student in Student.objects.all():
            for _ in range(2):
                Achievement.objects.create(
                    student=student,
                    title=fake.sentence(nb_words=4),
                    description=fake.text(),
                    category=random.choice(cats),
                    date=fake.date_between(start_date='-1y', end_date='today'),
                    status=random.choice(['Pending', 'Approved', 'Rejected']),
                )
        self.stdout.write(self.style.SUCCESS('Achievements recreated'))
