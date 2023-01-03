from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)