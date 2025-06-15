from rest_framework.response import Response
from .serializer import hr_serializer
from .models import hr
from rest_framework.decorators import api_view

@api_view(['GET'])

def hr_list(request):
    hr_data = hr.objects.all()
    hr_serializers = hr_serializer(hr_data, many=True)
    return Response(hr_serializers.data)
# Create your views here.
