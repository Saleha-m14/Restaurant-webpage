from django.db import models

# Create a model for table booking


class Booking(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    phone = models.IntegerField(null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    person_number = models.IntegerField(null=False, blank=False, default=2)


    def __str__(self):
        return self.name
