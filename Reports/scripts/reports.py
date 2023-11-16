#!/usr/bin/env python3
import base64
from io import BytesIO
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from django.db import connection


def month():
    query = "SELECT check_in_date, payments FROM test_reservation WHERE DATE(check_in_date) BETWEEN DATE('now', 'start of month') AND DATE('now')"
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    # df = pd.read_sql_query(query, db, parse_dates=["checkIn"])
    df = pd.DataFrame(results, columns=["check_in_date", "payments"])
    df.sort_values(by="check_in_date", inplace=True)

    df_grouped = df.groupby("check_in_date")["payments"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.plot(df_grouped["check_in_date"], df_grouped["payments"])
    fig.autofmt_xdate()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    graphic = base64.b64encode(buffer.read()).decode()
    total_earnings = df["payments"].sum()
    total_reservations = len(df)

    return graphic, total_earnings, total_reservations


"""
def week():
    db = sqlite3.connect("../../db.sqlite3")
    query = "SELECT checkIn, totalPayment FROM Reservation_reservations WHERE strftime('%W', checkIn) = strftime('%W', 'now')"

    df = pd.read_sql_query(query, db, parse_dates=["checkIn"])
    df.sort_values(by="checkIn", inplace=True)
    print(df.head())

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(df["checkIn"], df["totalPayment"])
    plt.gcf().autofmt_xdate()
    plt.show()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    graphic = base64.b64encode(buffer.read()).decode()

    context["graphic"] = graphic

    return context
"""
