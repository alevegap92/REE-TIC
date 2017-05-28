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
    foto= models.ImageField(upload_to = 'estudiantes',null=True,blank=True)
    tipo_usuario= models.CharField(
        max_length=10,
        choices=TIPO_USUARIO
    )
