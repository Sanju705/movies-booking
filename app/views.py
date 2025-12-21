from django.shortcuts import render, redirect
from .forms import ticketbooking
from .models import ticket
from django.core.mail import send_mail
from django.conf import settings
from random import randint

def index(request):
    if request.method == 'POST':
        form = ticketbooking(request.POST)
        if form.is_valid():
            ticket = form.save()
            subject = "Your movie ticket booking"
            message = (
                f"Thank you for booking!\n\n"
                f"Movie: {ticket.movie_name}\n"
                f"Date: {ticket.date}\n"
                f"Show time: {ticket.showtime}\n"
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                fail_silently=False,
            )
            return redirect("getttickets")
        else:
            form = ticketbooking()
    # context = {
    #     "form": form,
    # }

    return render(request, 'index.html')

def upcoming(request):
    return render(request, 'upcoming.html')

def events(request):
    return render(request, 'events.html')

def gettickets(request):
    return render(request, 'gettickets.html')