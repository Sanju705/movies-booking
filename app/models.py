from django.contrib.auth.models import AbstractUser
from django.db import models

class ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    date = models.DateField()
    showtime = models.TimeField()
    ticket = models.PositiveIntegerField()
    email = models.EmailField()

class CinemaUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
