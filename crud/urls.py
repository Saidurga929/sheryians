from django.urls import path
from .views import *

app_name='crud'

urlpatterns=[
    path('create/',create,name='create'),
    path('read/',read,name='read'),
    path('update/',update,name='update'),
    path('delete/',delete,name='delete'),
]