from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegistrationForm
from django.views.generic import CreateView, TemplateView,ListView, DetailView, UpdateView
from Home.models import Reservations, Blog
from Home.forms import ReservationsForm, BlogForms
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

#Account Management
class StaffLoginView(LoginView):
  template_name = 'users/loginTest.php'
  redirect_authenticated_user= True


class StaffLogoutView(LoginRequiredMixin,LogoutView):
  template_name = 'users/logout.php'
  login_url = "login"


# Reservation Class
class reserveListView(LoginRequiredMixin,ListView):
  model = Reservations
  context_object_name = 'reserve'
  template_name = 'users/home.php'
  login_url = "login"

class newReserveStaff(LoginRequiredMixin,CreateView):
  model = Reservations
  form_class = ReservationsForm
  success_url = 'main'
  template_name = 'users/reservations_form.php'
  login_url = "login"

class deleteReservation(LoginRequiredMixin,DeleteView):
  model= Reservations
  context_object_name = 'reserve'
  success_url = 'main'
  template_name = 'users/delete_reservation.php'
  login_url = "login"

# Blogs 


class newBlog(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
  model = Blog
  form_class = BlogForms
  success_url ='/blog'
  template_name = 'new_Blog.php'
  login_url = "login"
  permission_required = ('blog.can_view')

class viewBlogs(PermissionRequiredMixin, LoginRequiredMixin, ListView):
  permission_required = 'Home.view_Blog' 
  model = Blog
  context_object_name = 'blog'
  template_name = 'blog.php'
  login_url = "login"
  

class deleteBlogs(LoginRequiredMixin, DeleteView):
  model= Blog
  success_url = '/blog'
  template_name = 'delete_blog.php'
  login_url = "login"
class updateBlogs(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
  model = Blog
  form_class = BlogForms
  success_message = 'List succcesfully edited'
  success_url = 'blog'
  template_name = 'edit_blog.php'
  login_url = "login"

class detaliBlog(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog_view.php'



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.php', context)