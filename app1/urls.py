from django.urls import path
from .views import *

app_name='app1'

urlpatterns=[
    path('',home,name='name'),
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootCamp/',bootCamp,name='bootCamp'),
    path('requestCallBack/',requestCallBack,name='requestCallBack'),
    path('signIn/',signIn,name='signIn'),
    path('email/',email,name='email'),
    path('showcourse/<int:id>',showcourse,name='showcourse')
]