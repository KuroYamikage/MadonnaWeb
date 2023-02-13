from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.generic import CreateView, TemplateView,ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from blog.models import Blog
from blog.forms import BlogForms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, authenticate

# Create your views here.
#Blogs

class detaliBlog(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog_view.php'

class blogCustomer(ListView):
  model = Blog
  context_object_name = 'blog'
  template_name = 'blog_Customer.php'

class newBlog(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
  model = Blog
  form_class = BlogForms
  success_url ='/staff/blog'
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
  success_url = '/staff/blog'
  template_name = 'delete_blog.php'
  login_url = "login"
class updateBlogs(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
  model = Blog
  form_class = BlogForms
  success_message = 'List succcesfully edited'
  success_url = '/staff/blog'
  template_name = 'edit_blog.php'
  login_url = "login"


