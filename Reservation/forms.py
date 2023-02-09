from django import forms
from .models import Reservations


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ( 'date', 'downpayment', 'totalPayment',
            'balance', 'status')
        widgets = {
            'date' : forms.DateInput(attrs={'class': 'form-control'}),
            'totalPayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'balance' : forms.TextInput(attrs={'class' : 'form-control'}),
            'status' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
        labels = {

        }