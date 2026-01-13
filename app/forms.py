from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CinemaUser, ticket

class ticketbooking(forms.Form):
    # class Meta:
    #     model = ticket
    #     fields = '__all__'
    movie_name = forms.CharField()
    date = forms.DateField()
    showtime = forms.TimeField()
    ticket = forms.IntegerField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CinemaUser
        fields = ['username', 'email', 'phone', 'dob', 'password1', 'password2']
