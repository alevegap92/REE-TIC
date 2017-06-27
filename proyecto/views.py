from django.shortcuts import render, get_object_or_404, render_to_response
#Modelo y Formularios de proyecto
from .models import Proyecto, Picture, Choice
from django import forms
from .forms import ProyectoForm, PictureForm
#Vistas
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#from django.views.generic.detail import DetailView
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
    paginate_by = 6
    context_object_name = "proyecto_list"
    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(proyectoList2, self).get_context_data(**kwargs)
        #Agregamos un QuerySet de todos los Modelos necesarios para mostrar            
        context['paypal_list'] = PagoPaypal.objects.all()
        context['picture_list'] = Picture.objects.all()
        context['profile_list'] = Profile.objects.all()

        #total=0
        #for n in pago:
        #    total = total + n.donate
        return context

def proyectoList3(request):
    proyectos = Proyecto.objects.all().order_by('-choice__votes')
                
    return render(request, 'proyecto/proyecto_list1.html',
        {
            'proyectos': proyectos
        })
        


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
            Choice.objects.create(proyecto=post)
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


def vote(request, proyecto_id):
    p = get_object_or_404(Proyecto, id=proyecto_id)
    try:    
        selected_choice = Choice.objects.get(proyecto=p)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('proyecto/error.html', {})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('/')