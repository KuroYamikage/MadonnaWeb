from django import forms
from django.utils import timezone
from Reservation.models import Reservations, Customer, Facility


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
            'checkIn' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'checkOut' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'totalPayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'balance' : forms.TextInput(attrs={'class' : 'form-control'}),
            'status' : forms.TextInput(attrs={'class' : 'form-control',  'value' : 'Yes'}),
            'downpayment' : forms.TextInput(attrs={'class' : 'form-control'}),
            'discounted' : forms.NumberInput(attrs={'class' : 'form-control', 'value' : '1'}),

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


class FacilityForm(forms.ModelForm):
    model = Facility
    class Meta:
        model = Facility
        FacilityCategoriesChoices = (
            ('pool','Pool'),
            ('rooms','Rooms'),
            ('cottages','Cottages'),
            ('EH','Event Hall'),
     
  )
        fields = ( 'facilityName', 'facilityDescription', 'facilityPic', 'facilityPrice','facilityCategory', 'facilitymax' )
        widgets = {
            'facilityName' : forms.TextInput(attrs={'class': 'form-control'}),
            'facilityDescription' : forms.Textarea(attrs={'class': 'form-control'}),
            
            'facilityPrice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'facilitymax' : forms.NumberInput(attrs={'class': 'form-control'}),
            
            'facilityCategory': forms.RadioSelect(choices=FacilityCategoriesChoices),
        }
        labels = {
            'facilityName' : 'Facility Name',
            'facilityDescription' : 'Facility Description',
            'facilityPic' : 'Facility Pic',
            'facilityPrice' : 'Facility Price',
            'facilitymax' : 'Facility Maximum Occupancy',
            'facilityCategory' : 'Category'
            
        }