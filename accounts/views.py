from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmpData
from .serializers import EmpDataSerializer

# Create your views here.

@api_view(['GET'])
def Apioverview(request):
    return Response('API Calling is ready')

@api_view(['GET'])
def EmpList(request):
    emp=EmpData.objects.all()
    serializer=EmpDataSerializer(emp,many=True)
    return Response(serializer.data)