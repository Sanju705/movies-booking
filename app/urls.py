# from django.urls import path, include
# from . import views

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('index', views.index,name='index'),
    path("register/", views.register, name="register"),
    path('upcoming/',views.upcoming, name='upcoming'),
    path('events/',views.events, name='events'),
    path('gettickets/',views.gettickets, name='gettickets'),
    path('booked_ticket/<int:id>/', views.booked_ticket, name="booked_ticket")
]


