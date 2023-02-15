from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.StaffLoginView.as_view(), name='login'),
    path('logout/', views.StaffLogoutView.as_view(), name='logout'),
    path('staff/', views.reserveListView.as_view(), name='main'),
    path('staff/facility/new', views.newFacility.as_view(), name='facility.new')
]
