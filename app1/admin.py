from django.contrib import admin
from .models import Courses,Enquiry
# Register your models here.

class CourseModel(admin.ModelAdmin):
    list_display=['name','lang','price']


admin.site.register(Courses,CourseModel)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=['name','phone','date']


admin.site.register(Enquiry,EnquiryAdmin)