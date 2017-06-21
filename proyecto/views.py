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

#Funcion para subir imagenes
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
            return HttpResponseRedirect('proyecto/upload_imagen.html')
    else:
        picture_form = PictureForm()

    return render_to_response('proyecto/upload_imagen.html', locals(), context_instance=RequestContext(request))

#PayPal
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "ravp92-facilitator@gmail.com",
        "amount": "10",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "http://127.0.0.1:8000/" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)
