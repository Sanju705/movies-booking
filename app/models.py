from django.db import models

class ticket(models.Model):
    movie_name = models.CharField(max_length=100)
    date = models.DateField()
    showtime = models.TimeField()
    ticket = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.movie_name} - {self.date} {self.showtime}"
    
  