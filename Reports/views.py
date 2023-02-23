from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class SalesReport(TemplateView):
    template_name = "reports.php"
