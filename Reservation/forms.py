from django import forms
from django.utils import timezone
from Reservation.models import Reservations, Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = {"firstname", "lastname", "contactNumber", "email"}
        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "contactNumber": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        labels = {
            "firstname": "First Name",
            "lastname": "Last Name",
            "contactNumber": "Contact Number",
            "email": "Email",
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = (
            "checkIn",
            "checkOut",
            "downpayment",
            "totalPayment",
            "balance",
            "status",
            "discounted",
        )
        widgets = {
            "checkIn": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "checkOut": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "totalPayment": forms.TextInput(attrs={"class": "form-control"}),
            "balance": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.TextInput(attrs={"class": "form-control", "value": "Yes"}),
            "downpayment": forms.TextInput(attrs={"class": "form-control"}),
            "discounted": forms.NumberInput(
                attrs={"class": "form-control", "value": "1"}
            ),
        }
        labels = {
            "checkIn": "Check In Date",
            "checkOut": "Check Out Date",
            "totalPayment": "Total",
            "downpayment": "Downpayment Required",
            "balance": "Payment Balance",
            "status": "Status",
        }

    def clean_checkIn(self):
        check_in = self.cleaned_data["checkIn"]
        if check_in < timezone.now().date():
            raise forms.ValidationError("Check in date cannot be in the past")
        return check_in
