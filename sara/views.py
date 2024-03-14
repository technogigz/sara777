from django.shortcuts import render
from rest_framework import decorators, permissions,  status
from rest_framework.response import Response
from .serializers import saraserializer
from rest_framework.views import APIView

from .models import Addapplication
# Create your views here.
def index(request):
    vardata = Addapplication.objects.all()
    for obj in vardata:
        return render(request, 'index.html', {'applink':obj.applink, 'whatsapp':obj.whatsapp, 'email':obj.email, 'mobile':obj.mobile})
    

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.AllowAny])
def saraserializers(request):
    content_data = Addapplication.objects.all()
    serializer = saraserializer(content_data, many=True)
    return Response({'message': 'Success!', 'result': serializer.data}, status=status.HTTP_200_OK)
     