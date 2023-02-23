from django.db import models

# Create your models here.


class Reservations(models.Model):
    reservationID = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_created=True, null=True)
    time = models.TimeField(auto_created=True, null=True)
    discounted = models.BigIntegerField()
    checkIn = models.DateField()
    checkOut = models.DateField()
    downpayment = models.DecimalField(decimal_places=3, max_digits=10)
    totalPayment = models.DecimalField(decimal_places=3, max_digits=10)
    balance = models.DecimalField(decimal_places=3, max_digits=10)
    status = models.CharField(max_length=3)


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    contactNumber = models.CharField(max_length=12)
    email = models.EmailField()


class Discount(models.Model):
    discountCode = models.CharField(max_length=15)
    discountPercentage = models.DecimalField(decimal_places=3, max_digits=3)
    discountExpiration = models.DateTimeField()


class Facility(models.Model):
    facilityName = models.CharField(max_length=255)
    facilityDescription = models.CharField(max_length=255)
    facilityPic = models.ImageField()
    facilityPrice = models.DecimalField(decimal_places=3, max_digits=6)
    facilitymax = models.IntegerField()
