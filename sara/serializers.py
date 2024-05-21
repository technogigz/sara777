from .models import Addapplication
from rest_framework import  serializers


class saraserializer(serializers.ModelSerializer):           
    class Meta:
        model = Addapplication
        fields = ['applink','applink2','whatsapp','email','mobile']
