from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', views.index, name='index'),
    path('sample', views.sample, name='test'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]