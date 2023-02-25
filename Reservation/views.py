from django.shortcuts import render
from datetime import datetime
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
from Reservation.models import Reservations, Customer, Discount, Prices
from Reservation.forms import ReservationForm, CustomerForm, PriceForm
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def test(request):
    return HttpResponse("this is a test")


class reserveView(ListView):
    model = Reservations
    context_object_name = "reserve"
    template_name = "reservation.php"


  def get_context_data(self, **kwargs):
    context = super(reserveView, self).get_context_data(**kwargs)
    context['checkIn'] = Reservations.objects.values('checkIn')
    context['checkOut'] = Reservations.objects.values('checkOut')
    """ context['venue_list'] = Venue.objects.all()
    context['festival_list'] = Festival.objects.all()
    # And so on for more models """
    return context

class newReserve(CreateView):
<<<<<<< HEAD
    model = Reservations
    form_class = ReservationForm
    success_url = "/reserve"
    template_name = "reservation_form_Customer.php"

=======
  model = Reservations
  form_class = ReservationForm
  form2 = CustomerForm
  success_url = '/reserve'
  template_name = 'reservation_form_Customer.php'
>>>>>>> master

  def get_context_data(self, **kwargs):
    context = super(newReserve, self).get_context_data(**kwargs)
    context['prices'] = Prices.objects.all().values()
    context['checkOut'] = Reservations.objects.values('checkOut')
    """ context['venue_list'] = Venue.objects.all()
    context['festival_list'] = Festival.objects.all()
    # And so on for more models """
    return context

def reserveNew(request):
  obj = Customer.objects.values()
  form = ReservationForm(request.POST or None)
  form2 = CustomerForm(request.POST or None)
  context={
    "form": form,
    "form_2":form2,
    "object":obj,   
    "prices":Prices.objects.all().values()
  }

  if all([form.is_valid(), form2.is_valid()]):
    parent=form2.save(commit=False)
    child=form.save(commit=False)
    child.customer = parent
    print(form2.cleaned_data)
    print(form.cleaned_data)
    """ form2.save()
    form.save() """
    for x in obj:
      if form2.cleaned_data['firstname'].lower() == x['firstname'].lower() and form2.cleaned_data['lastname'].lower() == x['lastname'].lower() and form2.cleaned_data['email'].lower() == x['email'].lower():
        print(x['firstname'])
        form.cleaned_data['customer_id'] = x['id']
        print(form.cleaned_data)
  return render(request, 'reservation_form_Customer.php', context)



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
<<<<<<< HEAD
    model = Reservations
    form_class = ReservationForm
    success_url = "/staff"
    template_name = "reserve_edit.php"
=======
  model = Reservations
  form_class = ReservationForm
  success_url = '/staff'
  template_name = 'reserve_edit.php'

class addPrice(LoginRequiredMixin, CreateView):
  model = Prices
  form_class = PriceForm
  success_url = '/staff/'
  template_name = 'prices_new.php'
class editPrice(LoginRequiredMixin, UpdateView):
  model = Prices
  form_class = PriceForm
  success_url = '/staff/'
  template_name = 'prices_new.php'

""" class DiscountView(ListView):
  model = Discount
  template_name = 'discount_view.php'
   """
>>>>>>> master
