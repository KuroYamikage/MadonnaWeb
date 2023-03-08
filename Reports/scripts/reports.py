#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sqlite3
from io import BytesIO
import base64
from django.db import connection


def month():
    query = "SELECT checkIn, totalPayment FROM Reservation_reservations WHERE strftime('%m', checkIn) = strftime('%m', 'now')"

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    # df = pd.read_sql_query(query, db, parse_dates=["checkIn"])
    df = pd.DataFrame(results, columns=["checkIn", "totalPayment"])
    df.sort_values(by="checkIn", inplace=True)

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.plot(df["checkIn"], df["totalPayment"])
    fig.autofmt_xdate()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    graphic = base64.b64encode(buffer.read()).decode()
    total_earnings = df["totalPayment"].sum()
    total_reservations = len(df)

    return graphic, total_earnings, total_reservations


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
