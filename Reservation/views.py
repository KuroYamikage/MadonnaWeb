from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
)
from django.contrib.auth import login, authenticate
from Reservation.models import Reservations, Customer
from Reservation.forms import ReservationForm, CustomerForm
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def test(request):
    return HttpResponse("this is a test")


class reserveView(ListView):
    model = Reservations
    context_object_name = "reserve"
    template_name = "reservation.php"


class newReserve(CreateView):
    model = Reservations
    form_class = ReservationForm
    success_url = "/reserve"
    template_name = "reservation_form_Customer.php"


class newCustomer(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = "../reservation/new"
    template_name = "customer_form_Customer.php"


class moreDetailView(DetailView):
    model = Reservations
    context_object_name = "reserve"
    template_name = "test_reserve.php"


class reserveListView(LoginRequiredMixin, ListView):
    model = Reservations
    context_object_name = "reserve"
    template_name = "users/templates/users/home.php"
    login_url = "login"


class newReserveStaff(LoginRequiredMixin, CreateView):
    model = Reservations
    form_class = ReservationForm
    success_url = "main"
    template_name = "reservations_form.php"
    login_url = "login"


class deleteReservation(LoginRequiredMixin, DeleteView):
    model = Reservations
    context_object_name = "reserve"
    success_url = "main"
    template_name = "delete_reservation.php"
    login_url = "login"


class updateReserve(LoginRequiredMixin, UpdateView):
    model = Reservations
    form_class = ReservationForm
    success_url = "/staff"
    template_name = "reserve_edit.php"
