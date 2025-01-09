from django.shortcuts import render,redirect
from .models import Users
from .forms import UsersForm

# Create your views here.
def create(request):
    if request.method=="POST":
        f=UsersForm(request.POST)
        if f.is_valid():
            f.save()
    return redirect('app1:requestCallBack',{'form':UsersForm()})

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass