from test.models import Reservation, Room

from blog.forms import BlogForms
from blog.models import Blog, Gallery
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import DeleteView, FormView
from Home.forms import GalleryForm
from Reservation.forms import FacilityForm
from Reservation.models import Facility, Reservations

from .decorators import groups_required
from .forms import ResetPasswordForm, UserRegistrationForm, UserUpdateForm
from .mixins import GroupRequiredMixin

# Create your views here.


# Account Management
class StaffLoginView(LoginView):
    template_name = "accounts/auth-signin.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.groups.filter(name="Social Media Manager").exists():  # type: ignore
            return redirect("/staff/gallery")
        else:
            # redirect_authenticated_user= True
            return redirect("/staff")


class StaffLogoutView(LogoutView):
    template_name = "users/logout.php"
    login_url = "login"


@method_decorator(groups_required(["Admin", "Staff"]), name="dispatch")
class reserveListView(LoginRequiredMixin, ListView):
    model = Reservation
    context_object_name = "reserve"
    template_name = "users/home.php"
    login_url = "login"


@method_decorator(groups_required(["Admin"]), name="dispatch")
class RoomsList(LoginRequiredMixin, ListView):
    model = Room
    context_object_name = "room"
    template_name = "users/room_list.php"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_data"] = AdditionalModel.objects.all()
        return context


@method_decorator(groups_required(["Admin"]), name="dispatch")
class userList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "user1"
    template_name = "user_list.html"


@method_decorator(groups_required(["Admin"]), name="dispatch")
class registerUser(LoginRequiredMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = "register.html"
    success_url = "/accounts/"


class changepassword(PasswordChangeView, LoginRequiredMixin):
    form_class = PasswordChangeForm
    template_name = "users/user_changePass.php"
    success_url = "/staff"


@method_decorator(groups_required(["Admin"]), name="dispatch")
class editUser(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = "users/edit_user.php"
    success_url = "/accounts/"


def is_admin(user):
    return user.groups.filter(name="Admin").exists()


@method_decorator(groups_required(["Admin"]), name="dispatch")
class resetPasswordView(UserPassesTestMixin, FormView):
    template_name = "users/reset_password.php"
    form_class = ResetPasswordForm
    success_url = "/accounts/"

    def test_func(self):
        return is_admin(self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.get_user()
        return kwargs

    def get_user(self):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(User, pk=user_id)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Password changed successfully.")
        return super().form_valid(form)


# Blogs


class newBlog(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    model = Blog
    form_class = BlogForms
    success_url = "/blog"
    template_name = "new_Blog.php"
    login_url = "login"


class viewBlogs(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog.php"
    login_url = "login"


class deleteBlogs(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "blog"
    template_name = "delete_blog.php"
    login_url = "login"


class updateBlogs(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Blog
    form_class = BlogForms
    success_message = "List succcesfully edited"
    success_url = "blog"
    template_name = "edit_blog.php"
    login_url = "login"


class detaliBlog(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog_view.php"


# Home Page/Facilities
class viewFacility(LoginRequiredMixin, ListView):
    model = Facility
    context_object_name = "facility"
    template_name = "users/facility_staff.php"


class newFacility(LoginRequiredMixin, CreateView):
    model = Facility
    form_class = FacilityForm
    success_url = "/staff/facility"
    login_url = "login"
    template_name = "users/new_facility.php"


class editFacility(LoginRequiredMixin, UpdateView):
    model = Facility
    context_object_name = "facility"
    form_class = FacilityForm
    success_url = "/staff/facility"
    template_name = "users/edit_facility.php"


class addGallery(LoginRequiredMixin, CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = "users/gallery_add.php"
    login_url = "login"
    success_url = "/staff/gallery"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.galleryUploader = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class staffGallery(LoginRequiredMixin, ListView):
    model = Gallery
    context_object_name = "gallery"
    template_name = "users/gallery_staff.php"
    login_url = "login"


class detailGallery(LoginRequiredMixin, DetailView):
    model = Gallery
    context_object_name = "gallery"
    template_name = "users/gallery_detail.php"
    login_url = "login"


class editGallery(LoginRequiredMixin, UpdateView):
    model = Gallery
    form_class = GalleryForm
    context_object_name = "gallery"
    template_name = "users/gallery_edit.php"
    login_url = "login"

    def get_success_url(self):
        # Use reverse to dynamically generate the URL for the success_url
        return reverse("gallery.staff")


""" def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.php', context) """


class deleteGallery(LoginRequiredMixin, DeleteView):
    model = Gallery
    success_url = "/staff/gallery"
    template_name = "users/delete_gallery.php"
    login_url = "login"
