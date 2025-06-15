from rest_framework.response import Response  # ✅ correct import
from .models import employes
from .serializers import employ_serializer     # ✅ make sure this is the class
from rest_framework.decorators import api_view

@api_view(['GET'])
def emply_list(request):
    employ_all = employes.objects.all()
    serializer = employ_serializer(employ_all, many=True)
    return Response(serializer.data)          # ✅ use capital-R Response


# Create your views here.
