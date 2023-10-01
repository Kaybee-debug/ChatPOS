from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
   
