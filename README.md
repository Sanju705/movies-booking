# 🎬 CineTime - Movie Ticket Booking System

**A full-stack Django web application for managing movie ticket bookings with AI chatbot, automated email confirmations, QR codes, and Razorpay payment integration.**

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Email Configuration](#-email-configuration)
- [AI Chatbot Integration](#-ai-chatbot-integration)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

**CineTime** is a production-ready movie ticket booking system that combines modern web technologies with AI capabilities. Users can browse movies, book tickets, receive QR code confirmations via email, make payments via Razorpay, and interact with an AI chatbot for movie recommendations.

### Key Highlights:
✅ **User Authentication** - Custom user model with email & phone verification  
✅ **Movie Booking** - Select movie, date, showtime, and quantity  
✅ **Payment Integration** - Razorpay payment gateway for secure transactions  
✅ **Email Notifications** - Professional ticket confirmations with embedded QR codes  
✅ **AI Chatbot** - Google Gemini 2.0 Flash powered chatbot for movie recommendations  
✅ **Responsive UI** - Modern dark theme with gradient styling  
✅ **Admin Dashboard** - Comprehensive admin panel for managing bookings & users  

---

## ✨ Features Implemented

### 🎫 Booking Features
- ✅ Browse available movies
- ✅ Select preferred date and showtime
- ✅ Choose number of tickets
- ✅ Auto-calculated pricing
- ✅ Real-time seat availability check
- ✅ Instant booking confirmation

### 👤 User Features
- ✅ User registration with email & phone
- ✅ Login/Logout authentication
- ✅ User profile management
- ✅ Booking history view
- ✅ Ticket QR code download
- ✅ Email confirmation receipt

### 💳 Payment Features
- ✅ Razorpay payment gateway integration
- ✅ Secure payment processing
- ✅ Payment status tracking
- ✅ Order confirmation emails
- ✅ Multiple payment method support

### 📧 Email System
- ✅ Automated ticket confirmation emails
- ✅ Beautiful HTML email templates
- ✅ Embedded QR codes in emails
- ✅ Ticket details with pricing breakdown
- ✅ Professional branding

### 🤖 AI Features
- ✅ Google Gemini AI chatbot
- ✅ Movie recommendations
- ✅ Natural language processing
- ✅ Session-based conversation history
- ✅ Error handling with helpful messages

### 👨‍💼 Admin Features
- ✅ Complete ticket management
- ✅ User management
- ✅ Payment tracking
- ✅ Advanced filtering & search
- ✅ Inline editing capabilities
- ✅ Custom admin dashboard

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 5.2.4
- **Language**: Python 3.9+
- **Database**: SQLite3 (Development) / PostgreSQL (Production)
- **ORM**: Django ORM

### Frontend
- **HTML5/CSS3**: Responsive design
- **JavaScript**: Vanilla JS for interactions
- **Dark Theme**: Custom gradient-based styling
- **Responsive**: Mobile & desktop optimized

### External Services
- **Payment**: Razorpay API
- **Email**: Gmail SMTP (configured)
- **AI**: Google Generative AI (Gemini 2.0 Flash)
- **QR Codes**: Python qrcode library

### Libraries & Dependencies
```
Django==5.2.4
django-rest-framework==3.14.0
razorpay==1.4.1
google-generativeai>=0.3.0
qrcode==7.4.2
pillow==10.1.0
python-dotenv==1.0.0
```

---

## 📁 Project Structure

```
moviesbooking/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # This file
│
├── moviesbooking/           # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
│
├── app/                     # Main application
│   ├── models.py            # Database models
│   │   ├── ticket           # Ticket model
│   │   ├── CinemaUser       # Custom user model
│   │   └── Payment          # Payment model
│   │
│   ├── views.py             # View functions
│   │   ├── index()          # Booking page
│   │   ├── booked_ticket()  # Confirmation page
│   │   ├── register()       # User registration
│   │   ├── login()          # User login
│   │   └── chatbot()        # AI chatbot
│   │
│   ├── forms.py             # Django forms
│   │   ├── ticketbooking    # Booking form
│   │   └── RegisterForm     # Registration form
│   │
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin customization
│   ├── apps.py              # App configuration
│   ├── tests.py             # Unit tests
│   │
│   ├── email_service.py     # Email functionality
│   │   ├── generate_qr_code()
│   │   └── send_ticket_email()
│   │
│   ├── gemini_service.py    # AI chatbot service
│   │   └── GeminiChatbot    # Chatbot class
│   │
│   ├── api_views.py         # REST API endpoints
│   │   ├── chat_api()       # Chat endpoint
│   │   └── clear_chat()     # Clear history endpoint
│   │
│   ├── migrations/          # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_payment.py
│   │   ├── 0003_ticket_price.py
│   │   └── __pycache__/
│   │
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── index.html       # Booking page
│   │   ├── login.html       # Login page
│   │   ├── register.html    # Registration page
│   │   ├── booked_ticket.html # Confirmation
│   │   ├── payment.html     # Payment page
│   │   ├── upcoming.html    # Upcoming movies
│   │   ├── events.html      # Events page
│   │   └── chatbot.html     # AI chatbot interface
│   │
│   └── __pycache__/
│
├── static/                  # Static files
│   ├── CSS/                 # Stylesheets
│   └── chatbot.js           # Chatbot JavaScript
│
├── templates/               # Base templates
│   └── base.html            # Main template
│
└── requirements.txt         # Python dependencies
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git (optional)
- Gmail account (for email functionality)
- Google Gemini API key (for chatbot)

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd moviesbooking
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser

# When prompted:
Username: admin
Email: admin@example.com
Password: (your secure password)
```

### Step 6: Configure Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password_here
RAZORPAY_KEY_ID=your_razorpay_key
RAZORPAY_KEY_SECRET=your_razorpay_secret
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

### Step 8: Access Application
- **Frontend**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Chatbot**: http://127.0.0.1:8000/chatbot/

---

## ⚙️ Configuration

### Email Configuration (Gmail SMTP)

1. **Enable 2-Step Verification** on your Gmail account
2. **Generate App Password**:
   - Visit: https://myaccount.google.com/apppasswords
   - Select: Mail + Windows Computer
   - Copy the 16-character password

3. **Update settings.py**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'app-password-16-chars'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### Razorpay Configuration

1. **Sign up** at https://razorpay.com
2. **Get API Keys** from dashboard
3. **Update settings.py**:
```python
RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'
```

### Gemini AI Configuration

1. **Get API Key** from https://ai.google.dev
2. **Update settings.py**:
```python
GEMINI_API_KEY = 'your_gemini_api_key'
```

---

## 📖 Usage Guide

### For Users

#### Registration
1. Click "Register" on home page
2. Enter username, email, phone, DOB
3. Set secure password
4. Click "Create Account"
5. Verify email confirmation

#### Book Tickets
1. Login to your account
2. Go to booking page
3. Select movie from dropdown
4. Choose date using calendar picker
5. Select showtime
6. Choose number of tickets
7. Click "Book Now"
8. Proceed to payment (Razorpay)
9. Receive confirmation email with QR code

#### View Bookings
1. Login to account
2. Go to "My Bookings"
3. View all tickets
4. Download QR code
5. Print or show at cinema

#### Chat with AI
1. Go to "Chat" or "/chatbot/"
2. Ask about movie recommendations
3. Get personalized suggestions
4. View conversation history
5. Clear history to start fresh

### For Admins

#### Access Admin Panel
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Manage:
   - Users
   - Tickets
   - Payments
   - Apply filters & search

#### Manage Bookings
- View all tickets
- Filter by date, movie, user
- Search by movie name
- Inline edit booking details
- Delete bookings if needed

---

## 🔌 API Endpoints

### Chat API
```
Endpoint: POST /api/chat/
Purpose: Send message to AI chatbot
Body: {
    "message": "Your question here"
}
Response: {
    "response": "AI response",
    "status": "success"
}
```

### Clear Chat History
```
Endpoint: POST /api/clear-chat/
Purpose: Clear conversation history
Response: {
    "status": "success",
    "message": "Chat history cleared"
}
```

---

## 🗄️ Database Schema

### CinemaUser Model
```python
class CinemaUser(AbstractUser):
    phone = CharField(max_length=15, unique=True)
    dob = DateField(null=True, blank=True)
```

### Ticket Model
```python
class ticket(Model):
    movie_name = CharField(max_length=100)
    date = DateField()
    showtime = TimeField()
    ticket = PositiveIntegerField()
    email = EmailField()
    price = IntegerField(default=250)
```

### Payment Model
```python
class Payment(Model):
    user = ForeignKey(CinemaUser, on_delete=CASCADE)
    amount = IntegerField()
    razorpay_order_id = CharField(max_length=200)
    razorpay_payment_id = CharField(max_length=200, blank=True)
    razorpay_signature = CharField(max_length=200, blank=True)
    status = CharField(max_length=20, default="PENDING")
    created_at = DateTimeField(auto_now_add=True)
```

---

## 📧 Email Configuration Details

### Email Features
- ✅ Automatic sending on ticket booking
- ✅ Beautiful HTML formatting
- ✅ Embedded QR code image
- ✅ Ticket details with pricing
- ✅ Mobile-responsive layout
- ✅ Plain text fallback

### Email Contents
- Movie name & details
- Booking date & time
- Ticket quantity & price
- Total amount
- Ticket ID
- Scannable QR code
- Contact information

### Troubleshooting Emails

**Issue**: Emails not sending
- Check Gmail app password is correct
- Verify 2-Step Verification is enabled
- Check EMAIL_BACKEND in settings
- View terminal output for SMTP errors

**Issue**: Emails in spam folder
- Add sender to contacts
- Mark as "Not Spam"
- Check email authentication (SPF/DKIM)

---

## 🤖 AI Chatbot Integration

### Features
- **Model**: Google Gemini 2.0 Flash
- **Purpose**: Movie recommendations & booking assistance
- **Session**: Maintains conversation history
- **Smart Responses**: Context-aware recommendations

### How It Works
1. User sends message via chat interface
2. Message sent to `/api/chat/` endpoint
3. Gemini AI processes with system prompt
4. Response streamed back to frontend
5. Conversation stored in session

### System Prompt
The chatbot is configured to help with:
- Movie recommendations based on preferences
- Showtimes and availability
- Booking assistance
- Movie information and reviews

### Error Handling
- **429 Error**: API quota exceeded (free tier limit)
- **401 Error**: Invalid API key
- **404 Error**: Model not found (outdated model name)

Solution: Use `gemini-2.0-flash` model (latest & most reliable)

---

## 🔧 Useful Commands

```bash
# Run development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Check project for issues
python manage.py check

# Collect static files (production)
python manage.py collectstatic

# Create superuser via shell
python manage.py shell
>>> from app.models import CinemaUser
>>> user = CinemaUser.objects.create_superuser('admin', 'admin@gmail.com', 'password')
```

---

## 🐛 Troubleshooting

### ❌ Error: User has no email in profile
**Solution**: Update user profile with email address
```bash
python manage.py shell
>>> from app.models import CinemaUser
>>> user = CinemaUser.objects.get(username='admin')
>>> user.email = 'your-email@gmail.com'
>>> user.save()
```

### ❌ Error: Email not sending
**Check**:
1. Gmail app password is correct
2. 2-Step Verification enabled
3. Less secure apps access disabled
4. SMTP settings in settings.py
5. Terminal output for SMTP errors

**Test**:
```bash
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Test message', 'from@gmail.com', ['to@gmail.com'])
```

### ❌ Error: Razorpay payment failing
**Check**:
1. API keys correct in settings.py
2. Test mode enabled in Razorpay dashboard
3. Internet connection working
4. Payment amount in paise (multiply by 100)

### ❌ Error: Database migrations failing
**Solution**:
```bash
# Delete existing db.sqlite3 and migrations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### ❌ Error: Static files not loading
**Solution**:
```bash
python manage.py collectstatic --noinput
# Update STATIC_URL in settings.py if needed
```

### ❌ Error: Port 8000 already in use
**Solution**:
```bash
# Use different port
python manage.py runserver 8001

# Or kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 🚀 Future Enhancements

### Phase 2 Features
- [ ] Movie search & filtering
- [ ] Advanced seat selection map
- [ ] Booking history with cancellation
- [ ] Refund processing
- [ ] Multiple language support
- [ ] User reviews & ratings

### Phase 3 Features
- [ ] Mobile app (React Native)
- [ ] Analytics dashboard
- [ ] Promotional codes & discounts
- [ ] SMS notifications
- [ ] Theater management system
- [ ] Multi-city support

### DevOps & Deployment
- [ ] Docker containerization
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] AWS/Heroku deployment
- [ ] Performance monitoring
- [ ] Error tracking (Sentry)
- [ ] Log aggregation (ELK stack)

---

## 📞 Support & Contact

### Issues or Questions?
1. Check troubleshooting section
2. Review terminal output for errors
3. Check Django logs
4. Review email configuration

### Common Documentation
- Django Docs: https://docs.djangoproject.com/
- Razorpay Docs: https://razorpay.com/docs/
- Google Gemini: https://ai.google.dev/docs/
- Django Admin: https://docs.djangoproject.com/en/5.2/ref/contrib/admin/

---

## 👨‍💻 Author & Credits

**Developed by**: Kamani Sanjay Kumar  
**Email**: kamanisanju2705@gmail.com  
**Date**: January 2026  

### Technologies Used
- Django Web Framework
- Python Programming Language
- Google Generative AI
- Razorpay Payment Gateway
- Gmail SMTP Service
- SQLite/PostgreSQL Database

---

## 📄 License

This project is provided as-is for educational and commercial use.

---

**Last Updated**: January 23, 2026  
**Version**: 2.0 (With AI & Email Features)  
**Status**: Production Ready ✅
