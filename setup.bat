@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Seeding data (including superuser 'admin')...
python manage.py seed_data

echo Setup complete. Run 'python manage.py runserver' to start the server.
pause
