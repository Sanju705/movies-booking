from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    
    date = models.DateField()
    showtime = models.TimeField()
    ticket = models.PositiveIntegerField()
    email = models.EmailField(default="kamanisanju2705@gmail.com")
    price = models.IntegerField(default=250)

class CinemaUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()  # in paise
    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, blank=True)
    razorpay_signature = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.status}"
