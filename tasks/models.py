from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    direcction = models.CharField(max_length=75)
    department = models.CharField(max_length=100)
    color = models.CharField(max_length=75)
    
    
    
