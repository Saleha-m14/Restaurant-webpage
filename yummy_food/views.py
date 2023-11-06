from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import TableBookingForm
from django.contrib import messages
# Create your views here.


def home(request):
    """This is the first page that appears.
    It extends the base.html file and
    render index.html
    """
    return render(request, 'index.html')


def booking_page(request):
    """ This is the table booking page that 
    enables the user to fill the form and
    book a table. The should login to make a reservation.
    If user is loged in it renders booking.html and if not
    the user should login or signup.
    """
    form = TableBookingForm()
    if request.method == 'POST':
        form = TableBookingForm(data=request.POST)

        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user
            new_booking.save()
            messages.success(
                request, 'Your table in Yummy Restaurant is booked.')
            return redirect('managebooking')
        else:
            messages.error(
                request, 'You have already booked a table or entered invalid data'
            )
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)
    


def managebooking(request):
    """
    This is the view that shows the booking information
    that is made by the user if the user is not logged in 
    then redirect the user to the signup page.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'managebooking.html', context)
    else:
        redirect('../account/signup')


def changebooking(request, booking_id):
    """ This will render the change_booking.html and allows
    the user to bring changes to his/her bookings.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('managebooking')
    if request.method == 'POST':
        form = TableBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'You updated your bookings')
            return redirect('managebooking')
    form = TableBookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'change_booking.html', context)


def deletebooking(request, booking_id):
    """This is the view for deleting a booking that is
    made by a user. The user should match the user that
    made the booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('managebooking')
    booking.delete()
    messages.success(request, 'You deleted your booking!')
    return redirect('managebooking')
