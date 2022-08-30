from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=12)
    parentesco=models.CharField(max_length=20)
    dni=models.IntegerField()
    fecha_nacimiento=models.DateField()
    
    
