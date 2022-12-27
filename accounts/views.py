from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse("Welcome to Madonna's Web: Accounts Management")