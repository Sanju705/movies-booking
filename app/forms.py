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
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
        help_text='Required. Enter a valid email address.'
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '10-digit phone number'}),
        help_text='Required. 10-digit phone number.'
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Required. Your date of birth.'
    )

    class Meta:
        model = CinemaUser
        fields = ['username', 'email', 'phone', 'dob', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        
        # Add placeholders to widgets
        for field in self.fields:
            if 'placeholder' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({
                    'placeholder': f'Enter {field}'
                })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and CinemaUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and len(phone) < 10:
            raise forms.ValidationError('Phone number must be at least 10 digits.')
        if phone and CinemaUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('This phone number is already registered.')
        return phone
