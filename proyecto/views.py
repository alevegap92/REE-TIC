from django.shortcuts import render
#Modelo proyecto
from proyecto.models import Proyecto
from proyecto.forms import ProyectoForm
#Vistas
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.

#CLASES DE PROYECTO

class proyectoDetail(DetailView):
	model = Proyecto
	template_name = 'proyecto/proyecto_detalle.html'

class proyectoList(ListView):
	model = Proyecto
	template_name = 'proyecto/proyecto_list.html'
	paginate_by = 4

class proyectoList2(ListView):
	model = Proyecto
	template_name = 'proyecto/proyecto_list0.html'
	paginate_by = 12

class proyectoCreate(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class proyectoUpdate(UpdateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class proyectoDelete(DeleteView):
	model = Proyecto
	template_name = 'proyecto/proyecto_delete.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')
