from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class UserRegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2','group']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
            'password1' : forms.PasswordInput( attrs={'class' : 'form-control form-control-lg'}),
            'password2' : forms.PasswordInput( attrs={'class' : 'form-control form-control-lg'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control form-control-lg'}),
            'first_name' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
            'last_name' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
        }

        labels = {
            'username' : "Username",
            'email' : "Email",
            'first_name' : "First Name",
            'last_name' : "Last Name",
            'group' : "Assign as",
        }




class UserUpdateForm(UserCreationForm):
    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()
    is_active = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2','group', 'is_active']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
            'password1' : forms.PasswordInput( attrs={'class' : 'form-control form-control-lg'}),
            'password2' : forms.PasswordInput( attrs={'class' : 'form-control form-control-lg'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control form-control-lg'}),
            'first_name' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
            'last_name' : forms.TextInput( attrs={'class' : 'form-control form-control-lg'}),
            'group' : forms.CheckboxSelectMultiple ( attrs={'class' : 'form-control form-control-lg'}),
            'is_active' : forms.RadioSelect( attrs={'class' : 'form-control form-control-lg'}),
        }

        labels = {
            'username' : "Username",
            'email' : "Email",
            'first_name' : "First Name",
            'last_name' : "Last Name",
            'group' : "Assign as",
        }
