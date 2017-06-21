from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import view_that_asks_for_money, proyectoList, proyectoUpdate, proyectoDelete, proyectoDetail, proyectoList2, upload_image_view#,proyectoCreate,

urlpatterns = [
    #url(r'^nuevo$', login_required(proyectoCreate.as_view()), name='proyecto_crear'),
    url(r'^publish/$', login_required(views.publish), name='proyecto_crear'),
    url(r'^$', proyectoList.as_view(), name='proyecto_listar'),
    url(r'^todos$', proyectoList2.as_view(), name='proyecto_listar0'),
    url(r'^(?P<pk>\d+)$', proyectoDetail.as_view(), name='proyecto_detalle'),
    url(r'^(?P<pk>\d+)/editar$', login_required(proyectoUpdate.as_view()), name='proyecto_editar'),
    url(r'^(?P<pk>\d+)/eliminar/$', login_required(proyectoDelete.as_view()), name='proyecto_eliminar'),
    url(r'^(?P<pk>\d+)/upload$', login_required(views.upload_image_view), name='upload_image_view'),
    url(r'^paypal2', include('paypal.standard.ipn.urls')),
    url(r'^paypal$', views.view_that_asks_for_money, name='donar'),
]
