#!/usr/bin/env python3
import base64
from datetime import datetime
from io import BytesIO
from test.models import Reservation

import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from django.db.models import Sum
from django.utils import timezone
from plotly.subplots import make_subplots
from Reports.models import MonthReport


def month():
    now = datetime.now()
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0)

    queryset = Reservation.objects.filter(check_in_date__range=[start_of_month, now])
    df = pd.DataFrame(queryset.values("check_in_date", "payments"))
    df_grouped = df.groupby("check_in_date").agg({"payments": "sum"}).reset_index()
    fig = make_subplots()
    fig.add_trace(
        go.Scatter(
            x=df_grouped["check_in_date"], y=df_grouped["payments"], mode="lines"
        )
    )

    graphic = pyo.plot(fig, output_type="div", include_plotlyjs=True)
    total_earnings = queryset.values("payments").aggregate(
        total_earnings=Sum("payments")
    )["total_earnings"]
    total_reservations = queryset.count()

    return graphic, total_earnings, total_reservations


def year():
    current_year = timezone.now().year

    queryset = MonthReport.objects.filter(report_date__year=current_year)
    df = pd.DataFrame(
        queryset.values(
            "report_date", "month_over_month", "month_over_month_percentage"
        )
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(x=df["report_date"], y=df["month_over_month"], cliponaxis=False),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=df["report_date"],
            y=df["month_over_month_percentage"],
            mode="lines",
            cliponaxis=False,
        ),
        secondary_y=True,
    )
    tickvals = df["report_date"].tolist()
    fig.update_layout(
        xaxis=dict(tickvals=tickvals, type="date"),
        yaxis=dict(title="Month over Month", titlefont=dict(color="blue")),
        yaxis2=dict(
            title="(%)", titlefont=dict(color="red"), overlaying="y", side="right"
        ),
    )

    graphic = pyo.plot(fig, output_type="div", include_plotlyjs=False)

    return graphic
