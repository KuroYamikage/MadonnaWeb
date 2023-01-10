from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views.generic import CreateView, TemplateView,ListView, DetailView, UpdateView

from .models import Reservations
from .models import Blog
from .forms import ReservationsForm
from .forms import BlogForms



#Blog Files
class newBlog(CreateView):
  model = Blog
  form_class = BlogForms
  success_url ='Home/blog'
  template_name = 'new_Blog.php'

class viewBlogs(ListView):
  model = Blog
  context_object_name = 'blog'
  template_name = 'blog.php'
  


#Reservation Files

class newReserve(CreateView):
  model = Reservations
  form_class = ReservationsForm
  success_url = '../sample'
  template_name = 'reservations_form.php'
class updateReserve(UpdateView):
  model = Reservations
  form_class = ReservationsForm
  success_url = '../../sample'
  template_name = 'reserve_edit.php'

class sampleView(ListView):
  model = Reservations
  context_object_name = "reserve"
  template_name='test.php'

class moreDetailView(DetailView):
  model = Reservations
  context_object_name = 'reserve'
  template_name = 'test_reserve.php'


#Home Page Views
class indexView(TemplateView):
  template_name='index.php'

class aboutView(TemplateView):
  template_name='about.php'


class reserveView(ListView):
  model = Reservations
  context_object_name = 'reserve'
  template_name='reservation.php'

class addView(TemplateView):
  template_name = "add.php"


def reservations(request):
  reserve = Reservations.objects.all().order_by('-reservationID')
  template = loader.get_template('reservation.php')
  reserve_html = []
  for instance in Reservations.objects.all():  # it's not serialization, but extracting of the useful fields
      reserve_html.append({'pk': instance.reservationID, 'fname': instance.firstname, 'lname': instance.lastname, 
      'date': instance.date, 'dp': instance.downpayment, 'total': instance.totalPayment, 'bal': instance.balance
      , 'stat': instance.status})
  reserve_dic = {'reserve': reserve, 'ac_tab_n': 'ac_tab', 'reserve_html': reserve_html}
  return render(request, 'reservation.php', reserve_dic)


def addrecord(request):
  fname = request.POST['first']
  lname = request.POST['last']
  date = request.POST['date']   
  dp = request.POST['dp']
  tp = request.POST['tp']
  bal = request.POST['bal']
  stat=request.POST['status']
  newRec = Reservations(firstname=fname, lastname=lname, date=date, downpayment=dp, totalPayment=tp, balance=bal, status=stat )
  newRec.save()
  return HttpResponseRedirect(reverse('sample'))
# Create your views here.


