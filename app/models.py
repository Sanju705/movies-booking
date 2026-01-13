from django.db import models

class ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    date = models.DateField()
    showtime = models.TimeField()
    ticket = models.PositiveIntegerField()
    email = models.EmailField()