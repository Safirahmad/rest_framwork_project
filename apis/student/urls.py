# student/urls.py
from django.urls import path
from .views import student_list

urlpatterns = [
    path('students/', student_list),
]
