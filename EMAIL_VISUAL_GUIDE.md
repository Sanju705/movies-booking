# 📧 EMAIL FEATURE - VISUAL GUIDE & EXAMPLES

## 📬 What Users See

### Email in Inbox
```
From: your-email@gmail.com
To: user@example.com
Subject: 🎬 Your Movie Ticket Confirmation - Dune: Part Two
Date: Jan 23, 2026, 7:30 PM
```

### Email Body (HTML Rendered)
```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              🎬 Movie Ticket Confirmed!                 ║
║        Your booking is confirmed. Keep this              ║
║            email safe.                                   ║
║                                                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Ticket Details                                          ║
║  ─────────────────────────────────────────────────────   ║
║                                                           ║
║  Movie Name:           Dune: Part Two                    ║
║  Date:                 23 January 2026                   ║
║  Show Time:            07:00 PM                          ║
║  Number of Tickets:    2                                 ║
║  Price per Ticket:     ₹300                              ║
║  Total Amount:         ₹600                              ║
║  Ticket ID:            #42                               ║
║                                                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ⚠️ Important:                                            ║
║  Please present this QR code at the cinema               ║
║  entrance for ticket validation.                         ║
║                                                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║            Your Ticket QR Code                           ║
║  ─────────────────────────────────────────────────────   ║
║                                                           ║
║  Scan this QR code at the cinema or show it to           ║
║  the ticket counter.                                     ║
║                                                           ║
║              ▄▄▄▄▄▄▄                                      ║
║              █ ▄▄▄ █                                     ║
║              █ █   █ █                                   ║
║              █ █▀▀▀ █                                    ║
║              █       █                                   ║
║              ▀▀▀▀▀▀▀                                      ║
║                                                           ║
║   Movie:Dune: Part Two | Date:2026-01-23 |             ║
║   Time:19:00 | Seats:2                                  ║
║                                                           ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║         Thank you for booking with us!                  ║
║                                                           ║
║    This is an automated email. Please do not reply.      ║
║    For support, contact: your-email@gmail.com           ║
║    © 2026 Cine Movie Booking                            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🎬 Real Example

### Booking Process
```
1. User fills form:
   Movie: Oppenheimer
   Date: January 24, 2026
   Time: 9:00 PM
   Tickets: 3

2. User clicks "Book Ticket"

3. System creates ticket #47

4. IMMEDIATELY sends email with:
   ✅ All booking details
   ✅ QR code image
   ✅ Professional formatting
   ✅ Plain text fallback

5. User receives email in ~2 seconds
```

### Email Data in Backend

```python
# Ticket created
ticket_obj = {
    'id': 47,
    'movie_name': 'Oppenheimer',
    'date': '2026-01-24',
    'showtime': '21:00',
    'ticket': 3,
    'price': 300,
    'email': 'user@example.com',
    'total': 900  # 300 × 3
}

# QR code generated
qr_data = "Movie:Oppenheimer | Date:2026-01-24 | Time:21:00 | Seats:3"
qr_image = [base64 encoded PNG]

# Email sent
{
    'subject': '🎬 Your Movie Ticket Confirmation - Oppenheimer',
    'from': 'cinema@example.com',
    'to': 'user@example.com',
    'html': '<html with QR embedded>',
    'text': '<plain text version>'
}
```

---

## 🔧 Setup Process Visual

```
START
  │
  ├─► 1. Get App Password
  │   └─► Go to Google Security
  │       └─► Enable 2FA
  │           └─► Generate App Password (16 chars)
  │
  ├─► 2. Update settings.py
  │   └─► EMAIL_HOST = 'smtp.gmail.com'
  │       EMAIL_PORT = 587
  │       EMAIL_USE_TLS = True
  │       EMAIL_HOST_USER = 'your-email@gmail.com'
  │       EMAIL_HOST_PASSWORD = 'app-password'
  │       DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
  │
  ├─► 3. Restart Server
  │   └─► python manage.py runserver
  │
  ├─► 4. Test Booking
  │   └─► Create ticket through form
  │       └─► Check email inbox
  │           └─► Should arrive in 2-5 seconds
  │
  └─► DONE ✅
```

---

## 📊 Email Sending Diagram

```
┌─────────────────────────────────────────────────┐
│           USER BOOKS TICKET                     │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│    Create Ticket in Database                    │
│    (id=42, movie=Dune, date=2026-01-23, ...)   │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│   Call send_ticket_email(ticket, email)         │
└─────────────────────┬───────────────────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    ┌──────────────┐      ┌──────────────┐
    │ Generate QR  │      │ Build HTML   │
    │ Code Image   │      │ Email        │
    └──────┬───────┘      └──────┬───────┘
           │                     │
           │  base64 encode      │  embed QR
           │  ▼                  │  ▼
           └───────────┬─────────┘
                       │
                       ▼
        ┌──────────────────────────┐
        │  Create EmailMulti       │
        │  Alternatives object     │
        └──────────┬───────────────┘
                   │
       ┌───────────┴───────────┐
       │                       │
       ▼                       ▼
    ┌─────────┐          ┌─────────┐
    │ Text    │          │ HTML    │
    │ Version │          │ Version │
    └─────┬───┘          └─────┬───┘
          │                    │
          └────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────┐
    │  Send via Gmail SMTP     │
    │  (ssl, port 587)         │
    └──────────┬───────────────┘
               │
               ▼
    ┌──────────────────────────┐
    │  Gmail Server Sends      │
    │  Email to Recipient      │
    └──────────┬───────────────┘
               │
               ▼
    ┌──────────────────────────┐
    │  User Receives Email     │
    │  in Inbox                │
    │  ✅ With QR Code         │
    │  ✅ With Details         │
    │  ✅ Professional Format  │
    └──────────────────────────┘
