from django.db import models
from django.conf import settings
from django.utils import timezone

from embed_video.fields import EmbedVideoField
# Create your models here.
class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion_imagen = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='media/Galeria/', null=True, blank=True)

    def __str__(self): #Python 3
        return self.titulo

class proyecto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    titulo = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/Logos/', null=True, blank=True)
    descripcion_general = models.TextField(max_length=200, blank=True)
    descripcion_detallada =  models.TextField(max_length=1500, blank=True)
    definicion_problema =  models.TextField(max_length=1500, blank=True)
    definicion_solucion =  models.TextField(max_length=1500, blank=True)
    galeria_imagenes = models.ManyToManyField(Galeria, blank=True)
    video = EmbedVideoField(blank=True)
    #publicacion = models.DateField()
	#tiempo = models.DateTimeField(auto_now_add=True, auto_now=False)
	#actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 3
        return self.titulo
