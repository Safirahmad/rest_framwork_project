from rest_framework import serializers
from .models import students  # or Student if you follow naming conventions

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
