from django.db import models
from Reservation.models import Discount

# Create your models here.

class RoomType(models.Model):
    room_type = models.CharField(max_length=50)

    def __str__(self):
        return self.room_type

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.room_number  # You can change this to display room type and number

class RoomAvailability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room} on {self.date}"
    
class Reservation(models.Model):
    room = models.ManyToManyField(Room,  default=1)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    check_in_time = models.TimeField()  # New field for check-in time
    check_out_time = models.TimeField()  # New field for check-out time
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    num_guests = models.PositiveIntegerField(default=1)
    discount_code = models.ForeignKey(Discount, on_delete=models.SET_NULL, null= True, blank= True)
    reservation_time = models.CharField(max_length=10, choices=[('Morning', 'Morning'), ('Night', 'Night')])
    RESERVATION_TYPE_CHOICES = (
        ('private', 'Private'),
        ('public', 'Public'),
    )

    reservation_type = models.CharField(max_length=10, choices=RESERVATION_TYPE_CHOICES)
    reference_number = models.CharField(max_length=10, unique=True, null=True)
    reservationChoices=(
    ('Approved','Approved'),
    ('Pending','Pending'),
    ('Cancelled','Cancelled'),
  )
    status = models.CharField(choices=reservationChoices, max_length=10,default='Pending')


class UnavailableDate(models.Model):
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)