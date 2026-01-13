from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('upcoming/',views.upcoming, name='upcoming'),
    path('events/',views.events, name='events'),
    path('gettickets/',views.gettickets, name='gettickets'),
    path('booked_ticket/<int:id>/', views.booked_ticket, name="booked_ticket")
]

