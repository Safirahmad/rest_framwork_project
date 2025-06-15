from rest_framework import serializers
from .models import employes

class employ_serializer(serializers.ModelSerializer):
    class meta:
        model = employes
        fields = "__all__"