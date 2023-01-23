from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.StaffLoginView.as_view(), name='login'),
    path('logout/', views.StaffLogoutView.as_view(), name='logout'),
    path('staff/', views.reserveListView.as_view(), name='main'),
    path('blog/', views.viewBlogs.as_view(), name='blog'),
    path('blog/new', views.newBlog.as_view(), name='blog.add'),
    path('blog/delete/<int:pk>', views.deleteBlogs.as_view(), name='blog.delete'),
    path('blog/update/<int:pk>', views.updateBlogs.as_view(), name='blog.update'),
    path('reservation/new', views.newReserveStaff.as_view(), name='reservation.new.staff'),
    path('reservation/delete/<int:pk>', views.deleteReservation.as_view(), name='reservation.delete'),
]
