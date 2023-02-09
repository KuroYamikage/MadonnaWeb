from django.db import models

# Create your models here.

class Reservations(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  reservationID = models.BigAutoField(primary_key=True)
  date = models.DateField()
  downpayment = models.DecimalField(decimal_places=3, max_digits=10)
  totalPayment = models.DecimalField(decimal_places=3, max_digits=10)
  balance = models.DecimalField(decimal_places=3, max_digits=10)
  status = models.CharField(max_length=3)
  
