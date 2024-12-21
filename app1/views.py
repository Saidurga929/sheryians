from django.shortcuts import render

# Create your views here.
def name(request):
    return render(request,'Home.html')

def home(request):
    return render(request,'Home.html')

def courses(request):
    return render(request,'Courses.html')

def bootCamp(request):
    return render(request,'BootCamp.html')

def requestCallBack(request):
    return render(request,'RequestCallBack.html')

def signIn(request):
    return render(request,'SignIn.html')

def email(request):
    return render(request,'Email.html')