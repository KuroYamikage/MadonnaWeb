from django import forms
from .models import Reservations, Customer


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ( 'checkIn', 'checkOut', 'downpayment', 'totalPayment',
            'balance', 'status', 'discounted', )
        widgets = {
            'checkIn' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'checkOut' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'totalPayment' : forms.TextInput(attrs={'class' : 'form-control', 'disabled': 'true'}),
            'balance' : forms.TextInput(attrs={'class' : 'form-control', 'disabled': 'true'}),
            'status' : forms.TextInput(attrs={'class' : 'form-control', 'disabled': 'true'}),
            'downpayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'discounted' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }
        labels = {
            'checkIn' : 'Check In Date',
            'checkOut' : 'Check Out Date',
            'totalPayment' : 'Total',
            'downpayment' : 'Downpayment Required',
            'balance' : 'Payment Balance',
            'status' : 'Status'
        }

class CustomerForm(forms.ModelForm):
    class meta:
        model=Customer
        fields = {
            'firstname', 'lastname', 'contactNumber', 'email'
        }
        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'comtactNumber' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'firstname' : 'First Name',
            'lastname' : 'Last Name',
            'contactNumber' : 'Contact Number',
            'email' : 'Email'
        }