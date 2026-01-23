"""
Email utility for sending ticket details with QR code
Handles email composition and QR code generation
"""

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import qrcode
from io import BytesIO
import base64
import smtplib
import socket


def generate_qr_code(ticket_data):
    """
    Generate QR code from ticket data
    Returns base64 encoded image
    """
    qr_data = f"Movie:{ticket_data['movie_name']} | Date:{ticket_data['date']} | Time:{ticket_data['showtime']} | Seats:{ticket_data['ticket']}"
    
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return qr_base64, qr_data


def send_ticket_email(ticket_obj, user_email):
    """
    Send ticket confirmation email with QR code and details
    
    Args:
        ticket_obj: Ticket object with booking details
        user_email: User's email address
    """
    try:
        # Validate email address
        if not user_email or not isinstance(user_email, str) or '@' not in user_email:
            print(f"\u274c Invalid email address: '{user_email}'")
            print(f"   Please ensure user has email in their profile")
            return False
        
        print(f"\n📧 Sending ticket email to: {user_email}")
        print(f"   Ticket ID: #{ticket_obj.id}")
        
        # Generate QR code
        qr_base64, qr_data = generate_qr_code({
            'movie_name': ticket_obj.movie_name,
            'date': ticket_obj.date,
            'showtime': ticket_obj.showtime,
            'ticket': ticket_obj.ticket
        })
        
        # Email subject and from address
        subject = f"🎬 Your Movie Ticket Confirmation - {ticket_obj.movie_name}"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user_email]
        
        # HTML email content
        html_content = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 20px auto;
                        background-color: white;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    }}
                    .header {{
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        padding: 20px;
                        border-radius: 10px;
                        text-align: center;
                        margin-bottom: 30px;
                    }}
                    .header h1 {{
                        margin: 0;
                        font-size: 28px;
                    }}
                    .ticket-info {{
                        background-color: #f9f9f9;
                        padding: 20px;
                        border-radius: 8px;
                        margin: 20px 0;
                        border-left: 4px solid #667eea;
                    }}
                    .info-row {{
                        display: flex;
                        justify-content: space-between;
                        padding: 12px 0;
                        border-bottom: 1px solid #eee;
                    }}
                    .info-row:last-child {{
                        border-bottom: none;
                    }}
                    .label {{
                        font-weight: bold;
                        color: #333;
                        width: 150px;
                    }}
                    .value {{
                        color: #667eea;
                        font-weight: 500;
                    }}
                    .qr-section {{
                        text-align: center;
                        margin: 30px 0;
                        padding: 20px;
                        background-color: #f9f9f9;
                        border-radius: 8px;
                    }}
                    .qr-section h2 {{
                        color: #333;
                        margin-top: 0;
                    }}
                    .qr-code {{
                        max-width: 250px;
                        margin: 20px auto;
                    }}
                    .qr-code img {{
                        max-width: 100%;
                        height: auto;
                    }}
                    .footer {{
                        text-align: center;
                        margin-top: 30px;
                        padding-top: 20px;
                        border-top: 1px solid #eee;
                        color: #666;
                        font-size: 12px;
                    }}
                    .button {{
                        display: inline-block;
                        background-color: #667eea;
                        color: white;
                        padding: 12px 30px;
                        border-radius: 5px;
                        text-decoration: none;
                        margin-top: 15px;
                        font-weight: bold;
                    }}
                    .important {{
                        background-color: #fff3cd;
                        border-left: 4px solid #ffc107;
                        padding: 15px;
                        border-radius: 4px;
                        margin: 20px 0;
                        color: #333;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🎬 Movie Ticket Confirmed!</h1>
                        <p>Your booking is confirmed. Keep this email safe.</p>
                    </div>
                    
                    <h2>Ticket Details</h2>
                    <div class="ticket-info">
                        <div class="info-row">
                            <span class="label">Movie Name:</span>
                            <span class="value">{ticket_obj.movie_name}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Date:</span>
                            <span class="value">{ticket_obj.date.strftime('%d %B %Y')}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Show Time:</span>
                            <span class="value">{ticket_obj.showtime.strftime('%I:%M %p')}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Number of Tickets:</span>
                            <span class="value">{ticket_obj.ticket}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Price per Ticket:</span>
                            <span class="value">₹{ticket_obj.price}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Total Amount:</span>
                            <span class="value">₹{ticket_obj.price * ticket_obj.ticket}</span>
                        </div>
                        <div class="info-row">
                            <span class="label">Ticket ID:</span>
                            <span class="value">#{ticket_obj.id}</span>
                        </div>
                    </div>
                    
                    <div class="important">
                        <strong>⚠️ Important:</strong> Please present this QR code at the cinema entrance for ticket validation.
                    </div>
                    
                    <div class="qr-section">
                        <h2>Your Ticket QR Code</h2>
                        <p>Scan this QR code at the cinema or show it to the ticket counter.</p>
                        <div class="qr-code">
                            <img src="data:image/png;base64,{qr_base64}" alt="Ticket QR Code">
                        </div>
                        <p style="font-size: 12px; color: #666; margin: 10px 0;">
                            {qr_data}
                        </p>
                    </div>
                    
                    <div style="text-align: center; margin-top: 25px;">
                        <p>Thank you for booking with us!</p>
                    </div>
                    
                    <div class="footer">
                        <p>This is an automated email. Please do not reply to this email.</p>
                        <p>For support, contact us at {settings.EMAIL_HOST_USER}</p>
                        <p>&copy; 2026 Cine Movie Booking. All rights reserved.</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        # Plain text alternative
        text_content = f"""
        🎬 MOVIE TICKET CONFIRMATION
        
        Movie: {ticket_obj.movie_name}
        Date: {ticket_obj.date.strftime('%d %B %Y')}
        Show Time: {ticket_obj.showtime.strftime('%I:%M %p')}
        Number of Tickets: {ticket_obj.ticket}
        Price per Ticket: ₹{ticket_obj.price}
        Total Amount: ₹{ticket_obj.price * ticket_obj.ticket}
        Ticket ID: #{ticket_obj.id}
        
        QR Code Data:
        {qr_data}
        
        Please present the QR code at the cinema entrance for validation.
        
        Thank you for booking with us!
        
        ---
        This is an automated email. Please do not reply.
        For support, contact: {settings.EMAIL_HOST_USER}
        """
        
        # Create email with both HTML and text versions
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=to_email
        )
        
        # Attach HTML version
        email.attach_alternative(html_content, "text/html")
        
        # Send email
        try:
            sent = email.send(fail_silently=False)
            if sent:
                print(f"✅ Email sent successfully to {user_email}")
                print(f"   Ticket ID: #{ticket_obj.id}")
                print(f"   Movie: {ticket_obj.movie_name}")
                return True
        except smtplib.SMTPAuthenticationError as auth_err:
            print(f"❌ SMTP Authentication Error: Check your Gmail app password")
            print(f"   Error: {str(auth_err)}")
            return False
        except smtplib.SMTPException as smtp_err:
            print(f"❌ SMTP Error: {str(smtp_err)}")
            return False
        except socket.gaierror as sock_err:
            print(f"❌ Network Error: Cannot connect to Gmail SMTP server")
            print(f"   Error: {str(sock_err)}")
            return False
        
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        print(f"   Type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False
