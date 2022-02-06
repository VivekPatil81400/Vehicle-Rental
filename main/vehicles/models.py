from django.db import models
from customers.models import Customers

# Create your models here.
VEHICLE_TYPE = (
    ('bike','Bike'),
    ('cycle','Cycle'),
    ('car','Car'),
    ('boat','Boat'),
)

class Booking(models.Model):
    customer_name=models.ForeignKey('customers.Customers', related_name='customers', on_delete=models.CASCADE)
    rental_date=models.DateField(null=False)
    return_date=models.DateField()
    vehicle_type=models.CharField(max_length=6, choices=VEHICLE_TYPE, default='bike')

class Vehicles(models.Model):
    vehicle=models.CharField(max_length=6, choices=VEHICLE_TYPE, default='bike')
    count=models.IntegerField()

    def __str__(self):
        return self.vehicle
