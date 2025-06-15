# student/urls.py
from django.urls import path
from .views import hr_list

urlpatterns = [
    path('hr/', hr_list),
]
