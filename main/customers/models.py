from django.db import models
import uuid
# Create your models here.
class Customers(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    customer_email = models.CharField(max_length=30)

    def __str__(self):
        return self.customer_name