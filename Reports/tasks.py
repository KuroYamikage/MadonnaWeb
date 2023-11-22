from datetime import datetime
import calendar
from celery import shared_task
from .scripts.reports import month
from .models import MonthReport


@shared_task
def generate_monthly_report():
    current_year = datetime.now().year
    current_month = datetime.now().month
    end_of_month = calendar.monthrange(current_year, current_month)[1]
    today = datetime.now().day

    if current_month == 1:
        previous_month, previous_year = 12, current_year - 1
    else:
        previous_month, previous_year = current_month - 1, current_year

    if today == end_of_month:
        _, total_earnings, total_reservations = month()

        monthly_report = MonthReport(
            report_month=current_month,
            total_earnings=total_earnings,
            total_reservations=total_reservations,
        )

        monthly_report.save()
