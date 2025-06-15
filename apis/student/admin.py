from django.contrib import admin
from .models import students

class student_admin(admin.ModelAdmin):
    list_display=("name","roll_number","batch")
admin.site.register(students,student_admin)

# Register your models here.
