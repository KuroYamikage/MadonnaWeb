from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    contactNumber = models.CharField(max_length=12, null=False)
    email = models.EmailField(null=False)
    visit = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Reward(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=255)
    minimumVisits = models.IntegerField(default=0)
    customers = models.ManyToManyField(Customer, related_name="rewards")


class Discount(models.Model):
    discountCode = models.CharField(max_length=15, unique=True, blank=True, null=True)
    discountPrice = models.DecimalField(decimal_places=2, max_digits=10)
    discountActive = models.BooleanField(default=False)

    def __str__(self):
        return self.discountCode


class Facility(models.Model):
    FacilityCategoriesChoices = (
        ("pool", "Pool"),
        ("rooms", "Rooms"),
        ("cottages", "Cottages"),
        ("EH", "Event Hall"),
    )
    facilityName = models.CharField(max_length=255, unique=True)
    facilityDescription = models.CharField(max_length=255)
    facilityCategory = models.CharField(
        max_length=20, choices=FacilityCategoriesChoices, blank=False, default="pool"
    )
    facilityPic = models.ImageField(upload_to="facilities", null=True)
    facilityPrice = models.DecimalField(decimal_places=2, max_digits=8)
    # facilityPrice2 = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    # facilityPrice3 = models.DecimalField(decimal_places=2, max_digits=8, null=True)
    facility_free = models.IntegerField( default=0)
    facilitymax = models.IntegerField()
    facilityActive = models.BooleanField(default=False)

    def __str__(self):
        return self.facilityName


class Prices(models.Model):
    dayTimeChoices = (("Day", "Day"), ("Night", "Night"), ("Whole Day", "Whole Day"))
    maxPax = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dayTime = models.CharField(max_length=150, choices=dayTimeChoices)

    def __str__(self) -> str:
        return f"For {self.dayTime} Reservation with Maximum of {self.maxPax} Pax"


class Reservations(models.Model):
    reservationChoices = (
        ("Approved", "Approved"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    )

    reservationID = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    checkIn = models.DateField()
    checkOut = models.DateField()
    timeIn = models.TimeField()
    timeOut = models.TimeField()
    downpayment = models.DecimalField(decimal_places=3, max_digits=10)
    totalPayment = models.DecimalField(decimal_places=3, max_digits=10)
    balance = models.DecimalField(decimal_places=3, max_digits=10)
    status = models.CharField(
        choices=reservationChoices, max_length=10, default="Pending"
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1) # type: ignore
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, default=1) # type: ignore
    facility = models.ManyToManyField(Facility)
    prices = models.ForeignKey(Prices, on_delete=models.CASCADE)
    referenceNum = models.CharField(max_length=247, unique=True, null=True)


