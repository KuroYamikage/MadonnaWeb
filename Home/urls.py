from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sample', views.sample, name='sample'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('reserve', views.reservations, name='reserve'),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]