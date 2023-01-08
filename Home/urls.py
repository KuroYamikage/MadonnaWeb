from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sample', views.sample, name='sample'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('reserve', views.reservations, name='reserve'),
]