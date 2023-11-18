#!/usr/bin/env python3
import base64
from datetime import datetime
from io import BytesIO
from test.models import Reservation

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from django.utils import timezone
from Reports.models import MonthReport
from django.db.models import Sum


def generate_plot(
    queryset, x_field, y_field, date_format, date_locator, date_formatter
):
    df = pd.DataFrame(queryset.values(x_field, y_field))
    df.sort_values(by=x_field, inplace=True)

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter(date_formatter))
    ax.xaxis.set_major_locator(date_locator)
    ax.plot(df[x_field], df[y_field])
    fig.autofmt_xdate()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    graphic = base64.b64encode(buffer.read()).decode()

    return graphic


def month():
    now = datetime.now()
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0)

    queryset = Reservation.objects.filter(check_in_date__range=[start_of_month, now])

    graphic = generate_plot(
        queryset,
        x_field="check_in_date",
        y_field="payments",
        date_format="%m/%d/%Y",
        date_locator=mdates.DayLocator(),
        date_formatter="%m/%d/%Y",
    )

    total_earnings = queryset.values("payments").aggregate(
        total_earnings=Sum("payments")
    )["total_earnings"]
    total_reservations = queryset.count()

    return graphic, total_earnings, total_reservations


def year():
    current_year = timezone.now().year
    queryset = MonthReport.objects.filter(report_date__year=current_year)

    graphic = generate_plot(
        queryset,
        x_field="report_date",
        y_field="total_earnings",
        date_format="%m",
        date_locator=mdates.MonthLocator(),
        date_formatter="%m",
    )

    return graphic
