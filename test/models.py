from django.db import models
from Reservation.models import Discount, Facility
import random
import string
from decimal import Decimal

# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(Facility, on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    free_guests = models.IntegerField(default=0)

    def __str__(self):
        return self.room_number  # You can change this to display room type and number


    
class Reservation(models.Model):
    room = models.ManyToManyField(Room,  default=1, blank=True, null=True)
    POOL_CHOICES = (
        ('Pool 1','Pool 1'),
        ('Pool 2','Pool 2'),
    )
    pool = models.CharField(max_length=20, choices=POOL_CHOICES)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    check_in_time = models.TimeField()  # New field for check-in time
    check_out_time = models.TimeField()  # New field for check-out time
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    num_guests = models.PositiveIntegerField(default=1)
    num_child = models.PositiveIntegerField(default=0, null=True, blank=True)
    withRoom = models.BooleanField(null=True, blank=True)
    discount_code = models.ForeignKey(Discount, on_delete=models.SET_NULL, null= True, blank= True)
    reservation_time = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Night', 'Night')])
    RESERVATION_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    reservation_type = models.CharField(max_length=10, choices=RESERVATION_TYPE_CHOICES, null=False)
    reference_number = models.CharField(max_length=16, unique=True, null=True)
    reservationChoices=(
    ('Approved','Approved'),
    ('Pending','Pending'),
    ('Cancelled','Cancelled'),
  )
    status = models.CharField(choices=reservationChoices, max_length=10,default='Pending')
    date = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payments = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # type: ignore

    def generate_unique_reference_number(self):
        while True:
            reference_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            if not Reservation.objects.filter(reference_number=reference_number).exists():
                return 'MGREP-' + reference_number

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = self.generate_unique_reference_number()     
        super().save(*args, **kwargs)



class UnavailableDate(models.Model):
    dates = models.DateField()
    pool1 = models.BooleanField(default=False)
    pool2 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.dates)

class Prices(models.Model):
    dayTimeChoices = (('', '---------'),("Day", "Day"), ("Night", "Night"), ("22 Hours", "22 Hours"))
    reservationTypeChoices = (("Public","Public"),("Private","Private"))
    guestTypeChoices = (('', '---------'),("Adult","Adult"),("Child","Child"))
    maxPaxChoices = ((0, '---------'),(25,"25"),(50,"50"))
    dateChoices = (('', '---------'),("Weekday","Monday to Thursday"), ("Weekend","Friday to Sunday, and Holiday"))
    maxPax = models.IntegerField(blank=True, null=True, choices=maxPaxChoices)
    guest = models.CharField(choices=guestTypeChoices, blank=True, null=True, max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.CharField(choices=reservationTypeChoices, default="Private",max_length=10)
    time = models.CharField(max_length=150, choices=dayTimeChoices)
    withRoom = models.BooleanField(blank=True, null=True)
    date = models.CharField(blank=True, null=True, max_length=50, choices=dateChoices)

    # def __str__(self) -> str:
    #     return f"For {self.dayTime} Reservation with Maximum of {self.maxPax} Pax"



class Payment(models.Model):
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    payment_method_id = models.CharField(max_length=50)