# 📧 EMAIL SETUP GUIDE - Ticket Confirmation with QR Code

## Overview

When a user books a movie ticket, they automatically receive a beautiful email with:
- ✅ Movie details (name, date, time)
- ✅ Ticket information (quantity, price, total)
- ✅ QR code image (embedded in email)
- ✅ Professional HTML styling
- ✅ Plain text fallback

---

## 🔧 Setup Instructions

### Step 1: Configure Email Settings in Django

Edit `moviesbooking/settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Google App Password, NOT your regular password
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### Step 2: Get Google App Password (Gmail)

If using Gmail, you need an **App Password** (not your regular password):

1. Go to: https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already enabled)
3. Go to **App Passwords**
4. Select: App = Mail, Device = Windows Computer
5. Copy the 16-character password
6. Use this in `EMAIL_HOST_PASSWORD`

**Example:**
```
Regular password: MyPassword123
App password: uqem layc urhf rtgh  ← Use THIS
```

### Step 3: Update Settings.py

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kamanisanju2705@gmail.com'
EMAIL_HOST_PASSWORD = 'uqem layc urhf rtgh'  # App password from Google
DEFAULT_FROM_EMAIL = 'kamanisanju2705@gmail.com'
```

### Step 4: Or Use Environment Variables (Recommended)

Create `.env` file:
```
EMAIL_HOST_USER=kamanisanju2705@gmail.com
EMAIL_HOST_PASSWORD=uqem layc urhf rtgh
```

Update `settings.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
```

---

## 📧 Files Created/Modified

### New File: `app/email_service.py`
- `generate_qr_code()` - Generates QR code from ticket data
- `send_ticket_email()` - Sends formatted email with QR code

### Modified: `app/views.py`
- Added import: `from .email_service import send_ticket_email`
- Updated `index()` view to call `send_ticket_email()`

---

## 🎨 Email Template Preview

The email contains:
```
┌─────────────────────────────────────┐
│     🎬 Movie Ticket Confirmed!      │
│  Your booking is confirmed. Keep   │
│  this email safe.                  │
├─────────────────────────────────────┤
│ Ticket Details                      │
│                                     │
│ Movie Name: Dune: Part Two         │
│ Date: 23 January 2026              │
│ Show Time: 07:00 PM                │
│ Number of Tickets: 2               │
│ Price per Ticket: ₹300             │
│ Total Amount: ₹600                 │
│ Ticket ID: #42                     │
├─────────────────────────────────────┤
│     Your Ticket QR Code            │
│                                     │
│     [QR CODE IMAGE HERE]            │
│                                     │
│     Movie:Dune: Part Two |          │
│     Date:2026-01-23 | Time:...     │
├─────────────────────────────────────┤
│  Thank you for booking with us!    │
│                                     │
│  For support: support@cine.com     │
└─────────────────────────────────────┘
```

---

## 🧪 Test Email Sending

### Option 1: Test in Django Shell

```bash
python manage.py shell
```

```python
from app.models import ticket
from app.email_service import send_ticket_email
from datetime import date, time

# Create a test ticket
test_ticket = ticket.objects.create(
    movie_name="Test Movie",
    date=date.today(),
    showtime=time(19, 0),
    ticket=2,
    email="your-test-email@gmail.com",
    price=300
)

# Send test email
result = send_ticket_email(test_ticket, test_ticket.email)
print("Email sent successfully!" if result else "Failed to send email")
```

### Option 2: Use Django's Test Email Console

Update `settings.py`:
```python
# For development/testing - emails go to console instead of SMTP
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Emails will print to your terminal instead of sending.

### Option 3: Monitor Real Emails

After setting up real SMTP:
1. Restart Django server
2. Book a ticket through the web form
3. Check your email inbox
4. The email should arrive in ~2-5 seconds

---

## 🔒 Security Best Practices

1. **Never commit credentials** - Use `.env` file
2. **Use App Passwords** - Not your regular Gmail password
3. **Enable 2FA** - On your Google account
4. **Use environment variables** - Not hardcoded in settings.py
5. **Add to .gitignore** - Don't track `.env` in git

Example `.gitignore`:
```
.env
.env.local
*.env
__pycache__/
*.pyc
db.sqlite3
```

---

## 🐛 Troubleshooting

### ❌ Error: "Connection refused"
→ Check EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS settings

### ❌ Error: "Authentication failed"
→ Verify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
→ Make sure you're using App Password, not regular password

### ❌ Error: "SMTPAuthenticationError"
→ Gmail 2FA not enabled or wrong app password
→ Generate new App Password from Google

### ❌ Email not arriving
→ Check spam folder
→ Verify email address in ticket model
→ Check Django logs for errors

### ❌ QR code not showing in email
→ Some email clients don't support embedded images
→ QR code data is also provided as text

---

## 📊 Email Sending Flow

```
User Books Ticket
    ↓
Ticket created in database
    ↓
Call send_ticket_email()
    ↓
Generate QR code from ticket data
    ↓
Create HTML email with styling
    ↓
Embed QR code image in email
    ↓
Send via SMTP to user email
    ↓
Email received by user
```

---

## 🔌 Alternative Email Providers

### SendGrid
```python
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = 'your-sendgrid-key'
```

### AWS SES
```python
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'your-key'
AWS_SECRET_ACCESS_KEY = 'your-secret'
```

### Mailgun
```python
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'your-key'
MAILGUN_SERVER_NAME = 'sandboxXXX.mailgun.org'
```

---

## 📧 Customizing Email Template

To change email content, edit `app/email_service.py`:

### Change subject
```python
subject = f"🎬 Your Movie Ticket - {ticket_obj.movie_name}"
```

### Change styles/colors
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add more fields
```python
<div class="info-row">
    <span class="label">Cineplex:</span>
    <span class="value">Cineplex Downtown</span>
</div>
```

### Change footer
```python
<p>&copy; 2026 Your Cinema Name. All rights reserved.</p>
```

---

## 📈 Production Checklist

Before deploying to production:

- [ ] Email credentials in environment variables
- [ ] 2FA enabled on email account
- [ ] Using App Password (not regular password)
- [ ] SMTP server configured correctly
- [ ] Test email sending with real account
- [ ] Check email delivery in spam folder
- [ ] Monitor email sending logs
- [ ] Set up email error handling
- [ ] Configure bounce/complaint handling (if using AWS SES)

---

## 📞 Support

- Gmail SMTP: https://support.google.com/mail/answer/7126229
- SendGrid: https://sendgrid.com/docs/
- AWS SES: https://docs.aws.amazon.com/ses/
- Django Email: https://docs.djangoproject.com/en/5.0/topics/email/

---

**Your users will now receive beautiful ticket confirmation emails with QR codes! 📧✨**
