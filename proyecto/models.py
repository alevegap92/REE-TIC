from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#cargar video
from embed_video.fields import EmbedVideoField
# Create your models here.

class proyecto(models.Model):
    usuario = models.ForeignKey(User, default=1)
    titulo = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Logos/', null=True, blank=True)
    descripcion_general = models.TextField(max_length=200, blank=True)
    descripcion_detallada =  models.TextField(max_length=1500, blank=True)
    definicion_problema =  models.TextField(max_length=1500, blank=True)
    definicion_solucion =  models.TextField(max_length=1500, blank=True)
    video = EmbedVideoField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self): #Python 3
        return self.titulo
