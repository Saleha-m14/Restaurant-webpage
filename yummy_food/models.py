from django.db import models

# Create a model for table booking


class Booking(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.IntegerField(max_length=15, null=False, blank=False)
    email = models.EmailField()
    person_number = models.IntegerField(null=False, blank=False, default=2)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.name
