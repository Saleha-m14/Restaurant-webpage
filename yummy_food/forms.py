from django import forms
from .models import Booking


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
