from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.indexView.as_view(), name='index'),
    path('about', views.aboutView.as_view(), name='about'),
    path('sample', views.sampleView.as_view(), name='sample'),
    path('add/', views.addView.as_view(), name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('reserve', views.reserveView.as_view(), name='reserve'),
    path('reservation/<int:pk>', views.moreDetailView.as_view(),name = 'reservation'),
    path('reservation/new', views.newReserve.as_view(), name='reservation.new'),
    path('reservation/edit/<int:pk>', views.updateReserve.as_view(), name="reservation.edit"),
    path('blog/', views.viewBlogs.as_view(), name='blog'),
    path('blog/new', views.newBlog.as_view(), name='addblog'),

]