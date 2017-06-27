from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [
    url(r'^publish/$', views.publish, name='proyecto_crear'),
    #url(r'^$', proyectoList.as_view(), name='proyecto_listar'),
    url(r'^$', views.proyectoList3, name='proyecto_listar'),
    url(r'^(?P<pk>\d+)$', proyectoDetail.as_view(), name='proyecto_detalle'),
    url(r'^todito/$', proyectoList2.as_view(
      model=Proyecto,
      template_name = 'proyecto/proyecto_list0.html',
      context_object_name="proyecto_list",), 
      name='proyecto_listar0'),

    url(r'^(?P<pk>\d+)/editar$', login_required(proyectoUpdate.as_view()), name='proyecto_editar'),
    url(r'^(?P<pk>\d+)/eliminar/$', login_required(proyectoDelete.as_view()), name='proyecto_eliminar'),
    url(r'^(?P<pk>\d+)/upload$', login_required(views.upload_image_view), name='upload_image_view'),
    url(r'^vota/(?P<proyecto_id>[\w\-]+)/$', views.vote, name='vote'),
   #url(r'^(?P<pk>\d+)/like_post$', login_required(views.like_post), name='like_post'),
   # url(r'^paypal2', include('paypal.standard.ipn.urls')),
   # url(r'^paypal$', views.view_that_asks_for_money, name='donar'),
   # url(r'^paypal3$', views.money_request, name='donar'),
   # url(r'^confirm$', views.confirm)
]
