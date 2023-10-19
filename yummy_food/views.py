from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, redirect
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return HttpResponse('Success!')


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
    return HttpResponse("You booked a table in Yummy Restaurant")
