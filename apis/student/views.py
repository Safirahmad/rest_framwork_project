from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import students
from .serializers import StudentSerializer

@api_view(['GET'])
def student_list(request):
    students_data = students.objects.all()
    serializer = StudentSerializer(students_data, many=True)  # <-- This is calling the class
    return Response(serializer.data)

