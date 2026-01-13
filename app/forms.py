from django import forms

class ticketbooking(forms.Form):
    # class Meta:
    #     model = ticket
    #     fields = '__all__'
    movie_name = forms.CharField()
    date = forms.DateField()
    showtime = forms.TimeField()
    ticket = forms.IntegerField()