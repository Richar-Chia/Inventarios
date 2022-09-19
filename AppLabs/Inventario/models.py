from pyexpat import model
from django.db import models

# Create your models here.
class Estados_Sedes(models.Model):
    id_Estado = models.AutoField(primary_key=True)
    Nomre_Estado = models.CharField(max_length=255)
    Descripcion = models.CharField(max_length=255)


class sedes(models.Model):
    Nombre_Sede = models.CharField(max_length=255)
    id_Interno = models.AutoField(primary_key=True)
    id_Estado = models.ForeignKey(Estados_Sedes, on_delete=models.CASCADE, related_name="Estados_Sedes" )
    Switch_AI = models.BooleanField()
    Observaciones = models.CharField(max_length=1000)



