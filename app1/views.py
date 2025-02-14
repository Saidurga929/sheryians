from django.shortcuts import render,redirect
from .models import Courses
from .forms import Enquiry,EnquiryForm

# Create your views here.
def name(request):
    return render(request,'Home.html')

def home(request):
    datas=Courses.objects.all()
    return render(request,'Home.html',{'courses':datas})

def courses(request):
    datas=Courses.objects.all()
    return render(request,'Courses.html',{'courses':datas})

def bootCamp(request):
    return render(request,'BootCamp.html')

def requestCallBack(request):
    if request.method=="POST":
        f=EnquiryForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('app1:home')
    return render(request,'RequestCallBack.html')

def signIn(request):
    return render(request,'SignIn.html')

def email(request):
    return render(request,'Email.html')

def showcourse(request,id):
    course=Courses.objects.get(id=id)
    return render(request,'showcourse.html',{'course':course})