from django.db import models


class MonthReport(models.Model):
    report_date = models.DateField(auto_now_add=True)
    total_reservations = models.IntegerField()
    total_customers = models.IntegerField()
    total_earnings = models.IntegerField()
