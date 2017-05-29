from django.shortcuts import render
#Modelos y Formularios
from .models import Profile
from .forms import ProfileForm
#Vistas
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.

#CLASES  PARA Profile
#Class detail no se ha ocupado todavia.
class ProfileDetail(DetailView):
	model = Profile
	template_name = 'navbar3.html'

class ProfileUpdate(UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name ='proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')
