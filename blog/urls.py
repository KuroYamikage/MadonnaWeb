from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('staff/blog', views.viewBlogs.as_view(), name='blog'),
    path('new/', views.newBlog.as_view(), name='blog.add'),
    path('delete/<int:pk>/', views.deleteBlogs.as_view(), name='blog.delete'),
    path('update/<int:pk>/', views.updateBlogs.as_view(), name='blog.update'),
]