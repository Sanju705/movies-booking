 Ticket Booking System
A full-stack Django web application for managing movie ticket bookings with admin panel and user-friendly interface.

✨ Project Overview
This project is a Movie Ticket Booking Management System built with Django. Users can book tickets by selecting movies, dates, and showtimes. Admins can manage all bookings through a powerful Django admin interface with filtering, searching, and inline editing capabilities.

Perfect for learning Django ORM, Forms, Admin customization, and database management.

🚀 Features Implemented

✅ User Features:

Book movie tickets with movie name, date, and showtime

Clean, responsive booking form

Model-based data validation
 Admin Features:

Complete ticket management dashboard

Inline editing of bookings

Advanced filtering by date/movie

Search by movie name

Read-only ticket IDs for audit trail

Custom field organization

✅ Technical Features:

Django ModelForms for validation

Auto-generated primary keys

Date/Time field support

Admin customization (list_display, filters, etc.)

🛠️ Tech Stack
🔹 Backend: Django 5.2+
🔹 Database: SQLite (default) / PostgreSQL/MySQL
🔹 Language: Python 3.9+
🔹 Admin: Django Admin (fully customized)
🔹 Forms: Django ModelForms

📋 Setup Instructions
Prerequisites
Python 3.9+ installed

Git (optional)

Step 1: Clone & Navigate
git clone <your-repo-url>
cd moviesbooking
cd moviesbooking  # or your project name

Step 2: Create Virtual Environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

Step 3: Install Dependencies
pip install django
# or
pip install -r requirements.txt  # if available

Step 4: Database Setup
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

Step 5: Create Superuser (Admin)
python manage.py createsuperuser

Username: admin
Email: admin@example.com
Password: yourpassword123

Step 6: Run Development Server
python manage.py runserver

Step 7: Access Your App
🌐 Frontend: http://127.0.0.1:8000/
🛠️  Admin:   http://127.0.0.1:8000/admin/

⚙️ Useful Commands
| Command                          | Purpose                  |
| -------------------------------- | ------------------------ |
| python manage.py runserver       | Start development server |
| python manage.py migrate         | Apply database changes   |
| python manage.py makemigrations  | Create migration files   |
| python manage.py createsuperuser | Create admin user        |
| python manage.py shell           | Open Django shell        |
| python manage.py check           | Check for issues         |

🎨 Screenshots
Admin Dashboard
[Admin panel with ticket list, filters, search]
- Movie Name | Date | Showtime | Ticket ID
- Inline editing enabled
- Date filters & search working

Booking Form
[Clean form with dropdowns/fields for:]
- Movie Name (text)
- Date (calendar picker)
- Showtime (time picker)

🔧 Troubleshooting
❌ Error: admin.E124

bash
# Fix: Add list_display_links in admin.py
list_display_links = ['movie_name']
❌ No data in admin

bash
python manage.py migrate
python manage.py createsuperuser
❌ Server won't start

bash
pip install django
python manage.py check

🚀 Next Steps / Enhancements
 Add user authentication

 Theatre & seat selection

 Payment integration

 Email notifications

 Frontend with HTML templates

 Deploy to Heroku/PythonAnywhere

 👨‍💻 Author
 Kamani Sanjay Kumar
 Full-Stack Developer
