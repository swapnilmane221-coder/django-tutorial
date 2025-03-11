from django.db import models
class service(models.Model):
     service_icon = models.CharField(max_length=50)
     service_title = models.CharField(max_length=50)
     service_description = models.TextField()
     
# Create your models here.
