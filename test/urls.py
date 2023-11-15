from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("test/", views.testReserve, name="test"),
    path('create-reservation/',views.ReservationCreateView.as_view(), name='create_reservation'),
    path('private-reservation/',views.ReservationCreateViewPrivate.as_view(), name='private_reservation'),
    path('reservation-success/', views.ReservationSuccessView.as_view(), name='reservation_success'),
    path('validate_discount_code/', views.validate_discount_code, name='validate_discount_code'),
    path('reservation/summary/<str:reference_number>/', views.ReservationSummaryView.as_view(), name='reservation_summary'),
    path('create-price/', views.priceCreate.as_view(), name='create_price'),
    path('price/', views.priceList.as_view(), name='price'),
    path('price-update/<int:pk>', views.priceUpdate.as_view(), name='price_update'),
    path ('payment/',views.process_payment,name='pay'),
    path('reservation-edit/<int:pk>', views.ReservationUpdateView.as_view(), name='reservation_edit'),
    path('room_availability/', views.room_availability, name='room_availability'),
    path('pay/', views.pay_test, name='pay_test'), 
    path('payment/success/', views.payment_success, name='payment_success'),
    path('room_weekly_availability/', views.room_availability_weekly, name='week.availability'),
    path('payment/failure/', views.payment_failure, name='payment_failure'),

]  