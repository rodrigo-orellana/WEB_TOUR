# visitas_granada/model.py

from django.db import models

class Visita(models.Model):
	nombre      = models.CharField(max_length=100)
	descripción = models.CharField(max_length=1000)
	likes       = models.IntegerField(default=0)
	foto        = models.FileField(upload_to='fotos', blank=True)

class Comentario(models.Model):
	visita      = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto       = models.CharField(max_length=500)
