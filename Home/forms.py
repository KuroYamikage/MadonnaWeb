from django import forms
from .models import Reservations

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('firstname', 'lastname', 'date', 'downpayment', 'totalPayment',
            'balance', 'status')
        widgets = {
            'date' : forms.DateInput(attrs={'class': 'form-control'}),
            'firstname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'downpayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'totalPayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'balance' : forms.TextInput(attrs={'class' : 'form-control'}),
            'status' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
        labels = {
            'firstname' : 'First Name'
        }

        