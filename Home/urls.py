from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', views.indexView.as_view(), name='index'),
    path('about', views.aboutView.as_view(), name='about'),
    path('sample', views.sampleView.as_view(), name='sample'),
    path('add/', views.addView.as_view(), name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('reserve', views.reserveView.as_view(), name='reserve'),
    path('reservation/<int:pk>', views.moreDetailView.as_view(),name = 'reservation'),
    path('reservation/new', views.newReserve.as_view(), name='reservation.new'),
]