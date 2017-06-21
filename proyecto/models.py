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
    donate = models.IntegerField(blank=True)

    def __unicode__(self):
        return unicode(self.usuario)
    def __str__(self): #Python 3
        return self.titulo

#VOTOS!        
import secretballot      
secretballot.enable_voting_on(Proyecto)

class Picture(models.Model):
    picture = models.ImageField(upload_to='proyecto_pictures', blank=True)
    proyecto_picture = models.ForeignKey(Proyecto, related_name='images')

    def __unicode__(self,):
        return str(self.image)

class Comment(models.Model):
    user_comment = models.ForeignKey(User)
    post_comment = models.ForeignKey(Proyecto)
    text = models.TextField(max_length=500)

    def __unicode__(self):
        return unicode(self.id)

from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the business field request. (The user could tamper
        # with those fields on payment form before send it to PayPal)
        if ipn_obj.receiver_email != "ravp92-facilitator@gmail.com":
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received etc. are all what you expect.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)
valid_ipn_received.connect(show_me_the_money)


