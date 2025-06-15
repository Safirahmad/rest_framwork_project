from django.contrib import admin
from .models import hr
class hr_admin(admin.ModelAdmin):
    admin.site.register(hr)
# Register your models here.
