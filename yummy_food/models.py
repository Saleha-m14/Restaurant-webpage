from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create a model for table booking


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking")
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    person_number = models.IntegerField(null=False, blank=False, default=2)

    def __str__(self):
        return self.name
