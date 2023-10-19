from django import forms
from django.core.validators import EmailValidator
from .models import Booking


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
