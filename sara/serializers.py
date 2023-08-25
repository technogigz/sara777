from .models import Addapplication
from rest_framework import  serializers


class saraserializer(serializers.ModelSerializer):           
    class Meta:
        model = Addapplication
        fields = ['applink','whatsapp','email','mobile']