```

---

## 🎨 Email Styling Breakdown

```
Header Section:
┌─────────────────────────────────────┐
│ 🎬 Movie Ticket Confirmed!         │ ← Purple gradient
│ Your booking is confirmed...        │
└─────────────────────────────────────┘

Details Section:
┌─────────────────────────────────────┐
│ Movie Name:      Dune: Part Two    │ ← Left: label
│ Date:            23 January 2026    │ ← Right: value (purple)
│ Show Time:       07:00 PM           │
│ ...                                 │
└─────────────────────────────────────┘

Warning Box:
┌─────────────────────────────────────┐
│ ⚠️ Important:                       │ ← Yellow background
│ Please present this QR code...      │
└─────────────────────────────────────┘

QR Section:
┌─────────────────────────────────────┐
│   Your Ticket QR Code              │ ← Centered
│   [QR IMAGE]                        │
│   Movie:Dune... | Date:...         │
└─────────────────────────────────────┘

Footer:
┌─────────────────────────────────────┐
│ © 2026 Cine Movie Booking          │ ← Gray text
│ For support: email@...              │
└─────────────────────────────────────┘
```

---

## 💻 Code Flow Example

```python
# 1. User submits form
POST /index/
{
    'movie_name': 'Dune: Part Two',
    'showtime': '19:00',
    'ticket': 2,
    'date': '2026-01-23'
}

# 2. View processes
@login_required
def index(request):
    form = ticketbooking(request.POST)
    if form.is_valid():
        # Create ticket
        ticket_obj = ticket.objects.create(...)
        
        # Send email with QR
        email_sent = send_ticket_email(ticket_obj, ticket_obj.email)
        #                      ↑
        #        New function in email_service.py
        
        if email_sent:
            print("✅ Email sent")
        
        return redirect("pay", id=ticket_obj.id)

# 3. email_service.py handles email
def send_ticket_email(ticket_obj, user_email):
    # Generate QR
    qr_base64, qr_data = generate_qr_code({
        'movie_name': ticket_obj.movie_name,
        'date': ticket_obj.date,
        'showtime': ticket_obj.showtime,
        'ticket': ticket_obj.ticket
    })
    
    # Create beautiful HTML with QR
    html_content = f"""
    <html>
        <h1>🎬 Movie Ticket Confirmed!</h1>
        <div class="details">
            <p>Movie: {ticket_obj.movie_name}</p>
            <p>Date: {ticket_obj.date}</p>
            ...
            <img src="data:image/png;base64,{qr_base64}">
        </div>
    </html>
    """
    
    # Send email
    email = EmailMultiAlternatives(...)
    email.attach_alternative(html_content, "text/html")
    email.send()
    
    return True
```

---

## 📱 Mobile Email View

```
╔═════════════════════════╗
║  📧 Gmail              ║
╠═════════════════════════╣
║ [←]  Movie Ticket...   ║
╠═════════════════════════╣
║ 🎬 Movie Ticket...     ║
║ your-email@gmail...    ║
║                         ║
║ 🎬 Movie Ticket        ║
║ Confirmed!             ║
║                         ║
║ Your booking is...     ║
║ [Expand]               ║
╠═════════════════════════╣
║ ─────────────────────── ║
║ Movie Name:   Dune     ║
║ Date:         23 Jan   ║
║ Show Time:    7 PM     ║
║ Tickets:      2        ║
║ Price:        ₹600     ║
║ ID:           #42      ║
║                         ║
║    [QR Code]           ║
║                         ║
║ Thank you!             ║
║ ─────────────────────── ║
║                         ║
║     [Reply] [Archive]  ║
╚═════════════════════════╝
```

---

## 🧪 Test Scenarios

### Scenario 1: Successful Email
```
✅ Ticket created
✅ QR code generated
✅ Email sent to: user@example.com
✅ User receives in 2-5 seconds
```

### Scenario 2: Email Fails (No Internet)
```
❌ SMTP connection failed
✅ Still shows "payment" page
✅ Console logs error
⚠️ User can still access ticket
```

### Scenario 3: Invalid Email
```
❌ Email address invalid
✅ Still creates ticket
✅ Django handles exception
⚠️ User notified to try again
```

---

## 🎯 Key Features Visualized

```
Feature 1: QR Code
  Input: Ticket Data
  Process: Generate QR image
  Output: Base64 PNG in email
  Result: User can scan at cinema

Feature 2: Professional HTML
  Input: Ticket object
  Process: Build styled HTML
  Output: Beautiful email layout
  Result: Professional appearance

Feature 3: Error Handling
  Input: Any error during send
  Process: Catch exception
  Output: Log error, continue
  Result: Graceful degradation

Feature 4: Multiple Formats
  Input: HTML + Text content
  Process: Create both versions
  Output: HTML + Text alternatives
  Result: Works on all email clients
```

---

**All visuals showing how emails look and flow! 📧✨**
