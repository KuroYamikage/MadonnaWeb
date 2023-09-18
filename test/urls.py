from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("test/", views.testReserve, name="test"),
    path('create-reservation/',views. ReservationCreateView.as_view(), name='create_reservation'),
    path('reservation-success/', views.ReservationSuccessView.as_view(), name='reservation_success'),
]