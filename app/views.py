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
            ticket_obj = ticket.objects.create(movie_name = movie_name,
                                   date = date, 
                                   showtime = showtime,
                                   ticket = ticket_count
                                   )
            # send_mail("successfully booked movie ticket ",f"" ,settings.EMAIL_HOST_USER,[ticket_obj.email],fail_silently=False)
            send_mail(
    "successfully booked movie ticket",
    "",
    settings.EMAIL_HOST_USER,
    [ticket_obj.email],
    fail_silently=False
)

            return redirect("pay", id=ticket_obj.id)
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

    context = {
        "Ticket": Ticket,
        "qr_code": qr_base64
    }
    return render(request, "booked_ticket.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
