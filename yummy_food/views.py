from django.shortcuts import render
from .models import Booking
from .forms import TableBookingForm
# Create your views here.


def home(request):
    """This is the first page that appears.
    It extends the base.html file and
    render index.html
    """
    return render(request, 'index.html')


def signup(request):
    """ This is the sign up page"""
    return render(request, "signup.html")


def signin(request):
    """ This is the sign up page"""
    return render(request, "signin.html")


def booking_page(request):
    """ This is the table booking page that 
    enables the user to fill the form and
    book a table.
    """
    booking_form = TableBookingForm()
    if request.method == 'POST':
        booking_form = TableBookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()

    context = {
        'form': booking_form
    }
    return render(request, 'booking.html', context)
