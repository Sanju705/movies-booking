from django.shortcuts import render, HttpResponse,  get_object_or_404, redirect
from .forms import ticketbooking
from .models import ticket
from django.core.mail import send_mail
from django.conf import settings
from random import randint
import qrcode
from io import BytesIO
import base64

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