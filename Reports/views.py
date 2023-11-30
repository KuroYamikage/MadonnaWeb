from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Reports.scripts.reports import month, month_visitors, year
from .models import MonthReport
from users.decorators import groups_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)

# Create your views here.

@method_decorator(groups_required(["Admin"]), name="dispatch")
class SalesReport(TemplateView, LoginRequiredMixin):
    template_name = "reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        graph_month, total_earnings, total_reservations = month()
        graph_visitors, total_visitors = month_visitors()

        context["graph_month"] = graph_month
        context["total_earnings"] = total_earnings
        context["total_reservations"] = total_reservations
        context["graph_visitors"] = graph_visitors
        context["total_visitors"] = total_visitors

        return context

@method_decorator(groups_required(["Admin"]), name="dispatch")
def reports_month_history(request):
    months_history = MonthReport.objects.all()
    graph_year = year()
    return render(
        request,
        "months_history.html",
        {"months_history": months_history, "graph_year": graph_year},
    )
