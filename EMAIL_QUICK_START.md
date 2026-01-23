# 📧 EMAIL FEATURE - QUICK REFERENCE

## What's New

When users book movie tickets, they automatically receive:
- ✅ Beautiful HTML email with ticket details
- ✅ Movie name, date, and show time
- ✅ QR code embedded in email
- ✅ Price breakdown and total amount
- ✅ Ticket ID number
- ✅ Plain text fallback version

---

## 🚀 Quick Setup (5 minutes)

### 1. Get Gmail App Password
1. Go: https://myaccount.google.com/security
2. Enable 2-Step Verification (if needed)
3. Go to "App passwords"
4. Select Mail + Windows Computer
5. Copy the 16-character password

### 2. Update settings.py
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password-here'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

### 3. Run Server
```bash
python manage.py runserver
```

### 4. Test
1. Book a ticket
2. Check your email inbox
3. Email should arrive in 2-5 seconds

---

## 📁 Files Changed

### New File
- `app/email_service.py` - Email sending logic with QR code

### Modified Files
- `app/views.py` - Added email sending on ticket booking

---

## 🔌 Email Flow

```
User Books Ticket
    ↓
Ticket saved to database
    ↓
generate_qr_code() - Create QR image from ticket data
    ↓
send_ticket_email() - Generate HTML email
    ↓
Embed QR code image
    ↓
Send via Gmail SMTP
    ↓
User receives email with all details
```

---

## 📧 Email Contents

```
📧 Movie: Dune: Part Two
   Date: 23 January 2026
   Time: 07:00 PM
   Tickets: 2
   Price: ₹300 × 2 = ₹600
   
   [QR CODE IMAGE]
   
   Ticket ID: #42
```

---

## 🧪 Test Email (Without Real SMTP)

For development, use console email:

Edit `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Now emails print to your terminal instead of sending.

---

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| "Authentication failed" | Use App Password, not regular Gmail password |
| "Connection refused" | Check EMAIL_HOST and EMAIL_PORT |
| Email not arriving | Check spam folder, verify email is correct |
| QR code not showing | Some clients don't support embedded images (text backup provided) |

---

## ✅ Quick Checklist

- [ ] Gmail 2FA enabled
- [ ] App password generated
- [ ] EMAIL_HOST_USER set in settings.py
- [ ] EMAIL_HOST_PASSWORD set in settings.py
- [ ] Server restarted after changes
- [ ] Test email received

---

## 🔒 Security Note

**Never commit your password!** Use `.env` file instead:

```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

```
# .env
EMAIL_HOST_PASSWORD=your-app-password
```

Add `.env` to `.gitignore`

---

## 📧 What Users See

```
From: your-email@gmail.com
Subject: 🎬 Your Movie Ticket Confirmation - Dune: Part Two

═══════════════════════════════════════════
       🎬 Movie Ticket Confirmed!
═══════════════════════════════════════════

Ticket Details
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Movie Name:           Dune: Part Two
Date:                 23 January 2026
Show Time:            07:00 PM
Number of Tickets:    2
Price per Ticket:     ₹300
Total Amount:         ₹600
Ticket ID:            #42

⚠️ Important:
Please present this QR code at the cinema 
entrance for ticket validation.

Your Ticket QR Code
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         [QR CODE IMAGE]

Movie:Dune: Part Two | Date:2026-01-23...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for booking with us!

For support: your-email@gmail.com
```

---

## 💡 Tips

1. **Customize subject** - Edit `send_ticket_email()` in email_service.py
2. **Change colors** - Modify CSS in HTML template
3. **Add more fields** - Add info-row divs in email template
4. **Change sender name** - Update DEFAULT_FROM_EMAIL
5. **Send test email** - Run Django shell and use send_ticket_email()

---

**Your ticket emails are now live! 🚀📧**

See `EMAIL_SETUP.md` for complete documentation.
