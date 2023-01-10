from django import forms
from .models import Reservations
from .models import Blog

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

class BlogForms(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class' : 'form-control'}),
            'blog_content':forms.Textarea(attrs={'class' : 'form-control'})
        }
        labels = {
            'blog_title':'title',
            'blog_content':'content'
        }