from django.db import models

# Create your models here.

class Customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  contactNumber = models.CharField(max_length=12)
  email = models.EmailField()

  def __str__(self):
    return f'{self.firstname} {self.lastname}'

class Discount(models.Model):
  discountCode= models.CharField(max_length=15)
  discountPercentage = models.DecimalField(decimal_places=2, max_digits=6)
  discountExpiration = models.DateTimeField()

  def __str__(self):
    return self.discountCode

class Facility(models.Model):
  FacilityCategoriesChoices = (
    
    ('pool','Pool'),
    ('rooms','Rooms'),
    ('cottages','Cottages'),
    ('EH','Event Hall'),
     
  )
  facilityName = models.CharField(max_length=255)
  facilityDescription = models.CharField(max_length=255)
  facilityCategory = models.CharField(max_length=20, choices=FacilityCategoriesChoices, blank = False, default='pool')
  facilityPic = models.ImageField(upload_to='facilities', null=True)
  facilityPrice = models.DecimalField(decimal_places=2, max_digits=8)
  
  #facilityPrice2 = models.DecimalField(decimal_places=2, max_digits=8, null=True)
  #facilityPrice3 = models.DecimalField(decimal_places=2, max_digits=8, null=True)
  
  facilitymax = models.IntegerField()
  facilityActive = models.BooleanField(default=False)

  def __str__(self):
    return self.facilityName

class Reservations(models.Model):
  reservationID = models.BigAutoField(primary_key=True)
  date = models.DateField(auto_created=True, null=True)
  time = models.TimeField(auto_created=True, null=True)
  checkIn = models.DateField()
  discounted = models.BigIntegerField()
  checkOut=models.DateField()
  downpayment = models.DecimalField(decimal_places=3, max_digits=10)
  totalPayment = models.DecimalField(decimal_places=3, max_digits=10)
  balance = models.DecimalField(decimal_places=3, max_digits=10)
  status = models.CharField(max_length=3)
  customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
  discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
  facility = models.ManyToManyField(Facility)

  