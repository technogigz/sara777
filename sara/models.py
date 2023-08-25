from django.db import models

# Create your models here.
class Addapplication(models.Model):
    applink = models.CharField(max_length=500, verbose_name='App Link', null=True, blank=True)
    whatsapp = models.CharField(max_length=500, verbose_name='WhatsApp', null=True, blank=True)
    email = models.CharField(max_length=500, verbose_name='Email', null=True, blank=True)
    mobile = models.CharField(max_length=500, verbose_name='Phone', null=True, blank=True)

