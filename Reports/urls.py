from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("reports/", views.SalesReport.as_view(), name="reports"),
    path("reports/history", views.reports_month_history, name="reports.history"),
]
