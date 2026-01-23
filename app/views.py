from django.shortcuts import render, HttpResponse,  get_object_or_404, redirect
from .forms import ticketbooking
from .models import ticket
from django.core.mail import send_mail
from django.conf import settings
from random import randint
import qrcode
from io import BytesIO
import base64
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from .email_service import send_ticket_email

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)


@login_required
def index(request):
    form = ticketbooking()
    if request.method == 'POST':
        form = ticketbooking(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['movie_name']
            showtime = form.cleaned_data['showtime']
            ticket_count = form.cleaned_data['ticket']
            date = form.cleaned_data['date']
            print(movie_name,date,showtime,ticket_count)
            
            # Check if user has email
            user_email = request.user.email
            if not user_email:
                print(f"⚠️ User {request.user.username} has no email address in profile")
                print(f"   Please update your profile with an email address")
            
            ticket_obj = ticket.objects.create(movie_name = movie_name,
                                   date = date, 
                                   showtime = showtime,
                                   ticket = ticket_count,
                                   email = user_email
                                   )
            
            # Send detailed ticket confirmation email with QR code
            if user_email:
                email_sent = send_ticket_email(ticket_obj, user_email)
                
                if email_sent:
                    print(f"✅ Ticket confirmation email sent to {user_email}")
                else:
                    print(f"⚠️ Failed to send ticket confirmation email to {user_email}")
            else:
                print(f"⚠️ Cannot send email - user has no email address in profile")

            return redirect("booked_ticket", id=ticket_obj.id)
        else:
            print('ntg')
    
    context = {"form":form}

    return render(request, 'index.html',context)

def upcoming(request):
    return render(request, 'upcoming.html')

def events(request):
    return render(request, 'events.html')

def gettickets(request):
    return render(request, 'gettickets.html')

def chatbot(request):
    """Display the AI chatbot interface"""
    return render(request, 'chatbot.html')

def booked_ticket(request,id):
    Ticket = get_object_or_404(ticket, id=id)

    qr_data = f"Movie:{Ticket.movie_name} | Date:{Ticket.date} | Time:{Ticket.showtime} | Seat:{Ticket.ticket}"

    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    #  # Send detailed ticket confirmation email with QR code
    #         email_sent = send_ticket_email(ticket_obj, ticket_obj.email)
            
    #         if email_sent:
    #             print(f"✅ Ticket confirmation email sent to {ticket_obj.email}")
    #         else:
    #             print(f"⚠️ Failed to send ticket confirmation email to {ticket_obj.email}")

    context = {
        "Ticket": Ticket,
        "qr_code": qr_base64
    }
    return render(request, "booked_ticket.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.phone = form.cleaned_data['phone']
                user.dob = form.cleaned_data['dob']
                user.save()
                print(f"✅ New user registered successfully: {user.username}")
                print(f"   Email: {user.email}")
                print(f"   Phone: {user.phone}")
                return redirect('login')
            except Exception as e:
                print(f"❌ Error saving user: {str(e)}")
                return render(request, 'register.html', {'form': form, 'error': 'Failed to create account'})
        else:
            print(f"❌ Form validation failed for user: {form.data.get('username', 'unknown')}")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"   {field}: {error}")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

# def payment(request, id):
#     amount = 300  # Rs.300 ticket
#     amount_paise = amount * 100

#     order = client.order.create({
#         "amount": amount_paise,
#         "currency": "INR",
#         "payment_capture": "1"
#     })

#     payment = Payment.objects.create(
#         user=request.user,
#         amount=amount_paise,
#         razorpay_order_id=order['id']
#     )

def payment(request, id):
    ticket_obj = ticket.objects.get(id=id)

    amount = ticket_obj.price * ticket_obj.price * 100  # in paise

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "ticket": ticket_obj,
        "order_id": order['id'],
        "amount": ticket_obj.price * ticket_obj.prices,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }
    return render(request, "payment.html", context)


#     context = {
#         "order_id": order['id'],
#         "amount": amount,
#         "razorpay_key": settings.RAZORPAY_KEY_ID
#     }
#     return render(request, "payment.html", context)


# @csrf_exempt
# def payment_success(request):
#     if request.method == "POST":
#         razorpay_payment_id = request.POST.get("razorpay_payment_id")
#         razorpay_order_id = request.POST.get("razorpay_order_id")
#         razorpay_signature = request.POST.get("razorpay_signature")

#         payment = Payment.objects.get(razorpay_order_id=razorpay_order_id)
#         payment.razorpay_payment_id = razorpay_payment_id
#         payment.razorpay_signature = razorpay_signature
#         payment.status = "SUCCESS"
#         payment.save()

#         return render(request, "booked_ticket.html.html")
