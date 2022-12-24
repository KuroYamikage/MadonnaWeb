from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reservations

def index(request):
    template = loader.get_template('index.php')
    return HttpResponse(template.render())


def sample(request):
    reserve = Reservations.objects.all().values()
    template = loader.get_template('test.php')
    return HttpResponse(template.render())

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


