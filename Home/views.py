from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Reservations

def index(request):
    template = loader.get_template('index.php')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.php')
    return HttpResponse(template.render())

def reservations(request):
  reserve = Reservations.objects.all().values()
  template = loader.get_template('reservation.php')
  reserve_html = []
  for instance in Reservations.objects.all():  # it's not serialization, but extracting of the useful fields
      reserve_html.append({'pk': instance.reservationID, 'fname': instance.firstname, 'lname': instance.lastname, 
      'date': instance.date, 'dp': instance.downpayment, 'total': instance.totalPayment, 'bal': instance.balance
      , 'stat': instance.status})
  reserve_dic = {'reserve': reserve, 'ac_tab_n': 'ac_tab', 'reserve_html': reserve_html}
  return render(request, 'reservation.php', reserve_dic)

def sample(request):
    reserve = Reservations.objects.all().values()
    template = loader.get_template('test.php')
    reserve_html = []
    for instance in Reservations.objects.all():  # it's not serialization, but extracting of the useful fields
        reserve_html.append({'pk': instance.reservationID, 'fname': instance.firstname, 'lname': instance.lastname, 
        'date': instance.date, 'dp': instance.downpayment, 'total': instance.totalPayment, 'bal': instance.balance
        , 'stat': instance.status})
    reserve_dic = {'reserve': reserve, 'ac_tab_n': 'ac_tab', 'reserve_html': reserve_html}
    return render(request, 'test.php', reserve_dic)

def add(request):
  template = loader.get_template('add.php')
  return HttpResponse(template.render({}, request))

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



