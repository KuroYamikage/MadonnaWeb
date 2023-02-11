from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('test/', views.test,name='test'),
    path('reserve/', views.reserveView.as_view(), name='reserve'),
    path('reservation/<int:pk>', views.moreDetailView.as_view(),name = 'reservation'),
    path('reservation/new', views.newReserve.as_view(), name='reservation.new'),
    path('reservation/edit/<int:pk>', views.updateReserve.as_view(), name="reservation.edit"),
    path('reservation/delete/<int:pk>', views.deleteReservation.as_view(), name='reservation.delete'),
    path('staff/reserve', views.newReserveStaff.as_view(), name='reserve.staff.new'),


]