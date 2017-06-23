from django.shortcuts import render
#Modelo y Formularios de proyecto
from .models import Proyecto
from django import forms
from .forms import ProyectoForm, PictureForm
#Vistas
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#Para sumar
from django.db.models import Sum
#---------------CLASES Y FUNCIONES DE MODELO PROYECTO 100%----------------------#
from pagos.models import PagoPaypal
from cuenta.models import Profile




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

#class proyectoCreate(CreateView):
#	model = Proyecto
#	form_class = ProyectoForm
#	template_name = 'proyecto/proyecto_form.html'
#	success_url = reverse_lazy('proyecto:proyecto_listar')

def publish(request):
    if request.method == 'POST':
        post_form = ProyectoForm(data=request.POST)
        picture_form = PictureForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            if 'logo' in request.FILES:
                post.logo = request.FILES['logo']
            post.usuario = request.user
            post.save()
            picture = picture_form.save(commit=False)
            if 'picture' in request.FILES:
                picture.picture = request.FILES['picture']
            picture.proyecto_picture = post
            picture.save()
            message = "Se ha creado el proyecto corretamente!"
            return HttpResponseRedirect('/')
        else:
            print (post_form.errors, post_form)
    else:
        post_form = ProyectoForm()
        picture_form = PictureForm()
    return render(request,
                  'publish.html',
                  {'post_form': post_form, 'picture_form': picture_form})


class proyectoUpdate(UpdateView):
	model = Proyecto
    #post = post_form.save(commit=False)
   # if 'logo' in request.FILES:
    #    post.logo = request.FILES['logo']
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar') 


class proyectoDelete(DeleteView):
	model = Proyecto
	template_name = 'proyecto/proyecto_delete.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')



#------------FIN CLASES Y FUNCIONES DE MODELO PROYECTO 100%----------------------#  

#Funcion para dar likes(votos) a los proyectos
def like_post(request, proyecto_id):

    id_proyecto = None
    if request.method == 'GET':
        id_proyecto = request.GET['proyecto_id']

    likes = 0
    if id_proyecto:
        post = Post.objects.get(id=int(id_proyecto))
        if post:
            likes = post.num_likes + 1
            post.num_likes = likes
            post.save()

    return HttpResponse(likes)


#Funcion para subir varias imagenes imagenes 
def upload_image_view(request):
    if request.method == 'POST':
        picture_form = PictureForm(data=request.POST)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            if 'picture' in request.FILES:
                picture.picture = request.FILES['picture']
            picture.proyecto_picture = post
            picture.save()
            message = "Se ha creado el proyecto corretamente!"
            return HttpResponseRedirect('/')
    else:
        picture_form = PictureForm()

    return render_to_response('proyecto/upload_imagen.html', locals(), context_instance=RequestContext(request))

