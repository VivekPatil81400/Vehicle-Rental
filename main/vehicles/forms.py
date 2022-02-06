from django import forms
from .models import Booking

class Rentalform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'rental_date', 'return_date', 'vehicle_type']