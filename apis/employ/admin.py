from django.contrib import admin
from .models import employes
class employ_admin(admin.ModelAdmin):
    list_display=("name","email","age")
admin.site.register(employes,employ_admin)
# Register your models here.
