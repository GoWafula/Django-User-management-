from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request,'login/dashboard.html')


def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm

    else:
       form =CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("login")
    context = {
           'form':form
       }
    return render(request,'login/register.html',context)


