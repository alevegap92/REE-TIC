from django.db import models
from django.contrib.auth.models import User
# Create your models here.
TIPO_USUARIO = (
    ('ESTUDIANTE', 'Estudiante'),
    ('COLABORADOR', 'Colaborador'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=100, blank=True)
    apellido1 = models.CharField(max_length=80, blank=True)
    apellido2 = models.CharField(max_length=80, blank=True)
    rut = models.CharField(max_length=9, blank=True)
    telefono = models.CharField(max_length=8, blank=True)
    colegio = models.CharField(max_length=200, blank=True)
    curso = models.IntegerField(blank=True)
    tipo_usuario= models.CharField(
        max_length=10,
        choices=TIPO_USUARIO
    )

    def __unicode__(self):
        return "{0}".format(self.user.username)
    def __str__(self): #Python 3
        return self.user.username
    def get_profile2(self):
        return self.user.profile.id
    def get_profile(self):
        return self.user.id
    def get_nombre(self):
        return self.fist_name
