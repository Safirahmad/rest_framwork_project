# student/urls.py
from django.urls import path
from .views import emply_list

urlpatterns = [
    path('employ/', emply_list),
]