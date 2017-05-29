from registration.forms import RegistrationFormUniqueEmail
from django import forms
from .models import Profile

TIPO_USUARIO = (
    ('ESTUDIANTE', 'Estudiante'),
    ('COLABORADOR', 'Colaborador'),
)

class ProfileForm(RegistrationFormUniqueEmail):
    tipo_usuario = forms.CharField(label="¿Eres un colaborador de proyectos o un estudiante?",widget=forms.Select(choices=TIPO_USUARIO))
    fist_name = forms.CharField(label="Nombre Completo")
    apellido1 = forms.CharField(label="Apelldo Paterno")
    apellido2 = forms.CharField(label="Apellido Materno")
    rut = forms.CharField(label="RUT")
    telefono = forms.CharField(label="Telefono Celular +569")
    colegio = forms.CharField(label="Colegio")
    curso = forms.IntegerField(label="Curso: primero medio es 9, segundo medio es 10, etc")
    foto = forms.ImageField(label="Foto perfil")
