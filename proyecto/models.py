from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#cargar video
from embed_video.fields import EmbedVideoField
# Create your models here.

class Proyecto(models.Model):
    usuario = models.ForeignKey(User, default=1)
    titulo = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos', blank=True)
    descripcion_general = models.TextField(max_length=200, blank=True)
    descripcion_detallada =  models.TextField(max_length=1500, blank=True)
    definicion_problema =  models.TextField(max_length=1500, blank=True)
    definicion_solucion =  models.TextField(max_length=1500, blank=True)
    video = EmbedVideoField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    donate = models.PositiveIntegerField(blank=True)
    donate_min = models.PositiveIntegerField(null=True,blank=True)
    num_likes= models.PositiveIntegerField(null=True,blank=True,default=0)

    def __unicode__(self):
        return unicode(self.usuario)
    def __str__(self): #Python 3
        return self.titulo
       

class Picture(models.Model):
    picture = models.ImageField(upload_to='proyecto_pictures', blank=True)
    proyecto_picture = models.ForeignKey(Proyecto, related_name='images', on_delete=models.CASCADE)

    def __unicode__(self,):
        return str(self.image)

class Comment(models.Model):
    user_comment = models.ForeignKey(User)
    post_comment = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

    def __unicode__(self):
        return unicode(self.id)

class Choice(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.id)

