from django.db import models
class query(models.Model):
     name=models.CharField(max_length=50) 
     email=models.EmailField()
     username=models.CharField(max_length=50)
     password=models.CharField(max_length=50)        
# Create your models here.
class msg(models.Model):
     message=models.TextField()