from django import forms
from django.utils import timezone
from Reservation.models import Reservations, Customer, Facility, Prices


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
    model = Reservations
    class Meta:
        model = Reservations
        fields = (
            "checkIn",
            "checkOut",
            "downpayment",
            "totalPayment",
            "balance",
            'prices',
            'facility'
        )
        widgets = {
            'checkIn' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'checkOut' : forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'totalPayment' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'True',}),
            'balance' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'True'}),
            'downpayment' : forms.TextInput(attrs={'class' : 'form-control', 'readonly':'True',}),
            'facility' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control'})
        }

        labels = {
            "checkIn": "Check In Date",
            "checkOut": "Check Out Date",
            "totalPayment": "Total",
            "downpayment": "Downpayment Required",
            "balance": "Payment Balance",
            'facility': 'Additional Facilities'
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
        fields = ( 'facilityName', 'facilityDescription', 'facilityPic', 'facilityPrice','facilityCategory', 'facilitymax')
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

class PriceForm(forms.ModelForm):
    model = Prices
    class Meta:
        model = Prices
        dayTimeChoices = (
            ('day','Day'),
            ('night','Night'),
            ('whole','Whole Day')
        )

        maxPaxChoices = (
            (30, '30 pax'),
            (50, '50 pax'),
            (100, '100 pax'),
            (150, '150 pax')
        )
        fields = ('price', 'maxPax', 'dayTime')
        widgets = {

            'price' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'maxPax': forms.RadioSelect(choices=maxPaxChoices, attrs={'class' : 'form-control'}),
            'dayTime': forms.RadioSelect(choices=dayTimeChoices, attrs={'class' : 'form-control'})
        }

        label = {
            'price': 'Price',
            'dayTime' : 'Schedule',
            'maxPax' : 'Maximum Guest'
        }
  