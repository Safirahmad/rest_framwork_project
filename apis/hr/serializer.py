from rest_framework import serializers
from .models import hr

class hr_serializer(serializers.ModelSerializer):
    class Meta:
        model = hr
        fields = '__all__'
        